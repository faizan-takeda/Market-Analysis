# Robotics and automation deployment comparison

Cutoff 2026-11-21. "Robotics" covers three different things in the registry, and the companies are active in different ones. They are compared within a category only. Maturity values follow the A6 scale with the A10 retags applied (see [data_ai_maturity_matrix.md](data_ai_maturity_matrix.md)) [CLM-000284] [CLM-006026].

## 1. Category A: robotics sold as products (surgical and interventional)

Only J&J operates in this category. No Lilly, AbbVie or Takeda product-robotics evidence was found [CLM-006053].

| System | Regulatory record | Commercial and clinical evidence | Maturity | Claims |
|---|---|---|---|---|
| OTTAVA (table-integrated soft-tissue robot) | IDE approval announced 2024-11-12; first IDE cases early 2025 at Memorial Hermann-TMC; De Novo request received 2025-12-18; De Novo DEN250068 granted 2026-07-21 per the FDA record (J&J's release says 2026-07-22), Class II, upper-abdominal general laparoscopic procedures | J&J announced Memorial Hermann-TMC as the first hospital to install OTTAVA under an early-access commercial programme (announcement on 2026-11-19); completion of the installation is not shown. No revenue, unit-sale, order-book or clinical-superiority figure is disclosed. IDE operating rooms were as small as 243 sq ft, from a user survey of n=20 | **pilot** (A6); first installation announced, not shown completed | [CLM-002048] [CLM-002049] [CLM-014022] [CLM-014023] [CLM-000283] [CLM-014024] [CLM-000284] [CLM-006028] [CLM-006029] |
| MONARCH (bronchoscopy and urology) | MONARCH QUEST 3 clearance announced 2026-08-17; openFDA lists K260382 (Auris Health, decided 2026-07-25), whose link to the QUEST 3 name is inferred; K243219 also listed | Company-sponsored single-arm TARGET study: 679 patients, 21 sites, lesion reached in 98.7% of cases; installed base undisclosed | **operational** | [CLM-006027] [CLM-014025] [CLM-002067] [CLM-000286] |
| VELYS (knee, hip, spine) | Five 510(k) clearances in openFDA: K202769 (2021-01-14), K233227 (2023-12-14), K240211 (2024-06-05), K253551 (hip navigation) and K260480 (2026-06-25); VELYS Spine clearance announced 2024-08-02 | FY2025 10-K cites "pull through" for ATTUNE knees but no system or procedure counts; Orthopaedics grew 1.1% in FY2025 | **operational** (A10 retag from scaled) | [CLM-014026] [CLM-002066] [CLM-006026] [CLM-002029] |

Read together: J&J has regulator records for three platforms and company-reported clinical data for one. It has no disclosed installed base, procedure count or revenue for any of them, so deployment *scale* cannot be compared with anyone *(INTERPRETATION)* [CLM-006054]. The OTTAVA acquisition (Auris) carried a USD 0.9bn partial impairment in FY2021 [CLM-009047]. J&J's CEO said on 2026-05-27 that the company hoped for OTTAVA approval "by the end of this year, beginning of next year", and the FDA acted earlier [CLM-014070].

The OTTAVA "about 24 months from IDE to first commercial installation" figure in the earlier J&J dossier must not be used: the installation is announced, not completed, and A10 instructs that no IDE-to-install duration be derived [CLM-000284] [CLM-002049].

Device safety events that sit beside this category but are not robotics: Varipulse U.S. cases were paused on 2025-01-05 and FDA recorded 4 of 132 patients (about 3%) with stroke or TIA against about 1% expected; Impella Class I recall covered 66,390 pumps [CLM-002044] [CLM-014018] [CLM-002046].

## 2. Category B: laboratory automation and robotic labs (R&D infrastructure)

| Company | Evidence | Maturity | Claims |
|---|---|---|---|
| Lilly | Life Sciences Studio (San Diego, remote robotic lab; start 2017 per one source, public launch about 2020 per another, USD 90m reported) was acquired by Arctoris in 2024 and moved to Oxford; the reason for divestment is undisclosed. NVIDIA-Lilly co-innovation lab (agentic wet labs linked to dry labs, up to USD 1bn over five years) announced 2026-01-12, no source shows it operating | Studio: **operational, then divested**; co-innovation lab: **concept** | [CLM-006013] [CLM-006014] [CLM-006017] [CLM-000281] [CLM-014053] |
| J&J | No lab-automation evidence found; AI image analytics on its biosignature platform is qualitative | **operational** (qualitative, self-reported) | [CLM-006024] |
| AbbVie | BigHat pairs ML with a high-speed wet lab under its own platform, with no result yet | **prototype** | [CLM-006035] |
| Takeda | No public evidence of lab automation in the 20-F, report landing page or press; Nabla reports a three-to-four-week design-to-test loop (a company statement) | **evidence gap**; Nabla loop: **prototype** | [CLM-005067] [CLM-005080] [CLM-006040] |

Calibration: owned and venture-funded cloud-lab and biofoundry models ended in divestment or distressed sale in the cases reviewed (Lilly's studio, Zymergen sold for about USD 300m at about one-tenth of its IPO-era valuation after cumulative net losses of USD 1.2bn) [CLM-006052] [CLM-006051].

## 3. Category C: manufacturing and plant automation

| Company | Evidence | Maturity | Claims |
|---|---|---|---|
| Lilly | Lilly Lebanon Advanced Therapies (first dedicated genetic-medicine plant) opened 2026-05-06 with robotic machines that dose, measure and seal medicines, seen on a guided tour, no performance data. NVIDIA states Lilly uses robots for quality inspection and transport and plans digital twins on Omniverse, no counts. Capex rose from USD 1.3bn to USD 7.8bn (FY2021 to FY2025). Several announced sites are pre-operating: Houston (operational "within five years"), Alabama (completion 2032), Pennsylvania (operational 2031), Alzey (from 2027); only Concord NC (trade report), Kinsale and the Lebanon genetic-medicine plant show operating evidence | plant robotics: **operational** (no metrics); digital twins: **pilot** | [CLM-006002] [CLM-001041] [CLM-006006] [CLM-000168] [CLM-000172] [CLM-014008] [CLM-014009] [CLM-014010] [CLM-014012] [CLM-014014] [CLM-014015] |
| J&J | Gen-AI quality-control tool is the only manufacturing-adjacent item (see the AI matrix); no plant-robotics evidence found | n/a | [CLM-006021] |
| AbbVie | Not searched in depth; construction starts in Illinois and Massachusetts in 2025 are noted without automation detail | gap | [CLM-003082] |
| Takeda | More than 170 AI predictive-maintenance agents at Lessines; One Day Batch Release pilots at six sites with a 60% release-lead-time reduction targeted by 2028; plasma donation nomograms in 270+ centres. No continuous-manufacturing or robotics evidence found; the earlier baseline's "evidence gap" for automation is partly closed for AI-enabled maintenance, not for robotics | AI maintenance: **operational** (company report); batch release: **pilot** | [CLM-014041] [CLM-014042] [CLM-005060] [CLM-005067] |

Baseline note for Takeda: the capability baseline classes lab automation and robotics as EVIDENCE_GAP on the basis of CLM-005067; the 2026 integrated report evidence (CLM-014041, CLM-014042) post-dates that baseline and shows company-reported AI-enabled plant maintenance and a batch-release pilot. This does not change the robotics finding *(INTERPRETATION)* [CLM-005067] [CLM-014041].

## 4. Comparison validity

- Category A is a product business (revenue-bearing devices for hospitals); categories B and C are internal cost and cycle-time investments. A statement such as "J&J leads in robotics" is true only for Category A and says nothing about Lilly's or Takeda's plants *(INTERPRETATION)*.
- Within each category, maturity levels rest on company or vendor statements except the FDA device records [CLM-006054].
- Deployment scale (installed base, units, procedures, plant counts with robots) is undisclosed for every company, so no quantitative comparison is possible.

## 5. What is contested and unknown

- Contested: Lilly Studio start year and cost; Strateos fate [CLM-006014] [CLM-006015] [CLM-014057]. OTTAVA De Novo date (21 vs 22 July 2026) [CLM-014022] [CLM-000283].
- Unknown: installed bases and procedure counts for OTTAVA, MONARCH, VELYS; operating metrics for any pharma plant robotics; whether the NVIDIA lab has begun work [CLM-006029] [CLM-014053].
