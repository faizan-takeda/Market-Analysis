# TAKEDA 2040 — What We Must Build Today to Shape the Future of Medicine — master script

Runtime 06:42.17 (402.17 s, 12065 frames @ 30 fps) · 14 scenes · 954 narrated words · voice Kokoro-82M (hexgrad, Apache-2.0 weights) `af_heart` speed 1.12.

Competitor scenes (S02–S04): 183 words (19%), 76.0 s (19% of runtime). Takeda-centred scenes: 81% of words.

Timestamps are measured from the synthesised narration (`timeline/timeline.json`); cue times are ASR word onsets. Kind labels: FACT · INTERPRETATION · HYPOTHESIS · SCENARIO · RECOMMENDATION · ASSUMPTION. Evidence ids resolve in `New_mediciine/evidence_library/claims_registry.jsonl` (see `research/VIDEO_RESEARCH_REFERENCES.md`).

## Recognition

### S01 · The defining question

**00:00.00 → 00:26.23** · 26.23 s · audio 23.13 s · ASR WER 0.02

*Purpose:* Pose the film's question from Takeda's own position, not from competitors.  
*Take-away:* One medicine carries 21% of revenue and is dated; the question is what makes success repeatable.

**Narration**

> A single medicine can carry a company. At Takeda, Entyvio is twenty-one percent of revenue, and its exclusivity ends in the second half of this decade. But every medicine sits inside a wider system: science, data, manufacturing, evidence, partners, patients. So the question for the next fifteen years is not which drug comes next. It is what makes success repeatable.

**On-screen text**

- ENTYVIO · 21% of FY2025 revenue [CLM-005009]
- exclusivity ends in the second half of this decade
- What makes success repeatable?
- TAKEDA 2040

**Evidence**

- CLM-005009 — FACT
- CLM-005017 — FACT

*Accuracy notes:* 21% is Takeda's FY2025 disclosure (April 2025–March 2026). 'Second half of this decade' is Takeda's own wording for loss of regulatory exclusivity; exact biosimilar timing is uncertain per the same filing.

## Tension

### S02 · Lesson one: concentration cuts both ways (Lilly)

**00:26.23 → 00:51.90** · 25.67 s · audio 25.04 s · ASR WER 0.08

*Purpose:* Use Lilly as evidence that one-franchise growth creates exposure before LOE.  
*Take-away:* Growth concentrated in one molecule brings price and payer exposure early.

**Narration**

> Eli Lilly grew from twenty-eight to sixty-five billion dollars in four years; tirzepatide became fifty-six percent of its sales. But concentration cuts both ways: by late twenty twenty-six, realized prices had fallen fifteen percent, and one pharmacy benefit manager kept Lilly's drug off its preferred list for fifteen months. A single franchise creates exposure long before any patent expires.

**On-screen text**

- Eli Lilly revenue FY2021 → FY2025: USD 28.3bn → 65.2bn
- tirzepatide = 56.0% of FY2025 revenue
- Q3 2026 realized prices −15%
- CVS Caremark: off preferred template formularies Jul 2025 → Oct 2026

**Evidence**

- CLM-000133 — FACT
- CLM-000137 — FACT
- CLM-001003 — FACT
- CLM-014003 — FACT
- CLM-007011 — FACT
- CLM-007013 — FACT

**Non-claim labels on screen**

- closing sentence: INTERPRETATION

*Accuracy notes:* USD 28,318m FY2021 → USD 65,179m FY2025 (US GAAP, 10-K). Tirzepatide = Mounjaro + Zepbound, 56.0% of FY2025 revenue (computed from 10-K tables). Price decline is Lilly's Q3 2026 statement (realised prices -15% YoY). CVS Caremark removed Zepbound from commercial template formularies 1 Jul 2025 and restored it 1 Oct 2026 (15 months, computed). 'Long before any patent expires': tirzepatide patent 2036 (CLM-000250).

### S03 · Lesson two: the successor must exist before the cliff (AbbVie)

**00:51.90 → 01:15.73** · 23.83 s · audio 23.23 s · ASR WER 0.06

*Purpose:* Show the one competitor mechanism that transfers cleanly to Takeda's Entyvio problem.  
*Take-away:* Replacement worked because successors were already marketed; contracting only delays.

**Narration**

