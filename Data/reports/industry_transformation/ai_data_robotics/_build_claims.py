#!/usr/bin/env python3
"""A6 shard claim builder (rewrites shards/A6_ai_robotics/claims.jsonl) and writes claim_keys.json."""
import json
from pathlib import Path

OUT = Path("/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/shards/A6_ai_robotics/claims.jsonl")
KEYS = Path("/Users/palrahma/Desktop/MEDICINE/New_mediciine/industry_transformation/ai_data_robotics/claim_keys.json")
LV = "2026-11-21"
C = []
K = {}
LL, JJ, AV, TK, IN = "eli_lilly", "johnson_johnson", "abbvie", "takeda", "industry"


def S(n):
    return f"SRC-{n:06d}"


def c(key, statement, kind, status, cos, srcs, why, mat, domain="data_ai", loc=None, dates=None,
      contrary=None, single=True, impl=None, ents=None, rel=None, tags=None, csrc=None):
    cid = f"CLM-{6000 + len(C):06d}"
    r = {"claim_id": cid, "statement": statement, "kind": kind, "status": status, "companies": cos,
         "domain": domain, "supporting_source_ids": srcs, "confidence_rationale": why,
         "single_interested_source": single, "last_verified": LV, "maturity": mat}
    if loc:
        r["locator"] = loc
    if dates:
        r["dates"] = dates
    if contrary:
        r["contrary_evidence"] = contrary
    if csrc:
        r["contrary_source_ids"] = csrc
    if impl:
        r["implication"] = impl
    if ents:
        r["entities"] = ents
    if rel:
        r["related_reports"] = rel
    if tags:
        r["tags"] = tags
    C.append(r)
    K[key] = cid


R_LAND = ["New_mediciine/industry_transformation/ai_data_robotics/ai_data_robotics_landscape.md"]
R_CARD = ["New_mediciine/industry_transformation/ai_data_robotics/capability_mechanism_cards.md"]
R_LAB = ["New_mediciine/industry_transformation/ai_data_robotics/autonomous_lab_reality_check.md"]

# ---------------------------------------------------------------- LILLY
c("ll_foundry", "On 2024-10-02 Lilly announced a USD 4.5 billion Lilly Medicine Foundry in Lebanon, Indiana, a facility combining process research and clinical-supply manufacturing, with opening stated as late 2027, about 400 planned jobs, and technologies developed there to be transferred to Lilly's other sites.",
  "FACT", "SUPPORTED", [LL], [S(6000)], "Company release with forward-looking statement; no independent confirmation of design or automation content. Brief's 'automation claims' are not made in this release.", "concept",
  "robotics_automation", "paragraphs 1-3; sub-headline", {"event": "2024-10-02"}, impl="Capital commitment, not an operating capability; automation scope of the Foundry is not described in the release.", ents={"products": [], "partners": ["State of Indiana"], "technologies": ["advanced manufacturing", "process development"]}, rel=R_LAND)
c("ll_foundry_status", "As of the 6 May 2026 opening of Lilly Lebanon Advanced Therapies, local press reported the Lilly Medicine Foundry and the Lilly Lebanon API site were still planned, with the API site due to open in 2027.",
  "FACT", "SUPPORTED", [LL], [S(6012)], "Independent local public-media report of a ribbon-cutting; consistent with the 2024 release's late-2027 Foundry opening.", "concept",
  "robotics_automation", "paragraph 'Lilly will soon celebrate its 150th anniversary'", {"event": "2026-05-06"}, single=False, rel=R_LAND)
c("ll_adv_ther", "On 2026-05-06 Lilly opened its Lilly Lebanon Advanced Therapies genetic-medicine plant and announced a further USD 4.5 billion for the Lebanon campus (more than USD 21 billion of Indiana commitments since 2020); a reporter on the guided tour saw staff monitoring robotic machines that dose, measure and seal medicines.",
  "FACT", "SUPPORTED", [LL], [S(6012)], "Single local-news report of a company-guided tour; no throughput, yield, headcount or automation-rate data.", "operational",
  "robotics_automation", "paragraphs 1 and 'During a tour'", {"event": "2026-05-06"}, impl="Evidence that robotic fill-finish-type equipment is installed at a newly opened Lilly site; effect on cost or cycle time is not measured.", rel=R_LAND)
c("ll_aifactory_ann", "At NVIDIA GTC Washington, D.C. in October 2025, NVIDIA and Lilly announced a Lilly 'AI factory' built as an NVIDIA DGX SuperPOD with DGX B300 systems and 1,016 Blackwell Ultra GPUs, rated at over 9,000 petaflops of AI performance, to train biomedical foundation models.",
  "FACT", "SUPPORTED", [LL], [S(6001)], "Vendor blog co-promoting a customer; specifications are NVIDIA/Lilly statements. Adds detail to registry claims CLM-000282.", "prototype",
  "data_ai", "opening paragraphs", {"event": "2025-10"}, contrary="Brief expected 'more than 1,000 GPUs'; 1,016 confirmed by the vendor blog.", impl="Compute is purchased, replicable by competitors with capital; differentiation depends on data and models, not the cluster.", ents={"partners": ["NVIDIA"], "technologies": ["DGX SuperPOD B300", "BioNeMo", "Omniverse", "Isaac"]}, rel=R_LAND)
