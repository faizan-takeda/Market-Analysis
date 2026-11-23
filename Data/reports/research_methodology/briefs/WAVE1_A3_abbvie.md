# A3 — AbbVie Research Lead (wave 1)

Shard: `A3_abbvie` (SRC/CLM-003000..003999). Output dir: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/companies/abbvie/`. You may REPLACE `master_report.md` (interim v0.2 — keep accurate `CLM-000xxx` citations). Do NOT modify `financials/xbrl_annual_facts.md` or `pipeline/ctgov_inventory.md`.

## Research question
How did AbbVie absorb the largest loss of exclusivity in pharma history (Humira U.S., Jan 2023) and return to growth; what did the Allergan integration deliver; what is the real quality of its post-Humira engine (Skyrizi, Rinvoq, Botox, Vraylar, Elahere, Venclexta, oncology); where has capital been destroyed (Cerevel/emraclidine, Imbruvica decline, Vraylar?), and what positions it for 2030+?

## On-disk inputs (read FIRST)
`/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/extracted_text/sec/ABBV_10-K_*.txt` FY2021–FY2025. Grep: `Humira|adalimumab|biosimilar`, `Skyrizi`, `Rinvoq`, `Imbruvica`, `Venclexta`, `Botox`, `Vraylar`, `Elahere|ImmunoGen`, `Cerevel|emraclidine|tavapadon`, `Allergan`, `Capstan`, `Aliada`, `Gubra`, `Landos`, `Nimble`, `impairment|intangible`, `Inflation Reduction Act|Medicare`, `Vyalev|ABBV-951|complete response`, `Epkinly`, `Teliso-V|Emrelis`, `Rinvoq.*label|boxed warning|JAK`, `Executive Overview`, `Results of Operations`.

## Mandatory sub-questions
1. Business architecture: revenue by key product FY2021–25 (Humira U.S./international split; Skyrizi; Rinvoq; Imbruvica; Venclexta; Botox Therapeutic/Cosmetic; Vraylar; Juvederm; Elahere), therapeutic-area mix (immunology, oncology, neuroscience, aesthetics, eye care), margins, R&D % revenue, debt pay-down after Allergan then re-leveraging for ImmunoGen/Cerevel, dividends/buybacks. Add only what is not in CLM-000001..238/263..270.
2. Timeline 2021-11→2026-11: Rinvoq/JAK safety label changes (2021-12), Humira biosimilar entries (Amjevita 2023-01; wave 2023-07), Skyrizi/Rinvoq indication expansions (UC, Crohn's, GCA, vitiligo?), Imbruvica decline & Medicare negotiation selection (2023-08), ABBV-951 CRL (2023-03) → Vyalev approval (2024-10), ImmunoGen close (2024-02), Cerevel close (2024-08), emraclidine Phase 2 failures (2024-11) and the ~USD 3.5bn impairment (2025), tavapadon Phase 3 results/NDA, Capstan (2025, in-vivo CAR-T, up to USD 2.1bn), Aliada (2024-10), Nimble, Gubra (amylin, 2025-03), Landos, Celsius; CEO transition Gonzalez→Rob Michael (2024-07); Humira formulary exclusions (CVS 2024-04); 2025 guidance raises; 2027 Skyrizi+Rinvoq >USD 31bn target statement; U.S. manufacturing investment pledge (USD 10bn, 2025).
3. Pipeline quality: late-stage assets with NCTs (tavapadon, Teliso-V/Emrelis approval 2025-05, pivekimab, ABBV-400/Temab-A, lutikizumab, Rinvoq new indications, Skyrizi, Elahere expansions, Epkinly, Botox new indications, emraclidine status); discontinued programs; is the pipeline deep enough post-2030?
4. Commercial & patient: Humira defence tactics (contracting, rebates, biosimilar price dynamics; U.S. Humira revenue decline path), Skyrizi/Rinvoq access strategy, Botox Cosmetic consumer model (Allē loyalty), patient support, gross-to-net disclosures.
5. Allergan integration: synergies claimed vs delivered, Botox trajectory, aesthetics softness 2023–25, eye care divestiture considerations.
6. Leadership/operating model: Gonzalez→Michael, Roopal Thakkar (CSO), Jeff Stewart (CCO), Scott Reents (CFO); stated R&D philosophy (external innovation share).
7. Successes (top 5) / failures (≥5: emraclidine, Imbruvica, aesthetics slowdown, Rova-T (older), ABBV-951 CRL, Humira international erosion, any trial halts).
8. Moats (INTERPRETATION): immunology commercial infrastructure, lifecycle management/IP strategy, aesthetics consumer franchise, BD&L track record — mechanism + replication path each.
AI/robotics depth, policy detail, full deal inventory → A6/A8/A9 (summary ≤3 claims each).

## Web targets
`https://news.abbvie.com/` (web_fetch), 8-K exhibits (CIK 0001551152), FDA novel approvals 2022–2025 + Drugs@FDA, ClinicalTrials.gov v2, Reuters/STAT/Fierce/Endpoints/BioPharma Dive for corroboration and failures.

## Deliverables
`master_report.md` v1.0 (22 sections + ≥3 Capability Mechanism Cards), `timeline.md`, `business/business_model.md`, `pipeline/late_stage_assets.md`, `commercial_market_access/commercial.md`, `successes_failures/successes_failures.md`, `competitive_advantage/moats.md`, `leadership/leadership.md`, `map.md`, `evidence_gaps.md`. Shard target ≥30 sources (≥20 retrieved), ≥70 claims.
