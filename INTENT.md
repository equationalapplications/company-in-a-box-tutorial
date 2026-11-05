# INTENT — company-in-a-box-tutorial

**Read this file first.** It explains why this repo exists, the rules the
tutorial must follow, and what it deliberately does not do. It is written for
people first: a product owner should be able to read it and recognize the
product they want. Any agent writing a spec must check the spec against it.
If this file and another document disagree, this file wins on *intent* (what
we are trying to do) and the specs win on *detail* (exactly how).

This file says what the product should do, not how far it has got. What is
built today is recorded in the README and the specs. Change this file only
when the intent changes.

## Why this repo exists

Equational Applications (EA) runs a working **software company in a box**:
one human owner (the CEO) plus AI agents holding executive, worker, and
reviewer roles, with durable memory in **Curated Thoughts**, tool wiring in
**Curated Thoughts Integrations**, and **Hermes Agent** as the runtime. The
knowledge of how the pieces fit together lives only inside EA's private
vaults. A newcomer who wants to replicate the pattern has no single teaching
artifact.

This repo holds that artifact: a free, open-source (MIT), static HTML
tutorial site that teaches a brand-new user how to assemble the same kind of
company — EA's real practice as the worked example, the generic pattern as
the lesson. When the reader outgrows one person's brain and wants a *team's*
AI memory, the tutorial points them to
[SynapseTree.dev](https://synapsetree.dev), the hosted member of the same
memory family.

## The central design intent

> This is dense learning material for a new user. Give it to them in small
> bites. Pages with lots of white space. The landing page is an overview —
> what it is, why to use it. The next pages are simple, with just a few steps
> per page, to not overwhelm the user. Infographics used widely.

(Kurt VanDusen, CEO, when founding the repo — 2026-11-05.)

This is the repo's core intent. Every design decision is judged against it:
if a change adds density, removes white space, crams many steps onto one
page, or replaces a clear infographic with a wall of text, it is wrong for
this repo unless this intent is amended deliberately and in the open, via PR.

## Rules the tutorial must follow

1. **Small bites.** The landing page teaches only the overview. Every other
   page teaches one small thing in a few steps (target: five or fewer
   numbered steps per page).
2. **Breathing room.** Generous white space; no dense multi-column walls of
   text.
3. **Show, don't prose.** Infographics used widely — where a concept can be
   drawn, it is drawn.
4. **Accuracy over plausibility.** Every command, interface, and practice
   shown must be checked against the tools' real documentation and EA's real
   running setup. If EA doesn't actually do it, the tutorial doesn't say it.
5. **Plain language.** Every tool-specific term is defined in ordinary words
   at first use.
6. **No JavaScript required to learn.** The site is plain HTML/CSS/SVG with
   no build step; analytics stays a single cookieless script.
7. **Attribution and openness.** MIT licensed; every page carries a "Made
   with love" link back to EA and links to the relevant repos, docs, and
   websites.

## What this repo deliberately does not do

- **Not tool documentation.** The tools' own docs own their reference
  material; this site teaches how they compose.
- **Not a marketing site.** It teaches; product and pricing questions link
  out.
- **No frameworks, no bundler.** A newcomer can read the site's source as
  easily as its prose.
- **No secrets, no client material.** EA's private vault contents, customer
  work, and credentials never appear here.

## How changes are made

Spec first, then plan, then implementation, on one pull request per change
cycle (`specs/<name>/`); every spec carries an "Alignment with INTENT.md"
section; INTENT.md changes only when a person changes the product's intent.
