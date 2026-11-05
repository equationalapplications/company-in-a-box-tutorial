# Spec — company-in-a-box-tutorial static site

Status: Draft (T1.5 ladder converged — APPROVE WITH NITS; T3 Opus findings
folded; T4 Fable findings folded — heading to Fable delta verification,
then Kurt's spec gate)
Owner: Tessera — EA's executive agent (decision-log header: "Tessera is the
model, not just the author"; naming sanctioned by D2/D8)
Date: 2026-11-05

## Problem

EA runs a working "software company in a box" — one human (Kurt) plus AI
agents holding executive, worker, and reviewer roles, with durable memory in
Curated Thoughts, tool wiring in Curated Thoughts Integrations, and Hermes
Agent as the runtime. The knowledge of *how it fits together* exists only
inside EA's private vault and in scattered repo READMEs. A newcomer who wants
to replicate the pattern has no single teaching artifact: nothing that says
what the pieces are, why to use them, and in what order to set them up.

Evidence:

- Public repos exist and are linkable:
  `equationalapplications/curated-thoughts` (verified via `gh repo list`),
  `equationalapplications/curated-thoughts-integrations` (verified),
  `equationalapplications/hermes-agent` (verified).
- Hermes Agent's public docs exist and are live:
  https://hermes-agent.nousresearch.com/docs (HTTP 200, 2026-11-05). EA's
  `equationalapplications/hermes-agent` repo is a FORK of the upstream
  `NousResearch/hermes-agent` (verified via the GitHub API, 2026-11-05);
  the tutorial links ONLY the upstream repo and docs — EA's fork is never
  linked.
- SynapseTree.dev is live (HTTP 200, fetched 2026-11-05) and positions itself
  as the hosted, team-shared memory of the same family — the correct "next
  step when you have a team" destination the tutorial should point at.
- `equationalapplications.com` is live (HTTP 200, 2026-11-05).
- EA's delivery-flow procedures live in its private agent vault — no public
  equivalent exists.

All live-URL evidence above was captured 2026-11-05 and is re-runnable:
`tools/check_site.py` (implementation) re-verifies every external target on
every checker run — checker runs happen on PRs and on a schedule, never on
the deploy path; repo links were verified via `gh repo list` and the
fork relationship via the GitHub API.

## Proposed change

Build a multi-page, no-build-step static site (plain HTML + CSS + hand-authored
inline SVG infographics), MIT licensed, with "Made with love" attribution back
to EA on every page, deployed on GitHub Pages.

**Deployment boundary (review finding F2):** the Pages workflow uploads ONLY
the `site/` directory — the tutorial pages, `css/`, and the Search Console
verification file. `INTENT.md`, `AGENTS.md`, `README.md`, and `specs/` stay
repo-only (they are public on GitHub anyway, but they are not site content).
A post-deploy check asserts
`https://<site>/specs/company-in-a-box-tutorial/spec.md` returns 404
(the concrete path makes the assertion reproducible and immune to a bare
`/specs/` directory-404 false pass).

### Design law (from INTENT.md central intent)

- Landing page = overview: what it is, why to use it. Nothing else competes
  with it.
- Each following page teaches ONE small thing in a few steps. "Steps" is
  defined mechanically: the TOTAL count of top-level `li` children across
  ALL `ol` elements on a non-landing page, with no class opt-in — more
  than 5 is a HARD FAILURE of `tools/check_site.py` (nested lists don't
  count). Exactly one topic per page — its own row in the page map. Every page carries a
  `data-topic` attribute matching its page-map row, so a machine can check
  the label's presence and uniqueness; a human reviewer judges whether the
  content actually matches its one topic and signs off on the same table
  as a second gate.
- Generous white space; no dense multi-column text walls.
- Infographics used widely (one per page where the page map promises one).
- No JavaScript required to learn from the site (analytics is a single
  cookieless ~3.5KB script; a JS-free pixel is the documented fallback).

### Page map (13 pages + shared assets)

| # | File (under `site/`) | Teaches (exactly one topic) | Infographic | Grounded against |
|---|------|---------|-------------|------------------|
| 1 | `index.html` | Overview: what a company in a box is; why use it; where to start | Box diagram: you + memory + integrations + agent = a company | (links verified live) |
| 2 | `the-pattern.html` | The pattern: one person directing agent roles (executive, workers, reviewers) | Org chart: you → executive agent → delegated workers | EA's real one-person org [built]; CTI INTENT.md "From one agent to a team" cited ONLY as a "where this is heading" aside [intent] |
| 3 | `the-three-tools.html` | Meet the three tools, one glance each | Three-tool triangle feeding one company | CT INTENT.md cited ONLY for rules marked Built (e.g. one brain per vault); CTI INTENT.md is `[intent]` unless a README/CHANGELOG confirms the claim; Hermes docs [built] |
| 4 | `setup-hermes.html` | Install Hermes Agent and get a first response | Install flow: install → first conversation (profiles are an optional later step, not an install phase) | Hermes docs `getting-started/installation` + quickstart ("install to chatting in under 5 minutes" — profile NOT required; both 200, 2026-11-05) [built] + upstream-docs compat receipt |
| 5 | `setup-memory.html` | Install Curated Thoughts (the brain-and-vault idea explained inline only as far as the install needs) | Brain/vault diagram: files → facts → recall | CT repo + EA's internal CT installation runbook (fact-check only) [built] |
| 6 | `connect-memory.html` | Register the CT sidecar as the agent's MCP memory server | Agent ↔ sidecar ↔ vault wiring | CT repo + Hermes docs `user-guide/features/mcp` + `guides/use-mcp-with-hermes` (200, 2026-11-05) [built] |
| 7 | `first-integration.html` | Install the CTI Hermes plugin so remembered facts arrive in the agent's context automatically | Plugin lifecycle diagram: session start → each message → facts injected | CTI repo `integrations/hermes/` (`plugin.yaml`, `integration.yaml`, `hooks/` — verified in-tree, 2026-11-05) [built] |
| 8 | `procedures.html` | Give the company standing rules: the rule stack (INTENT.md → AGENTS.md → procedures → skills) | Rule stack diagram | INTENT/AGENTS pattern: CT + CTI repos [built]; skills: Hermes docs `user-guide/features/skills` + `user-guide/features/context-files` [built]; procedures: EA-internal, private fact-check only (no public equivalent) [built-in-EA, taught generically] |
| 9 | `delegate.html` | Delegate work to agent subagents | Dispatch diagram | Hermes docs `user-guide/features/delegation` + `guides/delegation-patterns` (200, 2026-11-05) [built] |
| 10 | `schedule.html` | Schedule recurring jobs | Clock diagram | Hermes docs `user-guide/features/cron` + `guides/automate-with-cron` (200, 2026-11-05) [built] |
| 11 | `delivery-flow.html` | Run one delivery: spec → plan → build → independent review → merge | Delivery pipeline | One-PR flow: CT INTENT.md "How changes are made" §one-PR sentence ONLY (ct-INTENT.md:324-326) [built]; that section's named-model review sentence is STALE the same way CTI CONTRIBUTING is — do not cite either for the review step; review stage grounded on EA's real ladder via private fact-check (D2 allows showing it), taught generically as "independent review before merge" |
| 12 | `team-memory.html` | Outgrow one brain: team AI memory at SynapseTree.dev | Local brain (one per person) → SynapseTree cloud hub → team's shared memory | SynapseTree's OWN product copy only, labeled as the product's description (cloud memory & sync hub; teams start with the MCP server; Free tier + Pro $29/mo — generally available, verified live 2026-11-05) [vendor-description]; page states plainly that local CT is one brain per vault (ct-INTENT.md:264) [built] and does NOT claim automatic local→cloud sync (CT's push path is checked at build against CT docs before any mention) |
| 13 | `links.html` | The link directory: where everything lives | (Link list; icon accents only) | every target re-verified by the checker |

