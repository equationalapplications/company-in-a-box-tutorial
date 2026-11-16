# Spec — configure-ct-hermes: expanding the tutorial to 15 pages

Status: Implemented, Tier-3 review converged 2026-11-16 (expansion rounds
1–4: PASS WITH MAJORS → REQUEST CHANGES → APPROVE-pending-wording →
APPROVE; all findings folded or adjudicated with cites). Implemented
2026-11-16 in `4266abe`…`72c6510` (the four build commits), plus review
folds `1d0ec80` onward on this branch. Write-time checks resolved — see
"Write-time check resolutions" below.

Owner ruling — target-state publication (Kurt, 2026-11-16, in-thread msg
1571898766007734333): "We continue to publish this tutorial as if those
issues are already fixed" (CT issues #355 Strict-card wording, #356
local-embedder calibration coverage). The pages therefore teach Wisdom
delivery as working on every embedder option, without the
today-state caveats (uncalibrated abstention, rarity on real messages);
only the mechanism (confident-match gate) and the verbose log's
`gate_uncalibrated` reason remain, phrased as forward-looking. This is a
deliberate owner decision that outranks the integrations README's
current known-limits wording; the CT fixes are tracked in #355/#356 and
this page's calibration/expectation text should be re-checked against
them when they land.

Date: 2026-11-16
Owner: Kurt VanDusen
Supersedes (in scope): `specs/first-integration-detail/spec.md` — that
delivery's page (`site/first-integration.html`) becomes one page of this
larger restructure.

## Problem

The tutorial teaches the three-tool pattern in 13 pages, but the middle of
the journey is compressed: installing Curated Thoughts jumps straight from
"open the app" to wiring Hermes, with no page on choosing models and privacy
(step 3 of the real setup), and "check that memory works" is buried as the
tail of the integration-install page. New users also get one over-promise:
that remembered facts "start showing up on their own" — which the
integrations' known limits do not support unconditionally (matching needs a
calibrated embedder and rarely fires on real messages yet; corrections
always flow).

This change restructures the site from 13 to 15 pages and from 7 to 9
numbered steps:

- `setup-memory.html` (step 2) expands to five real steps.
- NEW `models-privacy.html` — step 3, "Choose models and privacy".
- `connect-memory.html` renumbers 3 → 4; `first-integration.html` 4 → 5.
- NEW `check-it-works.html` — step 6, "Check that memory works".
- `procedures`/`delegate`/`schedule` renumber 5/6/7 → 7/8/9.

## Page map (15 rows)

| topic | File | Visible step | Change |
|---|---|---|---|
| 1 | index | — | page count text |
| 2 | the-pattern | — | — |
| 3 | the-three-tools | — | — |
| 4 | setup-hermes | 1 | — |
| 5 | setup-memory | 2 | expanded to 5 steps |
| 6 | models-privacy | 3 | NEW: "Step 3 · Choose models and privacy" |
| 7 | connect-memory | 3→4 | renumber |
| 8 | first-integration | 4→5 | trimmed to 3 steps |
| 9 | check-it-works | 6 | NEW: "Step 6 · Check that memory works" |
| 10 | procedures | 5→7 | renumber |
| 11 | delegate | 6→8 | renumber |
| 12 | schedule | 7→9 | renumber |
| 13 | delivery-flow | — | pager |
| 14 | team-memory | — | topic only |
| 15 | links | — | topic, step text, Ollama link |

## Per-page goals

### setup-memory.html (step 2, five steps)

1. **Download and install** from the CT Releases page, naming the real
   asset per OS (version marked as an example that will move).
2. **First launch** — quote the real wizard screen "Where is your vault?"
   (Browse… / Confirm); example folder `Documents/company-vault`; warn that
   switching vaults discards the knowledge layer (the app offers a backup
   first); point ahead to step 3 for the privacy/AI screens (keep defaults).
3. **Check the command-line tools** — `ct status` (see resolutions: there is
   no `ct --version`).
