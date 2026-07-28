# PROMPTS & BEATS — the single master file
### Every shot, every timecode, every look block, every prompt. Built 2026-07-28. **This is the file to open in execution mode.**

We are in **planning with outputs**: collect and approve every component, QA each one, then combine and
run SD2 generation in one paid push. Nothing here generates on its own.

**Companion files:** `DIRECTING_SYSTEM.md` (why the shots are what they are) · `BEAT_MAP.md` (the
lattice ruling) · `LOOK_BLOCKS_AND_W1_BOARD.md` (the three-block architecture, verbatim Franco) ·
`ASSET_MANIFEST.md` (the 43 pulled assets) · `OVERLAY_PROMPTS_W2-W6.md` (music, already locked).

---

## 0 · The spine — fixed, do not re-derive

| | |
|---|---|
| Tempo / meter | **128 BPM · 4/4** |
| One bar | **1.875 s** |
| One world | **8 bars = 15.000 s exactly** |
| Full reel | **6 worlds = 48 bars = 90.000 s exactly** |
| Audio spine | **E1** — continuous rhythmic spine, runs unbroken under all six worlds |
| Shot count | **24** — four per world |

**Every world transition lands on beat 1.** Only the internal sentence rhythm changes between worlds.

### The half-bar lattice — Franco, ratified 07-27

The uniform 2-bar shot plan is **obsolete**. Bar splits per world, all summing to 8:

| World | Splits | Note |
|---|---|---|
| 1 skate | 1.5 / 2.5 / 1 / 3 | |
| 2 bolly | 1.5 / 2 / 3 / 1.5 | spectacle gets the 3 |
| 3 agent | 1.5 / 3 / 1.5 / 2 | held close-up = 5.625 s |
| 4 car | 2 / 1.5 / 3 / 1.5 | the drift = 5.625 s |
| 5 sword | 2.5 / 1 / 3 / 1.5 | first strike is sharp punctuation |
| 6 runway | 2.5 / 2 / 2 / 1.5 | entrance breathes, return concise |

🔲 **Nelson's ratification stamp still outstanding.** Franco has specified it three times and every
downstream document is written against it.