> AbbVie faced the cliff Takeda now faces. Humira fell from twenty-one billion dollars to four and a half billion within three years of biosimilar entry. Yet AbbVie recovered, because Skyrizi and Rinvoq were already on the market, across Humira's major indications. Contracting held ninety-seven percent of volume for over a year. It delayed the fall. It did not prevent it.

**On-screen text**

- Humira: USD 21.2bn (2022) → 4.5bn (2025)
- Skyrizi + Rinvoq: USD 7.7bn → 25.9bn
- ≥97% of U.S. volume held to March 2024 — then the fall
- Successors marketed before the cliff

**Evidence**

- CLM-003002 — FACT
- CLM-003015 — FACT
- CLM-003014 — INTERPRETATION (arithmetic on 10-K figures)
- CLM-003084 — INTERPRETATION
- CLM-003007 — FACT (PARTIALLY_SUPPORTED; IQVIA via trade press)

*Accuracy notes:* Humira global net revenue USD 21,237m (2022) → 4,540m (2025); U.S. biosimilar entry began January 2023. AbbVie total revenue dipped in 2023 and exceeded the 2022 peak only in 2025 (CLM-003015). Skyrizi + Rinvoq USD 7,687m → 25,866m. '≥97% of U.S. adalimumab volume through March 2024' (14 months after entry) is a trade-press/IQVIA figure, PARTIALLY_SUPPORTED. Steep U.S. declines followed the April 2024 CVS formulary change (association, not proven causation, CLM-003010).

### S04 · Lesson three: diversification works; AI has no outcome yet (J&J and all four)

**01:15.73 → 01:42.23** · 26.50 s · audio 25.88 s · ASR WER 0.04

*Purpose:* Close the competitor act with the diversification lesson and the honest AI reality check.  
*Take-away:* Diversified bases absorb cliffs; no AI programme in the study has an independent outcome.

**Narration**

> Johnson and Johnson absorbed a forty-one percent fall in Stelara with a diversified base; its largest brand is only fifteen percent of sales. And artificial intelligence? Across all four companies, the research found no independent evidence that any AI programme has yet changed a cost, a timeline, or a revenue line. Lilly built an open robotic laboratory, then sold it. Announcements are not outcomes.

**On-screen text**

- Stelara −41.3% (FY2025) · largest J&J brand ≈15% of sales
- AI programmes: announcements ✓ · independent outcomes — none found
- Lilly robotic lab → sold to a CRO (2024)
- Announcements are not outcomes

**Evidence**

- CLM-000254 — FACT
- CLM-002073 — INTERPRETATION (arithmetic on 10-K)
- CLM-011052 — INTERPRETATION (PARTIALLY_SUPPORTED)
- CLM-006054 — INTERPRETATION (PARTIALLY_SUPPORTED; audit: wording stronger than sources — the film uses the narrower 'no independent evidence found')
- CLM-006013 — FACT
- CLM-006016 — FACT

*Accuracy notes:* Stelara −41.3% to USD 6,078m in FY2025; DARZALEX ≈15.2% of FY2025 sales. 'No independent evidence' is the audited, narrow form: no source opened shows a published discovery outcome, cost saving or revenue effect from any of the four companies' AI initiatives. Lilly's Life Sciences Studio was acquired by Arctoris (a CRO) in 2024; Lilly's reason is undisclosed (CLM-006017, contested).

## Tension → Discovery

### S05 · The central challenge

**01:42.23 → 02:12.93** · 30.70 s · audio 30.10 s · ASR WER 0.11

*Purpose:* Quantify Takeda's dated exposure and state the task.  
*Take-away:* Defend what is dated; build what repeats.

**Narration**

> Takeda. Entyvio brings in nine hundred fifty-eight billion yen. Medicare price negotiation takes effect in January twenty twenty-eight, and two biosimilar applications are already under FDA review. Vyvanse lost two hundred twenty billion yen in two years. If Entyvio erodes the way Humira did, three hundred eighty to seven hundred seventy billion yen a year is at risk; a scenario, not a forecast. But it defines the task: defend what is dated, and build what repeats.

**On-screen text**