4. **Drop in documents and keep the app running** — describe the
   source-documents folder the app sets up inside the vault without naming
   it (checker redaction law); headless: `ct watch` with `CURATED_VAULT_ROOT`
   set, or `ct ingest --yes` once.
5. **Approve proposed summary pages** in the app's Review screen (or
   `ct proposals review` in a terminal).

Plus: brain-location paragraph after the steps (`~/.brain`, `brain.db` and
`config.json`, `CURATED_BRAIN_DIR`); the existing SVG gains a `~/.brain`
label; keep the "Why a human approves" aside.

### models-privacy.html (NEW, step 3, four steps)

Lead: nothing here is required; with no setup at all text search always
works and semantic search uses a small built-in model.

1. **Check your privacy mode** (Settings → Privacy): Strict (default),
   Ephemeral cloud inference, Connected agent (Cloud Bridge) — one plain
   line each, plus the scope truth: Strict blocks cloud *generation* and the
   cloud *bridge*; embeddings follow their own setting and the default stays
   on-machine; pointing embeddings at a cloud API sends embedded text out in
   any mode.
2. **Choose how search understands meaning (embeddings).** Define the term;
   options: do nothing (built-in model, slower, downloads on first use);
   local Ollama, fully offline (the wizard's "Set up local search" screen
   configures it; the sidecar finds Ollama at `http://127.0.0.1:11434`);
   cloud API via `embed_profile` in the brain's `config.json` (there is no
   Settings screen for embeddings — link the CT README BYOI section). No
   `ollama pull` tag is taught (see resolutions).
3. **Choose who writes summary pages (generation)**, Settings → Models:
   Strict means Auto-Install (local model); an own endpoint (local Ollama or
   cloud, OpenAI-compatible) means switching to Ephemeral first, then base
   URL, optional key, model name, Save. Callout: this is not Hermes' model.
4. **If you picked a cloud embedding key, make it reach the sidecar** —
   `~/.hermes/.env` (`OPENROUTER_API_KEY`, no `sk-` sample values), the
   installer's `env:` lines, lookup order `EMBED_API_KEY` →
   `OPENROUTER_API_KEY` → `OPENAI_API_KEY`; a generation key entered in the
   app needs none of this.

SVG: NEW three-mode ladder (Strict / Ephemeral / Connected columns; rows
"your notes and the brain" = local everywhere, "summary writing" =
local / may use cloud / may use cloud, "cloud connection" = off / off /
read-only) plus a dashed note: embeddings are a separate choice — **no
embedding row in the ladder**.

The "Private by default" aside moves here from first-integration with one
correction (embeddings are not configured in Settings → Models; see
resolutions).

### first-integration.html (step 5, exactly 3 steps)

1. Download and unpack (unchanged text).
2. Run the installer + its "What you should see".
3. Place the printed config blocks (unchanged text; "tutorial step 3" →
   "tutorial step 4").

Removes: the doctor step, the restart step, the lifecycle SVG and the
"Private by default" aside (moved). Adds a one-line pointer: privacy
choices → step 3. Keeps the other-harnesses aside. Commit 3 adds the NEW
"where things land" SVG: tarball → `install.sh` →
`~/.hermes/plugins/curated-thoughts/` → printed blocks → a `config.yaml`
drawing showing the nesting of `mcp_servers.curated-thoughts` and
`plugins.enabled`.

### check-it-works.html (NEW, step 6, four steps)

1. **Run the doctor** — command moved word-for-word; generic sample output
   (describe the lines; never show a brain-database path), tally
   `0 FAIL, 1 WARN, 9 PASS` with the WARN being the expected
   embedding-backend hint; PASS/WARN/FAIL and exit codes 0/1/2; the
   `sidecar-env` sentence moved.
2. **Restart Hermes** — moved text, with the over-promise softened to the
   known limits (matching needs a calibrated embedder and rarely fires on
   real messages yet; corrections always flow).
3. **Ask something only your vault knows** (a document approved in step 2).
4. **Know what to expect, and turn on verbose mode** — `CT_WISDOM_VERBOSE=1`,
   `ct_wisdom_log.py --host hermes -n 5`, log at
   `~/.hermes/logs/ct-wisdom-verbose.jsonl`; reasons `no_match`, `deduped`,
   `gate_uncalibrated`.

