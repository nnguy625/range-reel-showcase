# REVIEW VERDICT — adversarial pass, 2026-07-25

*Two review rounds: creative plan, then execution and risk. Nothing had been generated, so every correction was free.*

---

## SCORE

Twelve substantive catches against the plan. One held position. The plan is materially better than it was this morning.

---

## WHAT GOT CORRECTED

**1. Identity had unowned variables.** The plan assigned face and clothing an owner and stopped there. Nothing owned height, shoulder width, proportions, hair silhouette, posture or gait. Six worlds could produce six differently-built women wearing related versions of the same face.
→ Added a body sheet in neutral fitted clothing, one fixed hair silhouette across all worlds, one identity-anchor shot per world, and a blind test on people who do not know her.

**2. World 3 into World 4 — wrong diagnosis.** The plan flagged the cut as weak. The worlds are the problem. Both were modern, armed, dark. A flawless transition still reads as a costume change inside one movie.
→ World 4 goes sunlit, dusty, warm, physically exposed. Closer to the actual genre reference anyway, which is sun and chrome rather than rain and neon.

**3. "Mirror her movement" is a dangerous word.** It may produce literal bilateral symmetry, cloned dancers, reversed limbs, or people facing each other.
→ Replaced with a concrete count: three foreground dancers reach the same arm line and foot plant at the same moment; background holds simpler complementary poses.

**4. Twenty-four equal shots is an editing constraint pretending to be a principle.** Forcing every shot to 3.7 seconds creates visible filler.
→ Roughly 17 shots with variable lengths. One bar for impacts, two bars for identity holds.

**5. The ending was the most dangerous shot in the reel**, not the drift. A continuous generation transforming environment, wardrobe, lighting, fabric, props and hair while face, body, stride, scale and screen position stay stable. The plan also called it "the closing argument," which made "no shot is load-bearing" false in its own document.
→ Concealed two-clip transition behind a full-frame occluder, emerging at the same stride phase, scale and screen position.

**6. "No shot is load-bearing" is false.** Six shots carry the concept.

**7. Three attempts per shot is arbitrary.** A disposable insert and the final transformation should not get equal budgets.
→ Stop on learning rate, not attempt count. Continue only when the next attempt tests a clear hypothesis. Stop when the same failure survives materially different approaches, or the last three meaningful changes produced no visible improvement.

**8. Rhythm is not culturally neutral.** Meter, swing, syncopation, backbeat placement, percussion tone and bass pattern all carry association. The skeleton reads as contemporary trailer or pop language — which is a culture, just a different ***REMOVED***
→ Keep the skeleton, drop the claim that it is neutral.

**9. Do not regenerate six variations.** Tempo drift is documented; "matches pretty well" is not sample-accurate synchronization.
→ **One continuous percussion file that never changes and is never regenerated.** Generate only the world-specific instrumental overlays, then trim, warp and crossfade them over the fixed spine in the edit.

**10. "Desaturation suppresses artifacts" is overstated.** It helps some colour defects. It does nothing for anatomy, identity, motion or temporal coherence. Wet ground is also not free — reflections are a second moving geometry system that can contradict the first.

**11. "Exactly what a production reel is judged on" is unsupported.** The reel demonstrates taste, generation skill and transition design. It does not demonstrate pipeline engineering, iteration discipline, tool integration or cost control. **The written record has to carry that**, and it only exists if failures and decisions are recorded live.

**12. World 2 risks generic exotica.** "India, Bollywood" is a location and an industry label, not a treatment. Period, production-design logic, dance vocabulary, location type and camera reference get defined before generating.

---

## WHAT WAS HELD

**The drift stays.** The recommendation was to cut it as expensive coverage. It is a director's requirement, not a coverage decision, so it stands. The exterior chase cam was cut instead — that was the genuinely redundant shot.

---

## MUSIC — CORRECTED ARCHITECTURE

**One percussion file. Forever. Never regenerated.**

Overlays only, per world. Trimmed, warped, crossfaded over the fixed spine in Resolve.

**Order of operations:**
1. Lock BPM, bar grid, total duration, transition bars, major impact beats.
2. Cut rough picture to that skeleton.
3. Generate and place the six overlays.
4. Finalise the arrangement, make small picture trims against it.
5. Lock picture and music together.

Never lock either one in isolation.

---

## CAMERA — RELIABILITY RULES

**One dominant source of motion per shot.** Camera, subject, or environment. Two is acceptable when one is simple. **Three at once is a high-risk shot.**

| Safe | Conditional | Exception only |
|---|---|---|
| Locked, slow push, slow pullback, simple pan, simple tilt, short straight lateral track | Low tracking and backward tracking — one subject, clean path, limited foreground occlusion, no busy crowd. Shallow arcs under 20–30°, not requiring exact facial geometry throughout | Full orbits, long reverse tracking through crowds, crane-plus-orbit compounds, rapid lens changes, moving camera with multiple moving bodies |

**Whip pans are unreliable when they must land on an exact composition.** Generate two stable shots and build the whip in Resolve.

**Allocation across 90 seconds:** one compound move at most. Identity anchors are locked. Strong movement belongs at world entrances, transitions and the peak. Never several aggressive moves consecutively. *Direction comes from contrast between stillness and motion, not from keeping the camera permanently caffeinated.*

Capability demonstrations from a vendor do not establish a predictable success rate.

---

## COMPOSITION — THE CHECKLIST

Applied to every still before it is animated.

**Placement.** Eyes near the upper-third line in close and medium shots. Face or torso clearly on a third, **or** exactly on the centreline. Avoid weak almost-centred framing.

**When to centre:** frontal identity reveals, symmetry, transformation, authority, direct confrontation, impact.
**When to go off-centre:** movement, eyelines, tension, environmental context.

**Directional space.** At least 1.5× more space in the direction of gaze or travel than behind.

**Headroom.** Close-up 2–5% of frame height. Medium and full-body 5–8%.

**Cropping.** Never through wrists, knees, ankles or elbows.

**Lens height.** Full-body action sits around lower-chest to waist height, camera level, wide enough to show the whole action path with room for the final position. Low and high angles need a stated power or vulnerability reason — they are not decoration.

**Separation.** No background lines through the head. No tangencies where limbs merge into scenery. Clean silhouette around face and shoulders.

**Foreground and negative space.** Foreground only for depth or eye direction, never to look cinematic. Negative space reserved for gaze, movement, reveal or transition information.

**Vertical safety.** Mark the central 32% of the 16:9 frame as the approximate 9:16 crop z***REMOVED*** Keep essential face and action inside it, or accept that the shot is horizontal-only.

**The gate:** before animation, the still must read at thumbnail size, the face must separate cleanly, the action must be understandable without the prompt, and the required crop must already work. **Video generation is not allowed to repair weak composition.**

---

## THE SINGLE HIGHEST-VALUE DECISION

**Make the deadline fixed and the shot list elastic.**

Every high-risk shot gets three versions defined now: the intended version, a simpler substitute, and a cut option. When the time tripwire fires, the substitute activates automatically. No debate, no one-last-prompt.

That is the mechanism that stops one shot becoming another two-week hostage.
