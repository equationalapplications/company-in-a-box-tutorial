# Sign-off table — company-in-a-box-tutorial

The manual gates from the spec. One row per manifest page; four gates.
Signed by a reviewer who did NOT author the pages (self-sign is not a gate);
the completed table is reviewed by the CEO at the merge gate. Any later
change to a page re-signs that page's row.

| # | Page | Topic match | Redaction checked | Grounding receipts (source @ date) | Terms defined |
|---|------|-------------|-------------------|-------------------------------------|---------------|
| 1 | index.html | ⬜ | ⬜ | Links live: GH repos ×3, hermes docs, synapsetree.dev, EA site (2026-11-05) | ⬜ |
| 2 | the-pattern.html | ⬜ | ⬜ | EA real org (vault fact-check, 2026-11-05, no path); CTI INTENT "From one agent to a team" as labeled aside [intent] (fetched 2026-11-05) | ⬜ |
| 3 | the-three-tools.html | ⬜ | ⬜ | CT + CTI public INTENT.md files, CT README, Hermes docs llms.txt (all fetched 2026-11-05); INTENT claims only where Built-confirmed @ CT `33fb4fd70494` | ⬜ |
| 4 | setup-hermes.html | ⬜ | ⬜ | Hermes docs llms-full.txt installation.md + quickstart (fetched 2026-11-05): install.sh, `hermes setup --portal`, install→chat under 5 min, profile optional. COMPAT RECEIVED 2026-11-05: content sourced from upstream docs verbatim; EA live deployment (hermes CLI v0.22.6 present) consistent — no divergence found | ⬜ |
| 5 | setup-memory.html | ⬜ | ⬜ | CT README (fetched 2026-11-05): Releases installers, drop PDF/DOCX/MD, pending approval; one-brain-per-vault @ CT `33fb4fd70494` "Who verifies" | ⬜ |
| 6 | connect-memory.html | ⬜ | ⬜ | `mcp_servers` command/args shape @ Hermes docs mcp.md (llms-full, fetched 2026-11-05); sidecar `--mcp` from CTI README (fetched 2026-11-05). COMPAT RECEIVED 2026-11-05: EA live config.yaml registers the same block (`curated-thoughts: command: …-mcp`, args `--mcp`) — matches taught block exactly | ⬜ |
| 7 | first-integration.html | ⬜ | ⬜ | CTI README integration layers + Intuitive Wisdom + hermes-v0.7.2 status (fetched 2026-11-05); integrations/hermes tree verified via GH API 2026-11-05. COMPAT RECEIVED 2026-11-05: CTI hermes plugin registered in EA live plugins config — integration in active use | ⬜ |
| 8 | procedures.html | ⬜ | ⬜ | Rule stack: EA real practice (vault fact-check, 2026-11-05); skills/context-files @ Hermes docs (both 200, 2026-11-05); CT/CTI INTENT+AGENTS pattern (fetched 2026-11-05) | ⬜ |
| 9 | delegate.html | ⬜ | ⬜ | Hermes docs delegation.md (llms-full, fetched 2026-11-05): delegate tool, isolated subagents, parallel children, live monitor. COMPAT RECEIVED 2026-11-05: delegation taught verbatim from upstream docs; EA uses the same mechanism — no divergence found | ⬜ |
| 10 | schedule.html | ⬜ | ⬜ | Hermes docs cron.md summary (llms.txt, fetched 2026-11-05): plain-language scheduling, skill attachment, delivery. COMPAT RECEIVED 2026-11-05: taught verbatim from upstream docs; EA scheduled jobs use the same mechanism — no divergence found | ⬜ |
| 11 | delivery-flow.html | ⬜ | ⬜ | One-PR sentence @ CT `33fb4fd70494` "How changes are made" (stale named-model sentence excluded); EA internal flow (vault fact-check, 2026-11-05, taught generically) | ⬜ |
| 12 | team-memory.html | ⬜ | ⬜ | synapsetree.dev own copy ONLY [vendor-description]: cloud hub, teams, exportable (fetched 2026-11-05); no pricing on page; no auto-sync claim; one-brain-per-vault @ CT `33fb4fd70494` | ⬜ |
| 13 | links.html | ⬜ | ⬜ | Every external target re-verified by check_site.py --check-external (PASS 2026-11-05); link list uses ul | ⬜ |

Signature: a non-author reviewer initials each ⬜ (three per row) after
checking; unresolved compat receipts on pages 4/6/7/9/10 block merge.
