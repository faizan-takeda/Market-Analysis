# Editorial review — script against the research (Gate 3)

Reviewer role: editorial/scientific check of `screenplay/scenes.json` against `New_mediciine/evidence_library` and `strategy/`. Each row is a sentence that was changed, cut or qualified during review, with the reason. Rows marked ✔ were verified unchanged.

## Changes made during review

| Scene | Original draft wording | Final wording | Reason |
|---|---|---|---|
| S04 | "no AI programme has changed a cost, a timeline or a revenue line" | "the research found **no independent evidence** that any AI programme has yet changed…" | Audit correction on CLM-006054: absence of evidence in sources opened, not proof of absence. |
| S04 | "J&J's OTTAVA robot is installed" | "Lilly built an open robotic laboratory, then sold it" (OTTAVA dropped from narration) | OTTAVA first clinical install was *announced*; the Lilly lab sale is the better-evidenced "announcements are not outcomes" example [CLM-006013, CLM-006016]. |
| S05 | "Entyvio will lose 383–766bn yen a year" | "If Entyvio erodes the way Humira did, 380 to 770 billion yen a year **is at risk; a scenario, not a forecast**" | ASM-024 is a SCENARIO; the base is global while first entry is a U.S. event (overstates the first three years). On-screen chip reads SCENARIO. |
| S06 | "OTTAVA… " (none) · "Takeda's Shonan labs" | kept; pronunciation fixed ("Shonan" phoneme entry) | ASR heard "its shonan" as one token; narration unchanged, dictionary entry added. |
| S08 | "170 agents save money at Lessines" | "one hundred seventy predictive-maintenance agents run; **their savings are unpublished**" | CLM-005058 is a vendor-hosted self-report; no savings figure exists in sources. |
| S10 | "Takeda will defend Entyvio" | "The Entyvio plan is honest: **delay** erosion, and **measure** it" | Prohibition on claiming LOE can be prevented; matches BET-04 wording. |
| S11 | "AbbVie lost USD 3.5bn on Cerevel" | "AbbVie wrote off **half of Cerevel within months**" (on-screen: −USD 4.5bn) | Audit correction: Q4-2024 impairment USD 4.5bn on an USD 8.7bn purchase [CLM-009054]. |
| S11 | "a five billion dollar acquisition breaches the covenant" | "a five billion dollar purchase **fails the arithmetic**" | 3.0x is a planning ceiling (ASM), not a covenant; 2.6x + Amitiza provision [CLM-005005, CLM-005014]. |
| S12 | "Alphabet lost 7.5bn on moonshots in 2025" | "Alphabet's other bets lost seven and a half billion dollars in twenty twenty-five alone" (on-screen notes the USD 2.1bn Waymo charge) | Matches the registry basis and period [CLM-011006]. |
| S13 | "Takeda will invest 1.9 billion" | "The balanced envelope is **about** one point nine billion… **planning assumptions, not a budget**" | Never present hypothetical amounts as an approved budget (ASM-002, ASM-118). |
| S13 | — | "The council… found **no funded bet robust to severe pricing pressure**; hence the gates." | Added: the council's adverse finding must be in the film, not only in the appendix. |

## Verified unchanged ✔

- S01 Entyvio 21% of FY2025 revenue [CLM-005009]; exclusivity "second half of this decade" (2032 patent horizon; biosimilar review ongoing) [CLM-005017].
- S02 Lilly USD 28.3bn (FY2021) → 65.2bn (FY2025) [CLM-000133, CLM-000137]; tirzepatide 56% of sales [CLM-001003]; realized price −15% Q3-2026 [CLM-014003]; CVS Caremark template exclusion Jul 2025 → Oct 2026 (15 months) [CLM-007011, CLM-007013].
- S03 Humira USD 21.2bn → 4.5bn [CLM-003002, CLM-003015]; Skyrizi + Rinvoq already marketed [CLM-003014, CLM-003084]; ≥97% volume held 14 months [CLM-003007, PARTIALLY_SUPPORTED — IQVIA via trade press, labelled].
- S04 Stelara −41.3% [CLM-000254]; largest brand ≈15% of J&J sales [CLM-002073]; AI outcomes not found [CLM-011052, CLM-006054]; Lilly lab sold [CLM-006013, CLM-006016].
- S06 >270 plasma centres and LA expansion [CLM-005063, CLM-005065, CLM-005060]; oveporexton discovered in Shonan, approved Aug 2026 [CLM-005048, CLM-005029]; rusfertide approved, zasocitinib priority review [CLM-005032, CLM-005035]; three positive Phase 3 readouts [CLM-005042]; cell-therapy exit and JPY 58.2bn write-down [CLM-009084]; soticlestat misses [CLM-005024].
- S07 ARCH: 2,000+ trials, <10 staff, no published outcome [CLM-006032, CLM-006034]; TuneLab data > USD 1bn [CLM-000280, CLM-006056]; compute rentable / data proprietary [CLM-006055, INTERPRETATION].
- S08 63.4% GenAI adoption [CLM-014043]; Lessines 170+ agents [CLM-014041]; agent platform [CLM-005058, vendor self-report]; JPY 200bn savings target [CLM-005059]; measurement independence (BET-17 design).
- S09 mature scripted automation seen in operation [CLM-006002]; cloud-lab fragility: Lilly lab sold [CLM-006013, CLM-006016], Zymergen bought for one-tenth of its IPO value [CLM-006051]; NVIDIA–Lilly lab announced, no outcome yet [CLM-000281, CLM-006007]; Takeda AI partners [CLM-006039, CLM-006041]; first-in-human gate (BET-07, RM-020).
- S10 CVS template move to Stelara biosimilars [CLM-007015]; Entyvio SC pen, HYHUB [CLM-007041, CLM-007042]; SC/home conversion as transferable mechanism [CLM-007053, INTERPRETATION]; no adherence outcomes published [CLM-007039, INCONCLUSIVE — labelled].
- S11 Nimbus USD 4.0bn upfront, Innovent USD 1.2bn [CLM-009076, CLM-009078]; AbbVie options USD 0.6–1.0bn/yr, zero approved [CLM-009097, INTERPRETATION]; Cerevel USD 8.7bn [CLM-009053], USD 4.5bn impairment [CLM-009054]; leverage 2.6x, Amitiza provision [CLM-005005, CLM-005014].
- S12 CUDA ten unprofitable years [CLM-011003]; Falcon 9 USD 390m vs NASA USD 1.7–4.0bn [CLM-011006]; Alphabet Other Bets −USD 7.5bn [CLM-011009]; EYLEA −42% [CLM-011017].
- S13 Medicare price Jan 2028 [CLM-007026]; R&D JPY 675.9bn FY2025 as the 3% base [CLM-005004]; AI partnership gate [CLM-006039].
- S14 closing lines contain no new facts.

## Balance check

Competitor share 19.2% of words / 18.9% of runtime (target 10–20%). Takeda share ≥ 80%. Runtime 6:42 (402.17 s; target 5–7 min). Scenes: 14 (target 14–22).

## Residual editorial risks (disclosed)

- The S05 scenario band applies a U.S.-pattern erosion rate to a global revenue base; stated as overstating the first three years in the strategy, and the film says "scenario, not a forecast".
- The ASR normaliser cannot verify drug-name spelling (Entyvio/Entivio); pronunciation was checked by ear in the voice A/B and the dictionary, not by ASR.
- "Second half of this decade" for Entyvio exclusivity compresses a 2028–2032 range (Medicare price 2028, earliest biosimilar window 2028–2032, patents to 2032) into one phrase; the on-screen markers show the dates individually.