c("ll_lillypod_live", "Lilly's AI supercomputer, branded LillyPod, was inaugurated at a ribbon-cutting in Indianapolis (reported late February 2026), assembled in about four months, with over 9,000 petaflops, 700 TB of genomics data and over 290 TB of GPU memory, and a stated target of 100% renewable electricity by 2030.",
  "FACT", "SUPPORTED", [LL], [S(6002), S(6003)], "Two sources, but the trade piece restates the NVIDIA/Lilly material, so corroboration is not independent. No independent benchmark or utilisation figure.", "operational",
  "data_ai", "NVIDIA blog paras 1-3; BiopharmaTrend 'Inside the Pod'", {"event": "2026-02"}, impl="Infrastructure is online; no disclosed model released from it or scientific result attributable to it.", ents={"partners": ["NVIDIA"], "technologies": ["DGX SuperPOD", "Spectrum-X"]}, rel=R_LAND + R_CARD)
c("ll_dry_lab", "Lilly's VP of R&D informatics said that productive teams typically analyse roughly 2,000 molecular ideas per target per year because each needs physical synthesis and testing, and that the supercomputer lets scientists evaluate billions of molecular hypotheses computationally before wet-lab work.",
  "FACT", "SUPPORTED", [LL], [S(6002)], "Executive statement published on a vendor blog: a FACT that the claim was made, not evidence that billions of hypotheses were tested or that hit quality improved.", "operational",
  "data_ai", "section 'Step Behind the Scenes of the LillyPod'", {"event": "2026-02"}, impl="The throughput claim is about candidate generation; the binding constraint (experimental validation) is unchanged until the wet-lab loop is automated.", rel=R_LAB)
c("ll_physical_ai", "NVIDIA's October 2025 blog states Lilly uses robots in its factories for quality inspection and transport of goods and plans digital twins of manufacturing lines on NVIDIA Omniverse; it gives no deployment counts, sites or results.",
  "FACT", "SUPPORTED", [LL], [S(6001)], "Vendor description; mixes present-tense use ('uses robots') with capability statements ('can create digital twins'). No quantified outcome.", "pilot",
  "robotics_automation", "section 'Research and Biomanufacturing With Physical and Agentic AI'", {"event": "2025-10"}, impl="Manufacturing digital twins and robots are asserted but unevidenced beyond one vendor article; 10-K (CLM-000252) quantifies none.", ents={"technologies": ["digital twin", "NVIDIA Isaac", "Omniverse"]}, rel=R_LAND)
c("ll_aifactory_outcome", "No source opened for this review reports a scientific, cycle-time or financial outcome attributable to the Lilly AI factory or the planned NVIDIA co-innovation lab as of 2026-11-21.",
  "INTERPRETATION", "INCONCLUSIVE", [LL], [S(6001), S(6002), S(6003)], "Absence of disclosure in the sources reviewed; not proof that no outcome exists. Lilly 10-K (CLM-000252) also quantifies no AI outcome.", "operational",
  "data_ai", None, None, impl="Treat Lilly's AI infrastructure as a capability bet whose value is unproven; revisit after Lilly's next R&D day or model releases via TuneLab.", rel=R_LAND)
c("ll_tunelab_benchling", "On 2026-01-08 Benchling announced it would distribute Lilly TuneLab antibody and small-molecule prediction models to its more than 1,300 biotech customers, with customers able to opt in 'later this year'; no uptake figures were given.",
  "FACT", "SUPPORTED", [LL], [S(6010)], "Distribution partner's own release (interested party). Platform launch itself is CLM-000280. A July 2026 Revvity Signals information sheet (metadata only, SRC-006035) indicates a second distribution channel.", "pilot",
  "data_ai", "paragraphs 1 and final", {"event": "2026-01-08"}, impl="Reach is being built through third-party platforms where biotech scientists already work; participation numbers remain undisclosed.", ents={"partners": ["Benchling", "NVIDIA FLARE"], "technologies": ["federated learning"]}, rel=R_LAND + R_CARD)
c("ll_insitro", "On 2025-09-09 insitro announced a collaboration to build machine-learning models predicting small-molecule ADMET and in vivo behaviour from Lilly's proprietary preclinical data, with the models to be available through Lilly TuneLab; it expands a 2024 insitro-Lilly relationship on siRNA delivery and antibody discovery.",
  "FACT", "SUPPORTED", [LL], [S(6008)], "Counterparty press release; no financial terms or model performance metrics disclosed.", "prototype",
  "data_ai", "paragraphs 1, 4 and 6", {"event": "2025-09-09"}, ents={"partners": ["insitro"], "technologies": ["ADMET prediction", "federated learning"]}, rel=R_LAND + R_CARD)
c("ll_chai", "BiopharmaTrend reported in early 2026 that Chai Discovery and Lilly agreed to build a custom antibody-design model on Lilly's proprietary data, with no financial terms disclosed; the reported double-digit zero-shot hit rate for Chai-2 is Chai's own claim.",
  "FACT", "PARTIALLY_SUPPORTED", [LL], [S(6011)], "Single trade article without a primary release opened; date approximated.", "prototype",
  "data_ai", "paragraphs 1 and 3", {"event": "2026-01"}, contrary="Primary Chai or Lilly announcement not opened.", impl="Lilly is buying access to several external model builders in parallel (insitro, Chai, Isomorphic, OpenAI).", ents={"partners": ["Chai Discovery"]}, rel=R_LAND)
c("ll_openai", "On 2024-06-25 Lilly announced a collaboration with OpenAI to use generative AI to invent novel antimicrobials against drug-resistant pathogens; the release states no financial terms, targets, timelines or results.",
  "FACT", "SUPPORTED", [LL], [S(6009)], "Company release. The research brief dated this collaboration to September 2025; the release is June 2024.", "concept",
  "data_ai", "paragraph 1", {"event": "2024-06-25"}, contrary="Brief's 'Sept 2025' date is not supported.", ents={"partners": ["OpenAI"]}, rel=R_LAND)
