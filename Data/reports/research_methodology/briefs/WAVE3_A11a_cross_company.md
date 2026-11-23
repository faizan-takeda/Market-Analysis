# A11a — Cross-Company Comparative Intelligence (wave 3; Phase 4)

Allowed writes: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/cross_company_analysis/**` and `/Users/palrahma/Desktop/MEDICINE/strategy/data/takeda_lessons.json`. Shard for any new evidence: `A11_strategy` (SRC/CLM-011000..). You synthesise; you do not re-research except to close a gap that blocks a comparison (≤10 new sources).

## Inputs (read in this order; use `grep -n` on the registry rather than reading it whole)
1. `research_methodology/briefs/WAVE1_COMMON.md` §1 (evidence rules) and `strategy/DATA_CONTRACT.md` (takeda_lessons.json shape).
2. Audit outputs if present: `quality/citation_audits/gate1_verdicts.md`, `quality/evaluation_results/wave1_scorecard.md`, `New_mediciine/evidence_library/conflicts_proposed_A10.jsonl` — treat claims flagged there as contested; do not build a comparison on a claim the auditor marked NUMBER_MISMATCH / NOT_FOUND.
3. The four dossiers `New_mediciine/companies/{eli_lilly,johnson_johnson,abbvie,takeda_public_baseline}/master_report.md` + their `timeline.md`, `business/business_model.md`, `successes_failures/successes_failures.md`, `competitive_advantage/moats.md`, `financials/xbrl_annual_facts.md`.
4. Horizontal reports: `New_mediciine/industry_transformation/{ai_data_robotics,partnerships_ecosystem,pipeline_regulatory,policy,commercial_patient}/*.md` (commercial_patient and `research_coverage/gapfill_wave2/gapfill_findings.md` may be arriving — use if present).
5. Registry lookups: `grep '"CLM-00xxxx"' New_mediciine/evidence_library/claims_registry.jsonl` for any number you quote.

## Deliverables (every material sentence carries `[CLM-…]`; unlabelled analysis is marked *(INTERPRETATION)*; no standardized scores unless the underlying metric is defined and comparable)
- `master_comparison.md` — answers, each with evidence: Why is Lilly winning where it wins? What makes J&J's pharma+MedTech combination distinctive (and where is the synergy claim unevidenced)? How did AbbVie absorb Humira LOE? Who converts R&D into commercial outcomes best (define the metric; reconcile periods, acquisitions, IPR&D accounting)? Who has the most defensible technology ecosystem? Which AI investments are operationally meaningful? Who has repeatable discovery/development capability? Which partnerships create durable options? What does each do better than the other two? Where is each vulnerable? What would change their positions by 2035?
- `competitive_capability_matrix.md` (capability × company; cells = evidence-backed statement + claim IDs; "no evidence" allowed)
- `five_year_timeline_comparison.md` (aligned 2021-11→2026-11 table, three companies + Takeda)
- `pipeline_and_revenue_dependence.md` (top-product concentration, LOE calendar, replacement evidence)
- `rd_investment_and_productivity.md` (R&D spend, acquired IPR&D, approvals per period, with period/accounting caveats; say where comparison is invalid)
- `data_ai_maturity_matrix.md` (from A6 cards + company claims; maturity levels only)
- `robotics_deployment_comparison.md`
- `partner_ecosystem_comparison.md` (from A9 inventory/edges)
- `loe_resilience_comparison.md`
- `commercial_capabilities_comparison.md` (from A7 if present, else dossiers)
- `strengths_and_vulnerabilities.md`
- `lessons_for_takeda.md` + `strategy/data/takeda_lessons.json` (≥15 lessons, each with competitor evidence IDs, transferability verdict, the Takeda baseline class from `companies/takeda_public_baseline/capability_baseline/capability_baseline.md`, and an IVB reference where internal validation is needed)
- `map.md`, `evidence_gaps.md` (comparisons you could not make and why)

## Rules
Reconcile fiscal periods (J&J 52/53-week; Takeda Apr–Mar), currencies (JPY vs USD — compare growth rates and shares, not absolute JPY vs USD, unless you state the FX basis), acquisition effects and segment definitions before any numeric comparison; if a comparison is invalid, say so. No forced conclusions, no radar-chart scores. Budget 400 tool calls; write files progressively; finish with FILES WRITTEN / TOP 10 COMPARATIVE FINDINGS (with claim IDs) / INVALID OR UNSUPPORTED COMPARISONS / EVIDENCE GAPS.
