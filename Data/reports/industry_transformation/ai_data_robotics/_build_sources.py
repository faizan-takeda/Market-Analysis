#!/usr/bin/env python3
"""A6 shard source builder (writes shards/A6_ai_robotics/sources.jsonl). Idempotent: rewrites file."""
import json
from pathlib import Path

OUT = Path("/Users/palrahma/Desktop/MEDICINE/New_mediciine/evidence_library/shards/A6_ai_robotics/sources.jsonl")
AD = "2026-11-21"
S = []


def src(title, publisher, company, domain, stype, url, cred, status, date=None, passage=None,
        locator=None, notes=None, lic="public web page; excerpt <=600 chars", period=None):
    n = 6000 + len(S)
    r = {"source_id": f"SRC-{n:06d}", "title": title, "publisher": publisher, "company": company,
         "domain": domain, "source_type": stype, "original_url": url, "canonical_url": url,
         "access_date": AD, "credibility": cred, "access_status": status, "licensing": lic}
    if date:
        r["publication_date"] = date
    if passage:
        r["inspected_passage"] = passage
    if locator:
        r["locator"] = locator
    if notes:
        r["notes"] = notes
    if period:
        r["reporting_period"] = period
    S.append(r)


# 6000
src("Lilly announces new $4.5 billion site - the Lilly Medicine Foundry", "Eli Lilly and Company (investor.lilly.com)",
    "eli_lilly", "robotics_automation", "press_release",
    "https://investor.lilly.com/news-releases/news-release-details/lilly-announces-new-45-billion-site-lilly-medicine-foundry-drive",
    "T2_company_technical", "retrieved", "2024-10-02",
    "The first-ever facility of its kind, combining research and manufacturing in a single location, the Medicine Foundry will be located in Indiana's LEAP Research and Innovation District in Lebanon, Indiana, and will expand the company's investment there to more than $13 billion.",
    "paragraph 1; 'Opening in late 2027' sub-headline", "Release date 2024-10-02 taken from the search-result snippet of the same URL; the fetched text omitted the dateline. Company-interested, forward-looking.")
# 6001
src("Lilly Deploys World's Largest, Most Powerful AI Factory for Drug Discovery Using NVIDIA Blackwell-Based DGX SuperPOD",
    "NVIDIA blog", "eli_lilly", "data_ai", "press_release",
    "https://blogs.nvidia.com/blog/lilly-ai-factory-nvidia-blackwell-dgx-superpod/", "T2_company_technical", "retrieved", "2025-10",
    "Built with 1,016 NVIDIA Blackwell Ultra GPUs and announced today at NVIDIA GTC Washington, D.C., the AI factory is poised to compress drug discovery timelines and enable accelerated breakthroughs in genomics, personalized medicine and molecular design at industrial scale.",
    "opening paragraphs; sections 'Research and Biomanufacturing With Physical and Agentic AI'",
    "Vendor (NVIDIA) blog co-promoting Lilly; date shown only as October 2025 (GTC Washington D.C.; exact day not in fetched text). Interested party.")
# 6002
src("Now Live: The World's Most Powerful AI Factory for Pharmaceutical Discovery and Development (LillyPod)", "NVIDIA blog",
    "eli_lilly", "data_ai", "press_release", "https://blogs.nvidia.com/?p=90297", "T2_company_technical", "retrieved", None,
    "Lilly this week launched the most powerful AI factory wholly owned and operated by a pharmaceutical company to help its teams make meaningful medical advancements faster, more accurately and at unprecedented scale. Dubbed LillyPod, it's the world's first NVIDIA DGX SuperPOD with DGX B300 systems.",
    "paragraphs 1-3 and 'Step Behind the Scenes of the LillyPod'",
    "Publication date not shown in fetched text (BiopharmaTrend coverage dated late Feb 2026). Vendor blog; interested party. Quotes Lilly executives.")
