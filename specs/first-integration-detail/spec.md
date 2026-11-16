# Spec — first-integration page: teach each install step in detail

Status: Implemented (2026-11-16; independent review PASS, adjudicated low finding: example tally is hedged with "like", no action)
Date: 2026-11-15
Owner: Tessera

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

Rewrite the three numbered steps on `site/first-integration.html` into three
fully taught steps. Each step gets: one or two sentences of context (what
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
2. **Run the installer, then the doctor.**
   - `bash hermes-0.7.2/scripts/install.sh` — copies the plugin into
     `~/.hermes/plugins/curated-thoughts/`, safe to run again any time, no
     administrator rights needed.
   - If the installer prints a config block, do exactly what its own
     message says about placement — `install.sh` prints two different
     cases (verified in the script, 2026-11-16): no `mcp_servers:` section
     yet → "Add the following to ~/.hermes/config.yaml", and the block
     goes in at the top level of the file, exactly as printed; an
     `mcp_servers:` section that lacks the `curated-thoughts` key →
     "Insert the following block INSIDE that section (indent one level)",
     so the block must be nested under the existing `mcp_servers:` line,
     not pasted at the bottom of the file (a top-level paste there would
     corrupt the YAML). Readers who skipped step 3 get the first case.
     Everyone gets the `plugins.enabled` entry that switches the plugin
     on. It never overwrites an existing entry. The page must teach both
     cases in plain words — YAML placement mistakes are the classic
     beginner trap here (Gemini review note, 2026-11-16).
   - `python3 ~/.hermes/plugins/curated-thoughts/scripts/ct_doctor.py check`.
   - Plain-language definitions at first use: plugin (an add-on Hermes
     loads), sidecar, brain, vault, registration — the four things the
     doctor checks, in ordinary words.
   - What you should see: a line per check, most saying PASS, then a tally.
     `0 FAIL` is the goal. WARN means it works but a feature is degraded —
     the line's `fix:` hint says exactly what to do. FAIL means stop and fix
     what the line says, then re-run.
3. **Restart Hermes and watch memory show up on its own.**
   - Quit and reopen Hermes so it loads the plugin.
   - The live signs, as today: a short recall of relevant procedures and
     facts at session start, and relevant facts appearing as you talk.
   - New troubleshooting hint: if nothing shows up, re-run the doctor, make
     sure `plugins.enabled` lists `curated-thoughts`, and make sure Curated
     Thoughts is version 3.3.0 or newer.

### Constraints honored

- Step-count law: the page keeps exactly 3 top-level `li` steps (checker
  hard limit is 5; nested lists do not count). Sub-details ride inside the
  steps as prose, `pre` blocks, and nested lists.
- No new scripts, no new external links (the releases link already exists).
- Sample output shown on the page must use generic paths (`~`, no real home
  directory names) to pass the checker's redaction grep.
- The example version `0.7.2` is marked as an example in the prose so the
  page does not rot when v0.7.3 ships.

## Files touched

- `site/first-integration.html` — the three `ol.steps` list items only,
  plus their nested detail. No other element changes.

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

- **Small bites:** still one topic, still 3 numbered steps; the added detail
  lives inside the steps as scannable commands and one-line hints, not as
  extra top-level steps.
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
