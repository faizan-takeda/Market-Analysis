# A10 audit: URL check (Task 4)

Date 2026-11-21. Markdown relative-link check: `python3 scripts/check_links.py` (175 relative links, 3 broken). Canonical-URL spot check: 40 URLs stratified across 98 hosts (cap 4 per host), `curl -sL -m 25` with a browser-style user agent, 1.2 s between requests, one retry (via `web_fetch`) for non-200 results.

Side effect to note: `scripts/check_links.py` writes `quality/coverage_reports/link_check_2026-11-21.json`, so the run overwrote the Director's earlier file of the same name (outside my permitted directories). The new content is the output above; the Director may re-run or restore from git.

## Relative links (markdown)
| File | Broken link | Cause |
|---|---|---|
| New_mediciine/companies/johnson_johnson/business/business_model.md | financials/xbrl_annual_facts.md (2 occurrences) | path resolves under business/; target is ../financials/xbrl_annual_facts.md |
| New_mediciine/companies/johnson_johnson/business/business_model.md | evidence_gaps.md | target is ../evidence_gaps.md |

## Canonical URLs (40)
Result by first pass: 30 x 200, 8 x 403, 2 x 404. After retry: both 404s load in `web_fetch` (FDA Novel Drug Approvals 2025, 46 approvals, includes Inluriyo and Imaavy; FDA Abiomed Automated Impella Controller recall notice), so they are bot-handling artefacts, not dead links. The 403s are bot walls (investor.lilly.com, bcg.com, opensecrets.org, api.open.fec.gov without key, stocktitan.net, docs.justia.com) or the SEC fair-access rule (sec.gov rejects a User-Agent without a contact address; a browser-style UA is not enough). No hard 404 was confirmed.

