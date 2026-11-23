#!/usr/bin/env python3
"""
EDGAR XBRL companyfacts extractor (A4 Financial Intelligence; deterministic, no LLM).

Pulls audited annual facts from https://data.sec.gov/api/xbrl/companyfacts/ for
Eli Lilly (CIK 59478), Johnson & Johnson (CIK 200406), AbbVie (CIK 1551152) and
Takeda (CIK 1395064, 20-F / IFRS).

Writes
  data/normalized/financials_annual.json           normalized per-company per-FY table
  New_mediciine/financial_models/edgar_facts_<co>.json   raw selected facts w/ accession
  New_mediciine/evidence_library/shards/A4_financial/{sources,claims}.jsonl
  New_mediciine/companies/<co>/financials/edgar_annual_facts.md  human-readable table

Every value carries: fiscal year (fy), period end, form (10-K/20-F), accession number
(accn) and the XBRL tag it came from. Values are USD (JPY for Takeda) as filed.
Partial-year (10-Q) values are deliberately excluded; FY2026 is NOT a full year.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from evidence import append_jsonl, now_iso, read_jsonl  # noqa: E402

UA = "MEDICINE-research-project palrahma@amazon.com"
COMPANIES = {
    "eli_lilly": {"cik": "0000059478", "name": "Eli Lilly and Company", "form": "10-K", "ns": "us-gaap", "ccy": "USD"},
    "johnson_johnson": {"cik": "0000200406", "name": "Johnson & Johnson", "form": "10-K", "ns": "us-gaap", "ccy": "USD"},
    "abbvie": {"cik": "0001551152", "name": "AbbVie Inc.", "form": "10-K", "ns": "us-gaap", "ccy": "USD"},
    "takeda": {"cik": "0001395064", "name": "Takeda Pharmaceutical Company Limited", "form": "20-F", "ns": "ifrs-full", "ccy": "JPY"},
}
# metric -> candidate tags in priority order (first tag with FY data wins, per year)
METRICS_GAAP = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "cost_of_sales": ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"],
    "rd_expense": ["ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost", "ResearchAndDevelopmentExpense"],
    "ipr_d_acquired": ["ResearchAndDevelopmentAssetAcquiredOtherThanThroughBusinessCombinationWrittenOff", "ResearchAndDevelopmentInProcess"],
    "pretax_income": ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "iprd_payments_cash": ["PaymentsToAcquireInProcessResearchAndDevelopment"],
    "sga_expense": ["SellingGeneralAndAdministrativeExpense", "SellingAndMarketingExpense"],
    "operating_income": ["OperatingIncomeLoss"],
    "net_income": ["NetIncomeLoss", "ProfitLoss"],
    "operating_cash_flow": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireOtherPropertyPlantAndEquipment"],
    "acquisitions_cash": ["PaymentsToAcquireBusinessesNetOfCashAcquired", "OtherPaymentsToAcquireBusinesses"],
    "dividends_paid": ["PaymentsOfDividends", "PaymentsOfDividendsCommonStock", "PaymentsOfOrdinaryDividends", "PaymentsOfDividendsCommonStockAndPreferredStock", "DividendsCommonStockCash"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
    "long_term_debt": ["LongTermDebtNoncurrent", "LongTermDebt"],
    "total_assets": ["Assets"],
    "cash": ["CashAndCashEquivalentsAtCarryingValue"],
    "goodwill": ["Goodwill"],
    "intangibles": ["IntangibleAssetsNetExcludingGoodwill"],
    "shares_diluted": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
    "eps_diluted": ["EarningsPerShareDiluted"],
    "income_tax": ["IncomeTaxExpenseBenefit"],
}
METRICS_IFRS = {
    "revenue": ["Revenue"],
    "cost_of_sales": ["CostOfSales"],
    "rd_expense": ["ResearchAndDevelopmentExpense"],
    "sga_expense": ["SellingGeneralAndAdministrativeExpense"],
    "operating_income": ["ProfitLossFromOperatingActivities"],
    "net_income": ["ProfitLoss", "ProfitLossAttributableToOwnersOfParent"],
    "operating_cash_flow": ["CashFlowsFromUsedInOperatingActivities"],
    "capex": ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
    "dividends_paid": ["DividendsPaidClassifiedAsFinancingActivities"],
    "long_term_debt": ["NoncurrentPortionOfNoncurrentBorrowings", "NoncurrentBorrowings", "Borrowings"],
    "total_assets": ["Assets"],
    "cash": ["CashAndCashEquivalents"],
    "goodwill": ["Goodwill"],
    "intangibles": ["IntangibleAssetsOtherThanGoodwill"],
    "eps_diluted": ["DilutedEarningsLossPerShare"],
    "income_tax": ["IncomeTaxExpenseContinuingOperations"],
}
FY_MIN, FY_MAX = 2019, 2025  # lookback 2 yrs before window for growth baselines; 2026 not a full year


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            import gzip
            data = gzip.decompress(data)
    return json.loads(data)


def pick_annual(facts: dict, ns: str, tags: list[str], form: str, ccy: str) -> dict[int, dict]:
    """Return {fy: {val, end, accn, tag, fy, fp, filed}} choosing, per FY, the value from the
    filing for that FY (most recently filed duplicate wins = restated figure, flagged)."""
    out: dict[int, dict] = {}
    for tag in tags:
        node = facts.get(ns, {}).get(tag)
        if not node:
            continue
        claimed_years = {fy for fy, r in out.items()}  # years already filled by a higher-priority tag
        units = node.get("units", {})
        series = units.get(ccy) or units.get(f"{ccy}/shares") or units.get("shares") or []
        for x in series:
            if x.get("form") != form or x.get("fp") != "FY":
                continue
            # duration facts have start+end ~ 1 year; instant facts have only end
            start, end = x.get("start"), x.get("end")
            if start and end:
                d0 = int(start[:4]) * 12 + int(start[5:7]); d1 = int(end[:4]) * 12 + int(end[5:7])
                if not (10 <= d1 - d0 <= 14):
                    continue  # skip quarterly/cumulative oddities
            fy_end_year = int(end[:4]) if end else x.get("fy")
            # Fiscal-year labelling: use the period END year (J&J FY ends late Dec/early Jan)
            fy = fy_end_year if (end and int(end[5:7]) >= 6) else fy_end_year - 1 if end else x.get("fy")
            if fy is None or fy < FY_MIN or fy > FY_MAX:
                continue
            rec = {"val": x["val"], "end": end, "start": start, "accn": x.get("accn"), "tag": tag,
                   "fy_label": x.get("fy"), "filed": x.get("filed"), "form": form}
            if fy in claimed_years:
                continue  # higher-priority tag already supplies this year
            prev = out.get(fy)
            # Prefer the ORIGINAL filing for that FY (first filed) but record restatement if later differs
            if prev is None or (prev["tag"] == tag and rec["filed"] < prev["filed"]):
                if prev and prev["val"] != rec["val"]:
                    rec["restated_later_to"] = prev["val"]
                    rec["restated_in_accn"] = prev["accn"]
                out[fy] = rec
            elif prev["tag"] == tag and rec["filed"] > prev["filed"] and rec["val"] != prev["val"]:
                prev.setdefault("restated_later_to", rec["val"]); prev.setdefault("restated_in_accn", rec["accn"])
    return out


def main():
    shard = ROOT / "New_mediciine" / "evidence_library" / "shards" / "A4_financial"
    shard.mkdir(parents=True, exist_ok=True)
    src_path, clm_path = shard / "sources.jsonl", shard / "claims.jsonl"
    have_src = {r["source_id"] for r in read_jsonl(src_path)}
    have_clm = {r["claim_id"] for r in read_jsonl(clm_path)}
    sid = 4000
    cid = 4000
    normalized: dict = {"generated": now_iso(), "note": "Audited annual facts from SEC XBRL companyfacts API. "
                        "FY = fiscal year of period end. Values as filed (USD; JPY for Takeda). 2026 excluded: not a full year.",
                        "companies": {}}
    accn_sources: dict[str, str] = {}  # accn -> source_id

    for co, meta in COMPANIES.items():
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{meta['cik']}.json"
        print(f"fetching {co} ...", file=sys.stderr)
        try:
            data = get(url)
        except Exception as ex:  # noqa: BLE001
            print(f"  FAILED {co}: {ex}", file=sys.stderr)
            normalized["companies"][co] = {"error": str(ex)[:200]}
            continue
        time.sleep(0.4)
        facts = data["facts"]
        metrics = METRICS_IFRS if meta["ns"] == "ifrs-full" else METRICS_GAAP
        table: dict[int, dict] = {}
        raw_sel: dict = {}
        for m, tags in metrics.items():
            ccy = "USD/shares" if m == "eps_diluted" and meta["ccy"] == "USD" else (
                "JPY/shares" if m == "eps_diluted" else ("shares" if m == "shares_diluted" else meta["ccy"]))
            series = pick_annual(facts, meta["ns"], tags, meta["form"], ccy)
            raw_sel[m] = series
            for fy, rec in series.items():
                table.setdefault(fy, {})[m] = rec["val"]
                table[fy].setdefault("_provenance", {})[m] = {k: rec[k] for k in ("tag", "accn", "end", "filed") if rec.get(k)}
                if rec.get("restated_later_to") is not None:
                    table[fy]["_provenance"][m]["restated_later_to"] = rec["restated_later_to"]
                if rec.get("accn"):
                    accn_sources.setdefault(rec["accn"], None)
        # derived ratios (INTERPRETATION-free arithmetic)
        for fy, row in table.items():
            rv = row.get("revenue")
            if rv:
                for k in ("rd_expense", "sga_expense", "operating_income", "net_income", "operating_cash_flow", "capex"):
                    if row.get(k) is not None:
                        row[f"{k}_pct_revenue"] = round(100.0 * row[k] / rv, 2)
                if row.get("cost_of_sales") is not None:
                    row["gross_margin_pct"] = round(100.0 * (rv - row["cost_of_sales"]) / rv, 2)
        normalized["companies"][co] = {"entity": data.get("entityName"), "cik": meta["cik"], "form": meta["form"],
                                       "currency": meta["ccy"], "years": {str(k): v for k, v in sorted(table.items())}}
        (ROOT / "New_mediciine" / "financial_models").mkdir(parents=True, exist_ok=True)
        (ROOT / "New_mediciine" / "financial_models" / f"edgar_facts_{co}.json").write_text(
            json.dumps({"entity": data.get("entityName"), "cik": meta["cik"], "selected": raw_sel}, indent=1, default=str), encoding="utf-8")

        # ---- source records: one per accession (each is an actual audited filing)
        for accn in sorted(a for a in accn_sources if accn_sources[a] is None):
            # find which fy/form this accn belongs to
            fy_for = [fy for fy, row in table.items() if any(p.get("accn") == accn for p in row.get("_provenance", {}).values())]
            if not fy_for:
                continue
            sid += 1
            source_id = f"SRC-{sid:06d}"
            accn_nodash = accn.replace("-", "")
            idx_url = f"https://www.sec.gov/Archives/edgar/data/{int(meta['cik'])}/{accn_nodash}/"
            rec = {
                "source_id": source_id, "title": f"{meta['name']} Form {meta['form']} FY{max(fy_for)} (accession {accn})",
                "publisher": "U.S. Securities and Exchange Commission (EDGAR) / registrant", "company": co,
                "domain": "financials", "source_type": "sec_filing", "original_url": idx_url, "canonical_url": idx_url,
                "publication_date": next((p["filed"] for row in table.values() for p in row.get("_provenance", {}).values() if p.get("accn") == accn), "unknown"),
                "reporting_period": f"FY{','.join(str(f) for f in sorted(set(fy_for)))}", "access_date": now_iso()[:10],
                "credibility": "T1_primary_official", "access_status": "api_json",
                "document_identifier": accn, "api_url": url,
                "inspected_passage": f"XBRL companyfacts API facts for accession {accn}; tags: " + ", ".join(sorted({p['tag'] for row in table.values() for p in row.get('_provenance', {}).values() if p.get('accn') == accn}))[:500],
                "notes": "Machine-extracted from SEC XBRL companyfacts. Values as filed; restatements flagged in provenance.",
                "licensing": "US government public record",
            }
            if source_id not in have_src:
                append_jsonl(src_path, rec)
            accn_sources[accn] = source_id
        # ---- claims: one per (fy, headline metric)
        for fy, row in sorted(table.items()):
            if fy < 2021:
                continue
            for m in ("revenue", "rd_expense", "ipr_d_acquired", "pretax_income", "operating_income", "net_income", "operating_cash_flow", "capex", "acquisitions_cash", "iprd_payments_cash", "buybacks", "dividends_paid"):
                if row.get(m) is None:
                    continue
                prov = row["_provenance"][m]
                src_id = accn_sources.get(prov.get("accn"))
                if not src_id:
                    continue
                cid += 1
                val = row[m]
                human = f"{val/1e9:,.3f} bn {meta['ccy']}"
                stmt = f"{meta['name']} reported {m.replace('_', ' ')} of {human} for fiscal year {fy} (period end {prov['end']}; XBRL tag {prov['tag']}; Form {meta['form']} accession {prov['accn']})."
                rec = {
                    "claim_id": f"CLM-{cid:06d}", "statement": stmt, "kind": "FACT", "status": "SUPPORTED",
                    "companies": [co], "domain": "financials", "supporting_source_ids": [src_id],
                    "locator": f"XBRL {prov['tag']} fy={fy} accn={prov['accn']}", "dates": {"period_end": prov["end"], "fiscal_year": fy},
                    "confidence_rationale": "Audited annual figure machine-read from SEC XBRL; no interpretation applied.",
                    "last_verified": now_iso()[:10], "value": val, "unit": meta["ccy"], "metric": m,
                    "contrary_evidence": (f"Restated in a later filing to {row['_provenance'][m]['restated_later_to']}" if row["_provenance"][m].get("restated_later_to") is not None else None),
                    "single_interested_source": False, "tags": ["edgar", "annual", m],
                }
                if rec["claim_id"] not in have_clm:
                    append_jsonl(clm_path, rec)
        # ---- human-readable table
        co_dir = ROOT / "New_mediciine" / "companies" / (co if co != "takeda" else "takeda_public_baseline") / "financials"
        co_dir.mkdir(parents=True, exist_ok=True)
        lines = [f"# {meta['name']} — audited annual facts (SEC XBRL)", "",
                 f"Source: SEC companyfacts API for CIK {meta['cik']} (Form {meta['form']}). Generated {now_iso()}. Currency {meta['ccy']} (billions). "
                 "FY = year of period end. Provenance (XBRL tag + accession) in `New_mediciine/financial_models/edgar_facts_" + co + ".json`. "
                 "2026 is excluded because it is not a completed fiscal year.", "",
                 "| FY | Revenue | R&D (excl. acquired IPR&D) | R&D % rev | Acquired IPR&D | Pretax income | Net income | Op. cash flow | Capex | Acq. (cash) | IPR&D payments | Buybacks | Dividends | Gross margin % |",
                 "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for fy, row in sorted(table.items()):
            f = lambda k: (f"{row[k]/1e9:,.2f}" if row.get(k) is not None else "–")  # noqa: E731
            lines.append(f"| {fy} | {f('revenue')} | {f('rd_expense')} | {row.get('rd_expense_pct_revenue','–')} | {f('ipr_d_acquired')} | {f('pretax_income')} | {f('net_income')} | {f('operating_cash_flow')} | {f('capex')} | {f('acquisitions_cash')} | {f('iprd_payments_cash')} | {f('buybacks')} | {f('dividends_paid')} | {row.get('gross_margin_pct','–')} |")
        lines += ["", "Claims for FY2021+ are registered in shard `A4_financial` (CLM-004xxx) with one source record per accession (SRC-004xxx).",
                  "Caveats: J&J FY2023+ reflects Kenvue separation (consumer health deconsolidated Aug 2023) — do not compare pre/post without adjustment. "
                  "AbbVie R&D includes acquired IPR&D expensed under ASU 2021 practice; see IPR&D line in JSON. Takeda reports IFRS in JPY; fiscal year ends March 31 (FY label = year of period end, so 'FY2025' = Apr-2024..Mar-2025)."]
        (co_dir / "edgar_annual_facts.md").write_text("\n".join(lines), encoding="utf-8")
        print(f"  {co}: {len(table)} fiscal years, metrics/yr ~{max((len([k for k in r if not k.startswith('_')]) for r in table.values()), default=0)}", file=sys.stderr)

    (ROOT / "data" / "normalized").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "normalized" / "financials_annual.json").write_text(json.dumps(normalized, indent=1, default=str), encoding="utf-8")
    print(json.dumps({"sources_written": sid - 4000, "claims_written": cid - 4000,
                      "out": "data/normalized/financials_annual.json"}, indent=2))


if __name__ == "__main__":
    main()
