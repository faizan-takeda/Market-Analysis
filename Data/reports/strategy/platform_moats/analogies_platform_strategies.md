# Platform-strategy analogies for pharma (A11b, wave 3)

Research cutoff 2026-11-21. **Every analogy here is a generator of hypotheses, not proof.** An analogy shows a mechanism worked once in another industry; it does not show the mechanism transfers. Each section gives mechanism, evidence (sources registered in shard `A11_strategy`, SRC-011000 to SRC-011016), what it predicts for pharma, where it breaks, and the hypothesis it generates for Takeda. Hypotheses are registered with kind HYPOTHESIS and tagged `for_bets_module`. Sources are T1 (SEC filings, NASA records, Nobel Committee) unless stated; claims marked "metadata only" were seen only as search snippets.

Takeda baseline classes referenced come from [capability_baseline.md](../../New_mediciine/companies/takeda_public_baseline/capability_baseline/capability_baseline.md). Moat taxonomy: [moat_mechanisms_taxonomy.md](moat_mechanisms_taxonomy.md).

## Summary table
| # | Analogy | Core mechanism | Strongest transferable element | Biggest break | Hypothesis ID |
|---|---|---|---|---|---|
| 1 | NVIDIA / CUDA | Loss-making developer software that locks demand to hardware | Federated shared layer rather than own platform | Small buyer set; each buyer owns data | [CLM-011027] |
| 2 | SpaceX reusable launch | Own the loop, iterate, buy outcomes fixed-price | Fixed-price outcome contracts; single-site pilots | Patient harm; GMP validation | [CLM-011031] |
| 3 | Google internal and external AI | Fund optionality from a profit pool | Capped exposure with stop rules | No patent cliff at Alphabet; scale | [CLM-011035] |
| 4 | Regeneron VelociSuite | In-house platform factory plus genetics engine | Run orexin science as a platform | Flagship product still eroded 42% | [CLM-011038] |
| 5 | TSMC / foundry | Neutral manufacturer plus partner ecosystem | Neutral capacity in plasma | Sponsors guard process and liability | [CLM-011041] |
| 6 | AWS | Internal capability productised externally | Productise only after measured advantage | Customers are rivals | [CLM-011045] |
| 7 | Intuitive Surgical | Installed base drives 84% recurring revenue | Device-drug pull-through (pens, HYHUB) | Ottava impairment; hospital capital cycle | [CLM-011048] |
| 8 | Roche-Flatiron | Pharma-owned data platform kept neutral | Neutral entity for a rare/plasma registry | No Takeda-area data network | [CLM-011051] |

---

## 1. NVIDIA / CUDA (developer tools to hardware moat)
**Mechanism.** NVIDIA announced CUDA in November 2006 [CLM-011000]. Its VP says CUDA succeeded because it changed C as little as possible, ran across GPU generations, "cost the company billions" and earned nothing for ten years [CLM-011003]. The 10-K says CUDA runs on all NVIDIA GPUs and over 7.5 million developers use it [CLM-011001]. Data Center revenue went from USD 47.5bn (FY2024) to USD 193.7bn (FY2026) [CLM-011002]. Mechanism summary [CLM-011024].
**Evidence strength.** T1 financials; the loss history is one interested executive's statement (T3 report of an interview) [CLM-011003]. Developer counts differ between the 10-K (7.5 million) and the company blog (11 million) [CLM-011000, CLM-011001].
**Prediction for pharma.** The durable asset is a data and model layer that others build on, since compute is purchasable; the closest pharma instance is Lilly TuneLab, operational with no outcome evidence [CLM-011025, CLM-000280, CLM-006007].
**Where it breaks.** Pharma has few buyers, each of which owns data; validation takes years through clinical trials; and NVIDIA's own 10-K lists customers' in-house capability and custom chips as a threat [CLM-011004, CLM-011026].
**Contrary evidence.** The risk factors above; also no pharma has reported developer adoption numbers for a model platform beyond Benchling's 1,300+ customer reach and a vendor blog's data-point counts [CLM-006008, CLM-009028].
**Hypothesis for Takeda (HYPOTHESIS).** Takeda gains more from joining a federated data layer than from building a proprietary platform [CLM-011027].