- ENTYVIO JPY 958.0bn · 21%
- Jan 2028 · Medicare negotiated price
- FDA review · 2 biosimilar applications
- Vyvanse: JPY 423.2bn → 203.2bn in two years
- SCENARIO 40–80% erosion → JPY 383–766bn/yr at risk (ASM-024) · not a forecast
- DEFEND what is dated · BUILD what repeats

**Evidence**

- CLM-005009 — FACT
- CLM-007026 — FACT
- CLM-014051 — FACT (PARTIALLY_SUPPORTED; trade reporting + company releases)
- CLM-005015 — FACT
- CLM-005001 — FACT
- CLM-005002 — FACT

**Non-claim labels on screen**

- range 383–766bn: SCENARIO (ASM-024: 40–80% erosion over three years applied to JPY 958.0bn; not a forecast)

*Accuracy notes:* Entyvio JPY 958.0bn FY2025. CMS selected Entyvio in January 2026 for a negotiated price effective January 2028. Two vedolizumab biosimilar BLAs accepted for FDA review (Alvotech AVT16; Fresenius Kabi/Polpharma PB016). Vyvanse JPY 423.2bn (FY2023) → 203.2bn (FY2025) = −220.0bn. Scenario range = 40%/80% × 958.0 = 383/766 JPY bn per year; the base is global while first entry is a U.S. event, so the range overstates the first three years (stated in the strategy).

## Discovery

### S06 · What Takeda already has

**02:12.93 → 02:39.50** · 26.57 s · audio 25.94 s · ASR WER 0.14

*Purpose:* Establish the baseline strengths so recommendations build on them, not around them.  
*Take-away:* Plasma scale, in-house orexin science, late-stage execution and stop discipline are evidenced strengths.

**Narration**

> Takeda is not starting from zero. More than two hundred seventy plasma centres, with fractionation capacity expanding. Its Shonan labs discovered oveporexton, approved in August twenty twenty-six for narcolepsy. Rusfertide followed; zasocitinib is under priority review. Three Phase three readouts came in positive, on plan. And Takeda has shown it can stop: it exited cell therapy and took the write-down.

**On-screen text**

- 270+ plasma centres · USD 230m LA fractionation expansion
- Oveporexton — discovered in Shonan — FDA approved 5 Aug 2026
- Rusfertide approved 28 Aug 2026 · Zasocitinib NDA under Priority Review
- 3 of 3 Phase 3 readouts positive on the 2024 plan
- Stop discipline: cell therapy exit, JPY 58.2bn impairment
- Public-evidence gaps: AI outcomes · lab automation · patient services

**Evidence**

- CLM-005063 — FACT
- CLM-005060 — FACT
- CLM-005065 — FACT
- CLM-005048 — FACT
- CLM-005029 — FACT
- CLM-005032 — FACT
- CLM-005035 — FACT
- CLM-005042 — FACT
- CLM-009084 — FACT
- CLM-005024 — FACT

**Non-claim labels on screen**

- all: FACT

*Accuracy notes:* 'More than 270' is Takeda's FY2025 wording (275 in FY2024). USD 230m Los Angeles expansion announced June 2024 (up to 2m litres/yr). Oveporexton (Orzeyful) FDA approval 5 Aug 2026 for narcolepsy type 1; discovered in Shonan per Takeda. Rusfertide (Mimrylo) approved 28 Aug 2026 (licensed from Protagonist). Zasocitinib NDA accepted under Priority Review 14 Sep 2026 (Nimbus acquisition). Dec-2024 R&D Day planned three 2025 readouts; all three read out positive (company-reported). Cell-therapy exit: JPY 58.2bn impairment (FY2025 20-F); soticlestat discontinued Jan 2025.

## Strategic possibility

### S07 · From products to repeatable scientific advantage

**02:39.50 → 03:07.30** · 27.80 s · audio 27.20 s · ASR WER 0.05

*Purpose:* Introduce the first build: proprietary decision-linked data as the compounding asset.  
*Take-away:* Compute and models are purchasable; decision-linked data is not. Build the governed data and decision layer.

**Narration**

> What should Takeda build first? What rivals cannot buy. Compute can be rented and models are converging; what stays proprietary is the data a company generates when it decides. AbbVie connected two thousand trials into one research hub with fewer than ten staff. It has published no outcome yet. Takeda's version: a governed data and decision layer, where every experiment and every go or no-go is logged against a baseline.

**On-screen text**

