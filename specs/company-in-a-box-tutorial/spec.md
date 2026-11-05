# Spec — company-in-a-box-tutorial static site

Status: Draft (in review — Tier 1.5 ladder running)
Owner: Tessera (Equational Applications LLC)
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
  https://hermes-agent.nousresearch.com/docs (HTTP 200, 2026-11-05).
- SynapseTree.dev is live (HTTP 200, fetched 2026-11-05) and positions itself
  as the hosted, team-shared memory of the same family — the correct "next
  step when you have a team" destination the tutorial should point at.
- EA's delivery-flow procedures live in its private agent vault — no public
  equivalent exists.

## Proposed change

Build a multi-page, no-build-step static site (plain HTML + CSS + hand-authored
inline SVG infographics), MIT licensed, with "Made with love" attribution back
to EA on every page, deployed on GitHub Pages.

**Deployment boundary (review finding F2):** the Pages workflow uploads ONLY
the `site/` directory — the tutorial pages, `css/`, and the Search Console
verification file. `INTENT.md`, `AGENTS.md`, `README.md`, and `specs/` stay
repo-only (they are public on GitHub anyway, but they are not site content).
A post-deploy check asserts `https://<site>/specs/...` returns 404.

### Design law (from INTENT.md central intent)

- Landing page = overview: what it is, why to use it. Nothing else competes
  with it.
- Each following page teaches ONE small thing in a few steps (target: ≤ 5
  numbered steps per page, and exactly one topic per page — its own row in
  the page map).
- Generous white space; no dense multi-column text walls.
- Infographics used widely (one per page where the page map promises one).
- No JavaScript required to learn from the site (analytics is a single
  cookieless ~3.5KB script; a JS-free pixel is the documented fallback).

### Page map (13 pages + shared assets)

| # | File (under `site/`) | Teaches (exactly one topic) | Infographic | Grounded against |
|---|------|---------|-------------|------------------|
| 1 | `index.html` | Overview: what a company in a box is; why use it; where to start | Box diagram: you + memory + integrations + agent = a company | (links verified live) |
| 2 | `the-pattern.html` | The pattern: one person directing agent roles (executive, workers, reviewers) | Org chart: you → executive agent → delegated workers | EA's real org (Tessera); CTI INTENT.md "From one agent to a team" |
|  3 | `the-three-tools.html` | Meet the three tools, one glance each | Three-tool triangle feeding one company | CT INTENT.md; CTI INTENT.md; Hermes docs |
| 4 | `setup-hermes.html` | Install Hermes Agent and get a first response | Install flow: prompt → profile → agent | Hermes docs install section + EA's live profile |
| 5 | `setup-memory.html` | Install Curated Thoughts; the brain + vault idea | Brain/vault diagram: files → facts → recall | CT repo + EA's `curated-thoughts-installation` procedure |
| 6 | `connect-memory.html` | Register Curated Thoughts as the agent's MCP memory server | Agent ↔ sidecar ↔ vault wiring | CTI repo (Hermes integration) + Hermes MCP docs |
| 7 | `first-integration.html` | Pick and install a first integration from CTI | Hub-and-spoke: vault at center, tools connected | CTI README + `integrations/<id>/integration.yaml` docs |
| 8 | `procedures.html` | Give the company standing rules: the rule stack (INTENT.md → procedures → skills) | Rule stack diagram | EA's real INTENT/AGENTS pattern (CT + CTI repos) |
| 9 | `delegate.html` | Delegate work to agent subagents | Dispatch diagram | Hermes docs delegation + EA delivery practice |
| 10 | `schedule.html` | Schedule recurring jobs | Clock diagram | Hermes cron docs + EA cron-ops practice |
| 11 | `delivery-flow.html` | Run one delivery: spec → plan → build → review → merge | Delivery pipeline | EA `pr-spec-driven` flow + CTI CONTRIBUTING "How changes are made" |
| 12 | `team-memory.html` | Outgrow one brain: team AI memory at SynapseTree.dev | One vault → cloud sync → team agents | synapsetree.dev (verified live) |
| 13 | `links.html` | All repos, docs, websites, license, attribution | (Link list; icon accents only) | every target re-verified at build |