| Source | Registry status | HTTP | URL |
|---|---|---|---|
| SRC-007018 | metadata_only | 200 | https://www.entyvio.com/entyvioconnect-form |
| SRC-008029 | blocked | 403 | https://www.opensecrets.org/federal-lobbying/clients/summary?id=D000000166 |
| SRC-008017 | retrieved | 200 | https://www.investor.jnj.com/files/doc_downloads/2024/04/2023-us-trade.pdf |
| SRC-007025 | blocked | 200 | https://www.biopharmadive.com/news/kisunla-modified-dosing-fda-approve-lilly-donanemab/752554/ |
| SRC-000029 | retrieved | 403 | https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies |
| SRC-003019 | retrieved | 200 | https://www.cms.gov/files/document/fact-sheet-medicare-selected-drug-negotiation-list-ipay-2026.pdf |
| SRC-002012 | retrieved | 200 | https://www.jnj.com/media-center/press-releases/johnson-johnson-medtech-receives-ide-approval-for-ottava-robotic-surgical-system |
| SRC-005016 | retrieved | 403 | https://www.bcg.com/publications/2024/a-global-biopharma-company-is-leading-digital-change |
| SRC-000022 | retrieved | 200 | https://data.sec.gov/api/xbrl/companyfacts/CIK0001395064.json |
| SRC-005015 | retrieved | 200 | https://ir.sse.or.jp/data/pdf/140120261028558569.pdf |
| SRC-002007 | retrieved | 200 | https://news.bloomberglaw.com/crypto/j-js-failed-bid-to-end-talc-suits-is-bankruptcy-voting-lesson |
| SRC-001003 | retrieved | 200 | https://www.prnewswire.com/news-releases/foundayo-orforglipron-lillys-new-oral-glp-1-pill-for-weight-loss-now-available-in-the-us-302737538.html |
| SRC-006029 | metadata_only | 200 | https://settervc.com/company/strateos |
| SRC-009019 | metadata_only | 200 | https://hub.waveup.com/funds/takeda-ventures |
| SRC-008021 | api_json | 200 | https://www.federalregister.gov/api/v1/documents/2025-06587.json |
| SRC-008020 | api_json | 403 | https://api.open.fec.gov/v1/committees/?q=abbvie%20political%20action |
| SRC-012042 | retrieved | 200 | https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2022/761105Orig1s016ltr.pdf |
| SRC-002011 | retrieved | 404 | https://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/catheter-controller-recall-abiomed-removes-automated-impella-controllers-due-purge-retainer-issues |
| SRC-009018 | metadata_only | 403 | https://www.stocktitan.net/news/TAK/innovent-biologics-announces-closing-of-global-strategic-partnership-f91oibph3tim.html |
| SRC-008009 | retrieved | 200 | https://news.abbvie.com/2026-01-12-AbbVie-and-Trump-Administration-Reach-Agreement-to-Improve-Access-and-Affordability-for-Americans |
| SRC-006027 | retrieved | 200 | https://www.drugdiscoverytrends.com/insilicos-ai-designed-rentosertib-shows-promise-in-first-phase-2a-trial-results/ |
| SRC-008022 | retrieved | 403 | https://www.sec.gov/Archives/edgar/data/59478/000005947826000013/lly-20251231.htm |
| SRC-008034 | metadata_only | 403 | https://docs.justia.com/cases/federal/district-courts/california/candce/3:2025cv03534/448395/126 |
| SRC-006002 | retrieved | 200 | https://blogs.nvidia.com/?p=90297 |
| SRC-003018 | retrieved | 200 | https://www.amgen.com/newsroom/press-releases/2023/01/amjevita-adalimumabatto-first-biosimilar-to-humira-now-available-in-the-united-states |
| SRC-007013 | retrieved | 200 | https://www.drugchannels.net/2025/10/the-stelara-biosimilar-price-war-how.html |
| SRC-007011 | retrieved | 200 | https://www.managedhealthcareexecutive.com/view/cvs-caremark-to-put-zepbound-back-on-formulary-and-add-foundayo |
| SRC-004002 | api_json | 403 | https://www.sec.gov/Archives/edgar/data/59478/000005947821000083/ |
| SRC-006003 | retrieved | 200 | https://www.biopharmatrend.com/news/eli-lilly-launches-pharmas-largest-ai-supercomputer-1512/ |
| SRC-006013 | retrieved | 200 | https://www.deeplearning.ai/the-batch/johnson-johnson-reveals-its-revised-ai-strategy |
| SRC-006007 | retrieved | 200 | https://www.genengnews.com/news/synbio-synergy-ginkgo-to-acquire-troubled-zymergen-for-300m/ |
| SRC-003011 | retrieved | 200 | https://finance.yahoo.com/sectors/healthcare/articles/abbvie-tops-quarterly-expectations-newer-115048815.html |
| SRC-008004 | retrieved | 200 | https://www.axinn.com/en/insights/axinn-viewpoints/here-we-go-again-third-round-of-inflation-reduction-act-drugs-listed |
| SRC-001007 | retrieved | 200 | https://www.prnewswire.com/news-releases/lilly-announces-plans-to-build-5-billion-manufacturing-facility-in-virginia-302556880.html |
| SRC-007017 | retrieved | 200 | https://www.helpathandpap.com/About.aspx |
| SRC-000031 | retrieved | 200 | https://nvidianews.nvidia.com/news/nvidia-and-lilly-announce-co-innovation-lab-to-reinvent-drug-discovery-in-the-age-of-ai |
| SRC-001032 | retrieved | 404 | https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2025 |
| SRC-008012 | retrieved | 200 | https://www.frierlevitt.com/articles/dc-circuit-340b-rebate-models-hrsa-approval/ |
| SRC-007008 | retrieved | 200 | https://www.biospace.com/lilly-cuts-insulin-prices-by-70-percent-and-caps-patient-insulin-out-of-pocket-costs-at-35-per-month |
| SRC-000033 | metadata_only | 200 | https://www.medtechdive.com/news/jj-gets-fda-authorization-for-ottava-robot-teeing-up-competition-with-int/825905/ |

## Observations
- Sources registered `retrieved` that are now behind a bot wall for scripted clients (SRC-000029 investor.lilly.com, SRC-005016 bcg.com, SRC-008022 SEC htm with this UA): none of the three has a stored local text file (`local_extracted_text_path` is null; SRC-005016 and SRC-008022 keep only an `inspected_passage`; SRC-000029 keeps neither). A third party re-checking from a script will see 403, and SRC-000029 has no preserved passage at all. Recommend storing raw copies (`--store-raw`) for these.
- Three `metadata_only` sources are retrievable: SRC-000034, SRC-009022, SRC-009017 (see audit_wave1_reinspection.md finding 4).
- `pubmed.ncbi.nlm.nih.gov` pages fetched by `tools/evidence.py` return a 129-byte "Cookies must be enabled" stub (stored text of SRC-001025 and SRC-001028). Use NCBI E-utilities (`eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&retmode=text&rettype=abstract`), which returned the retatrutide abstract.
