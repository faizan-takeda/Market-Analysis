# A10-bis Task 3: kind and status discipline on the new shards

Date 2026-11-21. Scope: claims with `merged_from_shard` in A7_commercial (59), A8_policy (55), A12_pipeline (153), A14_gapfill (75), A11_strategy (100). All 442 claims were screened by script (kind, status, source access status, source tier, maturity, wording) and the hits were read by hand. Proposals only; no registry was edited.

## Summary

| Check | Hits | Verdict |
|---|---|---|
| SUPPORTED resting only on a metadata_only, blocked or paywalled source | 0 | Clean. 12 claims cite a metadata_only source as their only support and every one is already PARTIALLY_SUPPORTED, NEEDS_MORE_RESEARCH or INCONCLUSIVE |
| FACT+SUPPORTED on T2 company sources only and not flagged single_interested_source | 7 (all A14) | Flag |
| FACT+SUPPORTED on T3/T4 sources only | 14 | Review 5, accept 9 |
| FACT claims with interpretive wording | 0 real, 3 mild | Accept with edits |
| FACT claims that are negative findings ("not located", "no evidence") | 9 | Retype or tag |
| AI or robotics claims in A14 and A7 without a maturity tag | 0 FACT; 37 INTERPRETATION, HYPOTHESIS or RECOMMENDATION claims in A11 | Tag with the maturity of the evidence they cite |
| Maturity tags that do not fit the evidence | 4 | Retag |
| A11 RECOMMENDATION labelled EVIDENCE_BACKED while status is PARTIALLY_SUPPORTED | 7 of 7 | Relabel |
| A11 HYPOTHESIS that reads as a recommendation | 2 | Reword or retype |

## 1. FACT+SUPPORTED resting only on company sources, not flagged single_interested_source (propose flag)

All seven are Lilly or J&J manufacturing or restructuring announcements, the claims where announced-versus-operating matters most:

CLM-014008 (Houston 6.5bn), CLM-014009 (Huntsville), CLM-014010 (Lehigh Valley), CLM-014011 (Limerick, Kinsale), CLM-014012 (Alzey), CLM-014015 (Lebanon), CLM-014020 (J&J Orthopaedics separation intent).

Each states what the company announced or expects. The statements themselves are worded as announcements ("expected to be operational", "will be operational in 2031"), so the kind and status are right; the missing flag is the defect. Only CLM-014014 (Concord, operating) is PARTIALLY_SUPPORTED because it uses a trade article; no Lilly site is shown operating by an independent or regulator source, which the manufacturing report should say.

## 2. SUPPORTED on T3 or T4 sources only (14)

CLM-008024 (Supreme Court cert denial, law-firm summaries), CLM-008039, CLM-008040, CLM-008041, CLM-008042 (D.C. Circuit 340B ruling, HRSA pilot, hospital suit: trade and HFMA reports), CLM-007013 (CVS restoration of Zepbound, trade article), CLM-007045 (Pear bankruptcy), CLM-014027 (Red River dismissal), CLM-014063 (a16z fund), CLM-014064 (JLABS withdrawal, BetaKit), CLM-014067, CLM-014068, CLM-014072 (executive statements via podcast and call summaries), CLM-011003 (CUDA quote; already flagged single_interested_source).

Propose: CLM-008024, CLM-008039..008042 and CLM-014027 are court events with a primary record (supremecourt.gov docket 25-749, D.C. Circuit opinion, S.D. Tex. order); keep SUPPORTED only after a primary record is stored, otherwise PARTIALLY_SUPPORTED. The executive-statement claims are correctly worded as "said" and can stay SUPPORTED as attribution. CLM-007013 was confirmed by me against a second outlet (Managed Healthcare Executive) and is fine.

## 3. Interpretive wording inside FACT claims

No FACT claim states a recommendation or forecast in the project's voice. Three mild cases:

- CLM-014039 ("The two dates therefore reflect FDA action versus company announcement"): an inference; my openFDA check confirms it, so keep, but split the inference into the implications field.
- CLM-014070 ("earlier than that stated expectation"): a comparison made by the auditor; move to implications.
- A12 FACT claims carry an `implications` field with "Novelty read: ... (INTERPRETATION)" text; the label is present, so this is acceptable.

## 4. Negative findings typed FACT (9)

CLM-007039, CLM-007048, CLM-008017, CLM-014005, CLM-014052, CLM-014057, CLM-014066 and, from earlier shards, CLM-005052, CLM-005072 are statements of the form "no source opened shows X". They are typed FACT with status INCONCLUSIVE, NEEDS_MORE_RESEARCH or SUPPORTED. The schema has no EVIDENCE_GAP kind, so propose a tag `negative_finding` plus a stated search scope (sources opened, terms used), and keep CLM-014005 SUPPORTED only for the two releases it names. CLM-008007 (a methodological statement that no causal inference is drawn) is INTERPRETATION with status INCONCLUSIVE; a disclaimer has no truth status and should be a note, not a claim.

## 5. Maturity tags

