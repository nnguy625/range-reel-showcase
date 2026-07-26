# PROJECT BRIEF FOR REVIEW — "RANGE REEL"
**Prepared for external review. Date: 2026-07-25.**

---

## 1. WHAT CHANGED

An 18-minute narrative short film has been parked. It stalled for two weeks on a single over-the-shoulder still, running eight prompt architectures across ten draws with zero usable hits, and produced one video draft judged unusable. The mid-August delivery date is g***REMOVED***

The diagnosis, from the production record rather than from feeling: a narrative short fights generative video's core weakness, which is sustained continuity across time and across cuts. Every hour went into that fight instead of into footage.

**The replacement is a 90-second genre-morph range reel.** Same character throughout. Six worlds. Her wardrobe, environment, and genre change under her while her face does not. Cut to a percussion-driven instrumental.

**Why this is a pivot and not a retreat:**

- Every cut is *motivated by the concept*, so visual drift becomes the aesthetic rather than a defect to fight.
- Shots are independent and roughly 3.7 seconds. A failed shot costs one generation, not a scene. Partial progress remains a deliverable.
- It demonstrates the things a production reel is judged on — range, character consistency under radical change, transition craft, music sync, throughput. A narrative short tests writing and directing, which is a different claim.

**Purpose of the artifact:** the reel plus its process documentation is the proof of method — the shots and the system that made them, shown together.

---

## 2. WHAT THE REEL MUST PROVE

In priority order. Review should weight feedback accordingly.

1. **It is obviously the same woman in all six worlds.** This is the technical claim. If a viewer with no context cannot tell, the reel has failed regardless of how good anything else looks.
2. **The cuts are designed, not assembled.** A gesture starts in one world and finishes in the next.
3. **It is engaging in the first two seconds and does not lose the viewer.** The prior work was judged "she looks real, but not engaging enough to stop a scroll." That is the specific failure being corrected.
4. **The range is legible.** Six visibly different genres, each competently executed rather than gestured at.

---

## 3. STRUCTURE AND TIMING

**130 BPM with a half-time backbeat** (kick on 1, snare on 3), giving a slow head-nod pocket over a fast grid.

| Unit | Length |
|---|---|
| 1 bar | 1.85s |
| 1 shot | 2 bars = 3.7s |
| 1 world | 8 bars = 14.8s |
| Master | 6 worlds = **88.6s** |

3.7 seconds per shot is deliberate. The director's note was that moments should breathe rather than rush. The generation model delivers 5-second clips, so every shot carries trim headroom rather than being cut to the frame.

A second cut of roughly 40 seconds, vertical, will be pulled from the master with the hook inside 1.5 seconds.

---

## 4. THE SIX WORLDS, SHOT BY SHOT

### World 1 — SoCal street, skateboarding (0:00–0:15)

| Shot | Beat | Camera |
|---|---|---|
| 1 | She pushes off, board under her, street ahead | Low track alongside the trucks |
| 2 | Speed builds, carving past parked cars | Rise to profile |
| 3 | Whip as she passes a pole | Whip pan |
| 4 | **Kickflip apex, slow motion** — board mid-rotation, body airborne | Low, rising with her |

The full trick is never generated. Apex only, no pop and no landing. The landing occurs in World 2.

### World 2 — India, Bollywood (0:15–0:30)

| Shot | Beat | Camera |
|---|---|---|
| 1 | She comes down out of the descent and lands in the street, movement already alive around her | Low, catching the arrival |
| 2 | She hits a move, the nearest dancers echo it, the ring picks it up | Tracking backward ahead of her |
| 3 | Full circle orbiting her, everyone on her shape, color at maximum | Push in, short hold |
| 4 | She breaks forward and runs through a curtain of hanging market fabric | Follow, into full-frame cloth |

**Key prompt decision:** the dancers *mirror her movement*. They are not described as synchronized. Synchronization asks the model to invent unison across many independently generated people. Mirroring gives it one canonical pose to propagate. Reviewers should challenge whether this distinction survives contact with the model.

**Depth of field is a deliberate exception** to the standing deep-focus rule. Her sharp, the ring soft but legible — costume color, arm position, direction of travel readable, faces soft. The blur is doing defect-suppression work.

### World 3 — Gun-fu, cold and desaturated (0:30–0:44)

| Shot | Beat | Camera |
|---|---|---|
| 1 | Bursts through the fabric already committed to a tumble roll, lands behind cover | Follow through the seam |
| 2 | **Held.** Back against cover, breathing, rounds striking the other side | Static, close |
| 3 | Cover tearing apart, muzzle flash strobing her face out of the dark | Slow push |
| 4 | She turns out and fires | Whip to her |

