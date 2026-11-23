# A2 — Johnson & Johnson Research Lead (wave 1)

Shard: `A2_jnj` (SRC/CLM-002000..002999). Output dir: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/companies/johnson_johnson/`. You may REPLACE `master_report.md` (interim v0.2 — keep its accurate `CLM-000xxx` citations). Do NOT modify `financials/xbrl_annual_facts.md` or `pipeline/ctgov_inventory.md`.

## Research question
What makes J&J's combination of Innovative Medicine and MedTech strategically distinctive; how did it manage the Stelara loss of exclusivity, the Kenvue separation and the talc litigation; what has it demonstrably built (vs announced) in oncology, immunology, neuroscience and surgical/cardiovascular technology; and where is it vulnerable?

## On-disk inputs (read FIRST)
`/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/extracted_text/sec/JNJ_10-K_*.txt` (FY2021 ends 2022-01-02, FY2022 2023-01-01, FY2023 2023-12-31, FY2024 2024-12-29, FY2025 2025-12-28). Grep: `Kenvue|Consumer Health separation`, `Stelara`, `Darzalex`, `Carvykti`, `Tecvayli|Talvey`, `Tremfya`, `Rybrevant|Lazcluze`, `Spravato`, `Caplyta|Intra-Cellular`, `Abiomed`, `Shockwave`, `talc|LTL|Red River`, `biosimilar`, `MedTech`, `Ottava|MONARCH|VELYS`, `Inflation Reduction Act|Xarelto|Imbruvica`, `impairment|in-process research`, `COVID-19 vaccine`, `RSV`.

## Mandatory sub-questions
1. Business architecture: segment revenue (Innovative Medicine vs MedTech, Consumer Health until 2023) FY2021–25; top products and their trajectories; U.S./international; margins; R&D (two segments); capex; cash returned; debt after acquisitions. Add only what is not already in CLM-000001..238/253..262.
2. Timeline 2021-11→2026-11: Kenvue IPO (2023-05) and split-off (2023-08); Abiomed close (2022-12), Shockwave (2024-05), V-Wave, Laminar, Ambrx (2024), Proteologix, Yellow Jersey/Numab, Intra-Cellular Therapies (close 2025-04); Stelara biosimilar entries (EU 2024-07; US 2025-01 onward); talc bankruptcy attempts (LTL 2021/2023 dismissed; Red River Talc plan rejected 2025-03); COVID vaccine wind-down; RSV vaccine discontinuation (2023); Xarelto and Stelara in Medicare negotiation; FDA approvals (Carvykti 2022-02, Tecvayli 2022-10, Talvey 2023-08, Rybrevant expansions, Lazcluze 2024-08, Tremfya UC/Crohn's, Spravato monotherapy 2025, Imaavy/nipocalimab 2025, Inlexzo/TAR-200 2025, Caplyta sNDA); MedTech: OTTAVA IDE/first cases, MONARCH urology, VELYS spine/knee, Impella labelling and FDA letters; Varipulse PFA pause 2025.
3. Pipeline quality: late-stage assets with NCTs (icotrokinra/JNJ-2113, nipocalimab, TAR-200, Rybrevant+Lazcluze, pasritamig, bleximenib, seltorexant, aticaprant (failed Phase 3 2025?), posdinemab…), the "26 drugs with >USD 1bn potential by 2030" statements vs actual approvals; discontinued programs.
4. MedTech: Abiomed/Impella outcomes and regulatory issues; Shockwave IVL integration; surgical robotics (OTTAVA status — one installation, IDE), MONARCH (bronchoscopy, kidney stones), VELYS adoption numbers if disclosed; orthopaedics spin-off (DePuy Synthes separation announced 2025-10).
5. Commercial & patient: Stelara→Tremfya conversion strategy, payer dynamics, patient support (J&J withMe), 340B rebate-model litigation (2024–25).
6. Leadership/operating model: Joaquin Duato (CEO 2022-01), Joe Wolk (CFO), John Reed→Jennifer Taubert/… (R&D leadership changes), Jim Swanson (CIO) statements; "Innovative Medicine" rebrand 2023.
7. Successes (top 5) / failures & weaknesses (≥5: talc, RSV, bermekimab, aticaprant, Varipulse pause, COVID vaccine, Stelara cliff, Impella letters).
8. Moats (INTERPRETATION with mechanism and replication path): oncology multi-myeloma franchise depth, MedTech+Pharma dual platform, JLABS/JJDC ecosystem, scale in immunology.
AI/robotics mechanism depth, policy detail, and the full deal inventory belong to A6/A8/A9 — summary level only (≤3 claims each).

## Web targets
- `https://www.jnj.com/media-center/press-releases`, `https://www.investor.jnj.com/` (web_fetch), 8-K exhibits (CIK 0000200406).
- FDA novel approvals 2022–2025 pages; Drugs@FDA; FDA devices database (`https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm`) for OTTAVA/MONARCH/VELYS/Impella.
- Court/regulatory records for talc (T1 where possible), Reuters/STAT/Fierce/Endpoints for corroboration.

## Deliverables
`master_report.md` v1.0 (22 sections + ≥3 Capability Mechanism Cards), `timeline.md`, `business/business_model.md`, `pipeline/late_stage_assets.md`, `robotics_automation/medtech_robotics_status.md`, `commercial_market_access/commercial.md`, `successes_failures/successes_failures.md`, `competitive_advantage/moats.md`, `leadership/leadership.md`, `map.md`, `evidence_gaps.md`. Shard target ≥30 sources (≥20 retrieved), ≥70 claims.