# 6003
src("Eli Lilly Launches Pharma's Largest AI Supercomputer", "BiopharmaTrend", "eli_lilly", "data_ai", "news_trade",
    "https://www.biopharmatrend.com/news/eli-lilly-launches-pharmas-largest-ai-supercomputer-1512/", "T3_independent_reputable", "retrieved", "2026-02",
    "LillyPod is delivering more than 9,000 petaflops (one quadrillion floating-point operations per second) of AI performance. It was assembled in approximately four months, having initially been announced in October 2025 as part of Lilly's \"AI-factory\" effort, and inaugurated in Indianapolis.",
    "'Inside the Pod' section",
    "Trade press restating company/NVIDIA statements ('According to the company'); NOT independent corroboration of performance claims. Month from search metadata (late Feb 2026).")
# 6004
src("Isomorphic Labs announces strategic multi-target research collaboration with Lilly", "Isomorphic Labs via PR Newswire",
    "eli_lilly", "partnerships_ma", "press_release",
    "https://www.prnewswire.com/news-releases/isomorphic-labs-announces-strategic-multi-target-research-collaboration-with-lilly-302027392.html",
    "T2_company_technical", "retrieved", "2024-01-07",
    "Under the terms of the agreement, Isomorphic Labs will partner with Lilly to discover small molecule therapeutics against multiple targets and will receive an upfront cash payment of $45 million. Isomorphic Labs is eligible to receive up to $1.7 billion in performance-based milestone payments, excluding the upfront payment and any subsequent tiered royalties of up to low double digits on net sales.",
    "paragraph 2", "Release date 2024-01-07 inferred from TechCrunch URL date and search metadata; the fetched page had no dateline. Issued by Isomorphic (interested party); Lilly terms are Isomorphic's statement.")
# 6005
src("Eli Lilly Sells Automated Lab to Arctoris, Platform Relocates to Oxford", "BiopharmaTrend", "eli_lilly", "robotics_automation", "news_trade",
    "https://www.biopharmatrend.com/news/eli-lilly-sells-automated-lab-to-arctoris-platform-relocates-to-oxford-949/", "T3_independent_reputable", "retrieved", "2024-09",
    "Arctoris, a contract research organization (CRO) specializing in automated drug discovery, has acquired Eli Lilly's Life Sciences Studio laboratory. The acquisition involves relocating the lab's advanced automation platform from San Diego to Arctoris' headquarters in Oxford, UK, effectively doubling the company's laboratory capacity.",
    "paragraphs 1-2", "Trade report; month from search metadata (Sept 2024). States lab 'established by Eli Lilly in 2017 as part of a $90 million investment' whereas Fierce Biotech (not opened) says it was launched ~2020; discrepancy unresolved. No sale price or reason for sale given.")
# 6006
src("Arctoris Opens Biophysics Centre To Target Data Bottleneck in AI Drug Design", "BiopharmaTrend", "industry", "robotics_automation", "news_trade",
    "https://www.biopharmatrend.com/news/arctoris-opens-biophysics-centre-to-target-data-bottleneck-in-ai-drug-design-1530/", "T3_independent_reputable", "retrieved", "2026-03",
    "In 2024, Arctoris acquired Eli Lilly's automated Life Sciences Studio and relocated it to Oxford, adding to its robotic infrastructure. More recently, Arctoris was selected for the UK's ARIA AI Scientist program to support development of an autonomous research system targeting endometriosis.",
    "'Context' section", "Trade press; month from search metadata (Mar 2026). Largely restates Arctoris announcements.")
# 6007
src("Synbio Synergy: Ginkgo to Acquire Troubled Zymergen for $300M", "GEN (Genetic Engineering & Biotechnology News)", "industry", "robotics_automation", "news_trade",
    "https://www.genengnews.com/news/synbio-synergy-ginkgo-to-acquire-troubled-zymergen-for-300m/", "T3_independent_reputable", "retrieved", "2022-07",
    "The $300 million purchase price is just one-tenth of Zymergen's approximately $3 billion valuation at the time of its eye-popping $575 million initial public offering (IPO), completed in April 2021.",
    "paragraph 'The $300 million purchase price...'", "Independent trade report with figures from Zymergen/Ginkgo filings. Month from search metadata (Jul 2022).")
