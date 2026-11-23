// Grounded Q&A retrieval: in-browser BM25 over claims, report sections and sources (passages from qa_index.json).
// No model is involved. The answer is only ever composed from retrieved records; unanswerable questions return the no-evidence state.
import type { QaDoc } from "./data";

const STOP = new Set(("evidence support supports number numbers the a an and or of to in for on by with from as at is are was were be been its their this that which these those into over under than then also not no yes per vs versus about after before during between within " +
  "what who whom whose when where why how does did do can could should would will has have had it we you they he she them his her our your i my me us any all some more most much many such there here what's whats tell give show list explain describe please").split(" "));

export const normalize = (s: string) => s.toLowerCase().replace(/johnson\s*(?:&|and)\s*johnson/g, "jnj").replace(/\bj\s*&\s*j\b/g, "jnj").replace(/eli lilly/g, "lilly");
export function stem(w: string): string {
  if (w.length > 4 && w.endsWith("ies")) return w.slice(0, -3) + "y";
  if (w.length > 5 && w.endsWith("sses")) return w.slice(0, -2);
  if (w.length > 3 && w.endsWith("s") && !/(ss|us|is)$/.test(w)) return w.slice(0, -1);
  return w;
}
export function tokenize(s: string): string[] {
  const out: string[] = [];
  for (const t of normalize(s).match(/[a-z0-9]+(?:\.[0-9]+)?/g) ?? []) { if (t.length < 2 || STOP.has(t)) continue; out.push(stem(t)); }
  return out;
}

const TITLE_BOOST = 3; const K1 = 1.4; const B = 0.72;
const TYPE_BOOST: Record<string, number> = { claim: 1.15, report: 1.0, source: 0.7 };
const COMPANY_WORDS: Record<string, string> = { lilly: "LLY", jnj: "JNJ", abbvie: "ABBV", takeda: "TAK" };

export interface Hit { doc: QaDoc; score: number; coverage: number; matched: string[] }
export interface Answerability { ok: boolean; reason: string; missing: string[]; figureNeeded: string[] }
export interface Retrieval { terms: string[]; hits: Hit[]; strong: Hit[]; answer: Answerability; companies: string[] }

interface Posting { doc: number; tf: number }
export interface QaIndexRt { docs: QaDoc[]; post: Map<string, Posting[]>; len: number[]; avg: number; N: number; df: (t: string) => number; idf: (t: string) => number; text: string[] }

export function buildIndex(docs: QaDoc[]): QaIndexRt {
  const post = new Map<string, Posting[]>(); const len: number[] = []; const text: string[] = [];
  docs.forEach((d, i) => {
    const tf = new Map<string, number>(); let l = 0;
    for (const t of tokenize(d.t)) { tf.set(t, (tf.get(t) ?? 0) + TITLE_BOOST); l += TITLE_BOOST; }
    const body = d.x ?? ""; for (const t of tokenize(body)) { tf.set(t, (tf.get(t) ?? 0) + 1); l += 1; }
    len.push(l); text.push(normalize(body));
    tf.forEach((v, t) => { let p = post.get(t); if (!p) { p = []; post.set(t, p); } p.push({ doc: i, tf: v }); });
  });
  const N = docs.length; const avg = len.reduce((a, b) => a + b, 0) / Math.max(1, N);
  const df = (t: string) => post.get(t)?.length ?? 0;
  const idf = (t: string) => Math.log(1 + (N - df(t) + 0.5) / (df(t) + 0.5));
  return { docs, post, len, avg, N, df, idf, text };
}

/** Passages from process documents (briefs, run logs, audits, evaluation files) are not evidence about pharma; they are kept out of answers. */
export const isMetaPath = (p?: string) => !!p && /^(research_methodology\/(briefs|research_runs)\/|quality\/|PROJECT_STATE|CONTINUE|COORDINATION|map\.md|README)/.test(p);

