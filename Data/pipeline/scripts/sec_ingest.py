#!/usr/bin/env python3
"""A4 Financial Intelligence — SEC EDGAR ingestion (stdlib only).

For each company:
  1. Fetch EDGAR submissions JSON -> inventory of 10-K / 20-F / 10-Q / 8-K filings (FY2021->today)
     saved to New_mediciine/evidence_library/links_and_metadata/<ticker>_sec_filings_inventory.json
  2. Fetch XBRL companyfacts JSON (public domain) -> raw_documents/sec/<ticker>_companyfacts.json
  3. Extract annual values for key concepts (10-K, fp=FY; 20-F for Takeda) -> stage one SOURCE record
     per companyfacts file and per annual report filing, and one FACT CLAIM per (concept, fiscal year),
     each carrying the accession number of the filing that reported the value.
  4. Write a reconciliation table (markdown) per company into companies/<dir>/financials/xbrl_annual_facts.md

Respects SEC fair-access policy: declared User-Agent, <=2 req/s.
Run:  python3 scripts/sec_ingest.py [LLY JNJ ABBV TAK]
Then: python3 scripts/registry.py merge-staging
"""
import json, os, sys, time, datetime, hashlib, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EL = os.path.join(ROOT, "New_mediciine", "evidence_library")
RAW = os.path.join(EL, "raw_documents", "sec")
META = os.path.join(EL, "links_and_metadata")
STAGE = os.path.join(EL, "staging", "A4_financial")
UA = os.environ.get("SEC_USER_AGENT", "MEDICINE-2040 research project (palrahma@amazon.com)")

COMPANIES = {
    "LLY": {"cik": "0000059478", "name": "Eli Lilly and Company", "dir": "eli_lilly", "annual_form": "10-K", "gaap": "us-gaap", "unit": "USD"},
    "JNJ": {"cik": "0000200406", "name": "Johnson & Johnson", "dir": "johnson_johnson", "annual_form": "10-K", "gaap": "us-gaap", "unit": "USD"},
    "ABBV": {"cik": "0001551152", "name": "AbbVie Inc.", "dir": "abbvie", "annual_form": "10-K", "gaap": "us-gaap", "unit": "USD"},
    "TAK": {"cik": "0001395064", "name": "Takeda Pharmaceutical Company Limited", "dir": "takeda_public_baseline", "annual_form": "20-F", "gaap": "ifrs-full", "unit": "JPY"},
}

