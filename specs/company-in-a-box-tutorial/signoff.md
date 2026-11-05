# Sign-off table — company-in-a-box-tutorial

The manual gates from the spec. One row per manifest page; four gates.
Signed by a reviewer who did NOT author the pages (self-sign is not a gate);
the completed table is reviewed by the CEO at the merge gate. Any later
change to a page re-signs that page's row.

| # | Page | Topic match | Redaction checked | Grounding receipts (source @ date) | Terms defined |
|---|------|-------------|-------------------|-------------------------------------|---------------|
| 1 | index.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | Links live: GH repos ×3, hermes docs, synapsetree.dev, EA site (2026-11-05) | ✅ (sign-off deleg_f609832f) |
| 2 | the-pattern.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | EA real org (vault fact-check, 2026-11-05, no path); CTI INTENT "From one agent to a team" as labeled aside [intent] (fetched 2026-11-05) | ✅ (sign-off deleg_f609832f) |
| 3 | the-three-tools.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | CT + CTI public INTENT.md files, CT README, Hermes docs llms.txt (all fetched 2026-11-05); INTENT claims only where Built-confirmed @ CT `33fb4fd70494` | ✅ (sign-off deleg_f609832f) |
| 4 | setup-hermes.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | Hermes docs llms-full.txt installation.md + quickstart (fetched 2026-11-05): install.sh, `hermes setup --portal`, install→chat under 5 min, profile optional. COMPAT RECEIVED 2026-11-05: content sourced from upstream docs verbatim; EA live deployment (hermes CLI v0.22.6 present) consistent — no divergence found | ✅ (sign-off deleg_f609832f) |
| 5 | setup-memory.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | CT README (fetched 2026-11-05): Releases installers, drop PDF/DOCX/MD, pending approval; one-brain-per-vault @ CT `33fb4fd70494` "Who verifies" | ✅ (sign-off deleg_f609832f) |
| 6 | connect-memory.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | `mcp_servers` command/args shape @ Hermes docs mcp.md (llms-full, fetched 2026-11-05); sidecar `--mcp` from CTI README (fetched 2026-11-05). COMPAT RECEIVED 2026-11-05: EA live config.yaml registers the same block (`curated-thoughts: command: …-mcp`, args `--mcp`) — matches taught block exactly | ✅ (sign-off deleg_f609832f) |
| 7 | first-integration.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | CTI README integration layers + Intuitive Wisdom + hermes-v0.7.2 status (fetched 2026-11-05); integrations/hermes tree verified via GH API 2026-11-05. COMPAT RECEIVED 2026-11-05: CTI hermes plugin registered in EA live plugins config — integration in active use | ✅ (sign-off deleg_f609832f) |
| 8 | procedures.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | Rule stack: EA real practice (vault fact-check, 2026-11-05); skills/context-files @ Hermes docs (both 200, 2026-11-05); CT/CTI INTENT+AGENTS pattern (fetched 2026-11-05) | ✅ (sign-off deleg_f609832f) |
| 9 | delegate.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | Hermes docs delegation.md (llms-full, fetched 2026-11-05): delegate tool, isolated subagents, parallel children, live monitor. COMPAT RECEIVED 2026-11-05: delegation taught verbatim from upstream docs; EA uses the same mechanism — no divergence found | ✅ (sign-off deleg_f609832f) |
| 10 | schedule.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | Hermes docs cron.md summary (llms.txt, fetched 2026-11-05): plain-language scheduling, skill attachment, delivery. COMPAT RECEIVED 2026-11-05: taught verbatim from upstream docs; EA scheduled jobs use the same mechanism — no divergence found | ✅ (sign-off deleg_f609832f) |
| 11 | delivery-flow.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | One-PR sentence @ CT `33fb4fd70494` "How changes are made" (stale named-model sentence excluded); EA internal flow (vault fact-check, 2026-11-05, taught generically) | ✅ (sign-off deleg_f609832f) |
| 12 | team-memory.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | synapsetree.dev own copy ONLY [vendor-description]: cloud hub, teams, exportable (fetched 2026-11-05); no pricing on page; no auto-sync claim; one-brain-per-vault @ CT `33fb4fd70494` | ✅ (sign-off deleg_f609832f) |
| 13 | links.html | ✅ (sign-off, non-author reviewer deleg_f609832f) | ✅ (grep clean + reviewer) | Every external target re-verified by check_site.py --check-external (PASS 2026-11-05); link list uses ul | ✅ (sign-off deleg_f609832f) |

SIGNED 2026-11-05 by the non-author sign-off reviewer (subagent
sa-0-0d60dd4c / delegation deleg_f609832f): 13/13 pages PASS on topic,
redaction, and terms — verdict file at
.hermes/cache/scratch/cib-ladder/signoff-verdict.md (transient). Compat
receipts on pages 4/6/7/9/10 received (see rows). CEO reviews this table
at the merge gate per D10.
