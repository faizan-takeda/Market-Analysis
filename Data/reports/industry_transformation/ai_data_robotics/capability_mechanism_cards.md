# Capability Mechanism Cards (A6, wave 1)

Scope: Lilly, J&J, AbbVie, Takeda (baseline), research cutoff 2026-11-21. Maturity scale: concept, prototype, pilot, operational, scaled, demonstrated_outcome. A press release proves an announcement, not an outcome. Claims in `[CLM-…]`; `CLM-000xxx` IDs are canonical registry claims. "Takeda relevance" uses build / buy / partner / watch / reject.

---

## Card 1. Lilly TuneLab (federated model-access platform) — Lilly

| Field | Content |
|---|---|
| Capability | Lilly-trained ADMET/safety/preclinical prediction models offered to outside biotechs; partners return data via federated learning. |
| Initial problem | Small biotechs lack consistent assay data; Lilly wants more training data and ecosystem pull (Catalyze360). |
| Starting investment | Lilly estimates the underlying data cost more than USD 1 billion to generate (company estimate, unaudited) [CLM-000280]. |
| Execution timeline | Launched 2025-09-09 [CLM-000280]; insitro ADMET models for it announced the same day [CLM-006009]; Benchling distribution announced 2026-01-08, opt-in "later this year" [CLM-006008]; Revvity Signals channel indicated mid-2026 (metadata only, SRC-006035). |
| Enabling assets | Decades of proprietary preclinical data; NVIDIA FLARE federated infrastructure; hosting by a third party [CLM-000280]; distribution through Benchling (1,300+ customers) [CLM-006008]; NVIDIA compute [CLM-006004]. |
| Evidence of value | None independent. No uptake, retraining count or scientific result disclosed [CLM-006008]. |
| Maturity | **operational** (platform live) with distribution at **pilot**. |
| Durability | Data moat is real if volume and consistency are as claimed; federated design means partner data improves Lilly-led models, strengthening lock-in (INTERPRETATION) [CLM-006055]. |
| Competitive response | Multi-pharma consortia (AISB) and open models (OpenFold3, Boltz, Chai) offer substitutes [CLM-006056, CLM-006042]. |
| Takeda relevance | **Watch / partner-as-user.** Takeda could be a TuneLab data-for-models participant; decide after independent results appear [CLM-006059]. |
| Evidence IDs | CLM-000280, CLM-006008, CLM-006009, CLM-006055, CLM-006056; SRC-006010, SRC-006008 |

---

## Card 2. LillyPod AI factory and NVIDIA co-innovation lab — Lilly

| Field | Content |
|---|---|
| Capability | Owned 1,016-GPU NVIDIA DGX SuperPOD (B300) to train biomedical foundation models; a planned USD 1 billion NVIDIA-Lilly co-innovation lab linking agentic wet labs and dry labs. |
| Initial problem | Wet-lab throughput limits (Lilly cites about 2,000 molecular ideas per target per year) [CLM-006005]. |
| Starting investment | Cluster cost not disclosed. Co-innovation lab: up to USD 1 billion over five years, jointly with NVIDIA [CLM-000281]. |
| Execution timeline | Announced October 2025 [CLM-006003]; inaugurated about February 2026, built in about four months [CLM-006004]; co-innovation lab announced 2026-01-12, work to begin early 2026 [CLM-000281]. |
| Enabling assets | NVIDIA hardware and BioNeMo/Omniverse/Isaac software; 700 TB genomics data [CLM-006004]; internal chief AI officer organisation. |
| Evidence of value | **None disclosed.** No model release, discovery result, cycle-time or cost number attributable to LillyPod [CLM-006007]. |
| Maturity | LillyPod: **operational** (infrastructure online). Co-innovation lab: **concept** [CLM-000281]. |
| Durability | Compute is purchasable; differentiation must come from data and models (INTERPRETATION) [CLM-006055]. Cluster is a capex bet with energy and obsolescence exposure. |
| Competitive response | BMS and Roche announced comparable pharma supercomputers (trade analysis only, not opened). |
| Takeda relevance | **Watch.** Do not match; buy cloud compute and partner [CLM-006058]. |
| Evidence IDs | CLM-000281, CLM-000282, CLM-006003–CLM-006007, CLM-006055; SRC-006001–006003 |

