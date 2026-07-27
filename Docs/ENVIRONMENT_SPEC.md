# RANGE REEL — ENVIRONMENT SPEC

*Locations, how they're referenced, and the contamination rules. Franco doctrine adopted 2026-07-26.*

---

## THE FINDING — why the combined board was discarded

A single six-world environment board was generated and **rejected as a production deliverable.** It
put six locations, rendered text, labelled panels, crowd performers and graffiti inside one image.
Every one of those is a contamination vector when the board is attached as a reference:

| What was in it | What it leaks into the generation |
|---|---|
| Six locations in one frame | the model blends worlds, or picks the wrong one |
| Panel labels, headers, swatch grids | rendered text and diagram furniture inside the shot |
| Crowd performers | uninvited people in an empty-location plate |
| Graffiti, signage | invented text on walls |

It survives only as a **mood/selection artifact**. It is never attached to a generation.

This is the same law already proven on characters — *"the current Bollywood references keep
contaminating the board"* (`FRANCO_DECISIONS.md:124`) — now generalized to locations. It is also the
same principle as the accessory-ownership rule in `ASSET_SPEC.md`: **one owner per variable, and no
reference carries a variable it doesn't own.**

---

## THE STANDARD — two assets per world, each with one job

| Asset | Owns | Never used for |
|---|---|---|
| **`@Env_Photo`** | location, architecture, materials, palette, atmosphere, lighting | geography, camera side, blocking |
| **`@Env_Map`** | geography, camera side, depth, blocking relationships | look, materials, light, palette |

The map is our bird's-eye master under a different name — the existing pipeline law (*bird's-eye
master per location BEFORE plates, red box = frame, circles = characters*) and Franco's geometry map
are the same instrument. They converged independently, which is a good sign for both.

**Image-only.** The photo sheet carries no text, no labels, no borders, no panel numbering, no
performers, no props. Thin neutral-grey gutters only.

---

## THE RULES

**1. One world at a time.** Never attach more than the current world's sheet. Uploading all six
recreates the contaminated board by other means.

**2. The map is conditional, not default.** Attach `@Env_Map` only when a reverse angle, a lateral
angle, or a repeated blocking relationship has to hold. Otherwise the photo sheet al***REMOVED***

**3. Never copy the sheet's layout into the shot.** Every prompt using a sheet states it explicitly:
*do not copy the sheet layout, borders, panels, gutters or diagram style into the image.*

**4. Plate first, then motion.** Environment refs do not go straight to video:

```
@Env_Photo (+ @Env_Map if needed)
  → ONE clean 16:9 environment plate, Nano Banana Pro
     stating exact camera position, lens, height, direction, framing
  → approve the plate
  → that single plate is the start-frame authority in SD2,
     alongside Paola, the world's props, and E1
```

The approved plate — not the sheet — is what SD2 ever sees. Sheets are upstream of plates; plates are
upstream of motion. Higgsfield's own guidance points the same way: start with one or two references
and use image-to-video where predictability matters.

**5. Empty locations.** Environment plates contain no performers and no props. People and objects
arrive at the shot stage, not the location stage.

---

## PER-WORLD STATUS

| # | World | Look locked | `@Env_Photo` | `@Env_Map` |
|---|---|---|---|---|
| 1 | Urban skate | **Huntington Beach, CA** — real coastal city, late-afternoon sun | ❌ **REJECTED** | missing |
| 2 | Bollywood street | warm, saturated, dusty sun, market fabric | ✅ clean | missing |
| 3 | Agent / night corridor | industrial, cold, desaturated, wet floor, fluorescent | ✅ clean | missing |
| 4 | Car chase / day desert | hot, exposed, dust, glare, asphalt, arid canyon | ✅ clean | missing |
| 5 | Japanese garden / night | moonlit, shoji glow, stone, water | ✅ **EXEMPT — locked** | ✅ bird's-eye |
| 6 | Couture runway | indoor, black gloss, gold spill, spotlight cones | ✅ clean | missing |

### Audit 2026-07-26 — sheet 01 rejected

Four sheets meet the standard: one hero panel, three supporting panels, a palette strip, thin
neutral-grey gutters, **zero text**. Sheet 01 is a different lineage — it is the original six-world
infographic template rebuilt for one world, and it carries every contamination vector the combined
board was rejected for:

| Present in sheet 01 | Consequence if attached |
|---|---|
| Title, section headers, numbered labels | rendered text and headers inside the plate |
| Hex codes, bullet notes, camera diagrams | diagram furniture inside the plate |
| `BLOCKING & SCALE GUIDE` panel | the map baked into the photo asset, violating role separation |
| `HUNTINGTON BEACH` rendered on a wall in-panel | invented signage propagating into shots |
| Graffiti lettering in the detail panels | invented text on surfaces |

**Sheet 01 does not get attached to anything.** It is regenerated to match sheets 02/03/04/06.

**Judgment calls logged, both accepted:** the runway sheet contains a seated audience and the
Bollywood sheet contains distant pedestrians. Both are deep-background, low-contrast and out of
focus — they read as architecture and ambient population rather than performers, and a runway with
no audience reads wrong. The no-performers rule targets foreground figures that compete for identity
or drift; these do neither.

### New canon from this batch

**World 1 is Huntington Beach, California** — a real, specific, modern coastal city: pier, boardwalk,
concrete skate bowl, palms, chain-link, low storefronts. This was not previously specified and is now
locked. Real named location beats a generic "SoCal plaza" for consistency. The *place* is canon; the
rendered `HUNTINGTON BEACH` signage in the rejected sheet is not — no lettering carries into plates.

### World 5 is exempt, and it was verified rather than assumed

Rebuilding the garden would replace approved geometry with new geometry — a straight T13 violation
(*approved images outrank derived work*). All four assets confirmed present on disk 2026-07-26:

- `ref_garden_nite_wide.png`
- `ref_garden_nite_loweye.png`
- `ref_garden_nite_3-4_house.png`
- `APPROVED_PLATES/GARDEN_NIGHT_BIRDSEYE_MASTER.png`

The bird's-eye master already serves as World 5's `@Env_Map`. Nothing to build.

---

## THE CAVEAT ON MACRO-TO-MICRO

SD2 can read a sheet and separate scene, character and prop references, taking composition and
shot-scale information from them. It does **not** reconstruct a dependable 3D set, and **unseen
reverse geometry stays unconstrained** — which is the entire reason the map is a separate asset
instead of an assumed property of the photo sheet.

Treat "the model understands the space" as false until a reverse angle proves it on that specific
location.

---

## OPEN

- [ ] **The five sheet files are not in this repo yet.** They exist in the Franco thread as links;
      they need to land in `Assets/Locations/` before anything can reference them. One folder per
      world, `NN_ROLE_name.png` per the REFPACK standard.
- [ ] Once they land: register each as a Higgsfield element, `@Env_Photo_<World>` / `@Env_Map_<World>`.
- [ ] World 5 needs no work — point at the existing plates.
