# SD2 EXTENSION + AUDIO TESTS — Franco's protocol
### Ruled 2026-07-31, on Nelson's proposal to use SD2's video-extension feature and full-world audio.
### **Run these in order. Test 1 first — it can erase the most plate work.**

---

## THE GOVERNING RULE

> *"The test should isolate one unknown at a time. **Do not combine extension behavior, audio behavior,
> and cross-world transformation in one heroic soup.** If it fails, we need to know which gear stripped."*

🔴 **Moderation-refused jobs do not count as failed tests. Only accepted generations count.** With a ~50%
refusal rate that distinction is the difference between a real result and a phantom ***REMOVED***

---

## TEST 1 — THE SEAM TEST. Run this first.

**Why first: it can delete most of the twelve missing seam plates.**

Use the **W3 hotel → W4 car** seam. Franco's reasoning — it is the friendliest real seam in the reel:
same Paola · same agent wardrobe · a natural full-frame occluder (the muzzle flash) · a clear gesture
rhyme (two-handed pistol grip → two hands on the wheel) · and cold interior → hot daylight gives the
transition **an obvious success condition**.

**Attach only:** one Paola face authority · agent wardrobe · hotel corridor · generic sidearm · the W4
car-interior authority · **an exact 8-second audio excerpt crossing the world boundary, with the boundary
at 3.750s.**

⚠ **No start frame. No end frame. That is the entire point of the test.**

**The ask:** the transition happens **entirely inside a complete whiteout.** Before the whiteout only the
hotel world exists; after it clears only the car world exists. She is already driving at speed, same black
wardrobe, both hands on the wheel. No gun remains, no hotel remains.

> *"Do not burden this test with a detailed gunfight or driving maneuver. It has one job: **preserve Paola
> and the gesture while replacing world and prop inside a total occlusion.**"*

### Decision rule — generate the SAME prompt until two accepted results

| Outcome | Verdict |
|---|---|
| **Both succeed** | **schedule-grade** for occluded seams — remove those plate obligations |
| **Both fail the same structural way** | **kill it**, retain the seam plates |
| **One passes, one fails** | generate a third accepted result |
| 2 of 3 pass | viable for **selected** seams |
| 1 of 3 pass | technically possible, **not reliable enough** to remove plate obligations |

**Success requires ALL of:** identity holds · no visible morph seam · gesture rhyme survives · world and
prop fully replaced · grade lands correctly on each side.

---

## TEST 2 — DOES SD2 USE THE FIRST 8s OF A 15s AUDIO REF, OR COMPRESS ALL 15?

A **diagnostic** clip, not a reel shot. Attach the full 15-second audio built with three unmistakable
sections, and instruct:

> *during the slow low kicks, walk slowly; when the fast high claps begin, immediately switch to rapid
> footwork; when the sustained tone begins, freeze completely with both arms raised.* **No cuts, no other
> action.**

| Result | Meaning |
|---|---|
| slow walk → rapid movement, **no freeze** | SD2 is using approximately **the first 8 seconds** ✅ |
| slow, fast **and** freeze all inside 8s | it is **compressing / remapping** the full 15s structure ⚠ |
| one generic behaviour | inconclusive — retry once, then **inspect the returned audio itself** |

---

## TEST 3 — DOES AN EXTENSION INHERIT THE AUDIO CLOCK?

Extend the accepted Test-2 diagnostic **forward**, re-attaching the **same complete 15-second audio**, with
the same rule (slow on kicks, rapid on claps, frozen arms-up on the sustained tone).

If the extension continues into the *next* section of the audio, the clock is inherited and **feeding full
world audio every time beats pre-trimmed slices.** If it restarts at the beginning, pre-trimmed slices win
and my slicer stays the method.

---

## TEST 4 — EXTEND-BEFORE AS THE LEAD-IN

Generate a **backward** extension from an accepted skate clip. Four seconds if the interface allows,
otherwise eight, inspecting only the portion immediately before the source.

**The ask:** she is *already* rolling forward on the same board, same street, same speed and direction as
the source opening; camera already travelling the same path at the same height. **A stable approach only —
no trick, no push, no carve, no turn, no pose, no new action.** The final 1.875s must be a simple steady
roll flowing directly into the source's first frame.

**Pass criteria:** same direction and speed · same camera vector · no invented setup action · no second
board or body · no colour or face degradation · the final 1.875s is a usable lead-in · the join hides by
trimming no more than a few frames.

### 🔑 The production rule if it passes

> *"**Extend backward from a stable opening state, never from the exact onset of the hero action.**"*

Because if the source begins on an explosive action, the model **invents preparation** — a crouch before
the jump, a wind-up before the strike, a push before the skate motion, a turn before camera alignment.

> *"So it is not inherently better than designing the lead-in inside the original generation. It is better
> **only when the source's first frames already describe the stable state you want extended backward.**"*

---

## ON FULL-15s AUDIO — do not adopt before Test 2 passes

> *"My prior is that each generation treats an attached audio reference as **beginning at zero** unless the
> extension backend explicitly carries a time-offset token. **Video continuation does not automatically
> imply audio-clock continuation.**"*

He also flags a hybrid failure worth watching for: source video motion continues, source audio is preserved
*in the video*, but newly attached audio conditioning **restarts at zero** — which would look right and
drift wrong.

---

## OUR OWN PRIOR ADVANTAGE — the reason extensions may suit us better than most

Already recorded in `SD2_GUIDE_FINDINGS.md`:

> *"Extension joins jump. Fix in the edit: trim ~6 frames off the outgoing and 1 off the incoming.
> **Better — plan joins to land on our half-bar cuts, where a discontinuity is invisible by design. Our
> lattice already gives us those.**"*

**If extension joins jump, put the join on a musical beat**, where a jump reads as a cut rather than a
glitch. At 128 BPM there is a bar line every 1.875s. Most people extending clips have no grid to hide the
seam on; we built one for the music months ago.

⚠ **Syntax trap:** write **`Extend @Video 1`** — never *"reference"*, which reclassifies the job and breaks
the extend.
⚠ **Lock anatomy on a short clip BEFORE extending** (seedance skill) — so the order is short clean clip →
confirm hands and face survive → then extend. Never extend first.