c("ll_isomorphic", "On 2024-01-07 Isomorphic Labs announced a multi-target small-molecule collaboration with Lilly: USD 45 million upfront, up to USD 1.7 billion in performance-based milestones, and tiered royalties up to low double digits.",
  "FACT", "SUPPORTED", [LL], [S(6004)], "Isomorphic's own release (Lilly terms as stated by counterparty); reproduced by trade press (SRC-006033 snippet) which is not independent.", "concept",
  "partnerships_ma", "paragraph 2", {"event": "2024-01-07"}, impl="Option-style economics: cash at risk is the USD 45 million upfront; no candidate has been disclosed in the sources reviewed.", ents={"partners": ["Isomorphic Labs"], "technologies": ["AlphaFold"]}, rel=R_LAND + R_CARD)
c("ll_strateos_lab_sale", "In 2024 (reported September) Arctoris acquired Lilly's Life Sciences Studio automated laboratory, relocating the platform from San Diego to Oxford and adding five automated biochemistry modules, a high-throughput screening module, a BSL2 cell-biology module and storage for 4 million compounds.",
  "FACT", "SUPPORTED", [LL], [S(6005)], "Trade report; the Fierce Biotech version (blocked, SRC-006028 snippet) says Lilly sold a majority of the lab. Sale price and reason not disclosed in any source opened.", "operational",
  "robotics_automation", "paragraphs 1-3", {"event": "2024-09"}, contrary="Fierce snippet says Lilly sold 'a majority', not all, of the lab; unresolved.", single=False, impl="A pharma-built open robotic lab was handed to an external CRO four years after launch.", ents={"partners": ["Arctoris", "Strateos"], "technologies": ["cloud lab", "robotic automation"]}, rel=R_LAB + R_CARD)
c("ll_lab_cost", "BiopharmaTrend states the Life Sciences Studio was established by Lilly in 2017 as part of a USD 90 million investment; a Fierce Biotech snippet describes the lab as launched four years before the 2024 sale, which conflicts with a 2017 start.",
  "FACT", "PARTIALLY_SUPPORTED", [LL], [S(6005), S(6028)], "One trade source for the USD 90 million and 2017 dates; the second source is a search snippet only. Dates conflict (2017 build vs ~2020 public launch).", "operational",
  "robotics_automation", "paragraph 'Originally established'", None, contrary="Fierce snippet: 'Four years after launching' (i.e., about 2020).", impl="Cost figure is unverified; treat as an order of magnitude.", rel=R_LAB)
c("ll_strateos_acq", "An aggregator profile (not opened; search snippet only) reports that Strateos, Lilly's robotic cloud-lab partner, was acquired by Multiply Labs in December 2023; no primary announcement was found and the research brief's 'Strateos closed 2023' framing is not confirmed as a closure.",
  "HYPOTHESIS", "NEEDS_MORE_RESEARCH", [LL], [S(6029)], "Metadata-only aggregator snippet (T5); requires a Strateos or Multiply Labs primary announcement or independent news report.", "unknown",
  "robotics_automation", None, {"event": "2023-12"}, impl="If confirmed, Strateos ended as an independent company via acquisition by a robotic-manufacturing firm, not an outright shutdown.", rel=R_LAB)
c("ll_arctoris_since", "By March 2026 Arctoris described the ex-Lilly platform as part of a cloud-controlled robotic system running biochemistry, biophysics, cell-biology and structural-biology workflows, announced a ten-fold biophysics instrumentation expansion, and said it was selected for the UK ARIA AI Scientist programme targeting endometriosis.",
  "FACT", "SUPPORTED", [IN], [S(6006)], "Trade report restating Arctoris announcements; interested-party source chain, no independent audit of utilisation.", "operational",
  "robotics_automation", "'Context' and opening paragraphs", {"event": "2026-03"}, impl="The asset survives in a service (CRO) model that sells experimental data to many AI-drug-discovery customers rather than serving one pharma.", ents={"partners": ["Arctoris", "ARIA"]}, rel=R_LAB)
c("ll_lab_retreat", "The Lilly-Strateos remote robotic laboratory (public launch about 2020) no longer operates under Lilly: its hardware was divested to a CRO in 2024. The reason is undisclosed, so the sources support a retreat from an owned open cloud lab but not a cause.",
  "INTERPRETATION", "PARTIALLY_SUPPORTED", [LL], [S(6005), S(6006), S(6028)], "Inference from sale of the asset; Lilly has given no rationale in sources opened. Lilly's January 2026 plan for 'agentic wet labs' (CLM-000281) shows it still invests in lab automation, but inside its own AI-centred programme.", "operational",
  "robotics_automation", None, None, contrary="Lilly may have divested for portfolio or utilisation reasons unrelated to technical failure.", impl="Calibration for Takeda: owning an open-access robotic lab did not keep it inside Lilly; renting from a CRO preserves optionality.", rel=R_LAB + R_CARD)
c("ll_gateway", "Lilly's use of a San Diego Gateway Labs site (announced with Alexandria Real Estate Equities) is listed in search results only; no Gateway Labs outcome data was opened in this review.",
  "FACT", "NEEDS_MORE_RESEARCH", [LL], [S(6005)], "Placeholder recording a gap; not substantively supported by an opened source.", "unknown",
  "partnerships_ma", None, None, impl="Gateway Labs/Catalyze360 not assessed.", rel=R_LAND) if False else None

# ---------------------------------------------------------------- J&J
c("jj_900", "In a March 2025 interview J&J's CIO said J&J had reviewed nearly 900 generative-AI use cases for ethical, regulatory and compliance risk, that much of the prior two years' gen-AI work had been proofs of concept and pilots, and that the company was now deploying gen AI.",
  "FACT", "SUPPORTED", [JJ], [S(6014)], "Executive statement in an interview by an investor; no independent verification.", "pilot",
  "data_ai", "answers on 'To what extent are Gen AI tools cascaded'", {"event": "2025-03-13"}, impl="J&J describes a funnel from hundreds of pilots to a focused set of deployments; the number deployed is not given.", rel=R_LAND)
