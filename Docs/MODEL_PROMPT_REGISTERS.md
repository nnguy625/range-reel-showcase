# NANO BANANA PRO vs GPT IMAGE 2 — how each one actually wants to be prompted
### Researched 2026-07-29 from first-party vendor docs. **This changes our house output format.**

---

## THE HEADLINE

**Neither pure natural language nor pure spec. It is LABELLED STRUCTURE WITH NARRATIVE CONTENTS —
and the two models want different variants of it.**

Our SHOT SPEC v2 has **the labels right and the contents wrong.** We write middot-separated fragments
inside each label. Google's own guidance says fragments are exactly what fails.

---

## TIER 1 — FIRST-PARTY VENDOR DOCS (authoritative)

### Nano Banana Pro / Gemini 3 Pro Image — Google

| Finding | Exact wording |
|---|---|
| **Narrative, not keywords** | *"A simple list of keywords won't cut it; you need to describe the scene narratively."* |
| **Text-to-image formula** | `[Subject] + [Action] + [Location/context] + [Composition] + [Style]` |
| **Reference formula** | `[Reference images] + [Relationship instruction] + [New scenario]` |
| **Preservation** | *"You can define a 'mask' through text to edit a specific part of an image while leaving the rest untouched."* → *"Be explicit about what to keep exactly the same."* |
| **🔴 POSITIVE FRAMING** | *"Describe what you want, not what you don't want (e.g. 'empty street' instead of 'no cars')."* |
| **Camera IS honoured** | *"Use specific hardware and photographic terminology to control the depth, distortion, and perspective."* Named f-stops, lens types, camera bodies all work. |
| **Materiality** | don't ask for "suit jacket," ask for *"navy blue tweed"* |
| **Reference count** | **6–14** images depending on surface |
| Pro-specific register | *"narrative descriptions with structured elements"* — labelled categories whose contents are narrative |
| Detail level | *"While simple prompts still work, achieving professional results requires more specific instructions."* |

### GPT Image 2 — OpenAI cookbook

| Finding | Exact wording |
|---|---|
| **Register is agnostic** | *"Minimal prompts, descriptive paragraphs, JSON-like structures, instruction-style prompts, and tag-based prompts can all work well"* — but *"prioritize a skimmable template over clever prompt syntax."* |
| **Order** | **background/scene → subject → key details → constraints** |
| **Reference addressing** | *"Reference each input by index and description ('Image 1: product photo… Image 2: style reference…')"* |
| **Edits** | *"change only X"* + *"keep everything else the same"*, and **repeat the preserve list on each iteration** to reduce drift |
| **🔴 NEGATIVES WORK HERE** | *"State exclusions and invariants explicitly ('no watermark,' 'no extra text,' 'preserve identity/geometry/layout')"* |
| **🔴 CAMERA IS LOOSE** | *"detailed camera specs may be interpreted loosely, so use them mainly for high-level look and composition rather than exact physical simulation."* |
| **Photorealism trigger** | *"include the word 'photorealistic' directly in the prompt"* — or "real photograph", "taken on a real camera" |

---

## THE DIVERGENCE TABLE — they are OPPOSITE on three axes

| Axis | Nano Banana Pro | GPT Image 2 |
|---|---|---|
| **Register** | narrative sentences inside labelled sections; **keyword fragments explicitly fail** | skimmable template is fine, even JSON-like |
| **Negatives** | ❌ **avoid** — convert to positive substitutes | ✅ **use** — explicit invariant lists, repeated every round |
| **Camera specs** | ✅ honoured — lens, f-stop, body, angle | ⚠ **interpreted loosely** — look and composition only |
| **Reference model** | relationship instruction — *what job does this ref do* | index + description — *"Image 1: …"* |
| **Ordering** | Subject → Action → Location → Composition → Style | Scene → Subject → Details → Constraints |

---

## 🎯 WHY THIS EXPLAINS NELSON'S EXACT A/B RESULTS

His verdicts, and the mechanical reason for each:

| His observation | The documented cause |
|---|---|
| *"nano — i like this look better"* | Nano **honours** camera/lens/lighting/film language. Our look block is strong and nano is the only one of the two that fully reads it. |
| *"nano drifted her face"* / broke the room | We handed nano a **fragment sheet**. Google says a keyword list *"won't cut it."* With no narrative binding pier → pocket → drape → corridor, it invents the relationships. |
| *"GPT2 seems to have her tuck in this corner & change geography"* | GPT2 **interprets camera specs loosely.** Our precise 80cm/35mm/past-the-pier block is near-inert on GPT2, so it re-placed the camera and rebuilt the room to suit. |
| *"gpt2 has some identity but she looks super older"* | We never gave GPT2 the thing its docs ask for — an **indexed reference list plus an invariant preserve list repeated every iteration.** |

**All four rejects are explained by prompting each model in the register the other one wants.**

---

## ⚠ WHERE THIS CONTRADICTS OUR OWN RULES

1. **`negation-summons-the-noun` is now confirmed — but only for nano.** Google's positive-framing rule is a
   third independent confirmation of our measured Suno finding and Franco's positive-material-lock ruling.
   **But OpenAI documents the opposite for GPT2.** So the negative block is not universally wrong — it is
   **model-specific.** Our single house negative block has been wrong on one of the two models the whole time.