Missing: none on A14 or A7 FACT claims that concern AI or robotics. A11 INTERPRETATION, HYPOTHESIS and RECOMMENDATION claims about AI and automation (CLM-011025, 011029, 011031, 011033, 011035, 011043, 011045, 011047, 011048, 011053, 011060, 011064..011066, 011071, 011074, 011076, 011080..011083, 011085, 011087..011090, 011092..011095, 011097, 011098) have no maturity tag. They are claims about options, not capabilities, so propose a tag of the maturity of the cited competitor evidence (for example CLM-011065 rests on the divested Arctoris model, OPERATIONAL but commodity; CLM-011060 on PROTOTYPE partnerships).

Tags that do not fit the evidence:

- CLM-014073 DEMONSTRATED_OUTCOME: a former CEO's interview claim of about 30% shorter narcolepsy trial development, no baseline or method, T3, PARTIALLY_SUPPORTED. It contradicts the master report's statement that no AI initiative shows a demonstrated outcome. Retag PILOT and flag single_interested_source (conflict record filed).
- CLM-014043 SCALED: 63.4% of staff "actively using" generative AI and 30.9% taking a course. Usage and training counts are adoption metrics; A10 round 1 made the same retag for J&J course completions. Propose OPERATIONAL.
- CLM-014030 PROTOTYPE on the Capstan acquisition (an asset-acquisition accounting claim). Not an AI or robotics capability; use not_applicable.
- CLM-014025 OPERATIONAL on the MONARCH QUEST 3 clearance: the claim is PARTIALLY_SUPPORTED and the "AI-powered" features are company marketing; the openFDA record only shows substantial equivalence for the platform. Propose PILOT for the AI feature, OPERATIONAL only for the device.
- CLM-014022, CLM-014023, CLM-014024 are tagged PILOT for OTTAVA (authorised, one announced early-access installation). Reasonable and consistent with the master text.

## 6. A11 strategy claims

Counts: 52 INTERPRETATION, 17 HYPOTHESIS, 7 RECOMMENDATION, 24 FACT. Status: 62 PARTIALLY_SUPPORTED, 17 NEEDS_MORE_RESEARCH, 21 SUPPORTED.

- **EVIDENCE_BACKED recommendations are PARTIALLY_SUPPORTED.** CLM-011054, 011060, 011065, 011068, 011069, 011072 and 011073 carry the label EVIDENCE_BACKED in their text and in the domain tables while the registry status is PARTIALLY_SUPPORTED. One label should win. Propose relabelling them "SUPPORTED_BY_ANALOGY: based on competitor evidence, not tested on Takeda", or keeping EVIDENCE_BACKED and upgrading the status after the weak step is repaired. The weakest: CLM-011054 (pooled models beat Takeda-only models; the evidence is a vendor-organised consortium result against public models, not peer reviewed), CLM-011072 (relies on T4 Drug Channels and a CVS release for Entyvio biosimilar risk; Entyvio biosimilars have FDA review dates only from a trade snippet, CLM-014051), CLM-011073 (a "do not" recommendation resting on CRS description of copay rules and an inference about fit).
- **HYPOTHESIS that reads as a recommendation.** CLM-011045 ("Takeda should not attempt to productise ...") and CLM-011066 ("Takeda should set explicit triggers ...") use directive wording. Retype as RECOMMENDATION with its own evidence label or reword as "Takeda could".
- **FACT claims in A11.** I re-opened 19 of the 24 against primary text (NVIDIA, Alphabet, Regeneron, TSMC, Amazon and Intuitive 10-K or 20-F; NASA documents; Nobel; Roche). All numbers match. CLM-011003 (CUDA quotes) could not be re-opened (Computer Weekly 403) and rests on one interested speaker via T3; it is correctly flagged. CLM-011013 and CLM-011014 rest on snippets (metadata_only) and are PARTIALLY_SUPPORTED, correctly.
- **Analogy transfer is stated as a hypothesis in the registry but as a table of options in the domain files** (see citation-consistency findings 11 and 17). The registry labelling is the more careful of the two.

## 7. Other discipline points

- CLM-007000 and CLM-007002 are SUPPORTED on press-release passages I could not re-open (403); the stored passage for CLM-007002 does not contain half the prices in the statement. Propose PARTIALLY_SUPPORTED until the full text is stored.
- CLM-012137 and CLM-012136 are SUPPORTED (registry values match) but their pairing with a company statement creates an apparent contradiction (conflict records filed).
- A12 deserves credit: all 46 regulatory-date claims and 43 registry-status claims match live records, and its INTERPRETATION claims are PARTIALLY_SUPPORTED. No retag is proposed for A12 beyond the date-label cases in the re-inspection file.

## 8. Cross-shard tag inconsistency found while answering the golden questions

OTTAVA carries maturity OPERATIONAL in CLM-000283 and CLM-000284 (Director/A6 records) but PILOT in CLM-014022, CLM-014023, CLM-014024 (A14) and CLM-002048, CLM-002049 (A2). The evidence (De Novo authorised, one announced early-access installation, no unit or revenue data) fits PILOT. Propose retagging CLM-000283 and CLM-000284 to PILOT.
