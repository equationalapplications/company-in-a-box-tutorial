# Ledger — company-in-a-box-tutorial

Status ledger for this spec folder. INTENT.md never carries status; this
file is the authoritative in-flight state (decision-log D11).

## Stage

**IMPLEMENTATION — in progress** (plan approved by Kurt, 2026-11-05).

## Approvals

| Gate | Status | Evidence |
|------|--------|----------|
| Design dialogue | DONE | owner rulings in the founding thread, 2026-11-05 |
| Spec (general) | DONE | owner message, 2026-11-05 |
| Cost-escalatory spec review | DONE | D9: T1.5 ladder + T3 Opus + T4 Fable + delta verify, within announced budget |
| Spec gate | DONE | owner message, 2026-11-05 |
| Plan gate | DONE | owner message, 2026-11-05 + SDD folder pattern ruling → D11 |
| Implementation | IN PROGRESS | commit map below |
| Review ladder (implemented diff) | PENDING | after implementation |
| Merge | PENDING | Kurt's go |

## Commit map (implementation)

| Step | Deliverable | Commit | State |
|------|-------------|--------|-------|
| 0 | Ledger (this file) | (this folder) | live — updated per stage |
| 1 | `tools/check_site.py` + `tools/requirements-dev.txt` | `a5b054d` + checker fixes | DONE — PASS on 13 pages (offline + external) |
| 2 | `.github/workflows/check.yml` | `a5b054d` | DONE |
| 3 | `site/css/style.css` | `3d7907b` | DONE |
| 4 | 13 pages (one commit each, page-map order) | `36f16b2`…`1946bbc` | DONE — checker PASS |
| 5 | sign-off (non-author reviewer) | — | IN PROGRESS — receipts filled, signature pending |
| 6 | `.github/workflows/pages.yml` + deploy verify | (this batch) | workflow written; deploy verify after merge |
| 7 | `README.md` | (this batch) | DONE |

Visual check (spec test 5): index + the-pattern rendered over CDP, screenshots
inspected 2026-11-05 — white space, hierarchy, step styling, header/footer OK.

## Open items

- GoatCounter account: Tessera preps, Kurt clicks signup. Site ships ZERO
  scripts until then; tag lands as a follow-up commit after.
- Search Console verification file: lands when Kurt creates the property.
- Board note: the delivery-board skill file is at its size limit — this
  ledger is the in-flight record (decision-log D9/D11).
