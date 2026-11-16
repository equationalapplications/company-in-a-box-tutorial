# Spec — first-integration page: teach each install step in detail

Status: In Tier-3 review (2026-11-16) — round-5 delta returned PASS WITH
MINORS; its five minors folded in this commit, closing delta round pending.

Verification record (2026-11-16): implemented and independently reviewed
(non-author reviewer PASS, deleg_268748ad); unit tests 24/24 OK
(`/usr/bin/python3 tools/test_check_site.py`); full checker PASS offline
and with `--check-external` (13 manifest pages, 0 warnings); visual render
checked in a real browser at desktop width (screenshots inspected);
gitleaks clean. Gates on `cdb6a3c` (round-2 fold): tests OK, checker PASS
offline + external, re-run after the commit. Gates on this fold: re-run
before the round-4 delta. Round map: r1 findings → `5e2cf5e`; r2 delta →
`cdb6a3c`; r3 delta → `12c2e3c`; r4 delta → this commit.
Date: 2026-11-15
Owner: Tessera

Known trade-offs (adjudicated, not defects): step-2 density (r3-m1
partial, r4-m6 rejected-with-cite — the reviewer marked it "not
required"; the mirrored nested bullets survived two review rounds and a
5th top-level step would trade INTENT's small-bites ruling against its
few-steps rule). r3-m3 note: the page flags `env:` differences but not
the `HERMES_CT_SIDECAR` command difference — r4-m3 fixed by adding
"(command: line may differ)" to the page.

## Problem

The heart of the tutorial, step 4 (`site/first-integration.html`), compresses
the entire integration install into three vague instructions: "grab the
latest hermes-v… release", "install it and run its doctor script", "restart
Hermes". None of these tells a new user what to actually do: what to click,
what a `.tar.gz` is, what command to run, what folder things land in, what
success looks like, or what to do when a line says WARN. Kurt calls this page
"the very heart of the tutorial" and asked for step-by-step detail with
context and helpful hints for an inexperienced user.

Evidence:

- The current page carries the three compressed items (read from the live
  site and from `site/first-integration.html` at commit 8dbc5f7).
- The real install procedure is concrete and verifiable. Verified
  2026-11-15 against the real release and real scripts:
  - Latest Hermes integration release: `hermes-v0.7.2`
    (`gh release list -R equationalapplications/curated-thoughts-integrations`).
    Its asset is `hermes-0.7.2.tar.gz`, and it extracts to a `hermes-0.7.2/`
    folder containing `plugin.yaml` and `scripts/install.sh` (verified by
    downloading and listing the real tarball).
  - `scripts/install.sh` is idempotent, needs no sudo, and never deletes
    user files. It copies the plugin into `~/.hermes/plugins/curated-thoughts/`,
    prints the MCP registration block and the `plugins.enabled` block it
    wants (writing config itself only when the config file is absent or has
    no `mcp_servers` section and `CT_INSTALL_EDIT=1` was set), and ends by
    telling the user to run the doctor (read from `install.sh` in
    `curated-thoughts-integrations`).
  - The doctor is run with
    `python3 ~/.hermes/plugins/curated-thoughts/scripts/ct_doctor.py check`.
    It prints one PASS/WARN/FAIL line per layer — sidecar, brain, vault,
    registration, import pre-flight, version compat — each WARN/FAIL with a
    `fix:` hint, and a final tally. Exit codes: 0 = all PASS, 1 = any FAIL,
    2 = no FAIL but at least one WARN. Verified by running it on EA's real
    machine: `0 FAIL, 1 WARN, 9 PASS — exit 2`.
  - Live fact delivery requires Curated Thoughts ≥ 3.3.0 (sidecar `ct wisdom
    match`); with an older sidecar it is a silent no-op (integrations
    README).
- Step 3's aside invites readers to skip the hand-edit and "skip ahead to
  step 4 and let the integration wire it" — so this page must work for
  readers with no `mcp_servers` entry yet, not only readers who did step 3.

## Proposed change

Rebuild the numbered steps on `site/first-integration.html` into four
fully taught steps (the original three, with the installer and doctor
split after Tier-3 review). Each step gets: one or two sentences of context (what
this step does and why), the exact commands in `pre`/`code` blocks, a
"What you should see" line describing real output shape, and a short hint
for the most likely hiccup. Nothing else on the page changes: the lead, the
layers paragraph, the SVG figure, the other-harnesses aside, the next-page
links, and the footer stay as they are.

Concrete content per step (every command below was verified against the real
release tarball and a real doctor run on 2026-11-15):

1. **Download and unpack the release.**
   - Context: a release is a packaged snapshot of the plugin; the Hermes
     one is a `.tar.gz` (tarball = a zipped folder).
   - Follow the releases link; pick the newest release whose tag starts with
     `hermes-v`; download its `hermes-<version>.tar.gz` asset.
   - Hint: the version number will be higher by the time you read this —
     that is fine; the newest `hermes-v…` is always the right pick. Releases
     for other harnesses (deepseek-v…, opencode-v…) sit next to it; do not
     grab those.
   - Unpack with `tar xzf hermes-0.7.2.tar.gz` (example version; use the
     name you downloaded). You get a `hermes-0.7.2/` folder.
