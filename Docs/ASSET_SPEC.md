# ASSET SPEC — reference sheet standards

*How every reference asset is built. Locked 2026-07-25.*

**Governing law:** exactly one reference owns each variable. If a variable has no owner, the shot does not get sent.

| Variable | Owner |
|---|---|
| Face and identity | `Paola_Face_Lock` element, **three angles** — see below |
| Body proportions, silhouette, posture | Body reference sheet, neutral fitted clothing |
| Hair silhouette | Fixed across all six worlds, defined once |
| Wardrobe | Per-world 3-panel headless sheet |
| Held objects | Per-prop multi-angle sheet |
| Location | Per-world environment plate |

Nothing describes the face except the face element. No wardrobe sheet, prop sheet, environment plate, or shot prompt is permitted to mention her features.

### Two corrections to the master face reference

**Remove the pink flower.** It leaks into the skate, agent and couture looks and makes them read as *dressed* rather than inhabited. The flower belongs to one world at most; the master belongs to all six.

**Build left and right three-quarter references from the same face.** A frontal image alone cannot police her nose, jaw and eye shape across three wardrobe panels and eighteen shots. Three angles, one identity.

**Permanent hair silhouette:** long black hair in **tight, defined spiral curls with clear ringlet separation**, voluminous and springy, falling past the shoulders. Stated identically in every prompt, never paraphrased, never changed per world. It is a second identity channel and changing it throws that channel away for nothing.

