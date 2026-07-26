# ASSET SPEC — reference sheet standards

*How every reference asset is built. Locked 2026-07-25.*

**Governing law:** exactly one reference owns each variable. If a variable has no owner, the shot does not get sent.

| Variable | Owner |
|---|---|
| Face and identity | `Paola_Face_Lock` element |
| Body proportions, silhouette, posture | Body reference sheet, neutral fitted clothing |
| Hair silhouette | Fixed across all six worlds, defined once |
| Wardrobe | Per-world 3-panel headless sheet |
| Held objects | Per-prop multi-angle sheet |
| Location | Per-world environment plate |

Nothing describes the face except the face element. No wardrobe sheet, prop sheet, environment plate, or shot prompt is permitted to mention her features.

---

## 1. WARDROBE SHEET — 3 panels, headless, full body, front

One per world. Six total; World 5's kimono sheet already exists.

**Layout.** Three panels, cleanly divided, equal width. Mid-grey seamless background, identical across all panels and all sheets. Even soft frontal light, no hard shadow, no rim, no atmosphere.

**Panels.** Full body front, full body front three-quarter, full body back. Same scale, same standing pose, same distance in every panel. Feet visible, shoes included.

**Headless.** The head is replaced with a smooth neutral grey oval — an anonymized mannequin head. Not cropped, not blurred, not a floating collar. A clean grey oval where the head would be.

**Why headless is non-negotiable:** attaching a sheet with a face alongside the face element causes the model to average two faces. Removing the head leaves identity with exactly one owner.

**Production method — generate fresh. Do not edit.** *(Director's ruling 2026-07-25, overriding the earlier edit-in-place approach.)* Editing an existing image degrades quality — the edit inherits the source's resolution ceiling and compression, and every subsequent pass compounds it. Each sheet is generated clean at 4K.

Written in the concise prose register: one entity bound in a single grammatical unit, in-distribution language, parameters as a short list at the end. Not a formula, not a spec dump.

**Downstream usage line, in every shot prompt that attaches it:**

> @wardrobe is WARDROBE REFERENCE ONLY. Ignore the mannequin head. Copy the outfit exactly.

### The six wardrobes

Six sheets. Worlds 3 and 4 share one costume.

| Sheet | Worlds | Note |
|---|---|---|
| Urban skate | 1 | Skate shoes, cap, tank top. Casual and attractive, never costumey. The tell that she skates is the stance and the shoes |
| Bollywood | 2 | **Must not repeat the crowd's colour family.** See colour separation below |
| Agent | 3 and 4 | One costume across both worlds |
| Kimono | 5 | Closed, obi. Sheet already exists |
| Strut | 6 | Gold couture, bias cut. Fabric must move on every step; a stiff garment kills the walk |
| Casual | closing | Returns her to the opening register |

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
2. Six wardrobe sheets, produced by editing not generating.
3. Six identity tests — one medium shot per wardrobe, face large and stable. **Blind-test these on people who do not know her: one woman or several?** Nelson's own recognition does not count as evidence, because he knows what the model was supposed to produce.
4. Props.
5. Environment plates.

Stills are flat-fee unlimited at 4K. Retries here are free. Spend them.