- Compute: rentable · Models: converging · Data: proprietary
- AbbVie ARCH: 2,000+ trials · <10 full-time staff
- Lilly TuneLab: data cost > USD 1bn (company estimate)
- No published outcome — either
- BET-01 Governed data & decision layer — BUILD (thin slice)

**Evidence**

- CLM-006055 — INTERPRETATION (PARTIALLY_SUPPORTED)
- CLM-006056 — INTERPRETATION
- CLM-006032 — FACT
- CLM-006034 — FACT
- CLM-000280 — FACT (company estimate)
- CLM-011052 — INTERPRETATION

**Non-claim labels on screen**

- BET-01: RECOMMENDATION (BUILD, thin slice; confidence: hypothesis)

*Accuracy notes:* ARCH: conceived 2020, built by fewer than ten full-time AbbVie staff plus contractors; 2,000+ trials' de-identified data reusable internally (company statements at Bio-IT World 2023). 'Over USD 1bn' is Lilly's own estimate of historical data cost. 'Models are converging' is the strategy's INTERPRETATION of shared federated models (TuneLab, AISB).

### S08 · Data as a strategic asset: baseline first, then claim

**03:07.30 → 03:27.40** · 20.10 s · audio 19.48 s · ASR WER 0.03

*Purpose:* Convert the data theme into a measurement discipline Takeda can apply immediately.  
*Take-away:* Takeda has adoption; it needs measured value with independent ownership.

**Narration**

> Takeda already has the platform. Sixty-three percent of the workforce uses generative AI. But usage is adoption, not value. At Lessines, one hundred seventy predictive-maintenance agents run; their savings are unpublished. Baseline first, then claim. And whoever measures should not own the savings target.

**On-screen text**

- Agent platform: 10,000+ employees
- 63.4% workforce GenAI usage (Mar 2026) — adoption, not value
- Lessines: 170+ predictive-maintenance agents — savings not published
- BET-17: baseline → claim · measurement owner ≠ savings owner

**Evidence**

- CLM-005058 — FACT (PARTIALLY_SUPPORTED; vendor-hosted self-report)
- CLM-014043 — FACT (adoption metric per audit)
- CLM-014041 — FACT (company report; no outcome figure)
- CLM-005059 — FACT

**Non-claim labels on screen**

- BET-17: RECOMMENDATION (EXPERIMENT; owner independent of the CFO savings target)

*Accuracy notes:* '10,000+ employees' and the agent platform come from a Databricks-hosted summary of Takeda's own session (interested sources). 63.4% workforce GenAI usage at 31 March 2026 (Takeda Annual Integrated Report). 170+ predictive-maintenance agents at Lessines (same report); no savings figure disclosed. The JPY 200bn savings target is owned by the CFO's transformation programme.

### S09 · The intelligent laboratory

**03:27.40 → 03:59.13** · 31.73 s · audio 31.12 s · ASR WER 0.00

*Purpose:* Separate established automation from emerging and undemonstrated autonomy; recommend rent-and-gate.  
*Take-away:* Climb the automation ladder only when triggers fire; gate AI partners on first-in-human data.

**Narration**

> In the laboratory, the same rule applies. Scripted automation, robots that dose, measure and screen, is mature and sold as a service. Remote cloud labs work but have proved commercially fragile. An AI that plans its own experiments is a prototype; first clinical data from such partnerships is still a year or two away. A fully autonomous discovery loop has not been demonstrated anywhere. So: rent automation, climb only when triggers fire, and gate the AI partners on first-in-human data.

**On-screen text**

- 1 · Scripted automation — operational (sold as a service)
- 2 · Remote cloud lab — works, commercially fragile
- 3 · AI-planned experiments — prototype; first-in-human data 1–2 yrs out
- 4 · Autonomous discovery loop — not demonstrated
- BET-09 rent · BET-10 owned lab: REJECT (triggers) · BET-07 gate on FIH data

**Evidence**

- CLM-006013 — FACT
- CLM-006016 — FACT
- CLM-006002 — FACT
- CLM-006051 — FACT (industry case, not one of the four)
- CLM-000281 — FACT (announcement, concept stage)
- CLM-006039 — FACT (company expectation)
- CLM-006041 — FACT
- CLM-006007 — FACT

