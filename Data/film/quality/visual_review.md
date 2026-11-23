# Visual review — composition, legibility, consistency

Method: preview frames at chosen film times (`motion/scripts/preview.mjs`, screenshots of the live scene) assembled into contact sheets (`previews/act1/`, `previews/act2/`, `previews/act3/`, `previews/act3b/`, `previews/act3c/`), then cue-frame sheets extracted from the final MP4 (`quality/sync_frames/SNN_cues.png`). Every scene was inspected at least once at 640×360 tile size and once at full 1920×1080 for the dense frames.

## System

- 1920×1080, centred coordinates; safe area x ∈ [−800, 800], y ∈ [−440, 440]; red eyebrow (act · title) top-left at y = −476; muted evidence strip (claim ids) bottom-right at y = +486; black overlay for fades (0.6 s in, 0.55 s out; 0.9 s at the film's end).
- Two palettes: `ink` (#0B1220) for S01–S05 and S12–S14; `paper` (#FAFAF7, warm off-white) for S06–S11, the Takeda-positive and action scenes. The switch happens at S05's last beat ("defend what is dated, build what repeats") and back at S12.
- Type: serif headlines and figures (Georgia-class), sans body (Helvetica-class), mono eyebrows and chips. Minimum rendered body size 18 px; chips 18 px mono tracked.
- Kind chips: SCENARIO (S05), ASSUMPTION (S13), BET ids (S07, S09, S10, S11); FACT qualifiers in grey mono where a claim is PARTIALLY_SUPPORTED.

## Findings and fixes, by pass

| Pass | Scene | Finding | Fix |
|---|---|---|---|
| act1 sheet | S01 | Pill label and 21% figure overlapped at the hub move | re-spaced; figure fades as hub moves |
| act1 sheet | S02 | Realised-price and PBM template labels collided | PBM timeline moved below the price line; template label split |
| act1 sheet | S03 | Successor bars crowded the Humira bar | lane widened; labels under bars |
| act1 sheet | S05 | Scenario band label clipped at left | band label moved inside the band; "SCENARIO · NOT A FORECAST" chip above |
| act2 sheet | S07 / S09 / S10 | Tag chips overlapping captions; ladder rows too tight | rows re-spaced; chips anchored left |
| act3 sheet | S11 | "+ USD 5bn purchase" weight landed on the gauge title; Cerevel crack ran through "8.7bn"; options caption ran into the gauge caption | weight lands under the hub; crack moved to the card's right third; options caption wrapped at 330 px; figure/caption moved down |
| act3 sheet | S12 | "− USD 7.5bn" figure overlapped the Alphabet caption; legend collided with the evidence strip | loss bar moved left, figure beside it; legend raised to y = 375 |
| act3 sheet | S13 | Milestone labels stacked on the headline (three rail markers 123 px apart cannot carry four-line labels) | redesign: lit rail ticks + three milestone columns below the rail; ribbon/envelope/council moved down; envelope origin at its left edge so the shrink keeps its left margin |
| act3 sheet | all | Eyebrow text clipped at the left edge in every scene (layout row centred on its anchor) | `offsetX={-1}` on the eyebrow row in `stage.tsx` |
| final MP4 | S01 / S14 | Title cards ran past the scene slots | timeline tails 2.5 s / 4.5 s (see synchronisation report) |
| final MP4 | S10 | "most members pay $0" pill narrower than its text | pill widened to 230 px |

## Checks passed on the final film

- No text outside the safe area; no element overlaps the eyebrow or the evidence strip (checked on all 14 cue sheets).
- Contrast (WCAG ratios computed from `motion/src/lib/theme.ts`): text on `ink` #F4F5F7/#0B1220 = 17.2:1; muted on ink #9AA3B5 = 7.4:1; text on `paper` #141A26/#FAFAF7 = 16.7:1; muted on paper #6B7280 = 4.6:1; red #E60012 on paper 4.6:1; white on red 4.8:1. Red on ink is 3.9:1 and is therefore used only for accents and large figures, never for body text.
- Motion: every reveal eases in 0.4–0.9 s; no element pops; bars grow with their figures; nothing moves during the last 0.5 s before a fade.
- Continuity: eyebrow names the act and topic on every frame; evidence strip lists the scene's claim ids on every frame; the TAKEDA 2040 title card opens and closes the film with the same typography.
- Cadence: 14 scenes, 20–36 s each (S08 20.1 s, S13 35.8 s), average 28.7 s; no scene has more than nine beats.

## Residual notes

- Dark-palette scenes have a mean luma of 17–28; on very bright displays the ink background reads near-black, which is intended.
- The S14 "What endures…" statement is centred on the left two-thirds while the ring appears at right; it is a deliberate asymmetric composition, not a centring error.
- Software rasterisation (SwiftShader) produces slightly softer anti-aliasing than GPU rendering; CRF 18 keeps text edges clean at 1080p.