Shared assets: `site/css/style.css` (single stylesheet, light palette, large
margins), footer block duplicated per page (no build step, so no includes —
kept identical by the link-check/consistency script), `LICENSE`, `README.md`,
`.github/workflows/pages.yml` (upload `site/` only, deploy on push to
`main`).

### Content commitments

- Every external link targets a verified-live URL: curated-thoughts repo,
  curated-thoughts-integrations repo, hermes-agent repo, Hermes docs,
  synapsetree.dev, equationalapplications.com — all re-verified at build time.
- **Grounding mandate (Kurt, 2026-11-05):** every command, configuration
  interface, and practice the tutorial teaches must be checked against the
  named source in the page map's "Grounded against" column (the tools' real
  docs/repos and EA's actual Tessera configuration) before it is written.
  Reviewers on the ladder are briefed to verify against the real setup, not
  plausibility. Goals: accuracy, clearness, friendliness.
- The worked example is honest: describes EA's real practice (memory sidecar,
  spec-driven delivery flow, review ladder, scheduled jobs) at the level a
  newcomer can copy; no secrets, no client material.
- Plain-language voice; every EA/agent term defined at first use.
- MIT license file ships (already on `main`); footer states MIT + attribution.

### Analytics (Kurt ruling, 2026-11-05: option 1)

- **GoatCounter** — free hosted service "for reasonable public usage"
  (personal sites and small-to-medium businesses fine — verified on
  goatcounter.com, 2026-11-05). Cookieless, ~3.5KB, single script tag per
  page, no GDPR consent notice needed; a JavaScript-free pixel is the
  documented fallback if we ever want zero scripts.
- **Google Search Console** — ownership verified by a single HTML verification
  file in `site/`; no page scripts.
- GA4 explicitly rejected: heavy JS + cookie-consent baggage conflicts with
  the site's privacy posture and design law 6.

### Alignment with INTENT.md

The spec serves INTENT.md directly: it operationalizes the central design
intent (small bites, white space, few steps per page, infographics widely,
overview-only landing — the page map gives every page exactly one topic and
the test plan enforces it), follows all seven rules (analytics choice honors
rule 6; the grounding mandate implements rule 4), and respects every non-goal
(no build step, no marketing content, no tool docs duplication). No
departures from INTENT.md.

## Files touched

- `INTENT.md`, `AGENTS.md` (this branch)
- `site/index.html`, `site/the-pattern.html`, `site/the-three-tools.html`,
  `site/setup-hermes.html`, `site/setup-memory.html`,
  `site/connect-memory.html`, `site/first-integration.html`,
  `site/procedures.html`, `site/delegate.html`, `site/schedule.html`,
  `site/delivery-flow.html`, `site/team-memory.html`, `site/links.html`
- `site/css/style.css`
- `.github/workflows/pages.yml` (uploads `site/` only)
- `README.md`, `LICENSE` (license already on main; README added by this PR)
- Search Console verification HTML file (`site/`; added at implementation)

## Test plan

1. **HTML validity** — every page parses clean under `html5lib` in strict
   mode (dev-only dependency; raises on malformed markup — `html.parser` is
   lenient and passes broken tags), plus a structural check (single `<h1>`,
   `<title>`, viewport meta present).
2. **Link check** — script walks all pages: every internal `href` resolves to
   an existing file/anchor; every external URL returns HTTP < 400 (curl HEAD,
   GET fallback); footer identical on all 13 pages (diff check).
3. **Design-law check** — each non-landing page's numbered steps ≤ 5; each
   page contains at least one inline SVG where the page map promises one;
   **single-topic check**: each page's content is judged against exactly its
   page-map row at test sign-off (reviewer initials the 13-row table).
4. **Analytics check** — the GoatCounter script appears exactly once per page
   and is the only third-party script anywhere on the site.
5. **Visual check** — render each page in the local browser over CDP and
   screenshot; confirm white space, readable hierarchy, SVGs render.
6. **Deploy check** — Pages workflow run green on `main` after merge; the
   published site URL serves all 13 pages (fetch each); `specs/` and other
   repo-only paths are NOT served (404 asserted).

## Open questions for Kurt

- None blocking. (Default decisions taken: repo name `company-in-a-box-tutorial`
  per approved option 1; Pages deployed from the `site/` directory via
  Actions; no custom domain.)