c("jj_80_20", "J&J's CIO said (as relayed by The Batch, citing Greylock and The Wall Street Journal) that 10-15% of use cases drove about 80% of the value, after which J&J moved responsibility for AI projects to departments to focus on high-value applications.",
  "FACT", "SUPPORTED", [JJ], [S(6013)], "Secondary summary; WSJ original is paywalled (SRC-006032 metadata only). Source chain traces to a single J&J executive.", "operational",
  "data_ai", "'How it works' paragraph", {"event": "2025-04"}, contrary="WSJ snippet adds that redundant or non-working projects are cut.", csrc=[S(6032)], impl="Evidence of portfolio pruning discipline rather than an outcome.", rel=R_LAND)
c("jj_enroll", "J&J's CIO said AI models recommending clinical-trial sites produced 'up to a 2.6x increase in enrollment' at better-performing, higher-enrolling recommended sites; the baseline, method and trials are not disclosed.",
  "FACT", "SUPPORTED", [JJ], [S(6014)], "Self-reported by the company executive; 'up to' metric without denominator.", "operational",
  "data_ai", "answer on 'end-to-end capabilities'", {"event": "2025-03-13"}, impl="Plausible mechanism (site selection) but unverified magnitude; do not treat as a demonstrated outcome.", rel=R_LAND + R_CARD)
c("jj_qc", "J&J's CIO said a gen-AI tool launched in quality control lets service representatives answer product-identification and regulatory questions across hundreds of thousands of SKUs in minutes instead of weeks.",
  "FACT", "SUPPORTED", [JJ], [S(6014)], "Executive claim without measurement method.", "operational",
  "data_ai", "answer on 'To what extent are Gen AI tools cascaded'", {"event": "2025-03-13"}, rel=R_LAND)
c("jj_training", "J&J's CIO reported more than 30,000 completions of its 'digital boot camp' courses and 47,000 employees completing a required generative-AI course, from a workforce of more than 130,000.",
  "FACT", "SUPPORTED", [JJ], [S(6014)], "Executive statement; training completion is an activity metric, not a value metric.", "scaled",
  "data_ai", "answer on 'how are you making sure AI tools are adopted'", {"event": "2025-03-13"}, rel=R_LAND)
c("jj_tools", "J&J's CIO named AI tools in use or deployed: a sales-rep assistant (AskJIA), an engagement tool (Engagement.AI) used for provider insights in over 14 countries, a supply-risk sensing platform, and an HR service agent; no usage or outcome data accompany them.",
  "FACT", "SUPPORTED", [JJ], [S(6014)], "Executive interview; names tools but quantifies none.", "operational",
  "data_ai", "answers on productivity and end-to-end capabilities", {"event": "2025-03-13"}, rel=R_LAND)
c("jj_biosignature", "J&J's CIO said AI-powered image analytics on its biosignature platform helped J&J deliver novel molecular entities 'faster than we would have been able to before'; no counts, timelines or comparison are given.",
  "FACT", "SUPPORTED", [JJ], [S(6014)], "Qualitative executive claim, no numbers.", "operational",
  "scientific_rd", "answer on 'end-to-end capabilities'", {"event": "2025-03-13"}, impl="Cannot be tested from public data; ask J&J for candidate counts and cycle times.", rel=R_LAND)
c("jj_10k", "J&J's FY2025 10-K says J&J uses data science, machine learning and other AI across parts of its business and warns that its AI investments may not deliver a competitive advantage or may become obsolete (line 428); it quantifies no AI outcome, and its text contains no references to OTTAVA or MONARCH.",
  "FACT", "SUPPORTED", ["johnson_johnson"], ["SRC-000010"], "Text search of the on-disk FY2025 10-K: AI risk-factor language at line 428 and regulatory discussion at line 313; OTTAVA and MONARCH zero hits. Canonical source SRC-000010.", "not_applicable",
  "data_ai", "lines 313, 428 of extracted_text/sec/JNJ_10-K_2025-12-28_0000200406-26-000016.txt", {"period": "FY2025"}, single=False, impl="Investors receive no robotics installed-base or AI value disclosure in the 10-K.", rel=R_LAND)
c("jj_velys", "J&J's FY2025 10-K attributes growth in Knees to the ATTUNE portfolio and 'pull through related to the VELYS Robotic assisted solution' but reports no VELYS system or procedure counts.",
  "FACT", "SUPPORTED", [JJ], ["SRC-000010"], "Direct 10-K text (line 821); canonical source. Quantified VELYS adoption numbers were not found in a primary source in this review.", "scaled",
  "robotics_automation", "line 821", {"period": "FY2025"}, contrary="No VELYS unit or procedure count located; VELYS Community snippet (25,000+ ATTUNE knees in 2024) not opened.", single=False, impl="Robotics matters commercially as a pull-through for implants; ask for installed base.", rel=R_LAND + R_CARD)
c("jj_monarch", "On 2026-08-17 J&J announced 510(k) clearance for MONARCH QUEST 3 software adding AI-powered nodule segmentation, registration and navigation improvements, a 3D Compass overlay and broader CBCT compatibility, and said it followed three launches in 18 months; supporting design evidence cited is internal technical reviews.",
  "FACT", "SUPPORTED", [JJ], [S(6015)], "Company release; clearance itself is a regulator action but the 510(k) record was not opened. No installed-base or procedure counts given.", "operational",
  "robotics_automation", "paragraphs 1-3 and references", {"event": "2026-08-17"}, impl="MONARCH is a mature, iterating software-defined platform (first flexible robotic bronchoscopy system per the release); AI is incremental inside a cleared device.", ents={"products": ["MONARCH QUEST 3"], "technologies": ["nodule segmentation", "CBCT"]}, rel=R_LAND + R_CARD)
