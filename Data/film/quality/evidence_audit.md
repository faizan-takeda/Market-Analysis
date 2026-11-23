# Evidence audit — every on-screen and spoken figure traced

Source of truth: `research/evidence_ledger.json` (built by `research/build_evidence_ledger.py` from `screenplay/scenes.json` and the MEDICINE registries). Counts: 14 scenes · 83 claim references · 67 distinct claims · 67 distinct sources · 26 strategy ids (ASM/BET/RM) · **0 unresolved ids**.

| Status in registry | References | How the film handles it |
|---|---|---|
| SUPPORTED | 71 | stated as FACT |
| PARTIALLY_SUPPORTED | 10 | qualified on screen (e.g. "IQVIA via trade press", "vendor-hosted self-report") or worded as interpretation |
| INCONCLUSIVE | 2 | worded as absence of evidence ("no independent evidence found", "none published") |

Registry kinds: 72 FACT, 11 INTERPRETATION. Kinds added by the film on derived or strategy items: SCENARIO (erosion band, ASM-024), ASSUMPTION (envelope ASM-002/ASM-118; leverage ceiling ASM-033; FX ASM-001), RECOMMENDATION (BET ids).

## Figure-by-figure check (spoken or on screen → registry)

| Scene | Figure | Registry value / period | Claim | OK |
|---|---|---|---|---|
| S01/S05 | Entyvio JPY 958.0bn, 21% | FY2025 revenue by product | CLM-005009 | ✔ |
| S01 | exclusivity "second half of this decade"; patents to 2032 | 20-F wording | CLM-005017 | ✔ |
| S02 | Lilly USD 28.3bn → 65.2bn | FY2021 28,318.4m; FY2025 65,179.0m | CLM-000133, CLM-000137 | ✔ |
| S02 | tirzepatide 56% of sales | 56.0% FY2025 | CLM-001003 | ✔ |
| S02 | realized prices −15% | Q3 2026 y/y | CLM-014003 | ✔ |
| S02 | off preferred list 15 months | CVS Caremark removal 1 Jul 2025 → restored 1 Oct 2026 | CLM-007011, CLM-007013 | ✔ |
| S03 | Humira USD 21.2bn → 4.5bn "within three years" | 2022 21,237m → 2025 4,540m | CLM-003002 | ✔ |
| S03 | Skyrizi + Rinvoq USD 7.7bn → 25.9bn | 2022 7,687m → 2025 25,866m | CLM-003014 | ✔ |
| S03 | ≥97% volume, 14 months | IQVIA via trade press (PARTIALLY_SUPPORTED) | CLM-003007 | ✔ qualified |
| S04 | Stelara −41.3% | 2025 vs 2024 | CLM-000254 | ✔ |
| S04 | largest brand ≈15% | Darzalex 15.2% of FY2025 sales | CLM-002073 | ✔ |
| S04 | "no independent evidence" of AI outcomes | INTERPRETATION, PARTIALLY_SUPPORTED | CLM-011052, CLM-006054 | ✔ worded as absence |
| S04/S09 | Lilly robotic lab sold (2024) | Arctoris acquisition | CLM-006013, CLM-006016 | ✔ |
| S05 | Medicare price Jan 2028 | CMS selection Jan 2026 | CLM-007026 | ✔ |
| S05 | two biosimilar applications under FDA review | AVT16; PB016 (PARTIALLY_SUPPORTED) | CLM-014051 | ✔ qualified |
| S05 | Vyvanse −JPY 220bn in two years | 423.2 → 203.2 (FY2023→FY2025) | CLM-005015 | ✔ |
| S05 | JPY 383–766bn/yr at risk | 40–80% × 958.0 | ASM-024 (SCENARIO) | ✔ labelled, "not a forecast" |
| S06 | >270 plasma centres; USD 230m LA expansion | FY2025 20-F; June 2024 announcement | CLM-005063, CLM-005065 | ✔ |
| S06 | oveporexton approved 5 Aug 2026; Shonan discovery | FDA approval; Takeda statement | CLM-005029, CLM-005048 | ✔ |
| S06 | rusfertide approved 28 Aug 2026; zasocitinib priority review | FDA; 14 Sep 2026 | CLM-005032, CLM-005035 | ✔ |
| S06 | three Phase 3 readouts positive on plan | Dec 2024 R&D Day plan | CLM-005042 | ✔ |
| S06 | cell-therapy exit, JPY 58.2bn impairment | FY ended March 2026 | CLM-009084 | ✔ |
| S07 | ARCH 2,000+ trials, <10 staff; no outcome | Bio-IT World 2023 | CLM-006032, CLM-006034 | ✔ |
| S07 | TuneLab data > USD 1bn (company estimate) | Sept 2025 | CLM-000280, CLM-006055 | ✔ labelled company estimate |
| S08 | 63% GenAI usage | 63.4% at 31 Mar 2026 | CLM-014043 | ✔ |
| S08 | 170 predictive-maintenance agents; savings unpublished | 2026 Integrated Report | CLM-014041 | ✔ |
| S08 | agent platform 10,000+ employees | Databricks session (vendor) | CLM-005058 | ✔ qualified |
| S09 | AI-partner first-in-human 1–2 yrs out; autonomous loop not demonstrated | INTERPRETATION / INCONCLUSIVE | CLM-006007, CLM-000281 | ✔ worded as absence |
| S09 | Zymergen bought for one-tenth of IPO value | July 2022 | CLM-006051 | ✔ |
| S10 | CVS templates → Stelara biosimilars, most members USD 0 | 1 Jul 2026 | CLM-007015 | ✔ |
| S10 | Entyvio SC pen; HYHUB 510(k) | FY2025 20-F | CLM-007041, CLM-007042 | ✔ |
| S10 | no adherence outcomes published (all four) | INCONCLUSIVE | CLM-007039 | ✔ worded as absence |
| S11 | Nimbus USD 4.0bn upfront (2023); Innovent USD 1.2bn upfront (2025) | Feb 2023; Oct 2025 | CLM-009076, CLM-009078 | ✔ |
| S11 | AbbVie options USD 0.6–1.0bn/yr; none approved | INTERPRETATION (PARTIALLY_SUPPORTED) | CLM-009097 | ✔ |
| S11 | Cerevel USD 8.7bn (2024); −USD 4.5bn within months | closed 1 Aug 2024; impairment after Nov 2024 | CLM-009053, CLM-009054 | ✔ |
| S11 | leverage 2.6x; Amitiza JPY 403.5bn; ~3.1x after USD 5bn | March 2026; ASM-001 150 JPY/USD | CLM-005005, CLM-005014, ASM-033 | ✔ ceiling labelled "planning" |
| S12 | CUDA 10 unprofitable years | NVIDIA, Mar 2026 | CLM-011003 | ✔ |
| S12 | Falcon 9 USD 390m vs USD 1.7–4.0bn | NASA assessment | CLM-011006 | ✔ |
| S12 | Other Bets −USD 7.5bn (2025) incl. USD 2.1bn Waymo charge | Alphabet 10-K | CLM-011009 | ✔ |
| S12 | EYLEA U.S. −42% (2025) | Regeneron 10-K | CLM-011017 | ✔ |
| S13 | envelope ≈ USD 1.92bn + ≈ 1.03bn; ≈ 3% of 14 yrs R&D | ASM-002, ASM-118; R&D JPY 675.9bn FY2025 | CLM-005004 | ✔ ASSUMPTION chip + "not a budget" |
| S13 | council: no funded bet robust to severe pricing pressure | council_reviews.json | — | ✔ |

## Audit corrections carried into the film
- OTTAVA: "announced", not "installed" (dropped from narration).
- Cerevel: USD 4.5bn impairment (not USD 3.5bn), on an USD 8.7bn (8.3bn net) purchase.
- AI outcomes: "no independent evidence found", never "none exists".
- Erosion band labelled SCENARIO; envelope labelled ASSUMPTION; leverage 3.0x described as a planning ceiling, not a covenant.

## Residual evidence risks
- Three INTERPRETATION claims rest on absence of evidence in the sources opened (CLM-006054, CLM-006007, CLM-007039); a later disclosure could overturn them. The film's wording leaves room for that.
- CLM-003007 (IQVIA via trade press) and CLM-005058 (vendor-hosted) are single-interested or secondary sources; both are qualified on screen.