**Non-claim labels on screen**

- ladder readiness: INTERPRETATION (autonomous_lab_reality_check.md)
- BET-09/BET-10/BET-07: RECOMMENDATION

*Accuracy notes:* Ladder: scripted automation operational/commodity (Arctoris platform, Lilly Lebanon robots); remote cloud lab operational but commercially fragile (Lilly's Studio divested to a CRO; Zymergen distressed sale as industry calibration); AI-planned loop prototype–pilot (Nabla expects first-in-human data within one to two years of Oct 2025; NVIDIA–Lilly lab is an announcement); autonomous end-to-end discovery with clinical outcome: not demonstrated in any source opened. Takeda partners: Nabla (> USD 1bn success-based), Iambic (> USD 1.7bn success-based).

### S10 · Commercial execution and care: the whole value chain

**03:59.13 → 04:29.17** · 30.03 s · audio 29.42 s · ASR WER 0.09

*Purpose:* Connect evidence to access decisions and patients; set honest expectations for Entyvio defence.  
*Take-away:* Delay and measure erosion; resolve the channel question; be the first to measure patient outcomes.

**Narration**

> Pharmacy benefit managers now decide biosimilar outcomes: when CVS moved its templates to Stelara biosimilars, most members paid nothing. The Entyvio plan is honest: delay erosion, and measure it. The subcutaneous pen drives uptake and the HYHUB device brings plasma therapy home. But the pharmacy channel is also where biosimilars win. No company studied publishes adherence outcomes; Takeda can be the first, starting with the oveporexton launch.

**On-screen text**

- CVS template formularies → Stelara biosimilars (Jul 2026) · most members $0
- Entyvio: delay and measure · benefit-channel gate 2027 H1 (BET-04)
- SC pen drives uptake · HYHUB moves Hyqvia into the home (BET-11)
- Caution: the pharmacy channel is where biosimilars win
- Adherence outcomes published: none (all four companies)
- BET-12: measure from the oveporexton launch

**Evidence**

- CLM-007015 — FACT
- CLM-007026 — FACT
- CLM-007041 — FACT
- CLM-007042 — FACT
- CLM-007053 — INTERPRETATION (PARTIALLY_SUPPORTED)
- CLM-007039 — FACT (INCONCLUSIVE: absence of published outcomes in sources opened)
- CLM-003007 — FACT
- CLM-003002 — FACT

**Non-claim labels on screen**

- BET-04/BET-11/BET-12: RECOMMENDATION
- RM-003: ASSUMPTION (gate date 2027 H1)

*Accuracy notes:* CVS Health: from 1 Jul 2026 its most common commercial template formularies prefer interchangeable Stelara biosimilars, most members paying $0. Benefit-channel gate (medical vs pharmacy split) is RM-003, 2027 H1, an ASSUMPTION; the registry has no Entyvio channel split. Entyvio SC 'continues to drive increased patient uptake' per Takeda's 20-F; HYHUB/HYHUB DUO 510(k) July 2025 for home transfer of Hyqvia. The SC-vs-PBM tension is the strategy's stated BET-04/BET-11 conflict. No source opened for any of the four companies reports adherence or persistence outcomes for patient programmes.

## Credible action

### S11 · Partnerships, acquisitions and the leverage test

**04:29.17 → 04:58.30** · 29.13 s · audio 28.51 s · ASR WER 0.14

*Purpose:* Show Takeda's actual external-innovation instrument and why the large acquisition is rejected.  
*Take-away:* Mid-size licensing fits the leverage ceiling; options are unproven; a USD 5bn purchase fails the arithmetic.

**Narration**

> Takeda's instrument for partnerships is the mid-sized licence: Nimbus for four billion dollars upfront, Innovent for one point two. AbbVie runs early options worth up to a billion a year, yet none signed in this period has produced an approved product. AbbVie wrote off half of Cerevel within months. At two point six times leverage, with Amitiza pending, a five billion dollar purchase fails the arithmetic. Fund a licensing channel instead, released when leverage allows.

**On-screen text**

- Nimbus USD 4.0bn upfront · Innovent USD 1.2bn upfront
- AbbVie early options: USD 0.6–1.0bn/yr · approvals from options in window: none
- Cerevel: USD 4.5bn impairment within months
- Leverage 2.6x → ~3.1x after USD 5bn (council arithmetic, ASM-033 ceiling 3.0x)
- BET-15 USD 5bn+ purchase: REJECT · BET-18 licensing channel: PARTNER (contingent)

**Evidence**

- CLM-009076 — FACT
- CLM-009078 — FACT
- CLM-009097 — INTERPRETATION (PARTIALLY_SUPPORTED)
- CLM-009053 — FACT
- CLM-009054 — FACT
- CLM-005005 — FACT (2.6x at Mar 2026 confirmed by audit)
- CLM-005014 — FACT

**Non-claim labels on screen**

- leverage 3.13x / 3.41x: ASSUMPTION (council arithmetic, ASM-033 ceiling 3.0x, ASM-119)
- BET-15 REJECT / BET-18 PARTNER: RECOMMENDATION (Director decision record)

*Accuracy notes:* Nimbus: USD 4.0bn upfront (Feb 2023) + up to USD 2bn milestones. Innovent: USD 1.2bn upfront incl. USD 100m equity (Oct 2025). AbbVie 'other' upfront stream USD 0.6–1.0bn/yr. 'No option from the window has produced an approved product' is the comparison's finding (HYPOTHESIS about durability). Emraclidine: Phase 2 miss Nov 2024, USD 4.5bn impairment in Q4 2024 (Cerevel closed Aug 2024). Leverage 2.6x adjusted net debt/EBITDA at 31 Mar 2026; Amitiza provision JPY 403.5bn. '5bn fails the arithmetic' is the council's computation (≈3.1x, ≈3.4x if the provision is debt-funded) against a 3.0x planning ceiling, ignoring free cash flow. Cerevel consideration USD 8.7bn (USD 8.3bn net of cash), closed 2024-08-01 [CLM-009053]; USD 4.5bn emraclidine impairment recorded after the November 2024 EMPOWER failures [CLM-009054].

### S12 · Long-term compounding: what the platform analogies really say

**04:58.30 → 05:30.87** · 32.57 s · audio 31.96 s · ASR WER 0.04

*Purpose:* Use the Module 2 analogies to set realistic expectations for platform bets.  
*Take-away:* Platforms compound slowly and protect no single product; cap the long bets and compound Takeda's own strengths.

**Narration**

> And the platform dream? NVIDIA says CUDA made no money for ten years. SpaceX built Falcon nine for a fraction of NASA's estimate. Alphabet's other bets lost seven and a half billion dollars in twenty twenty-five alone. Regeneron's discovery platform did not stop its lead product falling forty-two percent. Platforms compound slowly and protect no single product. So Takeda's long bets are capped options with stop rules, and the strengths it compounds are its own: plasma process data, and orexin biology.

**On-screen text**

- CUDA: 'didn't make money for 10 years' — NVIDIA
- Falcon 9: USD 390m vs NASA estimate USD 1.7–4.0bn
- Alphabet Other Bets: −USD 7.5bn (2025)
- EYLEA U.S. sales −42% (2025) despite a discovery platform
- Analogies, not proof · capped options with stop rules
- Compound what is Takeda's own: plasma process data · orexin biology

**Evidence**

- CLM-011003 — FACT (NVIDIA executive statement)
- CLM-011004 — FACT
- CLM-011006 — FACT (NASA assessment)
- CLM-011009 — FACT (Alphabet 10-K)
- CLM-011017 — FACT (Regeneron 10-K)

**Non-claim labels on screen**

- analogy readings: HYPOTHESIS generators, not proof (platform_moats/analogies_platform_strategies.md)
- BET-02 EXPERIMENT / BET-03 BUILD (gated) / BET-06 PARTNER: RECOMMENDATION

*Accuracy notes:* CUDA: NVIDIA's Ian Buck (March 2026) said CUDA cost billions and NVIDIA 'didn't make money for 10 years' on it. Falcon 9 + Falcon 1 development ≈ USD 390m (SpaceX figure verified by NASA) vs NASA model estimates USD 1.7–4.0bn. Alphabet Other Bets operating loss USD 7,515m in 2025 (incl. a USD 2.1bn Waymo compensation charge). EYLEA U.S. net sales −42% in 2025 (competition and the shift to EYLEA HD). The film labels these as analogies; the strategy treats them as hypothesis generators.

### S13 · Execution: the sequence, the gates, the envelope

**05:30.87 → 06:06.63** · 35.77 s · audio 35.15 s · ASR WER 0.09

*Purpose:* Give leadership the first three years, the gate logic and the honest size of the ask.  
*Take-away:* Start everything measurable in 2027; decide at dated gates; the envelope is a gated planning assumption.

**Narration**

> The sequence. Twenty twenty-seven: baselines, the data standard, rented automation and the Entyvio channel decision, together. Twenty twenty-eight: the Medicare price lands, the biosimilar playbook goes live, the AI partnerships face a go or no-go on data. The balanced envelope is about one point nine billion dollars over fourteen years, roughly three percent of today's R and D, plus a contingent pool for licences: planning assumptions, not a budget. The council that challenged this plan found no funded bet robust to severe pricing pressure; hence the gates.

**On-screen text**

- 2027 · baselines · data standard · rented automation · Entyvio channel gate
- 2028 · Medicare price (Jan) · biosimilar playbook live · AI partnerships go/no-go
- 2029 · plasma scale decision
- discovery → feasibility → pilot → scale · stop rules at every gate
- Balanced envelope: ~USD 1.92bn committed + ~1.03bn contingent (2027–2040) · ASSUMPTION, not a budget
- Council stress test: no funded bet robust to severe pricing pressure

**Evidence**

- CLM-007026 — FACT
- CLM-005004 — FACT
- CLM-006039 — FACT

**Non-claim labels on screen**

- RM-001/002/003/005 (2027 H1): ASSUMPTION (roadmap)
- RM-016 Jan 2028 Medicare price: FACT (CLM-007026)
- RM-026 playbook 2028 H1 / RM-020 AI go-no-go 2028 H2 / RM-025 plasma scale 2029 H2: ASSUMPTION (roadmap v2)
- ASM-002 USD 1,920m; ASM-118 ~1,030m contingent; ~3% of 14 years of R&D at ASM-001: ASSUMPTION
- council finding (no funded bet robust in SCN-3): council review (strategy/critical_challenges/scenario_stress_test.md)

*Accuracy notes:* Dates are roadmap v2 milestones (ASSUMPTION) except the Medicare effective date (FACT). Envelope: balanced USD 1,920m committed at gates, cumulative 2027–2040, plus ~USD 1,030m contingent headroom for BET-18; roughly 3.0% of fourteen years of flat R&D (JPY 675.9bn FY2025 at ASM-001 150 JPY/USD). Takeda's actual budget is not public (IVB-014). The council's stress test rated no funded bet robust under SCN-3 (pricing/biosimilar pressure).

## Conviction

### S14 · Closing: build the system around the medicines

**06:06.63 → 06:42.17** · 35.53 s · audio 30.41 s · ASR WER 0.03

*Purpose:* Land a memorable, evidence-consistent conclusion.  
*Take-away:* No single drug, deal or technology secures the decade; a repeatable, measured, connected organisation does.

**Narration**

> No single drug secures the next decade. No acquisition. No technology. What endures is an organisation that discovers repeatedly, measures honestly, connects evidence to patients, and learns faster than the market moves. Takeda has the raw material: a franchise to defend, launches in hand, plasma and orexin to compound, and the discipline to stop. Build the system around them. Start in twenty twenty-seven. Measure from day one. Decide at every gate.

**On-screen text**

- Not one drug · not one acquisition · not one technology
- Discover repeatedly · measure honestly · connect evidence to patients · learn faster
- Start in 2027 · Measure from day one · Decide at every gate
- TAKEDA 2040
- Evidence: MEDICINE 2040 encyclopedia · 524 sources · 1,401 claims · cutoff 2026-11-21

**Evidence**

- CLM-005009 — FACT
- CLM-005029 — FACT
- CLM-005032 — FACT
- CLM-005035 — FACT
- CLM-005063 — FACT
- CLM-005048 — FACT
- CLM-009084 — FACT

**Non-claim labels on screen**

- closing synthesis: RECOMMENDATION (deliverables/recommendations.md)
- raw-material list: FACT (see S06)

*Accuracy notes:* The closing restates the strategy's RECOMMENDATIONS; every 'raw material' item is a FACT established in S06. No claim of eliminating LOE is made.