c("jj_ottava", "J&J says OTTAVA has four arms integrated into the operating table and, in its IDE trial, fitted operating rooms as small as 243 sq ft (five of six trial ORs previously non-robotic); a user-experience survey behind its efficiency claims covered 12 surgeons and 8 staff after 1-5 gastric bypass cases each.",
  "FACT", "SUPPORTED", [JJ], [S(6016)], "Company-authored feature; footnotes show the survey is small (n=20) and Likert-based. Regulatory milestone is in CLM-000283.", "pilot",
  "robotics_automation", "Q&A on OR architecture; reference footnotes", {"event": "2026-10-08"}, impl="Differentiation is a footprint and table-integrated architecture; efficiency benefit unproven at scale.", ents={"products": ["OTTAVA"]}, rel=R_LAND + R_CARD)
c("jj_ottava_status", "As of 2026-11-19 OTTAVA has FDA De Novo authorization (2026-07-22, CLM-000283) and one announced commercial installation (CLM-000284), with J&J giving no revenue, unit-sale, order-book or procedure data.",
  "INTERPRETATION", "SUPPORTED", [JJ], ["SRC-000032", "SRC-000034", S(6016)], "Combines regulator-verified authorization with a single installation announced by the company; the J&J 10-K (FY2025) contains no OTTAVA text.", "pilot",
  "robotics_automation", None, {"event": "2026-11-19"}, single=False, impl="Commercial maturity is at launch; compare with Intuitive and Medtronic before assuming competitiveness.", rel=R_LAND + R_CARD)
c("jj_polyphonic", "J&J said on 2025-10-27 that its Polyphonic digital ecosystem 'is available in early access to select hospitals only', and that the first Polyphonic AI Fund QuickFire Challenge drew entries from 29 countries and awarded Mayo Clinic and QAS.AI.",
  "FACT", "SUPPORTED", [JJ], [S(6017)], "Company release; early-access wording is itself an admission of limited rollout.", "pilot",
  "data_ai", "final paragraphs", {"event": "2025-10-27"}, impl="Surgical-data network is pre-scale; value depends on hospitals contributing video data.", ents={"products": ["Polyphonic"], "partners": ["NVIDIA", "AWS", "Mayo Clinic"]}, rel=R_LAND + R_CARD)
c("jj_abudhabi", "On 2026-05-21 J&J announced a programme with the Abu Dhabi Department of Health under which Cleveland Clinic Abu Dhabi, PureHealth, Mediclinic and NMC Healthcare are to deploy Polyphonic across operating rooms, creating a governed anonymised surgical-data source for AI development; the release says deployment is 'expected'.",
  "FACT", "SUPPORTED", [JJ], [S(6018)], "Company release with forward-looking language; no OR counts or timeline.", "concept",
  "data_ai", "paragraphs 1-4", {"event": "2026-05-21"}, impl="A government-sponsored data node could give J&J a durable surgical-video dataset; not yet realised.", ents={"partners": ["Abu Dhabi DOH", "AWS", "NVIDIA"]}, rel=R_LAND + R_CARD)

# ---------------------------------------------------------------- ABBVIE
c("av_arch", "At Bio-IT World in 2023 AbbVie's head of AI said the AbbVie R&D Convergence Hub (ARCH), conceived in 2020, was built by fewer than ten full-time AbbVie staff plus many contractors (Modak, SciBite, Tellic, TXI), harmonised a corpus over 124 TB, and exposes a graph of over 30 million nodes and nearly 2 billion relationships to all R&D employees.",
  "FACT", "SUPPORTED", [AV], [S(6019)], "Trade write-up of AbbVie's own presentation (Bio-IT World Innovative Practices winner); figures are AbbVie-stated.", "operational",
  "data_ai", "sections 'Effort of Partners', 'Mining the Graph'", {"event": "2023-08-24"}, impl="ARCH is a knowledge-graph and data-governance asset; the source does not describe it as a generative-AI platform, contrary to the research brief.", ents={"partners": ["Modak", "SciBite", "Tellic", "TXI Digital", "Cloudera"], "technologies": ["knowledge graph", "NLP"]}, rel=R_LAND + R_CARD)
c("av_arch_cost", "AbbVie's head of AI said ARCH's first version was done 'quick' but 'not cheap' and 'not right [or final]', declined to give a price but called it a 'significant investment' requiring sacrifices elsewhere, and cited a December 2022 bioRxiv preprint on drug-repurposing flags as evidence of patient impact.",
  "FACT", "SUPPORTED", [AV], [S(6019)], "Candid speaker statement reported by a trade outlet; the preprint itself was not opened and no clinical outcome is cited.", "operational",
  "data_ai", "final paragraphs", {"event": "2023-08-24"}, contrary=None, impl="No outcome beyond a preprint; cost undisclosed. Value case rests on productivity and data reuse.", rel=R_LAND + R_CARD)
c("av_arch_governance", "AbbVie's ARCH governance gave all R&D employees access to data from medical affairs, discovery, clinical and real-world sources; per its head of AI, risk-based analysis allowed all 2,000+ clinical trials' de-identified data to be reused internally, with prison and pediatric populations excepted.",
  "FACT", "SUPPORTED", [AV], [S(6019)], "AbbVie-stated, via trade report.", "operational",
  "data_ai", "section 'Effort of Partners'", {"event": "2023-08-24"}, impl="The enabling asset is the governance decision to open trial data internally, which is replicable but organisationally hard.", rel=R_CARD)
