# A15 — Dossier integrator (wave 3): fold audit repairs and gap-fill findings into the four dossiers

Allowed writes: Markdown under `/Users/palrahma/Desktop/MEDICINE/New_mediciine/companies/{eli_lilly,johnson_johnson,abbvie,takeda_public_baseline}/**` EXCEPT `financials/xbrl_annual_facts.md`, `financials/edgar_annual_facts.md`, `pipeline/ctgov_inventory.md`. No registry/shard writes (cite existing IDs only; A14's claims are CLM-014xxx, A7's CLM-007xxx, A8's CLM-008xxx, A12's CLM-012xxx, A6 CLM-006xxx, A9 CLM-009xxx — all already in `claims_registry.jsonl`).

## Inputs
1. `quality/citation_audits/gate1_verdicts.md`, `audit_wave1_reinspection.md`, `audit_wave1_status_discipline.md`, `New_mediciine/evidence_library/conflicts_proposed_A10.jsonl` — the auditor's required repairs and contested claims.
2. `New_mediciine/research_coverage/gapfill_wave2/gapfill_findings.md` — each section ends with "Integrate into: <path>".
3. Horizontal reports to cross-link from each dossier: `industry_transformation/{ai_data_robotics,partnerships_ecosystem,pipeline_regulatory,policy,commercial_patient}/map.md` (link the specific files; pull the 3–5 most consequential claims per company per horizontal into the dossier sections 8–13, with claim IDs).
4. `research_methodology/briefs/WAVE1_COMMON.md` §1 and §4 (evidence rules, report rules).

## Work, per dossier (do Lilly, J&J, AbbVie, Takeda in that order; save after each)
- Apply every audit repair: fix locators the auditor corrected; where a number was NUMBER_MISMATCH, replace with the audited value and cite the auditor's record; where a claim is contested, mark the sentence *(contested — see conflicts_proposed_A10 #n)*; retype FACT→INTERPRETATION sentences the auditor flagged.
- Integrate gap-fill findings into the right sections (cite CLM-014xxx); update `timeline.md` with new dated events; update `evidence_gaps.md` to remove closed gaps and keep open ones.
- Fill sections 8 (AI/data), 9 (robotics), 12 (partnerships), 13 (policy), 10–11 (commercial/patient) from the horizontal reports with claim IDs and relative links (`../../industry_transformation/...`).
- Add a "Dossier status" header: version v1.1, Gate 1 verdict (from the auditor), date, claim count by company (`grep -c '"LLY"' …` style counts are fine).
- Keep every existing accurate citation; never delete evidence; never add a number without a claim ID.
- Update each company `map.md`.

## Output
Completion report: FILES CHANGED (per dossier: sections touched, repairs applied count, gap-fill items integrated count) / REPAIRS NOT APPLIED AND WHY / REMAINING GAPS. Budget 400 tool calls; use targeted str_replace edits, not full rewrites, so other agents' citations survive.
