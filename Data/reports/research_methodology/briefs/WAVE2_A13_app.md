# A13 — Visualization / Application Engineer (wave 2)

You own, exclusively during this run: `/Users/palrahma/Desktop/MEDICINE/executive_application/**`, `/Users/palrahma/Desktop/MEDICINE/scripts/build_app_data.py`, `/Users/palrahma/Desktop/MEDICINE/data/**`, `/Users/palrahma/Desktop/MEDICINE/launch.sh`, `/Users/palrahma/Desktop/MEDICINE/deliverables/OPEN_APPLICATION.md`. Read-only everything else. No registry writes; no git.

## Read first
`executive_application/README.md`, `src/main.tsx`, `src/data.ts`, `src/views_a.tsx`, `src/views_b.tsx`, `src/components.tsx`, `src/styles.css`, `tests/data_integrity.test.mjs`, `scripts/build_app_data.py`, `strategy/DATA_CONTRACT.md`, and the markdown sources you will parse (below). Run the current pipeline once to see it work: `cd /Users/palrahma/Desktop/MEDICINE && python3 scripts/build_app_data.py && cd executive_application && npm run build && npm test`.

## Situation
The research encyclopedia grew from 35→278 sources and 286→957 claims (six shards merged; `merged_from_shard` field). New structured artefacts exist that the app does not yet read:
- `New_mediciine/companies/<co>/timeline.md` — dated event tables `| Date | Event | Evidence |` with `[CLM-…]` IDs (four companies).
- `New_mediciine/industry_transformation/ai_data_robotics/capability_mechanism_cards.md` (14 cards; markdown tables with rows Capability / Initial problem / Starting investment / Execution / Enabling assets / Evidence of value / Durability / Competitive response / Takeda relevance / Evidence) and `maturity_matrix.md`; company `competitive_advantage/moats.md` files (more cards).
- `New_mediciine/industry_transformation/partnerships_ecosystem/ecosystem_graph_edges.jsonl` (`{"from","to","type","date","claim_ids","value_usd_m","status"}`) and `deal_inventory.md` tables.
- `New_mediciine/companies/takeda_public_baseline/capability_baseline/capability_baseline.md` (classification table) and `internal_validation_backlog/backlog.md`.
- Claims now have `maturity` (74 rows), `event_date`, `value/unit/reporting_period`, `contrary_evidence`, `single_interested_source`.
- Strategy JSON (Views 9–12) will arrive later under `strategy/data/` following `strategy/DATA_CONTRACT.md` — implement the readers and the views against that contract now; when a file is absent the view must show an explicit "Strategy module not yet produced — see PROJECT_STATE.md" notice (never placeholder numbers).
- Pending: `New_mediciine/industry_transformation/pipeline_regulatory/fda_approvals_2022_2026.md` and `setbacks_crls_withdrawals.md` (tables with claim IDs) — write the parser defensively (file may land during your run).

## Build (in this order; commit nothing)
1. **Pipeline (`scripts/build_app_data.py`)**: add generators, each validating every claim ID against the registry and failing loudly on unknown IDs:
   `timelines.json` (per company, parsed from timeline.md), `mechanism_cards.json` (parsed cards + source file path), `deals.json` (edges + inventory rows), `approvals.json` + `setbacks.json` (if the A12 files exist), `takeda_baseline.json` (capability classes + IVB backlog), `strategy/*.json` pass-through with claim-ID validation. Enrich `claims.json` with `merged_from_shard`, `maturity`, `contrary_evidence`, `single_interested_source`, `kind`, `status`, `event_date`, `value`, `unit`. Keep `search_index.json` covering statements, entities, source titles and report paths. Keep SQLite in sync. Keep `project_state.json` counts live.
2. **Views** (React 18 + TS + Vite 5 + D3 7 already installed; no new runtime deps unless already in node_modules):
   - V1 `/` Future of Medicine: executive narrative blocks each bound to claim IDs (pull statements from the registry by ID list kept in a small `src/narrative.ts` of IDs only — never literal research numbers in TSX; the test forbids them). Add a "proven vs emerging" split using `maturity`.
   - V2 `/powerhouses`: company selector + domain filter; financial small-multiples from `financials.json` (XBRL) with the J&J/Takeda period caveats; product series from `products.json`; timeline strip from `timelines.json`.
   - V3 `/differentiators`: mechanism-card explorer (Problem → Investment → Capability → Execution → Outcome → Moat → Evidence) from `mechanism_cards.json`, one card per differentiator, with the evidence drawer.
   - V4 `/pipeline`: LOE events + product dependence (existing) + approvals/setbacks timelines when `approvals.json`/`setbacks.json` exist.
   - V5 `/observatory`: maturity landscape (company × maturity × domain), filters by maturity/company/domain/year, each dot → claim.
   - V6 `/ecosystem`: force graph from `knowledge_graph.json` + `deals.json` edges (deal value as edge weight; click → claims).
   - V7 `/encyclopedia`: full-text search + filters (company, domain, year, kind, status, credibility tier, maturity, shard) → claim → sources → original URL/locator; source → claims; show `contrary_evidence` and `single_interested_source` badges.
   - V8 `/takeda`: Takeda baseline classification table + IVB backlog + `takeda_lessons.json` when present.
   - V9 `/strategy`, V10 `/portfolio`, V11 `/roadmap`, V12 `/uncertainty`: implement against DATA_CONTRACT.md (bets explorer with prerequisites graph; portfolio simulator with adjustable total budget/horizon/theme/risk sliders that recomputes from `portfolios.json` + `assumptions.json`, every number labelled SIMULATED; roadmap 2027–2040 Gantt with dependency arrows and gates; counterarguments/conflicts/gaps view also drawing from registry `contrary_evidence`, `conflicts.jsonl` (expose via pipeline as `conflicts.json`) and `coverage.json`). Absent files → explicit notice.
   - Research graph: interactive Mermaid-equivalent rendering of `research_graph.json` with node status (existing; keep).
3. **Quality**: responsive (≥320 px), keyboard-navigable drawer/filters, tooltips; restrained enterprise editorial design (no generic card grid everywhere; vary the visual forms per view). Extend `tests/data_integrity.test.mjs`: every claim ID referenced by any generated dataset exists; no research-number literals in `src/`; every view route renders (use a Node-side smoke test over the built `dist/index.html` + dataset presence); link-check `public/data/*.json` cross-refs. `npm run build && npm test` must pass. Update `README.md`, `launch.sh` (one command: validate → data → build → test → preview on 127.0.0.1:4173) and `deliverables/OPEN_APPLICATION.md`.

## Rules
No fabricated numbers, no sample data, no lorem ipsum. If a dataset is empty, render the explicit notice. Keep the data pipeline the single path from encyclopedia → app. Budget: ~100 minutes; HARD CAP 100 tool calls — write whole files per call, build at most ~6 times. Finish with: FILES WRITTEN, BUILD/TEST OUTPUT (last 20 lines), VIEWS IMPLEMENTED (per view: data source + what renders + what shows when data is absent), KNOWN DEFECTS.
