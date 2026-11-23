// Data access layer. Everything comes from /data/*.json written by ../scripts/build_app_data.py.
// No literals from research are allowed in components; if a dataset is missing, views render an explicit "not yet produced" state.
import { useEffect, useState } from "react";

export type Company = "LLY" | "JNJ" | "ABBV" | "TAK" | "MULTI" | "INDUSTRY" | "METHODOLOGY";
export interface SourceRef { source_id: string; locator: string }
export interface Claim {
  claim_id: string; statement: string; kind: "FACT" | "INTERPRETATION" | "HYPOTHESIS" | "SCENARIO" | "RECOMMENDATION";
  companies: Company[]; domains?: string[]; entities?: string[]; supporting_sources: SourceRef[];
  independent_corroboration?: string[]; single_interested_source?: boolean; contrary_evidence?: string[]; contrary_source_ids?: string[];
  value?: number | string | null; unit?: string | null; reporting_period?: string | null; event_date?: string | null; basis?: string | null;
  status: string; confidence_rationale?: string; maturity?: string | null; last_verified: string; implications?: string | null; run_id?: string;
  merged_from_shard?: string | null; related_reports?: string[]; tags?: string[];
}
export interface Source {
  source_id: string; title: string; publisher: string; company: Company; source_type: string; credibility_tier: string; canonical_url: string;
  published_at?: string | null; reporting_period?: string | null; retrieved_at: string; access_status: string; locator_hint?: string | null;
  identifiers?: Record<string, string | null>; limitations?: string | null; local_extracted_text_path?: string | null; subject_category?: string[];
}
export interface FinValue { value: number; unit: string; claim_id: string; period: string }
export interface Financials { [co: string]: { meta: { name: string; short: string; currency: string; fiscal_year: string }; concepts: { [concept: string]: { [fy: string]: FinValue } } } }
export interface ProductSeries { company: Company; product: string; molecule: string; role: string; unit: string; values: Record<string, number | null>; claims: string[]; loe_note: string | null }
export interface LoeEvent { company: Company; product: string; event: string; date: string; status: string; claims: string[] }
export interface Products { series: ProductSeries[]; loe_events: LoeEvent[] }
export interface KGNode { id: string; type: string; label: string }
export interface KGEdge { source: string; target: string; claims: string[]; domains: string[]; kinds: string[] }
export interface KG { nodes: KGNode[]; edges: KGEdge[]; note: string }
export interface RGNode { id: string; label: string; shape: string; status: string }
export interface RG { nodes: RGNode[]; edges: { source: string; target: string; label: string }[] }
export interface CoverageRow { company: string; family: string; status: string; discovered: number; reviewed: number; notes: string | null; gap: string | null }
export interface MaturityRow { claim_id: string; company: Company; companies: Company[]; maturity: string; statement: string; event_date?: string | null; entities: string[]; domains: string[]; sources: string[]; single_interested_source: boolean; status: string; shard?: string | null }
export interface MatrixRow { companies: Company[]; initiative: string; maturity_raw: string; maturity: string; claim_ids: string[]; outcome_evidence: string; note: string; domains: string[]; years: number[] }
export interface ProjectState {
  built_at: string; phase: string; sources: number; claims: number; claims_by_status: Record<string, number>; claims_by_kind: Record<string, number>;
  claims_by_maturity: Record<string, number>; claims_by_shard: Record<string, number>; claims_contrary: number; claims_single_source: number;
  sources_by_tier: Record<string, number>; sources_by_company: Record<string, number>; datasets: Record<string, number>; strategy_files: Record<string, boolean>; lead_model: string; harness: string;
}
export interface TimelineEvent { date: string; year: number | null; event: string; claim_ids: string[] }
export type Timelines = Record<string, { available: boolean; path?: string; events: TimelineEvent[] }>;
export interface CardField { label: string; text: string; claim_ids: string[] }
export interface MechCard {
  id: string; kind: "mechanism_card" | "moat"; title: string; companies: Company[]; company_label: string; fields: CardField[];
  stages: Record<string, { text: string; claim_ids: string[] }>; claim_ids: string[]; source_ids: string[]; contrary: string[]; source_file: string; gap?: boolean;
}
export interface DealEdge { from: string; to: string; type: string; date?: string; status?: string; claim_ids: string[]; value_usd_m?: number; year: number | null; from_code: string | null }
export interface DealRow { company: Company; date: string; year: number | null; counterparty: string; type: string; area: string; upfront: string; contingent: string; accounting: string; status: string; claim_ids: string[] }
export interface Deals { available: boolean; reason?: string; edges: DealEdge[]; inventory: DealRow[] }
export interface ApprovalRow { section: string; kind: string; company: Company | null; date: string; year: number | null; product: string; ingredient: string; detail: string; sponsor: string; claim_ids: string[] }
export interface SetbackRow { when: string; year: number | null; company: Company | null; asset: string; what: string; claim_ids: string[] }
export interface Optional<T> { available: boolean; reason?: string; rows: T[] }
export interface TakedaCap { area: string; class: string; class_raw: string; claim_ids: string[]; validation: string; ivb_refs: string[] }
export interface TakedaIvb { id: string; question: string; why: string; linked: string; owner: string; claim_ids: string[] }
export interface TakedaBaseline { available: boolean; reason?: string; capabilities: TakedaCap[]; backlog: TakedaIvb[] }
export interface Conflicts { available: boolean; items: Record<string, any>[] }
export interface StrategyFile { available: boolean; path: string; data: any }
export interface Strategy { files: Record<string, StrategyFile> }