c("av_bighat", "On 2023-12-05 AbbVie and BigHat Biosciences announced an AI/ML antibody collaboration in oncology and neuroscience using BigHat's Milliner platform, with USD 30 million upfront and up to about USD 325 million in R&D milestones plus royalties.",
  "FACT", "SUPPORTED", [AV], [S(6020)], "Company release; no candidate or result reported in sources opened. Total potential ~USD 355 million.", "prototype",
  "partnerships_ma", "paragraph 4", {"event": "2023-12-05"}, ents={"partners": ["BigHat Biosciences"], "technologies": ["machine learning antibody design"]}, rel=R_LAND + R_CARD)
c("av_10k", "AbbVie's FY2025 10-K says AbbVie has 'invested significantly in equipping employees with foundational artificial intelligence (AI) skills' and lists failure 'to adequately adopt emerging technologies such as artificial intelligence' among IT risk factors; it quantifies no AI outcome.",
  "FACT", "SUPPORTED", [AV], ["SRC-000003"], "Direct 10-K text (lines 397 and 540); canonical source SRC-000003.", "not_applicable",
  "data_ai", "lines 397, 540 of ABBV_10-K_2025-12-31_0001551152-26-000008.txt", {"period": "FY2025"}, single=False, rel=R_LAND)
c("av_valkai_context", "AbbVie's September 2026 Valkai partnership (CLM-000285) is described as framed under 'AI@AbbVie'; neither that release nor any other source opened gives deployment metrics, so it is an announcement at concept maturity.",
  "INTERPRETATION", "SUPPORTED", [AV], ["SRC-000035"], "Relies on registry claim CLM-000285 (canonical source SRC-000035).", "concept",
  "data_ai", None, {"event": "2026-09-29"}, single=False, rel=R_LAND)
c("av_arch_page", "AbbVie's own ARCH web page (not opened; HTTP 403) is indexed as describing ARCH connecting more than 200 internal and external sources and over 2 billion points of knowledge, consistent with the 2023 conference figures.",
  "FACT", "NEEDS_MORE_RESEARCH", [AV], [S(6031)], "Metadata-only snippet; consistency with Bio-IT World figures noted but page not read.", "operational",
  "data_ai", None, None, rel=R_LAND)

# ---------------------------------------------------------------- TAKEDA
c("tk_nabla", "On 2025-10-14 Reuters reported that Nabla Bio and Takeda signed a second multi-year AI protein-design collaboration (first launched 2022) with upfront and research payments in double-digit millions of dollars and over USD 1 billion in success-based payments; Nabla expected first-in-human data within one to two years.",
  "FACT", "SUPPORTED", [TK], [S(6022)], "Reuters wire reporting Nabla's disclosure; Takeda terms not independently stated.", "prototype",
  "partnerships_ma", "paragraphs 1-3, 8", {"event": "2025-10-14"}, impl="Takeda is buying access to a generative antibody-design engine; the value test is first-in-human data.", ents={"partners": ["Nabla Bio"], "technologies": ["JAM generative antibody design"]}, rel=R_LAND + R_CARD)
c("tk_nabla_speed", "Nabla's CEO told Reuters that Nabla's design-to-lab-test turnaround is three to four weeks, described as 'probably the fastest feedback loop in the industry'.",
  "FACT", "SUPPORTED", [TK], [S(6022)], "Counterparty CEO claim; no benchmark or data.", "prototype",
  "data_ai", "paragraph 6", {"event": "2025-10-14"}, rel=R_LAND)
c("tk_iambic", "On 2026-02-09 Iambic announced a multi-year collaboration with Takeda on small-molecule programs in oncology and gastroenterology/inflammation, with Takeda gaining access to Iambic's NeuralPLexer model and Iambic eligible for success-based payments that could exceed USD 1.7 billion plus royalties.",
  "FACT", "SUPPORTED", [TK], [S(6021)], "Counterparty paid press release; upfront amount not stated in the text opened.", "prototype",
  "partnerships_ma", "opening and final paragraphs", {"event": "2026-02-09"}, contrary="A secondary analysis (not opened) cites USD 27 million upfront; unverified.", impl="Takeda's CSO frames the aim as de-risking candidate selection and reaching IND faster; no results yet.", ents={"partners": ["Iambic Therapeutics"], "technologies": ["NeuralPLexer"]}, rel=R_LAND + R_CARD)
c("tk_aisb", "Takeda joined the AI Structural Biology consortium (with Bristol Myers Squibb and Astex, 1 Oct 2025) that already included AbbVie and J&J, to fine-tune OpenFold3 with proprietary protein-ligand structures using a federated approach.",
  "FACT", "SUPPORTED", [TK, AV, JJ], [S(6024)], "Trade report derived from the Apheris announcement; join date from search-result snippets of Reuters coverage.", "pilot",
  "data_ai", "paragraphs 1-3", {"event": "2025-10-01"}, single=False, impl="Federated pre-competitive modelling lets Takeda access better structure prediction without pooling data.", ents={"partners": ["Apheris", "Columbia AlQuraishi Lab"], "technologies": ["OpenFold3", "federated learning"]}, rel=R_LAND + R_CARD)
