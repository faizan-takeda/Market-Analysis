# Data and AI maturity matrix (levels only, no scores)

Cutoff 2026-11-21. Scale: concept < prototype < pilot < operational < scaled < demonstrated_outcome. A press release proves an announcement, not an outcome. "Outcome evidence" means an independently verifiable result (regulator record, peer-reviewed paper, audited number); company-stated results count as no [CLM-006054]. Sources are the A6 matrix and mechanism cards plus A14 gap-fill claims; no initiative was re-researched.

**Audit retags applied (A10, status-discipline audit).** CLM-006020 (J&J trial-site recommendation, "up to 2.6x" enrolment) is read as self-reported pilot-level evidence, not operational. CLM-006022 (30,000 course completions, 47,000 gen-AI course completions of 130,000+ employees) is a training metric, not a deployment, and is excluded from the maturity cells. CLM-006026 (VELYS "pull through") is read as operational, not scaled. CLM-006047, CLM-006049 and CLM-006051 describe Recursion, Exscientia/BenevolentAI and Zymergen, not the four companies, and are used only as industry calibration. CLM-000284 is read as an announced first installation site, not a completed installation [CLM-000284] [CLM-006020] [CLM-006022] [CLM-006026].

## 1. Matrix

Each cell gives the maturity level, the evidence, and whether independent outcome evidence exists (Y/N). "No evidence found" means no source opened for this project shows it; it is not a finding that the capability is absent.

| Layer | Lilly | J&J | AbbVie | Takeda |
|---|---|---|---|---|
| Owned compute | LillyPod, 1,016 Blackwell Ultra GPUs, over 9,000 petaflops: **operational**, outcome N [CLM-006003] [CLM-006004] [CLM-014054] [CLM-006007]. NVIDIA co-innovation lab, up to USD 1bn over five years: **concept**, N [CLM-000281] [CLM-014053] | No evidence found | No evidence found | No evidence found |
| Proprietary data platform | TuneLab (launched 2025-09-09): **operational**, outcome N; third-party distribution via Benchling: **pilot**; at least four partner organisations announced, no participant count or retraining result [CLM-000280] [CLM-006008] [CLM-014056]. | Polyphonic digital ecosystem: **pilot** ("early access to select hospitals only"); Abu Dhabi network: **concept**, N [CLM-006030] [CLM-006031] | ARCH knowledge graph: **operational** (124 TB harmonised data, over 30 million nodes, built by fewer than ten staff plus contractors); no outcome beyond an unopened preprint, N [CLM-006032] [CLM-006033] [CLM-006034] | Unified AI foundation on Databricks, agent platform for 10,000+ employees: **operational**, but the source is a vendor-hosted session summary, N [CLM-005058] |
| External AI-model partnerships (discovery) | Isomorphic and OpenAI: **concept**; insitro and Chai: **prototype**; no candidate named, N [CLM-006012] [CLM-006011] [CLM-006009] [CLM-006010] | AI in molecule design stated by the CEO without named programmes or metrics: **pilot**, N [CLM-014071] | BigHat antibody collaboration (USD 30m upfront): **prototype**, N [CLM-006035] | Nabla Bio (second collaboration, first-in-human data expected in one to two years per company) and Iambic: **prototype**, N [CLM-006039] [CLM-006040] [CLM-006041] |
| Consortium and federated learning | TuneLab federated learning on NVIDIA FLARE: **pilot**, N [CLM-006056] [CLM-014055] | AI Structural Biology (AISB) OpenFold3 fine-tuning: **pilot**; AISB Bind: **concept** [CLM-006042] [CLM-006044] | AISB OpenFold3: **pilot**; AISB Bind: **concept** [CLM-006042] [CLM-006044] | AISB OpenFold3 member since October 2025: **pilot**; not listed in AISB Bind [CLM-006042] [CLM-006044]. The only quantified cross-company result is a vendor benchmark (five firms, under ten weeks, over 20,000 private structures), not peer reviewed, N [CLM-006043] |
| Enterprise gen-AI and productivity | Only a 10-K statement of use and a risk factor; no deployment metric [CLM-000252] | About 900 use cases reviewed; moved from proofs of concept to deployment; named tools (sales assistant, engagement tool, supply-risk sensing): **pilot to operational**, self-reported, N [CLM-006018] [CLM-006019] [CLM-006023] | 10-K reports AI-skills investment and an adoption-failure risk; no outcome [CLM-006036] | 63.4% of the workforce actively used gen-AI tools at 31 March 2026 (46.6% a year earlier); the claim tag is SCALED but the measure is tool usage, not a business outcome, so read as **operational (usage)**, N [CLM-014043] *(INTERPRETATION)* |
| AI in clinical development | No evidence found | Trial-site recommendation, "up to 2.6x" enrolment at recommended sites, no baseline: **pilot** (self-reported), N [CLM-006020] | Valkai partnership announced 2026-09-29: **concept**, no deployment metric, N [CLM-000285] [CLM-006037] | Regulatory-submission agent listed as a production use case on a vendor page: **operational** (self-reported), N [CLM-005058]. AI in clinical development named in the 2026 integrated report with no metric [CLM-014045] |
| Manufacturing and supply-chain AI or digital twins | NVIDIA states plant robots and planned digital twins: **pilot**, vendor statement only, N [CLM-006006] | Gen-AI quality-control tool answering SKU and regulatory questions in minutes: **operational**, self-reported, N [CLM-006021] | Not searched in depth *(gap)* | More than 170 AI predictive-maintenance agents at Lessines: **operational**, company report, N [CLM-014041]. One Day Batch Release pilots at six sites, target 60% shorter release lead time by 2028: **pilot** [CLM-014042]. Plasma nomograms across 270+ centres: **operational**, benefit unquantified [CLM-005060] |
| Robotic or automated lab | Studio / Strateos remote lab built, then divested to Arctoris in 2024: **operational then divested**, reason undisclosed, N [CLM-006013] [CLM-006017] | No evidence found | BigHat's wet-lab loop sits with the partner [CLM-006035] | No public evidence found of lab automation [CLM-005067] [CLM-006045] |
| Independent outcome evidence | None found [CLM-006007] | Regulatory records exist for devices (OTTAVA De Novo, MONARCH 510(k), VELYS 510(k)s); none for AI-originated drug outcomes [CLM-014022] [CLM-014025] [CLM-014026] | None found [CLM-006054] | None found [CLM-006054] |

