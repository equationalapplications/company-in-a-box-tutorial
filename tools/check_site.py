#!/usr/bin/env python3
"""check_site.py — the site checker for company-in-a-box-tutorial.

Implements the spec's test plan (specs/company-in-a-box-tutorial/spec.md):
  1. HTML validity (html5lib strict) + structural checks — manifest pages only
  2. Link check (urllib, real UA, retries; 404/DNS=FAIL, 410=FAIL-after-retry,
     429/5xx/403/401/timeout=WARNING escalating after 3 consecutive runs)
  3. Design-law checks: <=5 total top-level <ol> <li> steps per non-landing
     page; SVG presence where the page map promises one; data-topic manifest
  4. Analytics: zero <script> per page, or exactly one real GoatCounter tag
     (placeholder code always fails); non-manifest root HTML: no scripts
  5. Redaction grep (paths) + optional gitleaks
Footer: byte-identical across the manifest AND contains the EA link + MIT.

Exit codes: 0 = pass (or "site not ready" skip), 1 = failures found.
"""
from __future__ import annotations

import json
import os
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
STATE_FILE = Path(__file__).resolve().parent / ".link-state.json"

# Page map: file -> data-topic number. Row 1 (index) is exempt from the
# step counter; row 13 (links) is exempt from the SVG-presence check.
MANIFEST = {
    "index.html": "1",
    "the-pattern.html": "2",
    "the-three-tools.html": "3",
    "setup-hermes.html": "4",
    "setup-memory.html": "5",
    "connect-memory.html": "6",
    "first-integration.html": "7",
    "procedures.html": "8",
    "delegate.html": "9",
    "schedule.html": "10",
    "delivery-flow.html": "11",
    "team-memory.html": "12",
    "links.html": "13",
}
SVG_EXEMPT = {"links.html"}
STEPS_EXEMPT = {"index.html"}
STEP_LIMIT = 5

EA_LINK = "https://equationalapplications.com"
MIT_MARK = "MIT"
GC_RE = re.compile(
    r'<script[^>]+data-goatcounter="https://[A-Za-z0-9-]+\.goatcounter\.com/count"[^>]*>'
)
GC_PLACEHOLDER_RE = re.compile(r"data-goatcounter=\"[^\"]*(YOURCODE|placeholder|example)[^\"]*\"", re.I)
SCRIPT_RE = re.compile(r"<script\b", re.I)
ON_HANDLER_RE = re.compile(r"\son[a-z]+\s*=\s*[\"']", re.I)

REDACTION_PATTERNS = [
    (re.compile(r"/home/", re.I), "vault path fragment: /home/"),
    (re.compile(r"~/(?!\.)"), "vault path fragment: ~/<non-dotfile>"),
    (re.compile(r"immutable-source-files", re.I), "vault tree: immutable-source-files"),
    (re.compile(r"documents/equational-wiki", re.I), "vault tree: documents/equational-wiki"),
]
TOKEN_PATTERNS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key id"),
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "API key (sk-…)"),
]

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
WARN_ESCALATE_AFTER = 3

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_html5lib():
    try:
        import html5lib  # noqa: F401
        return html5lib
    except ImportError:
        return None


def parse_strict(html5lib, text: str):
    """Parse via the documented tree-in-constructor pattern (passing
    treebuilder= to parse() misroutes the kwarg into the input stream),
    collecting the parser's spec-error list."""
    treebuilder = html5lib.getTreeBuilder("etree")
    parser = html5lib.HTMLParser(tree=treebuilder)
    root = parser.parse(text)
    return root, getattr(parser, "errors", [])


def walk_top_level_ol_li(root) -> int:
    """Count <li> children of top-level-in-body <ol> elements (not nested
    inside another <ol>). Lists nested inside <ul> ARE counted (a deliberate
    choice: <ul> is not a step list, so an <ol> under it starts a new step
    sequence). Namespace-agnostic (html5lib namespaced, plain ET in tests)."""
    count = 0
    body = None
    for el in root.iter():
        if el.tag.rsplit("}", 1)[-1].lower() == "body":
            body = el
            break
    if body is None:
        return count
    stack = list(body)
    while stack:
        el = stack.pop(0)
        tag = el.tag.rsplit("}", 1)[-1].lower()
        if tag == "ol":
            count += len([c for c in el if c.tag.rsplit("}", 1)[-1].lower() == "li"])
            continue  # do not descend: nested lists don't count
        stack.extend(el)
    return count


def get_text(el) -> str:
    return "".join(el.itertext())