const FIGURE_WORDS = ["revenue", "sale", "income", "profit", "cost", "price", "spend", "spending", "margin", "valuation", "headcount", "capex", "earning", "royalty", "fee"];
const NEG = new Set(["no", "not", "without", "nor", "none", "neither", "unreported", "undisclosed", "never", "lack", "lacks", "absent"]);
const isYearish = (t: string) => /^(19|20)\d\d$/.test(t) || /^\d{4}-\d\d(-\d\d)?$/.test(t);

/** Does this passage state a figure for the facet term (a number that is not a year/date, not negated), with the anchor entity close by? */
export function statesFigure(text: string, facet: string, near?: string): boolean {
  const words = text.toLowerCase().split(/\s+/);
  const base = (w: string) => stem(w.replace(/[^a-z0-9]/g, ""));
  for (let i = 0; i < words.length; i++) {
    if (base(words[i]) !== facet) continue;
    const before = words.slice(Math.max(0, i - 6), i).map((x) => x.replace(/[^a-z]/g, ""));
    if (before.some((x) => NEG.has(x))) continue;
    if (near && !words.slice(Math.max(0, i - 15), i + 16).some((w) => base(w) === near)) continue;
    for (let j = Math.max(0, i - 8); j <= Math.min(words.length - 1, i + 8); j++) {
      const t = words[j].replace(/^[^0-9]+|[^0-9a-z.%]+$/g, "");
      if (/^\d[\d.,]*(bn|m|k|%|b|x)?$/.test(t) && !isYearish(t.replace(/[,.]$/, ""))) return true;
    }
  }
  return false;
}

const UNKNOWN_WEIGHT = 4.5;

export function retrieve(ix: QaIndexRt, query: string, opts: { limit?: number } = {}): Retrieval {
  const terms = Array.from(new Set(tokenize(query)));
  const qn = normalize(query); const companies = Object.entries(COMPANY_WORDS).filter(([w]) => qn.includes(w)).map(([, c]) => c);
  const idMatches = (query.match(/\b(?:CLM|SRC)-\d{6}\b/gi) ?? []).map((s) => s.toUpperCase());
  // A term the corpus never uses may be an inflection of one it does ("respond" -> "response"): expand by a shared stem prefix.
  const search: [string, string][] = []; const weight = new Map<string, number>();
  for (const t of terms) {
    if (ix.df(t) > 0) { search.push([t, t]); weight.set(t, ix.idf(t)); continue; }
    const pre = t.length >= 5 && !/\d/.test(t) ? t.slice(0, Math.max(4, t.length - 2)) : "";
    const alts = pre ? Array.from(ix.post.keys()).filter((k) => k.startsWith(pre)).slice(0, 6) : [];
    if (alts.length) { alts.forEach((a) => search.push([a, t])); weight.set(t, Math.max(...alts.map((a) => ix.idf(a))) * 0.4); } else weight.set(t, UNKNOWN_WEIGHT);
  }
  const scores = new Map<number, number>(); const matched = new Map<number, Set<string>>();
  for (const [st, group] of search) {
    const p = ix.post.get(st); if (!p) continue; const idf = ix.idf(st) * (st === group ? 1 : 0.4);
    for (const { doc, tf } of p) {
      const sc = idf * ((tf * (K1 + 1)) / (tf + K1 * (1 - B + (B * ix.len[doc]) / ix.avg)));
      scores.set(doc, (scores.get(doc) ?? 0) + sc); (matched.get(doc) ?? matched.set(doc, new Set()).get(doc)!).add(group);
    }
  }
  const total = terms.reduce((a, t) => a + (weight.get(t) ?? 0), 0) || 1;
  const hits: Hit[] = []; const pos = new Map<QaDoc, number>();
  scores.forEach((sc, i) => {
    const d = ix.docs[i]; const m = matched.get(i)!; let cov = 0; m.forEach((t) => { cov += weight.get(t) ?? 0; });
    let score = sc * (TYPE_BOOST[d.k] ?? 1);
    if (companies.length && d.co.some((c) => companies.includes(c))) score *= 1.3;
    if (idMatches.includes(d.id.toUpperCase())) score += 100;
    hits.push({ doc: d, score, coverage: cov / total, matched: Array.from(m) }); pos.set(d, i);
  });
  for (const id of idMatches) { if (!hits.some((h) => h.doc.id === id)) { const i = ix.docs.findIndex((d) => d.id === id); if (i >= 0) { hits.push({ doc: ix.docs[i], score: 100, coverage: 1, matched: terms }); pos.set(ix.docs[i], i); } } }
  hits.sort((a, b) => b.score - a.score);

  const missing = terms.filter((t) => !search.some(([, g]) => g === t));
  const figureNeeded = terms.filter((t) => FIGURE_WORDS.includes(t));
  // The rarest term the corpus knows must be present in an evidence passage: it is what the question is about.
  const known = terms.filter((t) => ix.df(t) > 0 && !FIGURE_WORDS.includes(t) && !/^\d+$/.test(t)).sort((a, b) => ix.df(a) - ix.df(b));
  const anchor = known.length && ix.df(known[0]) <= Math.max(25, ix.N * 0.03) ? known[0] : undefined;
  const minCov = 0.55;
  const qualifies = (h: Hit) => {
    if (idMatches.includes(h.doc.id.toUpperCase())) return true;
    if (h.coverage < minCov) return false;
    // Figures are answered from claims only: a claim is one atomic dated statement, while a report chunk can sit a figure beside an unrelated name.
    if (figureNeeded.length) { if (h.doc.k !== "claim") return false; } else if (!(h.doc.k === "claim" || (h.doc.k === "report" && !isMetaPath(h.doc.path)))) return false;
    if (anchor && !h.matched.includes(anchor)) return false;
    const body = ix.text[pos.get(h.doc) ?? 0] ?? "";
    return figureNeeded.every((f) => statesFigure(body, f, anchor));
  };
  const strong = hits.filter(qualifies);
  let answer: Answerability;
  if (!terms.length) answer = { ok: false, reason: "The question contains no searchable terms.", missing: [], figureNeeded: [] };
  else if (!strong.length) {
    const why = missing.length ? `The corpus has no record containing: ${missing.join(", ")}.`
      : figureNeeded.length ? `No claim states a figure for \u201c${figureNeeded.join(", ")}\u201d together with ${anchor ?? "the other terms of the question"}.`
      : "No record covers enough of the question's terms to answer it.";
    answer = { ok: false, reason: why, missing, figureNeeded };
  } else answer = { ok: true, reason: "", missing, figureNeeded };
  return { terms, hits: hits.slice(0, Math.max(opts.limit ?? 40, 12)), strong: strong.slice(0, 60), answer, companies };
}

