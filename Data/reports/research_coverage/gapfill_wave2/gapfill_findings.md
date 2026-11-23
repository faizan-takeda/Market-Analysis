# A14 gap-fill findings (wave 2)

Research cutoff 2026-11-21. Shard `A14_gapfill` (SRC/CLM-014000..014074). Every sentence ends with claim IDs; unlabelled reading is marked *(INTERPRETATION)* or *(gap)*. Company releases are interested-party documents. Claim IDs `CLM-0140xx` resolve in `New_mediciine/evidence_library/shards/A14_gapfill/claims.jsonl`; `SRC-004xxx` / `SRC-000xxx` are canonical registry IDs.

## 1. Lilly: earnings 8-K exhibits (Q4 2025, Q3 2026)

**Established**
- Lilly's Q4 2025 release (8-K Ex. 99.1, filed 2026-02-04) reports FY2025 revenue of USD 65,179m (+45%): Mounjaro USD 22,965m, Zepbound USD 13,542m, Verzenio USD 5,723m. [CLM-014000]
- FY2025 R&D was USD 13,337m and acquired IPR&D USD 2,910m. Q4 2025 realized price fell 5% while volume rose 46%. [CLM-014004]
- Initial 2026 guidance was revenue USD 80-83bn, non-GAAP EPS USD 33.50-35.00 and performance margin 46.0-47.5%. [CLM-014001]
- The brief's "USD 91-92bn" is the raised guidance in the Q3 2026 release (2026-10-29), which lifted the revenue midpoint by USD 5.5bn from USD 85-87bn. Q3 2026 revenue was USD 24,397m (+39%). [CLM-014002]
- Q3 2026 revenue included about USD 900m of one-off benefits (USD 410m Jardiance milestones, rebate/discount estimate adjustments). Realized price fell 15% and volume rose 53%. [CLM-014003]
- The 10-K (not the 8-K) is the only filed source that quantifies LillyDirect: self-pay sales through LillyDirect were "a growing portion" of 2025 business, with no dollar figure. [CLM-014006]
- Neither earnings exhibit contains LillyDirect, self-pay, OSA or HFpEF statements. [CLM-014005]
- Zepbound/Mounjaro OSA is recorded as "approved in the U.S. and the EU in 2024" and HFpEF as "submitted in 2024"; the FY2025 10-K shows HFpEF "approved in the EU" only. [CLM-014007]

**Contested / unknown**: exact FDA action dates for OSA and the U.S. HFpEF outcome *(gap)*. Q3/9M 2026 are partial periods.

Integrate into: `New_mediciine/companies/eli_lilly/` dossier §2 (financials) and §4 (commercial/access); correct any "USD 91-92bn" attribution to "raised in Q3 2026 (Oct 29, 2026); initial Feb 2026 guidance USD 80-83bn".

## 2. Lilly manufacturing: announced vs operating

| Site | Announced (amount) | Stated operational date | Evidence of production | Claim |
|---|---|---|---|---|
| Concord, NC | 2022-01-28, USD 1bn, later USD 2bn | n/a | Trade report quoting site head: commercial production and shipments from end-2024 | [CLM-014014] |
| Lebanon, IN (Advanced Therapies) | part of USD 4.5bn (2026-05-06) | opened 2026-05-06 | Opened (company release) | [CLM-014015] |
| Lebanon, IN (API) | USD 9bn total (2024), +USD 4.5bn across two sites | "opens in 2027" | Not operating (USD 9bn 2024 figure: CLM-001038) | [CLM-014015] [CLM-001038] |
| Kenosha, WI | USD 3bn expansion (2024-12-05; USD 4bn total WI) | Spokesperson: production 2028 (news snippet) | Acquired plant existing; expansion under construction | [CLM-014013] |
| Alzey, DE | USD 2.5bn (2023-11) | "beginning in 2027" | None found | [CLM-014012] |
| Limerick, IE | USD 2bn total (expansion 2024-09) | "on track to start in 2026" | Not confirmed; Kinsale (USD 800m) producing since 2023 | [CLM-014011] |
| Houston, TX | USD 6.5bn (2025-09-23) | within five years | Groundbreaking 2026-09-21 | [CLM-014008] |
| Alabama (Huntsville) | >USD 6bn (2025-12-09) | completion 2032 | None; construction from 2026 | [CLM-014009] |
| Pennsylvania (Lehigh Valley) | >USD 3.5bn (2026-01-30) | operational 2031 | None | [CLM-014010] |
| Richmond/Goochland, VA | USD 5bn (2025-09-16) | n/a | Groundbreaking listed in Q3 2026 8-K (announcement terms: CLM-001040) | [CLM-014016] [CLM-001040] |