# 6008
src("insitro partners with Lilly to build first-in-kind machine learning models to advance small molecule drug discovery", "insitro", "eli_lilly", "data_ai", "press_release",
    "https://www.insitro.com/news/insitro-partners-with-lilly-to-build-first-in-kind-machine-learning-models-to-advance-small-molecule-drug-discovery/", "T2_company_technical", "retrieved", "2025-09-09",
    "Under the agreement, insitro will build advanced machine learning models and train them on Lilly's proprietary preclinical data, leveraging a rich set of in vitro and in vivo measurements from a vast array of compounds with established ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) properties",
    "paragraph 4", "Counterparty press release (interested party); no financial terms disclosed.")
# 6009
src("Lilly collaborates with OpenAI to discover novel medicines to treat drug-resistant bacteria", "Eli Lilly via PR Newswire", "eli_lilly", "data_ai", "press_release",
    "https://www.prnewswire.com/news-releases/lilly-collaborates-with-openai-to-discover-novel-medicines-to-treat-drug-resistant-bacteria-302180973.html", "T2_company_technical", "retrieved", "2024-06-25",
    "Eli Lilly and Company (NYSE: LLY) announced a collaboration with OpenAI that will allow Lilly to leverage OpenAI's generative AI to invent novel antimicrobials to treat drug-resistant pathogens.",
    "paragraph 1", "Date 2024-06-25 from search-result snippet of the same URL. The research brief's 'Sept 2025' date for this collaboration is incorrect. No terms, targets or outcomes disclosed.")
# 6010
src("Benchling and Lilly TuneLab Partner to Democratize Access to AI Models for Scientists Everywhere", "Benchling", "eli_lilly", "data_ai", "press_release",
    "https://www.benchling.com/blog/benchling-and-lilly-tunelab-partner-to-democratize-access-to-ai-models", "T2_company_technical", "retrieved", "2026-01-08",
    "Later this year, Benchling customers will be able to opt into the program and start using Lilly's proprietary models in their own scientific workflows.",
    "final paragraph before 'About Benchling'", "Platform partner press release (interested party). Reports no uptake numbers.")
# 6011
src("AI-Unicorn Chai Discovery and Eli Lilly to Train Custom AI Models for Biologics Design", "BiopharmaTrend", "eli_lilly", "data_ai", "news_trade",
    "https://www.biopharmatrend.com/news/ai-unicorn-chai-discovery-and-eli-lilly-to-train-custom-ai-models-for-biologics-design-1450/", "T3_independent_reputable", "retrieved", "2026-01",
    "Chai will provide Lilly with access to its generative antibody design models, including Chai-2, which reportedly achieves double-digit experimental hit rates in zero-shot design settings. The collaboration follows prior internal evaluation of Chai's designs by Lilly. No financial terms were disclosed.",
    "paragraph 3", "Month approximated from search metadata (early Jan 2026); article text carries no explicit date. Hit-rate claim is Chai's own ('reportedly').")
# 6012
src("Lilly unveils new genetic medicine facility in Lebanon LEAP District and $4.5 billion investment", "WFYI (Indianapolis public media)", "eli_lilly", "robotics_automation", "news_trade",
    "https://www.wfyi.org/wfyi-news/2026-05-06/lilly-unveils-new-genetic-medicine-facility-in-lebanon-leap-district-and-4-5-billion-investment", "T3_independent_reputable", "retrieved", "2026-05-06",
    "During a tour, the company debuted some of the new technology. Scientists in white lab coats monitored robotic machines that maneuver, dose, measure and seal the medicines.",
    "paragraph beginning 'Lilly plans to produce next generation medicines'", "Independent local reporter at the ribbon-cutting; observed a company-guided tour only. No throughput or yield data.")