**Built-vs-intent rule (Opus T3 M2, extended per Fable M4):** every grounding
source in the page map is marked `[built]` (behavior that exists today and
may be taught), `[intent]` (a stated direction — only as a clearly-labeled
"where this is heading" aside, never as how things work), or
`[vendor-description]` (what a product's own copy claims about itself —
taught as the product's description, never as verified behavior). Pages
teach only `[built]` behavior; INTENT files are cited only for claims their
own Built status confirms. Pages 4/6/7/9/10 are grounded on the UPSTREAM
Hermes docs (what a newcomer installs); the sign-off table's compat receipt
records any EA-deployment divergence found at build.

Every one of the 13 page-map files carries `data-topic="<page-map #>"`
(`index.html` included, topic `1`); `tools/check_site.py` fails the check if
any page's topic attribute is missing or duplicated. **The checker's manifest
covers exactly those 13 files** — the Search Console verification file (a
single Google-generated `<hash>.html`) and any other site-root HTML file not
in the manifest is excluded from the manifest, footer-identity, and analytics
checks by the manifest rule itself (it is still deployed).

Shared assets: `site/css/style.css` (single stylesheet, light palette, large
margins), footer block duplicated per page (no build step, so no includes —
kept identical by `tools/check_site.py`), `LICENSE`, `README.md`,
`.github/workflows/pages.yml` (upload `site/` only, deploy on push to
`main`), `.github/workflows/check.yml` (runs `tools/check_site.py` on PRs
and on a schedule — plus the post-deploy boundary check: fetch the published
URL's `/specs/...` path and assert 404; that check runs on `schedule` and
after `pages.yml` completes via `workflow_run`, skipped on `pull_request`,
where the published site is still the old deploy), `tools/check_site.py`
(dev-only checker: link check, footer diff, `data-topic` manifest check,
step counting, SVG presence, structural check, strict HTML parse),
`tools/requirements-dev.txt` (`html5lib` pin for the checker).

### Sign-off table (the manual gates)

The 13-row sign-off table is a separate checklist kept next to the page map
(`specs/company-in-a-box-tutorial/signoff.md`, added to Files touched) and
initialed at test time, with one row per page and four columns:

1. **Topic match** — reviewer initials confirming the page's content matches
   exactly its page-map row (the machine only checks the label; this human
   gate checks the content).
2. **Redaction checked** — checkbox stated VERBATIM as the loosened rule:
   "no secrets, credentials, client material, or vault-internal paths; EA's
   real practice and agent identity may be shown" (D2/D8). Enforced
   mechanically too: the checker greps `site/` for `/home/` paths,
   `immutable-source-files`, and key/token patterns and fails on any hit.
3. **Grounding receipts** — for every command, interface, AND practice claim
   on the page: the source (URL or repo file, or for private fact-checks the
   form "vault fact-check, date, checker" with no path) it was checked
   against, with the date checked. This is how INTENT.md rule 4 is enforced:
   no receipt, no sign-off. Pages 4/6/7/9/10 additionally carry a compat
   receipt: upstream-docs behavior confirmed against the version a newcomer
   would install.
4. **Terms defined** — reviewer initials confirming every tool-specific term
   was defined at first use. INTENT.md rule 5 is enforced as recorded
   reviewer judgment here, not by a machine check.

Re-sign rule: any change to a page re-signs that page's row (all four
columns) before merge; no blanket re-signs.