2. **The skill bans glossy-render keywords — but "photorealistic" is OpenAI's documented trigger word for
   GPT2.** The ban was written against nano-style models. Worth a controlled A/B; do not assume the ban
   generalises.

3. **We cap ourselves at 3–5 references. Nano Pro takes 6–14.** The 4–5 ceiling is the **Seedance 2.0** limit,
   not a nano limit — see `SD2_GUIDE_FINDINGS.md`. We have been importing a video-model constraint into
   still generation.

---

## ✅ THE FIX — ONE SPEC, TWO RENDERS

**Keep SHOT SPEC v2. Its job is to stop us omitting a job, and it works** — Franco caught two omissions
through it this week (the framing contradiction, the missing skin governor). It is the **internal ledger.**

Then **emit a model-specific render from it:**

### Nano render
- same section labels, but every line becomes a **complete descriptive sentence**
- middots and fragments removed
- every negative converted to a positive substitute
- keep the full camera block — nano is the one that reads it
- reference headers stay as **relationship instructions** (Franco's `REFERENCE ONLY for the identity of the
  room` is textbook Google — it IS the *"[Relationship instruction]"* slot in their multimodal formula)

### GPT2 render
- keep the skimmable template
- reorder to **scene → subject → details → constraints**
- address refs by **index + role**: `Image 1: the room. Image 2: her face. Image 3: her wardrobe.`
- **explicit invariant list, restated every iteration**
- keep the negative block — it works here
- demote the camera block to look-and-composition; expect the geometry to come from the plate, not the numbers
- include the literal word **photorealistic**

---

## 🧪 THE FREE TEST

Plate One has no character and no weapon, so it is the perfect control. **Generate it twice on Unlimited:**

- **A** — the ratified spec-style version in the World 3 plate review loop (kept private)
- **B** — the narrative-contents rewrite below

One variable: prompt register. Same model, same refs, same settings. Costs nothing.

### PLATE ONE — B, the nano-native rewrite

```
@Loc-Hotel-Cover is the reference for the identity of this room only. Take from it the architecture, the
materials, the placement and scale of every object, the way light behaves, and the physical relationship
between the draped opening, the pier, the right-hand wall, the luggage cart and the corridor. Do not take
its camera position, framing, crop or composition. This is a new camera placed inside that same unchanged
room.

The camera sits low, eighty centimetres off the floor, on a 35mm lens, pushed forward just past the plane
of the near right-hand pier so that the lens looks into the narrow pocket formed between that pier and the
right-hand wall. The pier stands right of centre with its full near face toward us, and its mass clearly
separates the pocket from the open corridor beyond. The pocket is a shallow dead end that terminates
against the right-hand wall; the floor does not continue past the pier on both sides, and there is no
further passage behind it. The right-hand wall runs unbroken along the back of the pocket. Away to the
left, the draped opening stands where it has always stood, and the corridor recedes into depth behind it.
The pocket itself is empty.

Every wall, pier, moulding and opening in this corridor is cream-painted plaster and painted panelling,
stone, dark brass, velvet and polished dark marble, and those are the only materials present anywhere in
frame. The wall sconces keep the exact positions, spacing, count and warmth they have in the reference.
The brass luggage cart stands where the reference puts it.

The sconces are the only working light along the corridor. Each is a warm tungsten fixture at mid-wall
height that holds one small contained pool of light on its own panel and dies out within a few feet, so
long unlit runs of open black separate one from the next. Beyond the draped opening a warm glow sits in the
far distance; it rims the edge of the drape and reaches nothing forward of it. No sconce reaches into the
pocket, which stays unlit.

This is a real photograph made at night on 35mm film, with fine natural grain, and most of the frame is
unlit negative space. Every source in it is warm-neutral, and the far shadows settle into a neutral
charcoal lit by nothing coloured. The corridor is empty of people. The image carries no added lighting, no
synthetic bloom, and no lettering, marking or emblem of any kind.
```

**Note what changed and what did not.** Same geometry, same materials, same light map, same reach fences —
nothing was softened. Only the *register*: sentences instead of fragments, and the four negatives at the end
rewritten as positive statements of what IS there. If B beats A on the pocket geometry, the register was the
bug all along, and every prompt in this project gets rewritten this way.

---

## 📌 THE SECOND FINDING — FRANCO IS QA'ING BLIND

Three of his tool routes are down at once:

1. *"I can't directly render the image from this interface right now"* — he cannot generate.
2. The **Drive connector** hangs ~8 min and returns nothing.
3. *"The direct CDN fetch failed on my side again"* — **twice now**, on links that HEAD-test 200 from here.

**So he ruled on four rejected images he never actually saw.** Round 1 through 3 were built from my text
description of them plus one plate Nelson had uploaded earlier in the thread.

That is why his rulings have all been **procedural and format-level** — build a plate, change the head
percentage, branch the skin block, rename the reference header. Every one is excellent and every one is
derivable from the prompt text al***REMOVED*** **None of them is a visual call**, because he cannot make one right now.

**Two consequences:**
- **Nelson has to attach plates directly in the thread**, every round. The CDN link route in
  `PLATE_CDN_LINKS.md` is no longer dependable and must not be assumed.
- **Franco cannot catch a register problem**, because a register problem only shows up in the returned
  image. Three rounds went into redlining the *content* of a spec-style prompt and neither of us questioned
  whether spec style was right for nano. **That is exactly the gap a second brain closes.**
