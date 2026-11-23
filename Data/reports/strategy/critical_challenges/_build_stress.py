#!/usr/bin/env python3
"""Generate scenario_stress_test.md from scenarios.json (strategy ratings) and the council's re-rated table."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _data_reviews import BET_NAMES, DECISIONS

scn = json.load(open(f"{ROOT}/data/scenarios.json"))
bets = {b["id"]: b for b in json.load(open(f"{ROOT}/data/strategy_bets.json"))["bets"]}
S = {s["id"]: s for s in scn["scenarios"]}
strategy = {r["bet_id"]: r for r in scn["robustness"]}
SC = ["SCN-1", "SCN-2", "SCN-3", "SCN-4", "SCN-5"]

# Council re-rating: only cells where the council disagrees are listed: (bet, scn) -> (rating, reason)
CH = {
 ("BET-01", "SCN-5"): ("fragile", "First discretionary cut in a cash squeeze; only the thin slice (metadata standard, decision log) is worth protecting."),
 ("BET-02", "SCN-3"): ("neutral", "Immunoglobulin exposure to MFN and negotiation was not researched, and PDT revenue was -1.5% at constant rates in H1 FY2026, so lower prices do not make the cost case stronger by themselves [CLM-005064]."),
 ("BET-02", "SCN-5"): ("neutral", "The baseline and shadow-mode tranche survives; the USD 350m roll-out is the first large item to be deferred when leverage binds."),
 ("BET-03", "SCN-3"): ("neutral", "Payoff is 2035-2038, after the Entyvio erosion window; it does not cushion SCN-3 and competes for the same cash."),
 ("BET-04", "SCN-3"): ("neutral", "Needed in every scenario, but the Medicare price from January 2028 is statutory and PBM private-label biosimilars route around contracts [CLM-007026] [CLM-007015]. Value holds only as delay."),
 ("BET-05", "SCN-5"): ("fragile", "SCN-5 contains launch slippage; PsA binary readout and inspection risk sit directly on this bet [CLM-005037] [CLM-012134]."),
 ("BET-06", "SCN-2"): ("neutral", "Option value does not depend on AI pace; 'robust' overstates it when no option has produced an approval [CLM-009097]."),
 ("BET-06", "SCN-3"): ("neutral", "The loss is capped, but options pay after 2035 and do not defend Entyvio net price in 2028-2034; 'robust' should mean value holds, not that the loss is small."),
 ("BET-06", "SCN-5"): ("fragile", "Upfronts and option fees are cash (ASM-106 excludes only contingent milestones); the constrained portfolio still allocates USD 300m (19%) here, and it is the first line to cut."),
 ("BET-07", "SCN-1"): ("option_value", "If AI accelerates, models commoditise (the SCN-1 driver) and value accrues to partners and to owners of proprietary data, not to licensees [CLM-006056]."),
 ("BET-09", "SCN-3"): ("neutral", "A rented-assay service is irrelevant to price pressure; its value is cost avoidance against an unknown baseline (IVB-002)."),
 ("BET-11", "SCN-3"): ("fragile", "SC pens move patients into the pharmacy benefit where PBM biosimilar templates operate [CLM-007015] [CLM-007016]; the effect after entry is unestablished [CLM-007053]."),
 ("BET-11", "SCN-5"): ("neutral", "Device capex is deferrable; the existing pen and HYHUB stay."),
 ("BET-12", "SCN-2"): ("neutral", "The pathway hypothesis has no outcome evidence in any scenario [CLM-007039]; 'robust' should be reserved for bets with evidence of value."),
 ("BET-12", "SCN-3"): ("neutral", "As above; compliance exposure rises under pricing pressure [CLM-007010]."),
 ("BET-12", "SCN-4"): ("option_value", "Care-model change could make pathway data valuable; no evidence yet [CLM-007045]."),
 ("BET-13", "SCN-4"): ("option_value", "Unproven; Flatiron's neutrality does not transfer [CLM-011050]."),
 ("BET-15", "SCN-2"): ("neutral", "Need for a bridge does not depend on AI pace."),
 ("BET-15", "SCN-3"): ("fragile", "Under pricing pressure free cash flow falls while leverage already fails the 3.0x test by council arithmetic [CLM-005005] [CLM-005014]."),
}
council = {b: {s: strategy[b][s] for s in SC} for b in strategy}
for (b, s), (r, _) in CH.items():
    council[b][s] = r

def bal(b):
    x = bets[b]["investment_usd_m"]["balanced"]
    return x["initial"] + x["follow_on"] + x["scaled"]
def h1(b):
    return bets[b]["investment_usd_m"]["balanced"]["initial"]

L = []
L.append("# Scenario stress test (A11e, wave 5)\n")
L.append("Research cutoff 2026-11-21. The five scenarios are those in `strategy/data/scenarios.json` (SCN-1 to SCN-5). They are SCENARIOs, not forecasts. The strategy's robustness table is reproduced and re-rated by the council. Where the council differs the cell is marked and the reason is given. Capital figures are the strategy's balanced-portfolio ASSUMPTIONs (cumulative 2027-2040, USD m); Takeda's budget is not public (IVB-014). Council arithmetic is derived from registry values and ASM-001 (JPY 150 per USD).\n")
L.append("## 1. Scenario recap and what each stresses\n")
for sid in SC:
    s = S[sid]
    L.append(f"- **{sid} {s['name']}.** {s['description'][:260].rstrip()}{'...' if len(s['description'])>260 else ''}")
L.append("")
L.append("## 2. Re-rated robustness table (council view; strategy rating in brackets where different)\n")
L.append("| Bet | Decision | Balanced USD m | " + " | ".join(SC) + " |")
L.append("|---|---|---|" + "---|" * len(SC))
changed = 0
for b in sorted(bets):
    cells = []
    for s in SC:
        c, st = council[b][s], strategy[b][s]
        if c != st:
            cells.append(f"**{c}** [{st}]"); changed += 1
        else:
            cells.append(c)
    L.append(f"| {b} {BET_NAMES[b]} | {DECISIONS[b]} | {bal(b)} | " + " | ".join(cells) + " |")
L.append(f"\nThe council re-rated {changed} of 85 cells ({changed/85:.0%}). Reasons:\n")
for (b, s), (r, why) in sorted(CH.items()):
    L.append(f"- **{b} in {s}: {strategy[b][s]} to {r}.** {why}")
L.append("")

L.append("## 3. Which bets break in each scenario\n")
L.append("'Breaks' means rated fragile by the council: value falls or spend is stranded. Stranded capital is the sum of the balanced totals of those bets (a ceiling, because gates would stop spend before the full total is committed).\n")
L.append("| Scenario | Bets that break (council) | Stranded balanced USD m | Share of USD 2,950m | Robust bets (council) | Robust balanced USD m |")
L.append("|---|---|---|---|---|---|")
tot = 2950
for s in SC:
    fr = [b for b in sorted(bets) if council[b][s] == "fragile"]
    ro = [b for b in sorted(bets) if council[b][s] == "robust"]
    fr_cap = sum(bal(b) for b in fr); ro_cap = sum(bal(b) for b in ro)
    L.append(f"| {s} | {', '.join(fr) or 'none'} | {fr_cap} | {fr_cap/tot:.0%} | {', '.join(ro)} | {ro_cap} |")
L.append("")
L.append("Reading *(council interpretation)*:\n")
L.append("- **SCN-1 (AI accelerates).** Nothing funded breaks. The risk is the opposite: BET-07 and BET-08 look like winners but the model commoditisation driver means Takeda gains only where it owns proprietary data (BET-01, BET-09). The bets that would pay (BET-07 at USD 180m) are option-sized, so the portfolio under-invests relative to an SCN-1 world by design, and the ambitious portfolio (USD 4,975m) is the only one that scales on it. Trigger: Nabla first-in-human and an independent Lilly-lab result [CLM-006039] [CLM-000281].")
L.append("- **SCN-2 (AI incremental).** BET-07 breaks (USD 180m, small) and BET-10 and BET-14 would break if funded. BET-01, BET-08, BET-09 and BET-17 survive as productivity and discipline spend. Note the SCN-2 world is the one the registry currently supports: no independent outcome exists for any AI platform [CLM-011052], and AI-origin Phase 2 success is cited as conventional [CLM-006049]. Treat SCN-2 as the base case for AI spending.")
n_strat_robust = sum(1 for b in strategy if strategy[b]["SCN-3"] == "robust")
n_council_robust = sum(1 for b in council if council[b]["SCN-3"] == "robust")
L.append(f"- **SCN-3 (pricing, regulatory and biosimilar pressure).** The most consequential scenario for the portfolio and the one the strategy treats most generously: it rates {n_strat_robust} bets robust, the council rates {n_council_robust}. BET-11 breaks (pharmacy-benefit channel), BET-15 breaks (leverage), and BET-04 is needed but insufficient because the January 2028 Medicare price is statutory. The exposure the portfolio is built to cover (JPY 383-766bn a year of Entyvio revenue at ASM-024) is addressed by no bet except through delay, so SCN-3 is where the strategy's gap is largest.")
L.append("- **SCN-4 (new modalities, care models, tech-native entrants).** Few bets break because few depend on it. BET-07 holds option value, but tech-native entrants (Isomorphic reportedly raised USD 600m [CLM-011014]) win partnerships that Takeda's USD 180m cannot match; BET-06 is the only bet that buys modality exposure and its payoff comes after 2035.")
L.append("- **SCN-5 (combined downside).** BET-01, BET-03, BET-05, BET-06 and BET-13 break (BET-15 by arithmetic). See section 4.\n")

L.append("## 4. Combined downside (SCN-5) in numbers\n")
L.append("SCN-5 combines AI incremental, pricing pressure, launch slippage and Amitiza cash near the full provision, with leverage near 3x and discretionary spend cut [CLM-005014] [CLM-005005].\n")
cap = {"BET-01": 120, "BET-02": 230, "BET-03": 300, "BET-04": 120, "BET-05": 130, "BET-06": 300, "BET-07": 80, "BET-08": 25, "BET-09": 50, "BET-11": 120, "BET-12": 50, "BET-17": 65}
L.append("Capital-constrained portfolio (USD 1,590m), council re-rating of SCN-5:\n")
L.append("| Council SCN-5 rating | Bets | Constrained USD m | Share of USD 1,590m |")
L.append("|---|---|---|---|")
for rt in ("robust", "neutral", "fragile", "option_value"):
    bs = [b for b in sorted(cap) if council[b]["SCN-5"] == rt]
    v = sum(cap[b] for b in bs)
    L.append(f"| {rt} | {', '.join(bs) or 'none'} | {v} | {v/1590:.0%} |")
frag_cap = sum(cap[b] for b in cap if council[b]["SCN-5"] == "fragile")
L.append(f"\n**Finding.** After the council's re-rating, {frag_cap} of the USD 1,590m constrained envelope ({frag_cap/1590:.0%}) sits in bets that break in the combined downside, against a strategy table in which only BET-03 was fragile (USD 300m, 19%). The strategy's statement that the constrained portfolio protects the dated defences holds (BET-04 USD 120m and BET-05 USD 130m are 16% of it); the remaining 84% is mostly long-dated or option spend.\n")
L.append("**Leverage arithmetic behind SCN-5** *(council arithmetic from registry values; free cash flow and acquired earnings ignored)*:\n")
L.append("| Case | Adjusted net debt JPY bn | Over EBITDA JPY 1,457.2bn |")
L.append("|---|---|---|")
for nm, nd in (("March 2026 as reported [CLM-005005]", 3817.6), ("Amitiza provision JPY 403.5bn debt-funded [CLM-005014]", 3817.6 + 403.5), ("USD 5bn purchase at JPY 150 (BET-15) only", 3817.6 + 750), ("Both", 3817.6 + 403.5 + 750)):
    L.append(f"| {nm} | {nd:,.1f} | {nd/1457.2:.2f}x |")
L.append("\nAdjusted net debt may already include the provision, and free cash flow after the JPY 313.2bn dividend paid in FY2025 [CLM-005006] would reduce it; both are unknown (IVB-012, IVB-014). The Amitiza figure is also not an upper bound: JPY 403.5bn is about three times the USD 884.9m single damages at JPY 152 per USD, and the third-party-payor class, interest, fees and appeal outcome are open [CLM-014048].\n")

L.append("## 5. Stress cases the strategy does not model (council-added, not in scenarios.json)\n")
L.append("**S-A. Early Entyvio biosimilar entry (2028-2029) with an Amitiza outcome at or above the provision.** ASM-025 (2031, range 2030-2032) excludes this. Basis: two biosimilar BLAs are under FDA review with one decision expected Q1 2027 per trade reporting, the reference product was approved in 2014, and Takeda says earlier launches must address patent validity and infringement [CLM-014051] [CLM-014050] [CLM-005017]. Which bets break:\n")
L.append("| Bet | Effect under S-A |")
L.append("|---|---|")
sa = [
 ("BET-04", "Playbook RM-026 (2029 H2) is dated after the earliest assumed entry (2030). It would be late. Re-date to 2028 H1 at no extra capital."),
 ("BET-05", "Becomes the only replacement in time; PsA readout (May 2027) and launch coverage carry more weight than their USD 180m suggests."),
 ("BET-03", "Payoff 2035-2038 misses the window entirely."),
 ("BET-06", "First approval 2035 (RM-043) misses the window; capital competes with the bridge."),
 ("BET-11", "SC migration before entry would increase pharmacy-benefit exposure at the worst moment."),
 ("BET-15", "A bridge purchase is needed sooner and is infeasible at 3.13x to 3.41x. This is where DEFER becomes a decision to leave a gap."),
]
for b, t in sa: L.append(f"| {b} | {t} |")
L.append("")
L.append("**S-B. AI-design success with no data advantage (SCN-1 in which Takeda is a licensee).** Partners and AI-native biotechs capture the value (SCN-1 driver: commodity models). BET-07 pays only success-based milestones, which are contingent liabilities above USD 1bn per deal [CLM-006039] [CLM-006041]. Takeda's gain depends on BET-01 and BET-09, which are small. The portfolio is not harmed but does not benefit.\n")
L.append("**S-C. Launch-wave concentration.** Three launches within 12 months [CLM-005074] with US revenue already falling 9.0% at actual rates in FY2025 [CLM-005001]. BET-04, BET-11 and BET-12 sit in the same US organisation (stage-gate owners). A launch problem in that organisation breaks three bets together, which the scenario table treats as independent.\n")

L.append("## 6. Robust core (least-regret set)\n")
L.append("The core is the least-regret set: bets the council would keep funded in every scenario and in S-A, either because value holds or because the bet addresses a dated or event-driven exposure at a capped cost. BET-03 and BET-05 are rated fragile in SCN-5 yet stay in the core as floors: BET-05 is the only replacement-revenue bet acting inside the Entyvio window and BET-03 is the only in-house diversification, so their fragility is the risk being managed, not a reason to cut. Council view, balanced H1 2027-2029 tranche (strategy's initial figures, ASSUMPTION):\n")
core = [
 ("BET-04", "Fixed dates, cheapest against exposure; re-date the playbook to 2028.", h1("BET-04")),
 ("BET-05", "Existing asset; the evidence is the best in the set.", h1("BET-05")),
 ("BET-11", "Existing capability; hold device capex to a baseline-first tranche (condition: resolve the PBM-channel conflict with BET-04).", h1("BET-11")),
 ("BET-17", "Cheap discipline that makes the AI claims testable; move measurement ownership away from the savings owner.", h1("BET-17")),
 ("BET-01", "Thin slice only (metadata standard and decision log) until gate 3.", h1("BET-01")),
 ("BET-09", "Rented, reversible; stage 1-2 only.", h1("BET-09")),
 ("BET-08", "Near-free and measurable.", h1("BET-08")),
 ("BET-02", "Baseline and shadow-mode tranche only (not the roll-out).", h1("BET-02")),
 ("BET-03", "Floor of discovery spend with a Phase 1 safety gate before H2 (constrained size).", h1("BET-03")),
]
L.append("| Bet | Core content | H1 USD m |")
L.append("|---|---|---|")
core_sum = 0
for b, t, v in core:
    L.append(f"| {b} {BET_NAMES[b]} | {t} | {v} |"); core_sum += v
gated = [("BET-06", h1("BET-06")), ("BET-07", h1("BET-07")), ("BET-12", h1("BET-12")), ("BET-13", h1("BET-13"))]
L.append(f"| **Core total** | | **{core_sum}** |")
h1_all = sum(h1(b) for b in bets)
L.append(f"\nThe balanced H1 tranche is USD {h1_all}m. The core is USD {core_sum}m ({core_sum/h1_all:.0%}). The remaining USD {h1_all-core_sum}m (BET-06 {h1('BET-06')}, BET-07 {h1('BET-07')}, BET-12 {h1('BET-12')}) should be released only on triggers: a deal-outcome scorecard (RM-007) for BET-06, Nabla first-in-human data for BET-07 beyond existing commitments, and an identified pathway bottleneck for BET-12.\n")
L.append("**What the core does not do.** It does not replace Entyvio revenue. It protects what is dated and measurable, keeps learning cheap and holds options open. The Entyvio gap is covered only by the existing pipeline, BET-05 breadth and, if built, a mid-size licensing channel that no bet funds (see decision memo).\n")
L.append("## 7. Capital timing against the Entyvio window\n")
late = [("BET-03", bal("BET-03")), ("BET-06", bal("BET-06")), ("BET-07", bal("BET-07")), ("BET-13", bal("BET-13"))]
ls = sum(v for _, v in late)
L.append(f"Bets the strategy's own evaluation puts at eight or more years to payoff are BET-03 (10), BET-06 (10), BET-07 (8) and BET-13 (8). Their balanced totals are USD {ls}m, {ls/tot:.1%} of USD 2,950m. Their payoff years (2035-2038) fall after the Entyvio erosion window that ASM-025 places at 2031-2034. The bets that act inside the window (BET-04, BET-05, BET-11) total USD {bal('BET-04')+bal('BET-05')+bal('BET-11')}m, {(bal('BET-04')+bal('BET-05')+bal('BET-11'))/tot:.0%} of the balanced envelope.\n")
L.append("## 8. Method limits\n")
L.append("- Ratings are interpretation. Takeda internal data (IVB-004, IVB-005, IVB-006, IVB-012) could change them.\n- Stranded-capital sums are ceilings. Stage gates cap capital at risk per gate (ASM-037 convention).\n- Scenario 'robust' in the strategy table means value holds or rises; the council applied the same definition and withheld 'robust' where the bet's value rests on a hypothesis with no outcome evidence.")
open(f"{HERE}/scenario_stress_test.md", "w").write("\n".join(L) + "\n")

# validate ids
reg = {json.loads(l)["claim_id"] for l in open(os.path.join(os.path.dirname(ROOT), "New_mediciine", "evidence_library", "claims_registry.jsonl")) if l.strip()}
txt = "\n".join(L)
bad = [c for c in set(re.findall(r"CLM-\d{6}", txt)) if c not in reg]
print("changed cells", changed, "core", core_sum, "h1_all", h1_all, "late", ls, "frag_cap", frag_cap, "bad ids", bad)
