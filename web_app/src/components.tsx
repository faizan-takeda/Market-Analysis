import { useEffect, useRef, useState } from "react";
import * as d3 from "d3";
import { Bundle, Claim, Source, COMPANY_COLORS, COMPANY_NAMES, fmtMoney, STRATEGY_ABSENT } from "./data";

export type Open = (id: string) => void;

export function useWidth(initial = 800): [React.RefObject<HTMLDivElement>, number] {
  const ref = useRef<HTMLDivElement>(null);
  const [w, setW] = useState(initial);
  useEffect(() => {
    const el = ref.current; if (!el) return;
    const ro = new ResizeObserver(() => setW(Math.max(280, el.clientWidth))); ro.observe(el); setW(Math.max(280, el.clientWidth));
    return () => ro.disconnect();
  }, []);
  return [ref, w];
}

export function CoTag({ co }: { co: string }) {
  return <span className="tag co" style={{ background: COMPANY_COLORS[co] ?? "#555" }}>{COMPANY_NAMES[co] ?? co}</span>;
}

export function SourceLink({ s, locator }: { s: Source | undefined; locator?: string }) {
  if (!s) return <span className="src">unknown source</span>;
  return (
    <span className="src">
      <a href={s.canonical_url} target="_blank" rel="noreferrer" title={s.title}>{s.source_id}</a> · {s.publisher}{s.published_at ? ` · ${s.published_at}` : ""} · {s.credibility_tier.replace(/_/g, " ")}
      {locator ? <><br />↳ {locator}</> : null}
    </span>
  );
}

/** Row of claim-id buttons that open the evidence drawer. */
export function Ids({ ids, open, label }: { ids: string[]; open: Open; label?: string }) {
  if (!ids || !ids.length) return null;
  return <span className="ids">{label ? <span className="meta">{label} </span> : null}{ids.map((id) => <button key={id} className="chip id" onClick={() => open(id)} title={`Open evidence for ${id}`}>{id.replace("CLM-", "")}</button>)}</span>;
}

export function Badges({ c }: { c: Claim }) {
  return (<>
    {c.contrary_evidence && c.contrary_evidence.length ? <span className="tag warnb" title="The registry records contrary or restating evidence for this claim">contrary evidence</span> : null}
    {c.single_interested_source ? <span className="tag warnb" title="Only the company itself supports this claim">single interested source</span> : null}
  </>);
}

export function ClaimCard({ c, b, onOpen }: { c: Claim; b: Bundle; onOpen?: Open }) {
  return (
    <article className="claim" style={{ borderLeftColor: COMPANY_COLORS[c.companies[0]] ?? "#999" }}>
      <div>
        {c.companies.map((co) => <CoTag key={co} co={co} />)}
        <span className={`tag ${c.kind}`}>{c.kind}</span>
        <span className={`tag ${c.status}`}>{c.status.replace(/_/g, " ")}</span>
        {c.maturity ? <span className="tag">maturity: {c.maturity}</span> : null}
        <Badges c={c} />
        <span className="src" style={{ float: "right" }}>{c.claim_id}</span>
      </div>
      <p>{c.statement}</p>
      <div className="meta">
        {c.value != null && typeof c.value === "number" ? <b>{fmtMoney(c.value, c.unit)} </b> : null}
        {c.reporting_period ? `${c.reporting_period} · ` : ""}{c.event_date ? `${c.event_date} · ` : ""}{c.basis ? `${c.basis} · ` : ""}verified {c.last_verified}{c.merged_from_shard ? ` · shard ${c.merged_from_shard}` : ""}
      </div>
      {c.contrary_evidence && c.contrary_evidence.length ? <div className="contrary"><b>Contrary / restating evidence:</b> {c.contrary_evidence.join(" · ")}</div> : null}
      {c.supporting_sources.map((ss, i) => <div key={i}><SourceLink s={b.sourceById.get(ss.source_id)} locator={ss.locator} /></div>)}
      {c.independent_corroboration && c.independent_corroboration.length ? <div className="src">independent corroboration: {c.independent_corroboration.join(", ")}</div> : null}
      {c.implications ? <div className="impl"><b>Implication (analyst, not fact):</b> {c.implications}</div> : null}
      {c.confidence_rationale ? <div className="meta" style={{ marginTop: 6 }}>Rationale: {c.confidence_rationale}</div> : null}
      {onOpen ? <div style={{ marginTop: 6 }}><button className="chip" onClick={() => onOpen(c.claim_id)}>Open evidence</button></div> : null}
    </article>
  );
}