- The FY2025 10-K names only Indiana, North Carolina, Puerto Rico and Wisconsin among "major production sites" and says more facilities "are expected to come online in future periods". [CLM-014016]
- Capex was USD 7.8bn in 2025 (USD 5.1bn in 2024); construction in progress was USD 13,013m at year-end 2025 versus USD 8,245m. [CLM-014017]
- *(INTERPRETATION)* Most of the "USD 50bn+" pledge is under construction or pre-construction; only Concord, Kinsale and the Lebanon genetic-medicine plant show operating evidence.

Integrate into: `New_mediciine/companies/eli_lilly/` dossier §9 (manufacturing).

## 3. J&J: Varipulse, aticaprant, DePuy Synthes separation, OTTAVA/MONARCH/VELYS, talc

**Varipulse.** FDA's correction notice: approved November 2024; 4 of 132 patients (about 3%) in the U.S. External Evaluation had stroke/TIA versus about 1% expected; Instructions for Use updated 2025-02-14 for all lots (most serious recall class, correction not removal); a post-approval study is planned. [CLM-014018]

**Aticaprant.** J&J discontinued the Phase 3 VENTURA programme on 2025-03-06 for insufficient efficacy; safety was acceptable. [CLM-014019]

**DePuy Synthes.** Intent to separate Orthopaedics announced 2025-10-14 (FY2024 sales about USD 9.2bn; Namal Nawana named Worldwide President). [CLM-014020] The 10-K targets completion 18-24 months after announcement; Orthopaedics FY2025 sales were USD 9.3bn (+1.1%). [CLM-014021]

**Surgical robotics.**
- OTTAVA De Novo DEN250068 was granted 2026-07-21 (received 2025-12-18), Class II, upper-abdominal general laparoscopic procedures. [CLM-014022]
- First IDE cases were early 2025; a hernia IDE was approved late 2025. [CLM-014023]
- The first early-access commercial installation was announced 2026-11-19. [CLM-014024]
- Duato had guided approval "by the end of this year, beginning of next year"; FDA acted earlier. [CLM-014070]
- MONARCH QUEST 3: J&J announced 510(k) clearance 2026-08-17; openFDA lists K260382 (Auris Health, decided 2026-07-25), whose link to the "QUEST 3" name is inferred. [CLM-014025]
- VELYS: openFDA lists K202769, K233227, K240211, K253551 (hip navigation) and K260480 (2026-06-25). [CLM-014026]
- No installed-base or procedure-count figure was found for VELYS, MONARCH or OTTAVA *(gap)*.

**Talc.**
- Judge Lopez denied confirmation of the Red River plan and dismissed the case on 2025-03-31. [CLM-014027]
- J&J reversed about USD 7bn of reserve, did not appeal, and carried a USD 3.4bn reserve at Q4 2025. [CLM-014028]
- On 2026-07-27 J&J announced a USD 5.5bn conditional resolution of about 76,000 remaining ovarian claims (first payment no more than USD 3bn in 2027; at least 95% participation required). Outcome unknown. [CLM-014029]

Integrate into: `New_mediciine/companies/johnson_johnson/` dossier (MedTech/robotics, failures, litigation, portfolio sections) and `industry_transformation/ai_data_robotics/` landscape (OTTAVA/MONARCH/VELYS regulatory record).

## 4. AbbVie: deal terms, Humira settlement history, Juvmo date