---

## Card 3. Lilly external AI-model partner portfolio (Isomorphic, insitro, Chai, OpenAI) — Lilly

| Field | Content |
|---|---|
| Capability | Parallel access to external model builders instead of a single in-house model. |
| Initial problem | Reach new small-molecule and antibody design capability faster than internal build. |
| Starting investment | Isomorphic: USD 45 million upfront, up to USD 1.7 billion milestones [CLM-006012]. insitro, Chai, OpenAI: no terms disclosed [CLM-006009, CLM-006010, CLM-006011]. |
| Execution timeline | Isomorphic 2024-01-07; OpenAI 2024-06-25 (brief's Sept 2025 date is wrong); insitro 2025-09-09; Chai early 2026 [CLM-006012, CLM-006011, CLM-006009, CLM-006010]. |
| Enabling assets | Lilly proprietary data (insitro, Chai models trained on it); partner models (AlphaFold lineage, generative antibody models). |
| Evidence of value | None disclosed; no candidate named in any opened source. Chai's double-digit hit rate is Chai's own claim [CLM-006010]. |
| Maturity | **concept** (Isomorphic, OpenAI), **prototype** (insitro, Chai). |
| Durability | Low individually; portfolio breadth hedges model-vendor risk (INTERPRETATION). |
| Competitive response | Every large pharma signs similar deals (Takeda–Nabla/Iambic; AbbVie–BigHat) [CLM-006039, CLM-006041, CLM-006035]. |
| Takeda relevance | **Partner** (already doing so); apply milestone-gated structures [CLM-006058]. |
| Evidence IDs | CLM-006009–CLM-006012; SRC-006004, 006008, 006009, 006011 |

---

## Card 4. Lilly Life Sciences Studio / Strateos remote robotic lab — Lilly (documented retreat)

| Field | Content |
|---|---|
| Capability | Remote-controlled, cloud-operated robotic lab (San Diego) integrating synthesis, purification, analysis and testing. |
| Initial problem | Faster, more reproducible discovery cycles and access for outside scientists. |
| Starting investment | Reported USD 90 million, established 2017 per one trade source; conflicts with a ~2020 public launch in a Fierce snippet [CLM-006014]. |
| Execution timeline | Public launch about 2020 (with Strateos); sold to CRO Arctoris and relocated to Oxford in 2024 [CLM-006013]. Strateos: one unopened aggregator snippet says acquired by Multiply Labs December 2023 [CLM-006015]; the brief's "closed 2023" is **not confirmed**. |
| Enabling assets | Strateos robotic cloud platform; Lilly demand. |
| Evidence of value | No disclosed discovery outcome from the lab in any source opened. |
| Maturity | Reached **operational**; ended as a divested asset [CLM-006017]. |
| Durability | Low as an owned open-access lab; the equipment survives in a CRO service model [CLM-006016]. |
| Competitive response | CROs (Arctoris) market automated data generation to AI-drug-discovery firms [CLM-006016]. |
| Takeda relevance | **Reject building** an owned cloud lab; **buy/partner** for automated data generation [CLM-006058]. |
| Contrary evidence | Reason for sale undisclosed; may be portfolio-driven. Lilly still plans "agentic wet labs" [CLM-000281]. |
| Evidence IDs | CLM-006013–CLM-006017, CLM-006052; SRC-006005, 006006, 006028 (metadata), 006029 (metadata) |

---

## Card 5. Lilly manufacturing automation: Lebanon Advanced Therapies and Medicine Foundry — Lilly

| Field | Content |
|---|---|
| Capability | New genetic-medicine plant with robotic dosing/sealing equipment; planned Foundry combining process R&D and clinical-supply manufacturing; robots/digital twins in plants per NVIDIA. |
| Initial problem | Capacity for obesity/diabetes and new modalities; speed from process development to clinic. |
| Starting investment | Foundry USD 4.5 billion (2024); further USD 4.5 billion on Lebanon (2026); Indiana commitments over USD 21 billion since 2020 [CLM-006000, CLM-006002]. Capex USD 7.8 billion in 2025 [CLM-000246]. |
| Execution timeline | Foundry announced 2024-10-02, opening late 2027, still planned in May 2026 [CLM-006000, CLM-006001]; Advanced Therapies opened 2026-05-06 [CLM-006002]. |
| Enabling assets | State of Indiana infrastructure support; NVIDIA digital-twin tooling (stated) [CLM-006006]. |
| Evidence of value | Opening observed by a reporter on a guided tour; no yield, cost or cycle-time data [CLM-006002]. |
| Maturity | Advanced Therapies **operational**; Foundry **concept**; digital twins **pilot** (stated, unevidenced). |
| Durability | Capital and permitting scale are a moat; automation content unquantified. |
| Takeda relevance | **Watch**; relevance for plasma and biologics fill-finish [CLM-000279]. |
| Evidence IDs | CLM-006000–CLM-006002, CLM-006006, CLM-000246; SRC-006000, 006012 |

---

## Card 6. J&J enterprise generative-AI portfolio — J&J

| Field | Content |
|---|---|
| Capability | Three layers: enterprise productivity, end-to-end process AI (trial-site selection, quality, sales copilots), AI embedded in products [CLM-006018, CLM-006023]. |
| Initial problem | Productivity and trial speed across 130,000+ employees. |
| Starting investment | Not disclosed. |
| Execution timeline | Experimentation from about 2022 (the interview refers to the past two years); centrally governed review of nearly 900 use cases; refocus in 2025 on high-value cases [CLM-006018, CLM-006019]. |
| Enabling assets | AI Council and Data Management Council; training of 47,000 employees in a generative-AI course [CLM-006022]; secure enclaves for models. |
| Evidence of value | Self-reported only: "up to 2.6x" enrolment at AI-recommended high-enrolling sites [CLM-006020]; weeks-to-minutes in a quality tool [CLM-006021]; 10–15% of use cases yield about 80% of value [CLM-006019]. No audited or independent result. |
| Maturity | **pilot** to **operational** (mixed); no demonstrated_outcome. |
| Durability | Low; productivity tools are commodity. Training and governance are slow to copy. |
| Takeda relevance | **Watch / adopt practice**: prune pilots early, measure per use case [CLM-006019]. |
| Evidence IDs | CLM-006018–CLM-006024; SRC-006013, 006014 |

---

## Card 7. J&J OTTAVA robotic surgical system — J&J

| Field | Content |
|---|---|
| Capability | Table-integrated four-arm soft-tissue robot connected to Polyphonic, with automated arm set-up. |
| Initial problem | Footprint, set-up complexity and data locked in existing robotic platforms. |
| Starting investment | Not disclosed. |
| Execution timeline | FDA De Novo 2026-07-22 [CLM-000283]; first commercial installation 2026-11-19 [CLM-000284]; IDE trial in six ORs, 243–694 sq ft [CLM-006028]. |
| Enabling assets | Ethicon instruments, robotics/AI hires (head of robotics R&D joined in 2024), Polyphonic data layer [CLM-006028]. |
| Evidence of value | Regulator authorisation is verified; efficiency claims rest on a survey of 12 surgeons and 8 staff [CLM-006028]. No revenue or procedure data; FY2025 10-K has no OTTAVA text [CLM-006025]. |
| Maturity | **pilot** (launch phase, one installation) [CLM-006029]. |
| Durability | Architecture and instrument breadth are differentiators; incumbents hold installed base (not studied here). |
| Takeda relevance | **Reject** (device); watch only as a read-across for data-linked robotics. |
| Evidence IDs | CLM-000283, CLM-000284, CLM-006025, CLM-006028, CLM-006029; SRC-006016 |

---

## Card 8. J&J MONARCH robotic bronchoscopy — J&J

| Field | Content |
|---|---|
| Capability | First flexible robotic bronchoscopy platform; AI nodule segmentation and CT-to-body-divergence handling in QUEST 3 software. |
| Initial problem | Reaching peripheral lung nodules for early lung-cancer diagnosis. |
| Starting investment | Not disclosed (Auris acquisition not reviewed here). |
| Execution timeline | Cleared 510(k) K152819 (referenced in release); QUEST 3 clearance announced 2026-08-17, third launch in 18 months [CLM-006027]. |
| Enabling assets | Installed base, software-updatable design, Polyphonic video library [CLM-006027]. |
| Evidence of value | Clearance (regulator action); support documents are internal technical reviews; installed base and procedure counts not disclosed; 10-K silent [CLM-006025]. |
| Maturity | **operational**. |
| Durability | Moderate; incremental AI inside cleared device, competitors (not studied) exist. |
| Takeda relevance | **Reject** (device). |
| Evidence IDs | CLM-006025, CLM-006027; SRC-006015 |

---

## Card 9. J&J VELYS robotic-assisted orthopaedics — J&J (thin evidence)

| Field | Content |
|---|---|
| Capability | CT-free robotic knee solution acting as pull-through for ATTUNE implants. |
| Initial problem | Robot-share race in knee arthroplasty. |
| Evidence of value | FY2025 10-K attributes Knees growth partly to VELYS pull-through but gives no unit or procedure counts [CLM-006026]. Adoption numbers were **not located** in a primary source. |
| Maturity | **scaled** at the level of commercial presence (INTERPRETATION); installed base unknown. |
| Takeda relevance | **Reject**; included for completeness. |
| Evidence IDs | CLM-006026; SRC-000010 |

---

## Card 10. J&J Polyphonic surgical data ecosystem — J&J

| Field | Content |
|---|---|
| Capability | Surgical video, device and AI-insight network; "AI Fund for Surgery"; Abu Dhabi node. |
| Initial problem | Surgical data is fragmented; AI needs governed multi-site datasets. |
| Execution timeline | Announced 2024-06-20 (page blocked; stated in search metadata only); AI Fund June 2025; first awardees 2025-10-27, "early access to select hospitals only" [CLM-006030]; Abu Dhabi programme 2026-05-21, deployment "expected" [CLM-006031]. |
| Enabling assets | Hospital partnerships, AWS and NVIDIA collaboration [CLM-006030]. |
| Evidence of value | None; the programme is data-gathering stage. |
| Maturity | Polyphonic early access: **pilot**; Abu Dhabi network: **concept**. |
| Durability | Potentially high if dataset ownership and hospital integration are exclusive (HYPOTHESIS). |
| Takeda relevance | **Watch** (data-network model). |
| Evidence IDs | CLM-006030, CLM-006031; SRC-006017, 006018 |

---

## Card 11. AbbVie R&D Convergence Hub (ARCH) — AbbVie

| Field | Content |
|---|---|
| Capability | Knowledge graph and data lake unifying 200+ sources; search and dossier applications; machine-learning workspaces. Not described as generative AI in the source opened. |
| Initial problem | Siloed R&D data; duplicate data acquisition. |
| Starting investment | "Significant investment", price undisclosed; fewer than ten FTE plus many contractors [CLM-006032, CLM-006033]. |
| Execution timeline | Conceived 2020; Bio-IT World award talk 2023-08-24 [CLM-006032]. |
| Enabling assets | Partners (Modak, SciBite, Tellic, TXI), Cloudera ML, governance decision to open de-identified trial data to all R&D [CLM-006032, CLM-006034]. |
| Evidence of value | A Dec 2022 preprint on repurposing flags (not opened); no clinical or financial outcome [CLM-006033]. |
| Maturity | **operational**. |
| Durability | Moderate: graph and governance are slow to replicate; vendors replicable. |
| Takeda relevance | **Build-lite / partner**: governance-first data integration is transferable; Takeda reports its own data modernization [CLM-000278]. |
| Evidence IDs | CLM-006032–CLM-006034, CLM-006038; SRC-006019, 006031 (metadata) |

---

## Card 12. AbbVie external AI: BigHat Biosciences and Valkai — AbbVie

| Field | Content |
|---|---|
| Capability | ML-guided antibody design with a wet lab (BigHat Milliner); clinical-development AI (Valkai). |
| Starting investment | BigHat: USD 30 million upfront, up to about USD 325 million milestones [CLM-006035]. Valkai: undisclosed [CLM-000285]. |
| Execution timeline | BigHat 2023-12-05; Valkai 2026-09-29. |
| Evidence of value | None disclosed for either [CLM-006037]. |
| Maturity | BigHat **prototype**; Valkai **concept**. |
| Takeda relevance | **Partner** analogues exist (Nabla). |
| Evidence IDs | CLM-006035, CLM-006037, CLM-000285, CLM-006036; SRC-006020 |

---

## Card 13. Takeda external AI deals: Nabla Bio and Iambic — Takeda

| Field | Content |
|---|---|
| Capability | Generative antibody design (Nabla JAM) and small-molecule AI incl. NeuralPLexer (Iambic). |
| Initial problem | Extend early pipeline after Takeda narrowed research focus (Reuters notes exit from cell-therapy research) [CLM-006039]. |
| Starting investment | Nabla: upfront and research payments in double-digit millions; Iambic: undisclosed upfront; success-based over USD 1 billion and over USD 1.7 billion respectively [CLM-006039, CLM-006041]. |
| Execution timeline | Nabla first collaboration 2022, second 2025-10-14; Iambic 2026-02-09. |
| Evidence of value | None; Nabla expects first-in-human data in one to two years [CLM-006039]. |
| Maturity | **prototype** (Nabla), **prototype/concept** (Iambic). |
| Takeda relevance | **Partner (in progress)**; set go/no-go gates [CLM-006058]. |
| Evidence IDs | CLM-006039–CLM-006041, CLM-006045; SRC-006021, 006022 |

---

## Card 14. Federated OpenFold3 / AI Structural Biology consortium — AbbVie, J&J, Takeda (plus BMS, Astex)

| Field | Content |
|---|---|
| Capability | Federated fine-tuning of OpenFold3 on proprietary protein-ligand structures; follow-on "AISB Bind". |
| Initial problem | Public structure data is too sparse for drug-like complexes. |
| Starting investment | Not disclosed. |
| Execution timeline | AbbVie and J&J first members (early 2025); BMS, Takeda, Astex joined 2025-10-01 [CLM-006042]. |
| Enabling assets | Apheris secure federated platform, Columbia AlQuraishi lab, 20,000+ private structures [CLM-006043]. |
| Evidence of value | Organiser reports +10 points pose accuracy and +11 points interface quality vs the strongest public model on 1,056 held-out structures; not peer-reviewed [CLM-006043]. |
| Maturity | **pilot** (first initiative complete); AISB Bind **concept** [CLM-006044]. |
| Durability | Network effects among members; open model weights limit exclusivity. |
| Takeda relevance | **Partner (in progress)**; note absence from AISB Bind founding list [CLM-006044]. |
| Evidence IDs | CLM-006042–CLM-006044, CLM-006056; SRC-006023, 006024 |