# 6013
src("AI Insights from Big Pharma: Johnson & Johnson reveals its revised AI strategy", "DeepLearning.AI - The Batch", "johnson_johnson", "data_ai", "news_trade",
    "https://www.deeplearning.ai/the-batch/johnson-johnson-reveals-its-revised-ai-strategy", "T4_expert_commentary", "retrieved", "2025-04",
    "A centralized governing board oversaw as many as 900 experiments. After finding that 10 percent to 15 percent of use cases drove about 80 percent of the value, the company shifted responsibility for AI projects to specific departments to focus on high-value applications.",
    "'How it works' paragraph", "Secondary summary of J&J CIO remarks given to Greylock and the Wall Street Journal; not independent of SRC-006014. Month approximated from search metadata (Apr 2025).")
# 6014
src("Gen AI Present and Future: A Conversation with Jim Swanson, CIO at Johnson & Johnson", "Greylock (Asheem Chandna interview)", "johnson_johnson", "data_ai", "interview_transcript",
    "https://greylock.com/greymatter/gen-ai-present-and-future-a-conversation-with-jim-swanson-cio-at-johnson-johnson/", "T2_company_technical", "retrieved", "2025-03-13",
    "Over the past two years, much of our Gen AI work was in proofs of concept and pilots; we were more focused on learning. But now we are at the point where we are deploying Gen AI to our benefit.",
    "answer to 'To what extent are Gen AI tools cascaded across J&J?'", "Interview with J&J's CIO by an investor (Greylock); interested party, no independent verification of quoted metrics.")
# 6015
src("Johnson & Johnson Announces MONARCH QUEST 3, Advancing the Latest in Robotically-Assisted Bronchoscopy", "Johnson & Johnson", "johnson_johnson", "robotics_automation", "press_release",
    "https://www.jnj.com/media-center/press-releases/johnson-johnson-announces-monarch-quest-3-advancing-the-latest-in-robotically-assisted-bronchoscopy", "T2_company_technical", "retrieved", "2026-08-17",
    "Johnson & Johnson today announced U.S. 510(k) regulatory clearance for MONARCH QUEST 3, the latest software update for the MONARCH Platform. ... MONARCH QUEST 3 is designed to deliver: AI-powered nodule segmentation, designed to automatically generate more accurate nodule boundaries with a single click during pre-procedural planning",
    "paragraphs 1 and 'Advancing navigation through MONARCH QUEST 3'", "Company release; performance support cited is internal technical reviews (Feb-Jul 2025), not peer-reviewed. Excerpt joins two passages with an ellipsis.")
# 6016
src("Inside J&J's OTTAVA Robotic Surgical System development", "Johnson & Johnson (jnj.com Innovation)", "johnson_johnson", "robotics_automation", "company_web",
    "https://www.jnj.com/innovation/inside-ottava-robotic-surgical-system-development", "T2_company_technical", "retrieved", "2026-10-08",
    "In our clinical trial results, we found that OTTAVA was able to go into operating rooms as small as 243 square feet that were previously considered too small for robotic surgery.",
    "Q&A 'How does the novel architecture of OTTAVA address today's OR' and footnote ***", "Company-authored feature. Surgeon/staff survey in footnote is n=12 surgeons and n=8 staff after 1-5 Roux-en-Y cases each (Likert scale). Interested party.")
# 6017
src("Johnson & Johnson Advances Polyphonic AI Fund for Surgery for Data-Driven Healthcare", "Johnson & Johnson", "johnson_johnson", "data_ai", "press_release",
    "https://www.jnj.com/media-center/press-releases/johnson-johnson-advances-polyphonic-ai-fund-for-surgery-for-data-driven-healthcare", "T2_company_technical", "retrieved", "2025-10-27",
    "The Polyphonic ecosystem is available in early access to select hospitals only.",
    "last paragraph before 'About Surgical Solutions'", "Company release (interested party).")