- Capstan: USD 2.1bn cash (USD 1.9bn net of cash acquired), asset acquisition expensed to IPR&D in Q3 2025; completion announced 2025-08-19. Lead asset is Phase 1. [CLM-014030]
- Other upfronts in the 10-Ks: Gilgamesh USD 906m, Ichnos Glenmark USD 700m, Gubra USD 350m, ADARx option USD 335m (2025); Aliada USD 1.4bn, Celsius USD 250m (2024). [CLM-014031]
- Aliada: USD 1.4bn cash (announced 2024-10-28, closed December 2024). AbbVie's release states J&J's venture arm JJDC co-founded Aliada and J&J scientists created its BBB-shuttle platform. [CLM-014032]
- Landos: USD 20.42/share (about USD 137.5m) plus a CVR worth up to USD 11.14/share (about USD 75m); completion 2024-05-23 per release snippet. [CLM-014033]
- Nimble: completed 2025-01-23 at USD 288m (USD 210m upfront plus contingent consideration, up to USD 130m further). [CLM-014034]
- Cerevel: USD 45.00/share, USD 8.7bn, completed 2024-08-01; assumed Pfizer licence with up to USD 1.6bn of milestones. [CLM-014035]
- Humira settlements: licences for U.S. biosimilars begin 2023 (Europe 2018); settlement terms are not disclosed. [CLM-014036] The 2019 indirect-purchaser antitrust suit was dismissed in June 2020 and appealed (later outcome not verified). [CLM-014037]
- Humira was about 27% of 2023 revenue. [CLM-014038]
- Juvmo: FDA approval 2026-09-25 (Drugs.com; Reuters snippet); AbbVie announced on 2026-09-28. The two dates are the FDA action and the company release. [CLM-014039] The NDA was submitted September 2025. [CLM-014040]

Integrate into: `New_mediciine/companies/abbvie/` dossier (M&A/pipeline/competitive sections); resolves wave-1's Juvmo 09-25 vs 09-28 question.

## 5. Takeda: Annual Integrated Report, ventures, R&D Day footnote, Entyvio, Amitiza

- The 2026 Annual Integrated Report (FY2025) was opened via pypdf (55 pages). It reports 170+ AI predictive-maintenance agents at Lessines. [CLM-014041]
- One Day Batch Release: six-site pilots, target of 60% shorter release lead time by 2028 and global rollout by 2029. [CLM-014042]
- 63.4% of the workforce actively used generative AI at 31 March 2026 (46.6% a year earlier). [CLM-014043]
- Takami transformation programme: qualitative benefits, no spend disclosed. [CLM-014044]
- AI partners named: Nabla Bio, TetraScience, APHERIS. [CLM-014045]
- On-time in-full rate was 99.6%; BioLife nomogram and Smart Donor Care were rolled out. [CLM-014046]
- R&D Day Dec-2024 footnote: the USD 10-20bn peak revenue range is not adjusted for probability of success and "should not be considered a forecast or target". [CLM-014049]
- Entyvio: some patents expire in 2032; UK/Netherlands revocation actions filed Feb-Apr 2026. [CLM-014050] Biosimilar BLAs (Alvotech AVT16, Fresenius/Polpharma PB016) accepted for FDA review. The Purple Book entry was not opened, so exclusivity status is unconfirmed. [CLM-014051]
- Takeda Ventures, Inc. is a 100%-owned subsidiary; no fund size or Center for External Innovation description exists in primary sources opened. [CLM-014052]
- Amitiza: jury verdict 2026-05-18 of USD 884.9m single damages (subject to trebling for two groups). Takeda booked a JPY 403.5bn provision and plans post-trial motions and appeal. Final judgment amount and post-trial status are unverified. [CLM-014048] [CLM-014047]

Integrate into: `New_mediciine/companies/takeda_public_baseline/` dossier (DD&T, manufacturing, pipeline footnote, IP, litigation).

## 6. AI/robotics: FDA device records, TuneLab, NVIDIA lab, Strateos