export function EvidenceDrawer({ id, b, onClose, onOpen }: { id: string | null; b: Bundle; onClose: () => void; onOpen: Open }) {
  const btn = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    if (!id) return;
    const prev = document.activeElement as HTMLElement | null;
    btn.current?.focus();
    const k = (e: KeyboardEvent) => { if (e.key === "Escape") onClose(); };
    window.addEventListener("keydown", k);
    return () => { window.removeEventListener("keydown", k); prev?.focus?.(); };
  }, [id, onClose]);
  if (!id) return null;
  const c = b.claimById.get(id);
  const s = b.sourceById.get(id);
  return (
    <aside className="drawer" role="dialog" aria-modal="false" aria-label="Evidence trail">
      <button ref={btn} className="close" onClick={onClose} aria-label="Close evidence drawer (Escape)">×</button>
      <div className="eyebrow">Evidence trail · {id}</div>
      {c ? (<>
        <ClaimCard c={c} b={b} />
        <h3>Sources behind this claim</h3>
        {c.supporting_sources.map((ss) => { const src = b.sourceById.get(ss.source_id); return src ? <SourcePanel key={ss.source_id} s={src} b={b} onOpen={onOpen} /> : null; })}
      </>) : s ? <SourcePanel s={s} b={b} onOpen={onOpen} /> : <p>Unknown id {id}</p>}
    </aside>
  );
}

export function SourcePanel({ s, b, onOpen }: { s: Source; b: Bundle; onOpen?: Open }) {
  const claims = b.claims.filter((c) => c.supporting_sources.some((x) => x.source_id === s.source_id));
  return (
    <div className="panel" style={{ marginBottom: 12 }}>
      <div><CoTag co={s.company} /><span className="tag">{s.source_type.replace(/_/g, " ")}</span><span className="tag">{s.credibility_tier.replace(/_/g, " ")}</span><span className="tag">{s.access_status}</span></div>
      <h3 style={{ marginTop: 8 }}>{s.title}</h3>
      <div className="meta src">{s.source_id} · {s.publisher}{s.published_at ? ` · published ${s.published_at}` : ""} · retrieved {s.retrieved_at.slice(0, 10)}</div>
      <p><a href={s.canonical_url} target="_blank" rel="noreferrer">Open original ↗</a>{s.identifiers?.accession_number ? <span className="src"> · accession {s.identifiers.accession_number}</span> : null}</p>
      {s.local_extracted_text_path ? <p className="src">local text: {s.local_extracted_text_path}</p> : null}
      {s.limitations ? <p className="meta">Limitations: {s.limitations}</p> : null}
      <p className="meta">{claims.length} claim(s) rest on this source.</p>
      {onOpen && claims.length ? <details><summary>Show claims from this source</summary><Ids ids={claims.slice(0, 80).map((c) => c.claim_id)} open={onOpen} />{claims.length > 80 ? <span className="meta"> (+{claims.length - 80} more)</span> : null}</details> : null}
    </div>
  );
}

export function Gap({ children }: { children: React.ReactNode }) {
  return <div className="notice gap" role="note"><b>Not yet researched / evidence gap.</b> {children}</div>;
}
export function Scenario({ children }: { children: React.ReactNode }) {
  return <div className="notice" role="note"><b>Scenario / simulated values — not reported facts.</b> {children}</div>;
}
/** Explicit absent-data notice. kind="strategy" uses the contract wording. */
export function Absent({ what, kind, file }: { what: string; kind?: "strategy" | "research"; file?: string }) {
  return <div className="notice absent" role="status"><b>{kind === "strategy" ? STRATEGY_ABSENT : "Not yet produced."}</b> {what}{file ? <span className="src"> · expected: {file}</span> : null}</div>;
}
export const Simulated = () => <span className="tag SCENARIO" title="Scenario value; not a reported fact">SIMULATED</span>;
export const Assumption = ({ id }: { id?: string }) => <span className="tag HYPOTHESIS" title="Explicit scenario assumption">ASSUMPTION{id ? ` ${id}` : ""}</span>;