def check_page(html5lib, path: Path, topic: str) -> str | None:
    """Returns the page's raw text (for cross-page checks); records failures."""
    raw = path.read_text(encoding="utf-8")

    # Strict parse
    try:
        root, parse_errors = parse_strict(html5lib, raw)
    except Exception as exc:  # catastrophic parse failure
        fail(f"{path.name}: strict parse error: {exc}")
        return None
    if parse_errors:
        sample = "; ".join(f"{pos}: {msg}" for pos, msg in parse_errors[:3])
        fail(f"{path.name}: {len(parse_errors)} markup error(s) — {sample}")
        return None

    def findall(tag):
        return root.findall(f".//{tag}") + root.findall(f".//{{*}}{tag}")

    # Structural: single h1, title, viewport meta
    h1s = findall("h1")
    if len(h1s) != 1:
        fail(f"{path.name}: expected exactly 1 <h1>, found {len(h1s)}")
    titles = findall("title")
    if len(titles) != 1 or not get_text(titles[0]).strip():
        fail(f"{path.name}: missing or empty <title>")
    metas = [m for m in findall("meta") if "viewport" in (m.get("name") or "")]
    if not metas:
        fail(f"{path.name}: missing viewport <meta>")

    # data-topic manifest (root <html> or <body>; .// misses the root)
    found_topic = root.get("data-topic")
    if not found_topic:
        body = root.find(".//{http://www.w3.org/1999/xhtml}body")
        if body is not None and body.get("data-topic"):
            found_topic = body.get("data-topic")
    if found_topic != topic:
        fail(f"{path.name}: data-topic is {found_topic!r}, expected {topic!r}")

    # SVG presence (all manifest pages promise one except links.html)
    if path.name not in SVG_EXEMPT and not findall("svg"):
        fail(f"{path.name}: no inline <svg> infographic found")

    # Step counter (total top-level <ol><li> per page; landing exempt)
    if path.name not in STEPS_EXEMPT:
        steps = walk_top_level_ol_li(root)
        if steps > STEP_LIMIT:
            fail(f"{path.name}: {steps} top-level <ol> steps (limit {STEP_LIMIT})")

    # Scripts: zero, or exactly one real GoatCounter tag; no inline handlers
    scripts = SCRIPT_RE.findall(raw)
    if ON_HANDLER_RE.search(raw):
        fail(f"{path.name}: inline event handler (on*=) found — no JS allowed")
    if scripts:
        if len(scripts) != 1:
            fail(f"{path.name}: {len(scripts)} <script> tags (max 1: GoatCounter)")
        elif GC_PLACEHOLDER_RE.search(raw):
            fail(f"{path.name}: placeholder GoatCounter code must never ship")
        elif not GC_RE.search(raw):
            fail(f"{path.name}: the single <script> is not a valid GoatCounter tag")

    # Internal href resolution (file AND anchor)
    for a in findall("a"):
        href = a.get("href") or ""
        if href.startswith(("http://", "https://", "mailto:", "#")) or not href:
            continue
        file_part, _, anchor = href.partition("#")
        if file_part and not (SITE / file_part).exists():
            fail(f"{path.name}: internal href '{href}' does not resolve")
        elif anchor and file_part:
            target_raw = (SITE / file_part).read_text(encoding="utf-8")
            if f'id="{anchor}"' not in target_raw:
                fail(f"{path.name}: internal href '{href}' anchor missing in "
                     f"{file_part}")
        elif anchor:
            if f'id="{anchor}"' not in raw:
                fail(f"{path.name}: anchor '#{anchor}' missing on this page")

    # Redaction grep
    for pattern, label in REDACTION_PATTERNS:
        if pattern.search(raw):
            fail(f"{path.name}: REDACTION hit — {label}")
    for pattern, label in TOKEN_PATTERNS:
        if pattern.search(raw):
            fail(f"{path.name}: possible secret — {label}")

    return raw


def footer_of(raw: str) -> str:
    m = re.search(r"<footer\b.*?</footer>", raw, re.S | re.I)
    return m.group(0) if m else ""


def check_external(url: str) -> str:
    """Returns 'OK', 'WARN', or 'FAIL'.
    404 = FAIL immediately; DNS resolution failure = FAIL after one retry;
    410 = FAIL after one retry; other HTTP errors (429/5xx/403/401) and
    timeouts/connection errors = WARN (escalation handled by the caller)."""
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status < 400:
                    return "OK"
                code = resp.status
        except urllib.error.HTTPError as exc:
            code = exc.code
        except urllib.error.URLError as exc:
            if isinstance(getattr(exc, "reason", None), socket.gaierror):
                # DNS resolution failure — hard after one retry
                if attempt == 0:
                    continue
                return "FAIL"
            return "WARN"
        except (TimeoutError, ConnectionError, OSError):
            return "WARN"
        if code == 404:
            return "FAIL"
        if code == 410 and attempt == 0:
            continue
        if code == 410:
            return "FAIL"
        return "WARN"
    return "WARN"


def load_state() -> dict:
    try:
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        pass  # corrupt state = start fresh; escalation just needs to rebuild
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=1, sort_keys=True))


