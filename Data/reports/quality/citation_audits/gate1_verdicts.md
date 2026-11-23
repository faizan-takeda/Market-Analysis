# A10: Gate 1 verdicts (Task 7)

Date 2026-11-21. Criteria (from the A10 brief): verified sources, five-year timeline, financial reconciliation, balanced success/failure, evidence-gap report. Evidence base: the 99-claim re-inspection ([audit_wave1_reinspection.md](audit_wave1_reinspection.md)), reconciliation ([audit_wave1_reconciliation.md](audit_wave1_reconciliation.md)), scorecard ([../evaluation_results/wave1_scorecard.md](../evaluation_results/wave1_scorecard.md)). Verdicts are sample-based: ticks mean no defect found in what I re-inspected, not that every claim was re-checked.

| Company | Verified sources | Five-year timeline | Financial reconciliation | Balanced success/failure | Evidence-gap report | Verdict |
|---|---|---|---|---|---|---|
| Eli Lilly | pass (17/17 figures correct, 12 locator fixes) | pass (FY2021 to Q3 2026; 2022 thin, 2 entries) | pass | pass | pass | **PASS** with minor repairs |
| Johnson & Johnson | pass (13/13) | pass (39 dated entries) | pass with label defect (see repairs) | pass | pass | **CONDITIONAL PASS** |
| AbbVie | pass (15/16; 1 label error) | pass | **fail** (debt label; deal-size bases) | pass | weak (5 lines; 8 metadata_only sources not discussed) | **CONDITIONAL PASS** after repairs |
| Takeda | pass with gaps (16/16 figures correct; 1 component unreachable; 1 source without local text) | **fail** (starts FY2022; Nov 2021 to Mar 2022 and FY2021 absent) | pass (24/24 XBRL = A4 pairs; dossier numbers match 20-F) | partial (failures are in sections, no successes_failures or moats file) | pass | **FAIL (repairable)** |

## Eli Lilly: PASS
Repairs (none blocks Gate 1):
1. Correct 12 approximate or wrong locators (list in the re-inspection table; e.g. CLM-001009 line 2255).
2. Add a basis label (expense vs cash paid) to CLM-001014, CLM-000247, CLM-009000; correct false precision "3,008.0".
3. Reword the implication on CLM-000280 ("monetises" implies revenue the corpus does not show).
4. Register the FY2021 IPR&D definition change (874.9 vs 970.1 incl. development milestones) in conflicts.jsonl.
5. 2022 timeline has two entries; add Alimta generics (CLM-001011) and the 2022 COVID antibody revenue decline if wanted for balance.

## Johnson & Johnson: CONDITIONAL PASS
Required before Gate 1 closes:
1. Master report lines 30, 74, 84 and CLM-000284: state "announced Memorial Hermann as first installation site", not a completed install; remove "about 24 months from IDE to first commercial install" until an install is confirmed.
2. "Regulator-verified" for OTTAVA/VELYS/MONARCH rests on J&J releases. Add FDA database records (openFDA 510(k): MONARCH K260382 and K243219, VELYS K260480 and K240211 were found by A10) and an FDA De Novo record for OTTAVA, or relabel as "company-reported".
3. Flag the 8 T2-only claims single_interested_source (CLM-002037, -002039, -002040, -002041, -002044, -002060, -002061, -002064).
4. Relabel CLM-000128..000132 ("non-current" debt is the debt-note subtotal incl. current portion; non-current is 39,438 at FY2025) and name the three debt bases used (39.4bn non-current, 41.4bn gross long-term, 47.9bn incl. loans and notes payable).
5. Fix the three broken relative links in `business/business_model.md` (`../financials/xbrl_annual_facts.md`, `../evidence_gaps.md`).

## AbbVie: CONDITIONAL PASS
Required:
1. Correct CLM-003042 and the business-model line that cites it (the series 75,962 / 63,128 / 59,245 / 66,841 / 64,503 is total long-term debt incl. current portion; balance-sheet non-current is 64,189 / 59,135 / 52,194 / 60,340 / 58,941). Same fix for CLM-000066..000070.
2. State the basis for deal sizes: ImmunoGen 10.1bn announced total value, 9.8bn consideration, 9.2bn net of cash; "18.5bn cash paid" is consideration transferred, 17.5bn net of cash acquired (CLM-003086, master Card 3 and line 45).
3. Expand `evidence_gaps.md` to cover the 8 metadata_only and 3 blocked sources and the unresolved Ventures founding date (2009 vs about 2015, CLM-009074).
4. Flag the 22 single-interested-source claims in dossier text where they carry strategic conclusions (Humira contracting percentages rely on T3 IQVIA/trade sources: CLM-003007, CLM-003009, CLM-003085, not re-opened by A10).

## Takeda: FAIL (repairable, estimated one short session)
Required:
1. Timeline: add FY2021 and Nov 2021 to Mar 2022 events already in the registry (Hasten China portfolio sale, March 2022, CLM-009086; Teijin transfer April 2021 as lookback; TAK-994 termination in 2021, CLM-012119) and add FY2022 events beyond TAK-994.
2. Create `business/business_model.md` (the directory is empty).
3. Create a successes and failures section or file with the failures now scattered (TAK-994, EXKIVITY, ALOFISEL, soticlestat, cell therapy, AMITIZA verdict) beside the successes (Entyvio SC, three 2026 approvals).
4. Rewrite CLM-005078: the restructuring series is about JPY 150bn (25 Mar 2026) -> 170.0bn (original FY2026 forecast) -> 160.0bn (revised, Oct 2026); 170bn is Takeda's own figure, not only press.
5. Cite the recognised cell-therapy impairment (JPY 58.2bn, FY2025 20-F) alongside the October 2025 estimate (58.0bn).
6. Preserve evidence for SRC-005015 (H1 FY2026 PDF has no extracted text file) and SRC-005018; verify or drop "137 Massachusetts roles" (Fierce returned 403).
7. Verify leverage figures CLM-005005 (2.6x, 3.1x, 2.8x, 2.6x): not located by A10.
8. Treat the USD 10-20bn six-asset peak range as a company statement (T2) wherever it is used.

## Cross-company repairs
- Apply the maturity retags and fill the 24 missing tags (see [audit_wave1_status_discipline.md](audit_wave1_status_discipline.md)).
- Re-register SRC-000034, SRC-009022 and SRC-009017 as retrieved; store raw copies for SRC-000029 and other bot-walled pages.
- Record conflicts (and independent corroboration where it exists) in `conflicts.jsonl` and `independent_corroboration`: both are empty or near-empty across the registry, so Independence and Contradiction handling cannot reach 2 on the rubric.
- Fix the PubMed fetch stub (use NCBI E-utilities) for SRC-001025 and SRC-001028.