export function Scroll({ children }: { children: React.ReactNode }) { return <div className="scroll" tabIndex={0} role="region" aria-label="Scrollable table">{children}</div>; }

/** Multi-series line chart. series: {key, color, points:[x,y]} */
export function LineChart({ series, height = 300, yLabel, xTicks }: { series: { key: string; color: string; points: [number, number][] }[]; height?: number; yLabel?: string; xTicks?: number[] }) {
  const ref = useRef<SVGSVGElement>(null);
  const [wrap, w] = useWidth(640);
  useEffect(() => {
    const svg = d3.select(ref.current); svg.selectAll("*").remove();
    const m = { t: 16, r: 90, b: 34, l: 56 }; const iw = w - m.l - m.r, ih = height - m.t - m.b;
    const xs = series.flatMap((s) => s.points.map((p) => p[0])); const ys = series.flatMap((s) => s.points.map((p) => p[1]));
    if (!xs.length) return;
    const x = d3.scaleLinear().domain(d3.extent(xs) as [number, number]).range([0, Math.max(40, iw)]);
    const y = d3.scaleLinear().domain([Math.min(0, d3.min(ys) ?? 0), (d3.max(ys) ?? 1) * 1.08]).nice().range([ih, 0]);
    const g = svg.attr("viewBox", `0 0 ${w} ${height}`).append("g").attr("transform", `translate(${m.l},${m.t})`);
    g.append("g").attr("class", "axis").attr("transform", `translate(0,${ih})`).call(d3.axisBottom(x).tickValues(xTicks ?? Array.from(new Set(xs))).tickFormat((d) => String(d)));
    g.append("g").attr("class", "axis").call(d3.axisLeft(y).ticks(5).tickFormat((d) => d3.format("~s")(d as number)));
    g.append("g").attr("class", "axis").selectAll("line").data(y.ticks(5)).join("line").attr("x1", 0).attr("x2", iw).attr("y1", (d) => y(d)).attr("y2", (d) => y(d)).attr("stroke", "#eef0f4");
    if (yLabel) g.append("text").attr("x", -m.l + 4).attr("y", -4).attr("fill", "#6b7384").attr("font-size", 11).text(yLabel);
    const line = d3.line<[number, number]>().x((d) => x(d[0])).y((d) => y(d[1])).curve(d3.curveMonotoneX);
    for (const s of series) {
      const pts = [...s.points].sort((a, b) => a[0] - b[0]);
      g.append("path").datum(pts).attr("fill", "none").attr("stroke", s.color).attr("stroke-width", 2.2).attr("d", line);
      g.selectAll(null).data(pts).join("circle").attr("cx", (d) => x(d[0])).attr("cy", (d) => y(d[1])).attr("r", 3.2).attr("fill", s.color).append("title").text((d) => `${s.key}: ${d3.format(",.1f")(d[1])} (${d[0]})`);
      const last = pts[pts.length - 1];
      g.append("text").attr("x", x(last[0]) + 6).attr("y", y(last[1]) + 4).attr("fill", s.color).attr("font-size", 11).attr("font-weight", 600).text(s.key.length > 14 ? s.key.slice(0, 13) + "…" : s.key);
    }
  }, [series, w, height, yLabel, xTicks]);
  return <div ref={wrap}><svg ref={ref} width="100%" height={height} role="img" aria-label={yLabel ?? "chart"} /></div>;
}

