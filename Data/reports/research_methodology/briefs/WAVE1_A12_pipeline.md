# A12 — Scientific, Pipeline & Regulatory Intelligence (horizontal, wave 1)

Shard: `A12_pipeline` (SRC/CLM-012000..012999). Output dir: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/industry_transformation/pipeline_regulatory/`. Companies: Lilly, J&J, AbbVie, Takeda.

## Research question
What did each company actually get approved, what failed or was delayed, and how good is the late-stage pipeline (quality, concentration, modality mix, scientific platforms) 2021-11→2026-11 — measured from regulator records, trial registries and peer-reviewed primary publications rather than company pipeline slides?

## Inputs
- Existing CT.gov inventories (do not redo): `/Users/palrahma/Desktop/MEDICINE/New_mediciine/companies/<co>/pipeline/ctgov_inventory.md` and `New_mediciine/financial_models/ctgov_<co>.jsonl` (lead-sponsor Phase 2/3 registrations by start year). Cite the A4 shard claim for the dataset.
- 10-K/20-F text on disk (`extracted_text/sec/`) sections "Research and Development" / "Pipeline" / "Regulatory" for each year — company-stated late-stage lists and discontinuations.

## Mandatory sub-questions
1. **FDA novel approvals 2022–2026 per company** from `https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2022` (…2023, 2024, 2025, 2026): product, active ingredient, approval date, indication, sponsor; plus BLA/CBER approvals (Carvykti 2022-02, Tecvayli, Talvey, Kisunla, Imaavy…) from FDA biologics pages. One FACT claim per approval (≈25–35 claims). Verify sponsor attribution (e.g., Imbruvica J&J/AbbVie; Epkinly AbbVie/Genmab).
2. **Major supplemental approvals that drove revenue** (Mounjaro→Zepbound obesity 2023-11; Zepbound OSA 2024-12; Skyrizi UC 2024-06 / Crohn's 2022-06; Rinvoq UC/Crohn's/GCA; Tremfya UC 2024-09 / Crohn's 2025-03; Darzalex Faspro expansions; Carvykti 2L 2024-04; Rybrevant+Lazcluze 1L 2024-08; Entyvio SC 2023-09/2024-04; Vyvanse pediatric?) — ≈15 claims.
3. **CRLs, failures, withdrawals, delays** (≥15 claims): Lilly (lebrikizumab CRL 2023-10 manufacturing; mirikizumab CRL 2023-04; donanemab adcomm/delay 2024; sintilimab CRL 2022; Olumiant alopecia OK; retatrutide? ; Verzenio? ; tirzepatide shortages), J&J (RSV vaccine discontinued 2023-03; bermekimab 2022; aticaprant Phase 3 stop 2025-03; nipocalimab in some indications; Varipulse pause 2025-01; talc not pipeline), AbbVie (ABBV-951 CRL 2023-03; emraclidine EMPOWER-1/2 failures 2024-11; Rinvoq boxed warning 2021-12; navitoclax; Vraylar MDD?; teliso-V accelerated → confirm), Takeda (TAK-994 2021-10; soticlestat Phase 3 miss 2024-06; Exkivity withdrawal 2023-10; Alofisel withdrawal 2024; TAK-279?; mobocertinib; Eohilia OK 2024-02; fruquintinib OK 2023-11; Qdenga U.S. BLA withdrawal 2023-07).
4. **Late-stage pipeline quality snapshot at cutoff** per company: top ~8 Phase 3 assets with NCT IDs, primary completion dates, modality, mechanism novelty (first-in-class vs best-in-class), and peer-reviewed primary readouts where published (NEJM/Lancet DOIs — abstract-level inspection via PubMed is fine). Flag concentration (e.g., Lilly incretins) and modality breadth (ADC, bispecific, cell therapy, RNA, gene editing, radioligand, oral peptides).
5. **Scientific platform capabilities** (≥10 claims): Lilly (oral GLP-1 chemistry, radioligand via POINT, gene editing via Verve, siRNA lepodisiran), J&J (bispecific T-cell engagers, CAR-T with Legend, ADC via Ambrx, oral peptide icotrokinra via Protagonist), AbbVie (ADC platform ImmunoGen/Temab-A, in-vivo CAR-T Capstan, neuroscience small molecules), Takeda (TYK2 oral, orexin agonists, plasma-derived, siRNA via Arrowhead fazirsiran, cell therapy exit?). Evidence: approvals, Phase 3 starts, peer-reviewed data.
6. **Regulatory relationships**: breakthrough / priority / fast-track counts if disclosed; National Priority Vouchers (Lilly orforglipron 2025); FDA accelerated-approval withdrawals (Exkivity, etc.).

## Evidence standard
T1 = FDA/EMA/CT.gov/PubMed/peer-reviewed. Company press releases establish the announcement; regulator record establishes the approval. Each approval claim: product, date, indication, FDA page locator. Each failure claim: date, what failed (endpoint/CRL reason if disclosed), source.

## Deliverables
`fda_approvals_2022_2026.md` (table per company with claim IDs), `setbacks_crls_withdrawals.md`, `late_stage_pipeline_snapshot.md` (per company table with NCTs), `scientific_platforms.md`, `pipeline_quality_assessment.md` (INTERPRETATION: depth, concentration, modality mix, revenue-replacement adequacy — label clearly), `map.md`, `evidence_gaps.md`. Shard target ≥35 sources (≥25 retrieved), ≥90 claims.