c("tk_aisb_results", "Apheris states that five companies (AbbVie, Astex, BMS, J&J, Takeda) jointly fine-tuned OpenFold3 in under ten weeks on over 20,000 private structures, outperforming every public model tested by about 10 points on pose accuracy and 11 points on interface quality on 1,056 held-out private structures; results are not peer-reviewed.",
  "FACT", "PARTIALLY_SUPPORTED", [TK, AV, JJ], [S(6023)], "Organiser/vendor self-report on its own benchmark; no external replication.", "pilot",
  "data_ai", "metrics panel", None, contrary=None, impl="Concrete evidence that a multi-pharma federated model can beat public models on drug-like complexes, subject to independent confirmation.", ents={"partners": ["Apheris"], "technologies": ["OpenFold3", "AISB-1-Fed"]}, rel=R_LAND + R_CARD)
c("tk_aisb_bind", "Apheris lists a follow-on 'AISB Bind' effort in which AbbVie, AstraZeneca, Bristol Myers Squibb and Johnson & Johnson will federate-train a small-molecule binding-prediction model, marked 'in progress'; Takeda is not listed among its founding partners.",
  "FACT", "SUPPORTED", [AV, JJ, TK], [S(6023)], "Organiser page text; status 'in progress'.", "concept",
  "data_ai", "section 'AISB BIND'", None, impl="Takeda is absent from the next-stage binding consortium as listed; a watch item.", rel=R_LAND)
c("tk_baseline", "Takeda's 20-F lists digital transformation and AI integration as initiatives and risk factors with no quantified AI outcome (CLM-000278), and none of the Takeda sources opened in this review reports a named, internally deployed AI system with metrics.",
  "INTERPRETATION", "SUPPORTED", [TK], ["SRC-000024", S(6022), S(6021)], "Based on registry claim CLM-000278 plus absence of first-party deployment evidence in sources opened; Takeda newsroom and DD&T materials not searched exhaustively.", "unknown",
  "data_ai", None, None, single=False, impl="Takeda's disclosed AI posture is external partnering; baseline depth only.", rel=R_LAND)

# ---------------------------------------------------------------- INDUSTRY CALIBRATION
c("in_fda", "In January 2025 FDA issued draft, non-binding guidance (docket FDA-2024-D-4689) proposing a risk-based credibility-assessment framework for AI models used to support regulatory decision-making on drug safety, effectiveness or quality for a defined context of use.",
  "FACT", "SUPPORTED", [IN], [S(6025)], "FDA primary record. Finalisation after January 2025 not checked; a Federal Register notice (2025-01-07) exists (SRC-006034, metadata only).", "not_applicable",
  "policy_regulation", "guidance summary paragraph", {"event": "2025-01"}, single=False, impl="Regulatory expectations apply to AI that supports submissions, not to internal discovery AI.", rel=R_LAND)
c("in_recursion", "In May 2025 Recursion ended development of four of its 11 programmes (REC-994, REC-2282, REC-3964, REC-4209) and paused a fifth; its CEO said REC-994's long-term extension did not sustain early signals, REC-3964's halt was strategic, and cash fell to USD 509 million at 31 March 2025 from USD 603 million.",
  "FACT", "SUPPORTED", [IN], [S(6026)], "Independent trade report quoting the company and an analyst; platform-derived molecules failing mid-stage is a calibration data point.", "demonstrated_outcome",
  "successes_failures", "opening and 'Limited tumor shrinkage' sections", {"event": "2025-05"}, single=False, impl="AI-platform origin did not protect clinical programmes from ordinary attrition.", rel=R_LAND)
c("in_insilico", "A June 2025 Nature Medicine Phase IIa study (71 IPF patients, 12 weeks) of AI-discovered rentosertib showed +98.4 mL mean FVC at 60 mg versus -20.3 mL on placebo, with seven discontinuations for liver injury or dysfunction and 67% completion of the high-dose arm versus 88% on placebo, as reported by Drug Discovery Trends.",
  "FACT", "SUPPORTED", [IN], [S(6027)], "Trade report of a peer-reviewed paper (paper not opened here); authors cite small, homogeneous cohort and short follow-up as limits.", "demonstrated_outcome",
  "successes_failures", "paragraphs 1-3", {"event": "2025-06-03"}, contrary="Safety signals (liver injury) and small n.", impl="Best public yardstick that a fully AI-originated target and molecule can show Phase IIa signal; far from approval.", rel=R_LAND)
c("in_ai_pos", "Drug Discovery Trends cites prior analyses that AI-originated compounds clear Phase 2 at about the same 40% rate as conventional drugs and lists discontinued Exscientia (EXS-21546) and BenevolentAI (BEN-2293) programmes.",
  "FACT", "PARTIALLY_SUPPORTED", [IN], [S(6027)], "Secondary citation of unspecified analyses; underlying studies not opened.", "demonstrated_outcome",
  "successes_failures", "'Early signal' section", None, impl="No evidence yet of a higher clinical success rate for AI-originated molecules.", rel=R_LAND)
c("in_insilico_ph3", "Insilico announced the start of a Phase III trial of rentosertib on 2026-07-07 (search snippet seen; page and trial registry not opened).",
  "HYPOTHESIS", "NEEDS_MORE_RESEARCH", [IN], [S(6030)], "Metadata-only company snippet; verify on ClinicalTrials.gov.", "unknown",
  "scientific_rd", None, {"event": "2026-07-07"}, rel=R_LAND)
c("in_zymergen", "Ginkgo Bioworks agreed in July 2022 to buy Zymergen for about USD 300 million, one-tenth of its roughly USD 3 billion valuation at its April 2021 IPO, after Zymergen reported cumulative net losses of USD 1.2 billion, discontinued its first product, and had cut 220 jobs with 80 more planned.",
  "FACT", "SUPPORTED", [IN], [S(6007)], "Independent trade report citing company filings; Zymergen's later Chapter 11 is in search snippets only.", "demonstrated_outcome",
  "robotics_automation", "paragraphs 'The $300 million purchase price' and 'Sustained net losses'", {"event": "2022-07"}, single=False, impl="Highly automated, ML-driven biofoundry did not deliver commercial products at the scale priced into its IPO.", ents={"partners": ["Ginkgo Bioworks"], "technologies": ["biofoundry automation"]}, rel=R_LAB)