## 2. SpaceX reusable launch (iteration, vertical integration, infrastructure ownership)
**Mechanism.** NASA documents give the cost outcome: Falcon 9 development about USD 390m (Falcon 9 USD 300m plus Falcon 1 USD 90m, verified by NASA) against NASA model estimates of USD 1.7-4.0bn [CLM-011005, CLM-011006]; a Falcon 9 plus Dragon ISS mission at about USD 140m (USD 23,300/kg versus USD 93,400/kg for the Shuttle), cost to the ISS down by a factor of four [CLM-011007]. The acquisition model was firm fixed price with cost risk on the supplier [CLM-011008]. Summary [CLM-011028].
**Evidence strength.** T1 NASA documents. The cause of the gap (iteration, vertical integration, fewer processes, reuse) is not isolated; NASA states it is difficult to determine why actual cost was so far below the model [CLM-011006].
**Prediction for pharma.** Gains in manufacturing and automation come from owning a whole loop and iterating hardware fast, and from buying outcomes at fixed price [CLM-011029]. Testable at plant scale: Takeda's Los Angeles plasma expansion (USD 230m) and Lilly's Medicine Foundry (USD 4.5bn, concept) [CLM-005065, CLM-006000].
**Where it breaks.** NASA records that each commercial cargo partner suffered catastrophic failures that the contract absorbed [CLM-011008]; in pharma a failed batch or trial can harm patients and GMP validation slows iteration; Takeda's own Hikari warning letter caused a supply shortage [CLM-011030, CLM-005020].
**Hypothesis for Takeda (HYPOTHESIS).** Contract plasma automation and digital upgrades fixed-price, outcome-linked, in one site before network roll-out [CLM-011031].

## 3. Google internal and external AI investment (optionality, outcomes, capital exposure, failures)
**Mechanism.** Alphabet funds long-horizon research inside a profitable core (capex USD 91.4bn in 2025) and a separate Other Bets unit whose operating loss was USD 4.1bn (2023), USD 4.4bn (2024) and USD 7.5bn (2025, including a USD 2.1bn Waymo compensation charge) [CLM-011010, CLM-011009]. Documented outcome: AlphaFold2 predicted the structure of virtually all 200 million known proteins, used by over two million people in 190 countries, and shared the 2024 Nobel Prize in Chemistry [CLM-011012]. Externally, Isomorphic Labs (a DeepMind spin-out) reportedly raised USD 600m (snippet) and signed Lilly (USD 45m upfront, up to USD 1.7bn) with no disclosed candidate [CLM-011014, CLM-006012]. Summary [CLM-011032].
**Failures and capital exposure.** Alphabet dissolved Google Health in August 2021 after about three years and roughly 500 staff (two snippets, pages not opened) [CLM-011013]; its 10-K says the life-sciences bets may not be successful or profitable [CLM-011011]. The Other Bets loss rose USD 3.1bn from 2024 to 2025 [CLM-011009].
**Prediction for pharma.** AI-for-biology advances arrive first as scientific tools and partnered spin-outs, not as drugs [CLM-011033].
**Where it breaks.** Alphabet funds from an advertising profit pool with no patent cliff; pharma funds R&D from products that lose exclusivity; Alphabet's capex alone exceeds any pharma AI disclosure by orders of magnitude [CLM-011034, CLM-011010].
**Contrary evidence.** Isomorphic raised outside capital, which suggests optionality cost can be shared [CLM-011014].
**Hypothesis for Takeda (HYPOTHESIS).** Copy only the capped-exposure rule: a ring-fenced AI and automation option budget with explicit stop criteria, consistent with Takeda's record of stops (soticlestat, cell therapy exit with a JPY 58.2bn impairment) [CLM-011035, CLM-005024, CLM-009084].

## 4. Regeneron VelociSuite (biotech platform factory)
**Mechanism.** Regeneron replaced six megabases of mouse immunoglobulin loci with human loci (VelocImmune), and built VelociGene, VelociMouse, VelociMab, Veloci-Bi, VelociT and VelociHum for antibodies and bispecifics [CLM-011015]. The Regeneron Genetics Center has sequenced over 3 million samples with automation and cloud computing for target discovery [CLM-011016]. Summary [CLM-011036].
**Evidence strength.** T1 10-K; contribution to approved products is not quantified in the filing.
**Prediction for pharma.** A proprietary discovery factory supplies molecules and targets across many programmes at lower marginal cost than buying assets *(INTERPRETATION)*.
**Where it breaks.** EYLEA U.S. net sales fell 42% in 2025 and the company relies on Dupixent profit share from the Sanofi collaboration, so a platform does not protect individual product revenue [CLM-011017, CLM-011037].
**Hypothesis for Takeda (HYPOTHESIS).** Treat orexin science as a platform with a multi-asset plan, if a second differentiated asset is shown credible [CLM-011038, CLM-012149, CLM-005023].

