#!/usr/bin/env python3
"""Validate council_reviews.json, counterarguments.json and the critical_challenges markdown against the claims
registry, assumptions.json and strategy_bets.json (DATA_CONTRACT.md shapes)."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REG = os.path.join(os.path.dirname(ROOT), "New_mediciine", "evidence_library", "claims_registry.jsonl")
claims = {json.loads(l)["claim_id"] for l in open(REG) if l.strip()}
asm = {a["id"] for a in json.load(open(f"{ROOT}/data/assumptions.json"))["assumptions"]}
bets = {b["id"] for b in json.load(open(f"{ROOT}/data/strategy_bets.json"))["bets"]}
errs = []
cr = json.load(open(f"{ROOT}/data/council_reviews.json"))
ca = json.load(open(f"{ROOT}/data/counterarguments.json"))
COUNCILS = {"scientific", "technology", "commercial", "capital", "regulatory_ethics", "red_team", "takeda_execution"}
for r in cr["reviews"]:
    for k in ("bet_id", "council", "verdict", "rationale", "unresolved", "claim_ids"):
        if k not in r: errs.append(f"review missing {k}")
    if r["bet_id"] not in bets: errs.append(f"bad bet {r['bet_id']}")
    if r["council"] not in COUNCILS: errs.append(f"bad council {r['council']}")
    if r["verdict"] not in ("support", "conditional", "oppose"): errs.append("bad verdict")
for d in cr["disagreements"]:
    if d["bet_id"] not in bets or "text" not in d: errs.append("bad disagreement")
pairs = {(r["bet_id"], r["council"]) for r in cr["reviews"]}
unreviewed = {u["bet_id"] for u in cr.get("unreviewed", [])}  # v2: council-proposed bets awaiting independent review
if pairs != {(b, c) for b in bets if b not in unreviewed for c in COUNCILS}: errs.append("review coverage incomplete")
for b in unreviewed:
    print(f"NOTE {b} is listed as not independently reviewed (council-proposed); verdicts pending")
TYPES = {"unsupported_assumption", "unresolved_question", "conflicting_sources", "public_knowledge_gap", "failed_hypothesis", "alternative_interpretation", "caveat"}
ids = set()
for i in ca["items"]:
    for k in ("id", "target", "type", "text", "claim_ids", "assumption_ids"):
        if k not in i: errs.append(f"item missing {k}")
    if i["id"] in ids: errs.append(f"dup id {i['id']}")
    ids.add(i["id"])
    if i["type"] not in TYPES: errs.append(f"{i['id']} bad type")
    if not (i["target"] in bets or i["target"] == "THEME" or i["target"] in claims): errs.append(f"{i['id']} bad target")
    for a in i["assumption_ids"]:
        if a not in asm: errs.append(f"{i['id']} unknown {a}")
blob = json.dumps(cr) + json.dumps(ca)
md = {}
for f in glob.glob(f"{HERE}/*.md"):
    md[os.path.basename(f)] = open(f).read()
used = set(re.findall(r"CLM-\d{6}", blob))
for t in md.values(): used |= set(re.findall(r"CLM-\d{6}", t))
unknown = sorted(c for c in used if c not in claims)
asm_used = set(re.findall(r"ASM-\d{3}", blob))
for t in md.values(): asm_used |= set(re.findall(r"ASM-\d{3}", t))
asm_unknown = sorted(a for a in asm_used if a not in asm)
ivb_bad = sorted(i for i in set(re.findall(r"IVB-\d{3}", blob + "".join(md.values()))) if not 1 <= int(i[4:]) <= 14)
print(f"reviews {len(cr['reviews'])}, disagreements {len(cr['disagreements'])}, counter items {len(ca['items'])}")
print(f"distinct claim ids used: {len(used)}; unknown: {len(unknown)} {unknown}")
print(f"unknown ASM: {asm_unknown}; bad IVB: {ivb_bad}; contract errors: {len(errs)}")
for e in errs: print("  ERROR", e)
print(f"UNKNOWN IDs TOTAL: {len(unknown) + len(asm_unknown) + len(ivb_bad)}")
sys.exit(1 if (unknown or asm_unknown or ivb_bad or errs) else 0)
