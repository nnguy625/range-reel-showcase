# PROMPT PATTERN — the house form, extracted from what has actually worked here

*Written 2026-07-27 after a cloud session drifted off-pattern and broke a wardrobe sheet (elongated
necks, missing sunglasses). Every rule below is extracted from prompts in THIS repo that produced
approved assets — not from doctrine imported from the parked short film. Receipts are cited.*

**Read this before writing any generation prompt. If a prompt does not look like the examples in
`LOCATION_PLATES.md`, it is off-pattern.**

---

## THE SIX RULES

### 1. Plain descriptive prose. No labels, no blocks, no notation inside the prompt body.
One flowing description. No `SHOT:` / `LIGHT:` / `CAPTURE:` headers, no `X = a + b`, no bullet lists
of parameters mid-body. `ASSET_SPEC.md` states it directly: *"Written in the concise prose register:
one entity bound in a single grammatical unit, in-distribution language, parameters as a short list at
the end. Not a formula, not a spec dump."*

### 2. Concrete repetition, never an abstract rule.
For any variation on an existing asset, name three or four **specific objects** that must persist:

> *"The same Southern California residential street, **same houses, same parked cars, same palms,
> same midday light**, photographed from the opposite direction."*

Never write a general law and expect the model to apply it across several elements. The approved
back-panel instruction names ONE element and gives the reason:

> *"Because she is facing away, her right side appears on the RIGHT side of this panel — **the flower**
> must sit on the opposite side of the frame from where it appears in the front-facing crop."*

**Receipt:** an abstract substitute — *"each asymmetric detail appears on the opposite side of the
frame from where it would in the front view"* — covering four elements at once, broke the sheet.

### 3. Camera in real units.
"eye level about 1.6 metres, 24mm lens" · "about 30 centimetres off the road surface, 35mm lens,
tilted slightly up." Height in metres or centimetres, lens in mm, position in plain words.

### 4. The craft block is a CONSTANT. Append it unchanged; never rewrite it per prompt.
`LOCATION_PLATES.md` carries one SHARED CRAFT BLOCK — including its never list — appended to every
plate prompt identically. The never list is **not** re-authored each round.

**Receipt:** writing a bespoke never list every attempt, growing it reactively, is what drove constraint
load up until anatomy paid for it. A ban earns a permanent place in the block or it does not exist.

### 5. Short. 80–120 words for a plate.
The approved plate prompts are that long. Length is not thoroughness; it is competition for attention.

### 6. Order: subject and shot first, then camera, then content, then light, then the constant block.
Front position carries the most weight. Spend it on what the image IS, never on fabric detail or
housekeeping.

**Receipt:** front-loading a long wardrobe sentence ahead of the panel structure produced a sheet whose
panels were mis-proportioned — the structural instruction had been buried.

---

## THE ORDER OF OPERATIONS — proven, do not shortcut

From `LOCATION_PLATES.md`, corrected after the first SoCal set came back as four different streets:

1. Generate the **hero** al***REMOVED*** Approve it.
2. Save it as an **element**.
3. Generate every variation with that element **attached**, opening with the world-reference line.
   Variations are *variations on an image*, never fresh descriptions.

> **Generating a matched set from text alone does not work.** A description makes the model invent a
> new thing that matches the description. Four generations = four different places.

Same law on the character side (`ASSET_SPEC.md`): the wardrobe test-pass gate comes first — the outfit
approved on a neutral body — *then* the sheet. **Never generate the sheet from a description al***REMOVED*****

---

## REFERENCES: WHO OWNS WHAT

- **Identity comes from the attached face element. Nothing else describes the face.** (`ASSET_SPEC:30`)
  But DO enumerate what must match — *"matching @Face exactly — same face, same sunglasses, same
  flower on her right, same earrings."* Naming the match-targets is not describing the face.
  **Receipt:** dropping that enumeration lost the sunglasses entirely.
- **ONE face reference per generation, never two.** Two sources average into a third person.
- **Describe nothing an attached reference already owns** — but everything no reference owns must be
  described, or the model invents it. **Receipt:** the Bollywood sheet cropped above the feet, so
  ankles, hem length and footwear were all up for invention.
- **Fix the ref, not the never list.** An accessory that keeps appearing is arriving on a reference.

---

## WHEN IT BREAKS

1. **One variable per retry.** (`STATE.md` HARD RULE 2.) Patch the working prompt; never rewrite it.
   **Receipt:** a from-scratch rewrite changed six things at once and broke a sheet that had been fine.
2. **Three attempts, no fourth.** (HARD RULE 1.)
3. **If a multi-panel generation drifts, stop re-rolling it** — generate the panels separately and
   assemble. Multi-panel single-generation is the highest-difficulty operation available; on the parked
   film it failed ten consecutive rounds on two different engines.

---

## THE DRIFT THIS DOCUMENT EXISTS TO PREVENT

A session that has been working on a different project will import that project's register and laws.
The parked short film ran experiments in formula and notation registers; **none of that belongs here.**
This project's proven register is plain descriptive prose with a constant craft block, and its receipts
are in `LOCATION_PLATES.md` and the approved wardrobe sheets.

**Before writing a prompt: open the nearest approved example and match its shape.**