export interface Report { path: string; title: string; pillar: string; company: string; section: string; also: string[]; markdown: string; word_count: number; claim_ids: string[]; source_ids: string[]; updated: string }
export interface ReportsFile { generated: string; count: number; reports: Report[] }
export interface QaDoc { k: "claim" | "source" | "report"; id: string; t: string; x: string; co: string[]; kind?: string; sr?: string[]; path?: string; h?: string; pillar?: string; ids?: string[] }
export interface QaIndex { count: number; docs: QaDoc[] }

export interface ResearchLog { experiments: Record<string, any>[]; backlog: Record<string, any>[] }

export interface Bundle {
  log: ResearchLog; reports: ReportsFile; qa: QaIndex; reportByPath: Map<string, Report>;
  claims: Claim[]; sources: Source[]; financials: Financials; products: Products; kg: KG; rg: RG;
  coverage: { rows: CoverageRow[]; updated_at?: string }; maturity: MaturityRow[]; matrix: Optional<MatrixRow> & { rows: MatrixRow[] }; state: ProjectState; index: Record<string, string[]>;
  timelines: Timelines; cards: { available: boolean; reason?: string | null; cards: MechCard[] }; deals: Deals; approvals: Optional<ApprovalRow>; setbacks: Optional<SetbackRow>;
  takeda: TakedaBaseline; conflicts: Conflicts; strategy: Strategy;
  claimById: Map<string, Claim>; sourceById: Map<string, Source>;
}

const base = (import.meta as any).env?.BASE_URL ?? "./";
/** Single-file export: scripts/build_single_file.py inlines every dataset as one JSON blob in <script id="medicine-data">. */
let inlined: Record<string, unknown> | null | undefined;
function inlinedData(): Record<string, unknown> | null {
  if (inlined !== undefined) return inlined ?? null;
  inlined = null;
  if (typeof document !== "undefined") {
    const w = window as any;
    if (w.__MEDICINE_DATA__) inlined = w.__MEDICINE_DATA__;
    else { const el = document.getElementById("medicine-data"); if (el && el.textContent) { try { inlined = JSON.parse(el.textContent); } catch { inlined = null; } } }
  }
  return inlined ?? null;
}
async function j<T>(name: string): Promise<T> {
  const inl = inlinedData();
  if (inl && name in inl) return inl[name] as T;
  const r = await fetch(`${base}data/${name}`);
  if (!r.ok) throw new Error(`missing dataset ${name} (${r.status}) — run scripts/build_app_data.py`);
  return r.json();
}