### Content commitments

- Every external link targets a verified-live URL: curated-thoughts repo,
  curated-thoughts-integrations repo, upstream hermes-agent repo
  (`NousResearch/hermes-agent`) + Hermes docs, synapsetree.dev,
  equationalapplications.com — every one re-verified by the checker on every
  run (EA's fork is linked nowhere in the tutorial; only upstream is).
- **Grounding mandate (Kurt, 2026-11-05):** every command, configuration
  interface, and practice the tutorial teaches must be checked against the
  named source in the page map's "Grounded against" column (the tools' real
  docs/repos and EA's actual Tessera configuration) before it is written.
  Reviewers on the ladder are briefed to verify against the real setup, not
  plausibility. Goals: accuracy, clearness, friendliness.
- **Redaction rule (private sources, loosened per decision-log D8):** EA's
  private vault material is consulted for ACCURACY only — and the rule bans
  exactly what INTENT.md's non-goal bans: secrets, credentials, client
  material, and vault-internal paths never appear. EA's public agent
  identity (Tessera) and EA's real practice MAY be shown openly — that is
  the CEO's founding ruling (D2: "Tessera is the model, not just the
  author"), which no review finding may narrow. Public repos' INTENT.md /
  CONTRIBUTING files and the tools' public docs are the citable sources;
  the private vault is the fact-checker, never the source. The 13-row
  sign-off table includes a redaction checkbox per page.
- The worked example is honest: describes EA's real practice (memory sidecar,
  spec-driven delivery flow, review ladder, scheduled jobs) at the level a
  newcomer can copy; no secrets, no client material.
