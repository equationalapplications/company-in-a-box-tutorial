# Ledger — first-integration detail

Status ledger for this spec folder. INTENT.md never carries status; this
file is the authoritative in-flight state (decision-log D11 pattern).

## Stage

**IMPLEMENTATION — in progress** (spec approved via relayed Gemini review,
2026-11-16; plan authored same day under the owner's "ready for execution"
authorization).

## Approvals

| Gate | Status | Evidence |
|------|--------|----------|
| Spec gate | DONE | Kurt-approved Gemini review posted in-thread, 2026-11-16 (msg 1571873225405894749) |
| Reviewer consideration fold | DONE | Gemini's config-handoff note verified against `install.sh` before adoption — its "paste at root level" wording is correct only for the no-section case; spec teaches both installer print cases |
| Plan gate | (covered by the owner's "ready for execution" authorization on the relayed review — single-page docs diff) | 2026-11-16 |
| Implementation | IN PROGRESS | see commit map |
| Independent review | PENDING | reviewer must not be the implementer |
| Ready flip | PENDING | only after review converges; spec → Implemented, plan/ledger deleted |
| Merge | PENDING | Kurt merges on attended runs |

## Commit map

| Step | Deliverable | Commit | State |
|------|-------------|--------|-------|
| 1 | spec: approval + config-placement fold | (pending) | PENDING |
| 2 | page rewrite (the three `ol.steps` items) | (pending) | PENDING |
| 3 | cleanup + ready flip | (pending) | PENDING |

## Working notes

- Installer print cases verified 2026-11-16 in
  `integrations/hermes/scripts/install.sh` (curated-thoughts-integrations):
  case A "No 'mcp_servers:' section found. Add the following to
  ~/.hermes/config.yaml:" (top-level paste); case B "An 'mcp_servers:'
  section exists but has no 'curated-thoughts' key. Insert the following
  block INSIDE that section (indent one level):" (nested paste).
- Checker counts only top-level `<ol>` `<li>` children; nested `<ul>` is
  safe for the 3-step law.
- Footer byte-identity: footer must not be touched; verified per commit.