/** Small-multiple bar chart; bars are focusable and open evidence. */
export function MiniBars({ data, color, height = 90, fmt, open }: { data: { label: string; value: number; claim_id?: string }[]; color: string; height?: number; fmt: (v: number) => string; open?: Open }) {
  const [wrap, w] = useWidth(240);
  if (!data.length) return <div className="meta">no data</div>;
  const max = Math.max(...data.map((d) => Math.abs(d.value)), 1e-9); const bw = Math.max(8, (w - 8) / data.length - 6);
  return (
    <div ref={wrap}>
      <svg width="100%" height={height + 30} viewBox={`0 0 ${w} ${height + 30}`} role="img" aria-label="bar series">
        {data.map((d, i) => { const h = Math.max(1, (Math.abs(d.value) / max) * height); const x = 4 + i * (bw + 6);
          return (<g key={d.label} tabIndex={d.claim_id ? 0 : -1} role={d.claim_id ? "button" : undefined} aria-label={`${d.label} ${fmt(d.value)}`} style={{ cursor: d.claim_id ? "pointer" : "default" }}
            onClick={() => d.claim_id && open?.(d.claim_id)} onKeyDown={(e) => { if (d.claim_id && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); open?.(d.claim_id); } }}>
            <title>{`${d.label}: ${fmt(d.value)}`}</title>
            <rect x={x} y={height - h + 14} width={bw} height={h} fill={color} opacity={i === data.length - 1 ? 1 : 0.55} rx={1.5} />
            <text x={x + bw / 2} y={height + 26} textAnchor="middle" fontSize={9} fill="#6b7384">{d.label.replace("FY", "")}</text>
            {(i === 0 || i === data.length - 1) ? <text x={x + bw / 2} y={height - h + 10} textAnchor="middle" fontSize={9.5} fill="#3b4452" fontWeight={600}>{fmt(d.value)}</text> : null}
          </g>); })}
      </svg>
    </div>
  );
}

export interface SwimItem { lane: string; t: number; label: string; claim_ids: string[]; color?: string; shape?: "dot" | "diamond" | "cross" }
/** Swim-lane time strip. Items sharing a lane/time are stacked. Each item is keyboard-focusable. */
export function Swim({ lanes, items, open, domain, laneH = 54 }: { lanes: { key: string; label: string; color: string }[]; items: SwimItem[]; open: Open; domain?: [number, number]; laneH?: number }) {
  const [wrap, w] = useWidth(800);
  const ts = items.map((i) => i.t); if (!ts.length) return <div className="meta">no dated items</div>;
  const [t0, t1] = domain ?? [Math.floor(Math.min(...ts)), Math.ceil(Math.max(...ts)) + 0.001];
  const ml = 84, mr = 16, iw = Math.max(120, w - ml - mr); const x = d3.scaleLinear().domain([t0, t1]).range([0, iw]);
  const years = d3.range(Math.ceil(t0), Math.floor(t1) + 1);
  const stack: Record<string, number> = {}; const pos = items.map((it) => { const k = `${it.lane}|${Math.round(x(it.t) / 11)}`; const n = stack[k] ?? 0; stack[k] = n + 1; return n; });
  const H = lanes.length * laneH + 28;
  return (
    <div ref={wrap} className="swim">
      <svg width="100%" height={H} viewBox={`0 0 ${w} ${H}`} role="group" aria-label="timeline">
        {years.map((y) => <g key={y}><line x1={ml + x(y)} x2={ml + x(y)} y1={14} y2={H - 14} stroke="#eceff4" /><text x={ml + x(y)} y={10} textAnchor="middle" fontSize={10} fill="#6b7384">{y}</text></g>)}
        {lanes.map((l, li) => <g key={l.key}><text x={0} y={22 + li * laneH + laneH / 2} fontSize={11.5} fontWeight={600} fill={l.color}>{l.label}</text><line x1={ml} x2={ml + iw} y1={22 + li * laneH + laneH / 2} y2={22 + li * laneH + laneH / 2} stroke="#dfe3ea" /></g>)}
        {items.map((it, i) => { const li = lanes.findIndex((l) => l.key === it.lane); if (li < 0) return null; const cx = ml + x(it.t); const cy = 22 + li * laneH + laneH / 2 + (pos[i] % 2 ? 1 : -1) * Math.ceil(pos[i] / 2) * 9; const col = it.color ?? lanes[li].color;
          return (<g key={i} tabIndex={0} role="button" aria-label={it.label} style={{ cursor: "pointer" }} onClick={() => it.claim_ids[0] && open(it.claim_ids[0])} onKeyDown={(e) => { if ((e.key === "Enter" || e.key === " ") && it.claim_ids[0]) { e.preventDefault(); open(it.claim_ids[0]); } }}>
            <title>{it.label}</title>
            {it.shape === "diamond" ? <rect x={cx - 4.5} y={cy - 4.5} width={9} height={9} fill={col} transform={`rotate(45 ${cx} ${cy})`} /> : it.shape === "cross" ? <path d={`M${cx - 4},${cy - 4}L${cx + 4},${cy + 4}M${cx - 4},${cy + 4}L${cx + 4},${cy - 4}`} stroke={col} strokeWidth={2.4} /> : <circle cx={cx} cy={cy} r={4.5} fill={col} />}
          </g>); })}
      </svg>
    </div>
  );
}

