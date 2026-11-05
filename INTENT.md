# INTENT.md — company-in-a-box-tutorial

## What this IS

A free, open-source (MIT), static HTML tutorial site that teaches a brand-new
user how to assemble a **software company in a box**: a one-person software
company where AI agents do the company's work, built from three tools —

1. **Curated Thoughts** — the company's memory (a durable, curated knowledge
   vault with a local MCP sidecar any agent can consult).
2. **Curated Thoughts Integrations** — the open-source collection that wires
   that memory into the rest of the tool ecosystem.
3. **Hermes Agent** — the company's doer: the agent runtime that holds the
   role, follows procedures, delegates, schedules, and delivers.

Equational Applications (EA) is the worked example: EA runs exactly this setup
for real, with an executive agent (Tessera) operating a software company. The
tutorial teaches the generic pattern using EA's real practice as evidence.

When the reader outgrows one person and wants a *team's* AI memory, the
tutorial points them to [SynapseTree.dev](https://synapsetree.dev) — the same
memory family, hosted and shared.

## Central intent (Kurt, 2026-11-05)

> This is dense learning material for a new user. Give it to them in small
> bites. Pages with lots of white space. The landing page is an overview —
> what it is, why to use it. The next pages are simple, with just a few steps
> per page, to not overwhelm the user. Infographics used widely.

This ruling is the repo's core intent. **Every design decision in this repo is
judged against it**: if a change adds density, removes white space, crams many
steps onto one page, or replaces a clear infographic with a wall of text, it
is wrong for this repo unless the intent file itself is amended (deliberately
and in the open, via PR).

## Non-goals

- Not documentation of any single tool (the tools' own docs own that).
- Not a marketing site (it teaches; it links out for products and pricing).
- Not a build-step site: no framework, no bundler — plain HTML/CSS/SVG that a
  newcomer can read as easily as the tutorial's prose.
- No secrets, credentials, or EA private client material — ever.

## Attribution & license

MIT licensed. Every page carries a "Made with love" link back to
[Equational Applications](https://equationalapplications.com). The tutorial
links to all relevant repos, docs, and websites.