- Plain-language voice; every EA/agent term defined at first use.
- MIT license file ships (already on `main`); footer states MIT + attribution.

### Analytics (Kurt ruling, 2026-11-05: option 1)

- **GoatCounter** — free hosted service "for reasonable public usage"
  (personal sites and small-to-medium businesses fine). Captured verbatim
  from https://www.goatcounter.com on 2026-11-05: "GoatCounter.com is
  currently offered for free for reasonable public usage. Running your
  personal website or small-to-medium business on it is fine, but sending
  millions of pageviews/day isn't." Cookieless; their copy: "adds just
  ~3.5KB of extra data to your site" (same page, same date). Single script
  tag per page. GoatCounter states it "doesn't need a GDPR notice" (their
  privacy design: no cookies, no personal-data tracking) — that is the
  vendor's claim plus our assessment, not a legal opinion; if this ever
  matters commercially, flag for counsel. A JavaScript-free pixel is the
  documented fallback if we ever want zero scripts.
- **Google Search Console** — ownership verified by a single HTML verification
  file in `site/`; no page scripts.
- GA4 explicitly rejected: heavy JS + cookie-consent baggage conflicts with
  the site's privacy posture and INTENT.md rule 6.

### Alignment with INTENT.md

The spec serves INTENT.md directly: it operationalizes the central design
intent (small bites, white space, few steps per page, infographics widely,
overview-only landing — the page map gives every page exactly one topic,
machine-checked for label integrity and human-signed for content), follows
all seven rules with honest enforcement claims (analytics honors rule 6;
rule 4 is enforced through the sign-off table's grounding receipts plus the
redaction rule, which operationalizes the no-private-contents non-goal for
the grounding workflow; rule 5 is enforced as recorded reviewer judgment in
the same table). No departures from INTENT.md; INTENT.md itself is unchanged
by this spec.

## Files touched

- `INTENT.md`, `AGENTS.md` (added by this PR; the spec does not change their
  content)
- `.github/workflows/check.yml`
- `site/index.html`, `site/the-pattern.html`, `site/the-three-tools.html`,
  `site/setup-hermes.html`, `site/setup-memory.html`,
  `site/connect-memory.html`, `site/first-integration.html`,
  `site/procedures.html`, `site/delegate.html`, `site/schedule.html`,
  `site/delivery-flow.html`, `site/team-memory.html`, `site/links.html`
- `site/css/style.css`
- `.github/workflows/pages.yml` (uploads `site/` only)
- `README.md`, `LICENSE` (license already on main; README added by this PR)
- Search Console verification HTML file (`site/`; added at implementation)
- `tools/check_site.py`, `tools/requirements-dev.txt` (added at
  implementation)
- `specs/company-in-a-box-tutorial/signoff.md` (the sign-off checklist)

Scope note: this PR is the one-PR lifecycle — the spec lands first (this
branch), and `site/`, `tools/`, the workflow, and `README.md` are added on
this same branch after the plan gate. "This PR" in this document means the
full branch, not its current commits.