## 2. What is established

- Across the 29 company-level A6 entries, 18 sit at concept, prototype or pilot, and none reaches demonstrated outcome [CLM-006054].
- Lilly has the largest evidenced infrastructure build and the only owned-compute and data-as-product pair; the registry shows no scientific, cycle-time or financial result from either [CLM-006053] [CLM-006007].
- J&J's devices carry the only regulator records among the four companies' AI-adjacent products, and those records concern devices, not discovery [CLM-006054] [CLM-014022] [CLM-014025].
- AbbVie internalises data (ARCH, a knowledge graph, not generative AI) and buys models (BigHat, Valkai) [CLM-006032] [CLM-006035] [CLM-000285].
- Takeda's disclosed strategy is partnership-led, and its 2026 integrated report adds company-reported operating items in manufacturing AI and workforce adoption that the earlier baseline did not have [CLM-006053] [CLM-014041] [CLM-014043].

## 3. Answers to the two comparison questions

**Which technology ecosystem is most defensible?** The registry cannot support a ranking. The candidate moat the A6 analysis identifies is Lilly's proprietary experimental data (company-estimated to cost over USD 1bn to generate) paired with a federated platform, but the same analysis rates the moat claim only partially supported and finds no outcome [CLM-006055] [CLM-000280]. Federated consortia and open models are available substitutes [CLM-006056]. The statement "Lilly has the most defensible ecosystem" is therefore a *(HYPOTHESIS)*, not a finding.

**Which AI investments are operationally meaningful?** Operationally meaningful here means operational or higher status plus a disclosed operating scale. On that test the items are LillyPod (compute online) [CLM-006004], ARCH (internal graph with disclosed size) [CLM-006032], Takeda's Lessines predictive maintenance and plasma nomograms (company-reported scale, benefit unquantified) [CLM-014041] [CLM-005060], and J&J's gen-AI quality-control tool (qualitative) [CLM-006021]. No item has an independently verified effect on cost, cycle time or revenue. Announcement-stage items (NVIDIA lab, Valkai, Isomorphic, OpenAI) are not operationally meaningful on this evidence [CLM-000281] [CLM-000285] [CLM-006012] [CLM-006011].

## 4. Industry calibration

AI-platform pipelines still show ordinary attrition (Recursion ended four of 11 programmes in 2025), the best public AI-origin clinical data are a small Phase IIa (rentosertib, 71 patients, 12 weeks, with liver-related discontinuations), and owned automation ventures ended in divestment or distressed sale (Lilly's studio, Zymergen sold at about one-tenth of its IPO valuation) [CLM-006047] [CLM-006048] [CLM-006052] [CLM-006051]. FDA's January 2025 draft AI guidance is non-binding [CLM-006046].

## 5. What is contested

- Why Lilly divested the Studio (model failed, low utilisation or portfolio reasons) and whether Strateos closed or was acquired (an unverified aggregator snippet says Multiply Labs acquired it in December 2023); the two cited pages date the Studio to 2017 and mention no Strateos or 2020 launch [CLM-006017] [CLM-006015] [CLM-014057].
- Whether Takeda's executive and vendor accounts of its AI use reflect production scale; both are interested sources [CLM-005057] [CLM-005058].

## 6. What is unknown

- Any peer-reviewed or audited result from an autonomous closed-loop lab at the four companies [CLM-006052].
- TuneLab uptake and retraining counts; NVIDIA lab operating status; ARCH outcomes [CLM-014056] [CLM-014053] [CLM-006032].
- J&J and AbbVie compute capacity; AbbVie manufacturing digitalisation *(gap)*.