Short shots generate as **4-second clips** (SD2's floor) with the endpoint staged early, then get
trimmed on the half-bar cut.

---

## 1 · Master timing table — all 24 shots

| World | Shot | Bars | In | Out | Length |
|---|---|---|---|---|---|
| **1 skate** | 1 | 1.5 | 0.0000 | 2.8125 | 2.8125 |
| | 2 | 2.5 | 2.8125 | 7.5000 | 4.6875 |
| | 3 | 1 | 7.5000 | 9.3750 | 1.8750 |
| | 4 | 3 | 9.3750 | 15.0000 | 5.6250 |
| **2 bolly** | 1 | 1.5 | 15.0000 | 17.8125 | 2.8125 |
| | 2 | 2 | 17.8125 | 21.5625 | 3.7500 |
| | 3 | 3 | 21.5625 | 27.1875 | 5.6250 |
| | 4 | 1.5 | 27.1875 | 30.0000 | 2.8125 |
| **3 agent** | 1 | 1.5 | 30.0000 | 32.8125 | 2.8125 |
| | 2 | 3 | 32.8125 | 38.4375 | 5.6250 |
| | 3 | 1.5 | 38.4375 | 41.2500 | 2.8125 |
| | 4 | 2 | 41.2500 | 45.0000 | 3.7500 |
| **4 car** | 1 | 2 | 45.0000 | 48.7500 | 3.7500 |
| | 2 | 1.5 | 48.7500 | 51.5625 | 2.8125 |
| | 3 | 3 | 51.5625 | 57.1875 | 5.6250 |
| | 4 | 1.5 | 57.1875 | 60.0000 | 2.8125 |
| **5 sword** | 1 | 2.5 | 60.0000 | 64.6875 | 4.6875 |
| | 2 | 1 | 64.6875 | 66.5625 | 1.8750 |
| | 3 | 3 | 66.5625 | 72.1875 | 5.6250 |
| | 4 | 1.5 | 72.1875 | 75.0000 | 2.8125 |
| **6 runway** | 1 | 2.5 | 75.0000 | 79.6875 | 4.6875 |
| | 2 | 2 | 79.6875 | 83.4375 | 3.7500 |
| | 3 | 2 | 83.4375 | 87.1875 | 3.7500 |
| | 4 | 1.5 | 87.1875 | 90.0000 | 2.8125 |

---

## 2 · How every prompt is built — the three-block architecture

Franco's structural ruling. **Never write look and shot in one tangled paragraph again.**

| Block | Owns | Reuse |
|---|---|---|
| **Look block** | what the entire world feels like | written **once per world**, pasted into every shot |
| **Shot block** | what happens in this particular frame | per shot |
| **Reference block** | what must remain visually identical | per shot |

A look block has six components — **capture format · exposure · colour grade · lighting design · lens
and atmosphere · texture and imperfections** — plus a negative block against fake HDR, oversharpening,
plastic skin, cyberpunk neon, crushed blacks, perfect symmetry and video-game rendering.

⚠ **Borrow structure, never mood.** *"Copy the way it describes the image, not the actual mood."*

---

## 3 · The directing logic behind every shot

Franco's reverse-engineering of Nelson's instinct, in one line:

```
inherit motion  →  translate into genre language  →  expand into spectacle  →  end on a transformation frame
```

**A world never simply ends.** Shot 4 is always a transformation anchor. Camera position is an arc:
behind = we join her · beside = we feel her speed · in front = we anticipate · below = she is iconic.
Full write-up in `DIRECTING_SYSTEM.md`.

---

# WORLD 1 · SO CAL STREET SKATE — 0.0000–15.0000
### ✅ BOARD COMPLETE — `Assets/Plates/STORYBOARD/W1 SKATE.png`

**Grade name (footer):** WARM SUN-BLEACHED SO CAL · **Camera style:** LIVE-ACTION SKATE FILM

### Look block — Franco, verbatim
> It should feel like a premium live-action skate film frame shot in bright Southern California
> daylight. Natural sun, dry air, palm-lined neighborhood, warm realistic skin, slightly sun-bleached
> color, golden highlights, subtly cool shadows, moderate saturation, soft highlight roll-off, clean
> blacks, fine grain, realistic lens softness, and authentic in-camera texture. The image should feel
> grounded, physical, and filmed for real — not glossy commercial, not influencer-clean, not AI shiny,
> not music-video fake. Lighting comes from real daylight and environmental bounce only. The camera
> feels low, close, and physically present, like a real skate filmer, but the overall finish is
> elevated and cinematic.

⚠ **The named failure mode:** *"don't let the skate look become too 'fashion commercial'… Not raw
enough to look cheap. Not polished enough to lose the street."*

### Shots — as built on the approved board

| Shot | Bars / Time | Lens | Height | Move | Action | Last frame |
|---|---|---|---|---|---|---|
| **1** | 1.5 · 0–2.8125 | 35mm | 20–30 cm | Low tracking | Push off strong, then both feet settle on board. Moving diagonally from foreground-left toward midground-right. | Both feet planted, momentum established, partial side profile readable, camera beginning to unwrap toward side position for shot 2. |
| **2** | 2.5 · 2.8125–7.5 | 26mm | 45–60 cm | Wrapped tracking | Builds speed and performs two committed carves. Environment opens wide around her. | Exits second carve, begins straightening board, knees flexed, weight dropping, preparing for crouch. |
| **3** | 1 · 7.5–9.375 | 40mm | 30–40 cm | Reverse tracking | Crouch and pop setup. Compress, load the board, tail strikes, takeoff begins. | Board has just separated from pavement, upward acceleration has started. |
| **4** | 3 · 9.375–15.0 | 32mm | 15–25 cm | Low tracking + upward tilt into slow-mo hold | Kickflip rotation and hero apex. Paola centered high in frame, face readable, board level beneath her. | **Exact transition anchor into World 2.** Same scale, angle and airborne posture. **She has not landed yet.** |

**Wardrobe:** white tank over black inner, black leggings, black beanie, **curls** · **Prop:** skateboard

---

# WORLD 2 · BOLLYWOOD STREET — 15.0000–30.0000
### ✅ LOOK BLOCK LOCKED · ✅ BOARD REBUILT ON IT, 2026-07-28

> 📥 **Board is rendered in Franco's thread and needs saving** as
> `Assets/Plates/STORYBOARD/W2 BOLLYWOOD.png`. **Nelson saves it** — do not click ChatGPT's download
> button, it opens a native dialog that blocks the renderer.
>
> **QA on the rebuilt board — passes.** Red reads as hero, crowd sits in dusty teal, street stays warm
> stone, gold held to the border. Spec strips correct: Shot 1 = 35 mm / 90 cm, Shot 2 = 50 mm / 120 cm,
> Shot 3 = 28 mm / 140 cm, Shot 4 = 40 mm / 110 cm. Timecodes match the lattice.
>
> ⚠ **One note carried forward to the start frame, not a board defect.** Panel 1 reads as *already
> mid-dance* rather than absorbing a landing. The spec strip describes the match-cut receive correctly,
> so the wording is right — but the actual W2 **start frame** must make the incoming body geometry
> unmistakably a **landing** before it becomes the hop. The bridge only works if the audience feels the
> impact.

## 🎨 GRADE NAME: **LUMINOUS DUSTY-TEAL BOLLYWOOD**

> **This look block is the master prompt.** It feeds the board, the start frame, the end frame, every
> intermediate plate and the SD2 prompt. Franco built it after inspecting the actual identity master,
> face CU, wardrobe sheet and market plate.

### Compressed one-line world look — paste this into every W2 generation
> Premium live-action contemporary Bollywood street-dance frame, bright sunlit market street, luminous
> open exposure, pomegranate-red hero sari against a dusty-teal crowd, restrained antique-gold accents,
> warm natural skin tones, daylight-only motivated lighting, soft highlight roll-off, subtle halation,
> slight atmospheric dust, graceful stabilized camera, real textile texture, and no wedding gloss,
> festival overload, neon music-video color, or AI polish.

### The six components — Franco, verbatim

**1 · Capture character.** A premium contemporary Bollywood street-dance film frame — **not a mythic
period piece and not a glossy bridal ad.** Large-format live-action cinema capture, graceful stabilized
movement, choreography-friendly coverage, clean human readability. Elegant and musical, polished enough
to feel expensive, but still grounded in a real street with real dancers.

**2 · Exposure.** Bright, open and readable — **a sunlit street feel, not moody low key.** Midtones
healthy and luminous, never crushed. Protect the red sari and skin highlights from clipping. Paola sits
**a third to half a stop** brighter than the crowd — enough to separate, no more. Energized by daylight
and movement, not by fake overexposure or white-hot bloom.

**3 · Colour grade.** **The red sari is the hero colour and must dominate**, reading as *pomegranate
red, rich but not candy-bright.* The crowd lives in **dusty teal and muted blue-green** so Paola
separates instantly. Antique gold stays narrow and controlled — **about five percent of the total
read**, just enough to catch edges and jewellery. Environment sits in warm stone, beige and dusty
neutrals so red and teal carry the world. Skin natural and warm.
⚠ *Do not let the market turn into an orange-and-gold festival soup, and do not let the image slide
into cliché teal-orange action grading.*

**4 · Lighting.** **Motivated by real daylight only** — sun, open sky fill, wall bounce, practical
ambient bounce off the street. Best version is warm directional sunlight with soft ambient fill, giving
Paola gentle shape on face and sari **without looking studio-lit.** Background dancers lit consistently
with her, never singled out. Any backlight should make the georgette **breathe at the edges**.

**5 · Lens and atmosphere.** Clean lens behaviour, soft highlight roll-off, **restrained halation — not
dreamy blur.** Motion blur may live in the dancers and fabric but must read as *photographed movement,
not smeared AI motion.* Slight atmospheric dust. Overall **lively, airy and rhythmic — not heavy,
smoky or mystical.**

**6 · Texture and exclusions.** Physically filmed: real skin, real textile weave, real georgette drape,
believable gold trim, believable street surfaces. Fine grain if useful, **but not gritty.**
⚠ **Must not become:** wedding photography · devotional pageantry · over-saturated music-video gloss ·
Holi-colour chaos · fantasy-palace Bollywood · neon-nightclub Bollywood · AI beauty-poster polish.
⚠ **Do not over-jewel her** — the narrow border and sunglasses already do the work.

> The brief is **"contemporary synchronized street spectacle,"** not *"ornamental maximalism."*

---

**Nelson's brief:** *"match cut land into the scene & immediately dance doing the same hop while
travelling, w/ coordinate arm & hand movements, while the back up dancers are also syncing their dance
moves w/ hers so it looks bollywood synchronized."*

**Core instinct:** the landing is not a reset. **She arrives already inside the dance.**
Chain: match-cut continuity → embodied motion → synchronized expansion → spectacle payoff.

### Shots — locked by Franco 07-28

| Shot | Bars / Time | Beat |
|---|---|---|
| **1** | 1.5 · 15.0000–17.8125 | Match-cut **receive** from the W1 kickflip apex — same scale, angle and downward motion — then convert the landing into a travelling dance hop in the same direction. **The hop is the bridge.** Feet absorb impact, body rebounds into rhythm. Medium-full, slightly low, front 3/4 or side 3/4. The camera *receives* her arrival rather than observing it. Short, punchy bridge shot. |
| **2** | 2 · 17.8125–21.5625 | **Arms and hands become the star.** Still travelling, still dancing; the nearest dancers snap into her choreography — precise pickup, not random crowd dancing. The *"she leads, they answer"* shot. Synchronization grows outward from her. **Paola moves, the world obeys.** |
| **3** | 3 · 21.5625–27.1875 | **Full synchronized payoff.** The whole ring locks to her. Orbiting coverage — circular movement is *earned* here in a way it never was in skate. Not realism first: **spectacle through coordination.** Colour, costume and rhythm bloom. Longest shot in the world. |
| **4** | 1.5 · 27.1875–30.0000 | She **breaks forward through the hanging fabric.** Not an exit — a transformation gesture. The fabric wipe becomes the corridor. |

> *"Land into dance, dance becomes leadership, leadership becomes synchronized spectacle, spectacle
> becomes the transition."*

**Handoff note (Franco):** W2 Shot 1 begins from the exact W1 airborne body geometry and direction of
travel — **but the board is gone** and the costume and world are swapped. The hop is the bridge.

**Wardrobe:** pomegranate-red raw-silk blouse, fluid georgette sari, **narrow antique-gold border
only — gold ≈5%**, pointed-corner sunglasses, sleek centre part and low bun. Crowd stays **dusty teal**
so the red separates.

⚠ **The feet gap — Franco's ruling, 07-28.** Her Bollywood sheet is cropped above the feet.
**Board now, patch feet before video generation.** The board only needs action, camera, timing and
handoff logic, and a simplified full-body silhouette carries that. It becomes a real problem at **SD2
time on Shots 1 and 2**, where sari hem, ankle behaviour and hop mechanics matter.
**→ Build `Pao-Bolly-Full`: barefoot, anklet, sari hem visible, neutral front stance, plus a lower-body crop.**

---

# WORLD 3 · AGENT CORRIDOR — 30.0000–45.0000
### ✅ LOOK BLOCK LOCKED 2026-07-28 · shot logic + board still owed

## 🎨 GRADE NAME: **COLD GRAPHITE-CYAN PRECISION THRILLER**

> ⚠ **Provenance caveat, Franco's own words:** *"The exact 004016 CDN file did not resolve in this
> session, so this is corrected against the visible corridor plate, not a claim that I inspected that
> exact angle."* The link **HEAD-tests 200 from this machine** — his fetch failed on his side, not a
> dead link. **A link that resolves for me can still fail for him.** Re-send it with the board request.

### Compressed master look block — paste into every W3 generation
> Grounded premium live-action gun-fu thriller, ARRI Alexa-style LogC capture, cold industrial concrete
> corridor with wet reflective flooring, restrained graphite and cyan-blue grade, slightly underexposed
> but fully readable, natural warm-tan skin separated from the cold environment, deep detailed blacks,
> overhead practical lighting and reflected floor bounce only, subtle doorway spill, brief warm-white
> muzzle flashes, soft highlight roll-off, restrained halation, slight atmospheric depth, realistic lens
> behaviour.

### The six components — Franco, verbatim

**1 · Capture character.** Premium grounded live-action action cinema, ARRI Alexa-style LogC. The
corridor's strong architectural lines stay **disciplined and geometric.** Camera controlled, deliberate,
stabilized — no chaotic handheld except perhaps a brief physical jolt on impact. **Captured, not
rendered.** Enough depth that the corridor feels *long and oppressive.*
> **The visual relationship: architecture controls the frame, Paola controls the action.**

**2 · Exposure.** **Slightly underexposed, roughly half a stop dark** — but concrete texture, wet-floor
reflections and the black wardrobe layers must stay distinguishable. Paola's face sits **half to
three-quarters of a stop brighter** than the immediate background during the held close-up.
> ⚠ **The 5.625 s close-up is the crux.** It needs visible eye detail, small catchlights, natural skin
> texture and separation between black hair, black bomber and dark corridor. **Too dark and the held
> shot is dead. Too bright and it becomes beauty lighting and breaks the world.**

**3 · Colour grade.** Corridor lives in **graphite, charcoal, cold cyan-blue and a faint industrial
green cast** in the concrete. **Not vivid blue. Not neon teal.** Paola's skin stays natural warm tan but
restrained — **her warmth is the only human counterpoint to the environment. Do not push her orange.**
Black wardrobe separates by **texture**: tank = dense matte black · bomber = slightly cooler low-sheen
black · utility trousers a third value.

**4 · Lighting.** Overhead practicals and **reflected floor bounce only**, plus subtle doorway spill.
Wet floor throws reflections upward giving Paola **under-bounce** so she reads without looking
studio-lit. For the held close-up, a **motivated overhead-side practical** shapes one cheek and makes
eye catchlights, with negative fill controlling the other side — **no soft frontal beauty key.**
> **Muzzle flashes are events, not the permanent lighting design.** They briefly reveal concrete
> texture and edge-light the bomber, then disappear.

**5 · Lens and atmosphere.** Physically believable and slightly oppressive. Moderate lens compression,
especially on the held close-up, **but do not erase the receding architecture.** Restrained haze — just
enough to separate distant practicals. *"The plate already has a damp, heavy feeling, so avoid adding
theatrical smoke."* Gentle bloom around practical bulbs and wet reflections, subtle halation, shadows
stay detailed.

**6 · Texture and exclusions.** Restrained fine grain, realistic motion blur, **metal reflections hard
but imperfect**, real skin without beauty filtering.
⚠ **Must not become:** cyberpunk blue · teal-and-orange blockbuster grading · Matrix green · glossy
fashion noir · crushed-black silhouette soup · milky lifted blacks · commercial beauty portrait ·
fog-filled music-video atmosphere · video-game corridor rendering · over-sharpened tactical cosplay ·
permanent orange muzzle-flash lighting.

---

### The earlier draft look block — superseded, kept for reference
Written before the plates existed. Franco has now corrected it against the real corridor.
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

**Shot structure:** 1.5 / 3 / 1.5 / 2 — the **3-bar held close-up is 5.625 s**, the longest single
held frame in the reel. **Incoming:** the fabric wipe from W2 Shot 4. **Outgoing:** the gun pose that
W4 Shot 1 match-cuts into the steering wheel.

**Wardrobe:** black scoop-neck tank, high-waisted matte black utility trousers, cropped black bomber
worn open, narrow black belt, mid-calf black lace-up tactical boots. **Sleek** hair. *(Full verbatim
prompt in `ASSET_SPEC.md`.)*

---

# WORLD 4 · CAR CHASE — 45.0000–60.0000
### 🟢 SHOT LOGIC COMPLETE — Franco wrote it unprompted · board owed

**Nelson's brief:** *"the car chase i don't want agent, i want fast & furious visual style & grade."*

Franco: *"This is not corridor gun-fu in a car."* Same escalation rule, but **the body is now fused to
the vehicle.**

| Shot | Bars / Time | Beat |
|---|---|---|
| **1** | 2 · 45.0000–48.7500 | **Match from the gun pose into the wheel.** Hands already active — continuity carried through the arms and grip. The sensation changes immediately from *aiming* to *driving under force*. Camera inside the cabin or very near it: vibration, sunlight, dust, engine urgency. **Kinetic pressure, not corridor precision.** |
| **2** | 1.5 · 48.7500–51.5625 | **Externalize the motion.** Low fast exterior — road-level, wheel-line or side tracking. The car is not posed, it is **attacking space**. Make us feel acceleration, don't just show a car. |
| **3** | 3 · 51.5625–57.1875 | **The big move** — drift, hard corner, evasive manoeuvre, near miss, threading traffic. World 4's equivalent of the Bollywood spectacle shot. **The money action beat**, not a pretty car shot. Make the force legible: *she is controlling chaos.* |
| **4** | 1.5 · 57.1875–60.0000 | **Outgoing transformation.** Something flares, whips, wipes or rotates into the katana world — sunlight streak, dust burst, windshield flare, spinning motion. *"You don't just stop the chase. You convert the motion."* |

### Grade — and why the W3/W4 separation is load-bearing

> *"That separation is important because otherwise the reel feels like one long action mode."*

| | **World 3 · Agent** | **World 4 · Car** |
|---|---|---|
| Temperature | cold | **hot** |
| Space | architectural | open |
| Energy | controlled, precise, disciplined | kinetic, exposed, physically risky |
| Palette | blue, steel | amber, tan, sun-baked, chrome and windshield reflections |
| Reference | **John Wick** | **Fast and Furious** |

W4 is *sunlit, dusty, hot, warmer than World 3, less blue, less steel, more exposed.*

**Wardrobe:** same agent costume — it was specified to survive both worlds unchanged — with the
**messy bun and curls**. **Assets:** the richest world we have — 3 car interiors, both cars as 6-view
sheets, 4 desert road angles.

---

# WORLD 5 · JAPAN SWORD — 60.0000–75.0000
### 🔲 SHOT LOGIC OWED · ✅ **assets complete — the earlier "blocked" call was wrong**

**Structure:** 2.5 / 1 / 3 / 1.5 — the **1-bar second shot is the sharpest punctuation in the reel**
(1.875 s), and it lands right after the longest opening. First strike reads as a hard accent.

**Incoming:** the flare / dust burst / rotation out of W4 Shot 4.

**Assets — 17 items, all on Drive as of 07-28.** Four night-garden angles already form the four-POV set
(MAP = `W5_Garden_MAP_birdseye`, WIDE = `W5_Garden_NIGHT_wide`, WORK = `W5_Garden_NIGHT_shoji_POV`,
REVERSE = `W5_Garden_NIGHT_front_POV`), plus `W5_Kimono_sheet` at 5504×3072 and
`W5_Kimono_night_fullbody`, which is the hero frame — Paola lit in the night garden, arms open.
**No new plates required. No credits.**

> ⚠ **WARDROBE CONFLICT — Franco must rule.** Built = **pale pink/cream kimono, magenta obi**.
> Written spec = **midnight indigo, black-plum obi, oxblood sleeve lining**. Different garments.
> Several panels also carry the **pink flower Franco said to remove**. Either the W5 grade gets built
> around the pink that exists, or the kimono gets rebuilt to the indigo spec. **This blocks the W5
> look block**, because the grade has to know what colour the costume is.

---

# WORLD 6 · GOLD COUTURE RUNWAY — 75.0000–90.0000
### 🔲 SHOT LOGIC OWED · assets complete

**Structure:** 2.5 / 2 / 2 / 1.5 — *"entrance breathes, return concise."* The only world with two equal
middle shots; it walks rather than escalates.

**This is the reel's last visual detonation.** Gold goes from ≈5% trim in World 2 to **≈80%** here —
*"world two whispers gold and world six detonates it."*

### Wardrobe — the hardest sheet to stabilize
Single-piece gown, **burnished antique gold metallic silk lamé**, controlled low sheen — never plastic
or foil. Asymmetric **one-shoulder bodice covering her LEFT shoulder**, right shoulder bare. One fixed
anchor at the **left hip** holds a permanently sewn architectural pleated drape of **6–8 broad knife
pleats** that opens outward on every step. Long clean column skirt, one thigh-high slit over the left
leg, short restrained train. Minimal antique-gold ankle-strap heels. Small warm-gold hoop earrings.

**Non-negotiable hierarchy:** garment construction → hip-panel continuity → material realism → body
and pose. *"The hip attachment is the piece most likely to shapeshift."*

⚠ **There is NO hip fan** — that was a hallucination that propagated through the spec. It is a
**left-shoulder cape panel into a short train**. The reference board is the authority.
⚠ Must read as modern couture — **never a sari, lehenga, toga, pageant dress or bridal gown.**

**Assets:** six runway angles, the most of any location.

---

## 4 · SD2 generation path — Franco's revised layering, 07-28

**This changed today and it changes what the boards are for.**

> *"Then use: start frame + end frame + Paola ref + environment ref + audio for the first SD2 world
> test, and only add the storyboard if the middle progression gets muddy."*

So the **primary** path is **start frame + end frame + Paola ref + environment ref + audio**.
The **storyboard is a corrective layer**, held in reserve for when the middle progression drifts —
not a default input. Earlier guidance treated the board as one of three mandatory layers; **this
supersedes it.**

### What SD2 does and does not do with a board
**Understands:** the board as a sequence roadmap · reading order TL → TR → BL → BR · timestamps tied
to panels · broad progression of pose, camera and scene.
**Will not reliably do:** frame-accurate panel order · respect exact cut times because they are
written on it · preserve all four panels evenly · genuinely *cut* when the visual jumps are large.

⚠ **Describing what the progression MEANS beats listing timestamps.** The shot logic above is the
valuable half; the timecodes are the **trim plan**, not the instruction.

### Audio export rule
Export **each shot's exact section** from the master rather than feeding every clip the full 90 s.
Include **one bar of pre-roll** where Higgsfield allows it, and make the requested visible movement
**start on a clearly identified transient** — otherwise the model picks its own section and the anchor
becomes decorative.

---

## 5 · Standing constraints — never violate

- **4K + Unlimited toggle ON**, verified visually every batch. Never generate when it asks for credits.
- **Zero dollars spent** without Nelson's explicit go.
- Never delete — stage to `_TO_DELETE_VERIFY`.
- **Never create Higgsfield elements via MCP** — they store an expiring signed URL and die. Web UI only.
- Every Paola prompt embeds the 3 Drive reference links + feature block + gate-v2.

---

## 6 · Open items

| # | Item | Blocks |
|---|---|---|
| 1 | **W2 board** — Franco rendering now | W2 execution |
| 2 | **W3, W5, W6 shot logic** — Franco offered, never claimed | 3 boards |
| 3 | **W5 assets** — no character sheet, no location, not on Drive | all W5 work |
| 4 | **`Pao-Bolly-Full`** barefoot full-body + lower-body crop | W2 SD2 gen, not boarding |
| 5 | **Lattice ratification stamp** — Nelson's formal call | nothing; everything already assumes it |
| 6 | **Exact SD2 prompt structure** — Franco offered reference hierarchy, storyboard wording, timestamp wording | paid generation |
| 7 | **L/R three-quarter identity refs** — Franco asked for these twice; a frontal alone *"will not adequately police her nose, jaw and eye shape"* | identity drift across angles |
