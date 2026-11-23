# A1 — Eli Lilly Research Lead (wave 1)

Shard: `A1_lilly` (SRC/CLM-001000..001999). Output dir: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/companies/eli_lilly/` (sub-folders exist). You may REPLACE `master_report.md` (currently an interim v0.2 skeleton — keep every accurate `CLM-000xxx` citation it already has). Do NOT modify `financials/xbrl_annual_facts.md` or `pipeline/ctgov_inventory.md` (cite them).

## Research question
How did Eli Lilly go from a USD 28bn (FY2021) to a USD 65bn (FY2025) company, what does it actually do differently, what has it demonstrably achieved vs merely announced, where has it failed, and which of its investments are positioning it for 2030+?

## On-disk inputs (read these FIRST — they are the five 10-Ks)
`/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/extracted_text/sec/LLY_10-K_<FYE>_<accession>.txt` for FY2021–FY2025. For each year grep: `Executive Overview`, `Results of Operations`, `Revenue by product`, `acquisition`, `collaboration`, `impairment`, `Mounjaro`, `Zepbound`, `Trulicity`, `Verzenio`, `Taltz`, `donanemab|Kisunla`, `orforglipron`, `retatrutide`, `manufacturing|capacity|Lebanon|Concord|Alzey|Limerick|Kenosha`, `LillyDirect`, `Medicare|Inflation Reduction Act|340B|insulin`, `patent|exclusivity`, `legal proceedings`. Build the dated five-year timeline from these before touching the web.

## Mandatory sub-questions (each needs a status)
1. Business/financial architecture: revenue by product FY2021–25 (U.S./ex-U.S.), concentration (tirzepatide share), gross & operating margin trend, R&D as % revenue, capex trajectory and named sites, debt build-up, buybacks/dividends vs reinvestment. (Numbers already in registry: cite CLM-000001..238/239..252; add only what is missing — product-level and site-level.)
2. Transformation timeline 2021-11→2026-11: approvals (Mounjaro 2022-05, Zepbound 2023-11, Kisunla 2024-07, Omvoh, Jaypirca, Ebglyss, Inluriyo…), label expansions (OSA, HFpEF), CRLs/delays (donanemab adcomm 2024, Lebrikizumab CRL 2023, Mirikizumab CRL 2023), supply shortages, price cuts (insulin 2023), orforglipron Phase 3 readouts 2025, retatrutide, pricing agreement with the U.S. administration (Nov 2025) and TrumpRx/LillyDirect.
3. R&D operating model & pipeline quality: therapeutic concentration, late-stage asset list with NCT numbers for the top 8 (orforglipron, retatrutide, olomorasib, imlunestrant, lepodisiran, bimagrumab, eloralintide, remternetug…), discontinued programs, R&D spend productivity narrative. Use ClinicalTrials.gov v2 for the NCT facts.
4. Commercial & patient: LillyDirect (launch 2024-01, what it does, cash-pay vial pricing), gross-to-net pressure disclosures, compounding litigation, access/coverage facts (Medicare obesity coverage date), patient support.
5. Manufacturing: announced investments 2023–2026 (amounts, sites, dates), the "Lilly Medicine Foundry", capacity commentary and shortages; distinguish announced vs operating.
6. Leadership & operating model: Dave Ricks tenure, Dan Skovronsky (CSO), Diogo Rau (CIDO), Anat Ashkenazi→Lucas Montarce (CFO change 2024), organisational statements. One or two inspected interview/transcript sources are enough; metadata-only for the rest.
7. Successes (top 5, verified) and failures/weaknesses (≥5: e.g. Vitrakvi impairment, Trulicity decline, Alzheimer's delays, Verve/Loxo write-downs if any, supply, compounding, concentration risk, litigation). Each with evidence.
8. Moats (INTERPRETATION, each with the mechanism and how a rival could replicate): incretin manufacturing scale, oral GLP-1 timing, proprietary preclinical data (TuneLab), compute partnerships.
AI/robotics, policy detail and the deal-by-deal M&A inventory are owned by horizontal agents A6/A8/A9 — cover them at summary level only (≤3 claims each), citing what you inspect.

## Web targets (open, do not just snippet)
- `https://www.lilly.com/news` (press releases; 8-K exhibits on EDGAR for the earnings releases: CIK 0000059478).
- FDA: `https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2022` … `-2025` (filter Lilly sponsors), Drugs@FDA for label dates.
- ClinicalTrials.gov v2 JSON for NCTs. PubMed/NEJM for the SURMOUNT/SURPASS/ACHIEVE/TRAILBLAZER-ALZ 2 primary papers (metadata + abstract is enough).
- T3 corroboration: Reuters, STAT, Endpoints, Fierce (via web_fetch), BioPharma Dive.

## Deliverables
- `master_report.md` v1.0 with the 22 sections of the master prompt §9 (short sections allowed where evidence is thin — say so). Include ≥3 **Capability Mechanism Cards** (table: Capability / Initial problem / Starting investment / Execution / Enabling assets / Evidence of value / Durability / Competitive response / Takeda relevance / Evidence IDs).
- `timeline.md` (dated events with claim IDs), `business/business_model.md`, `pipeline/late_stage_assets.md`, `commercial_market_access/commercial.md`, `successes_failures/successes_failures.md`, `competitive_advantage/moats.md`, `leadership/leadership.md`, `map.md`, `evidence_gaps.md`.
- Shard: target ≥30 sources (≥20 retrieved) and ≥70 claims.