Shot 2 is the cheapest shot in the reel and possibly the most valuable — static, close, face large and lit, identity locking hard. Everything around it is movement. One beat of a person deciding to move is what gives the movement meaning.

The gunshot is not generated. The *light the gunshot makes* is. Mechanism stays mostly off-frame or in silhouette.

Desaturation additionally suppresses the standard artifact set — oily skin, plastic highlights, color fringing are all more visible in saturated footage. Wet ground adds reflections at no cost.

### World 4 — Car chase (0:44–0:59)

| Shot | Beat | Camera |
|---|---|---|
| 1 | Interior, her at the wheel, windows down | Passenger side, face lit by passing light |
| 2 | Exterior chase, speed, the pursuer closing | Low chase cam |
| 3 | **The drift** | Exterior, arcing |
| 4 | Mid-drift she leans out and fires; cut to the pursuer spinning into the blockage | Interior, then hard cut to consequence |

She fires at the wheel, not the driver. Character choice, kept deliberately.

Cause and effect are split across the cut. Two tires deflating because she shot them is a causal chain to render inside one clip. She fires, cut, the pursuer spins out.

**Highest-risk shot in the reel is the exterior drift** — a rigid body rotating while translating. Three attempts, no fourth. The fallback is already designed: shoot it from inside, her face steady in frame while the world rotates past the window. Car static in frame, background does the moving, identity holds throughout.

### World 5 — Japan, sword (0:59–1:14)

Tone: serious. Choreography reference is *The Last Samurai* — committed single strikes with pauses between, weight and stance, no flurries and no wire work.

| Shot | Beat | Camera |
|---|---|---|
| 1 | Standoff, moonlit garden, blades drawn, held | Previously approved composition |
| 2 | First exchange, one committed strike, blades meet | Low, tight |
| 3 | The counter, her turn, decisive | Arc with the cut |
| 4 | She spins with an opening at his neck — **cut on the blade mid-arc** | Follow the rotation |

That rhythm — strike, separate, breathe, strike — is both the reference's actual cadence and the safest generation pattern available. Single committed movements render cleanly and the pauses are natural cut points.

**This world reuses existing assets.** Character sheets, three environment angles, a floorplan, and an approved two-hander composition already exist from the parked project. It is the only world that starts from work already d***REMOVED***

### World 6 — Gold couture, returning to normal (1:14–1:29)

| Shot | Beat | Camera |
|---|---|---|
| 1 | The turn completes as a model's turn at the top of an aisle, gold | Reveal, wide to medium |
| 2 | **The walk.** On the beat, every step landing on a hit | Tracking backward ahead of her |
| 3 | The turn, the peak | Slow orbit |
| 4 | She keeps walking and it becomes the SoCal sidewalk, casual clothes, board under her arm | Continuous, no cut |

The music does **not** drop to silence here. The arrangement strips to bare percussion so every step lands on a hit. This is a power beat, not a stillness beat.

Gold is deliberate rather than decorative. Gold already appears in World 2 as festival color — powder, marigold, jewelry. Its return as couture is the same color arriving refined, not a repeat. It also sits correctly against warm skin in a way the originally drafted red did not. The fabric must move on every step; a stiff garment kills the walk.

Shot 4 is the closing argument. The runway becomes a sidewalk, the gown becomes jeans, the walk never breaks stride. Same woman. No voiceover, no card required.

---

## 5. THE GESTURE CHAIN

The governing rule: **a gesture begins in world A and completes in world B.** Not similar poses either side of a cut. One continuous shape, interrupted by the world changing around it.

A second rule sits underneath it: **cut on the wind-up, relocate the payoff.** Show the preparation and the mid-motion, cut before the resolution, let the next world deliver it transformed. The viewer's brain completes the movement, and what it completes into is somewhere else entirely.

| Cut | Gesture completing across it | Mask |
|---|---|---|
| 1 → 2 | Airborne, coming down. Kickflip apex completes as her landing in the street | none, hard match |
| 2 → 3 | Forward run through an occluder | hanging market fabric, full frame |
| 3 → 4 | Arms extended forward. Firing becomes hands on the wheel | none, hard cut on the beat |
| 4 → 5 | Rotation. The drift's spin completes as her turning to face him | none, hard match |
| 5 → 6 | Rotation. A killing arc completes as a runway turn | none, hard match |
| 6 → out | The walk continues, the world changes under her | none, continuous |

Transition types are mixed on purpose — one masked seam, four hard matches, one continuous. All-masked reads as a transition demo. All-cut reads as a slideshow.

Masked transitions require the occluder to fill 100% of frame for several frames. Two clips: one ending as it fills, one beginning as it clears, motion continuous across the seam in direction and speed.

---

