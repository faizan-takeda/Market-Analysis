// Views 7, 8, 12 and the research graph: Encyclopedia, What Takeda Can Learn, Evidence & Uncertainty, Research graph
import { useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { Bundle, Claim, BASELINE_CLASSES, COMPANY_NAMES, STRATEGY_ABSENT, strat, uniq } from "./data";
import { Absent, ClaimCard, CoTag, Dag, Gap, Ids, Open, Scroll, SourcePanel } from "./components";
import { ClaimLine } from "./views_a";

const pretty = (s: string) => s.replace(/_/g, " ").toLowerCase();
const yearsIn = (c: Claim) => uniq(((c.event_date ?? "") + " " + (c.reporting_period ?? "")).match(/20\d\d/g) ?? []);

function Sel({ label, value, set, options, fmt }: { label: string; value: string; set: (v: string) => void; options: string[]; fmt?: (v: string) => string }) {
  return <label className="sel">{label}<select value={value} onChange={(e) => set(e.target.value)}><option value="all">all</option>{options.map((o) => <option key={o} value={o}>{fmt ? fmt(o) : o}</option>)}</select></label>;
}

export function Encyclopedia({ b, open }: { b: Bundle; open: Open }) {
  const [sp0] = useSearchParams(); const [q, setQ] = useState(sp0.get("q") ?? ""); const [co, setCo] = useState("all"); const [dom, setDom] = useState("all"); const [kind, setKind] = useState("all"); const [status, setStatus] = useState("all");
  const [tier, setTier] = useState("all"); const [year, setYear] = useState("all"); const [mat, setMat] = useState("all"); const [shard, setShard] = useState("all");
  const [flag, setFlag] = useState<"all" | "contrary" | "single">("all"); const [mode, setMode] = useState<"claims" | "sources">("claims"); const [limit, setLimit] = useState(60);
  const hits = useMemo(() => {
    const terms = q.toLowerCase().split(/\s+/).filter((t) => t.length > 2);
    const sets: Set<string>[] = terms.map((t) => { const s = new Set<string>(); for (const [tok, list] of Object.entries(b.index)) if (tok.includes(t)) for (const x of list) s.add(x); return s; });
    if (!sets.length) return null;
    const out = new Set<string>(); sets[0].forEach((x) => { if (sets.every((s) => s.has(x))) out.add(x); }); return out;
  }, [q, b]);
  const opts = useMemo(() => ({
    dom: uniq(b.claims.flatMap((c) => c.domains ?? [])).sort(), year: uniq(b.claims.flatMap(yearsIn)).sort(), mat: uniq(b.claims.map((c) => c.maturity ?? "").filter(Boolean)).sort(),
    shard: uniq(b.claims.map((c) => c.merged_from_shard ?? "canonical")).sort(), status: uniq(b.claims.map((c) => c.status)).sort(), kind: uniq(b.claims.map((c) => c.kind)).sort(), tier: uniq(b.sources.map((s) => s.credibility_tier)).sort(),
  }), [b]);
  const claims = b.claims.filter((c) => (!hits || hits.has(c.claim_id)) && (co === "all" || c.companies.includes(co as any)) && (dom === "all" || (c.domains ?? []).includes(dom)) && (kind === "all" || c.kind === kind) && (status === "all" || c.status === status)
    && (year === "all" || yearsIn(c).includes(year)) && (mat === "all" || c.maturity === mat) && (shard === "all" || (c.merged_from_shard ?? "canonical") === shard)
    && (flag === "all" || (flag === "contrary" ? !!c.contrary_evidence?.length : !!c.single_interested_source)) && (tier === "all" || c.supporting_sources.some((s) => b.sourceById.get(s.source_id)?.credibility_tier === tier)));
  const sources = b.sources.filter((s) => (!hits || hits.has(s.source_id)) && (co === "all" || s.company === co) && (tier === "all" || s.credibility_tier === tier) && (year === "all" || ((s.published_at ?? "") + (s.reporting_period ?? "")).includes(year)));
  return (
    <>
      <div className="eyebrow">View 7 · The Research Encyclopedia</div>
      <h1>Search every claim and source</h1>
      <p className="lede">Claim → sources → original URL and locator, and source → claims. Free text matches statements, entities, domains, report paths, source titles and IDs.</p>
      <div className="toolbar"><input placeholder="search, e.g. Skyrizi, capex, OTTAVA, Vyvanse, or a claim ID" value={q} onChange={(e) => { setQ(e.target.value); setLimit(60); }} aria-label="search the encyclopedia" style={{ flex: "1 1 280px" }} /></div>
      <div className="toolbar filters">
        <Sel label="company" value={co} set={setCo} options={Object.keys(COMPANY_NAMES)} fmt={(v) => COMPANY_NAMES[v]} />
        <Sel label="domain" value={dom} set={setDom} options={opts.dom} fmt={pretty} />
        <Sel label="year" value={year} set={setYear} options={opts.year} />
        <Sel label="kind" value={kind} set={setKind} options={opts.kind} />
        <Sel label="status" value={status} set={setStatus} options={opts.status} fmt={pretty} />
        <Sel label="source tier" value={tier} set={setTier} options={opts.tier} fmt={(v) => v.replace(/_/g, " ")} />
        <Sel label="maturity" value={mat} set={setMat} options={opts.mat} fmt={pretty} />
        <Sel label="shard" value={shard} set={setShard} options={opts.shard} />
      </div>
      <div className="toolbar">
        <div className="chips" role="group" aria-label="flags">
          <button className={`chip ${flag === "all" ? "on" : ""}`} aria-pressed={flag === "all"} onClick={() => setFlag("all")}>any evidence profile</button>
          <button className={`chip ${flag === "contrary" ? "on" : ""}`} aria-pressed={flag === "contrary"} onClick={() => setFlag("contrary")}>has contrary evidence</button>
          <button className={`chip ${flag === "single" ? "on" : ""}`} aria-pressed={flag === "single"} onClick={() => setFlag("single")}>single interested source</button>
        </div>
        <div className="chips" role="group" aria-label="mode">
          <button className={`chip ${mode === "claims" ? "on" : ""}`} aria-pressed={mode === "claims"} onClick={() => setMode("claims")}>claims ({claims.length})</button>
          <button className={`chip ${mode === "sources" ? "on" : ""}`} aria-pressed={mode === "sources"} onClick={() => setMode("sources")}>sources ({sources.length})</button>
        </div>
      </div>
      {mode === "claims" ? claims.slice(0, limit).map((c) => <ClaimCard key={c.claim_id} c={c} b={b} onOpen={open} />) : sources.slice(0, limit).map((s) => <SourcePanel key={s.source_id} s={s} b={b} onOpen={open} />)}
      {(mode === "claims" ? claims.length : sources.length) > limit ? <button className="chip" onClick={() => setLimit(limit + 100)}>show 100 more ({(mode === "claims" ? claims.length : sources.length) - limit} remaining)</button> : null}
      {(mode === "claims" ? claims.length : sources.length) === 0 ? <Gap>Nothing matches these filters.</Gap> : null}
    </>
  );
}

const CLASS_TONE: Record<string, string> = { EXISTING_STRENGTH: "ok", EXISTING_BUT_UNDERDEVELOPED: "mid", EVIDENCE_GAP: "gap", POTENTIAL_NEW_CAPABILITY: "new", OTHER: "oth" };

export function TakedaLearn({ b, open }: { b: Bundle; open: Open }) {
  const t = b.takeda; const [ivb, setIvb] = useState<string | null>(null);
  const lessons = strat<{ lessons: any[] }>(b, "takeda_lessons")?.lessons;
  const tak = b.claims.filter((c) => c.companies.includes("TAK") && c.run_id !== "RUN-0001-sec-ingest");
  const classes = [...BASELINE_CLASSES, "OTHER"];
  if (!t.available) return <><div className="eyebrow">View 8 · What Takeda Can Learn</div><h1>Takeda baseline</h1><Absent what={t.reason ?? "Takeda baseline files not found."} file="New_mediciine/companies/takeda_public_baseline/" /></>;
  return (
    <>
      <div className="eyebrow">View 8 · What Takeda Can Learn</div>
      <h1>Takeda's public baseline, classified by evidence</h1>
      <p className="lede">Each capability area is classified from public sources only. “Evidence gap” means no public evidence was found; it is not a finding that the capability is missing. Items that need non-public information sit in the internal-validation backlog.</p>
      <div className="classes">
        {classes.map((cl) => { const rows = t.capabilities.filter((c) => c.class === cl); return (
          <section key={cl} className={`class ${CLASS_TONE[cl]}`} aria-label={pretty(cl)}>
            <h3>{pretty(cl === "OTHER" ? "other / exited" : cl)} <small>{rows.length}</small></h3>
            {rows.length ? rows.map((r) => <div key={r.area} className="cap"><b>{r.area}</b>{r.class_raw !== r.class ? <div className="meta">{r.class_raw}</div> : null}<Ids ids={r.claim_ids} open={open} />{r.ivb_refs.map((i) => <button key={i} className={`chip id ${ivb === i ? "on" : ""}`} onClick={() => setIvb(ivb === i ? null : i)} title="Highlight in the validation backlog">{i}</button>)}</div>) : <p className="meta">none</p>}
          </section>); })}
      </div>
      <h2 style={{ marginTop: 32 }}>Internal-validation backlog</h2>
      <p className="meta">Decisions that depend on these items stay labelled as assumptions until Takeda confirms them.</p>
      <Scroll><table><thead><tr><th>ID</th><th>Question</th><th>Why it matters</th><th>Owner</th><th>Evidence</th></tr></thead><tbody>
        {t.backlog.map((r) => <tr key={r.id} className={ivb === r.id ? "hl" : ""}><td className="num">{r.id}</td><td>{r.question}</td><td>{r.why}</td><td>{r.owner}</td><td><Ids ids={r.claim_ids} open={open} /></td></tr>)}</tbody></table></Scroll>
      <h2 style={{ marginTop: 32 }}>Lessons from competitors</h2>
      {!lessons ? <Absent kind="strategy" what="Transferability lessons (what each competitor did, and whether it transfers to Takeda) are produced by the strategy team." file="strategy/data/takeda_lessons.json" /> : (
        <div className="lessons">{lessons.map((l) => <article key={l.id} className="lesson"><div><span className="tag">{l.area}</span>{l.competitor ? <CoTag co={l.competitor} /> : null}<span className={`tag xfer ${l.transferability}`}>{pretty(l.transferability ?? "")}</span></div>
          <p>{l.what_they_did}</p><p className="meta"><b>Why:</b> {l.why}</p><p className="meta">Takeda baseline: {l.takeda_baseline_class ?? "n/a"}{l.internal_validation ? ` · needs ${l.internal_validation}` : ""}</p>
          <Ids ids={l.evidence_claim_ids ?? []} open={open} label="competitor evidence" /><Ids ids={l.takeda_claim_ids ?? []} open={open} label="Takeda evidence" /></article>)}</div>)}
      <details style={{ marginTop: 24 }}><summary>All {tak.length} Takeda claims in the registry</summary>{tak.map((c) => <ClaimLine key={c.claim_id} c={c} open={open} />)}</details>
    </>
  );
}

export function Uncertainty({ b, open }: { b: Bundle; open: Open }) {
  const [lens, setLens] = useState<"contrary" | "single" | "weak" | "nonfact">("contrary");
  const lists = {
    contrary: b.claims.filter((c) => c.contrary_evidence?.length), single: b.claims.filter((c) => c.single_interested_source),
    weak: b.claims.filter((c) => c.status !== "SUPPORTED"), nonfact: b.claims.filter((c) => c.kind !== "FACT"),
  };
  const cov = b.coverage.rows; const st = (s: string) => cov.filter((r) => r.status === s).length;
  const ca = strat<{ items: any[] }>(b, "counterarguments")?.items; const sc = strat<any>(b, "scenarios"); const cr = strat<any>(b, "council_reviews");
  const types = ca ? uniq(ca.map((i) => i.type)) : [];
  const tone = (v: string) => (v === "robust" || v === "support" ? "ok" : v === "fragile" || v === "oppose" ? "bad" : v === "option_value" || v === "conditional" ? "mid" : "oth");
  const scn: string[] = sc?.scenarios?.map((s: any) => s.id) ?? [];
  return (
    <>
      <div className="eyebrow">View 12 · Evidence, Uncertainty and Counterarguments</div>
      <h1>Why we could be wrong</h1>
      <dl className="kpis">
        <div><dt>claims with contrary evidence</dt><dd>{lists.contrary.length}</dd></div>
        <div><dt>single interested source</dt><dd>{lists.single.length}</dd></div>
        <div><dt>not fully supported</dt><dd>{lists.weak.length}</dd></div>
        <div><dt>interpretations, hypotheses, recommendations</dt><dd>{lists.nonfact.length}</dd></div>
        <div><dt>source families fully reviewed</dt><dd>{st("reviewed")}/{cov.length}</dd></div>
      </dl>
      <h2>Counterarguments to the strategy</h2>
      {!ca ? <Absent kind="strategy" what="Counterarguments (unsupported assumptions, unresolved questions, conflicting sources, public-knowledge gaps, failed hypotheses) are produced with the strategy." file="strategy/data/counterarguments.json" /> : (
        types.map((tp) => <section key={tp} className="ca-group"><h3>{pretty(tp)}</h3>{ca.filter((i) => i.type === tp).map((i) => <div key={i.id} className="ca"><span className="src">{i.id} → {i.target}</span><p>{i.text}</p><Ids ids={i.claim_ids ?? []} open={open} />{(i.assumption_ids ?? []).map((a: string) => <span key={a} className="tag HYPOTHESIS">{a}</span>)}</div>)}</section>))}
      <h2 style={{ marginTop: 28 }}>Scenario robustness</h2>
      {!sc ? <Absent kind="strategy" what="Scenario definitions and the robustness of each bet under them." file="strategy/data/scenarios.json" /> : <>
        <Scroll><table className="matrix"><thead><tr><th>Bet</th>{scn.map((s) => <th key={s} title={sc.scenarios.find((x: any) => x.id === s)?.name}>{s}</th>)}<th>Rationale</th></tr></thead><tbody>
          {(sc.robustness ?? []).map((r: any) => <tr key={r.bet_id}><td><b>{r.bet_id}</b></td>{scn.map((s) => <td key={s}><span className={`cell ${tone(r[s])}`}>{pretty(r[s] ?? "n/a")}</span></td>)}<td>{r.rationale}</td></tr>)}</tbody></table></Scroll>
        <div className="legend">{sc.scenarios.map((s: any) => <span key={s.id}><b>{s.id}</b> {s.name}</span>)}</div></>}
      <h2 style={{ marginTop: 28 }}>Council reviews and disagreements</h2>
      {!cr ? <Absent kind="strategy" what="Council verdicts per bet and unresolved disagreements." file="strategy/data/council_reviews.json" /> : <>
        <Scroll><table className="matrix"><thead><tr><th>Bet</th><th>Council</th><th>Verdict</th><th>Rationale</th><th>Unresolved</th><th>Evidence</th></tr></thead><tbody>
          {(cr.reviews ?? []).map((r: any, i: number) => <tr key={i}><td><b>{r.bet_id}</b></td><td>{pretty(r.council)}</td><td><span className={`cell ${tone(r.verdict)}`}>{r.verdict}</span></td><td>{r.rationale}</td><td>{r.unresolved}</td><td><Ids ids={r.claim_ids ?? []} open={open} /></td></tr>)}</tbody></table></Scroll>
        {(cr.disagreements ?? []).map((d: any, i: number) => <p key={i} className="contrary"><b>{d.bet_id}:</b> {d.text}</p>)}</>}
      <h2 style={{ marginTop: 28 }}>Registry evidence profile</h2>
      <div className="toolbar"><div className="chips" role="group" aria-label="evidence profile">
        {(["contrary", "single", "weak", "nonfact"] as const).map((k) => <button key={k} className={`chip ${lens === k ? "on" : ""}`} aria-pressed={lens === k} onClick={() => setLens(k)}>{{ contrary: "contrary evidence", single: "single interested source", weak: "not fully supported", nonfact: "not a fact" }[k]} ({lists[k].length})</button>)}</div></div>
      {lists[lens].slice(0, 40).map((c) => <ClaimCard key={c.claim_id} c={c} b={b} onOpen={open} />)}
      {lists[lens].length > 40 ? <p className="meta">First 40 of {lists[lens].length}; filter the rest in the Encyclopedia.</p> : null}
      <h2 style={{ marginTop: 28 }}>Recorded conflicts and status adjustments</h2>
      {!b.conflicts.items.length ? <Gap>No conflicts file entries yet.</Gap> : <Scroll><table><thead><tr><th>Type</th><th>Claim</th><th>Change</th><th>Reason</th><th>By</th></tr></thead><tbody>
        {b.conflicts.items.map((c, i) => <tr key={i}><td>{pretty(String(c.type ?? ""))}</td><td>{c.claim_id ? <Ids ids={[c.claim_id]} open={open} /> : ""}</td><td>{c.from ? `${c.from} → ${c.to}` : ""}</td><td>{c.reason ?? c.text ?? ""}</td><td className="src">{c.by ?? ""}</td></tr>)}</tbody></table></Scroll>}
      <h2 style={{ marginTop: 28 }}>Research coverage ledger</h2>
      <Scroll><table><thead><tr><th>Company</th><th>Source family</th><th>Status</th><th>Found / reviewed</th><th>Open gap</th></tr></thead><tbody>
        {cov.map((r, i) => <tr key={i}><td><CoTag co={r.company} /></td><td>{r.family}</td><td><span className={`tag ${r.status === "reviewed" ? "SUPPORTED" : r.status === "not_started" ? "CONTRADICTED" : "PARTIALLY_SUPPORTED"}`}>{r.status.replace(/_/g, " ")}</span></td><td className="num">{r.discovered} / {r.reviewed}</td><td style={{ fontSize: "0.85rem" }}>{r.gap ?? r.notes ?? ""}</td></tr>)}</tbody></table></Scroll>
      <h2 style={{ marginTop: 28 }}>Known methodological caveats</h2>
      <ul>
        <li>XBRL values are as tagged by registrants; where a year's value came from a later filing's comparative, the claim says so (possible recast).</li>
        <li>J&J earlier-year figures include Consumer Health; a step across the separation mixes perimeter and performance.</li>
        <li>Takeda's latest-year XBRL facts were not available from the SEC API; headline values were extracted from the 20-F text.</li>
        <li>Press releases establish announcements, not outcomes; maturity above “concept” needs non-company evidence.</li>
        <li>Multiple agent shards were merged into one registry; the shard of origin is shown on each claim and can be filtered in View 7.</li>
        <li>Strategy files, when present, are validated against the registry for IDs only; their content is analysis, not fact. When absent the strategy views say: {STRATEGY_ABSENT}.</li>
      </ul>
    </>
  );
}

export function ResearchGraph({ b }: { b: Bundle }) {
  const color: Record<string, string> = { done: "#0f6b3d", active: "#C5000F", pending: "#9aa3b2" };
  const counts = b.rg.nodes.reduce<Record<string, number>>((m, n) => ({ ...m, [n.status]: (m[n.status] ?? 0) + 1 }), {});
  const [sel, setSel] = useState<string | null>(null); const n = b.rg.nodes.find((x) => x.id === sel);
  return (
    <>
      <div className="eyebrow">Research graph</div>
      <h1>How the research is organised and where it stands</h1>
      <p className="lede">The workflow graph from the research methodology, coloured by node status. Arrows run from prerequisite to dependent step.</p>
      <div className="legend" style={{ marginBottom: 10 }}>{Object.keys(color).map((k) => <span key={k}><i style={{ background: color[k] }} />{k} ({counts[k] ?? 0})</span>)}</div>
      <div className="panel" style={{ padding: 8 }}><Dag nodes={b.rg.nodes.map((x) => ({ id: x.id, label: x.label, sub: x.status, color: color[x.status] ?? "#9aa3b2" }))} edges={b.rg.edges} selected={sel} onSelect={setSel} /></div>
      {n ? <p className="panel" aria-live="polite"><b>{n.label}</b> — status: {n.status}. Predecessors: {b.rg.edges.filter((e) => e.target === n.id).map((e) => e.source).join(", ") || "none"}; successors: {b.rg.edges.filter((e) => e.source === n.id).map((e) => e.target).join(", ") || "none"}.</p> : null}
    </>
  );
}
