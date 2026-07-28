# LOOK BLOCKS + THE WORLD 1 STORYBOARD PROMPT
### Franco, 2026-07-27. Captured verbatim on Nelson's instruction — *"tell pablo how to prompt the storyboard w/ all these updates on nano pro 4k"*.

---

## 1. THE THREE-BLOCK ARCHITECTURE — this changes how every prompt is built

Franco's structural ruling. Split every prompt into three independent blocks:

| Block | Owns |
|---|---|
| **Look block** | what the **entire world** feels like |
| **Shot block** | what happens in **this particular frame** |
| **Reference block** | what must remain **visually identical** |

> *"That separation will make the six worlds much easier to control."*

A look block is written once per world and reused across every shot in it. This is the thing we have
never had — until now, look and shot have been tangled in one paragraph per generation.

### The six components of a look block

Derived from the reference example Nelson brought in. **A look block is not a colour grade** — it is a
complete visual-look specification:

1. **Capture format** — e.g. *"ARRI Alexa-style LogC image"*. Imitates a high-end cinema camera before
   grading: gentle contrast, highlight detail, flexible shadows. *ELI5: expensive cinema camera, not a ph***REMOVED****
2. **Exposure** — *"natural low-light exposure", "underexposed but readable", "lifted shadows"*.
   *ELI5: dark and moody, but not black soup.*
3. **Colour grade** — the creative treatment. *ELI5: warm lamps, earthy colours, less saturation.*
4. **Lighting design** — *"motivated by real sources only"*: streetlights, windows, headlights,
   dashboards, actual fixtures. *ELI5: no invisible Hollywood spotlight following her around.*
5. **Lens and atmosphere** — softness, haze, bloom, halation, natural lens compression, soft motion blur.
   *ELI5: light glows slightly, distance layers, movement looks photographed not frozen.*
6. **Texture and imperfections** — fine film grain, imperfect real-camera texture, natural skin.
   *ELI5: "leave a little dirt under the fingernails of the image."*

Plus a **negative block** against the standard AI failure modes: fake HDR, oversharpening, plastic
skin, cyberpunk neon, crushed blacks, perfect symmetry, video-game rendering.

⚠ **Franco's caution on borrowing a look:** *"Use the Bond prompt as a **structural model, not a look
model**. Copy the way it describes the image, not the actual mood."* He also noted the reference
"does not create one universal James Bond look" — different Bond films differ wildly; it describes a
restrained European night spy thriller.

### World 3 agent-corridor look block — Franco's, verbatim

> Grounded premium live-action action-thriller frame, ARRI Alexa-style LogC capture, cold
> architectural corridor, restrained steel-blue and charcoal color grade, natural skin tones, deep but
> readable blacks, cool overhead practical lights, controlled pools of white light, subtle warm skin
> separation, soft highlight roll-off, slightly lifted shadow detail, realistic lens softness,
> restrained halation, fine film grain, subtle atmospheric haze and imperfect real-camera texture.
>
> The image should feel dark, precise and dangerous but remain completely readable. Maintain
> controlled contrast and clean action geography. Lighting comes only from corridor fixtures, doorway
> spill, muzzle flashes and environmental bounce. No glossy commercial lighting or perfect beauty
> treatment.
>
> Natural physical texture in skin, clothing, concrete, metal, smoke and reflections. Serious
> live-action weight, disciplined framing and no digital or AI gloss.

### World 1 skate look block — Franco's, in plain English

> It should feel like a premium live-action skate film frame shot in bright Southern California
> daylight. Natural sun, dry air, palm-lined neighborhood, warm realistic skin, slightly sun-bleached
> color, golden highlights, subtly cool shadows, moderate saturation, soft highlight roll-off, clean
> blacks, fine grain, realistic lens softness, and authentic in-camera texture. The image should feel
> grounded, physical, and filmed for real — not glossy commercial, not influencer-clean, not AI shiny,
> not music-video fake. Lighting comes from real daylight and environmental bounce only. The camera
> feels low, close, and physically present, like a real skate filmer, but the overall finish is
> elevated and cinematic.

⚠ **Skate is NOT the spy structure applied literally.** Skate wants brighter exposure, cleaner
daylight, more openness and freshness, less murky atmosphere.

⚠ **The specific danger Franco named:** *"don't let the skate look become too 'fashion commercial'.
If we over-polish it, it stops feeling like skate and starts feeling like Nike ad cosplay. You want
authentic skate energy plus cinematic finish. Not raw enough to look cheap. Not polished enough to
lose the street."*

---

## 2. THE WORLD 1 STORYBOARD PROMPT — Nano Pro 4K, paste-ready

