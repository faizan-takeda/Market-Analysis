# Evidence gaps (A5 Takeda)

Research cutoff 2026-11-21. Takeda fiscal years run April-March (FY2025 = April 2025 to March 2026). Claim IDs resolve in `New_mediciine/evidence_library/shards/A5_takeda/claims.jsonl`; `CLM-000xxx` IDs resolve in the canonical `claims_registry.jsonl`. Only public sources were used.

## Closed in v1.1
- Annual Integrated Report 2026 PDF body: opened via pypdf in wave 2 [CLM-014041] [CLM-014042] [CLM-014043] [CLM-014044] [CLM-014045] [CLM-014046].
- Footnote basis for the USD 10-20bn peak estimate: R&D Day footnote located (not probability-adjusted; not a forecast or target) [CLM-014049].
- Leverage ratios [CLM-005005]: confirmed in the 20-F text (master_report §1).
- Takeda Ventures: a 100%-owned subsidiary; no fund size or portfolio count [CLM-014052].
- Timeline gap for FY2021 and FY2022: filled from registry claims (timeline.md).
- EDGAR 6-K R&D Day exhibit: opened [CLM-014049]. Amitiza: verdict details [CLM-014048].

## Could not open or read
- takeda.com newsroom list: page returned only a heading (script-rendered); releases came from TSE mirrors (fse.or.jp).
- takeda.com pipeline asset table (PDF download) [CLM-005082].
- Annual Integrated Report 2026 PDF body [CLM-005081] (opened in wave 2; see above).
- HTTP 403: Business Wire (Kim announcement, Jan 2025), Fierce Pharma (Amitiza verdict, restructuring), Fierce Biotech (soticlestat), Japanese consulate (Thousand Oaks), Investing.com and StockTitan (H1 results).
- Fortune (Ricci interview): paywalled; snippet only.
- EDGAR 6-K index, EMA/PMDA records, Reuters articles: not individually opened.

## Not found in sources opened
- Takeda Ventures, Center for External Innovation, external pipeline share [CLM-005052].
- "~80 markets" figure; patient assistance programs [CLM-005070, CLM-005072].
- Lab/manufacturing automation, continuous manufacturing, Singapore / Grange Castle / Osaka capex [CLM-005067, CLM-005066].
- Quantified AI outcomes; DD&T spend [CLM-005055, CLM-005080].
- Buyback amounts, FX hedging, FY2021 leverage ratio, Velcade history, non-U.S. Takhzyro expiry.
- Probability-adjusted peak sales: none public; the USD 10-20bn range is a company statement [CLM-005041] [CLM-014049]. (v1.0 gap "footnote basis" closed.)
- SRC-005015 (H1 FY2026 PDF) has no extracted-text file in the registry; key passages copied to [evidence_notes/h1_fy2026_extracts.md](evidence_notes/h1_fy2026_extracts.md). SRC-005018 (BioSpace, about JPY 170bn) was not re-opened; the 170bn figure rests on Takeda's own forecast note.
- "137 Massachusetts roles" (Fierce Biotech, HTTP 403): unverified and not used [CLM-005025].
- AMITIZA final judgment amount, trebling and post-trial status; D. Mass. docket not opened [CLM-014048] [CLM-014047].
- Entyvio biosimilar exclusivity: Purple Book entry not opened; BLAs accepted for review [CLM-014051].
- Nov 2021 to Mar 2022 dated events: only Hasten (March 2022) and Ricci (February 2022) are evidenced; no registry claim covers other events in that interval.
- Takeda Ventures fund size, portfolio count and CEI scope [CLM-014052] [CLM-009092]; Takeda Digital Ventures and T-CiRA unverified.
- Horizontal gaps: [ai_data_robotics](../../industry_transformation/ai_data_robotics/evidence_gaps.md), [partnerships](../../industry_transformation/partnerships_ecosystem/evidence_gaps.md), [pipeline](../../industry_transformation/pipeline_regulatory/evidence_gaps.md), [policy](../../industry_transformation/policy/evidence_gaps.md), [commercial](../../industry_transformation/commercial_patient/evidence_gaps.md).
- Peer-reviewed Phase 3 publications for oveporexton, zasocitinib, rusfertide.

## Suggested next queries
1. Open the AIR 2026 PDF; extract DD&T, supply chain, R&D model passages.
2. EDGAR 6-K exhibits: FY2025 Q4 presentation, R&D Day slides (footnote 1), H1 FY2026 presentation.
3. Search "Takeda Ventures", "Takeda Digital Ventures", "Shonan iPark automation".
4. FDA Orange/Purple Book and PMDA records for exclusivity dates.
5. Independent coverage of zasocitinib competitive position; NEJM/Lancet papers.
6. D. Mass. docket for post-trial status of the Amitiza case.