## 6. PRODUCTION LAW: CONSEQUENCE VERSUS MECHANISM

A narrow rule, applied only where the model cannot hold the physics — never as a way to hide action.

| Instead of | Generate |
|---|---|
| Two tires deflating because they were shot | Her firing, cut, the spin-out |
| A rigid body rotating while translating *(fallback only)* | Her face steady, the world rotating past the window |

The mechanism is shown everywhere it is the shot. The kickflip apex and the muzzle flash on her face are **mid-motion moments**, which is where the spectacle lives, and both are generated directly.

---

## 7. ASSET ARCHITECTURE

Governing principle, carried over from the parked project: **exactly one reference owns each variable.** If a variable has no owner, the shot does not get sent.

**Identity.** A single character element, `Paola_Face_Lock`, already built and used across 20 generations. It owns identity and nothing else does. It carries into every world unchanged. No world description, wardrobe note, or environment prompt is permitted to also describe her face.

**Wardrobe.** One three-panel reference sheet per world, front-facing, **headless**. Headless is not cosmetic — attaching a full sheet alongside a face reference causes the model to average two faces. Removing the head from the wardrobe sheet leaves identity with exactly one owner.

| World | Wardrobe |
|---|---|
| 1 | Skate casual — relaxed cut below, fitted above, real skate shoes, nothing costumey |
| 2 | Sari, festival color, gold at the edges |
| 3 | Agent — tailored, dark, functional |
| 4 | Driver — stripped down, practical |
| 5 | Kimono, closed, obi *(sheet already exists)* |
| 6 | Gold couture, bias cut, fabric that moves on every step |

World 1's wardrobe returns in the final shot, so it is used twice.

**Props.** The test for whether something is a prop rather than wardrobe: **does it change state during the reel?**

Anything that gets drawn, pulled, ridden, set down, or that appears and disappears needs its own reference, because its appearance must stay locked independently of the body carrying it. There is a second reason pointing the same way — held objects sit in hand contact, which is the highest-failure-rate region of any frame, so they earn a dedicated reference with maximum detail.

| Props | Wardrobe |
|---|---|
| Sword, sidearm, skateboard | Belts, jewelry, footwear, obi |

Sunglasses are wardrobe unless she removes them, at which point they become a prop.

---

## 8. DE-RISKING RULES

Direct countermeasures to what killed the parked project.

1. **Three attempts per shot.** Three failures means change the framing or cut the shot. There is no fourth version.
2. **No shot is load-bearing.** Any beat can be dropped without breaking the piece.
3. **Frame for the face.** Identity pressure and small subject scale is a contradiction the model resolves by discarding ***REMOVED*** Never write both into the same shot.
4. **One variable per retry.**
5. **Beat map locked before generation.** No generating into an undecided edit.

---

## 9. WHAT IS KNOWN ABOUT THE TOOLING

Verified rather than assumed, since several assumptions did not survive checking.

- Generation caps at 4 to 15 seconds per clip across every provider checked. A 90-second reel is an assembly problem by definition.
- Stepping above 720p on video drops out of flat-fee billing into metered per-generation charges. Every retry stops being free.
- The one comparable independent artifact — a 20-minute solo AI film on the identical toolchain — disclosed **3,229 generations across 242 hours**. Its 4K was an upscale, not native generation. Scaled proportionally, a cut-dense 90-second reel should be budgeted at 240 generations and upward.
- **No one has published a test of whether generation resolution affects face stability or identity consistency.** This is the single most relevant unknown and it is unanswered in either direction.

---

## 10. QUESTIONS FOR REVIEW

Ranked. Direct attacks preferred over general impressions.

1. **Does the same-woman claim survive six wardrobe changes?** The mitigation is a single face element plus headless wardrobe sheets plus a rule that shots requiring identity are medium or closer. Is that sufficient, and where does it break first?

2. **World 3 into World 4 is the weakest cut.** It is the only hard cut between two adjacent modern-action worlds, so a wardrobe change there risks reading as a continuity error rather than a world change. Does the audience have the rule by then, or does it need a mask?

3. **Is "the dancers mirror her movement" actually a better prompt than "synchronized dancers"?** The reasoning is that mirroring supplies one canonical pose to propagate rather than asking for invented unison. This is a hypothesis, not a tested finding.

4. **Is four shots enough per world to establish a genre?** Or do some worlds need five and others three?

5. **Does the ending land?** Gold couture walking continuously into a sidewalk and jeans, no card, no voiceover. Is that legible as a thesis or merely as an ending?

6. **What is missing?** Specifically: which shot in this plan will fail first, and what should replace it.

---

*Six worlds, twenty-four shots, 88.6 seconds. Nothing has been generated yet. This is the last cheap moment to be wrong.*
