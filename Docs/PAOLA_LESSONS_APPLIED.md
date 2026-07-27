# PAOLA LESSONS → RANGE REEL

*Distilled from the Paola short-film production record (the production record →
`PAOLA_PRODUCTION_MEMORY.md`, ~3,500 lines) and the 07-24/07-27 cloud sessions. Paola is parked; these
are the transferable laws. Written cloud-side 2026-07-27 so the local desk can pick up.*

**How to read this:** every law below is receipt-backed — it was paid for with real generations. Where
this reel's `STATE.md` HARD RULES already encode a law independently, it is marked **[CONFIRMS]** — that
convergence is itself evidence. Where it is new to this project, **[NEW]**.

---

## 0. THE EXPENSIVE LESSON — what three weeks bought

The Paola standoff wide consumed ~3 weeks and ~25+ draws chasing **face identity on a figure roughly 40
pixels tall**. It never landed. The frame was, by the project's own locked edit plan, a **1-second
insurance shot**. Two failures compounded: a shot was allowed to become load-bearing, and it was QA'd at
4K-still fidelity for a 720p delivery medium.

**[CONFIRMS]** this reel's HARD RULES 3 and 4 — *"Frame for the face — never write identity pressure and
small scale into the same shot"* and *"No shot is load-bearing."* Those two rules are the whole lesson.
They are not stylistic preferences; they are the price of three weeks.

**Applied to the reel:** every world needs at least one face-readable shot (the boards already do this —
W1-S4 apex "face readable", W3-S2 "face large and lit", W4-S1 MCU). Wides carry **silhouette, wardrobe,
motion and screen position** — never likeness. If a wide comes back with a generic face, that is a
correct render, not a defect.

---

## 1. REFERENCE / IDENTITY LAWS

**1.1 One identity authority per generation. [CONFIRMS]**
Two non-identical face sources average into a third person. Receipt: `@Pao_Kim_Face_Front` +
`@Standoff-PaolaMCU` together produced a stranger. Matches HARD RULE 9.

**1.2 ★ NEVER FENCE THE IDENTITY SOURCE. [NEW — the single highest-value law here]**
Do **not** write *"use her identity but ignore the sheet's studio lighting / gray backdrop / clean
finish."* Identity and finish are **not separable channels** — telling the model to distrust how the
sheet renders her makes it distrust her face too. Receipt: identity was landing 2/2, the fence was added
to fix studio-clean skin, and identity collapsed and stayed collapsed for four prompt versions.
**Fix finish positively** (inherit the plate's grain, depth-appropriate texture, anatomical shadow
falloff) and in the closing filter only. **Priority: identity is unrecoverable downstream; finish is a
ten-minute grade fix.** Protect identity in-gen, fix finish in post.

**1.3 Name the channels, don't just point. [NEW]**
`@Pao-Face-Bolly` alone is a weaker binding than *"her face, hairline, bun and brows carried identically
from her reference, her features remaining completely unchanged."* Naming **which** channels to carry is
not re-describing (no "almond eyes") — it is a pointer with a channel list, and it matches Google's
officially documented feature-pinning template. Compatible with HARD RULE 13.

**1.4 Each inline tag mention is binding weight. [NEW]**
Aliasing tags to variables (`INSERTS = @A + @B`, then referring to "INSERTS") measurably thinned identity
binding. Repeat the actual tag at every use site. A tag is not a variable name; it is the binding.

**1.5 Describe nothing the reference already owns. [CONFIRMS]**
Matches HARD RULE 13. Prose competes with the ref and sometimes wins. Corollary from Paola: **if the
structural ref draws it (pose, prop-in-hand, placement), do not restate it in words** — restating gives
the model a second, competing authority.

---

## 2. PROMPT-FORMAT LAWS (nano stills: proxies, key stills, plates, elements)

**2.1 ★ PROSE IS IN-DISTRIBUTION; NOTATION IS NOT. [NEW — explains draw-to-draw variance]**
Image models are trained on captions and photo descriptions. Equation-style notation (`X = a + b → c`)
is code-shaped: the model must *translate* it before rendering, and translates it **slightly differently
every draw**. That translation variance is inconsistency. **Consistency across draws is the signature of
on-distribution prompting.** For anything needing repeatability — 48 proxies, 24 key stills — write
flowing prose. Notation is fine for human-facing spec docs; it is not fine in the prompt box.

