// Executive narrative for View 1. This file holds only framing prose and claim IDs.
// Every statement and figure shown to the reader is pulled from the claims registry by ID (data/claims.json);
// the integrity test fails if a claim ID here is unknown or if research numbers appear as literals in src/.
export interface NarrativeBlock { id: string; stage: string; heading: string; lead: string; claimIds: string[] }

export const NARRATIVE: NarrativeBlock[] = [
  { id: "changing", stage: "What is changing", heading: "Price-setting and exclusivity are moving from the company to the state and the market",
    lead: "Government price negotiation, tariff-linked agreements and biosimilar entry now shape revenue as much as clinical success does. The records below are the primary-source evidence for each.",
    claimIds: ["CLM-001017", "CLM-003080", "CLM-001037", "CLM-000254", "CLM-000263"] },
  { id: "winning", stage: "Who is winning", heading: "Scale comes from a few franchises, and the leaders are concentrated in them",
    lead: "The strongest recent growth sits in single mechanisms or franchise pairs. Concentration is a strength and a risk in the same filing.",
    claimIds: ["CLM-000242", "CLM-000266", "CLM-000255"] },
  { id: "why", stage: "Why they are winning", heading: "Capacity, successor sequencing and disciplined deal flow",
    lead: "The mechanisms visible in the filings are manufacturing investment ahead of demand, a successor product launched before the incumbent loses protection, and a repeatable acquisition programme.",
    claimIds: ["CLM-000246", "CLM-003014", "CLM-000258"] },
  { id: "defensible", stage: "What is defensible", heading: "Moats that need years and capital to copy",
    lead: "Capability cards and moat analyses separate what a rival can buy from what it must build. They are interpretations and are labelled as such in the differentiators view.",
    claimIds: ["CLM-001038", "CLM-002072", "CLM-003084"] },
  { id: "takeda", stage: "What Takeda possesses", heading: "A large immunology franchise, a live exclusivity sequence and an early replacement signal",
    lead: "Takeda's public record shows a strong anchor product, products already losing exclusivity, one late-stage replacement asset and little disclosed evidence of AI outcomes.",
    claimIds: ["CLM-000274", "CLM-000275", "CLM-000276", "CLM-000277", "CLM-000278"] },
  { id: "ai", stage: "AI, data and robotics", heading: "Announcements are plentiful and outcome evidence is rare",
    lead: "Platforms are live at leading companies, yet independent evidence of value is thin and several industry attempts ended in documented retreats.",
    claimIds: ["CLM-000280", "CLM-006047", "CLM-006051"] },
];

export const PROVEN_LEVELS = ["OPERATIONAL", "SCALED", "DEMONSTRATED_OUTCOME"];
export const EMERGING_LEVELS = ["CONCEPT", "PROTOTYPE", "PILOT"];

// The ten-step story spine. Steps bound to a narrative block above scroll to it; later steps point at the forward-looking pages.
export interface SpineStep { id: string; label: string; block?: string; to?: string; lead?: string }
export const SPINE: SpineStep[] = [
  { id: "changing", label: "What is changing", block: "changing" },
  { id: "winning", label: "Who is winning", block: "winning" },
  { id: "why", label: "Why", block: "why" },
  { id: "defensible", label: "What is defensible", block: "defensible" },
  { id: "takeda", label: "What Takeda already has", block: "takeda" },
  { id: "opportunity", label: "Where the opportunity is", to: "/takeda", lead: "Gaps and under-developed capabilities in Takeda's public record mark where the opportunity could lie. This list is derived from the capability baseline; it is an analysis of the record, not a forecast." },
  { id: "build", label: "What to build", to: "/strategy", lead: "Strategic bets, each tied to evidence and to explicit assumptions. Hypotheses until the council and red-team reviews are complete." },
  { id: "invest", label: "What to invest", to: "/portfolio", lead: "Capital allocation across bets and horizons. Every amount is a labelled assumption, never a reported figure." },
  { id: "execute", label: "How to execute", to: "/roadmap", lead: "A sequenced roadmap with dependencies and decision gates." },
  { id: "measure", label: "How to measure", to: "/uncertainty", lead: "Stage gates, stop criteria and the strongest counterarguments, so that progress is judged against evidence." },
];
