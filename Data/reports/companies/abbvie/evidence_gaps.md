# Evidence gaps (A3; expanded v1.1, 2026-11-21)

## Source-level gaps (sources registered but not read in full)
**Metadata-only (8) — conclusions that depend on them stay PARTIALLY_SUPPORTED or are cross-checked elsewhere:**
- SRC-003027 AbbVie completes Capstan acquisition (release): close terms now taken from the FY2025 10-K [CLM-014030] [CLM-009058].
- SRC-003028 AbbVie and Trump administration agreement (release): terms from the 10-K and A8 [CLM-008032]; the release text itself was not read [CLM-003081].
- SRC-003033 Reuters, 2027 Skyrizi+Rinvoq forecast raised to USD 27bn: only the snippet; target claim is company-reported [CLM-003022].
- SRC-003034 FY2025 and Q4 2025 results release: financials come from the 10-K; the call is covered by a transcript quote [CLM-014072].
- SRC-003035 Motley Fool Q3 2025 call transcript: snippet only.
- SRC-003036 Amjevita U.S. launch release: launch-price discounts rest on the snippet [CLM-003006].
- SRC-003037 ImmunoGen completion release; SRC-003038 Cerevel completion release: closing dates and amounts now confirmed from 10-K text [CLM-003053] [CLM-009056] [CLM-009053].
**Blocked (3):** SRC-003029 (Fierce, Skyrizi/Rinvoq projection), SRC-003030 (Fierce, Humira biosimilar share), SRC-003031 (Forbes/CVS Humira shift). The Humira contracting percentages therefore rest on trade sources not re-opened by the auditor [CLM-003007] [CLM-003009] [CLM-003085].
**Unavailable (1):** SRC-003032 (ASPE IRA research series, HTTP 502); IRA prices are taken from CMS-based claims [CLM-008010] [CLM-008012] [CLM-008013].
**API-only (7):** ClinicalTrials.gov JSON records SRC-003020..003026 (no narrative; trial-level statements are registry facts, not interpretations).
**Also:** AbbVie Ventures Impact Report 2025 (SRC-009014) is metadata-only and the PDF returned HTTP 403 to the auditor.

## Closed in v1.1
- Juvmo date: FDA action 2026-09-25, company announcement 2026-09-28 [CLM-012017] [CLM-014039].
- Aliada, Landos, Celsius, Nimble terms [CLM-014032] [CLM-014033] [CLM-009064] [CLM-014034]; Humira settlement licence-start years (terms undisclosed) [CLM-014036]; 2019 antitrust suit and Seventh Circuit outcome [CLM-014037] [CLM-008048].
- Deal-size and debt bases (master_report §22).

## Unresolved question: AbbVie Ventures founding date
'Investing since 2009' (web page) versus 'Ten years ago, AbbVie Ventures launched' (2025 impact report, about 2015) [CLM-009074] [CLM-009101] (conflicts_proposed_A10 #5). Likely reading *(INTERPRETATION, not to be asserted)*: 2009 is when venture investing began within the Abbott lineage; about 2015 is the dedicated strategic group. Next step: re-fetch the PDF with `--store-raw` and read page 1; open the web page.

## Original wave-1 gaps (A3)
- Blocked/unavailable: Fierce (403) 2027 target and Humira share pieces; Forbes (403); ASPE PDF (502). Metadata-only: Capstan close, Trump agreement release, FY2025 results release, Reuters $27bn, Motley Fool Q3 2025, AJMC, ImmunoGen/Cerevel closing releases.
- Not researched (budget cap): Apogee price (Aliada, Landos, Celsius, Nimble now closed above); Humira settlement terms remain undisclosed [CLM-014036]; gross-to-net; Allē/patient support; Skyrizi biosimilar timeline; Botox new indications; ABBV-400 indications; second-generation IL-23 competition; Skyrizi/Rinvoq FDA label detail beyond 10-K.
- Unresolved: per-arm EMPOWER results (fetched table lost alignment); NCT05443724 termination reason; Juvmo exact FDA action date (RESOLVED v1.1: 09-25 FDA, 09-28 company) [CLM-014039]; the brief's USD 10bn 2025 pledge not located [CLM-003082]; brief's ~3.5bn 2025 impairment contradicted [CLM-003058].
- Next queries: SEC 8-Ks for Capstan/Apogee terms; Drugs@FDA Juvmo; Humira patent-settlement 10-K Item 3 history; Endpoints/STAT on Cerevel diligence.