**2.2 Do not mix registers at the entity layer. [NEW]**
A formula skeleton with prose entity sentences performed **worse than either pure form** — one draw came
back a literal photographic negative, the other with the composition mirrored. Pick one register per
prompt.

**2.3 "color-negative" in notation context renders as an image operation. [NEW]**
`GENERATE one color-negative photograph = ...` inverted the frame. Safe form: *"a still photograph on
real color-negative **film**"* — the noun is *film*. General rule: notation changes how technical nouns
are parsed.

**2.4 Bind related things into ONE grammatical unit. [CONFIRMS]**
Matches HARD RULE 14. Extension from Paola: a **character** is an entity — her identity, wardrobe, pose,
location and prop belong in one sentence. Split across separate lines, the model merges them differently
each roll.

**2.5 Negations belong ONLY in the closing filter. [NEW — refines HARD RULE 10]**
An inline negation primes its own nouns at the exact decision site. `"crouched at the veranda edge, never
on the gravel, never seated"` primed *gravel* and *seated* precisely where placement is decided. Put every
ban at the end, after all positive description, where the model treats it as a quality filter.

**2.6 State screen side in words. [NEW — directly relevant to this reel]**
A structural/blueprint reference alone does **not** hold screen direction under a generative register.
Dropping the words "frame-left" produced a mirrored composition. Since this reel runs L→R across worlds
1–4, flips to R→L in world 5, and returns L→R in world 6, **every prompt states the side explicitly**
in text — in addition to `BOARDING_SPEC`'s map-and-cross-product discipline.

