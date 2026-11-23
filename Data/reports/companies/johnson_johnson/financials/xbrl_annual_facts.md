# Johnson & Johnson — annual financial facts from SEC XBRL (as filed)

Source: SEC companyfacts API for CIK 0000200406 (https://data.sec.gov/api/xbrl/companyfacts/CIK0000200406.json), retrieved 2026-11-21. 
Basis: US GAAP, USD, calendar fiscal years. Values are as tagged by the registrant in the annual report for that year (restatements noted where a later filing supplied the value). 
Each cell is a FACT claim in `claims_registry.jsonl` carrying the filing accession number. Non-GAAP measures (e.g. adjusted EPS) are **not** here.

| Concept | XBRL tag | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Total revenue (USD millions) | `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` | 93,775.0 | 94,943.0 | 85,159.0 | 88,821.0 | 94,193.0 |
| Cost of sales (USD millions) | `us-gaap:CostOfGoodsAndServicesSold` | 29,855.0 | 31,089.0 | 26,553.0 | 27,471.0 | 30,256.0 |
| Research and development expense (USD millions) | `us-gaap:ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost` | 14,714.0 | 14,603.0 | 15,085.0 | 17,232.0 | 14,665.0 |
| Selling, general and administrative expense (USD millions) | `us-gaap:SellingGeneralAndAdministrativeExpense` | 24,659.0 | 24,765.0 | 21,512.0 | 22,869.0 | 23,676.0 |
| Net income attributable to company (USD millions) | `us-gaap:NetIncomeLoss` | 20,878.0 | 17,941.0 | 35,153.0 | 14,066.0 | 26,804.0 |
| Diluted EPS | `us-gaap:EarningsPerShareDiluted` | 7.81 | 6.73 | 13.72 | 5.79 | 11.03 |
| Net cash from operating activities (USD millions) | `us-gaap:NetCashProvidedByUsedInOperatingActivities` | 23,410.0 | 21,194.0 | 22,791.0 | 24,266.0 | 24,530.0 |
| Capital expenditures (PP&E purchases) (USD millions) | `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment` | 3,652.0 | 4,009.0 | 4,543.0 | 4,424.0 | 4,832.0 |
| Acquired IPR&D expensed (asset acquisitions) (USD millions) | `us-gaap:ResearchAndDevelopmentInProcess` | 900.0 | 783.0 | — | — | — |
| Income before income taxes (USD millions) | `us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest` | 22,776.0 | 21,725.0 | 15,062.0 | 16,687.0 | 32,581.0 |
| Cash paid for business acquisitions, net (USD millions) | `us-gaap:PaymentsToAcquireBusinessesNetOfCashAcquired` | 60.0 | 17,652.0 | 0.0 | 15,146.0 | 17,541.0 |
| Total assets (USD millions) | `us-gaap:Assets` | 182,018.0 | 187,378.0 | 167,558.0 | 180,104.0 | 199,210.0 |
| Long-term debt incl. current portion (USD millions; A10 label fix — tag LongTermDebt is not the balance-sheet non-current amount) | `us-gaap:LongTermDebt` | 32,116.0 | 28,439.0 | 27,350.0 | 32,400.0 | 41,438.0 |

## Provenance per value (accession numbers)

| Concept | FY | Value | Form | Accession | Filed | Period |
|---|---|---|---|---|---|---|
| revenue | 2021 | 93,775.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| revenue | 2022 | 94,943.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| revenue | 2023 | 85,159.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| revenue | 2024 | 88,821.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| revenue | 2025 | 94,193.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| cost_of_sales | 2021 | 29,855.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| cost_of_sales | 2022 | 31,089.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| cost_of_sales | 2023 | 26,553.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| cost_of_sales | 2024 | 27,471.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| cost_of_sales | 2025 | 30,256.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| rnd_expense | 2021 | 14,714.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| rnd_expense | 2022 | 14,603.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| rnd_expense | 2023 | 15,085.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| rnd_expense | 2024 | 17,232.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| rnd_expense | 2025 | 14,665.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| sga_expense | 2021 | 24,659.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| sga_expense | 2022 | 24,765.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| sga_expense | 2023 | 21,512.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| sga_expense | 2024 | 22,869.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| sga_expense | 2025 | 23,676.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| net_income | 2021 | 20,878.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| net_income | 2022 | 17,941.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| net_income | 2023 | 35,153.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| net_income | 2024 | 14,066.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| net_income | 2025 | 26,804.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| eps_diluted | 2021 | 7.81 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| eps_diluted | 2022 | 6.73 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| eps_diluted | 2023 | 13.72 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| eps_diluted | 2024 | 5.79 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| eps_diluted | 2025 | 11.03 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| op_cash_flow | 2021 | 23,410.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| op_cash_flow | 2022 | 21,194.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| op_cash_flow | 2023 | 22,791.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| op_cash_flow | 2024 | 24,266.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| op_cash_flow | 2025 | 24,530.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| capex | 2021 | 3,652.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| capex | 2022 | 4,009.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| capex | 2023 | 4,543.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| capex | 2024 | 4,424.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| capex | 2025 | 4,832.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| acquired_iprd_expense | 2021 | 900.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| acquired_iprd_expense | 2022 | 783.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| pretax_income | 2021 | 22,776.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| pretax_income | 2022 | 21,725.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| pretax_income | 2023 | 15,062.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| pretax_income | 2024 | 16,687.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| pretax_income | 2025 | 32,581.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| acquisitions_cash | 2021 | 60.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | 2021-01-04 → 2022-01-02 |
| acquisitions_cash | 2022 | 17,652.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | 2022-01-03 → 2023-01-01 |
| acquisitions_cash | 2023 | 0.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | 2023-01-02 → 2023-12-31 |
| acquisitions_cash | 2024 | 15,146.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | 2024-01-01 → 2024-12-29 |
| acquisitions_cash | 2025 | 17,541.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | 2024-12-30 → 2025-12-28 |
| total_assets | 2021 | 182,018.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | instant → 2022-01-02 |
| total_assets | 2022 | 187,378.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | instant → 2023-01-01 |
| total_assets | 2023 | 167,558.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | instant → 2023-12-31 |
| total_assets | 2024 | 180,104.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | instant → 2024-12-29 |
| total_assets | 2025 | 199,210.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | instant → 2025-12-28 |
| long_term_debt | 2021 | 32,116.0 | 10-K | 0000200406-22-000022 | 2022-02-17 | instant → 2022-01-02 |
| long_term_debt | 2022 | 28,439.0 | 10-K | 0000200406-23-000016 | 2023-02-16 | instant → 2023-01-01 |
| long_term_debt | 2023 | 27,350.0 | 10-K | 0000200406-24-000013 | 2024-02-16 | instant → 2023-12-31 |
| long_term_debt | 2024 | 32,400.0 | 10-K | 0000200406-25-000038 | 2025-02-13 | instant → 2024-12-29 |
| long_term_debt | 2025 | 41,438.0 | 10-K | 0000200406-26-000016 | 2026-02-11 | instant → 2025-12-28 |

## Gaps

Concepts shown as — were not tagged under the candidate XBRL names for that year and must be read from the filing text (tracked in the coverage ledger).
