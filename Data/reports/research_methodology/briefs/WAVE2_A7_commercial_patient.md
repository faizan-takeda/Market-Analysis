# A7 — Commercial, Market-Access & Patient-Experience Intelligence (horizontal, wave 2)

Shard: `A7_commercial` (SRC/CLM-007000..007999). Output dir: `/Users/palrahma/Desktop/MEDICINE/New_mediciine/industry_transformation/commercial_patient/`. Companies: Lilly, J&J, AbbVie, Takeda (baseline depth).

## Research question
How does each company actually win and defend market share — launch execution, payer/PBM contracting, patient support and access programs, direct-to-patient channels, pricing posture, distribution, real-world evidence, HCP engagement — and which new care-delivery models (home administration, connected devices, remote monitoring, decentralized trials, digital therapeutics) have they deployed with evidence of adoption? Which of these transfer to Takeda's therapeutic mix (GI, rare, PDT, neuroscience, oncology, vaccines)?

Already in registry (cite, do not redo): grep `claims_registry.jsonl` for `LillyDirect`, `Cordavis`, `CVS`, `withMe`, `gross-to-net`, `Allē`, `patient support`, `Entyvio SC`, `Medicare` — company agents captured some (e.g., CLM-001042 LillyDirect launch; CLM-003007/8/10 Humira/CVS/Cordavis; CLM-001036/37 Nov-2025 pricing agreement).

## Mandatory sub-questions
1. **Direct-to-patient and cash channels**: LillyDirect (launch, cash-pay Zepbound vial prices and their cuts 2024-08, 2025-02, 2025-11; TrumpRx), Novo comparison only as context; J&J and AbbVie DTC/cash programs if any; Takeda none? Evidence of volume (any disclosed share of self-pay).
2. **Payer/PBM dynamics and gross-to-net**: disclosed gross-to-net pressure (10-K language), rebate levels where disclosed, formulary events (CVS Caremark Humira removal 2024-04; Stelara biosimilar formulary moves 2025; Zepbound/Wegovy exclusive formulary deals 2025 e.g., CVS Caremark choosing Wegovy 2025-07; employer coverage trends), Medicare Part D redesign impact statements, 340B.
3. **Launch execution**: launch curves disclosed (Mounjaro/Zepbound quarterly, Skyrizi/Rinvoq, Tremfya, Carvykti capacity-constrained launch, Spravato REMS centres, Vyalev, Kisunla slow uptake and reasons, Qdenga), launch-readiness mechanisms (field force size, omnichannel statements, specialty pharmacy, hub services).
4. **Patient support and adherence**: Lilly (Lilly Cares, savings cards, insulin USD 35 cap), J&J (withMe, Janssen CarePath), AbbVie (myAbbVie Assist, Complete programs, Allē loyalty with member counts), Takeda (Help at Hand, Takeda Patient Support); evidence of outcomes (adherence, time-to-therapy) if any — mostly company-reported; flag.
5. **Care-delivery innovation**: home/self-administration shifts (Entyvio SC pen, Tremfya SC, Darzalex Faspro, Vyalev pump, Zepbound vials), connected devices/digital (J&J Impella Connect?, Abiomed; Lilly connected pens Tempo; AbbVie Vraylar? no), remote monitoring in trials, decentralized/hybrid trials statements (Lilly, J&J), digital therapeutics (any evidence; most pharma retreated — e.g., Pear bankruptcy 2023 as industry calibration), site-of-care economics (infusion vs SC).
6. **Real-world evidence & HCP engagement**: RWE programs with published outputs (e.g., tirzepatide RWE, Entyvio RWE), omnichannel/HCP engagement statements with any metrics, medical affairs digital.
7. **Pricing posture & access controversies**: list prices vs net, price cuts (insulin), international reference pricing/MFN exposure, access litigation (compounding), reputation events.
8. **Transfer to Takeda** (INTERPRETATION, labelled): which mechanisms fit Takeda's portfolio and which do not (e.g., cash-pay DTC fits obesity, not rare disease), with the evidence IDs behind the judgment.

## Web targets
10-K/20-F text on disk (grep `gross-to-net|rebates|formulary|patient support|direct-to-consumer|LillyDirect|specialty pharmacy|hub`), company newsrooms, earnings-release 8-K exhibits (EDGAR), FDA label/REMS pages, KFF/Health Affairs/STAT/Reuters/Endpoints/Fierce (web_fetch) for formulary events and uptake, PubMed for RWE publications. Respect blocked hosts (2 tries → record and move on).

## Deliverables
`commercial_models_comparison.md` (table per mechanism × company with evidence IDs), `patient_programs_and_care_delivery.md`, `launch_execution_evidence.md`, `pricing_access_and_payer_dynamics.md`, `transfer_to_takeda.md` (INTERPRETATION, each item tied to a Takeda baseline class from `New_mediciine/companies/takeda_public_baseline/capability_baseline/capability_baseline.md`), `map.md`, `evidence_gaps.md`. Shard target ≥25 sources (≥15 retrieved), ≥50 claims. HARD CAP: 100 tool calls — batch fetches; write shard + reports by call ~85.