def main() -> int:
    args = sys.argv[1:]
    check_external_links = "--check-external" in args

    html5lib = load_html5lib()
    if html5lib is None:
        print("FAIL: html5lib is required (pip install -r tools/requirements-dev.txt)")
        return 1

    missing = [f for f in MANIFEST if not (SITE / f).exists()]
    if missing:
        allow_empty = "--allow-empty-site" in sys.argv
        if allow_empty and len(missing) == len(MANIFEST):
            print("SKIP: --allow-empty-site set and no manifest files exist.")
            return 0
        fail(f"manifest files missing from site/ (deleted or never built): "
             f"{', '.join(sorted(missing))}")

    raws: dict[str, str] = {}
    for fname, topic in MANIFEST.items():
        if fname in missing:
            continue  # already reported; opening it would crash
        raw = check_page(html5lib, SITE / fname, topic)
        if raw is not None:
            raws[fname] = raw

    # Footer: present, byte-identical across manifest, AND content-bearing
    footers = {f: footer_of(r) for f, r in raws.items()}
    absent = [f for f, ft in footers.items() if not ft]
    if absent:
        fail(f"pages missing a <footer> block: {', '.join(sorted(absent))}")
    distinct = set(footers.values())
    if len(distinct - {""}) != 1:
        fail(f"footer blocks are not byte-identical across manifest pages "
             f"({len(distinct - {''})} distinct)")
    footer_sample = next((ft for ft in footers.values() if ft), "")
    if footer_sample:
        if EA_LINK not in footer_sample:
            fail("footer is missing the EA link")
        if MIT_MARK not in footer_sample:
            fail("footer is missing the MIT statement")

    # Non-manifest root HTML files: no scripts
    manifest_set = set(MANIFEST)
    for extra in SITE.glob("*.html"):
        if extra.name in manifest_set:
            continue
        if SCRIPT_RE.search(extra.read_text(encoding="utf-8")):
            fail(f"{extra.name}: non-manifest HTML must contain no <script>")

    # Redaction grep + token patterns over ALL of site/ (manifest pages were
    # already scanned individually — skip them here to avoid double reports)
    manifest_paths = {(SITE / f).resolve() for f in MANIFEST}
    for f in SITE.rglob("*"):
        if f.is_file() and f.resolve() not in manifest_paths \
                and f.suffix in {".html", ".css", ".js", ".svg", ".txt"}:
            text = f.read_text(encoding="utf-8", errors="replace")
            for pattern, label in REDACTION_PATTERNS:
                if pattern.search(text):
                    fail(f"{f.relative_to(REPO)}: REDACTION hit — {label}")
            for pattern, label in TOKEN_PATTERNS:
                if pattern.search(text):
                    fail(f"{f.relative_to(REPO)}: possible secret — {label}")

    # Optional gitleaks (mandatory in CI — spec: "any hit fails the check").
    # gitleaks exits 1 when it finds leaks, so ANY non-zero exit fails here.
    import os
    import shutil
    gitleaks = shutil.which("gitleaks")
    if gitleaks:
        import subprocess
        # No report flags: default stdout output is stable across versions
        # (report formats changed between 8.28 and 8.30). gitleaks exits 1
        # when it finds leaks, so ANY non-zero exit fails here.
        proc = subprocess.run(
            [gitleaks, "git", "--no-banner", "--redact"],
            cwd=REPO, capture_output=True, text=True)
        if proc.returncode != 0:
            fail(f"gitleaks findings (exit {proc.returncode}):\n"
                 f"{proc.stdout}\n{proc.stderr}")
    elif os.environ.get("GITHUB_ACTIONS") == "true":
        fail("gitleaks binary not found in CI — the secret gate is mandatory")

    # External links
    if check_external_links:
        state = load_state()
        warn_counts = state.setdefault("warn_streak", {})
        # Spec test 2: the streak advances on SCHEDULED runs only — a
        # transient 429 across three PR pushes must not fail the PR.
        advance_streak = os.environ.get("GITHUB_EVENT_NAME", "") == "schedule"
        urls = set()
        for raw in raws.values():
            urls.update(re.findall(r'href="(https?://[^"]+)"', raw))
        for url in sorted(urls):
            result = check_external(url)
            if result == "OK":
                if advance_streak:
                    warn_counts.pop(url, None)
            elif result == "FAIL":
                fail(f"external link hard failure (404/DNS): {url}")
                warn_counts.pop(url, None)
            else:
                if advance_streak:
                    warn_counts[url] = warn_counts.get(url, 0) + 1
                    if warn_counts[url] >= WARN_ESCALATE_AFTER:
                        fail(f"external link warned {warn_counts[url]} consecutive "
                             f"scheduled runs, escalating: {url}")
                        continue
                warn(f"external link warning: {url}")
        if advance_streak:
            save_state(state)

    # Report
    for w in warnings:
        print(f"WARNING: {w}")
    for f in failures:
        print(f"FAIL: {f}")
    if failures:
        print(f"\ncheck_site: {len(failures)} failure(s), {len(warnings)} warning(s)")
        return 1
    print(f"check_site: PASS ({len(MANIFEST)} manifest pages, "
          f"{len(warnings)} warning(s), external={'yes' if check_external_links else 'no'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
