# Plan — first-integration page detail rewrite

Status: Executing under the spec approval relayed by Kurt (Gemini review,
2026-11-16: "ready for execution").
Owner: Tessera
Date: 2026-11-16
Spec: [spec.md](spec.md) (Reviewed 2026-11-16)

## Commits

1. `docs(spec): record approval + config-placement guidance` — spec status
   flip to Reviewed and the Gemini review's config-handoff consideration,
   folded only after verification against the real `install.sh` (the
   suggested "paste at root level" wording is correct for one of the
   installer's two print cases and wrong for the other; the spec now teaches
   following the installer's own placement message).
2. `feat: teach each first-integration step in detail` — the page rewrite
   itself. Only the three top-level `<ol class="steps">` list items and
   their nested detail change; lead, layers paragraph, figure, aside,
   next-page links, and footer stay byte-identical.
3. Cleanup commit (only after the review loop converges): flip the spec's
   status to `Implemented`, delete plan.md and ledger.md (transient
   scaffolding), then flip the PR from draft to ready.

## Per-commit tests

- Commit 1: spec-only — `git diff --stat` must show nothing under `site/`.
- Commit 2: `python3 tools/test_check_site.py` (unit tests), then
  `python3 tools/check_site.py` (full: html5lib strict parse, ≤5-step law,
  footer byte-identity across the manifest, link check, gitleaks gate).

## Risks and mitigations

- YAML-placement prose could bloat the page — mitigated: it rides inside
  the existing step 2 as a short nested list, keeping exactly 3 top-level
  steps.
- Drift outside `ol.steps` — spec forbids it; the checker's footer
  identity check plus a manual `git diff` scope check verify.
- Example-version rot — the version number is marked as an example in the
  prose (spec constraint), so shipping v0.7.3 later cannot stale the page.
