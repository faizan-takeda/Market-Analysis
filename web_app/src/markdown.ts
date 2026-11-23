// Markdown -> HTML for the report reader. Pure string functions (no DOM) so the same code renders in the browser and in the server-side tests.
import { marked } from "marked";

export interface Heading { level: number; text: string; slug: string }
export interface Rendered { html: string; outline: Heading[] }

export const slugify = (s: string) => s.toLowerCase().replace(/<[^>]+>/g, "").replace(/&[a-z#0-9]+;/g, " ").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "section";
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const strip = (h: string) => h.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").trim();

/** Resolve a relative link against the directory of the current report path. Returns null for non-local targets. */
export function resolveRel(from: string, href: string): string | null {
  if (/^[a-z][a-z0-9+.-]*:/i.test(href) || href.startsWith("#") || href.startsWith("//")) return null;
  const clean = href.split("#")[0].split("?")[0];
  if (!clean) return null;
  const parts = from.split("/").slice(0, -1);
  for (const seg of clean.split("/")) { if (seg === "." || seg === "") continue; if (seg === "..") parts.pop(); else parts.push(seg); }
  return parts.join("/");
}

/** Replace CLM-/SRC- tokens in text nodes (outside links and code) with chip buttons. Unknown ids stay plain text. */
function chipify(html: string, known: (id: string) => boolean): string {
  let depth = 0; const out: string[] = [];
  for (const seg of html.split(/(<[^>]+>)/)) {
    if (seg.startsWith("<")) {
      if (/^<(a|code|pre|button)\b/i.test(seg)) depth++; else if (/^<\/(a|code|pre|button)>/i.test(seg)) depth = Math.max(0, depth - 1);
      out.push(seg); continue;
    }
    out.push(depth ? seg : seg.replace(/\b(CLM|SRC)-(\d{6})\b/g, (m) => (known(m) ? `<button type="button" class="idchip" data-id="${m}" title="Open evidence ${m}">${m.slice(4)}</button>` : m)));
  }
  return out.join("");
}

export function renderMarkdown(md: string, path: string, known: (id: string) => boolean, isReport: (p: string) => boolean): Rendered {
  let html = marked.parse(md, { async: false, gfm: true }) as string;
  html = html.replace(/<script[\s\S]*?<\/script>/gi, "").replace(/\son\w+="[^"]*"/gi, "");
  const outline: Heading[] = []; const seen: Record<string, number> = {};
  html = html.replace(/<h([1-4])>([\s\S]*?)<\/h\1>/g, (_m, lv: string, inner: string) => {
    const text = strip(inner); let slug = slugify(text); const n = (seen[slug] = (seen[slug] ?? 0) + 1); if (n > 1) slug = `${slug}-${n}`;
    outline.push({ level: Number(lv), text, slug });
    return `<h${lv} id="${slug}">${inner}</h${lv}>`;
  });
  html = html.replace(/<table>/g, '<div class="tablewrap" tabindex="0" role="region" aria-label="table"><table>').replace(/<\/table>/g, "</table></div>");
  html = html.replace(/<a href="([^"]*)"([^>]*)>/g, (_m, href: string, rest: string) => {
    const h = href.replace(/&amp;/g, "&"); const target = resolveRel(path, h);
    if (target && /\.md$/i.test(target) && isReport(target)) return `<a href="#/read/${esc(target)}" data-route="1"${rest}>`;
    if (target) return `<a href="#" data-missing="${esc(target)}" class="missing" title="Local file is not part of the bundled reports: ${esc(target)}"${rest}>`;
    if (/^https?:/i.test(h)) return `<a href="${esc(h)}" target="_blank" rel="noreferrer noopener"${rest}>`;
    return `<a href="${esc(h)}"${rest}>`;
  });
  return { html: chipify(html, known), outline };
}

export const plainText = (md: string) => md.replace(/\[([^\]]*)\]\([^)]*\)/g, (_m, t: string) => t).replace(/[|`*_>#]+/g, " ").replace(/\s+/g, " ").trim();
export const firstParagraph = (md: string, max = 230) => {
  for (const block of md.split(/\n\s*\n/)) {
    const t = block.trim(); if (!t || /^(#|\||>|-{3}|```|\*\s|-\s|\d+\.\s)/.test(t)) continue;
    const p = plainText(t); if (p.length > 40) return p.length > max ? p.slice(0, max).replace(/\s+\S*$/, "") + "…" : p;
  }
  return "";
};