export interface DagNode { id: string; label: string; sub?: string; color?: string }
/** Layered directed graph (longest-path layering) with arrowheads; nodes are keyboard-selectable. */
export function Dag({ nodes, edges, selected, onSelect, height }: { nodes: DagNode[]; edges: { source: string; target: string; label?: string }[]; selected?: string | null; onSelect?: (id: string) => void; height?: number }) {
  const [wrap, w] = useWidth(800);
  const ids = new Set(nodes.map((n) => n.id)); const es = edges.filter((e) => ids.has(e.source) && ids.has(e.target) && e.source !== e.target);
  const layer: Record<string, number> = Object.fromEntries(nodes.map((n) => [n.id, 0]));
  for (let it = 0; it < nodes.length; it++) { let ch = false; for (const e of es) if (layer[e.target] < layer[e.source] + 1 && layer[e.source] + 1 <= nodes.length) { layer[e.target] = layer[e.source] + 1; ch = true; } if (!ch) break; }
  const L = Math.max(0, ...Object.values(layer)) + 1; const cols: DagNode[][] = Array.from({ length: L }, () => []); nodes.forEach((n) => cols[layer[n.id]].push(n));
  const nw = Math.max(120, Math.min(190, (w - 20) / L - 30)), nh = 46, gx = Math.max(24, (w - 20 - L * nw) / Math.max(1, L - 1)), gy = 14;
  const maxRows = Math.max(...cols.map((c) => c.length)); const H = height ?? maxRows * (nh + gy) + 20;
  const p: Record<string, { x: number; y: number }> = {};
  cols.forEach((c, ci) => c.forEach((n, ri) => { p[n.id] = { x: 10 + ci * (nw + gx), y: 10 + ri * (nh + gy) + ((maxRows - c.length) * (nh + gy)) / 2 }; }));
  const wrapText = (s: string, n: number) => { const out: string[] = []; let cur = ""; for (const wd of s.split(" ")) { if ((cur + " " + wd).trim().length > n) { out.push(cur); cur = wd; } else cur = (cur + " " + wd).trim(); } if (cur) out.push(cur); return out.slice(0, 2); };
  return (
    <div ref={wrap} className="scroll"><svg width={Math.max(w, L * (nw + 24))} height={H} role="group" aria-label="dependency graph">
      <defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="#6b7384" /></marker></defs>
      {es.map((e, i) => { const a = p[e.source], b2 = p[e.target]; const x1 = a.x + nw, y1 = a.y + nh / 2, x2 = b2.x, y2 = b2.y + nh / 2; const mx = (x1 + x2) / 2;
        return <path key={i} d={`M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2 - 2},${y2}`} fill="none" stroke="#8a93a5" strokeWidth={1.3} markerEnd="url(#arr)"><title>{e.label ?? `${e.source} → ${e.target}`}</title></path>; })}
      {nodes.map((n) => { const q = p[n.id]; const sel = selected === n.id;
        return (<g key={n.id} transform={`translate(${q.x},${q.y})`} tabIndex={onSelect ? 0 : -1} role={onSelect ? "button" : undefined} aria-label={n.label} aria-pressed={sel} style={{ cursor: onSelect ? "pointer" : "default" }}
          onClick={() => onSelect?.(n.id)} onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); onSelect?.(n.id); } }}>
          <title>{`${n.label}${n.sub ? ` — ${n.sub}` : ""}`}</title>
          <rect width={nw} height={nh} rx={6} fill={sel ? "#FFF1F2" : "#fff"} stroke={sel ? "#C5000F" : n.color ?? "#c9cfda"} strokeWidth={sel ? 2 : 1.3} />
          {n.color ? <rect width={4} height={nh} rx={2} fill={n.color} /> : null}
          {wrapText(n.label, Math.floor(nw / 6.4)).map((t, i) => <text key={i} x={12} y={17 + i * 13} fontSize={11} fill="#141a24">{t}</text>)}
          {n.sub ? <text x={12} y={nh - 5} fontSize={9} fill="#6b7384">{n.sub}</text> : null}
        </g>); })}
    </svg></div>
  );
}

