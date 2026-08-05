---
name: sd2-range-reel-prompting
description: >
  THE canonical method for writing Seedance 2.0 (SD2/Higgsfield) video prompts on Range Reel —
  every measured law from a scored study of public community renders (kept private), every Franco
  ruling, the plate-first architecture that produced W2 A-6/A-7, the audio-carrier system, the
  choreography grammar, and the full fire-time checklist. Use for ANY SD2 prompt writing, review,
  or debugging on Range Reel; any W2-W6 clip design; any question about why a render failed.
  This file is the compaction-insurance copy: if context was compressed, TRUST THIS FILE over
  any paraphrase of the rules. Cross-check Docs/STATE.md for the live project position.
---

# SD2 RANGE REEL PROMPTING — the complete method as of 2026-08-04

> 🔴 **READ THIS FIRST — WHAT "SD2" MEANS HERE.** Throughout this file and every Range Reel doc,
> **SD2 = SEEDANCE 2.0**, ByteDance's video generation model, which we drive through **Higgsfield**.
> **It is NOT Stable Diffusion.** Nothing in this file transfers to Stable Diffusion, and no Stable
> Diffusion convention (negative-prompt fields, weight syntax like `(word:1.2)`, LoRA/CFG/sampler
> settings, comma-separated keyword stacks, booru tags) applies. Seedance takes natural cinematic
> prose, attached media references with named jurisdictions, and platform-side controls. If a future
> session sees "SD2" and reaches for Stable Diffusion habits, that is the single most damaging
> misreading of this document.

**Provenance, so you trust it:** every law here is (a) measured on our own fires, (b) confirmed
across a scored study of public community renders (kept private) reviewed sighted by three independent referees (me = Pablo,
Franco = GPT reviewer, Codex), or (c) a Franco ruling Nelson adopted. Tier is marked where it
matters. Full evidence: `Docs/JOINT_REVIEW_CONVERGED.md` (rev5) · `Docs/W2_A6_FRANCO_RULING.md` ·
`Docs/PROMPT_W2_CLIP1.md` · memory
`sd2-proven-prompt-tiers`.

---

## 0. THE GOVERNING LAW — ONE CHANNEL, ONE OWNER

