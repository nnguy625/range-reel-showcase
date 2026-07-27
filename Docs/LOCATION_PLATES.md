# RANGE REEL — LOCATION PLATES

*The plate set that stops environment drift. Written 2026-07-26.*

**Gate for every generation below: GPT Image 2 · 16:9 · High · 4K · Unlimited toggle ON and the
Generate button showing NO credit number.** Save into the **Locations** folder of the Paola Cinematic
project.

---

## WHY FOUR PLATES, AND WHY THESE FOUR

Two findings drove this, both from research on how these specific models actually behave:

**In image-to-video, the first frame IS the environment.** SD2 takes the room from the uploaded
frame, not the prompt — the prompt should describe what *changes over time*, not what exists. So a
plate is not concept art. It is the literal source of truth for every shot built on it.

**Drift scales with clip length.** Five-second clips hold tight; thirty-second clips fall apart. Our
shots are **3.75s**, comfortably inside the stable window. Length is not our risk — *inconsistency
between separately-generated start frames* is.

**Two to four non-redundant references beat six overlapping ones.** Overlap gives the model no new
information. So four plates, each answering a question the others cannot.

| Plate | Camera | What it locks |
|---|---|---|
| `01_MAP` | top-down bird's-eye | geography — where things are relative to each other, before any render exists |
| `02_WIDE` | eye level ~1.6 m, 24 mm | the hero image. Materials, palette, light direction, time of day |
| `03_WORK` | the world's action height, 35 mm | the angle most shots are actually taken from |
| `04_REVERSE` | 180° from WIDE, same height | proves the space continues behind camera |

**The reverse plate is the one people skip and the one that matters.** Without it the model has only
ever "seen" the location from one direction, so any shot facing the other way invents a new room.

**Naming:** `LOC_<Name>_<NN>_<ROLE>` — e.g. `LOC_SoCalStreet_02_WIDE`. Then one Higgsfield element
per location named `Loc-<Name>`, built from `02_WIDE` + `04_REVERSE` (the two that carry the most
non-redundant information). Later shots attach that element and inherit the room.

**The MAP is not a render source.** It never gets attached to a shot as a look reference — it exists
so the human and the shot-builder agree on geography. Attaching it to a photoreal shot would poison
the style.

---

## ⚠ THE ORDER OF OPERATIONS — THIS IS THE WHOLE METHOD

**Corrected 2026-07-26 after the first SoCal set came back as four different streets.**

Generating all four plates from text alone DOES NOT WORK. "The same street, same bungalows, same
palms" is a description, and a description makes the model invent a *new* street that matches the
description. Four generations = four neighbourhoods. The plates then actively teach the model four
different rooms, which is worse than having no plates.

**The correct sequence:**

1. **Generate `02_WIDE` first, al***REMOVED***** This is the hero. Approve it before anything else exists.
2. **Save it as an element** — `Loc-<Name>`.
3. **Generate `03_WORK` and `04_REVERSE` with that element ATTACHED**, using the world-reference
   opener below. They are variations *on an image*, never fresh descriptions.
4. `01_MAP` is schematic and can be generated from text, but its geography must match the wide.

**This is already proven in this project.** The Japan garden set (July 17) holds across three angles
because the reverse plate attached the wide and opened with exactly this. The SoCal set failed
because it didn't.

### The world-reference opener — use verbatim

```
@Loc-<Name> — WORLD REFERENCE: carry the geography, materials, light logic and palette
identically from this plate. Same location, new angle. Never reinvent the world. The
reference IS the geometry — do not re-enumerate or redesign it.
```

### The ANCHOR line — mandatory, one per plate

Name **one specific object** from the wide that must reappear in the new angle, and say where it now
sits. This is what proves it is the same place rather than a similar ***REMOVED***

> Japan garden, the version that worked: *"the weathered stone lantern — now DEEP in the frame, off
> to one side, out on the gravel, its single candle flame the one warm point far out · the continuity
> anchor that proves it's the same place."*

Pick the anchor from the approved wide once it exists — a specific parked vehicle, a corner house, a
utility pole, a market stall, a pillar. It must be findable from more than one direction.

**Describe only what CHANGES** — the camera position and what it now sees. Everything else comes from
the attached plate.

---

## SHARED CRAFT BLOCK

Every plate below is generated with no people in frame unless stated, so the environment stays a
clean backdrop. Deep focus and matte materials throughout — shallow depth of field and over-sharpened
surfaces smear under SD2 motion.

```
Empty location, no people, no figures, no crowds. Deep focus, everything sharp from
foreground to horizon. Real matte materials with real texture. Photographed on a real
camera, fine natural film grain.

Never generate: people, figures, silhouettes or body parts. Text, signage lettering,
logos, brand names or licence plates. CGI, 3D render, video-game look, digital
smoothness, HDR overprocessing, plastic surfaces. Shallow depth of field or heavy bokeh.
```