## 5. TSMC and the foundry model (semiconductors)
**Mechanism.** TSMC states it is a dedicated foundry, unveiled its Open Innovation Platform in 2008 with partners building design infrastructure, earned 74% of 2025 wafer revenue from 7 nm and below, spent NT$1.27 trillion on capex in 2025 and guides to US$52-56bn in 2026 [CLM-011018, CLM-011019]. Summary [CLM-011039].
**Evidence strength.** T1 20-F; the neutrality-toward-customers claim is TSMC's known positioning but was not located verbatim in the passages read (flagged in the claim).
**Prediction for pharma.** A neutral capacity provider with a partner ecosystem wins when sponsors prefer not to build leading-edge capacity; pharma CDMOs are the nearest analogue *(INTERPRETATION)*.
**Where it breaks.** Sponsors hold patents and guard process know-how and safety liability, and plasma carries donor-supply and regulatory limits that wafers do not [CLM-011040].
**Hypothesis for Takeda (HYPOTHESIS, low confidence).** Test a neutral-capacity or shared-analytics role in plasma if utilisation shows spare capacity [CLM-011041, CLM-005065].

## 6. AWS (cloud: internal capability productised)
**Mechanism.** Amazon's 10-K describes AWS as a broad set of on-demand services to developers and enterprises [CLM-011020]. AWS had USD 128.7bn net sales and USD 45.6bn operating income in 2025, about 57% of Amazon's USD 80.0bn consolidated operating income (computed) [CLM-011020]. Summary [CLM-011042].
**Prediction for pharma.** The first pharma capability to be productised is one with standalone cost advantage and external demand; TuneLab is the nearest case [CLM-011043, CLM-009027].
**Where it breaks.** Pharma's would-be customers are competitors, and patient data is constrained by consent; consortia like AISB show rivals will cooperate only under federation [CLM-011044, CLM-006056].
**Hypothesis for Takeda (HYPOTHESIS).** Do not productise internal capabilities until a measured internal advantage exists; Takeda has none public [CLM-011045, CLM-006045].

## 7. Intuitive Surgical (industrial and medical robotics: installed base)
**Mechanism.** About 11,106 da Vinci systems installed, about 3.15 million procedures in 2025, and recurring revenue (instruments, service, leases) of USD 8.47bn, 84% of revenue [CLM-011021]. Summary [CLM-011046].
**Prediction for pharma.** Value accrues to the owner of the installed base and per-use consumables, as with pens and devices tied to a drug *(INTERPRETATION)*.
**Where it breaks.** J&J's robotics entry cost a USD 0.9bn Ottava impairment and OTTAVA has one announced installation; hospitals' capital cycles control adoption [CLM-011047, CLM-009047, CLM-006029].
**Hypothesis for Takeda (HYPOTHESIS).** Pull-through economics are cheaper to capture via drug-device combinations (Entyvio pen, HYHUB) than via robotics [CLM-011048, CLM-007041, CLM-007042].

## 8. Roche-Flatiron (healthcare technology: data platform ownership)
**Mechanism.** Roche paid USD 1.9bn (closed 6 April 2018) and kept Flatiron a separate legal entity with segregated data; Flatiron then partnered with 14 of the top 15 oncology companies (2018 figures) [CLM-011022]. Flatiron markets regulatory use of its real-world data, shown here only as a vendor snippet [CLM-011023]. Summary [CLM-011049].
**Prediction for pharma.** A neutral data asset can serve competitors; ownership by one pharma works only if neutrality is protected *(INTERPRETATION)*.
**Where it breaks.** Flatiron is oncology-specific and built in US community oncology; Takeda's core areas lack such a network, and Roche's realised value was not verified here [CLM-011050].
**Hypothesis for Takeda (HYPOTHESIS).** A neutral registry in a rare or plasma-treated disease could be a data moat, if built as a neutral entity [CLM-011051, CLM-005072].

---
## Cross-analogy reading *(INTERPRETATION)*
- Two analogies (NVIDIA, AWS) depend on an installed developer or customer base that pharma lacks; two (SpaceX, TSMC) depend on capital-intensive operations where Takeda has plasma manufacturing; two (Intuitive, Regeneron) are about owning a repeatable engine; Google and Flatiron concern optionality and neutrality.
- Takeda-specific hypotheses that survive the "where it breaks" test best are the ones tied to existing Takeda classes: PDT manufacturing (2), orexin (3) and drug-device combinations (1, 8). The rest are low-confidence.
- No analogy is evidence that any of these moves works in pharma; each needs an internal test listed in the internal validation backlog.

## Evidence gaps
Not researched: Moderna's platform (mRNA), Genentech/Roche research model, ASML, Epic. Developer counts and cost history for NVIDIA are company statements; SpaceX's cause-of-cost-gap is unresolved; Google Health and Isomorphic claims are snippet-level. See [evidence_gaps.md](../future_of_pharma/evidence_gaps.md).