/** Force-directed graph. Edge weight (if given) sets stroke width; dashed edges mark terminated/dissolved links. */
export function ForceGraph({ nodes, edges, onEdge, height = 560 }: { nodes: { id: string; type: string; label: string }[]; edges: { source: string; target: string; claims: string[]; weight?: number; dashed?: boolean }[]; onEdge: (e: any) => void; height?: number }) {
  const ref = useRef<SVGSVGElement>(null);
  const [wrap, w] = useWidth(900);
  useEffect(() => {
    const svg = d3.select(ref.current); svg.selectAll("*").remove(); svg.attr("viewBox", `0 0 ${w} ${height}`);
    const ns: any[] = nodes.map((n) => ({ ...n })); const ls: any[] = edges.map((e) => ({ ...e }));
    const wmax = Math.max(1, ...ls.map((l) => l.weight ?? 0)); const sw = d3.scaleSqrt().domain([0, wmax]).range([1.2, 9]);
    const color = (t: string, id: string) => t === "company" ? (COMPANY_COLORS[id] ?? "#333") : t === "technology" ? "#C5000F" : t === "product" ? "#0f6b3d" : t === "deal" ? "#7a4b00" : "#8a8f9c";
    const sim = d3.forceSimulation(ns).force("link", d3.forceLink(ls).id((d: any) => d.id).distance(70)).force("charge", d3.forceManyBody().strength(-160)).force("center", d3.forceCenter(w / 2, height / 2)).force("collide", d3.forceCollide(18));
    const g = svg.append("g");
    const link = g.append("g").selectAll("line").data(ls).join("line").attr("stroke", "#b9c1cf").attr("stroke-dasharray", (d: any) => (d.dashed ? "4 3" : null))
      .attr("stroke-width", (d: any) => (d.weight != null ? sw(d.weight) : Math.min(6, 1 + d.claims.length))).attr("tabindex", 0).attr("role", "button").style("cursor", "pointer")
      .attr("aria-label", (d: any) => `link, ${d.claims.length} claim(s)`).on("click", (_, d) => onEdge(d)).on("keydown", (ev: KeyboardEvent, d) => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); onEdge(d); } });
    link.append("title").text((d: any) => `${d.claims.length} claim(s)${d.weight != null ? `, value ${d.weight} (USD m)` : ""} — click for evidence`);
    const node = g.append("g").selectAll("g").data(ns).join("g").call(d3.drag<any, any>().on("start", (ev, d) => { d.fx = d.x; d.fy = d.y; }).on("drag", (ev, d) => { d.fx = ev.x; d.fy = ev.y; }).on("end", (_, d) => { d.fx = null; d.fy = null; }) as any);
    node.append("circle").attr("r", (d: any) => d.type === "company" ? 16 : 7).attr("fill", (d: any) => color(d.type, d.id)).attr("stroke", "#fff").attr("stroke-width", 1.5);
    node.append("text").text((d: any) => d.label).attr("x", (d: any) => (d.type === "company" ? 20 : 10)).attr("y", 4).attr("font-size", (d: any) => (d.type === "company" ? 13 : 10)).attr("fill", "#3b4452");
    sim.on("tick", () => { link.attr("x1", (d: any) => d.source.x).attr("y1", (d: any) => d.source.y).attr("x2", (d: any) => d.target.x).attr("y2", (d: any) => d.target.y); node.attr("transform", (d: any) => `translate(${d.x},${d.y})`); });
    svg.call(d3.zoom<SVGSVGElement, unknown>().scaleExtent([0.4, 3]).on("zoom", (ev) => g.attr("transform", ev.transform)) as any);
    return () => { sim.stop(); };
  }, [nodes, edges, w, height, onEdge]);
  return <div ref={wrap}><svg ref={ref} width="100%" height={height} role="group" aria-label="Innovation ecosystem graph (links are focusable; an accessible list follows)" /></div>;
}
