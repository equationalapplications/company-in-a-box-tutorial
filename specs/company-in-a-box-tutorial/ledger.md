# Ledger — company-in-a-box-tutorial

Status ledger for this spec folder. INTENT.md never carries status; this
file is the authoritative in-flight state (decision-log D11).

## Stage

**IMPLEMENTATION — in progress** (plan approved by Kurt, 2026-11-05).

## Approvals

| Gate | Status | Evidence |
|------|--------|----------|
| Design dialogue | DONE | D1–D5, Discord thread 2026-11-05 |
| Spec (general) | DONE | msg 1567915303479017656 |
| Cost-escalatory spec review | DONE | D9: T1.5 ladder + T3 Opus + T4 Fable + delta verify, $4.02 of $8.50 |
| Spec gate | DONE | msg 1567942439455686788 (option 1) |
| Plan gate | DONE | msg 1567943892282908773 (option 1 + SDD folder pattern ruling → D11) |
| Implementation | IN PROGRESS | commit map below |
| Review ladder (implemented diff) | PENDING | after implementation |
| Merge | PENDING | Kurt's go |

## Commit map (implementation)

| Step | Deliverable | Commit | State |
|------|-------------|--------|-------|
| 0 | Ledger (this file) | — | this commit |
| 1 | `tools/check_site.py` + `tools/requirements-dev.txt` | — | pending |
| 2 | `.github/workflows/check.yml` | — | pending |
| 3 | `site/css/style.css` | — | pending |
| 4 | 13 pages (one commit each, page-map order) | — | pending |
| 5 | sign-off (non-author reviewer) | — | pending |
| 6 | `.github/workflows/pages.yml` + deploy verify | — | pending |
| 7 | `README.md` | — | pending |

## Open items

- GoatCounter account: Tessera preps, Kurt clicks signup. Site ships ZERO
  scripts until then; tag lands as a follow-up commit after.
- Search Console verification file: lands when Kurt creates the property.
- Board note: `tessera-delivery-flow-board` SKILL.md at 100K-char limit —
  this ledger is the in-flight record (D9/D11).