## Test plan

1. **HTML validity** — every MANIFEST page (the 13 page-map files — all
   checker tests 1–3 are scoped to exactly these) parses clean under
   `html5lib` in strict mode (dev-only dependency; raises on malformed
   markup — `html.parser` is lenient and passes broken tags; the Google
   verification file, which has no doctype, is outside this scope), plus a
   structural check (single `<h1>`, `<title>`, viewport meta present).
2. **Link check** — `tools/check_site.py` walks the 13 manifest pages: every
   internal `href` resolves to an existing file/anchor; every external URL is
   checked from Python (`urllib` with a real browser user-agent — no curl
   binary dependency, GET fallback, 2 retries). Classification: 404 and DNS
   resolution failure are HARD FAILURES; 410 (gone) is a hard failure after
   one retry; 429/5xx/403/401/timeouts/connection errors are WARNINGS that
   ESCALATE to failures if the same URL warns on 3 consecutive scheduled
   runs (an expired domain can't hide forever). The checker runs on PRs and
   as a scheduled job — it is NOT a step in the Pages deploy workflow, so
   deploys never gate on third-party availability. Footer check: all 13
   footers byte-identical AND each contains the `equationalapplications.com`
   link and the MIT statement (identity alone could pass a footer that is
   uniformly missing the attribution).
3. **Design-law check** — each non-landing page's numbered steps ≤ 5; each
   page contains at least one inline SVG where the page map promises one;
   **single-topic check** — mechanical part: `tools/check_site.py` verifies
   every page's `data-topic` attribute against the page-map manifest (missing
   or duplicated topic = failure); human part: the reviewer initials the
   13-row table confirming content matches its topic. The Alignment section
   therefore claims a machine-checked topic manifest PLUS a manual
   sign-off — not a fully automated guarantee.
4. **Analytics check** — each manifest page contains EXACTLY ONE `<script>`
   element and it is the GoatCounter tag; inline scripts, `on*` handlers,
   and scripts inside SVGs all count and fail the check; non-manifest root
   HTML files (e.g. the Search Console verification file) are asserted to
   contain no `<script>` at all. The checker also FAILS while the
   GoatCounter site code is still a placeholder (a placeholder tag must
   never reach the live site). SRI pinning or self-hosting the counter
   script is decided at implementation.
5. **Visual check** — render each page in the local browser over CDP and
   screenshot; confirm white space, readable hierarchy, SVGs render.
6. **Deploy check** — Pages workflow run green on `main` after merge; the
   published site URL serves all 13 pages (fetch each, expecting 200 —
   `/index.html` returning 200 proves the site is actually published);
   `https://<site>/specs/company-in-a-box-tutorial/spec.md` returns 404
   (paired with the index-200 check so an unpublished site can't pass
   vacuously). The boundary check's `workflow_run` job runs only after a
   SUCCESSFUL deploy conclusion. Note: GitHub disables scheduled workflows
   after 60 days of repo inactivity — the scheduled link/topic checks are
   best-effort maintenance; PR-time checks are the primary gate.

## Open questions for Kurt

- **GoatCounter account** (m7): the analytics script needs an account and a
  site code (`https://<code>.goatcounter.com/count`). Who creates it — you,
  or shall I prepare everything and you just click the signup confirmation?
  The script can be written and merged with a placeholder code until then.
- **Tessera naming confirmed open** (M4/D8): the spec treats Tessera as
  nameable (D2), and D8 now records that explicitly — shout if you want it
  otherwise.
- **Sign-off table signer** (Fable m8): 52 manual cells (13 pages × 4
  gates) need an accountable initial. Proposal: Tessera signs each row at
  test time and YOU review the completed table at the merge gate — Kurt
  initialing 52 cells is not sustainable. Confirm or override.

(Default decisions taken: repo name `company-in-a-box-tutorial` per approved
option 1; Pages deployed from the `site/` directory via Actions; no custom
domain.)