c("in_automation_calib", "Across the cases reviewed, the owned or venture-funded 'cloud lab' and biofoundry models (Lilly Life Sciences Studio, Zymergen) ended in divestment or distressed sale, while the service-lab model continues at a CRO (Arctoris); no fully autonomous closed-loop lab with a published discovery outcome was found in any source opened.",
  "INTERPRETATION", "PARTIALLY_SUPPORTED", [LL, IN], [S(6005), S(6006), S(6007)], "Pattern from three cases, one with unknown cause; Emerald Cloud Lab and others not investigated.", "operational",
  "robotics_automation", None, None, contrary="Sample is small; absence of evidence for autonomous labs reflects limited search, not proof.", impl="Treat 'autonomous lab' as early-stage; buy data generation as a service.", rel=R_LAB)

# ---------------------------------------------------------------- CROSS-CUTTING INTERPRETATIONS / RECOMMENDATIONS
c("x_posture", "Lilly has the most aggressive AI build (own compute, a data-as-product platform, many external model partners), J&J concentrates on productivity use cases plus MedTech robotics and surgical data, AbbVie on an internal knowledge graph plus partners, and Takeda on external partnerships.",
  "INTERPRETATION", "SUPPORTED", [LL, JJ, AV, TK], [S(6002), S(6014), S(6019), S(6022)], "Synthesis of company-stated activities in sources opened; all interested-party.", "unknown",
  "competitive_advantage", None, None, single=False, rel=R_LAND)
c("x_outcomes", "Only J&J's MedTech devices have regulator-verified and commercial milestones (OTTAVA De Novo, MONARCH 510(k) iterations); no source opened shows a published discovery outcome, cost saving or revenue effect from any of the four companies' AI drug-discovery or data initiatives.",
  "INTERPRETATION", "SUPPORTED", [LL, JJ, AV, TK], [S(6015), S(6016), S(6002), S(6014), S(6019)], "Based on the sources opened; J&J's 2.6x enrolment and similar figures are self-reported, not independent.", "unknown",
  "competitive_advantage", None, None, single=False, impl="Maturity is dominated by announcements and infrastructure; Takeda should not infer competitor advantage from announcement volume.", rel=R_LAND)
c("x_defensibility", "Lilly's most defensible asset is proprietary experimental data (company-estimated over USD 1 billion to generate, CLM-000280) paired with a federated platform that lets partners add data; compute and third-party models are purchasable by rivals.",
  "INTERPRETATION", "PARTIALLY_SUPPORTED", [LL], [S(6001), S(6010), S(6002)], "Reasoned from company descriptions; the USD 1 billion figure is Lilly's own estimate and unaudited.", "operational",
  "competitive_advantage", None, None, impl="Replicating needs decades of consistent assay data, which Takeda may not have in comparable volume.", rel=R_LAND + R_CARD)
c("x_federated", "Both Lilly TuneLab and the Apheris AISB consortium use federated learning so partners can improve shared models without pooling raw data; TuneLab is Lilly-led and AISB is multi-pharma, with Takeda, AbbVie and J&J in AISB.",
  "INTERPRETATION", "SUPPORTED", [LL, TK, AV, JJ], [S(6010), S(6023), S(6008)], "Both descriptions come from the operators.", "pilot",
  "data_ai", None, None, single=False, impl="Federated models are the emerging route for smaller data holders such as Takeda.", rel=R_LAND)
c("x_cost", "Disclosed cash costs of the AI programmes are limited to deal terms (Isomorphic USD 45 million upfront, BigHat USD 30 million, Nabla double-digit millions, Iambic unspecified), the unquantified ARCH investment, a USD 1 billion co-innovation lab (CLM-000281) and a USD 90 million legacy lab figure.",
  "INTERPRETATION", "SUPPORTED", [LL, AV, TK], [S(6004), S(6020), S(6022), S(6021), S(6019), S(6005)], "Compilation of figures from opened sources; many are 'up to' totals.", "unknown",
  "financials", None, None, single=False, impl="Return on AI spend cannot be computed from public data.", rel=R_LAND)
c("x_takeda_rec", "Takeda should prioritise partner-and-watch moves: continue federated consortia (AISB), use contract automation rather than build an owned robotic lab, and require Nabla/Iambic go/no-go gates tied to first-in-human data before scaling spend; matching Lilly's compute build is not supported by the evidence.",
  "RECOMMENDATION", "SUPPORTED", [TK], [S(6005), S(6007), S(6022), S(6023)], "Judgement derived from maturity evidence above; sized only to public information.", "unknown",
  "strategy", None, None, single=False, rel=R_LAND + R_LAB)
c("x_takeda_watch", "Takeda should watch four triggers: independent scientific outputs from Lilly's TuneLab and LillyPod, OTTAVA commercial uptake data, the Nabla first-in-human readout, and whether AISB expands beyond structure prediction without Takeda.",
  "RECOMMENDATION", "SUPPORTED", [TK], [S(6002), S(6022), S(6023), "SRC-000034"], "Triggers follow the evidence gaps in this review.", "unknown",
  "strategy", None, None, single=False, rel=R_LAND)

C[:] = [x for x in C if x is not None]
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as fh:
    for r in C:
        fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
KEYS.write_text(json.dumps(K, indent=1))
print(len(C), "claims", C[0]["claim_id"], C[-1]["claim_id"])
