#!/usr/bin/env python3
"""RUN-0003 — A6 AI/Data/Robotics: four company technology announcements inspected in full (web fetch, 2026-11-21)
plus independent trade-press corroboration found via search. Maturity tags follow the ROS enumeration.
Press releases establish that an announcement occurred, not that value was realized (source_quality_rules.md)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import ROOT  # noqa
T = "2026-11-21T12:10:00+00:00"; D = "2026-11-21"


def src(tmp, co, title, publisher, stype, tier, url, pub, cat, status="retrieved", local=None, sha=None, rights="company_terms", lim=None):
    return {"record_type": "source", "tmp_id": tmp, "title": title, "author_or_org": publisher, "publisher": publisher, "company": co,
            "subject_category": cat, "source_type": stype, "credibility_tier": tier, "original_url": url, "canonical_url": url,
            "published_at": pub, "reporting_period": None, "retrieved_at": T, "identifiers": {}, "local_document_path": local,
            "local_extracted_text_path": None, "content_sha256": sha, "access_status": status, "rights": rights,
            "limitations": lim or "Company announcement; establishes the announcement, not realized value.", "added_by": "A6", "run_id": "RUN-0003-tech-press"}


def clm(stmt, cos, domains, ents, support, corro, single, maturity, kind="FACT", status="SUPPORTED", rationale="", impl=None, event=None, value=None, unit=None, contrary=None):
    return {"record_type": "claim", "statement": stmt, "kind": kind, "companies": cos, "domains": domains, "entities": ents,
            "supporting_sources": support, "independent_corroboration": corro, "single_interested_source": single, "contrary_evidence": contrary or [],
            "value": value, "unit": unit, "reporting_period": None, "event_date": event, "basis": None, "status": status,
            "confidence_rationale": rationale, "maturity": maturity, "last_verified": D, "related_reports": [], "implications": impl, "added_by": "A6", "run_id": "RUN-0003-tech-press"}


recs = [
 src("TMP-tunelab", "LLY", "Lilly launches TuneLab platform to give biotechnology companies access to AI-enabled drug discovery models built through over $1 billion in research investment", "Eli Lilly and Company (PR Newswire)", "press_release", "T2_company_published",
     "https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies", "2025-09-09", ["data_ai", "partnerships_ma"]),
 src("TMP-tunelab-dive", "LLY", "Lilly to give biotech startups access to AI tools", "BioPharma Dive", "news_report", "T3_independent_reporting",
     "https://www.biopharmadive.com/news/eli-lilly-biotech-ai-tunelab-drug-discovery-startups/759630/", "2025-09-09", ["data_ai"], status="metadata_only", rights="copyrighted_excerpt_only", lim="Located via search; headline and dateline confirmed, article body not yet inspected."),
 src("TMP-nvidia-lab", "LLY", "NVIDIA and Lilly Announce Co-Innovation AI Lab to Reinvent Drug Discovery in the Age of AI", "NVIDIA Newsroom", "press_release", "T2_company_published",
     "https://nvidianews.nvidia.com/news/nvidia-and-lilly-announce-co-innovation-lab-to-reinvent-drug-discovery-in-the-age-of-ai", "2026-01-12", ["data_ai", "robotics_automation", "partnerships_ma"],
     local="New_mediciine/evidence_library/raw_documents/press/LLY_nvidia_lab.html", sha="3663e612774278aa"),
 src("TMP-ottava-fda", "JNJ", "Johnson & Johnson Receives FDA Market Authorization in the U.S. for its OTTAVA Robotic Surgical System", "Johnson & Johnson", "press_release", "T2_company_published",
     "https://investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-Receives-FDA-Market-Authorization-in-the-U-S--for-its-OTTAVA-Robotic-Surgical-System/default.aspx", "2026-07-22", ["robotics_automation", "policy_regulation"]),
 src("TMP-ottava-mtd", "JNJ", "J&J gets FDA authorization for Ottava robot, teeing up competition with Intuitive", "MedTech Dive", "news_report", "T3_independent_reporting",
     "https://www.medtechdive.com/news/jj-gets-fda-authorization-for-ottava-robot-teeing-up-competition-with-int/825905/", "2026-07-22", ["robotics_automation"], status="metadata_only", rights="copyrighted_excerpt_only", lim="Located via search; headline/dateline confirmed, body not yet inspected."),
 src("TMP-ottava-install", "JNJ", "Johnson & Johnson Announces First Commercial Installation of the OTTAVA Robotic Surgical System at Memorial Hermann Health System", "Johnson & Johnson", "press_release", "T2_company_published",
     "https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-Announces-First-Commercial-Installation-of-the-OTTAVA-Robotic-Surgical-System-at-Memorial-Hermann-Health-System/default.aspx", "2026-11-19", ["robotics_automation", "commercial_market_access"], status="metadata_only", lim="Located via search (snippet only); full text not yet inspected."),
 src("TMP-valkai", "ABBV", "AbbVie Partners with Valkai to Apply Advanced AI Across Targeted Areas of Clinical Development", "AbbVie (PR Newswire)", "press_release", "T2_company_published",
     "https://news.abbvie.com/2026-09-29-AbbVie-Partners-with-Valkai-to-Apply-Advanced-AI-Across-Targeted-Areas-of-Clinical-Development", "2026-09-29", ["data_ai", "partnerships_ma"],
     local="New_mediciine/evidence_library/raw_documents/press/ABBV_valkai.html", sha="d97edaac6dc8e982"),
 # ---- claims ----
 clm("On September 9, 2025 Eli Lilly launched Lilly TuneLab, an AI/ML platform giving selected biotech companies access to Lilly-trained drug-discovery models (drug disposition, safety and preclinical datasets covering hundreds of thousands of molecules); Lilly estimates the underlying proprietary data cost over USD 1 billion to generate. Access is federated (third-party hosted) and partners contribute training data in return.",
     ["LLY"], ["data_ai", "partnerships_ma", "competitive_advantage"], ["Eli Lilly", "TuneLab", "Catalyze360", "federated learning"],
     [{"source_id": "TMP-tunelab", "locator": "paragraphs 1-3 of the release"}], ["TMP-tunelab-dive"], False, "OPERATIONAL",
     rationale="Launch and design verified in the full release; independent outlet confirms the launch date. The USD 1 billion figure is Lilly's own estimate of historical data cost, not an audited number. No outcome evidence yet.",
     impl="An ecosystem/platform move: Lilly monetises proprietary data as influence over the biotech pipeline (data-for-access), analogous in intent to developer-platform strategies; whether it yields assets is unproven.", event="2025-09-09"),
 clm("On January 12, 2026 NVIDIA and Eli Lilly announced an AI co-innovation lab in the San Francisco Bay Area with up to USD 1 billion joint investment over five years in talent, infrastructure and compute, built on NVIDIA BioNeMo and the Vera Rubin architecture, initially targeting a 'continuous learning system' connecting Lilly's agentic wet labs with computational dry labs; work was expected to begin in South San Francisco in early 2026.",
     ["LLY"], ["data_ai", "robotics_automation", "partnerships_ma"], ["Eli Lilly", "NVIDIA", "BioNeMo", "autonomous laboratory"],
     [{"source_id": "TMP-nvidia-lab", "locator": "News summary and paragraphs 2-6"}], [], True, "CONCEPT",
     rationale="Joint announcement by both parties; 'up to' commitment, no spend yet reported; lab had not started at announcement. Maturity = announced concept.",
     impl="Signals Lilly's bet that the discovery bottleneck is data generation + compute, not model access; the robotics/'physical AI' element targets manufacturing capacity, Lilly's stated binding constraint.", event="2026-01-12", value=1000, unit="USD_millions"),
 clm("The NVIDIA–Lilly release states that Lilly's previously announced AI supercomputer ('AI factory', announced in autumn 2025) is intended to train large biomedical foundation models and to support manufacturing, medical imaging and scientific-agent applications, including digital twins of manufacturing lines using NVIDIA Omniverse.",
     ["LLY"], ["data_ai", "robotics_automation"], ["Eli Lilly", "NVIDIA", "AI factory", "digital twin"],
     [{"source_id": "TMP-nvidia-lab", "locator": "paragraphs 'Building a Continuous Learning System' and 'physical AI'"}], [], True, "CONCEPT",
     rationale="Intent statements only; the original AI-factory announcement has not yet been retrieved (open item).", impl=None),
 clm("On July 22, 2026 the U.S. FDA granted De Novo authorization to Johnson & Johnson's OTTAVA table-integrated soft-tissue robotic surgical system for multiple upper-abdominal general-surgery procedures (including gastric bypass, cholecystectomy, gastrectomy, sleeve, appendectomy, hiatal hernia repair); J&J said it would launch with select U.S. customers and that an inguinal-hernia trial was ongoing.",
     ["JNJ"], ["robotics_automation", "policy_regulation", "pipeline"], ["Johnson & Johnson", "OTTAVA", "FDA De Novo", "surgical robotics"],
     [{"source_id": "TMP-ottava-fda", "locator": "paragraphs 1-3"}], ["TMP-ottava-mtd"], False, "OPERATIONAL",
     rationale="Regulatory authorization is a verifiable event, independently reported the same day. Authorization ≠ clinical superiority or commercial adoption.",
     impl="J&J now has a regulated entrant against Intuitive after years of delay; the strategic question is adoption economics, not technical feasibility.", event="2026-07-22"),
 clm("On November 19, 2026 J&J announced the first commercial installation of OTTAVA at Memorial Hermann–Texas Medical Center (Houston), following the July 2026 De Novo authorization.",
     ["JNJ"], ["robotics_automation", "commercial_market_access"], ["Johnson & Johnson", "OTTAVA", "Memorial Hermann"],
     [{"source_id": "TMP-ottava-install", "locator": "headline and first paragraph (search snippet)"}], [], True, "OPERATIONAL", status="PARTIALLY_SUPPORTED",
     rationale="Only the headline/snippet has been read; full release not yet inspected. One site = launch, not scale.", event="2026-11-19"),
 clm("On September 29, 2026 AbbVie announced a partnership with Valkai (life-sciences AI platform) to deploy AI capabilities in targeted areas of clinical development, framed under its enterprise 'AI@AbbVie' approach; the release reports no deployed-system metrics, timelines or financial terms.",
     ["ABBV"], ["data_ai", "partnerships_ma"], ["AbbVie", "Valkai", "AI@AbbVie", "clinical development"],
     [{"source_id": "TMP-valkai", "locator": "paragraphs 1-4 and 'About AI@AbbVie'"}], [], True, "PILOT",
     rationale="Single company source; aspirational language ('potential to help'); maturity set to PILOT at most, pending any evidence of deployment.",
     impl="Consistent with a buy/partner posture on AI tooling rather than Lilly's build-infrastructure posture; a comparison point for the cross-company AI matrix.", event="2026-09-29"),
 clm("Across the three competitors' most recent technology announcements, only OTTAVA has a regulator-verified milestone (FDA De Novo) and a commercial installation; Lilly's TuneLab is a live platform without disclosed scientific outcomes; the NVIDIA–Lilly lab and the AbbVie–Valkai partnership are announcements with no reported deployment metrics.",
     ["MULTI"], ["data_ai", "robotics_automation", "competitive_advantage"], ["Eli Lilly", "Johnson & Johnson", "AbbVie"],
     [{"source_id": "TMP-tunelab", "locator": "whole release"}, {"source_id": "TMP-nvidia-lab", "locator": "whole release"}, {"source_id": "TMP-ottava-fda", "locator": "whole release"}, {"source_id": "TMP-valkai", "locator": "whole release"}], [], False, None, kind="INTERPRETATION",
     rationale="Analyst synthesis of the four inspected releases; scope limited to these items, not the companies' full AI portfolios.",
     impl="Maturity, not announcement volume, should drive the cross-company AI/robotics matrix."),
]
out_dir = os.path.join(ROOT, "New_mediciine", "evidence_library", "staging", "A6_ai_robotics"); os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "batch_0003_tech_press.jsonl")
with open(out, "w") as f:
    for r in recs:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"staged {sum(r['record_type']=='source' for r in recs)} sources, {sum(r['record_type']=='claim' for r in recs)} claims -> {out}")