SVG: the lifecycle diagram moved from first-integration with its caption
corrected to "speaks up when it finds a confident match".

## Mechanical changes

- `tools/check_site.py`: MANIFEST grows to the 15 rows above (comments at
  the exemption note and the sitemap check updated to 15).
- `site/sitemap.xml`: add the two new URLs.
- `README.md`: 13 pages → 15.
- `index.html`: "ten short pages: seven numbered steps" → "twelve short
  pages: nine numbered steps".
- Renumbering per the page map on setup-memory, connect-memory,
  first-integration, procedures, delegate, schedule, delivery-flow,
  team-memory, links (titles, h1, data-topic, "Next:" lines, pagers);
  links.html step mentions 5/6/7 → 7/8/9 and gains an Ollama link
  (`https://ollama.com/download`).
- New pages: header and footer byte-for-byte from an existing page; zero
  `<script>`; one `<h1>`; exactly one inline SVG each; ≤5 steps.

## Write-time check resolutions (owner-verified — do not re-litigate)

- `ct --version` does NOT exist; the sanity check is `ct status` (a short
  table: docs, chunks, wiki entries, pending proposals, schema version,
  brain-database path, last ingest run). The sample must stay generic — no
  literal database path.
- Release assets (version an example that will move): Linux
  `Curated.Thoughts_3.13.0_amd64.deb` (AppImage/rpm also exist), macOS
  `Curated.Thoughts_3.13.0_universal.dmg`, Windows
  `Curated.Thoughts_3.13.0_x64-setup.exe`.
- `ollama pull nomic-embed-code` FAILS (HTTP 404). Teach NO `ollama pull`
  tag; local search is configured by the wizard's "Set up local search"
  screen; advanced users set `embed_profile` in the brain's `config.json`
  (CT README BYOI section).
- The app's nav label is "Review" (not "Review desk").
- Wizard screens in order: "Where is your vault?" → "Choose your privacy
  posture" → "Set up local search" → "Pick your AI" (Auto-Install
  (recommended) / Skip – Use my own) → "watch it think" → "You're ready".
  Settings tabs: Vault, Privacy, Knowledge schema, Models, Librarian,
  Agents, Maintenance, Appearance.
- Privacy truth: Strict blocks cloud generation and the cloud bridge;
  embeddings follow their own setting (default on-machine); a cloud
  embedding API receives embedded text in any mode. In Strict the generation
  form is disabled: local generation = Auto-Install; an own endpoint means
  switching to Ephemeral first.
- Redaction laws: never write the string naming the immutable source
  folder; no `/home/` paths; `~/` only before dotfiles; no `sk-` samples.
- Footer byte-for-byte across pages; zero `<script>`; one `<h1>` per page;
  exactly one inline SVG on each new page per §4 of the plan.

## Alignment with INTENT.md

- **Small bites:** each page stays at ≤5 numbered steps (the checker
  enforces it); the expansion *splits* dense content rather than adding
  density — the integration page drops from five steps to three.
- **Breathing room:** new pages follow the existing one-column template.
- **Show, don't prose:** each new page carries exactly one inline SVG; the
  setup-memory diagram gains a label rather than prose.
- **Accuracy over plausibility:** every wizard screen, settings tab,
  privacy-mode behavior, release asset and command in this spec was checked
  against the CT source, its README, and live runs; the one thing the app's
  UI misstates (Strict card wording) is described truthfully without
  contradicting it, and the over-promise about automatic facts is softened
  to the integrations' documented limits.
- **Plain language:** embedding, doctor, PASS/WARN/FAIL, Intuitive Wisdom,
  verbose mode are defined in ordinary words at first use.
- **No JS, attribution:** unchanged; headers/footers copied byte-for-byte.

## Sign-off

| Page / area | Reviewed by | Date | Verdict |
|---|---|---|---|
| (pending Tier-3 review cycle) | — | — | — |