# concept -> (label, candidate XBRL tags in priority order)
US_GAAP_CONCEPTS = {
    "revenue": ("Total revenue", ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"]),
    "cost_of_sales": ("Cost of sales", ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"]),
    "rnd_expense": ("Research and development expense", ["ResearchAndDevelopmentExpense", "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost"]),
    "sga_expense": ("Selling, general and administrative expense", ["SellingGeneralAndAdministrativeExpense", "MarketingSellingAndAdministrativeExpense"]),
    "operating_income": ("Operating income", ["OperatingIncomeLoss"]),
    "net_income": ("Net income attributable to company", ["NetIncomeLoss", "ProfitLoss"]),
    "eps_diluted": ("Diluted EPS", ["EarningsPerShareDiluted"]),
    "op_cash_flow": ("Net cash from operating activities", ["NetCashProvidedByUsedInOperatingActivities"]),
    "capex": ("Capital expenditures (PP&E purchases)", ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireOtherPropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"]),
    "acquired_iprd_payments": ("Cash paid for acquired in-process R&D (asset acquisitions)", ["PaymentsToAcquireInProcessResearchAndDevelopment"]),
    "acquired_iprd_expense": ("Acquired IPR&D expensed (asset acquisitions)", ["ResearchAndDevelopmentAssetAcquiredOtherThanThroughBusinessCombinationWrittenOff", "ResearchAndDevelopmentInProcess"]),
    "pretax_income": ("Income before income taxes", ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]),
    "acquisitions_cash": ("Cash paid for business acquisitions, net", ["PaymentsToAcquireBusinessesNetOfCashAcquired", "OtherPaymentsToAcquireBusinesses", "PaymentsToAcquireBusinessesGross"]),
    "total_assets": ("Total assets", ["Assets"]),
    "long_term_debt": ("Long-term debt (noncurrent where tagged LongTermDebtNoncurrent; incl. current portion where only LongTermDebt is tagged)", ["LongTermDebtNoncurrent", "LongTermDebt"]),
}
IFRS_CONCEPTS = {
    "revenue": ("Revenue", ["Revenue"]),
    "cost_of_sales": ("Cost of sales", ["CostOfSales"]),
    "rnd_expense": ("Research and development expense", ["ResearchAndDevelopmentExpense"]),
    "sga_expense": ("Selling, general and administrative expense", ["SellingGeneralAndAdministrativeExpense"]),
    "operating_income": ("Operating profit", ["ProfitLossFromOperatingActivities"]),
    "net_income": ("Profit attributable to owners of parent", ["ProfitLossAttributableToOwnersOfParent", "ProfitLoss"]),
    "eps_diluted": ("Diluted EPS", ["DilutedEarningsLossPerShare"]),
    "op_cash_flow": ("Net cash from operating activities", ["CashFlowsFromUsedInOperatingActivities"]),
    "capex": ("Purchases of PP&E", ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"]),
    "total_assets": ("Total assets", ["Assets"]),
    "long_term_debt": ("Noncurrent borrowings", ["NoncurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings", "BorrowingsNoncurrent", "NoncurrentFinancialLiabilities"]),
}
YEARS = [2021, 2022, 2023, 2024, 2025]


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity", "Host": url.split("/")[2]})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            time.sleep(0.6)
            return data if binary else data.decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 503) and attempt < 2:
                time.sleep(3 * (attempt + 1)); continue
            raise
    raise RuntimeError("unreachable")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def inventory(ticker, co):
    url = f"https://data.sec.gov/submissions/CIK{co['cik']}.json"
    raw = fetch(url, binary=True)
    sub = json.loads(raw)
    rec = sub["filings"]["recent"]
    rows = []
    for i in range(len(rec["accessionNumber"])):
        form = rec["form"][i]
        fdate = rec["filingDate"][i]
        if fdate < "2021-11-21":
            continue
        if form not in ("10-K", "10-K/A", "20-F", "20-F/A", "10-Q", "8-K", "6-K", "DEF 14A", "ARS"):
            continue
        accn = rec["accessionNumber"][i]
        accn_nodash = accn.replace("-", "")
        primary = rec["primaryDocument"][i]
        rows.append({
            "form": form, "filing_date": fdate, "report_period": rec["reportDate"][i],
            "accession_number": accn,
            "primary_document_url": f"https://www.sec.gov/Archives/edgar/data/{int(co['cik'])}/{accn_nodash}/{primary}",
            "index_url": f"https://www.sec.gov/Archives/edgar/data/{int(co['cik'])}/{accn_nodash}/",
            "description": rec["primaryDocDescription"][i],
        })
    os.makedirs(META, exist_ok=True)
    out = os.path.join(META, f"{ticker}_sec_filings_inventory.json")
    with open(out, "w") as f:
        json.dump({"ticker": ticker, "cik": co["cik"], "entity_name": sub.get("name"), "sic": sub.get("sic"),
                   "sic_description": sub.get("sicDescription"), "fiscal_year_end": sub.get("fiscalYearEnd"),
                   "source_url": url, "retrieved_at": now(), "sha256": sha256(raw), "filings": rows}, f, indent=1)
    return out, rows, sub, sha256(raw)


def companyfacts(ticker, co):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{co['cik']}.json"
    raw = fetch(url, binary=True)
    os.makedirs(RAW, exist_ok=True)
    path = os.path.join(RAW, f"{ticker}_companyfacts.json")
    with open(path, "wb") as f:
        f.write(raw)
    return path, json.loads(raw), sha256(raw), url


def annual_values(facts, co, concepts):
    """Return {concept_key: {fy: {val, accn, filed, start, end, tag, fp, form, frame}}} using annual-duration
    values reported in the annual form. For the same (tag, fy) the latest-filed value wins (restatements)."""
    taxonomy = co["gaap"]
    res = {}
    units_pref = {"USD": ["USD"], "JPY": ["JPY"]}[co["unit"]]
    for key, (label, tags) in concepts.items():
        per_tag = []
        for tag in tags:
            node = facts.get("facts", {}).get(taxonomy, {}).get(tag)
            if not node:
                continue
            unit_key = None
            for u in units_pref + (["USD/shares"] if key == "eps_diluted" else []) + (["JPY/shares"] if key == "eps_diluted" else []):
                if u in node.get("units", {}):
                    unit_key = u; break
            if not unit_key:
                continue
            found = {}
            for v in node["units"][unit_key]:
                if v.get("form") not in (co["annual_form"], co["annual_form"] + "/A"):
                    continue
                if v.get("fp") != "FY":
                    continue
                start, end = v.get("start"), v.get("end")
                is_instant = start is None
                if not is_instant:
                    d0 = datetime.date.fromisoformat(start); d1 = datetime.date.fromisoformat(end)
                    if not (330 <= (d1 - d0).days <= 380):
                        continue  # keep only ~12-month durations
                fy = int(v.get("fy")) if v.get("fy") else None
                # for calendar-year filers the annual value's end date year == fiscal year
                end_year = (datetime.date.fromisoformat(end) - datetime.timedelta(days=10)).year
                if co["unit"] == "USD":
                    fy_key = end_year
                else:  # Takeda FY ends 31 March: FY label = year in which it started
                    fy_key = end_year - 1 if end[5:7] == "03" else end_year
                if fy_key not in YEARS:
                    continue
                # keep the record from the filing whose own fiscal year matches (originally reported), else latest
                prev = found.get(fy_key)
                cand = {"val": v["val"], "accn": v["accn"], "filed": v["filed"], "start": start, "end": end,
                        "tag": f"{taxonomy}:{tag}", "unit": unit_key, "fp": v.get("fp"), "form": v.get("form"), "frame": v.get("frame"), "fy_in_filing": fy}
                if prev is None:
                    found[fy_key] = cand
                else:
                    # prefer the value from the filing for that fiscal year (as originally reported);
                    # if both are from same filing year keep latest filed
                    prev_match = prev["fy_in_filing"] == fy_key
                    cand_match = fy == fy_key
                    if (cand_match and not prev_match) or (cand_match == prev_match and cand["filed"] > prev["filed"]):
                        found[fy_key] = cand
            if found:
                per_tag.append(found)
        # choose the primary tag = best year coverage, then largest median magnitude (the main
        # income-statement line is always the largest among same-named candidates, e.g. J&J tags
        # IPR&D impairments as ResearchAndDevelopmentExpense but its main R&D line as ...ExcludingAcquiredInProcessCost)
        if per_tag:
            def med(d):
                vals = sorted(abs(x["val"]) for x in d.values()); return vals[len(vals)//2]
            per_tag.sort(key=lambda d: (len(d), med(d)), reverse=True)
            node_res = res.setdefault(key, {"label": label, "values": {}})
            for found in per_tag:
                for fy_key, cand in found.items():
                    if fy_key not in node_res["values"]:
                        cand = dict(cand); cand["filled_from_secondary_tag"] = found is not per_tag[0]
                        node_res["values"][fy_key] = cand
    return res


def fmt(v, unit):
    if unit in ("USD/shares", "JPY/shares"):
        return f"{v:,.2f}"
    return f"{v/1e6:,.1f}"


def stage_records(ticker, co, inv_path, inv_rows, inv_sha, cf_path, cf_sha, cf_url, values):
    os.makedirs(STAGE, exist_ok=True)
    recs = []
    t = now()
    cf_tmp = f"TMP-{ticker}-companyfacts"
    recs.append({"record_type": "source", "tmp_id": cf_tmp,
                 "title": f"SEC XBRL company facts — {co['name']} (CIK {co['cik']})",
                 "author_or_org": "U.S. Securities and Exchange Commission (XBRL financial data API)",
                 "publisher": "SEC EDGAR", "company": ticker, "subject_category": ["financials"],
                 "source_type": "xbrl_companyfacts", "credibility_tier": "T1_primary_official",
                 "original_url": cf_url, "canonical_url": cf_url, "published_at": None, "reporting_period": None,
                 "retrieved_at": t, "identifiers": {"cik": co["cik"]},
                 "local_document_path": os.path.relpath(cf_path, ROOT), "content_sha256": cf_sha,
                 "access_status": "retrieved", "rights": "public_domain",
                 "limitations": "Values as tagged by the registrant in XBRL; restated values may differ from originally reported figures. Non-GAAP measures are not in XBRL.",
                 "added_by": "A4", "run_id": "RUN-0001-sec-ingest"})
    recs.append({"record_type": "source", "tmp_id": f"TMP-{ticker}-inventory",
                 "title": f"SEC EDGAR filing index (submissions API) — {co['name']}",
                 "author_or_org": "U.S. Securities and Exchange Commission", "publisher": "SEC EDGAR",
                 "company": ticker, "subject_category": ["financials", "business"], "source_type": "government_data",
                 "credibility_tier": "T1_primary_official",
                 "original_url": f"https://data.sec.gov/submissions/CIK{co['cik']}.json",
                 "canonical_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={co['cik']}&type=&dateb=&owner=include&count=40",
                 "published_at": None, "reporting_period": None, "retrieved_at": t, "identifiers": {"cik": co["cik"]},
                 "local_document_path": os.path.relpath(inv_path, ROOT), "content_sha256": inv_sha,
                 "access_status": "retrieved", "rights": "public_domain", "limitations": "Recent-filings window only (EDGAR 'recent' array).",
                 "added_by": "A4", "run_id": "RUN-0001-sec-ingest"})
    # one source per annual report filing in scope
    accn_to_tmp = {}
    for r in inv_rows:
        if r["form"] in (co["annual_form"], co["annual_form"] + "/A"):
            tmp = f"TMP-{ticker}-{r['accession_number']}"
            accn_to_tmp[r["accession_number"]] = tmp
            period_year = int(r["report_period"][:4])
            rp = f"TAK-FY{period_year-1}" if ticker == "TAK" else f"FY{period_year}"
            recs.append({"record_type": "source", "tmp_id": tmp,
                         "title": f"{co['name']} Form {r['form']} for period ending {r['report_period']}",
                         "author_or_org": co["name"], "publisher": "SEC EDGAR", "company": ticker,
                         "subject_category": ["financials", "business", "pipeline", "policy_regulation"],
                         "source_type": "sec_filing", "credibility_tier": "T1_primary_official",
                         "original_url": r["primary_document_url"], "canonical_url": r["primary_document_url"],
                         "published_at": r["filing_date"], "reporting_period": rp, "retrieved_at": t,
                         "identifiers": {"accession_number": r["accession_number"], "cik": co["cik"]},
                         "local_document_path": None, "content_sha256": None,
                         "access_status": "metadata_only", "rights": "public_domain",
                         "locator_hint": "Item 7 MD&A; Item 8 Financial Statements",
                         "limitations": "Registered from the EDGAR index; full-text inspection of this filing is tracked separately in the coverage ledger.",
                         "added_by": "A4", "run_id": "RUN-0001-sec-ingest"})
    # claims
    for key, node in values.items():
        for fy in sorted(node["values"]):
            v = node["values"][fy]
            unit = v["unit"]
            disp_unit = "USD_millions" if unit == "USD" else "JPY_millions" if unit == "JPY" else unit
            val = v["val"] / 1e6 if unit in ("USD", "JPY") else v["val"]
            rp = f"TAK-FY{fy}" if ticker == "TAK" else f"FY{fy}"
            period_txt = f"fiscal year {fy} (Apr {fy}–Mar {fy+1})" if ticker == "TAK" else f"fiscal year {fy}"
            stmt = (f"{co['name']} reported {node['label'].lower()} of {fmt(v['val'], unit)} "
                    f"{'million ' if unit in ('USD','JPY') else ''}{unit.split('/')[0]} for {period_txt} "
                    f"({v['start'] or 'as of'} to {v['end']}), as tagged {v['tag']} in Form {v['form']} accession {v['accn']} filed {v['filed']}.")
            support = [{"source_id": cf_tmp, "locator": f"facts.{v['tag'].replace(':','.')}.units.{unit}; end={v['end']}; accn={v['accn']}; frame={v['frame']}"}]
            if v["accn"] in accn_to_tmp:
                support.append({"source_id": accn_to_tmp[v["accn"]], "locator": "Item 8 — Consolidated financial statements (value as tagged in the filing's XBRL)"})
            recs.append({"record_type": "claim", "statement": stmt, "kind": "FACT", "companies": [ticker],
                         "domains": ["financials"], "entities": [co["name"]], "supporting_sources": support,
                         "independent_corroboration": [], "single_interested_source": False,
                         "contrary_evidence": [], "value": round(val, 3), "unit": disp_unit,
                         "reporting_period": rp, "event_date": v["end"],
                         "basis": "IFRS as filed" if ticker == "TAK" else "US GAAP as filed (XBRL)",
                         "status": "SUPPORTED",
                         "confidence_rationale": "Audited annual financial statement value from the registrant's SEC XBRL submission; regulatory filing, not a press claim." + (" NOTE: value taken from a secondary candidate XBRL tag because the primary tag was not used for this year; definitional consistency with other years should be checked against the filing text." if v.get("filled_from_secondary_tag") else "") + (f" NOTE: value is a comparative taken from the FY{v['fy_in_filing']} filing rather than the original FY{fy} report, so it may reflect a recast/restatement." if v.get("fy_in_filing") and v["fy_in_filing"] != fy else ""),
                         "maturity": None, "last_verified": t[:10],
                         "related_reports": [f"New_mediciine/companies/{co['dir']}/financials/xbrl_annual_facts.md"],
                         "implications": None, "added_by": "A4", "run_id": "RUN-0001-sec-ingest",
                         "_concept_key": key, "_fy": fy})
    out = os.path.join(STAGE, f"{ticker}_sec_batch.jsonl")
    with open(out, "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return out, len([r for r in recs if r["record_type"] == "claim"])


def write_table(ticker, co, values, cf_url):
    d = os.path.join(ROOT, "New_mediciine", "companies", co["dir"], "financials")
    os.makedirs(d, exist_ok=True)
    unit_lbl = "USD millions" if co["unit"] == "USD" else "JPY millions"
    lines = [f"# {co['name']} — annual financial facts from SEC XBRL (as filed)", "",
             f"Source: SEC companyfacts API for CIK {co['cik']} ({cf_url}), retrieved {now()[:10]}. ",
             f"Basis: {'IFRS, JPY, fiscal years ending 31 March (FY label = starting year)' if ticker=='TAK' else 'US GAAP, USD, calendar fiscal years'}. "
             "Values are as tagged by the registrant in the annual report for that year (restatements noted where a later filing supplied the value). ",
             "Each cell is a FACT claim in `claims_registry.jsonl` carrying the filing accession number. Non-GAAP measures (e.g. adjusted EPS) are **not** here.", "",
             f"| Concept | XBRL tag | " + " | ".join(f"FY{y}" for y in YEARS) + " |", "|---|---|" + "---|" * len(YEARS)]
    for key, node in values.items():
        tag = next(iter(node["values"].values()))["tag"]
        unit = next(iter(node["values"].values()))["unit"]
        cells = []
        for y in YEARS:
            v = node["values"].get(y)
            cells.append(fmt(v["val"], unit) if v else "—")
        lbl = node["label"] + ("" if unit.endswith("shares") else f" ({unit_lbl})")
        lines.append(f"| {lbl} | `{tag}` | " + " | ".join(cells) + " |")
    lines += ["", "## Provenance per value (accession numbers)", "", "| Concept | FY | Value | Form | Accession | Filed | Period |", "|---|---|---|---|---|---|---|"]
    for key, node in values.items():
        for y in sorted(node["values"]):
            v = node["values"][y]
            flag = (" (comparative from FY%s filing)" % v['fy_in_filing']) if v.get('fy_in_filing') and v['fy_in_filing'] != y else ""
            lines.append(f"| {key} | {y} | {fmt(v['val'], v['unit'])} | {v['form']} | {v['accn']}{flag} | {v['filed']} | {v['start'] or 'instant'} → {v['end']} |")
    lines += ["", "## Gaps", "", "Concepts shown as — were not tagged under the candidate XBRL names for that year and must be read from the filing text (tracked in the coverage ledger)."]
    with open(os.path.join(d, "xbrl_annual_facts.md"), "w") as f:
        f.write("\n".join(lines) + "\n")


def main(argv):
    tickers = argv[1:] or list(COMPANIES)
    summary = {}
    for t in tickers:
        co = COMPANIES[t]
        print(f"== {t} inventory"); inv_path, rows, sub, inv_sha = inventory(t, co)
        print(f"   {len(rows)} filings since 2021-11-21; annual forms: {sum(1 for r in rows if r['form'].startswith(co['annual_form']))}")
        print(f"== {t} companyfacts"); cf_path, facts, cf_sha, cf_url = companyfacts(t, co)
        vals = annual_values(facts, co, IFRS_CONCEPTS if t == "TAK" else US_GAAP_CONCEPTS)
        print(f"   concepts found: {sorted(vals)}")
        write_table(t, co, vals, cf_url)
        out, n = stage_records(t, co, inv_path, rows, inv_sha, cf_path, cf_sha, cf_url, vals)
        print(f"   staged {out} ({n} claims)")
        summary[t] = {"filings": len(rows), "concepts": {k: sorted(v['values']) for k, v in vals.items()}, "claims": n}
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main(sys.argv)