**2.7 Gaze: the target outranks the angle. [NEW]**
Name **who** they look at; never specify a face angle. An angle word ("near-frontal", "turned across the
frame") is a *turn* instruction and it beats the look. Two reference frames for one head = a coin flip.

**2.8 Position ↔ gaze coupling. [NEW]**
An unstable placement produces an unstable eyeline — the model computes the look *from wherever it put
her*. **Never debug gaze before placement is deterministic.** Fix placement first, by pure defer to the
structural reference.

**2.9 Texture spec scales with pixel budget. [NEW]**
Prompting pores / nostril shadow / individual hairs on a distant figure yields a face **sharper and
cleaner than its own depth plane** — the overprocessed tell. Write "depth-appropriate skin and cloth
response" for anything not in close-up.

**2.10 ★ CLOSING THESIS LINE. [NEW — graft from the JSFILMZ Vault, 500 pro prompts]**
54% (272/500) of professional prompts end on one short **non-technical** sentence stating the shot's
point: *"Arrival as intimidation." "Time as the only character."* It gives the model a single
interpretive target for every micro-decision the prompt does not specify. Absent from our formats.
**Add one to every board panel and key still.** For this reel each shot already has one — the beat's
argument. W1-S4: *"The apex, held longer than physics allows."*

**2.11 Concision is confirmed at scale. [NEW]**
Same corpus: **average 74 words, 4.2 sentences.** Positional grammar measured across 500 prompts: camera
move and subject go **first**, technical/lens/grade go **last**. Our long prompts are outliers, not
craft.

---

## 3. WORKFLOW LAWS

**3.1 ★ COMPOSITE INTO A LOCKED PLATE — do not re-render the world. [NEW — highest-value workflow graft]**
When an at-standard environment plate exists, the strongest operation is **insertion**, not
reconstruction: the plate is a locked photographic base, preserved pixel-for-pixel except where the
inserted figure occludes it, grounds a contact shadow into it, or throws a source-consistent cast shadow
across it. Two consequences, both measured: **environment realism becomes free** (those are preserved
pixels, not generated ones), and the model's whole budget goes to the figure. This is also the operation
Google documents first-class. **Directly applicable:** this project has four plates per location and
`Loc-<Name>` elements. Key stills should insert characters into them, never regenerate the location.

**3.2 Base defects are editor-recoverable; staging and identity are not. [NEW]**
If a draw nails staging and identity but drifts the grade, or loses the moon, or warms the palette —
**keep it**. Those live in the base layer you already own as a separate asset; mask and correct in
Resolve. QA staging and identity first, treat base defects as post.

**3.3 Wrong-but-consistent beats wrong-and-inconsistent. [NEW]**
A consistent error is a fixable prompt. Inconsistent output is a slot machine, and no amount of wording
converges it. When choosing between formats, choose the one that repeats.

**3.4 Batch discipline: judge N together, not one at a time. [NEW — refines HARD RULE 1]**
At a realistic 1-in-4 hit rate, sequential single draws read as constant failure even when the band
exists. Fire the allowed attempts as a **batch**, then cherry-pick. HARD RULE 1's "three attempts, no
fourth" stands — this changes only how they are judged.

**3.5 Two word-rounds, then change channel. [NEW]**
If two revisions fail on the same named defect, the word channel is saturated. Switch channels: a
targeted edit, a crop-scale re-render, a geometry change, a different shot. Paola lost roughly two weeks
to round six through fifteen of wordsmithing.

**3.6 Targeted edit is the sanctioned finisher. [NEW]**
Google documents text-defined semantic masking: *"change only the [element] … keep everything else in the
image exactly the same, preserving the original style, lighting, and composition."* For a face that
misses at scale, the fix is a **face-only edit pass on the keeper**, or a full-res crop re-rendered and
composited back — not another full generation.

**3.7 Animatic before polish. [CONFIRMS — now with an external receipt]**
Pixar editor Ken Schretzmann: *"In live-action you shoot first and edit later. In animation you edit
first and shoot later."* Cut decisions are cheap at the animatic stage and prohibitive after. This
project's gate is already the animatic; the doctrine confirms it is the correct gate, and that **no
polished still should be generated until the animatic proves the handoffs.**

**3.8 Segment-lock against a dated milest***REMOVED*** [NEW]**
Micro-budget feature practice (Noam Kroll): lock the edit **reel by reel** against a hard external date;
each locked segment advances immediately to sound/finish while the rest iterates, with one master
timeline holding continuity. **Applied:** lock world by world. A locked world goes to finish; unlocked
worlds keep iterating. The lock serves the date, not aesthetic completion.

---

## 4. A PRE-SPEND RISK SCORER (Vault graft, mechanical, weak-model runnable)

Score any prompt **before** firing. Start at 0, add:

| +1 each | |
|---|---|
| carries a negative list | +2 |
| "lens switches to" mid-shot | +1 |
| intercut / high-speed insert | +1 |
| ≥3 variable slots | +1 |
| >95 words | +1 |
| crowd · stampede · riot · **dancers** · battle · army · swarm · pack of · herd | +1 |
| **parkour · flip · somersault · cartwheel · backflip · tumble · acrobat** | +1 |

**≤1 → ★★★ · ≤3 → ★★ · else ★.** The source library scores 348 / 149 / 3.

**Every risk term is a failure mode someone already paid to discover.** Two of them are in this reel's
own beat map: **W1-S4 kickflip** (flip) and **W2 dancers/ring** (dancers), and **W3-S1 tumble**. Those
three shots are pre-flagged as the reel's hardest generations — budget extra attempts there and design
the boards to reduce risk (apex only, no full trick — already the rule; dancers as a *ring* behind her
rather than individually choreographed bodies).

---

## 5. WHAT DOES **NOT** TRANSFER

- **Paola's continuity apparatus.** The short film's cross-shot identity/geometry ledger existed because
  one location and one wardrobe ran across 20+ shots. This reel is six independent worlds — continuity
  cost is at the **six anchored cuts only**, not everywhere.
- **The reconstruction paradigm.** Blueprint-fill (rebuild the whole frame from line art) was Paola's
  method for a set with no at-standard plate. Here the plates exist — composite instead (§3.1).
- **A handheld-with-breath default and flat-gray unlit reference plates** — both conflict with
  this project's locked-camera and baked-plate approach. Graft mechanisms, not defaults.
