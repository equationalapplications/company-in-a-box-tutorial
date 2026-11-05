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
| Implementation | DONE | `36f16b2`…(HEAD) — 13 pages, checker, tests, workflows; see commit map |
| Independent sign-off | DONE | 13/13 pages PASS all gates — non-author reviewer deleg_f609832f (verdict in signoff.md) |
| Review ladder (implemented diff) | DONE | T1.5 five rungs + Opus delta; all findings folded, tests 24/24 + checker PASS |
| Merge | DONE | merged on Kurt's go 2026-11-05 17:49Z (`31851c1`); Pages live |
| Deploy + live verification | DONE | deploy workflow green; 13 pages + CSS all HTTP 200 at the live URL; `/specs/…` 404 asserted (repo docs not published); first-run CI fix: gitleaks checksums asset name corrected (`gitleaks_8.30.1_checksums.txt`) |

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

- GoatCounter: SELF-HOSTED (D12) — parallel session provisions infra
  (analytics-infra). Site ships ZERO scripts until the instance is
  reachable; the tag + checker regex amendment land as a follow-up commit
  after.
- Search Console verification file: lands when Kurt creates the property.
- Board note: the delivery-board skill file is at its size limit — this
  ledger is the in-flight record (decision-log D9/D11).
