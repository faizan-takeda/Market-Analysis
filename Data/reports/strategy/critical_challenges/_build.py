#!/usr/bin/env python3
"""Build A11e outputs: council_reviews.json, counterarguments.json, council_reviews.md, red_team.md,
counterarguments_and_uncertainty.md; validate claim ids against the registry and assumptions/bets/IVB references."""
import json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # strategy/
sys.path.insert(0, HERE)
from _data_reviews import *   # noqa
from _data_redteam import RED
from _data_counter import ITEMS

REG = os.path.join(os.path.dirname(ROOT), "New_mediciine", "evidence_library", "claims_registry.jsonl")
claims = {}
for l in open(REG):
    if l.strip():
        d = json.loads(l)
        claims[d["claim_id"]] = d
asm_ids = {a["id"] for a in json.load(open(f"{ROOT}/data/assumptions.json"))["assumptions"]}
bet_ids = {b["id"] for b in json.load(open(f"{ROOT}/data/strategy_bets.json"))["bets"]}
errors = []

# ------------------------------------------------------------------ council_reviews.json
reviews = []
for bet in sorted(R):
    for c in COUNCILS:
        v, rat, unres, cl = R[bet][c]
        reviews.append({"bet_id": bet, "council": c, "verdict": v, "rationale": rat, "unresolved": unres, "claim_ids": cl.split()})