2. **Run the installer.**
   - `bash hermes-0.7.2/scripts/install.sh` — copies the plugin (an
     add-on Hermes loads) into `~/.hermes/plugins/curated-thoughts/`,
     safe to run again any time, no administrator rights needed.
   - If the installer prints a config block, follow its own placement
     message and match it to what the reader's file shows. `install.sh`
     prints two blocks, each with two cases (verified in the script,
     2026-11-16): an `mcp_servers` block ("No 'mcp_servers:' section
     found" → paste the whole block at the top level, exactly as printed
     — usually the case for readers who skipped step 3's hand-edit;
     section exists without the `curated-thoughts` key → copy every
     printed line except the repeated `mcp_servers:` header, shifted so
     `curated-thoughts:` sits one indent level under the existing
     `mcp_servers:` line) and a `plugins` block ("No 'plugins:' section
     found" → whole block at the top level; section exists without the
     entry → add `- curated-thoughts` under `enabled:`, creating
     `enabled:` if needed).
   - CRITICAL (Tier-3 r2, 2026-11-16, verified in the script): in the
     section-exists branch the installer's printed `mcp_servers` copy
     still carries its own `mcp_servers:` header line, pre-indented —
     pasting it whole nests the section inside itself and corrupts the
     config. The page must teach copying every printed line except that
     header, shifted so `curated-thoughts:` sits one indent level under
     the existing `mcp_servers:` line, with a target-shape snippet
     presented as an example. The printed block can also include `env:`
     lines (non-default brain location, external embedder) and the
     command honors `HERMES_CT_SIDECAR` (Tier-3 r3, 2026-11-16, verified
     in the script) — the snippet may show the no-env default but must
     say so, and must tell readers to keep their existing entries. YAML
     placement is the classic beginner trap here (Gemini review note,
     2026-11-16). The installer never overwrites an existing entry.
   - Dormancy consequence (installer's own words): without the `plugins`
     entry the tools work but the skills and session-start hook stay
     dormant — that is step 4's "nothing shows up" symptom.
   - What you should see: near the end, under `== Plugin enablement ==`,
     either an `OK:` line or a config block to paste; the run finishes
     with `== Done ==`.
   - Env nuance (Tier-3 r5, verified in `ct_env.py` `sidecar_env_needs`):
     live `env:` lines can come from a non-default brain location *or* a
     detected external embedder (`EMBED_API_KEY` first, else OpenRouter/
     OpenAI default); the commented block is only a fallback hint.
3. **Run the doctor.**
   - `python3 ~/.hermes/plugins/curated-thoughts/scripts/ct_doctor.py check`.
   - Plain-language definitions at first use: sidecar, brain, vault,
     registration — the four things the doctor checks, in ordinary words.
   - What you should see: a line per check (plus import pre-flight and
     version compatibility), most saying PASS, then a tally.
     `0 FAIL` is the goal. WARN means it works but a feature is degraded —
     the line's `fix:` hint says exactly what to do. FAIL means stop and fix
     what the line says, then re-run.
4. **Restart Hermes and watch memory show up on its own.**
   - Quit and reopen Hermes so it loads the plugin.
   - The live signs, as today: a short recall of relevant procedures and
     facts at session start, and relevant facts appearing as you talk.
   - New troubleshooting hint: if nothing shows up, re-run the doctor, make
     sure `plugins.enabled` lists `curated-thoughts`, and make sure Curated
     Thoughts is version 3.3.0 or newer.

### Constraints honored

- Step-count law: the page keeps 4 top-level `li` steps (checker hard
  limit is 5; nested lists do not count). Originally specced as exactly 3;
  Tier-3 review (2026-11-16) showed step 2 carried two actions and ~30
  lines against INTENT's small-bites ruling, so it was split into an
  installer step and a doctor step. Sub-details ride inside the steps as
  prose, `pre` blocks, and nested lists.
- No new scripts, no new external links (the releases link already exists).
- Sample output shown on the page must use generic paths (`~`, no real home
  directory names) to pass the checker's redaction grep.
- The example version `0.7.2` is marked as an example in the prose so the
  page does not rot when v0.7.3 ships.

## Files touched

- `site/first-integration.html` — the `ol.steps` list items (4 after the
  Tier-3 split) and their nested detail. No other element changes.

## Test plan

1. `python3 tools/test_check_site.py` — unit tests pass.
2. `python3 tools/check_site.py` — full checker passes (HTML validity,
   ≤5-step law, link check, redaction grep, footer byte-identity).
3. Visual check in a browser at desktop width: page stays airy, commands
   read as clearly as step 3's config block.
4. Ground truth re-verification: the commands on the page were executed or
   read from the real release asset and real scripts (evidence captured
   2026-11-15, recorded above); no command appears on the page that was not
   verified.

## Alignment with INTENT.md

- **Small bites:** still one topic, now 4 numbered steps (inside the ≤5
  law); the added detail lives inside the steps as scannable commands and
  one-line hints, not as extra top-level steps beyond that.
- **Breathing room:** `pre` blocks and short hint lines add white space, not
  density; no multi-column walls.
- **Show, don't prose:** the existing SVG figure stays; the new material is
  commands and output shapes, which cannot be drawn.
- **Accuracy over plausibility:** every command, path, exit-code meaning,
  and output shape was verified against the real release tarball, the real
  installer and doctor scripts, and a real doctor run (2026-11-15).
- **Plain language:** release, tarball, plugin, sidecar, brain, vault, and
  registration are each defined in ordinary words at first use.
- **No JavaScript, attribution:** untouched.
