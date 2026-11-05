# company-in-a-box-tutorial

**Build a software company in a box** — a free, open-source, static HTML
tutorial: how one person runs a whole software company with AI agents doing
the work, using three open-source tools (Curated Thoughts, Curated Thoughts
Integrations, Hermes Agent). Equational Applications runs exactly this setup
for real; this tutorial teaches the pattern using their practice as the
worked example.

Read it at: **https://equationalapplications.github.io/company-in-a-box-tutorial/**

## Structure

- `site/` — the tutorial (13 single-topic pages, plain HTML/CSS/SVG, no
  build step, no JS required)
- `specs/company-in-a-box-tutorial/` — this delivery's `spec.md`, `plan.md`,
  `ledger.md` (status), and `signoff.md` (accuracy sign-off table)
- `tools/check_site.py` — the site checker: strict HTML parse, internal link
  resolution, external link liveness (with warning escalation), data-topic
  manifest, step-count and SVG design-law checks, zero-or-one-script
  analytics rule, redaction grep
- `INTENT.md` — what this repo is and the rules every page and spec must
  follow (intent only — no status; status lives in the spec folder's ledger)

## Working on the site

```bash
pip install -r tools/requirements-dev.txt
python tools/check_site.py                   # offline checks
python tools/check_site.py --check-external  # + live link liveness
```

Then open `site/index.html` in a browser. Every change must pass the
checker and align with `INTENT.md` (see `AGENTS.md`).

## License

MIT — see [LICENSE](LICENSE). Made with ❤️ by
[Equational Applications LLC](https://equationalapplications.com).