---

## WORLD 1 — SOCAL RESIDENTIAL STREET

Palette: bleached asphalt, dry palms, stucco, chain-link, hard noon sun. Light: high sun, short hard
shadows, warm.

**`LOC_SoCalStreet_01_MAP`**
```
Top-down bird's-eye orthographic map of a Southern California residential street, drawn
as a clean flat diagram. A straight two-lane residential road runs left to right through
the frame with parked cars along both kerbs, single-storey stucco bungalows with flat
driveways on both sides, palm trees at regular intervals on the verge, and a cross street
entering from the bottom. Clean schematic top-down view, uniform lighting, no perspective,
no people, no text or labels.
```

**`LOC_SoCalStreet_02_WIDE`** — the hero
```
Wide establishing photograph of an empty Southern California residential street at midday,
camera at eye level about 1.6 metres, 24mm lens, standing in the middle of the road looking
straight down it. Cracked pale asphalt with faded lane paint running away to a vanishing
point. Single-storey stucco bungalows in warm cream and dusty pink on both sides, low
chain-link and hedge front yards, parked cars along both kerbs. Tall thin palm trees
spaced along the verge against a pale hot sky. Hard high sunlight, short dark shadows,
bleached highlights, dry warm palette.
[+ shared craft block]
```

**`LOC_SoCalStreet_03_WORK`** — low skate-level
```
The same Southern California residential street, same houses, same parked cars, same palms,
same midday light. Camera very low, about 30 centimetres off the road surface, 35mm lens,
tilted slightly up and looking down the length of the street. The cracked asphalt texture
fills the foreground and runs away sharply to the vanishing point, kerb and parked cars at
the frame edges. Same location, new angle. Do not reinvent the street.
[+ shared craft block]
```

**`LOC_SoCalStreet_04_REVERSE`**
```
The same Southern California residential street, same houses, same parked cars, same palms,
same midday light, photographed from the opposite direction. Camera at eye level about 1.6
metres, 24mm lens, standing in the road looking back the way it came, so the cross street
is now behind the camera and the road runs away to the opposite horizon. Same location,
reverse angle. Do not reinvent the street.
[+ shared craft block]
```

---

## WORLD 2 — INDIAN MARKET STREET

Palette: dusty teal awnings and crowd wear, saffron and marigold accents, warm dust haze. Light:
low golden hour, long shadows.

**`LOC_MarketStreet_01_MAP`**
```
Top-down bird's-eye orthographic map of a narrow market street, drawn as a clean flat
diagram. A straight pedestrian street runs top to bottom through the frame, lined both
sides with market stalls under square awnings, with a wider open square at the top end and
hanging fabric lines crossing overhead at two points. Clean schematic top-down view,
uniform lighting, no perspective, no people, no text or labels.
```

**`LOC_MarketStreet_02_WIDE`** — the hero
```
Wide establishing photograph of a narrow Indian market street at golden hour, camera at eye
level about 1.6 metres, 24mm lens, looking straight down the street. Market stalls line both
sides under square canvas awnings in dusty teal, stacked produce and brass goods, worn
stone paving underfoot. Lines of hanging fabric cross overhead between the buildings,
catching the low sun. Warm dust haze in the air, long low golden light raking down the
street, deep warm shadows. Saffron and marigold colour accents against the dusty teal.
[+ shared craft block]
```

**`LOC_MarketStreet_03_WORK`** — the fabric curtain
```
The same Indian market street, same stalls, same dusty teal awnings, same golden hour light.
Camera at eye level about 1.6 metres, 35mm lens, close to a curtain of hanging market fabric
that crosses the street, so the hanging cloth fills most of the frame with the lit street
visible through and past it. The fabric is lit from behind by the low sun. Same location,
new angle. Do not reinvent the street.
[+ shared craft block]
```

**`LOC_MarketStreet_04_REVERSE`**
```
The same Indian market street, same stalls, same dusty teal awnings, same golden hour light,
photographed from the opposite direction. Camera at eye level about 1.6 metres, 24mm lens,
looking back up the street toward the open square at the far end, low sun now behind the
camera. Same location, reverse angle. Do not reinvent the street.
[+ shared craft block]
```

---

## WORLD 3 — COLD INTERIOR CORRIDOR

Palette: desaturated steel, concrete, cold cyan practicals, wet floor. Light: hard cold sources,
deep shadow, high contrast.

Desaturation is doing hidden work here — every AI tell is more visible in saturated footage, and a
cold grade suppresses them. Wet floor buys reflections, which read as production value for free.

