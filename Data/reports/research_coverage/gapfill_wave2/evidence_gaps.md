# Evidence gaps (A14 wave 2)

Unavailable MCP servers in this session: andes-mcp, chorus (failed to start; not needed).

## Blocked or unopened sources
- J&J MedTech Varipulse resume release (jnjmedtech.com): HTTP 403; FDA's correction notice used instead [CLM-014018].
- Fierce Biotech JLABS New York closure: HTTP 403; snippet only [CLM-014065].
- Investing.com AbbVie Morgan Stanley transcript: HTTP 403; Motley Fool Q4 2025 call used [CLM-014072].
- multiplylabs.com/news: no Strateos match; no Strateos or Multiply Labs primary release found [CLM-014057].
- Reuters Juvmo article, Axcelead and Edaily TuneLab items, FDA Entyvio review document: snippets only (metadata_only) [CLM-014039] [CLM-014056] [CLM-014051].
- Lilly investor.lilly.com release datelines were stripped on fetch; dates for Houston, Alabama, Pennsylvania, Kenosha and Limerick come from search-result datelines and are noted in the source records.

## Unresolved questions
1. Zepbound OSA and HFpEF exact FDA action dates; U.S. HFpEF outcome (10-K says EU-only approval at FY2025) [CLM-014007]. Next: Drugs@FDA label history for NDA 217806.
2. Whether Limerick began production in 2026, Concord's production start in a filed document, and any operating evidence for Kenosha, Alzey [CLM-014011] [CLM-014012] [CLM-014013] [CLM-014014]. Next: Lilly 10-Q Q3 2026 (Item 2 / MD&A), Irish and German local reporting.
3. VELYS, MONARCH and OTTAVA installed-base or procedure counts: none disclosed in sources opened. Next: J&J Q3 2026 earnings call transcript, MedTech investor presentation.
4. Whether openFDA K260382 is the MONARCH QUEST 3 clearance (inferred) [CLM-014025]. Next: FDA 510(k) summary PDF for K260382.
5. Talc: participation outcome versus the 95% threshold, court action after 2026-07-27, and the Red River docket entry itself (Dkt. 1424) [CLM-014027] [CLM-014029]. Next: CourtListener/PACER; J&J Q3 2026 10-Q.
6. Humira settlement terms and the appellate result of In re Humira antitrust [CLM-014036] [CLM-014037]. Next: Seventh Circuit opinion (2022).
7. Landos completion date confirmed only by a release snippet; Celsius terms from 10-K upfront only [CLM-014033] [CLM-014031].
8. Takeda: Purple Book exclusivity for Entyvio (BLA 125476, approved 2014-05-20 per FDA snippet) [CLM-014051]; Amitiza judgment entry, trebling and post-trial rulings after the 20-F [CLM-014048]; Takeda Ventures / Center for External Innovation scale [CLM-014052].
9. NVIDIA-Lilly co-innovation lab: no operating confirmation; LillyPod launch date unresolved [CLM-014053] [CLM-014054].
10. TuneLab participant count and any federated-model retraining result [CLM-014056].
11. Venture-arm scale: Lilly Ventures fund, JJDC portfolio, AbbVie Ventures, Takeda Ventures counts not found in primary sources [CLM-014063] [CLM-014066] [CLM-014052]. JLABS 2026 site count depends on a snippet [CLM-014065].
12. Lilly 2022 licence upfronts beyond the 10-K asset-acquisition table (e.g., Akouos) and 2024 licence deals were not enumerated [CLM-014058] [CLM-014059].
13. Leadership: AbbVie and Takeda interviews are third-party transcripts; no Julie Kim interview transcript opened (shareholder letter used) [CLM-014072] [CLM-014074].

## Method limits
- Many 2026-dated facts rest on company releases (single interested source). Flags are in each claim's `single_interested_source`.
- 10-K locators use extracted-text line numbers from `extracted_text/sec/*.txt`; some are marked approximate with "~".
- Dates for several press releases come from search metadata rather than the fetched page.

## Suggested next research
- Lilly Q3 2026 10-Q and Q3 earnings-call transcript (manufacturing status, LillyDirect share).
- J&J Q3 2026 10-Q (talc participation, DePuy separation structure) and call transcript (robotics adoption).
- Drugs@FDA/Purple Book pulls for Zepbound, Juvmo, Entyvio.
- D. Mass. Amitiza docket (judgment entry, post-trial motions).