Never give two references competing ownership of one visual channel. Per-shot/per-time-segment
reference assignment produces montage; orthogonal jurisdiction assignment coexists (7 refs went
12/12 in corpus). This extends to NEGATIONS: a written "no X" LOSES to an attached reference
containing X (seq53 glasses; proven on our own footage — v13 said "no skateboard in frame at any
point" and W2 A-5 rendered W1's skateboard on the bazaar stone for 0.5s).

**Corollaries:**
- An attachment the prompt assigns NO role will self-insert as content/screen time (seq17).
- Never attach a source clip whose world you intend to replace — jurisdiction prose cannot strip it.
- Control DIAGRAMS (pose diagrams, arrow paths) fail to control AND can leak their pixels into the
  render (seq41 — magenta arrows painted into frames). Photographic references only.
- Negation taxonomy: ROLE/USAGE negations obey ("do not use as a starting frame, take only the
  space and texture" — works at production scale). TEMPORAL negations obey
  ("no slow motion at any point"). CONTENT-vs-attached-ref negations LOSE. Text-only negation
  batteries are safe when no reference carries the noun.

## 1. THE PLATE-FIRST ARCHITECTURE (the seam solution — proven by A-6/A-7)

**The strongest control grammar in the model (Tier 1, n=4 corpus near-perfect + our A-6):**
attach a photographic start frame and write:

```
@Plate is the exact first frame and strict opening-state anchor. Begin on @Plate exactly, without
reframing or an establishing insert. Every dancer who will appear is already present and moving in
frame ***REMOVED*** Paola appears once; no new figure enters.
```

- Text-only first-frame orders LOSE to the model's establishing-shot grammar (seq47). Opening
  states need an attached owner.
- The plate is built, not generated: extract the best real frame → model-edit for additions →
  **MASK-COMPOSITE the additions onto the untouched original** (the mask-composite law: an image never
  runs through a model twice in full; every full pass destroys texture and drifts color/geometry —
  we measured a 20% subject shrink from one full pass). Scripts:
  local align/mask-composite scripts (not in this repo). Align scored ONLY on a
  band with no added content; grade-match the edit to the original (per-channel mean/std on an
  unchanged band) or additions read pasted. Result: face MAE 0.000 = geometry gate passes by
  construction.
- **Reference stack for a plate-anchored shot:** @Plate + ONE face-only identity element
  (`@Pao-Face-Bolly is the sole authority for Paola's facial identity, and nothing else`) +
  audio carrier. NOTHING else — no wardrobe sheet, no location element (plate owns them at t=0),
  no pose diagram, no descent video. Location element returns only in clips WITHOUT a
  photographic opening plate (W2 clips 2-3).
- A faithfully-preserved plate defect is still a defect (clone dancers came through perfectly).
  Fix upstream with a LOCALIZED mask-composited patch; never a second full-frame pass; a recolour
  is not a new person — "a separate casting choice, not the same performer in wardrobe B."
- QA every plate at 1:1 native res (the skateboard was invisible at thumbnail size) and run the
  GEOMETRY GATE: head-to-foot span vs the matched frame, not just foot position.

## 2. THE BUDGET — BEATS vs SECONDS (word count is NOT the constraint)

- 2,211-word corpus prompt delivered 8/8; 1,335-word delivered 13/13. Words restating invariants
  are free. Words adding BEATS cost runtime.
- **An 8s one-take carries TWO macrobeats** (Franco, final). Cuts buy beat density (5 shots fit
  6s as authored montage); one-take spends it. Over-full timelines TRUNCATE THE TAIL — SD2 never
  compresses to fit; the ordered ending simply never happens (seq73). Never park the final-frame
  contract at the end of a long list.
- Camera CONDITIONS cost no beat budget (a continuous retreat that never restarts). A
  disturbance-recovery arc (dancer forces a lateral yield) is a FULL beat — cut it or spend it.
- A held pose/isolation is CHEAPER than travel (no changing foot placement/geography) but not
  free: it has an entry condition, a repeated rhythmic behavior, a sustained body rule, an exit
  trigger. Fuse the landing INTO the first held state to save a beat.
- Micro-events are free ONLY as properties of an existing beat (smile settles during landing).
  They cost attention when they need their own trigger/timing/reversal (grin opens AND closes
  within a bar = a performed appointment).

## 3. CHOREOGRAPHY GRAMMAR (the A-6/A-7 lessons)

- **"One phrase that changes shape once" produced a locked T-pose.** The working form couples
  arms to WEIGHT TRANSFER: one finite exchange, two coupled weight transfers, wrists and fingers
  CONTINUOUSLY active, asymmetric elbows, and the phrase "cuts before it repeats or settles into
  a held line." That is the line between arm soup (unbounded improvisation) and mannequin.
- **Marching is a LOWER-BODY defect.** Straight-ahead alternating steps + upright torso + no
  lateral loading = procession, regardless of arms. Fix: "one diagonal garba cross-step rather
  than a straight forward walk: weight shifts visibly left to right, hips and shoulders
  counter-rotate, one knee lifts briefly on the rebound."
- **Layered dancing (Nelson's direction):** name the layers as SIMULTANEOUS — "her bare feet keep
  their own rhythm against the stone, her arms carry a separate line above them, and her wrists
  and fingers articulate precise classical Indian hand shapes continuously inside that line."
- **Unison with human variance (Nelson's anti-robot law):** accents stay simultaneous, execution
  varies — "arms reaching to slightly different heights, one a fraction ahead of the beat and
  another a fraction behind, skirts flaring to different widths." Named physical differences,
  bounded ("a fraction", "slightly"), never the word "imperfect" (unrenderable) and never
  staggered reaction WAVES (they fight deliberate unison).
- **Tempo lock (fixes "too slow / off beat"):** "The attached track is the sole timing clock.
  All choreographic accents move at the full 128 BPM pulse, one clean accent per beat, with no
  preparation pause or half-time phrasing." The carrier influences major events but does NOT
  govern every accent — numbers control rate, audible events control sections; the jobs don't
  conflict.
- **Section switching = causal-musical grammar, never timecodes** (P5: timecodes in a continuous
  take cut at the number; seq43: time blocks phasing ONE camera path are the only safe use).
  Name switches as unique audible events: "as the landing bass decays and only the sparse plucked
  line remains" / "on the first heavy bass-and-drum strike" / "when the low end drops away and
  the sparse plucked line returns."
- Vocabulary bans: "bobble" → loose neck wobble; use "crisp lateral Indian head isolation, chin
  level, shoulders and ribcage held quiet." "Glide/throne-room" wording invites the regal march.
  "The arms never repeat" = unlimited improvisation = arm soup.
- Ensemble motion caps: a full orbit/side-exchange cannot resolve in <1s without teleportation —
  "a small traffic accident wearing bangles." For sub-second bursts write the IMPRESSION: nearest
  pair cross behind her in opposite directions, outer rows whip half-turns, motion blur rings
  her, she stays planted and readable.
- **"Moving AI figurine" is a MOVEMENT note, not a skin note** — fixed smile + hidden eyes +
  rigid shoulders + marching + clones + identical timing. Fix choreography first; grain last
  ("grain can disguise smoothness, it cannot generate cheek tension"). Face realism lever #1 is
  LIGHT: asymmetric bounce ("warm stone bounce reaches her face from camera-left rather than
  evenly... skin keeps small irregular highlights, pore breakup and natural tonal variation,
  never uniform matte beauty fill").

## 4. CAMERA

- One continuous move as a CONDITION, physically motivated, with operator texture ("operator
  breath and micro-settling, shoulder-mounted mass, human correction"). Chained verbs are fine
  when causally glued into ONE journey (FPV dive-orbit-rise = one flight).
- Subject-motivated moves deliver (a 180° pivot caused by her pass = 10/10); self-directed
  orbits wander. Route exits through the camera channel ("she moves out of frame due to real
  camera parallax"), never object behavior.
- **Never order a reveal of geography that is not already established** — SD2 delivers the
  reveal as a HARD CUT hidden in the pan blur (seq63 whip-pan trap). Dancers enter the HELD
  frame or exist from frame one; nothing "is revealed."
- A retreating camera STRETCHES perceived tempo — but as a SECONDARY cause, and a good retreat
  is an asset (Franco's sighted A-7 reversal: it "opens the market naturally and gives the
  ensemble depth" — he WITHDREW his blind kill-the-retreat ruling after watching). The form
  that survives footage: retain the retreat through the landing/expansion, ease to a slow drift
  during in-place sections, hold subject scale through sub-second bursts, resume restrained —
  NEVER a hard stop (reads as a camera reset). Modulate the retreat; don't remove it.
- Plate-anchored shots: OPTICS = preserve the plate. "Preserve the exact perspective, lens
  geometry and subject scale of @Plate. No focal-length change and no field-of-view drift."
  No mm, no "anamorphic" (asks the model to redesign a format the plate fixed). Film SURFACE
  (stock/grain/shutter) stays a separate style line.

## 5. AUDIO (the carrier system)

- **The carrier must be REAL MUSIC.** A click track is 93% silence and SD2 fills the void with
  its own score. Current W2 clip-1 carrier: `CANDIDATE_CARRIER_W2_CLIP1_V16_7137_8s.wav`
  (V16_BOLLY_a from source 7.137s, 8.000s exact). Attach it; write "The attached clip is the
  only audio source. No dialogue and no voices."
- SD2 phase cannot be prompted (internal ~1s clock; density promptable, phase not). **Landing-
  on-beat is engineered by cutting the GUIDE carrier so the low-end event lands on the expected
  contact frame** — A-6 contact measured at frame 11 = 0.458s; the 7.137 cut puts the bass swell
  peak at 0.460s. IT WORKED ("does drop on the beat" — Nelson).
- **Never shift the EDITORIAL window to chase a landing.** Guide ≠ edit master. The W2 world
  window stays source 7.400-22.400 (W3 slam at 22.400). Final sync happens in POST on the
  selected keeper: duck the early low-frequency kick in the master, transplant/rebuild it at the
  keeper's ACTUAL contact frame. A rendered clip's handle cannot create negative pre-roll.
- A landing time measured on ONE take is not a constant across siblings.
- W2 music structure (clip time on the 7.137 guide): bass swell 0.36-0.76 (peak 0.46 = the drop
  from W1) → sparse plucked 0.76-3.86 → heavy bass burst 3.86-4.61 → sparse 4.61-7.81 → from
  7.81 the BUILD fires continuously to the W3 slam. Nelson's arc: drop into W2 → 7s of air →
  build (clip 2's job) → drop into W3.

## 6. THE PROMPT SKELETON (v16/v17 form — current best)

```
One continuous 8-second take, real-time, no internal cuts.
[one-sentence scene intent]
[@Plate authority + occupancy block — §1 verbatim]
[@Face element single-authority line]
GEO SPATIAL LAYOUT (locked across every W2 shot — pure spatial map):
[immutable geography ONLY: corridor, what's frame-left/right, sun position, the 180° axis rule.
 NO camera height/movement in GEO — pasting those into every clip of a scene forces every shot
 into the same move. Write once per world, paste verbatim into each clip of that world.]
OPTICS  [preserve-the-plate block — §4]
CAMERA  [one condition + operator texture — §4]
ACTION  [tempo lock → landing fused into first state → sections switched by audible events →
         layered choreography + unison-with-variance — §3. Two macrobeats.]
ACTING  [slim: body status + one expression evolution + gaze discipline. "The warm opening smile
         settles into calm command on contact; her gaze stays on the travel path, never the lens.
         The dancers dance with their own faces; nobody mirrors her mouth." Master profiles live
         in the registry, NEVER pasted whole into runtime — triggered appointments (chin-lift-
         per-accent) render as head-bobbing.]
PHYSICS [contact, weight transfer, cloth delay, anklets, dust — concise, not duplicated in ACTING]
LIGHTING[source + direction + camera side + exposure priority + "no frontal key, no beauty fill"]
AUDIO   [carrier-only block — §5]
FINAL FRAME [broad composition, mid-phrase, "the retreat never fully settled before the cut" —
         framing-class only; object-persistence finals fail; broad ≫ microstate]
[no-text line: "No on-screen text anywhere in frame — no lettering, signage, logos, captions"]
Style: [Kodak Vision3 250D rendition, fine restrained 35mm grain, 180-degree shutter blur,
        "Preserve the flare, bokeh and optical character already present in @Plate", photographed-
        not-generated battery. Cinematic realism = "real people acting in a movie" is the target.]
```

**Tags:** paste form is `@Name` (the composer resolves it; never a raw UUID, never <<<Name>>>).
Every pronoun that could be a tag IS the tag when elements are attached; with a plate-anchored
stack, "Paola" as a name is fine since no ambiguous element competes. Counts: describe, never
number ("a small group", never "three dancers") — counts fail by VISIBILITY (melee blurs, bodies
clone into backgrounds; QA for hero-clones). Text renders only with an owner asset (short caps
ad-overlay is the one promptside exception).

## 7. FIRE-TIME CHECKLIST (controls are the other half of the prompt)

1. **Unlimited ARMED before typing** (Enter submits). ANY credit figure on Generate = STOP.
2. Aspect **16:9 explicit** — never Auto (Auto returned 4398×1886 from "anamorphic"). 4K. 8s.
   Audio ON. Speedramp off.
3. Composer CLEARED of stale prompts first.
4. Attachments = exactly the §1 stack. Verify what the composer shows; if the plate lands under
   a different name than the prompt's tag, fix the tag before firing.
5. **Batch siblings** — identical wording gave 0.23 and 0.90; never judge a prompt from one take.
6. BRIEF-VS-PROMPT AUDIT before every fire: table every requirement Nelson has stated (incl.
   earlier messages), quote the literal line delivering each. Can't quote = ABSENT. A Franco
   risk-mitigation is NEVER the creative spec — a mitigation contradicting a stated requirement
   is a CONFLICT to surface.
7. Iteration law: ONE line changes per round, log prompt version + change + verdict. 10-15 round
   HARD CEILING → simplify the SHOT (split it, remove an action, change the angle), not the
   words. Three failed rewrites on one axis = the prompt was never the variable (GATE I): ask
   what ASSET is missing (motion reference video, plate, element).

## 8. PROCESS AROUND THE PROMPT

- **GDF loop** on every render: probe → QA with frames actually looked at (contact sheet + defect
  strips at native res) → Drive → Franco reviews the ARTIFACT → his ruling reported as HIS, my
  read as mine → Nelson decides. Franco advises, Nelson decides — never relay a stop rule as the
  decision.
- **Franco delivery (current state 2026-08-04):** his session has NO live web access — links are
  dead, folder paths are dead, and my file-upload tool only accepts Nelson-attached files. What
  works: PASTE FRAMES as clipboard images directly into the thread (works, proven), or Nelson
  drags the mp4 into the chat himself (720p review copies ~1.4MB:
  `Assets/Video/MOTION_REFS/A7_REVIEW_720p.mp4` pattern). He must SEE the artifact — stills
  cannot carry beat-sync; only a video with audio can.
- **Asset registry law:** an element does not exist until it has a row in `Docs/ASSET_REGISTRY.md`
  (name + id + what is actually in the picture). dancers1/dancers2 (two 7-woman casting sheets,
  14 distinct approved women — THE anti-clone resource) were lost to compaction because they
  lived only in Higgsfield. Anything created in a vendor UI gets a registry row the same session.
- **Never delete** (stage to `_TO_DELETE_VERIFY`/`_SUPERSEDED`) · **change control**: any change
  to assets/attachments/settings/scope is proposed and waits for Nelson's OK · verify writes
  (grep for the new string; an unconditional success print is a lie) · verify cloud sync via the
  Drive API, not local mirror byte counts.
- **Docs that anchor a fresh session:** `Docs/STATE.md` (live position) → this skill → 
  `Docs/PROMPT_W2_CLIP1.md` + successors (current locked prompt) →
  `Docs/JOINT_REVIEW_CONVERGED.md` rev5 (evidence) → `Docs/ASSET_REGISTRY.md` (what exists).

## 9. CURRENT W2 POSITION (as of this file's writing — check STATE.md for drift)

- A-7 = best draft (Nelson), banked as fallback, and **Franco's SIGHTED review (he fetched the
  mp4 via Drive connector in a fresh thread BRANCH — branching restores tools when a session
  loses web access) confirms**: landing on-beat by ear, no double-downbeat; wrist/finger work a
  real improvement (strongest 1.0-2.0s, 3.0-4.5s); ensemble variance reads human; slow zones
  located at 0.75-1.90s and 2.00-3.40s (half-time drift = the tempo-lock line's target); clone
  defect still visible in motion ~5-6.5s.
- **Sighted re-rule: "A-7 remains the stronger known shot."** The A→B→A sectioned design =
  one controlled experimental SIBLING only ("a creative gamble against a banked keeper"), with:
  ACTIVE isolation (feet rooted, torso under visible muscle control, head strikes on the pulse,
  wrists articulating — never a frozen statue), the retreat RETAINED and modulated (§4), the
  crossing IMPRESSION not literal circles, full-tempo accents. Two blind calls were reversed by
  footage — the standing proof of watch-the-artifact.
- **Motion-reference ruling:** feeding SD2 its own output is conditionally sound; a FULL A-7 +
  A-7-2 stitch is NOT (feeds back figurine carriage, clone signatures, cadence drift; the edit
  seam can be read as choreography/camera permission). If tested: a 3-5s curated subject-centred
  study — one continuous passage from ONE clip, cropped around Paola, defect frames excluded, no
  audio; A-7-2's arm sweep as a SEPARATE test. Pablo's added flag: a motion video + @Plate both
  touch her body channel — jurisdiction collision class; separate experiment lane only.
- Clone-dancer plate patch: pending, sourced from dancers1/dancers2 casting sheets.
- W2 clip 2 owns: the build section, the full ensemble orbit, the W3 handoff at source 22.400.