/** Split a compound question ("what is X and what is Y") into its sub-questions. Returns [] when the question has a single part. */
export function splitParts(query: string): string[] {
  const parts = query.replace(/\?+\s*$/, "").split(/\s*(?:,\s*and|;|,|\band)\s+(?=(?:what|which|how|who|when|where|why|is|are|was|were|did|does|do)\b)/i).map((x) => x.trim()).filter(Boolean);
  return parts.length > 1 ? parts.map((x) => x + "?") : [];
}

export interface PartialRetrieval { view: Retrieval; supported: string[]; unsupported: { part: string; reason: string }[] }
/** When the whole question has no evidence but some sub-question does, answer those and report the rest as not covered. */
export function retrievePartial(ix: QaIndexRt, query: string, whole: Retrieval): PartialRetrieval | null {
  if (whole.answer.ok) return null;
  const parts = splitParts(query); if (!parts.length) return null;
  const rs = parts.map((p) => ({ p, r: retrieve(ix, p) })); const ok = rs.filter((x) => x.r.answer.ok);
  if (!ok.length || ok.length === rs.length && false) return null;
  const seen = new Set<string>(); const strong = ok.flatMap((x) => x.r.strong).filter((h) => (seen.has(h.doc.id) ? false : (seen.add(h.doc.id), true)));
  return { view: { ...ok[0].r, strong, hits: ok.flatMap((x) => x.r.hits).slice(0, 40), answer: { ok: true, reason: "", missing: [], figureNeeded: [] } },
    supported: ok.map((x) => x.p), unsupported: rs.filter((x) => !x.r.answer.ok).map((x) => ({ part: x.p, reason: x.r.answer.reason })) };
}
