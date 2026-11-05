# Plan — company-in-a-box-tutorial static site

Status: Approved by Kurt 2026-11-05 (with the D11 SDD-folder-pattern ruling).
Owner: Tessera
Date: 2026-11-05
Spec: [spec.md](spec.md) (ladder-complete, approved 2026-11-05)

## Principles for this build

- One commit per deliverable; the branch never has a broken intermediate
  state (checker exists before pages do).
- Every page: valid HTML5, single `<h1>`, `data-topic="<row #>"`, one inline
  SVG infographic, ≤5 top-level `<ol>` steps, footer with EA "Made with ❤️"
  link + MIT statement, **zero `<script>` tags** until a real GoatCounter
  code exists.
- Each page commit carries its grounding receipts (sources + dates) in the
  commit message; `signoff.md` rows are filled as pages land, then signed by
  a non-author reviewer before merge.

## Steps

1. **Checker first** — `tools/check_site.py` (link check w/ urllib + UA +
   retries + warning classes, footer identity+content diff, `data-topic`
   manifest vs page map, total-`ol`-steps ≤5 counter, exactly-one-or-zero
   script rule, SVG presence, structural checks, html5lib strict parse,
   redaction grep + gitleaks hook) and `tools/requirements-dev.txt`
   (`html5lib`, `gitleaks` pinned). Verify the checker RUNS green against
   an empty `site/` (manifest-absent = skip, not fail).
2. **`check.yml`** — PR + schedule + `workflow_run` boundary check
   (post-deploy: `/index.html` 200, `/specs/company-in-a-box-tutorial/spec.md`
   404).
3. **Design system** — `site/css/style.css`: light palette, max-width
   ~72ch content column, large margins, generous line-height, step-list
   styling, SVG figure styling. No frameworks.
4. **Pages in page-map order** (index → the-pattern → the-three-tools →
   setup-hermes → setup-memory → connect-memory → first-integration →
   procedures → delegate → schedule → delivery-flow → team-memory →
   links). One commit each: write against the spec's "Grounded against"
   source, fill its `signoff.md` grounding-receipts row, run the checker.
   CT citations pinned to section headings @ `33fb4fd70494`.
5. **Sign-off** — after all 13 rows have receipts: dispatch a non-author
   reviewer subagent to sign topic/redaction/terms columns; compat receipts
   for pages 4/6/7/9/10 (upstream docs vs a fresh upstream install's
   behavior); resolve or cut any divergence (blocks sign-off).
6. **Deploy** — `.github/workflows/pages.yml` (upload `site/` only); verify
   workflow green, fetch all 13 URLs, boundary 404 assert.
7. **README.md** — repo overview, local checker instructions, license +
   attribution. (Search Console verification file: added when Kurt creates
   the GSC property; GoatCounter tag: follow-up commit after signup.)

## Test execution

After every page commit: `python tools/check_site.py` locally. After step 4:
full checker + html5lib strict + CDP screenshot of all 13 pages (visual
check per spec test 5). After step 6: live-URL fetches per spec test 6.

## Out of scope here

Analytics tag (awaits GoatCounter account), Search Console file (awaits
property creation), custom domain (rejected by default).
