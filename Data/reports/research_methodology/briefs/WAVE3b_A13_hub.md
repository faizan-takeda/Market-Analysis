# A13 (wave 3b) — Turn the application into the final "go-to" content hub: Takeda white/red design, full report reader, pillar architecture, grounded Q&A, single-file export

You exclusively own: `executive_application/**`, `scripts/build_app_data.py`, `scripts/build_single_file.py` (new), `data/**`, `launch.sh`, `deliverables/OPEN_APPLICATION.md`. Read-only elsewhere. No registry writes. No git. `npm install` from the public registry is allowed (`marked` is available: 18.x; `minisearch` optional).

## User requirements (verbatim intent)
"Final HTML webpage with very professional and visually engaging UI and very detailed content; divide all research content very well and in detail. Clean Q&A without heavy LLMs — free / open-source LLM APIs — but Q&A is one feature; the aim is detailed, clear, best content, best visuals and analytics, amazing UI to read. Professional white background and red theme aligned to Takeda. Very clear differentiation between Commercial, R&D, future plan, etc. The web page must be the final go-to content hub."

## 1. Design system (replace the current dark/neutral theme)
- Background `#FFFFFF`; surfaces `#FAFAFA`; borders `#E5E7EB`; ink `#111827`; muted `#6B7280`.
- Takeda red primary `#E60012`; hover `#C5000F`; deep `#8F000B`; tints `#FFF1F2`, `#FDE1E4`. Red is used for structure (section rules, active nav, primary buttons, key figures), never as a background for long text.
- Company palette for charts (distinct, print-safe): Lilly `#0F766E`, J&J `#1D4ED8`, AbbVie `#7C3AED`, Takeda `#E60012`; neutral grey for industry.
- Type: headlines in a serif stack (`"Source Serif 4", "Iowan Old Style", Georgia, serif`), body in `Inter, -apple-system, "Segoe UI", sans-serif`, tabular numerals for figures; 16px base, generous line-height, max text width ~72ch, page width 1280px.
- Badges: kind (FACT solid red outline; INTERPRETATION grey; HYPOTHESIS amber; SCENARIO blue; RECOMMENDATION deep red) and maturity ladder (concept → demonstrated_outcome) rendered consistently everywhere. Claim IDs are red mono chips that open the Evidence drawer.
- Motion: subtle (150–200 ms), no decorative animation. Print stylesheet (A4, hide nav, show URLs of sources).
- Keyboard: skip-link, focus rings, drawer trap, Esc closes.

## 2. Information architecture — pillar navigation (top bar + per-pillar left sub-nav)
1. **Overview** (View 1): the story spine — What is changing → Who is winning → Why → What is defensible → What Takeda already has → Where the opportunity is → What to build → What to invest → How to execute → How to measure. Each block binds to claim IDs (from `src/narrative.ts`), KPI tiles from registry values, "proven vs emerging" split, reading guide to the pillars, and the research-integrity note (counts, audit result, cutoff).
2. **Companies**: Lilly · J&J · AbbVie — each a company page with tabs: Dossier (rendered `master_report.md`), Timeline (`timelines.json` strip + table), Business & Financials (XBRL small multiples + `business_model.md`), Pipeline, Commercial, Successes & Failures, Moats, Leadership, Evidence gaps. Plus **Compare** (View 2) and **Differentiators** (View 3).
3. **Commercial & Market Access**: A7 reports (`industry_transformation/commercial_patient/*.md`) + `cross_company_analysis/commercial_capabilities_comparison.md` when present + LOE/product dependence charts.
4. **R&D, Science & Pipeline**: A12 reports (approvals table, setbacks, late-stage snapshot, scientific platforms, quality assessment) + View 4 timelines + `rd_investment_and_productivity.md` when present.
5. **Data, AI & Robotics**: A6 reports (landscape, 14 mechanism cards, maturity matrix, autonomous-lab reality check) + View 5 Observatory.
6. **Partnerships & Ecosystem**: A9 reports + View 6 graph + `partner_ecosystem_comparison.md` when present.
7. **Policy & Regulation**: A8 reports (IRA exposure table, pledges, 340B, litigation, lobbying).
8. **Takeda Baseline**: View 8 + rendered Takeda dossier, capability baseline, LOE exposure, IVB backlog.
9. **Future Plan** (clearly separated visual language — a thin red "FORWARD-LOOKING / SCENARIO" banner on every page): Future of Pharma (7 domain files under `strategy/future_of_pharma/`), Platform analogies (`strategy/platform_moats/`), Strategic Bets (View 9), Capital Allocation (View 10), Roadmap 2027–2040 (View 11), Scenarios, Council & Red Team, Counterarguments & Uncertainty (View 12). Files may be absent while waves 3–5 run: render the explicit "not yet produced" notice.
10. **Evidence & Method**: Encyclopedia (View 7), Sources browser, Conflicts & audit (conflicts.json + `quality/citation_audits/*.md` + `quality/evaluation_results/*.md` rendered), Coverage (`coverage_summary.md`), Research operating system + research graph (interactive), Research runs & experiments log, Project state / Continue.
11. **Ask** — grounded Q&A (section 4).
Global: search box in the top bar (jumps to Encyclopedia), breadcrumb, "Evidence" drawer everywhere, footer with cutoff date, counts, and "FACT ≠ INTERPRETATION" legend.

