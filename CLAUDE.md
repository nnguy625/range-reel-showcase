# RANGE REEL — OPERATING RULES

**These load every session. They override default behaviour. Nelson should never have to repeat ***REMOVED*****

---

## 🔴 1. CHANGE CONTROL — NOTHING CHANGES WITHOUT HIS OK

**A diagnosis is not a mandate.** Finding a problem does not authorise fixing it.

A change = assets · elements · attachments · settings he set · route or method · scope · file placement ·
staging to `_TO_DELETE_VERIFY` · what gets sent to Franco.

State it, wait. Short, ops, scan-friendly:
```
ATTACHMENTS — NO CHANGE.        (or: CHANGE PROPOSED, needs your OK)
PROMPT CHANGES — 3, all wording:
1. ...
```
**Default every round: same attachments + corrected prompt.** Redesign only when he asks.

**The bottleneck is ROUND COUNT, not prompt quality.** Unlimited closes; the deadline is mid-August.
Every round spent redesigning is a round he is not generating.

## 🔴 2. NEVER GENERATE IF UNLIMITED IS OFF

Arm the toggle **before** typing — Enter submits. **If any credit figure shows on GENERATE, stop.**
No credit spend without his explicit approval. He fires; I deliver plans and paste-ready prompts.

## 🔴 3. NEVER DELETE

Local → `_TO_DELETE_VERIFY/`. Drive → `_SUPERSEDED/`. Staging something out is itself a change (rule 1).

---

## PROMPT LAWS — SD2 / HIGGSFIELD

| # | Law |
|---|---|
| P1 | **Every pronoun that could be an element tag IS the tag.** `@Pao-Urban rides`, never "she rides". Throughout the body, not once in a header. |
| P2 | **Tag form is `@Name`** — `@Pao-Urban`, `@Skateboard`, `@Loc-SoCal-Street`. Never a UUID. Never `<<<Name>>>`. |
| P3 | **Settings are CONTROLS, never prompt text** — aspect, resolution, duration, speedramp (this is how slow-mo is set), bitrate, audio on/off, batch, model, Unlimited. |
| P4 | **Describe nothing an attached reference already owns.** Elements get a positive jurisdiction line only. Never describe a surface `@Skateboard` owns. ⚠ Whether Subject Lock / World Plate should re-describe is an **open question — ask Franco.** |
| P5 | **No timecodes in a continuous take.** Causal order only. Measured: timestamps produced a hard cut at 1.083s. |
| P6 | **One camera move per shot.** Come-around AND rise is two. |
| P7 | **Attached clip owns timing.** Never write per-beat cues alongside attached audio. |
| P8 | **Minimal trick spec.** Name the action once, one tether, one endpoint. Measured monotonic: every added mechanic made it worse. |
| P9 | **Negation summons the noun** — positive phrasing by default. Five negation batteries are sanctioned; anything else ships positive. |
| P10 | **`Extend @Video 1`**, never "reference @Video 1" — *reference* reclassifies the job into a lookalike. |
| P11 | **Naming a beat licenses it to expand.** Subordinate beats stay inside the block of the action they serve. |
| P12 | **Moderation is lane-dependent.** Unlimited is STRICTER than credits. Leaner prompt = safer. |

**Prompt block order:** the house skeleton in `Docs/SKILL_sd2-range-reel-prompting.md` §6. Blocks not yet needed as of
World 1: `CAPTURE CADENCE`, `NO ON-SCREEN TEXT`, `PROP LOCK`. PROP LOCK is the home for any prop that must render
exactly — the skateboard kept morphing and belongs there.

---

## WORKING LAWS

- **Read the owning doc, not a summary — and not a template.** Copying the locked clip-1 prompt as a
  template is how its defects propagate.
- **QA an asset at NATIVE RESOLUTION before proposing it.** A 480px contact sheet hid a broken board.
  A seed asset gets gated before it seeds anything.
- **No conclusion over truncated output.** Re-pull untruncated before any "neither / none / this confirms".
- **No "impossible" without three attempts that differ in KIND.**
- **Stratify before calling anything random.**
- **A promise needs a timer.** I go dormant at turn end — arm `run_in_background` or the promise is false.
- **Franco advises, Nelson decides.** Report his ruling as *his ruling*, then my own read. Never relay a
  Franco stop rule as the decision.
- **Franco reviews the ARTIFACT.** Send watchable links, never `PENDING`. Ask him to refute me, not agree.
- **The prompt ships WHOLE, in the chat body**, every round it changes — after Franco has wargamed it.
- **Debrief style:** ELI5 → ops bullets → casual summary. Dense over long. Clickable links to everything.

---

## PROJECT FACTS

**Reel:** 90.000s · 128 BPM · 4/4 · 48 bars · six worlds × 8 bars × 15.000s.
**1 bar = 1.875s · 1 beat = 0.46875s.**

**W1** = two clips at 4+4 bars. Clip 1 = 0.000–7.500 (real-time push + carve). Clip 2 = 7.500–15.000
(slow-mo kickflip, **ends airborne** — wheels never touch inside W1; the drop lands on W2's first frame).

**W1 elements:** `@Pao-Urban` · `@Skateboard` · `@Loc-SoCal-Street`
**W1 clip-2 attachments:** `Assets/Video/W1_CLIP1_A6b_TRIM_7s500_EXTSOURCE.mp4` (extend source, 180 frames
= 7.500000s exact) + `Assets/Music/AUDIO_CARRIERS/GUIDE_CLICK_W1_CLIP2_TAPERED_8s.wav`

**Key docs:** `Docs/STATE.md` (state anchor) · `Docs/PROMPT_W1_CLIP1.md` (locked clip 1) ·
`Docs/SD2_GUIDE_FINDINGS.md` (vendor guide vs our build) · `Docs/SD2_MODERATION_MODEL.md`
**Memory:** `the agent memory index`
**Drive:** `GDRIVE:/RANGE_REEL_ASSETS/SD2 DRAFT/`

**Environment:** Windows. **`py`, not `python`.** ffmpeg filter `file=` breaks on a Windows drive-letter
colon — `cd` to the output dir and use a bare filename. ChatGPT renders truncate; reload to recover.

**Reviewer messages go through the reviewer's own interface; long briefs are attached as files.**
