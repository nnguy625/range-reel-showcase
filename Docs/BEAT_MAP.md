# PAOLA RANGE REEL — BEAT MAP v3
*Phase 0. Six worlds locked 2026-07-25. Nothing generates until the track exists.*

**The claim the reel makes:** one woman, six worlds, her face holds throughout. The music makes the same argument — one rhythmic spine, six arrangements. Same essence, adapts to anything.

---

## THE GRID

**128 BPM, half-time backbeat** (kick on 1, snare on 3). Slow head-nod pocket over a fast grid.

*(Corrected 2026-07-26. 130 was a planning number chosen before the track existed; the built spine measures 128.2 and the spine is the physical artifact, so it wins. 128 is also the cleaner grid — see below.)*

| Unit | Length |
|---|---|
| 1 bar | 1.875s |
| ~~1 shot~~ | ~~2 bars = 3.75s~~ — ⚠ **SUPERSEDED, see below** |
| 1 world | 8 bars = **15.000s exactly** |
| Full master | 6 worlds = **90.000s exactly** |

> ## ⚠ THE UNIFORM 2-BAR SHOT IS OBSOLETE — DO NOT GENERATE AGAINST IT
>
> **Franco, 2026-07-27:** *"Ratify the half-bar lattice. The uniform two-bar plan is **obsolete** and
> should be removed from BEAT_MAP and BOARDING_SPEC **before it accidentally drives generation**."*
>
> He has now given the same six allocations **twice independently** (overnight, and again on 07-27),
> and his `WORLD1_SHOT_PLAN.md` is already written against them. **Every world still totals 8 bars and
> 15.000 s, and every world transition still lands on beat 1** — only the internal sentence rhythm
> changes.
>
> | World | Bars | |
> |---|---|---|
> | 1 skate | **1.5 / 2.5 / 1 / 3** | |
> | 2 bolly | **1.5 / 2 / 3 / 1.5** | |
> | 3 agent | **1.5 / 3 / 1.5 / 2** | held close-up = 5.625 s |
> | 4 car | **2 / 1.5 / 3 / 1.5** | the drift = 5.625 s |
> | 5 sword | **2.5 / 1 / 3 / 1.5** | first strike is a sharp punctuation |
> | 6 runway | **2.5 / 2 / 2 / 1.5** | entrance breathes, return concise |
>
> Short shots generate as **four-second clips** (SD2's floor) with the endpoint staged early, then get
> trimmed on the half-bar cut.
>
> Franco's plain-language version: *"the old plan cut every sentence into four equal chunks. The new
> plan still rhymes, but it breathes like a movie instead of marching like PowerPoint."*
>
> **🔲 Nelson's ratification stamp is still outstanding.** Franco recommends it, the desk agrees, and
> `WORLD1_SHOT_PLAN.md` already uses it — but the formal call is Nelson's. The old numbers are struck
> through rather than deleted so nothing generates against them in the meantime.

~~3.75s per shot is deliberate. Moments breathe, they don't rush.~~ **The trim-headroom argument
survives the change** — SD2 delivers 4–5 s clips, so the 1-bar (1.875 s) and 1.5-bar (2.8125 s) shots
are trim jobs rather than generations, and the 3-bar shots (5.625 s) sit just above a single clip.

**128 makes every boundary land on a whole second.** Each world is exactly 15.000s and the master is exactly 90.000s, so world changes fall at 0:15, 0:30, 0:45, 1:00 and 1:15 with no rounding. At 130 they drifted by a fifth of a second per world.

---

## THE SIX WORLDS

| # | World | Time | Signature instrument |
|---|---|---|---|
| 1 | SoCal street, skate | 0:00–0:15 | muted bass, chopped guitar harmonics |
| 2 | India, Bollywood | 0:15–0:30 | plucked sitar, dhol accents |
| 3 | Gun-fu, Wick | 0:30–0:45 | low strings, muted brass, struck steel |
| 4 | Car chase, sunlit | 0:45–1:00 | distorted baritone, engine-tuned synth |
| 5 | Japan, sword | 1:00–1:15 | shamisen, koto, shakuhachi breath |
| 6 | Gold couture → normal | 1:15–1:30 | deep house bass, glassy pulses |

Spine never stops: low drums, backbeat, shaker subdivisions. **The constant is rhythm, the swap is timbre.** Anything with a passport goes in the swap layer.

The spine is built: `Assets/Music/E1_MASTER_90.wav`, 90.000s at 128 BPM, ten dropouts patched out.

---

## WORLD 1 — SOCAL STREET

| Shot | Beat | Camera |
|---|---|---|
| 1 | She pushes off, board under her, street ahead | Low track alongside the trucks |
| 2 | Speed builds, she carves past parked cars | Rise to profile |
| 3 | Whip as she passes a pole | Whip pan |
| 4 | **Kickflip apex, slow motion** — board mid-rotation, body airborne | Low, rising with her |

**Never generate the full trick.** Apex only. No pop, no land. The landing happens in World 2.

---

## WORLD 2 — INDIA, BOLLYWOOD

| Shot | Beat | Camera |
|---|---|---|
| 1 | She comes down out of the descent and lands in the street, movement already alive around her | Low, catching the arrival |
| 2 | She hits a move, nearest dancers take it, the ring picks it up | Tracking backward ahead of her |
| 3 | Full circle orbiting her, everyone on her shape, color at maximum | Push in, short hold |
| 4 | She breaks forward, runs through a curtain of hanging market fabric | Follow, into full-frame cloth |

**Mimicry, not synchronization.** "The dancers echo her movement" gives the model one canonical pose to propagate. "Twenty synchronized dancers" asks it to invent unison across twenty independently generated people, which is the thing it cannot do.

**Circling helps mechanically.** Dancers orbiting enter and leave frame constantly, so no individual has to hold together longer than a beat.

**Depth of field:** her sharp, ring soft but readable. Costume color, arm position, direction of travel stay legible. Faces go soft. This is a deliberate exception to the deep-focus rule — the blur is doing defect-hiding work.

---

## WORLD 3 — GUN-FU · 0:30–0:45

| Shot | Beat | Camera |
|---|---|---|
| 1 | Bursts through the fabric already committed to the tumble roll, lands behind cover | Follow through the seam |
| 2 | **Held.** Back against cover, breathing, rounds hitting the other side | Static, close |
| 3 | Cover tearing apart, muzzle flash strobing her face out of the dark | Slow push |
| 4 | She turns out and fires | Whip to her |

Shot 2 is the cheapest shot in the reel and possibly the most valuable. Static, close, face large and lit — identity locks hard. Everything around it is movement; one beat of a person deciding to move is what makes the movement mean something.

**Don't generate the gunshot, generate the light it makes.** Face strobing out of darkness on the beat, mechanism mostly off-frame or in silhouette.

**Desaturation is doing hidden work.** Oily skin, plastic highlights, color fringing — every AI tell is more visible in saturated footage. A cold desaturated grade suppresses all of them. Add wet ground; reflections read as production value for free.

---

## WORLD 4 — CAR CHASE, SUNLIT · 0:45–1:00

| Shot | Beat | Camera |
|---|---|---|
| 1 | Interior, her at the wheel, windows down | Passenger-side, her face lit by passing light |
| 2 | Exterior chase, speed, the pursuer closing | Low chase cam |
| 3 | **The drift** | Exterior, arcing |
| 4 | Mid-drift she leans out and fires; cut to the pursuer spinning into the blockage | Interior → hard cut to consequence |

**She shoots the wheel, not the driver.** Character choice. Reads as competence, not brutality, and keeps the reel showable anywhere.

**Split cause from effect across the cut.** Two specific tires deflating because she shot them is a causal chain to render inside one clip. Show her fire, cut, show the spin-out. Standard action grammar and more legible than the literal version.

**Drift fallback:** if the exterior drift fails three attempts, shoot it from **inside** — her face steady in frame while the world rotates past the window. Car static in frame, background does the moving, identity holds. Three attempts, no fourth.

---

## WORLD 5 — JAPAN, SWORD · 1:00–1:15

*Tone: serious. Last Samurai choreography — committed single strikes with pauses between, weight and stance, no flurries, no wire work. The comedy/umbrella ruling was made for the short film and does not travel here.*

| Shot | Beat | Camera |
|---|---|---|
| 1 | Standoff, moonlit garden, blades drawn, held | The approved composition |
| 2 | First exchange, one committed strike, blades meet | Low, tight |
| 3 | The counter, her turn, decisive | Arc with the cut |
| 4 | She spins, the blade comes around with an opening at his neck — **cut on the blade mid-arc** | Follow the rotation |

The Last Samurai rhythm — strike, separate, breathe, strike — is both the reference's actual cadence and the safest generation pattern. Single committed movements generate cleanly; the pauses are natural cut points.

**Blade continuity** is the one thing to watch: a sword is a rigid object that must hold length and shape across frames. Motion blur on the committed cut covers most of it. Sparks on contact are a light event, which the model handles well.

**Assets already on disk — this world starts from a shoot that already happened:**
- Character: `REF-PAO-KIMONO-FINAL.png`, `Paola_Kimono Ref Sheet.png` (6-panel), `REF-PAO-FACE-POSITIVE.png`, `PAOLA_IDENTITY_ANCHOR_IMG0147_v1.jpeg`
- Ninja: `REF-NINJA.png`, `NinjaREF1.png`, `ninja_strawhat_REF_moonlit.jpeg`
- Garden night, three angles: `ref_garden_nite_wide.png`, `ref_garden_nite_loweye.png`, `ref_garden_nite_3-4_house.png`
- Floorplan: `APPROVED_PLATES/GARDEN_NIGHT_BIRDSEYE_MASTER.png`
- Approved two-hander: `APPROVED_PLATES/01_COMPOSITION.png`

---

## WORLD 6 — GOLD COUTURE → NORMAL · 1:15–1:30

| Shot | Beat | Camera |
|---|---|---|
| 1 | The rotation completes as a model's turn at the top of the aisle, gold | Reveal, wide to medium |
| 2 | **The walk.** On the beat, every step landing on a hit | Tracking backward ahead of her |
| 3 | The turn, the peak | Slow orbit |
| 4 | She keeps walking and it becomes the SoCal sidewalk, same casual clothes she opened in, no board | Concealed two-clip cut behind a full-frame occluder |

**The runway does not drop to silence.** The arrangement strips to bare percussion so every step lands on a hit. This is a power beat, not a stillness beat — it keeps the head-bob promise through the peak instead of breaking it.

Shot 4 is the reel's closing argument. The runway becomes a sidewalk, the gown becomes the clothes she opened in, the walk never breaks stride. Same woman. Stated without a word of voiceover.

She comes back without the board. She opened carrying the thing that started the journey and returns not needing it. It also strips a prop, a hand-contact region and a rigid-body geometry out of the most transformation-heavy shot in the piece.

**This is a concealed two-clip cut, not one continuous generation.** A full-frame occluder — the gown itself in motion is the least arbitrary option — covers the seam, and she emerges at the same stride phase, scale and screen position. Asking one generation to transform environment, wardrobe, lighting and fabric while holding face, body, stride and framing was the single riskiest thing in the plan.

---

## THE GESTURE CHAIN

A gesture starts in world A and completes in world B. Not similar poses either side of a cut — one continuous shape, interrupted by the world changing around it.

| Cut | Gesture | Mask |
|---|---|---|
| 1 → 2 | Airborne, coming down. Kickflip apex completes as her landing in the street | none, hard match |
| 2 → 3 | Forward run through an occluder | **hanging market fabric**, full frame |
| 3 → 4 | Arms extended forward. Firing becomes hands on the wheel | none, hard cut on the beat |
| 4 → 5 | Rotation. The drift's spin completes as her turning to face him | none, hard match |
| 5 → 6 | Dissolve. His particles fill frame and clear onto the aisle | **particles**, full frame |
| 6 → end | The walk continues, the world changes under her | none, continuous |

**Mixing transition types is deliberate.** Two masked seams, three hard matches, one continuous. All-masked reads as a transition demo; all-cut reads as a slideshow.

**Masked transitions require 100% frame coverage for several frames.** Two clips: one ending as the occluder fills, one starting as it clears. Motion continuous across the seam — same direction, same speed.

---

## THE LAW THIS REEL RUNS ON

**Generate the consequence, skip the mechanism.** It decided four shots independently before anyone named it:

| Instead of | Generate |
|---|---|
| The full kickflip | The apex |
| The gunshot | The light it makes |
| Two tires deflating on cue | Her firing, cut, the spin-out |
| A car rotating while translating | Her face steady, the world rotating past the window |

---

## MUSIC

**Reference:** Rurouni Kenshin, Kyoto arc — taiko and shamisen driving underneath, shakuhachi over the top, strings carrying urgency, martial pulse. Modernized: tighter drums, real sub-bass.

**Structure:** hard open at full energy, escalate through the action worlds, strip to bare percussion for the runway, resolve back to the opening texture.

**No lyrics.** Wordless chant only if it earns its place.

**Already built and directly reusable:** `Paola's Theme` exists as five arrangements — Percussion, Bass, Synth, Soft, Piano. Same theme, re-arranged per context. That is this reel's structure, already proven in June. The percussion stem is the closest thing on disk to the spine and is the reference to hand Suno rather than describing it in words.

---

## DE-RISKING RULES

1. **Three attempts per shot.** Three failures → change the framing or cut the shot. There is no fourth version, ever.
2. **No shot is load-bearing.** Any beat can drop without breaking the piece.
3. **Frame for the face.** Identity pressure and small scale is a contradiction the model resolves by picking ***REMOVED*** Never write both.
4. **One variable per retry.**
5. **Beat map locked before generation.** No generating into an undecided edit.

---

## OPEN

- [ ] The track. Everything downstream is timed off it. **This is the next action.**
- [ ] Resolution decision — pending the SD2 4K research and one controlled A/B clip (same prompt, same reference, same seed, 720p vs 4K, crop-zoom both faces at full res).
- [ ] Five new character elements (worlds 1–4 and 6). World 5 is already built.
- [ ] Vertical cut: ~40s pulled from the master, hook inside 1.5s, built to loop.