**`LOC_Corridor_01_MAP`**
```
Top-down bird's-eye orthographic map of a long industrial interior corridor, drawn as a
clean flat diagram. A straight corridor runs left to right through the frame with regularly
spaced structural pillars along both walls, two doorways on the lower wall, a stack of
crates forming cover a third of the way along, and a T-junction at the right end. Clean
schematic top-down view, uniform lighting, no perspective, no people, no text or labels.
```

**`LOC_Corridor_02_WIDE`** — the hero
```
Wide establishing photograph of a long empty industrial corridor at night, camera at eye
level about 1.6 metres, 24mm lens, looking straight down the corridor. Bare concrete walls
with exposed steel structure, regularly spaced pillars, a wet reflective concrete floor.
Cold cyan practical lights at intervals along the ceiling, pools of light with deep black
shadow between them, a T-junction visible at the far end. Heavily desaturated cold palette,
high contrast, lifted open blacks that still hold detail. Damp still air.
[+ shared craft block]
```

**`LOC_Corridor_03_WORK`** — behind cover
```
The same industrial corridor, same concrete, same pillars, same cold cyan practicals, same
wet floor. Camera low, about 1 metre, 35mm lens, tucked in close beside a stack of heavy
crates that form solid cover in the foreground, looking along the corridor past the cover.
The crate edge occupies one side of the frame. Same location, new angle. Do not reinvent
the corridor.
[+ shared craft block]
```

**`LOC_Corridor_04_REVERSE`**
```
The same industrial corridor, same concrete, same pillars, same cold cyan practicals, same
wet floor, photographed from the opposite direction. Camera at eye level about 1.6 metres,
24mm lens, standing at the T-junction looking back down the corridor the way it came. Same
location, reverse angle. Do not reinvent the corridor.
[+ shared craft block]
```

---

## WORLD 4 — SUNLIT DESERT HIGHWAY

Palette: bleached tarmac, pale sand, bare distant mountains, white-hot sky. Light: hard high sun,
blown highlights, heat shimmer.

Cars already exist as elements: `Pao-Car-Ext` and `car-chaser-ext`. Interiors are specced separately
— one panel per perspective, and sides named physically (left-hand drive), never by seat role.

**`LOC_DesertRoad_01_MAP`**
```
Top-down bird's-eye orthographic map of an empty desert highway, drawn as a clean flat
diagram. A straight two-lane highway runs bottom to top through the frame with a long
sweeping curve near the top, flat open scrub desert on both sides, a dry wash crossing
under the road at one point, and scattered low rock outcrops. Clean schematic top-down
view, uniform lighting, no perspective, no vehicles, no people, no text or labels.
```

**`LOC_DesertRoad_02_WIDE`** — the hero
```
Wide establishing photograph of an empty two-lane desert highway at midday, camera at eye
level about 1.6 metres, 24mm lens, standing on the centre line looking straight down the
road. Bleached grey tarmac with faded centre line running to a distant vanishing point,
flat pale scrub desert on both sides, bare low brown mountains along the horizon, white-hot
pale sky. Hard vertical sunlight, heat shimmer rising off the far tarmac, blown highlights,
dry bleached palette. No vehicles.
[+ shared craft block]
```

**`LOC_DesertRoad_03_WORK`** — low chase height
```
The same empty desert highway, same tarmac, same mountains, same midday light. Camera very
low, about 40 centimetres off the road surface, 35mm lens, looking down the road. The tarmac
texture and faded centre line fill the foreground and run away sharply, heat shimmer over
the distance. Same location, new angle, no vehicles. Do not reinvent the road.
[+ shared craft block]
```

**`LOC_DesertRoad_04_REVERSE`**
```
The same empty desert highway, same tarmac, same mountains, same midday light, photographed
from the opposite direction. Camera at eye level about 1.6 metres, 24mm lens, standing on
the centre line looking back the way it came, the long sweeping curve now visible ahead.
Same location, reverse angle, no vehicles. Do not reinvent the road.
[+ shared craft block]
```

---

## WORLD 6 — RUNWAY AND AISLE

Palette: warm gold-white, polished floor, dark surrounds. Light: bright overhead runway wash against
a dark house.

The reel's closing shot turns this into the SoCal sidewalk behind a full-frame occluder, so the
runway's floor tone and light direction should sit close enough to World 1's street that the cut can
hide inside a moving gown.

**`LOC_Runway_01_MAP`**
```
Top-down bird's-eye orthographic map of a fashion show runway, drawn as a clean flat
diagram. A long straight runway strip runs bottom to top through the frame with rows of
seating along both sides, a wide backstage entrance arch at the top end, and a broad open
turning circle at the bottom end. Clean schematic top-down view, uniform lighting, no
perspective, no people, no text or labels.
```