# 6018
src("Johnson & Johnson Advances Creation of Global Intelligent OR Network in collaboration with Department of Health - Abu Dhabi", "Johnson & Johnson MedTech", "johnson_johnson", "data_ai", "press_release",
    "https://www.jnjmedtech.com/en-US/news/press-releases/johnson-johnson-advances-creation-of-global-intelligent-or-network-in-collaboration-with-department-of-health-abu-dhabi/", "T2_company_technical", "retrieved", "2026-05-21",
    "the initiative is expected to deploy the Polyphonic Surgery application into Abu Dhabi's intelligent health system to connect operating rooms across the emirate to a surgical intelligence system.",
    "paragraph 1", "Company release; forward-looking ('expected to deploy'); no deployed-site count.")
# 6019
src("AbbVie's R&D Convergence Hub", "Bio-IT World (Allison Proffitt)", "abbvie", "data_ai", "news_trade",
    "https://www.bio-itworld.com/news/2023/08/24/abbvie-s-r-d-convergence-hub", "T3_independent_reputable", "retrieved", "2023-08-24",
    "The ARCH project relied on less than ten full-time AbbVie employees, Martin said, but many contractors. \"The number of partners and consultants we brought in to co-develop the interfaces, to co-build the infrastructure, that's significant.\"",
    "section 'Effort of Partners'", "Trade report of a conference talk by AbbVie's head of AI (interested speaker); award-winner write-up. Reports AbbVie-stated figures, not audited.")
# 6020
src("AbbVie and BigHat Biosciences Announce Research Collaboration to Leverage AI and ML to Discover Next-Generation Therapeutic Antibodies", "AbbVie via PR Newswire", "abbvie", "partnerships_ma", "press_release",
    "https://news.abbvie.com/2023-12-05-AbbVie-and-BigHat-Biosciences-Announce-Research-Collaboration-to-Leverage-Artificial-Intelligence-and-Machine-Learning-to-Discover-Next-Generation-Therapeutic-Antibodies", "T2_company_technical", "retrieved", "2023-12-05",
    "Under the terms of the agreement, BigHat will receive an upfront payment of $30 million and may be eligible to receive up to approximately $325 million in aggregate research and development milestones, with potential for further commercial milestones as well as tiered royalties on net sales.",
    "paragraph 4", "Company release (interested party).")
# 6021
src("Iambic Announces Collaboration with Takeda to Advance AI-Driven Design of Small Molecules (Business Wire, reproduced by Yahoo Finance)", "Iambic via Business Wire / Yahoo Finance", "takeda", "partnerships_ma", "press_release",
    "https://finance.yahoo.com/news/iambic-announces-collaboration-takeda-advance-130000281.html", "T2_company_technical", "retrieved", "2026-02-09",
    "Under the terms of the agreement, Iambic will receive upfront, research cost, and technology access payments and is eligible to receive success-based payments that could exceed $1.7 billion. The company is also eligible to receive royalties on net sales of any products generated from this collaboration.",
    "final paragraph", "Counterparty paid press release (flagged 'paid press release'); upfront amount not stated in the opened text.")
# 6022
src("US biotech Nabla Bio, Japan's Takeda expand AI drug design partnership", "Reuters via Yahoo Finance", "takeda", "partnerships_ma", "news_tier1",
    "https://finance.yahoo.com/news/us-biotech-nabla-bio-japans-090242368.html", "T3_independent_reputable", "retrieved", "2025-10-14",
    "Under the new multi-year agreement, which builds on an earlier collaboration launched in 2022, Nabla will receive upfront and research cost payments in double-digit millions. The company is also eligible for success-based payments worth more than $1 billion.",
    "paragraph 2", "Reuters wire; terms and timelines are Nabla's statements.")