dis = [{"bet_id": b, "text": t} for b, t in DISAGREEMENTS]
json.dump({"reviews": reviews, "disagreements": dis}, open(f"{ROOT}/data/council_reviews.json", "w"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ counterarguments.json
items = []
for i, (tgt, typ, text, cl, asm) in enumerate(ITEMS, 1):
    items.append({"id": f"CA-{i:03d}", "target": tgt, "type": typ, "text": text, "claim_ids": cl, "assumption_ids": asm})
json.dump({"items": items}, open(f"{ROOT}/data/counterarguments.json", "w"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ validation
allowed_targets = bet_ids | {"THEME"}
for it in items:
    if not (it["target"] in allowed_targets or re.fullmatch(r"CLM-\d{6}", it["target"])):
        errors.append(f"{it['id']}: bad target {it['target']}")
    if re.fullmatch(r"CLM-\d{6}", it["target"]) and it["target"] not in claims:
        errors.append(f"{it['id']}: target claim unknown {it['target']}")
    for c in it["claim_ids"]:
        if c not in claims: errors.append(f"{it['id']}: unknown claim {c}")
    for a in it["assumption_ids"]:
        if a not in asm_ids: errors.append(f"{it['id']}: unknown assumption {a}")
    # ids mentioned in text
    for c in re.findall(r"CLM-\d{6}", it["text"]):
        if c not in claims: errors.append(f"{it['id']}: unknown claim in text {c}")
    for a in re.findall(r"ASM-\d{3}", it["text"]):
        if a not in asm_ids: errors.append(f"{it['id']}: unknown assumption in text {a}")
for r in reviews:
    if r["bet_id"] not in bet_ids: errors.append(f"review bad bet {r['bet_id']}")
    if r["verdict"] not in ("support", "conditional", "oppose"): errors.append("bad verdict")
    if r["council"] not in COUNCILS: errors.append("bad council")
    if not r["claim_ids"]: errors.append(f"{r['bet_id']} {r['council']}: no claim ids")
    for text in (r["rationale"], r["unresolved"]):
        for c in re.findall(r"CLM-\d{6}", text):
            if c not in claims: errors.append(f"review text unknown claim {c}")
        for a in re.findall(r"ASM-\d{3}", text):
            if a not in asm_ids: errors.append(f"review text unknown assumption {a}")
    for c in r["claim_ids"]:
        if c not in claims: errors.append(f"{r['bet_id']} {r['council']}: unknown claim {c}")
if len(reviews) != 17 * 7: errors.append(f"expected 119 reviews, have {len(reviews)}")
for b in bet_ids:
    for c in COUNCILS:
        if not any(r["bet_id"] == b and r["council"] == c for r in reviews): errors.append(f"missing {b} {c}")
for b, v in RED.items():
    for c in v[2].split():
        if c not in claims: errors.append(f"red {b}: unknown claim {c}")
    for blob in (v[0], v[1], " ".join(v[3]), " ".join(v[4])):
        for c in re.findall(r"CLM-\d{6}", blob):
            if c not in claims: errors.append(f"red {b}: unknown claim in text {c}")
        for a in re.findall(r"ASM-\d{3}", blob):
            if a not in asm_ids: errors.append(f"red {b}: unknown assumption {a}")
for b, t in DISAGREEMENTS:
    if b not in bet_ids: errors.append(f"disagreement bad bet {b}")
    for c in re.findall(r"CLM-\d{6}", t):
        if c not in claims: errors.append(f"disagreement unknown claim {c}")

# ------------------------------------------------------------------ council_reviews.md
SYM = {"support": "S", "conditional": "C", "oppose": "O"}
L = []
L.append("# Strategic Council review of the 17 bets (A11e, wave 5)\n")
L.append("Research cutoff 2026-11-21. Independent challenge by a fresh-context agent. Claim IDs were re-checked against `claims_registry.jsonl`, including `correction`, `contrary_evidence` and status fields. Takeda fiscal years run April-March (FY2025 = April 2025 to March 2026). Bet decisions are those in `strategy/data/strategy_bets.json`; this file does not change them.\n")
L.append("**How to read the verdicts.** A verdict is the council's stance on the *proposed decision as recorded* (BUILD, INVEST, PARTNER, EXPERIMENT, DEFER or REJECT). `support` backs the decision as written. `conditional` backs it only if the stated condition is met. `oppose` disputes the decision or its sizing. For REJECT and DEFER bets, `support` means the council endorses the REJECT or DEFER, and the rationale begins 'Endorses'. Councils were run independently and their disagreements are recorded in the log below, not averaged away. Dollar figures are the strategy's ASSUMPTIONs (ASM-002 to ASM-004, ASM-101 to ASM-117); Takeda's budget is not public (IVB-014).\n")
L.append("**Claim-quality findings that apply to every council** (re-checked against the registry):\n")
L.append("- Of 215 distinct claim IDs cited by the 17 bets, 134 are SUPPORTED, 57 PARTIALLY_SUPPORTED, 17 NEEDS_MORE_RESEARCH and 7 INCONCLUSIVE. The NEEDS_MORE_RESEARCH claims are mostly the registry's own HYPOTHESIS entries for the AI, plasma, orexin, registry and launch-pathway bets (CLM-011027 to CLM-011081), so those bets cite hypotheses as evidence.")
L.append("- Six bets (BET-04, 05, 08, 09, 11, 16) are labelled `evidence_backed` although a load-bearing claim is PARTIALLY_SUPPORTED or NEEDS_MORE_RESEARCH (for example CLM-007053 for BET-11, CLM-011065 and CLM-011066 for BET-09, CLM-011054 for BET-08).")
L.append("- Known errors that remain in the strategy text: 'CVS removed Zepbound for about 11 months [CLM-007011]' (the claim records an 11% share-price fall; CVS restored Zepbound from 1 October 2026 per CLM-007013, about 15 months); stage-gate capital at risk exceeds the bet size by USD 5m for BET-02, 07, 09 and 11; BET-13 is DEFER but funded USD 80m in the balanced envelope.")
L.append("- Corrections honoured: JPY 58.2bn cell-therapy impairment, restructuring series 150, 170.0 and 160.0bn, Morphic basis, OTTAVA announced not completed, J&J AI metrics self-reported.\n")

L.append("## Verdict matrix (bet by council)\n")
hdr = "| Bet | Decision | " + " | ".join(c.replace("_", " ") for c in COUNCILS) + " | S/C/O |"
L.append(hdr)
L.append("|" + "---|" * (len(COUNCILS) + 3))
for b in sorted(R):
    cnt = Counter(R[b][c][0] for c in COUNCILS)
    L.append(f"| {b} {BET_NAMES[b]} | {DECISIONS[b]} | " + " | ".join(SYM[R[b][c][0]] for c in COUNCILS) + f" | {cnt['support']}/{cnt['conditional']}/{cnt['oppose']} |")
tot = Counter(r["verdict"] for r in reviews)
L.append(f"\nTotals over 119 reviews: support {tot['support']}, conditional {tot['conditional']}, oppose {tot['oppose']}. S = support, C = conditional, O = oppose.\n")

for c in COUNCILS:
    L.append(f"## {COUNCIL_TITLES[c]}\n")
    L.append(f"*Question:* {COUNCIL_QUESTIONS[c]}\n")
    L.append("| Bet | Verdict | Rationale | Unresolved | Claims |")
    L.append("|---|---|---|---|---|")
    for b in sorted(R):
        v, rat, unres, cl = R[b][c]
        L.append(f"| {b} {BET_NAMES[b]} ({DECISIONS[b]}) | **{v}** | {rat} | {unres} | {' '.join('['+x+']' for x in cl.split())} |")
    L.append("")

L.append("## Disagreements log (not harmonised)\n")
for b, t in DISAGREEMENTS:
    L.append(f"- **{b}.** {t}")
L.append("")

L.append("## Unresolved assumptions that most limit these verdicts\n")
L.append("| Assumption or gap | What it limits | Councils affected | Resolves with |")
L.append("|---|---|---|---|")
rows = [
 ("ASM-024 and ASM-025: Entyvio erosion and entry year (2031, range 2030-2032)", "BET-04, 05, 06, 11, 15 and every timing argument; entry in 2027-2029 is outside the range", "capital, commercial, red team", "IVB-004; Purple Book and litigation record"),
 ("ASM-033 and ASM-034: leverage ceiling and Amitiza cash (provision JPY 403.5bn, TPP class and appeal open)", "BET-15 feasibility, the constrained-versus-balanced choice, SCN-5", "capital, execution", "IVB-012"),
 ("ASM-020 to ASM-022 and ASM-028: probabilities are judgment", "The capital ranking of BET-03, 05, 06, 07", "capital, scientific", "IVB-005, IVB-008"),
 ("IVB-001: production inventory of AI and data products", "BET-01 scale, BET-07 and BET-08 value, BET-17 baselines", "technology, scientific, execution", "Takeda internal inventory"),
 ("IVB-006 and ASM-031: plasma headroom and economic value of a 2% gain", "BET-02 follow-on of USD 350m", "capital, scientific, red team", "Takeda internal yield and cost data; plasma-peer benchmark"),
 ("Entyvio benefit-channel mix (medical versus pharmacy)", "BET-04 lever and BET-11 interaction", "red team, commercial", "IVB-004"),
 ("Orexin competitor pipeline", "BET-03 head-start and sizing", "red team, scientific", "Outside-registry competitor scan"),
 ("Nabla first-in-human timing and contract terms", "BET-07 gating, BET-10 triggers", "scientific, technology, red team", "Company data (expected 2026-2028)"),
 ("Takeda Ventures and CEI scope (IVB-007)", "BET-06 execution capacity", "execution", "Takeda internal"),
 ("IVB-014: approved technology envelope", "All sizing", "capital", "Takeda internal"),
]
for r in rows: L.append("| " + " | ".join(r) + " |")
L.append("")
open(f"{HERE}/council_reviews.md", "w").write("\n".join(L))

# ------------------------------------------------------------------ red_team.md
T = []
T.append("# Red team: the strongest case against each bet (A11e, wave 5)\n")
T.append("Research cutoff 2026-11-21. Each entry gives the strongest argument against the bet as recorded, the evidence (registry claims re-checked, with corrections), what would have to be true for the bet to survive, and kill criteria with a date or gate where one exists. 'Exposure' rates how much of the bet's case depends on the attacked premise: HIGH means the premise is load-bearing and unproven; MEDIUM means it is contestable but the bet survives with a changed framing; LOW means little is lost if the attack is right. Entries for REJECT and DEFER bets attack the *rejection*. Kill criteria that cite the stage-gate file reuse its stop tests; criteria marked 'council' are proposed here and are not in the stage gates.\n")
T.append("## Exposure summary\n")
T.append("| Bet | Decision | Exposure |")
T.append("|---|---|---|")
for b in sorted(RED):
    T.append(f"| {b} {BET_NAMES[b]} | {DECISIONS[b]} | {RED[b][5]} |")
T.append("")
for b in sorted(RED):
    sc, ev, cl, mbt, kill, rating = RED[b]
    T.append(f"## {b} {BET_NAMES[b]} ({DECISIONS[b]}; exposure {rating})\n")
    T.append(f"**Strongest case against.** {sc}\n")
    T.append(f"**Evidence.** {ev} {' '.join('['+x+']' for x in cl.split())}\n")
    T.append("**What would have to be true for the bet to survive.**")
    for x in mbt: T.append(f"- {x}")
    T.append("\n**Kill criteria.**")
    for x in kill: T.append(f"- {x}")
    T.append("")
open(f"{HERE}/red_team.md", "w").write("\n".join(T))

# ------------------------------------------------------------------ counterarguments_and_uncertainty.md
TYPES = [
 ("unsupported_assumption", "Unsupported assumptions"),
 ("unresolved_question", "Unresolved questions"),
 ("conflicting_sources", "Conflicting sources"),
 ("public_knowledge_gap", "Public-knowledge gaps (internal-validation backlog and outside-registry gaps)"),
 ("failed_hypothesis", "Failed strategic hypotheses (competitor and Takeda failures that warn against a bet)"),
 ("alternative_interpretation", "Alternative interpretations"),
 ("caveat", "Caveats behind the recommendations"),
]
M = []
M.append("# Counterarguments and uncertainty (View 12 content, A11e wave 5)\n")
M.append("Research cutoff 2026-11-21. Every item has an id (CA-nnn) matching `strategy/data/counterarguments.json`. Targets are a bet (BET-nn), a single registry claim (CLM-nnnnnn) or THEME for portfolio-wide points. Conflicts come from `conflicts_proposed_A10.jsonl`, `conflicts_proposed_A10b.jsonl` and the registry's `correction` and `contrary_evidence` fields. Items marked 'council arithmetic' are calculations made here from registry values and ASM-001; they are not Takeda disclosures.\n")
cnt = Counter(i["type"] for i in items)
M.append("| Type | Items |\n|---|---|")
for t, title in TYPES: M.append(f"| {title} | {cnt[t]} |")
M.append(f"| Total | {len(items)} |\n")
for t, title in TYPES:
    M.append(f"## {title}\n")
    for it in items:
        if it["type"] == t:
            refs = " ".join("[" + c + "]" for c in it["claim_ids"])
            asm = (" (" + ", ".join(it["assumption_ids"]) + ")") if it["assumption_ids"] else ""
            M.append(f"- **{it['id']} ({it['target']}).** {it['text']} {refs}{asm}")
    M.append("")
open(f"{HERE}/counterarguments_and_uncertainty.md", "w").write("\n".join(M))

print("reviews", len(reviews), "disagreements", len(dis), "counter items", len(items), dict(cnt))
print("verdict totals", dict(tot))
print("errors", len(errors))
for e in errors: print("  ERROR", e)
sys.exit(1 if errors else 0)