- FDA device records for OTTAVA/MONARCH/VELYS are covered in section 3. [CLM-014022] [CLM-014025] [CLM-014026]
- NVIDIA-Lilly co-innovation lab: announced 2026-01-12 with up to USD 1bn over five years; work "expected to begin in South San Francisco early this year". No source opened confirms it is operating. [CLM-014053]
- LillyPod: 1,016 Blackwell Ultra GPUs, more than 9,000 petaflops, inaugurated in Indianapolis; vendor blog, date unresolved. [CLM-014054]
- TuneLab: federated-learning platform on NVIDIA FLARE; partner releases from Charles River (2026-06-18), Twist (2026-09-16), Axcelead and Korean biotechs. No participant count or retraining result. [CLM-014055] [CLM-014056]
- Strateos: aggregators say Multiply Labs acquired it in December 2023, but no primary source was found, so it remains unverified. [CLM-014057]

Integrate into: `New_mediciine/industry_transformation/ai_data_robotics/` landscape and evidence_gaps (items 1, 4, 5).

## 7. Partnerships: deal terms and venture-arm scale

- Lilly asset-acquisition expense: DICE USD 1,915.5m, Versanis USD 604.1m, Emergence USD 406.5m, Mablink USD 256.6m, Beam opt-in USD 216.3m (2023); Morphic USD 2,548.5m (2024). [CLM-014058]
- Lilly 2021-22: Foghorn USD 316.6m, Rigel USD 125.0m, BioMarin PRV USD 110.0m; IPR&D totals USD 970.1m (2021) and USD 908.5m (2022). [CLM-014059]
- Takeda upfronts: HUTCHMED USD 400m (April 2023, up to USD 730m more) and Protagonist USD 300m (April 2024). [CLM-014060]
- Takeda upfronts: Keros USD 200m (February 2025) and Innovent USD 1.2bn (December 2025). [CLM-014061]
- Takeda upfronts: Nimbus USD 4.0bn and AC Immune USD 100m. [CLM-014062]
- Lilly's a16z fund: USD 500m, Lilly-funded (January 2025). No standalone Lilly Ventures fund size found. [CLM-014063]
- JLABS has shrunk: 11 sites (August 2025) after Toronto, Houston and Washington D.C. exits; a snippet says New York is closing, leaving three U.S. sites. [CLM-014064] [CLM-014065]
- No JJDC, AbbVie Ventures or Takeda Ventures portfolio counts were found in primary sources. [CLM-014066] [CLM-014052]

Integrate into: `New_mediciine/industry_transformation/partnerships_ecosystem/` reports (deal ledger, venture arms); update JLABS "scale" statements.

## 8. Leadership statements (one inspected source per company)

- Lilly (Ricks, podcast ~Nov 2025): GLP-1s are "probably 80% of the economic value"; R&D at 20-25% of sales. [CLM-014067] Gateway Labs/Catalyze360 are framed as an experiment that "may not work". [CLM-014068]
- J&J (Duato, Bernstein 2026-05-27): 2026 guidance 6.1% adjusted operational growth, over USD 100bn. [CLM-014069] AI is used in molecule design and clinical operations, with no named programmes or metrics. [CLM-014071] The OTTAVA approval-timing expectation was beaten. [CLM-014070]
- AbbVie (Michael, Q4 2025 call): record USD 61.2bn ex-IPR&D revenue despite about USD 16bn of U.S. Humira erosion; 90 clinical programmes; more than USD 5bn of business development. [CLM-014072]
- Takeda (Weber, Semafor Jan 2026): goal to double research productivity with AI; about 30% shorter narcolepsy development time (single-source claim). [CLM-014073] Kim's May 2026 letter sets "two horizons" and an AI-heavy reorganisation. [CLM-014074]

Integrate into: leadership sections of each company dossier under `New_mediciine/companies/*/` and the strategy inputs.

## Brief and wave-1 corrections surfaced

- "USD 91-92bn" Lilly guidance dates from Q3 2026, not the February release. [CLM-014001] [CLM-014002]
- Juvmo FDA action date is 2026-09-25 and the announcement is 2026-09-28. [CLM-014039]
- Aliada originated in J&J's JJDC/J&J scientists, then sold to AbbVie. [CLM-014032]
- JLABS network is contracting. [CLM-014064]