# 6023
src("AI Structural Biology (AISB) network - Federated OpenFold3 Initiative results", "Apheris", "industry", "data_ai", "company_web",
    "https://www.apheris.com/networks/aisb", "T2_company_technical", "retrieved", None,
    "AbbVie, Astex Pharmaceuticals, Bristol Myers Squibb, Johnson & Johnson and Takeda each fine-tuned OpenFold3 locally, inside their own environment. Only model parameters were aggregated. No structures were pooled.",
    "section 'Five member companies contributed proprietary structures'", "Vendor/organiser page (interested party); page undated (references 2026 data); benchmark results are not peer-reviewed.")
# 6024
src("Three more pharmas join OpenFold3 AI consortium", "pharmaphorum", "industry", "data_ai", "news_trade",
    "https://pharmaphorum.com/news/three-more-pharmas-join-openfold3-ai-consortium", "T3_independent_reputable", "retrieved", "2025-10",
    "Bristol Myers Squibb, Takeda, and Astex Pharma have joined a recently formed consortium that is working on refining the OpenFold structure prediction platform with pharma industry data.",
    "paragraph 1", "Trade report derived from Apheris announcement; month from search metadata (early Oct 2025). Not independent of SRC-006023.")
# 6025
src("Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products (draft guidance)", "U.S. Food and Drug Administration", "industry", "policy_regulation", "regulatory_record",
    "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological", "T1_primary_official", "retrieved", "2025-01",
    "Specifically, this guidance provides a risk-based credibility assessment framework that may be used for establishing and evaluating the credibility of an AI model for a particular context of use (COU).",
    "guidance summary paragraph; docket FDA-2024-D-4689", "FDA guidance landing page; draft, 'Not for implementation. Contains non-binding recommendations.' Finalisation status not checked.", lic="US government record")
# 6026
src("Recursion Halts Four Pipeline Programs, Sharpening Cancer, Rare Disease Focus", "GEN (Genetic Engineering & Biotechnology News)", "industry", "successes_failures", "news_trade",
    "https://www.genengnews.com/topics/artificial-intelligence/recursion-halts-four-pipeline-programs-sharpening-cancer-rare-disease-focus/", "T3_independent_reputable", "retrieved", "2025-05",
    "Recursion said it will end development for four of its 11 pipeline programs ... and pause a fifth program, in a pruning designed to further focus the artificial intelligence (AI)-based drug developer on cancer and rare disease treatments.",
    "opening paragraph and program list", "Independent trade report with company and analyst quotes. Month from search metadata (May 2025).")
# 6027
src("Insilico's AI-designed rentosertib shows promise in first phase 2a trial results", "Drug Discovery Trends (WTWH Media)", "industry", "scientific_rd", "news_trade",
    "https://www.drugdiscoverytrends.com/insilicos-ai-designed-rentosertib-shows-promise-in-first-phase-2a-trial-results/", "T3_independent_reputable", "retrieved", "2025-06",
    "Previous analyses show AI-originated compounds clear phase 2 at roughly the same 40% rate as conventional drugs, with early high-profile failures including Exscientia's discontinued cancer treatment EXS-21546 and BenevolentAI's dermatitis drug BEN-2293.",
    "section 'Early signal for AI-generated TNIK drug'", "Trade report on Nature Medicine paper (paper itself not opened by this agent). Includes Insilico CEO email statements.")
# 6028 metadata_only
src("Eli Lilly sells and ships San Diego robot lab to UK-based company", "Fierce Biotech", "eli_lilly", "robotics_automation", "news_trade",
    "https://www.fiercebiotech.com/cro/eli-lilly-sells-science-studio-lab-arctoris-moving-automation-platform-san-diego-oxford", "T3_independent_reputable", "metadata_only", "2024-09",
    notes="HTTP 403 on two attempts (web_fetch and CLI). Only the search-result snippet was seen: 'Four years after launching a remote-controlled robotic laboratory in San Diego, Eli Lilly is shipping the operation overseas ... selling a majority of the Life Sciences Studio laboratory to Arctoris'. Not opened.", lic="metadata only")
