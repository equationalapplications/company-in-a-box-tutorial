# Spec — company-in-a-box-tutorial static site

Status: Draft
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
- Hermes Agent's public docs exist: https://hermes-agent.nousresearch.com/docs
- SynapseTree.dev is live (fetched 2026-11-05) and positions itself as the
  hosted, team-shared memory of the same family — the correct "next step when
  you have a team" destination the tutorial should point at.
- EA's internal delivery flow / procedures live in the private vault
  (`~/Documents/equational-wiki/.../procedures/`) — no public equivalent.

## Proposed change

Build a multi-page, no-build-step static site (plain HTML + CSS + hand-authored
inline SVG infographics), MIT licensed, with "Made with love" attribution back
to EA on every page, deployed on GitHub Pages from the repo root.

### Design law (from INTENT.md central intent)

- Landing page = overview: what it is, why to use it. Nothing else competes
  with it.
- Each following page teaches ONE small thing in a few steps (target: ≤ 5
  numbered steps per page).
- Generous white space; no dense multi-column text walls.
- Infographics used widely (one per page minimum where a concept can be drawn).
- No JavaScript required to learn from the site (static pages only).

### Page map (11 pages + shared assets)

| # | File | Teaches | Infographic |
|---|------|---------|-------------|
| 1 | `index.html` | Overview: what a software company in a box is; why use it; the three tools at a glance; link to start | Box diagram: you + memory + integrations + agent = a company |
| 2 | `the-pattern.html` | The pattern: one person, agent roles (executive, workers, reviewers), procedures, memory | Org-chart: you → executive agent → delegated workers |
| 3 | `the-three-tools.html` | Meet Curated Thoughts (memory), Curated Thoughts Integrations (wiring), Hermes Agent (the doer) | Three-tool triangle feeding one company |
| 4 | `setup-hermes.html` | Step 1: install Hermes Agent, first run | Install flow: prompt → profile → agent |
| 5 | `setup-memory.html` | Step 2: install Curated Thoughts; the brain + vault idea | Brain/vault diagram: durable notes → embeddings → recall |
| 6 | `connect-memory.html` | Step 3: register Curated Thoughts as the agent's MCP memory server | Agent ↔ sidecar ↔ vault wiring |
| 7 | `first-integration.html` | Step 4: pick and install a first integration from curated-thoughts-integrations | Hub-and-spoke: vault at center, tools connected |
| 8 | `procedures.html` | Step 5: give the company standing rules — INTENT.md, procedures, skills | Rule stack: intent → procedures → skills |
| 9 | `put-to-work.html` | Step 6: put the company to work — delegation, scheduled jobs, a delivery from spec to merge | Delivery pipeline: spec → plan → build → review → merge |
| 10 | `team-memory.html` | Step 7: outgrow one brain — team AI memory at SynapseTree.dev | One vault → cloud sync → team agents |
| 11 | `links.html` | All repos, docs, websites, license, attribution | (Link list; icon accents only) |

Shared assets: `css/style.css` (single stylesheet, light palette, large
margins), footer partial duplicated per page (no build step, so no includes —
kept identical by the link-check/consistency script), `LICENSE`, `README.md`,
`.github/workflows/pages.yml` (deploy repo root to GitHub Pages on push to
`main`).

### Content commitments

- Every external link targets a verified-live URL: curated-thoughts repo,
  curated-thoughts-integrations repo, hermes-agent repo, Hermes docs,
  synapsetree.dev, equationalapplications.com.
- The worked example is honest: describes EA's real practice (memory sidecar,
  spec-driven delivery flow, review ladder, scheduled jobs) at the level a
  newcomer can copy; no secrets, no client material.
- Plain-language voice; every EA/agent term defined at first use.
- MIT license file ships (already on `main`); footer states MIT + attribution.

## Files touched

- `INTENT.md`, `AGENTS.md` (this branch, already drafted)
- `index.html`, `the-pattern.html`, `the-three-tools.html`, `setup-hermes.html`,
  `setup-memory.html`, `connect-memory.html`, `first-integration.html`,
  `procedures.html`, `put-to-work.html`, `team-memory.html`, `links.html`
- `css/style.css`
- `.github/workflows/pages.yml`
- `README.md`, `LICENSE` (license already on main; README added by this PR)

## Test plan

1. **HTML validity** — every page passes Python `html.parser` without error
   (no unclosed tags), plus a structural check (single `<h1>`, `<title>`,
   viewport meta present).
2. **Link check** — script walks all pages: every internal `href` resolves to
   an existing file/anchor; every external URL returns HTTP < 400 (curl HEAD,
   with GET fallback); footer identical on all 11 pages (diff check).
3. **Design-law check** — each non-landing page's numbered steps ≤ 5; each
   page contains at least one inline SVG where the page map promises one.
4. **Visual check** — render each page in the local browser over CDP and
   screenshot; confirm white space, readable hierarchy, SVGs render.
5. **Deploy check** — Pages workflow run green on `main` after merge; the
   published site URL serves all 11 pages (verify by fetching each).

## Open questions for Kurt

- None blocking. (Default decisions taken: repo name `company-in-a-box-tutorial`
  per approved option 1; Pages deployed from repo root via Actions; no custom
  domain.)
