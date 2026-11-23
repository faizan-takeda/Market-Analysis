# New_mediciine — research encyclopedia map (state 2026-11-21, session 2 close; unchanged by the session-3 film, which only reads these registries)

The encyclopedia is the system of record; the application is a view over it. Everything here is ID-addressed (`SRC-######`, `CLM-######`); statements are immutable, amendments carry an `audit_history`.

## Layout
| Folder | Contents | State |
|---|---|---|
| [evidence_library/](evidence_library/) | `source_registry.jsonl` (**524**), `claims_registry.jsonl` (**1,401**), `conflicts.jsonl` (110 records: audit proposals, amendments, status adjustments), `source_aliases.jsonl`, [schemas/](evidence_library/schemas/) (canonical) and [schema/](evidence_library/schema/) (shard CLI), [shards/](evidence_library/shards/) (12 agent shards, all merged), `staging/` (session-1 batches), `raw_documents/` (git-ignored), [extracted_text/](evidence_library/extracted_text/) (115 files incl. 20 annual reports FY2021–25), [links_and_metadata/](evidence_library/links_and_metadata/) (EDGAR inventories), `conflicts_proposed_A10*.jsonl` (auditor proposals, applied) | complete for this session |
| [companies/eli_lilly/](companies/eli_lilly/map.md) | dossier **v1.1** (22 sections, mechanism cards), timeline, business, pipeline, commercial, successes/failures, moats, leadership, evidence gaps, XBRL table, CT.gov inventory | Gate 1 **PASS** |
| [companies/johnson_johnson/](companies/johnson_johnson/map.md) | dossier v1.1 incl. `robotics_automation/medtech_robotics_status.md` | Gate 1 CONDITIONAL PASS (repairs applied) |
| [companies/abbvie/](companies/abbvie/map.md) | dossier v1.1 (5 mechanism cards) | Gate 1 CONDITIONAL PASS (repairs applied) |
| [companies/takeda_public_baseline/](companies/takeda_public_baseline/map.md) | baseline v1.1: financials, LOE, pipeline, R&D model, data/AI, manufacturing, commercial, leadership, [capability_baseline](companies/takeda_public_baseline/capability_baseline/capability_baseline.md) (16 areas classified), [internal_validation_backlog](companies/takeda_public_baseline/internal_validation_backlog/backlog.md) (14 items), business model, successes/failures | Gate 2 PASS; Gate 1 repairs applied, re-audit pending |
| [industry_transformation/ai_data_robotics/](industry_transformation/ai_data_robotics/map.md) | landscape, 14 capability mechanism cards, maturity matrix, autonomous-lab reality check | A6 ACCEPT |
| [industry_transformation/partnerships_ecosystem/](industry_transformation/partnerships_ecosystem/map.md) | deal inventory (audited 10-K notes), outcomes scorecard, external-innovation machinery, platform-vs-asset classification, `ecosystem_graph_edges.jsonl` | A9 ACCEPT |
| [industry_transformation/pipeline_regulatory/](industry_transformation/pipeline_regulatory/map.md) | FDA approvals 2022–26 (46 verified), setbacks (19), late-stage snapshots with NCTs, scientific platforms, quality assessment | A12 ACCEPT |
| [industry_transformation/policy/](industry_transformation/policy/map.md) | IRA exposure by product/round, pledges and MFN agreements, 340B, litigation, lobbying (partial) | A8 REVISE (lobbying totals missing) |
| [industry_transformation/commercial_patient/](industry_transformation/commercial_patient/map.md) | commercial models, patient programs & care delivery, launch execution, pricing/payer dynamics, transfer to Takeda | A7 REVISE (flag calibration) |
| [cross_company_analysis/](cross_company_analysis/map.md) | `master_comparison.md` + 12 matrices + `lessons_for_takeda.md` (21 lessons → `../strategy/data/takeda_lessons.json`) | decision-grade with conditions (A10-bis) |
| [research_coverage/](research_coverage/coverage_summary.md) | computed coverage ledger (85 rows) + Director rows; [gapfill_wave2/](research_coverage/gapfill_wave2/map.md) second-pass findings | current |
| [financial_models/](financial_models/) | `product_revenue_series.json`, EDGAR facts, CT.gov inventories | current |
| [unanswered_questions/](unanswered_questions/research_questions.md) | question decomposition + negative tests | current |
| knowledge_graph/ | generated into `../data/normalized/knowledge_graph.json` and `deals.json` | generated |

## Which report depends on which evidence
| Report | Depends on |
|---|---|
| `companies/*/financials/xbrl_annual_facts.md` | SEC companyfacts + 10-K/20-F records (RUN-0001; A4 shard) |
| `companies/*/master_report.md` v1.1 | company shard (A1/A2/A3/A5) + horizontal shards (A6, A7, A8, A9, A12) + gap-fill (A14) + audit repairs (A10) |
| `cross_company_analysis/*` | all dossiers + horizontals; honours `correction` fields; refuses invalid rankings |
| `../strategy/*` (v2) | accepted claims only (Gate 3) + `ASM-` assumptions; challenged by `../strategy/critical_challenges/` |
| `../deliverables/*` | cross-company layer + strategy v2 + council; 184 claims cited |
| `../video_production/` (TAKEDA 2040 film, session 3) | 67 distinct claims (71 SUPPORTED / 10 PARTIALLY_SUPPORTED / 2 INCONCLUSIVE references) + 26 ASM/BET/RM ids, read-only from these registries; ledger `../video_production/research/evidence_ledger.json`, trail `../video_production/deliverables/VIDEO_RESEARCH_REFERENCES.md`. The film adds no records here. |

## How to add evidence (any agent)
1. Get your shard and next IDs: `~/.local/share/mise/installs/python/3.12/bin/python3 tools/evidence.py ids <shard>` (ranges in `research_methodology/agent_protocols.md`).
2. Append `sources.jsonl` / `claims.jsonl` records (formats in agent_protocols.md §2); `validate --shard <shard> --path <file>` must report 0 errors.
3. Director merges: `python3 scripts/merge_shards.py <shard>` → `python3 scripts/validate_registries.py` PASS.
4. Audit proposals go to `evidence_library/conflicts_proposed_<agent>.jsonl`; the Director applies them with an `apply_audit*.py` script (never edit statements).
5. `python3 scripts/update_coverage.py`, a run note in `research_methodology/research_runs/`, update the folder `map.md`, then `./launch.sh`.