**`LOC_Runway_02_WIDE`** — the hero
```
Wide establishing photograph of an empty fashion show runway, camera at eye level about 1.6
metres, 24mm lens, standing on the runway looking toward the backstage entrance arch. A long
polished pale floor strip running away to the arch, rows of empty seating in deep shadow on
both sides, a dark ceiling above. Bright warm overhead light washing straight down the
runway strip, the surrounding house falling into near black. Warm gold-white highlights
against deep shadow, high contrast, glossy floor reflections.
[+ shared craft block]
```

**`LOC_Runway_03_WORK`** — tracking height
```
The same fashion runway, same polished floor, same seating rows in shadow, same warm
overhead wash. Camera lower, about 1.2 metres, 35mm lens, on the runway looking back along
its length toward the open turning circle at the far end, so the strip runs away from
camera. Same location, new angle. Do not reinvent the runway.
[+ shared craft block]
```

**`LOC_Runway_04_REVERSE`**
```
The same fashion runway, same polished floor, same seating rows in shadow, same warm
overhead wash, photographed from the opposite direction. Camera at eye level about 1.6
metres, 24mm lens, standing at the backstage arch looking out down the full length of the
runway. Same location, reverse angle. Do not reinvent the runway.
[+ shared craft block]
```

---

## WORLD 5 — JAPAN GARDEN, ALREADY BUILT

Not in scope. Plates exist in `Documents/Paola JPG/`: `ref_garden_nite_wide.png`,
`ref_garden_nite_loweye.png`, `ref_garden_nite_3-4_house.png`, plus
`APPROVED_PLATES/GARDEN_NIGHT_BIRDSEYE_MASTER.png` — which is already exactly this MAP + WIDE +
WORK + REVERSE structure, built before the structure was named.

---

## ⚠ THE MAP RULING — SUPERSEDES THE SCHEMATIC MAP PROMPTS ABOVE (Nelson, 2026-07-26)

**MAP plates are PHOTOREAL OVERHEAD DRONE SHOTS, never illustrations, diagrams or schematics.**
Nelson's call: the drone version locks the same geography, matches the other three plates'
materials, and could double as a real establishing shot. A schematic can do none of those.

Every `01_MAP` block above still says "clean flat diagram / clean schematic top-down view". **That
wording is dead.** Generate MAPs as: photoreal drone or roof-rig photograph, lens pointing STRAIGHT
DOWN, a true 90-degree top-down nadir, with the world-reference element attached for materials.
Exteriors fly at ~40–60 m. Interiors use "the roof has been lifted clean off the building and the
camera hangs high above it" — that phrasing is what actually produced a true nadir.

Two model notes, both observed 2026-07-26:
- **GPT Image 2 obeys the nadir instruction. Nano Banana Pro does not** — asked for a runway MAP it
  returned a handsome ~45° raked high angle instead. Route MAPs to GPT Image 2.
- Both banks of `NEVER a diagram / blueprint / floor plan / orthographic / flat vector / minimap`
  and `no text, labels, arrows, scale bars` are load-bearing. Keep them.

---

## STATUS — ALL FIVE LOCATIONS COMPLETE 4/4 (2026-07-26)

| Location | Element | MAP | WIDE | WORK | REVERSE |
|---|---|---|---|---|---|
| SoCal street | `Loc-SoCal-Street` (+ `Loc-SoCal-Street-Aerial`) | ✓ | ✓ | ✓ | ✓ |
| Market street | `Loc-Market-Street` | ✓ | ✓ | ✓ | ✓ |
| Corridor | `Loc-Corridor` | ✓ | ✓ | ✓ | ✓ |
| Desert road | `Loc-Desert-Road` | ✓ | ✓ | ✓ | ✓ |
| Runway | `Loc-Runway` | ✓ | ✓ | ✓ | ✓ |

All 23 plates sit in the **Locations** folder of the Paola Cinematic project. `Loc-Runway` was
built from the Nano Banana Pro wide (brighter, polished floor, arch reading clearly, geography
legible) over the GPT Image 2 wide (prettier and moodier but near-black, less to hold onto). The
GPT Image 2 wide is still in the folder as an alternate mood plate, as is a Nano Banana Pro
high-angle runway geography plate.

**One deviation from the spec above, deliberate:** the doc's `LOC_Runway_03_WORK` and
`LOC_Runway_04_REVERSE` both look toward the turning circle, which would have produced two
near-identical plates. WORK was re-aimed to face the arch from 1.2 m, 35 mm, off the centre line at
the runway's right edge — a genuinely different framing. REVERSE stayed the true 180 from the arch.

---

## OPEN

- [ ] Franco's QA on this plate set. Three attempts failed — he burns the full ~5 minute budget on
      web search and returns citations with no answer body, on both the old thread and a fresh ***REMOVED***
      Not a thread problem, a mode problem. Retry on a lower reasoning setting.
- [ ] Check the runway floor tone against World 1's street before locking, since the closing cut
      hides between them.