let cache: Promise<Bundle> | null = null;
export function loadBundle(): Promise<Bundle> {
  if (!cache) {
    cache = (async () => {
      const [claims, sources, financials, products, kg, rg, coverage, maturity, matrix, state, index, timelines, cards, deals, approvals, setbacks, takeda, conflicts, strategy, reports, qa, log] = await Promise.all([
        j<Claim[]>("claims.json"), j<Source[]>("sources.json"), j<Financials>("financials.json"), j<Products>("products.json"),
        j<KG>("knowledge_graph.json"), j<RG>("research_graph.json"), j<{ rows: CoverageRow[] }>("coverage.json"), j<MaturityRow[]>("maturity.json"), j<any>("maturity_matrix.json"),
        j<ProjectState>("project_state.json"), j<Record<string, string[]>>("search_index.json"), j<Timelines>("timelines.json"), j<any>("mechanism_cards.json"), j<Deals>("deals.json"),
        j<any>("approvals.json"), j<any>("setbacks.json"), j<TakedaBaseline>("takeda_baseline.json"), j<Conflicts>("conflicts.json"), j<Strategy>("strategy.json"), j<ReportsFile>("reports.json"), j<QaIndex>("qa_index.json"), j<ResearchLog>("research_log.json"),
      ]);
      return { claims, sources, financials, products, kg, rg, coverage, maturity, matrix, state, index, timelines, cards, deals, approvals, setbacks, takeda, conflicts, strategy, reports, qa, log, reportByPath: new Map(reports.reports.map((r) => [r.path, r])),
        claimById: new Map(claims.map((c) => [c.claim_id, c])), sourceById: new Map(sources.map((s) => [s.source_id, s])) };
    })();
  }
  return cache;
}

export function useBundle() {
  const [b, setB] = useState<Bundle | null>(null);
  const [err, setErr] = useState<string | null>(null);
  useEffect(() => { loadBundle().then(setB).catch((e) => setErr(String(e))); }, []);
  return { bundle: b, error: err };
}

export const COMPANY_NAMES: Record<string, string> = { LLY: "Eli Lilly", JNJ: "Johnson & Johnson", ABBV: "AbbVie", TAK: "Takeda", MULTI: "Cross-company", INDUSTRY: "Industry", METHODOLOGY: "Methodology" };
export const COMPANY_COLORS: Record<string, string> = { LLY: "#0F766E", JNJ: "#1D4ED8", ABBV: "#7C3AED", TAK: "#E60012", MULTI: "#6B7280", INDUSTRY: "#6B7280", METHODOLOGY: "#6B7280" };
export const MATURITY_ORDER = ["CONCEPT", "PROTOTYPE", "PILOT", "OPERATIONAL", "SCALED", "DEMONSTRATED_OUTCOME"];
export const BASELINE_CLASSES = ["EXISTING_STRENGTH", "EXISTING_BUT_UNDERDEVELOPED", "EVIDENCE_GAP", "POTENTIAL_NEW_CAPABILITY"];
export const fmtMoney = (v: number, unit?: string | null) => {
  if (unit === "percent") return `${v}%`;
  if (unit === "count") return v.toLocaleString();
  if (unit === "JPY_billions") return `¥${v.toLocaleString(undefined, { maximumFractionDigits: 1 })}bn`;
  if (unit === "JPY_millions") return `¥${(v / 1000).toLocaleString(undefined, { maximumFractionDigits: 1 })}bn`;
  if (unit === "USD_millions") return v >= 1000 ? `$${(v / 1000).toLocaleString(undefined, { maximumFractionDigits: 1 })}bn` : `$${v.toLocaleString(undefined, { maximumFractionDigits: 0 })}m`;
  if (unit && unit.endsWith("/shares")) return `$${v.toFixed(2)}`;
  return v.toLocaleString();
};
export const fmtUsdM = (v: number) => (v >= 1000 ? `$${(v / 1000).toLocaleString(undefined, { maximumFractionDigits: 1 })}bn` : `$${v.toLocaleString(undefined, { maximumFractionDigits: 0 })}m`);
export const uniq = <T,>(a: T[]) => Array.from(new Set(a));
/** Strategy file accessor: returns undefined if the file is absent. */
export function strat<T = any>(b: Bundle, name: string): T | undefined {
  const f = b.strategy.files[name];
  return f && f.available ? (f.data as T) : undefined;
}
export const STRATEGY_ABSENT = "Strategy module not yet produced — see PROJECT_STATE.md";
/** Decimal-ish year from labels such as 2024-07-02, 2024-07, 2024, FY2023. */
export function yearFrac(s: string): number | null {
  const m = s.match(/(20\d\d)(?:-(\d\d))?(?:-(\d\d))?/);
  if (!m) return null;
  return +m[1] + (m[2] ? (+m[2] - 1) / 12 : 0.5) + (m[3] ? (+m[3] - 1) / 365 : 0);
}