# 6029
src("Strateos profile (acquisition by Multiply Labs, December 2023)", "Setter VC company profile", "industry", "robotics_automation", "other",
    "https://settervc.com/company/strateos", "T5_speculative", "metadata_only", None,
    notes="Search snippet only: 'In December 2023, Strateos was acquired by Multiply Labs'. Aggregator profile, not opened; no primary announcement found. Treated as unverified; use only for a HYPOTHESIS claim.", lic="metadata only")
# 6030
src("Insilico Initiates Phase III Clinical Trial for Rentosertib", "Insilico Medicine", "industry", "scientific_rd", "press_release",
    "https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr", "T2_company_technical", "metadata_only", "2026-07-07",
    notes="Search snippet only (dateline 'July 7, 2026'; Phase IIa +98.4 mL FVC at 60 mg). Page not opened. Registry/ClinicalTrials.gov confirmation of Phase III not checked.", lic="metadata only")
# 6031
src("AI & Data Convergence (ARCH)", "AbbVie", "abbvie", "data_ai", "company_web",
    "https://www.abbvie.com/science/areas-of-innovation/ai-and-data-convergence.html", "T2_company_technical", "metadata_only", None,
    notes="HTTP 403 on fetch. Search snippet only: ARCH 'centralize[s] and connect[s] data from more than 200 internal and external sources ... over 2 billion points of knowledge'. Not opened.", lic="metadata only")
# 6032
src("Johnson & Johnson Pivots Its AI Strategy", "Wall Street Journal", "johnson_johnson", "data_ai", "news_tier1",
    "https://www.wsj.com/articles/johnson-johnson-pivots-its-ai-strategy-a9d0631f", "T3_independent_reputable", "paywalled", "2025-04",
    notes="Paywalled; only search snippet seen: CIO Swanson says resources go only to highest-value GenAI use cases while redundant or non-working projects are cut. Metadata only.", lic="paywalled (metadata only)")
# 6033
src("Isomorphic lands deals with Lilly, Novartis worth nearly $3B", "Fierce Biotech", "eli_lilly", "partnerships_ma", "news_trade",
    "https://www.fiercebiotech.com/biotech/alphabets-isomorphic-stacks-two-new-deals-lilly-novartis-worth-nearly-3b-ahead-buzzy-jpm", "T3_independent_reputable", "metadata_only", "2024-01",
    notes="Fierce Biotech blocks scripted clients (HTTP 403 pattern); snippet only. Not opened.", lic="metadata only")
# 6034
src("Federal Register: Considerations for the Use of AI To Support Regulatory Decision-Making for Drug and Biological Products; Draft Guidance; Availability; Comment Request", "Federal Register", "industry", "policy_regulation", "regulatory_record",
    "https://www.federalregister.gov/documents/full_text/html/2025/01/07/2024-31542.html", "T1_primary_official", "metadata_only", "2025-01-07",
    notes="Fetch redirected to an anti-bot 'unblock' host; not opened. Search snippet confirms notice 2024-31542 published 2025-01-07.", lic="metadata only")
# 6035
src("Revvity Signals: TuneLab-at-Revvity Federated Learning Program information sheet", "Revvity Signals Software", "eli_lilly", "data_ai", "company_web",
    "https://revvitysignals.com/sites/default/files/documents/4766/TuneLab-at-Revvity-Federated-Learning-Program-2026-08-03-09-50-03.pdf", "T2_company_technical", "metadata_only", "2026-07",
    notes="Search snippet only (information sheet dated July 2026 describing Lilly as program initiator and Revvity Signals hosting the models). Not opened.", lic="metadata only")

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as fh:
    for r in S:
        fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
print(len(S), "sources written; last id", S[-1]["source_id"])