## 3. Report reader (the content backbone)
Pipeline: bundle every Markdown file under `New_mediciine/**`, `strategy/**`, `research_methodology/**` (incl. briefs), `quality/**`, root `map.md`/`PROJECT_STATE.md`/`CONTINUE.md`/`COORDINATION.md` into `reports.json` entries `{path, title (first H1), pillar, company, section, markdown, word_count, claim_ids[], updated}`. Render with `marked` (install) in a `Reader` component: tables become responsive styled tables; `[CLM-xxxxxx]`/`SRC-xxxxxx` tokens become evidence chips; relative `.md` links route inside the app (`#/read/<path>`); a right-hand "On this page" outline; "Open source file path" shown. Every pillar page lists its reports with word counts and last-updated.

## 4. Ask — grounded Q&A without heavy LLMs
- Pipeline builds `qa_index.json`: passages = every claim (statement + implication + entities + company + domains + ids), every report section (heading + ~300-word chunk, path, pillar) and every source title. In the browser implement BM25 (own ~80-line TS or `minisearch`) with field boosts; stemming light (lowercase, strip plurals).
- Retrieval-only answer (default, always works, zero cost): top 8–12 passages → "Grounded answer" composed as cited bullets (claim statement + kind badge + company + source link), grouped by company/domain, with a "What the evidence base does not say" line when fewer than 3 strong matches, and the golden questions as suggestions. The negative test must hold: a question with no evidence returns "no evidence in the corpus", never an invented answer.
- Optional "Synthesize with an open-source LLM" toggle: provider A = **local Ollama** (`http://127.0.0.1:11434/api/chat`, model default `qwen2.5:3b`, OpenAI-compatible path also fine), provider B = any OpenAI-compatible endpoint (base URL + key entered by the user, stored only in localStorage; e.g. Groq/HF free tiers). Status pill checks `/api/tags`. Strict grounding prompt: "Answer only from the numbered evidence passages; cite [CLM-…]; if the passages do not answer, say so"; temperature 0; stream tokens; show the retrieved passages beneath the answer; label "LLM synthesis — verify against the cited claims". Fallback to retrieval-only when unreachable, with one-line setup instructions (`brew install ollama && ollama pull qwen2.5:3b && ollama serve`). The Director is installing Ollama in parallel; do not install anything yourself. Never send anything except the question and retrieved passages.

## 5. Single-file export
`scripts/build_single_file.py`: after `vite build`, inline CSS/JS and every `public/data/*.json` into one `deliverables/MEDICINE_2040_Hub.html` (data as `<script type="application/json" id="medicine-data">` or `window.__MEDICINE_DATA__`); `src/data.ts` must prefer the inlined data when present and fall back to `fetch`. Hash routing must work from `file://`. Target < 15 MB; report the size. Keep the served build (`./launch.sh` → 127.0.0.1:4173) as the primary path.

## 6. Quality bar
`npm run build && npm test` green; extend tests: reports.json covers ≥ 95 Markdown files, every claim chip id exists, every pillar route renders, Q&A negative test (query "TuneLab revenue 2025" yields the no-evidence state), single-file HTML exists and contains the data blob. Responsive check at 360px and 1280px by dumping the rendered markup (no visual tools available). Update `README.md`, `launch.sh` (validate → data → build → test → single-file → preview; starts Ollama if installed and not running) and `deliverables/OPEN_APPLICATION.md` (how to open both the served app and the single HTML; how to enable the LLM option).

## Priorities if the budget tightens (400 tool calls)
(1) theme + pillar IA + reader/reports.json → (2) Q&A retrieval → (3) single-file export → (4) LLM option → (5) tests/docs. Write whole files per call; build ≤ 10 times. Finish with: FILES WRITTEN / BUILD-TEST OUTPUT / PILLAR → ROUTE → DATA map / Q&A design summary / SINGLE-FILE size / KNOWN DEFECTS.
