# Domain 1: Data advantage (A11b, wave 3)

Research cutoff 2026-11-21. Takeda fiscal years run April-March (FY2025 = April 2025 to March 2026). Options are labelled EVIDENCE_BACKED (follows from cited evidence) or HYPOTHESIS (reasoned, needs non-public data). Nothing here is an endorsement. Baseline class numbers refer to [capability_baseline.md](../../New_mediciine/companies/takeda_public_baseline/capability_baseline/capability_baseline.md).

Problem addressed: drug discovery and development decisions depend on proprietary experimental, clinical and real-world data that is fragmented inside each company and too sparse in public sources for drug-like targets. *(INTERPRETATION)*

## What the evidence shows
**Deployed versus announced (competitors)**
- Lilly TuneLab is live: launched 2025-09-09, Lilly-trained models offered to biotechs with federated learning, underlying data cost estimated by Lilly at over USD 1 billion [CLM-000280]. Distribution through Benchling (1,300+ customers) is opt-in "later this year", with no uptake figure [CLM-006008]. A vendor blog reports over 2 million Lilly and 675,000 partner data points as of October 2026 (single vendor source) [CLM-009028]. Maturity: operational platform, pilot distribution, no independent outcome [CLM-006007].
- AbbVie ARCH is operational: conceived 2020, built by fewer than ten full-time staff plus contractors over a 124 TB corpus, and governance opened de-identified data from 2,000+ clinical trials to all R&D [CLM-006032, CLM-006034]. Outcome evidence is a preprint not opened by A6.
- J&J Polyphonic is early access to select hospitals; the Abu Dhabi network is "expected" [CLM-006030, CLM-006031]. Maturity: pilot and concept.
- Five companies (AbbVie, Astex, BMS, J&J, Takeda) fine-tuned OpenFold3 on over 20,000 private structures; the organiser reports about 10 points better pose accuracy than the best public model on 1,056 held-out structures, not peer reviewed [CLM-006043]. Takeda is not on the AISB Bind founding list [CLM-006044].
- Across these four assets, none has independent outcome evidence [CLM-011052].

**Takeda baseline**
- Public evidence is a platform and an aspiration: a Databricks-hosted agent platform for 10,000+ employees (vendor-hosted, partly supported) [CLM-005058], 80% external digital workforce when the transformation was designed [CLM-005057], a stated aim to embed AI in every stage of discovery [CLM-005053], and no quantified outcome [CLM-006045, CLM-011053].

**Contrary evidence**
- NVIDIA states that customers with in-house capability can replace platform layers [CLM-011004], which applies to data platforms too *(INTERPRETATION)*. The A10 audit also marks the AISB result as vendor-organised and the CIO-reported J&J metrics as self-reported [CLM-006020].

## Where proprietary advantage exists
- Proprietary experimental data generated over decades is the one defensible asset; compute and third-party models are purchasable by rivals [CLM-006055].
- Advantage is strongest where data is expensive to regenerate (company-estimated over USD 1 billion for TuneLab) and where partners add data back, strengthening the model *(INTERPRETATION)* [CLM-011082, CLM-011087].
- Open standards or partnering fit better for public-like tasks (structure prediction, ADMET baselines) where no single company has enough data; federated consortia are the common mechanism [CLM-006056].

## Takeda fit and baseline class
| Therapeutic area | Data position | Baseline class | Evidence |
|---|---|---|---|
| Plasma-derived therapies | 270+ collection centers with adaptive donor nomograms; immunoglobulins 18% of FY2025 revenue | 2 Plasma network and PDT manufacturing (EXISTING_STRENGTH) | [CLM-005060, CLM-005063, CLM-005064] |
| GI / immunology | Entyvio is 21% of revenue; trial and real-world data scale unknown | 1 GI / immunology (EXISTING_STRENGTH) | [CLM-005009] |
| Rare disease, neuroscience (orexin) | Discovery in Shonan; patient numbers small | 3 Rare / orexin (EXISTING_STRENGTH) | [CLM-005048] |
| Enterprise data and AI platform | Platform exists; production use and outcomes unproven | 9 (EXISTING_BUT_UNDERDEVELOPED) | [CLM-005058, CLM-005080] |
| AI-enabled discovery | No outcome evidence | 10 (EVIDENCE_GAP) | [CLM-005049] |

Economics: Takeda R&D expense was JPY 675.9bn in FY2025 [CLM-005004]; the public record gives no technology capital envelope (IVB-014), so any build-size claim is an assumption *(gap)*. Evidence requirements: a data investment is justified only by a measured change in cycle time, hit rate or cost per decision, none of which Takeda or any competitor has published.

## Options (not endorsements)
| # | Option | Label | What must be true | Claim |
|---|---|---|---|---|
| 1.1 | Keep participating in federated consortia (AISB) and evaluate follow-on tasks from measured value | EVIDENCE_BACKED | Pooled models beat Takeda-only models on Takeda targets; governance protects raw data | [CLM-011054] |
| 1.2 | One governed cross-franchise R&D data layer (ARCH-type) | HYPOTHESIS | Takeda data is fragmented as AbbVie's was; reuse of trial data is permitted | [CLM-011055] |
| 1.3 | Treat plasma donor, yield and process data as the proprietary data class | HYPOTHESIS | Data is captured consistently across centers and predicts yield or cost | [CLM-011056] |
| 1.4 | Build a TuneLab-style external model platform | HYPOTHESIS (low confidence) | Data volume and external demand comparable to Lilly; see analogy NVIDIA [CLM-011027] | [CLM-011027] |

## Success criteria
- Production inventory of data and AI products with users and outcomes (closes IVB-001).
- A named decision (target selection, trial design, supply planning) where a model changed the outcome, with a pre-agreed baseline *(HYPOTHESIS)*.
- Federated model gains on Takeda held-out data versus public models, reported with the organiser's method disclosed *(HYPOTHESIS)*.

## Risks
- Regulatory: FDA's January 2025 draft guidance proposes a risk-based credibility framework for AI used in regulatory decisions, so model evidence must be documented [CLM-006046].
- Data and liability: Takeda's 20-F warns AI models may be flawed or trained on inadequate data [CLM-005054].
- Privacy and consent limit pooling; federation reduces but does not remove this *(INTERPRETATION)*.
- Platform lock-in: a competitor-led federated platform strengthens that competitor's models as partners contribute [CLM-006055].

## Evidence and gaps
Gaps: internal AI inventory (IVB-001), TuneLab uptake, ARCH outcomes, Takeda data estate, plasma yield data (IVB-006). Details in [evidence_gaps.md](evidence_gaps.md).
