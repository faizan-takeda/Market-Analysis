// Report reader: renders any bundled Markdown file. Claim/source ids become evidence chips; relative .md links route inside the app.
import { useEffect, useMemo } from "react";
import { Link, useLocation, useParams, useSearchParams } from "react-router-dom";
import { Bundle, Report, COMPANY_NAMES } from "./data";
import { Open } from "./components";
import { firstParagraph, renderMarkdown, slugify } from "./markdown";
import { pillarOf, PILLARS, sectionLabel } from "./pillars";

export const readPath = (p: string) => `/read/${p}`;
const fmtWords = (n: number) => n.toLocaleString();

/** The markdown body. Click delegation: evidence chips open the drawer; links to files that are not bundled are inert. */
export function MdView({ b, r, open }: { b: Bundle; r: Report; open: Open }) {
  const rendered = useMemo(() => renderMarkdown(r.markdown, r.path, (id) => b.claimById.has(id) || b.sourceById.has(id), (p) => b.reportByPath.has(p)), [b, r]);
  return (
    <div className="md" onClick={(e) => {
      const t = e.target as HTMLElement;
      const chip = t.closest?.("button[data-id]"); if (chip) { open(chip.getAttribute("data-id") as string); return; }
      if (t.closest?.("a[data-missing]")) e.preventDefault();
    }} dangerouslySetInnerHTML={{ __html: rendered.html }} />
  );
}

export function useOutline(b: Bundle, r: Report | undefined) {
  return useMemo(() => (r ? renderMarkdown(r.markdown, r.path, (id) => b.claimById.has(id) || b.sourceById.has(id), (p) => b.reportByPath.has(p)).outline.filter((h) => h.level <= 3) : []), [b, r]);
}

export function ReportMeta({ r }: { r: Report }) {
  return <span className="meta">{fmtWords(r.word_count)} words · {r.claim_ids.length} claim ids · updated {r.updated}</span>;
}

export function ReportCard({ r }: { r: Report }) {
  return (
    <Link className="rcard" to={readPath(r.path)}>
      <span className="rcard-sec">{sectionLabel(r.section)}{r.company !== "MULTI" && r.company !== "INDUSTRY" && r.company !== "METHODOLOGY" ? ` · ${COMPANY_NAMES[r.company] ?? r.company}` : ""}</span>
      <b>{r.title}</b>
      <span className="rcard-ex">{firstParagraph(r.markdown, 180)}</span>
      <ReportMeta r={r} />
      <code className="rcard-path">{r.path}</code>
    </Link>
  );
}

export function ReportGrid({ reports, empty }: { reports: Report[]; empty?: React.ReactNode }) {
  if (!reports.length) return <>{empty ?? null}</>;
  return <div className="rgrid">{reports.map((r) => <ReportCard key={r.path} r={r} />)}</div>;
}

/** Group reports by section label and render each group as a card grid. */
export function GroupedReports({ reports, empty }: { reports: Report[]; empty?: React.ReactNode }) {
  if (!reports.length) return <>{empty ?? null}</>;
  const groups = new Map<string, Report[]>(); reports.forEach((r) => { const k = sectionLabel(r.section); groups.set(k, [...(groups.get(k) ?? []), r]); });
  return <>{Array.from(groups.entries()).map(([k, rs]) => <section key={k} className="rgroup"><h3>{k} <small>{rs.length}</small></h3><ReportGrid reports={rs} /></section>)}</>;
}

/** A report shown inline inside a page, collapsible, with a link to the full reader. */
export function ReportEmbed({ b, r, open, startOpen = true }: { b: Bundle; r: Report; open: Open; startOpen?: boolean }) {
  return (
    <details className="embed" open={startOpen}>
      <summary><span>{r.title}</span><ReportMeta r={r} /><Link to={readPath(r.path)} onClick={(e) => e.stopPropagation()}>Open in reader →</Link></summary>
      <MdView b={b} r={r} open={open} />
    </details>
  );
}

export function Notice({ title, children }: { title: string; children?: React.ReactNode }) {
  return <div className="notice absent" role="status"><b>{title}</b> {children}</div>;
}

export function Reader({ b, open }: { b: Bundle; open: Open }) {
  const params = useParams(); const loc = useLocation(); const [sp] = useSearchParams();
  const path = decodeURI(params["*"] ?? "");
  const r = b.reportByPath.get(path);
  const outline = useOutline(b, r);
  const h = sp.get("h");
  useEffect(() => {
    if (!r) return;
    const el = h ? document.getElementById(h) : null;
    if (el) el.scrollIntoView({ block: "start" }); else window.scrollTo?.(0, 0);
  }, [path, h, r, loc.key]);
  if (!r) return (
    <>
      <div className="eyebrow">Report reader</div>
      <h1>Report not in the bundle</h1>
      <Notice title="Not yet produced.">The file <code>{path || "(no path)"}</code> is not part of the bundled reports. It may not exist yet. Run <code>python3 scripts/build_app_data.py</code> after it is written.</Notice>
      <p><Link to="/reports">Browse all reports</Link></p>
    </>
  );
  const pl = PILLARS.find((x) => x.id === r.pillar) ?? pillarOf("/");
  const siblings = b.reports.reports.filter((x) => x.path !== r.path && x.path.split("/").slice(0, -1).join("/") === r.path.split("/").slice(0, -1).join("/"));
  return (
    <div className="reader">
      <article className="reader-main">
        <div className="eyebrow"><Link to={pl.path}>{pl.label}</Link> › {sectionLabel(r.section)}</div>
        <h1>{r.title}</h1>
        <p className="meta"><ReportMeta r={r} /> · source file <code>{r.path}</code></p>
        <MdView b={b} r={r} open={open} />
        {siblings.length ? <aside className="related"><h3>Other reports in this folder</h3><ul>{siblings.map((s) => <li key={s.path}><Link to={readPath(s.path)}>{s.title}</Link> <span className="meta">{fmtWords(s.word_count)} words</span></li>)}</ul></aside> : null}
      </article>
      <nav className="outline" aria-label="On this page">
        <h4>On this page</h4>
        <ul>{outline.map((o, i) => <li key={i} className={`lv${o.level}`}><a href={`#/read/${r.path}?h=${o.slug}`}>{o.text}</a></li>)}</ul>
        {r.claim_ids.length ? <><h4>Claims cited</h4><div className="ids">{r.claim_ids.slice(0, 40).map((id) => <button key={id} className="idchip" onClick={() => open(id)}>{id.slice(4)}</button>)}{r.claim_ids.length > 40 ? <span className="meta"> +{r.claim_ids.length - 40} more</span> : null}</div></> : null}
      </nav>
    </div>
  );
}
export { slugify };
