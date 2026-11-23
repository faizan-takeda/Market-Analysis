# Domain 3: Robotics and autonomous science (A11b, wave 3)

Research cutoff 2026-11-21. Options are labelled EVIDENCE_BACKED or HYPOTHESIS; none is an endorsement. Technical maturity is taken from A6's [autonomous_lab_reality_check.md](../../New_mediciine/industry_transformation/ai_data_robotics/autonomous_lab_reality_check.md) and [maturity_matrix.md](../../New_mediciine/industry_transformation/ai_data_robotics/maturity_matrix.md), with the A10 corrections applied: the claim that Lilly's lab was a "Strateos" venture launched about 2020 is unsupported (CLM-006017), the reason for the sale is undisclosed, and the Studio dates to 2017 in the sources that support it [CLM-006014].

Problem addressed: wet-lab throughput and reproducibility limit how many hypotheses can be tested; Lilly cites about 2,000 molecular ideas per target per year because each needs physical synthesis and testing [CLM-006005]. *(INTERPRETATION)*

## What the evidence shows
**Deployed**
- High-throughput scripted automation is operational and commodity: Arctoris runs the former Lilly platform as a CRO service, with five biochemistry modules, a screening module, a BSL2 cell-biology module and 4 million compound storage, and expanded biophysics capacity ten-fold [CLM-006013, CLM-006016].
- Plant automation that operates is conventional: Lilly Lebanon Advanced Therapies opened 2026-05-06 with robotic dosing and sealing seen on a tour, no performance data [CLM-006002].

**Announced or prototype**
- Lilly-NVIDIA co-innovation lab (up to USD 1bn over five years, jointly) targeting a continuous learning system linking agentic wet labs and dry labs: concept [CLM-000281]. LillyPod is operational compute with no reported result [CLM-006004, CLM-006007].
- Fast AI-to-wet-lab loops are vendor claims: Nabla three to four weeks design-to-test [CLM-006040]; BigHat pairs ML with a high-speed lab under an AbbVie deal [CLM-006035]. Robots and digital twins in Lilly plants are a vendor-blog capability claim, the audit calls the pilot tag generous [CLM-006006].
- Medicine Foundry (USD 4.5bn, opening late 2027) is concept [CLM-006000, CLM-006001].

**Failures and exits**
- Lilly's Life Sciences Studio went to the CRO Arctoris in 2024; a reported USD 90m build cost conflicts on dates [CLM-006013, CLM-006014]. Zymergen sold to Ginkgo for about USD 300m, one-tenth of its IPO valuation, after USD 1.2bn cumulative net losses [CLM-006051]. Pattern: owned and venture-funded cloud lab or biofoundry models ended in divestment or distressed sale; the service model continues [CLM-006052, CLM-011063].
- J&J's Ottava (Auris) took a USD 0.9bn partial impairment in fiscal 2021 [CLM-009047]. This is device robotics, not lab robotics, but shows robotics capital risk.

**Takeda baseline**
- No public evidence of lab automation, continuous manufacturing or manufacturing robotics [CLM-005067]. Plasma network grew from 233 to 275 centers (FY2022-FY2024) and a USD 230m Los Angeles fractionation expansion adds up to 2 million litres per year [CLM-005063, CLM-005065]. Hikari FDA warning letter (June 2020) caused a supply shortage [CLM-005020]. Synthesis: [CLM-011064].

## Staged automation ladder and technical maturity today
| Stage | Hardware | Data | Oversight | Validation | Regulatory | Investment evidence | Barriers | Metrics | Maturity today |
|---|---|---|---|---|---|---|---|---|---|
| 1 Assisted | Benchtop liquid handlers, instruments | LIMS, electronic notebooks | Scientist runs each step | Instrument qualification | GLP/GMP on existing rules | Not disclosed (gap) | Training, integration | Throughput, error rate | Operational, commodity [CLM-006013] |
| 2 Automated | Integrated HTS and dosing lines | Structured assay data | Protocol-driven, operator checks exceptions | Process validation per assay | As stage 1; GMP lines validated | Lilly Studio about USD 90m reported (conflicting dates) [CLM-006014] | Utilisation, maintenance | Cost per data point, uptime | Operational; Lilly plant robotics unquantified [CLM-006002] |
| 3 Integrated smart lab | Robotic labs tied to scheduling and ML planning | Closed data pipeline from instrument to model | Human approves designs and exceptions | Model credibility and data provenance | FDA draft AI credibility framework if used in submissions [CLM-006046] | Co-innovation lab up to USD 1bn over five years (joint) [CLM-000281] | Data quality, interfaces, vendor lock-in | Cycle time design-to-result, model hit rate | Prototype to pilot; vendor claims only [CLM-006040, CLM-006035] |
| 4 Bounded autonomous experimentation | Same plus closed-loop selection of next experiments within set limits | Active-learning loops with logged decisions | Humans set bounds, audit trails | Prospective validation against human-run controls | Unsettled for submission use | Zymergen: USD 1.2bn cumulative loss without a commercial product [CLM-006051] | Reproducibility, failure modes, evidence of benefit | Experiments per decision, success versus control | Not demonstrated by any source opened [CLM-011062] |
| 5 Scaled automation | Multi-site, GMP-integrated autonomous operation | Enterprise digital thread | Exception-based | Continuous verification | GMP expectations for automated release | Foundry USD 4.5bn at concept [CLM-006000] | Capital, workforce transition, validation burden | Cost per batch, deviation rate, speed to clinic | Concept; no operating example in the set [CLM-006001] |