Franco's master prompt, verbatim. Built on the **half-bar lattice** (1.5 / 2.5 / 1 / 3 bars) and it
carries **curly hair under the beanie**, consistent with the 07-27 hair ruling.

```
Generate one single 4K storyboard image in a 2x2 grid, four panels total, showing WORLD 1 of the
Paola Range Reel.

This is not a finished render and not a wardrobe board. It is a colored cinematic storyboard board.
It should be clean, legible, premium, and production-useful. Each panel must read like a simplified
live-action film frame, not rough sketch art, not comic-book ink, not a fashion collage. Use real
color, simple tonal blocking, clear composition, and readable human silhouette. Faces can be
simplified but Paola must still read as the same woman. Keep the same aspect ratio and visual
language across all four panels.

Overall board format:
One single image. 2x2 layout. Panels numbered 1, 2, 3, 4. Each panel is 16:9.
Add small clean captions under each panel with: shot number, time range, bar count, lens, camera
height, camera movement, brief action, last-frame handoff note.

WORLD:
World 1, SoCal street skate. Bright Southern California daylight. Palm-lined residential
neighborhood. Parked cars, dry pavement, open street, low suburban houses. Premium live-action
skate-film look. Warm sun-bleached SoCal grade with golden highlights, subtly cool shadows, moderate
saturation, soft highlight roll-off, clean blacks, slight fine grain, realistic lens softness,
authentic in-camera texture. Natural daylight only. No artificial lighting. Do not make it glossy
commercial, not over-polished, not influencer-clean, not AI shiny.

PAOLA:
Use approved Paola identity. Female, same performer throughout. Urban skate outfit only:
black beanie, black curly hair visible under beanie, white loose outer tank, black inner tank,
black fitted leggings, black skate shoes, black layer tied at waist if needed.
Use approved skateboard prop.
She travels left toward right overall, but shot 1 may move diagonally from foreground into midground
while still biasing screen-right.

Important board rule:
Each panel should show the intended strongest story moment of the shot, not random mid-action.
Panel 4 must show the exact final handoff frame for transition into World 2.
This board is the visual generation spec for later image-to-video.

SHOT PLAN:

Panel 1. Shot 1. Time 0:00 to 0:02.8125. 1.5 bars.
Shot size: low medium-full. Lens: 35mm. Camera height: 20 to 30 cm above pavement.
Angle: three-quarter rear-left.
Camera movement: stabilized tracking shot following Paola as she pushes away from camera, moving
diagonally from foreground-left toward midground-right. The camera begins behind her and drifts
slightly outward by the end so we begin to read more of her side profile.
Action: she pushes off strongly, then both feet settle on the skateboard.
Composition: low to the ground, board and pushing foot emphasized, neighborhood receding ahead.
Caption note for last frame: both feet planted, momentum established, partial side profile readable,
camera beginning to unwrap toward side position for shot 2.

Panel 2. Shot 2. Time 0:02.8125 to 0:07.5000. 2.5 bars.
Shot size: full shot moving wider. Lens: 26mm. Camera height: 45 to 60 cm above pavement.
Angle: starts rear three-quarter-left and becomes a clean left-side profile.
Camera movement: wrapped tracking move, not a full orbit. Camera eases outward from behind into a
lateral parallel track.
Action: Paola builds speed and performs two committed carves.
Composition: she remains center-left, environment opens wide around her, parked cars and palms help
sell speed.
Caption note for last frame: she exits second carve, begins straightening board, knees flexed, weight
dropping, clearly preparing for crouch.

Panel 3. Shot 3. Time 0:07.5000 to 0:09.3750. 1 bar.
Shot size: medium-full or tight full. Lens: 40mm. Camera height: 30 to 40 cm above pavement.
Angle: low three-quarter front-right.
Camera movement: short reverse tracking move holding her scale as she crouches; slight downward dip
with her body and slight upward tilt beginning at the pop.
Action: crouch and pop setup. She compresses, loads the board, tail strikes, and takeoff begins at
the end of the shot.
Composition: her full body mechanics and skateboard must be readable.
Caption note for last frame: board has just separated from pavement, upward acceleration has started,
this is the spring-loading shot before the hero payoff.

Panel 4. Shot 4. Time 0:09.3750 to 0:15.0000. 3 bars.
Shot size: low-angle full-body hero shot. Lens: 32mm. Camera height: 15 to 25 cm above pavement.
Angle: three-quarter front-left.
Camera movement: low tracking move and upward tilt following takeoff, then easing into a floating
hold during slow-motion apex.
Action: kickflip rotation and hero apex.
Composition: Paola centered high in frame, face clearly readable, knees tucked, skateboard level
beneath her, silhouette clean, enough negative space around her for the World 2 handoff.
This is the most important panel.
Caption note for last frame: exact transition anchor into World 2. Same scale, vertical position,
camera angle, horizon relationship, and airborne posture will be used for the Bollywood
wardrobe/environment swap. She has not landed yet.

Style and quality notes:
This should look like a polished cinematic storyboard, not a sketchy animatic and not a finished film
still. Use clear clean frames with enough realism to communicate the intended look and grade.
Keep Paola consistent across all four panels. Keep the skateboard consistent across all four panels.
Make the environment coherent from panel to panel.
No extra props, no text clutter, no invented scene changes. No Bollywood elements here.
No duplicate figures in one panel. No incorrect left-right travel.
No fisheye distortion unless extremely subtle. No random drone view.
No over-rendered beauty portrait look.

If using reference images:
Use the approved urban outfit board for wardrobe.
Use the approved skateboard prop board for the skateboard.
Use the approved SoCal street reference for environment.
Use the approved colored skate look frame as the color-and-grade authority.
Do not import any Bollywood wardrobe or scenery into this board.
```