*(Director's ruling 2026-07-25, superseding the sleek-low-bun proposal. "Curly" alone renders as a loose wave — the curl pattern must be named or it defaults soft. Add "no loose waves" to the never list.)*

**Continuity anchor:** the small hoop earrings already present, standardised as **warm-gold huggies** in the clean identity master. They survive every neckline, sit correctly with both the sari and the kimono without hijacking either, and give a third identity signal alongside face and hair.

**The identity elements, as built** *(2026-07-26)*. The clean face master now exists as a named element, **`Pao-Face-CU`** — flower removed, sleek centre part, gold huggie hoops, black tank. The Bollywood world carries its own identity element, **`Pao-Face-Bolly`**. These are the elements attached under the `@face` role; nothing else describes the face.

---

## 1. WARDROBE SHEET — 3 panels, headless, full body, front

One per world. Six total; World 5's kimono sheet already exists.

**Layout.** Three panels, cleanly divided, equal width. Mid-grey seamless background, identical across all panels and all sheets. Even soft frontal light, no hard shadow, no rim, no atmosphere. Identical wardrobe, proportions and scale across all three.

**The three panels each do a different job** — this is the two-headless-panel structure, face in exactly one panel:

| Panel | Content | Why |
|---|---|---|
| Left | Full body **front, genuinely headless** | Wardrobe front with no face to average |
| Middle | Full body **back, with head** | Headwear and curl mass from behind, for the backward-tracking shots. The back of a head cannot average into a face |
| Right | **The approved chest-up crop** | Identity, in one panel only |

**Headless means absent, not masked.** *(Correction 2026-07-25 — "head replaced by a grey oval" produced a grey oval face on an intact head wearing the beanie.)* Write it as: the figure ends cleanly at the shoulder line, no head, no neck, no neck stub, no hair. A garment on a headless mannequin torso. Put "no grey oval face, no mask, no mannequin head" in the never list.

**Headless instructions leak.** *(Failure class logged 2026-07-26.)* Writing that a body part is "simply absent" does not stay where you put it — the model generalises the amputation to other parts. It removed both hands from a front panel. An absence has to be **bounded**: state that **only the head and neck** are absent, that the body is **otherwise whole**, and give the hands a defined position — *"arms relaxed at her sides with both hands fully visible and complete, five fingers each."* Any body part left unstated is a part the model is free to delete.

Add to the never list: "no missing hands, no amputated or truncated limbs, no arms ending at the wrist."

**Asymmetric elements mirror on back panels.** *(Failure class logged 2026-07-26.)* A flower worn on her right appeared on the same side of the *frame* in both the front and the back panel — which puts it on the wrong side of her head the moment she faces away.

**Standing rule:** any asymmetric element — flower, pallu drape, waist-tied hoodie knot, holster — must have its side named **relative to her body and also relative to the frame in that specific view**. "On her right" alone lets the model hold frame position and swap her body; "left of frame" alone lets it swap her sides. Naming only one of the two produces the mirror.

**Why one face panel only:** attaching a multi-face sheet alongside the face element makes the model average faces. One panel carries identity; the other two carry wardrobe. The sheet carries wardrobe, the crop carries identity.

**Panel count is a resolution decision.** At 16:9 4K, three equal panels give each roughly **1280px of width**, so a chest-up crop rendered *inside* a sheet is always softer than a dedicated 4K close-up. Where the identity crop already exists as its own element, panel three is a downscaled duplicate of an asset already held at full resolution. **In that case, build the sheet as two panels at 4:3** — front headless, back with head — and let the element carry identity.

**Order of operations.** Wardrobe test-pass gate first — the outfit rendered and approved on a neutral body, silhouette and fabric verified — *then* the sheet. Never generate the sheet from a description al***REMOVED***

**Production method — generate fresh. Do not edit.** *(Director's ruling 2026-07-25, overriding the earlier edit-in-place approach.)* Editing an existing image degrades quality — the edit inherits the source's resolution ceiling and compression, and every subsequent pass compounds it. Each sheet is generated clean at 4K.

Written in the concise prose register: one entity bound in a single grammatical unit, in-distribution language, parameters as a short list at the end. Not a formula, not a spec dump.

**Downstream usage line, in every shot prompt that attaches it:**

> @wardrobe is WARDROBE REFERENCE ONLY. Ignore the mannequin head. Copy the outfit exactly.

### The six wardrobes

**Five sheets.** Worlds 3 and 4 share one costume. The opening costume returns unchanged at the close.

### Her palette — what works against this face

Warm medium-tan skin, dark high-contrast hair and brows, warm brown eyes, oval tapered face, defined collarbones.

**Strong near the face:** pomegranate red, midnight indigo, deep forest, blackened aubergine, warm ivory, burnished gold.
**Flattens her, avoid:** beige, pale champagne, dusty grey, washed pastel pink.
**Necklines that frame her:** clean square, open V, precise asymmetry.

### The five costumes

| Sheet | Worlds | Design |
|---|---|---|
| Urban skate **LOCKED 07-25** | 1 and the close | Loose white scoop-neck tank, wide straps, deep armholes, soft curved hem, one small chest pocket, draping jersey. Fitted black athletic tank underneath showing at the neckline and through the side armholes as a crisp black border. Matte black high-waisted full-length leggings. Lightweight black zip hoodie tied at the waist, sleeves centred front, body behind the hips. Low-profile black skate shoes, black laces, restrained white midsoles. Soft black cuffed beanie, or a curved-brim black cap — **never a flat brim** |
| Bollywood | 2 | Vivid deep red sari, fitted square-neck sleeveless blouse, fluid and wrapped close through waist and hips, **narrow antique-gold border only**. Sunglasses with a light enough tint that her eyes stay readable. Crowd sits in dusty teal |
| Agent | 3 and 4 | Blackened-aubergine bodysuit under a structured graphite cropped jacket, high-waisted narrow trousers, matte boots |
| Kimono | 5 | Midnight indigo, black-plum obi, restrained oxblood sleeve lining |
| Strut | 6 | **Burnished old gold, not pale champagne.** Simple bias-cut column with one darker bronze pleated fan at the hip |

### The silhouette collision — Bollywood and couture

These two are the pair at risk of reading the same, since both can become floor-length asymmetric drapery. Separate them deliberately:

| | Bollywood | Couture |
|---|---|---|
| Waist | visibly bared | uninterrupted through the torso |
| Line | soft, diagonal | vertical, architectural |
| Surface | matte silk | metallic |
| Gold coverage | **~5%**, trim only | **~80%**, the whole image |

That gold ratio is the point. **World two whispers gold. World six detonates it.**

**Urban silhouette law:** fitted through the legs, relaxed through the torso. Narrow lower body under a casual layered upper body. Athletic, agile, quietly stealthy — never oversized streetwear. White appears in exactly two places, the outer tank and the shoe sole; a third white element means the palette drifted.

**Never on the urban look:** costume-stereotype styling, biker styling, gymwear, tactical clothing, baggy menswear, polished fashion editorial.

**The board is present at the open and absent at the close.** Same clothes, same walk, no board. She began carrying the thing that started the journey and returns without needing it. It also removes a prop, a hand-contact region and a rigid-body geometry from the single most transformation-heavy shot in the reel.

**Why worlds 3 and 4 share a costume.** The hard cut between them was the plan's weakest seam, because a wardrobe change at a cut between two adjacent action worlds reads as a continuity error rather than a world change. Holding the costume constant while the world flips from cold nocturnal corridor to sunlit dusty road makes the change unambiguously environmental. The world does the work; the costume stays still.

**Colour separation rule.** In any shot with a crowd, she must be the only instance of her colour in frame. Crowd sits in one restrained family; she carries the one that does not repeat. This is costume design doing engineering work — it makes her findable in a busy frame and doubles as an identity signal.

---

## 2. BODY SHEET — the missing owner

One sheet, built once, used in every world.

Neutral fitted clothing — plain, close to the body, nothing that hides proportion. Same three-panel layout, same grey seamless, same lighting. **Headless, same grey oval.**

This owns height, shoulder width, waist and hip proportion, limb length, and standing posture. Without it, six wardrobes can produce six differently-built women wearing related versions of the same face.

**Known limitation:** a static sheet cannot own gait, weight distribution, or movement identity. Those are checkable after the fact but not enforceable in a prompt. Flagged as an open risk.

---

## 3. HAIR — defined once, fixed everywhere

One hairstyle silhouette across all six worlds, stated identically in every prompt. Not "hair appropriate to the world." A recognizable shape that survives wardrobe change is a second identity channel, and changing it throws away that channel for no gain.

Write it as a short fixed phrase, reused verbatim, never paraphrased.

---

## 4. PROP SHEET — multi-angle turnaround

One per held object. Built like a character sheet.

**Layout.** Cleanly divided panels, equal size, mid-grey seamless background identical to the wardrobe sheets. Even soft light, no hard shadow, no reflection, no environment. The object floats at consistent scale and consistent distance in every panel.

**Angles — as many as the object justifies.** Minimum four, and the panel count is stated in the prompt so the model divides the frame cleanly rather than inventing a layout.

| Prop | Panels |
|---|---|
| Sword | Full length side, full length reverse side, hilt and guard detail, blade tip detail, sheathed, and the sheath alone |
| Sidearm | Left profile, right profile, top-down, muzzle-on, grip detail |
| Skateboard | Deck top with griptape, deck underside with graphic, side profile, three-quarter, trucks and wheels detail |

**Why props get their own sheet, restated.** Two reasons, and both matter.

First, state change. Anything drawn, pulled, ridden, set down, or that appears and disappears must hold its appearance independently of the body carrying it.

Second, hand contact. Held objects sit in the highest-failure-rate region of any frame, so they earn a dedicated reference at maximum detail.

**Wardrobe, by contrast:** belts, jewelry, footwear, obi. Worn and static. Sunglasses are wardrobe unless she removes them, at which point they become a prop.

**Continuity anchor.** One small piece of jewelry persists across all six worlds and is named in every prompt as a continuity line. Cheap to check frame to frame, and it functions as a third identity signal alongside face and hair.

---

## 5. ENVIRONMENT PLATE — per world

Empty location, no character. Shot at the exact light the world runs in. Where the world contains a crowd shot, the plate is captured at soft even light — golden hour or equivalent — because hard shadow logic across many bodies is the fastest way to break a frame.

Approved plate becomes the location reference and is attached with an explicit scope line:

> @location is LOCATION REFERENCE — this exact place at this exact light.

---

## 6. THE PROMPT CONVENTION

Every reference carries a stated role and an explicit scope limit. Pattern taken from working professional prompts:

```
@face is the performer — identity only.
@body is BODY REFERENCE ONLY — proportions and posture. Ignore the clothing.
@wardrobe is WARDROBE REFERENCE ONLY — ignore the mannequin head, copy the outfit exactly.
@prop is PROP REFERENCE ONLY — this exact object.
@location is LOCATION REFERENCE — this exact place at this exact light.
```

Identity gets belt and suspenders: the face reference **and** a short written feature list, stated the same way every time.

Composition and prohibitions close the prompt, not open it. A quality bar line ends every prompt, and its last term is negative.

---

## 7. BUILD ORDER FOR ASSETS

1. Body sheet and hair definition. Everything else inherits from these.
2. Five wardrobe sheets, generated fresh at 4K. Never edited — see the production-method ruling above.
3. Six identity tests — one medium shot per wardrobe, face large and stable. **Blind-test these on people who do not know her: one woman or several?** Nelson's own recognition does not count as evidence, because he knows what the model was supposed to produce.
4. Props.
5. Environment plates.

Stills are flat-fee unlimited at 4K. Retries here are free. Spend them.