Reading: stages 1-2 are mature enough to rent or buy; stage 3 can be piloted with strict gates; stage 4 and above have no independent demonstration, so any commitment is an option on technology not yet shown to work [CLM-011062].

## Where proprietary advantage exists
- Not in the robots: automation and CRO capacity are purchasable, and the one open-access owned lab was divested [CLM-006016, CLM-006052].
- In the data the automation generates and the process knowledge in manufacturing (for example plasma yield) [CLM-005064] *(INTERPRETATION)*.
- Open standards and partnering are better for stages 1-3 data generation; ownership is plausible only where a process is core and unique, such as plasma fractionation *(HYPOTHESIS)*.

## Takeda fit and baseline class
| Therapeutic area | Fit | Baseline class | Evidence |
|---|---|---|---|
| PDT | Fractionation and fill-finish automation have clearest unit economics; process and quality record includes one warning letter | 2 (EXISTING_STRENGTH), 12 Manufacturing quality (EXISTING_BUT_UNDERDEVELOPED) | [CLM-005065, CLM-005020] |
| Rare / neuroscience / GI discovery | Rent data generation (CRO) rather than own | 11 Lab automation and robotics (EVIDENCE_GAP) | [CLM-005067, CLM-006016] |
| Oncology, vaccines | No evidence of fit | 11 | none |

Economics: no Takeda automation spend is public (IVB-002, IVB-014) *(gap)*.

## Options (not endorsements)
| # | Option | Label | What must be true | Claim |
|---|---|---|---|---|
| 3.1 | Rent automated data generation from CROs and cloud labs; do not build an owned robotic lab | EVIDENCE_BACKED | CRO capacity and data quality meet Takeda needs | [CLM-011065] |
| 3.2 | Pilot fixed-price, outcome-linked automation upgrades at one plasma site before network roll-out | HYPOTHESIS | Yield and cost per litre show headroom (IVB-006) | [CLM-011031] |
| 3.3 | Set triggers for moving up the ladder (independent Lilly-lab result, Nabla first-in-human data, CRO cost benchmark) | HYPOTHESIS | Triggers are observable within 12-24 months | [CLM-011066] |
| 3.4 | Build an owned autonomous discovery lab (stage 4-5) | not supported by evidence | No independent demonstration; two owned models divested or sold distressed [CLM-006052] | none |

## Success criteria
- Cost per data point and turnaround from a CRO pilot versus internal baseline *(HYPOTHESIS)*.
- Plasma site: yield per litre of plasma, deviation rate and cost per litre before and after upgrade (company-defined, IVB-006) *(HYPOTHESIS)*.
- Evidence gate for stage 3+: prospective comparison of AI-planned versus human-planned experiments on the same target *(HYPOTHESIS)*.

## Risks
- Capital risk: documented distressed outcomes [CLM-006051, CLM-006052].
- Quality and compliance risk: Takeda has a documented warning letter and supply shortage, so automation in GMP settings needs validation before scale [CLM-005020].
- Workforce framing: automation changes tasks; do not describe it as replacing staff (see Domain 7).
- Safety: an autonomous system selecting experiments needs human-set bounds and audit trails *(INTERPRETATION)*.

## Evidence and gaps
Gaps: Takeda lab and plant automation footprint (IVB-002), cost per experiment for any pharma robotic lab, Emerald Cloud Lab and other cloud labs (not investigated by A6), reason for Lilly's sale [CLM-006017 unsupported detail], and whether the Lilly-NVIDIA lab has started. See [evidence_gaps.md](evidence_gaps.md).