### Short form — paste after refs are attached

```
Generate one single 4K colored cinematic storyboard board, 2x2 grid, for WORLD 1 only, SoCal street
skate. Four numbered 16:9 panels showing Paola in her approved urban skate outfit and approved
skateboard, in a palm-lined residential SoCal street, bright natural daylight, warm sun-bleached SoCal
filmic grade. The board is a production storyboard, not a finished render and not rough sketch art.
Each panel must show the key moment of the shot and include clean captions with shot number, time,
bars, lens, camera height, camera movement, action, and last-frame handoff note.

Panel 1: 0:00–0:02.8125, 1.5 bars, 35mm, 20–30 cm high, low 3/4 rear-left tracking push-off, Paola
moves diagonally from foreground-left toward midground-right, camera drifts slightly outward, both
feet settle on board.
Panel 2: 0:02.8125–0:07.5000, 2.5 bars, 26mm, 45–60 cm high, wrapped tracking move from rear 3/4 into
lateral profile, two strong carves, wider environmental speed.
Panel 3: 0:07.5000–0:09.3750, 1 bar, 40mm, 30–40 cm high, low 3/4 front-right reverse track, crouch
and pop, tail strikes, board begins takeoff.
Panel 4: 0:09.3750–0:15.0000, 3 bars, 32mm, 15–25 cm high, low hero shot with upward tilt into
slow-motion apex, kickflip midair, Paola centered high in frame, face readable, board level beneath
feet. This final panel is the exact World 2 transition anchor.
```

---

## 3. FEEDING THE BOARD TO SD2 — Franco's honest assessment

Nelson asked whether SD2 can be told to follow the 2×2 board top-left → right with timestamps.

> *"Yes — you can do that, and it can help. But think of it as **'guidance,' not 'hard obedience.'**"*

**What SD2 is likely to understand:** the board as a sequence roadmap · reading order top-left,
top-right, bottom-left, bottom-right · timestamps tied to panels · broad progression of pose, camera
and scene.

**What it will NOT do reliably:** follow panel order with frame-accurate discipline · respect exact
cut times just because they are written on the board · preserve all four panels evenly *(it may
over-favour one or blend them)* · truly **cut** between shots if the visual jumps are too different.

**The wording to use:**
```
Follow the storyboard in reading order: panel 1 top-left, panel 2 top-right, panel 3 bottom-left,
panel 4 bottom-right.
Use these time ranges: 0.0–2.8s panel 1 · 2.8–7.5s panel 2 · 7.5–9.4s panel 3 · 9.4–15.0s panel 4
Camera starts low behind her during push-off, unwraps to lateral carve, moves to low front
crouch/pop, then ends in slow-motion kickflip apex.
```
⚠ **That last line matters more than the timestamps al***REMOVED***** Telling it what the progression *means*
beats telling it when to cut.

**Use a whole-world board only when:** the sequence is one connected physical action · the same
environment persists · the same wardrobe persists · the shot evolution is smooth, not wildly
discontinuous.

| World | Suitability |
|---|---|
| **1 skate** | **best candidate** — push-off → carve → crouch → kickflip is one continuous movement chain |
| 2 bolly | could work |
| 3 agent, 4 car | **riskier** — action geography and continuity get complex |

**Best practice — three layers together, never the board alone:**
**start frame + 2×2 storyboard + motion description with time ranges**, and for the highest chance,
**start frame + storyboard + audio + strong prompt**.

> *"Treat it like: 'I am giving SD2 a visual roadmap and hoping it interpolates the route correctly.'"*

**Franco has offered** to write the exact SD2 prompt structure for this method — reference hierarchy,
storyboard wording and timestamp wording. Worth taking him up on before the first paid generation.
