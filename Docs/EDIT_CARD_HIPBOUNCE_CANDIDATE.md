# VIDEO_EDIT CARD — HIPBOUNCE EDIT CANDIDATE (2026-08-07)

**Source:** the 8.04s full-phrase take (`Inspiration/hip-bounce vid edit.mp4`, Drive copy
`EDIT_CANDIDATE_FULLPHRASE_8s.mp4`). Worth salvaging because it already has: full-body framing,
Paola identity + saree, and the **staggered plant with the rear heel on the ball** — Nelson's look.

**Registry facts:** SD2.5 `video_edit` edits one source video, **keeps the source's duration**
(duration/aspect settings ignored), and per ByteDance can modify **actions and storylines**, not just
repaint appearance. So the landing pause can plausibly become moving hip-bounce frames inside the same
8.04s. What is NOT guaranteed: re-timing the whole take to a new musical grid — global beat correction
is experimental.

**Franco's protocol — two PARALLEL diagnostics from the ORIGINAL source, never sequential** (a
sequential chain can't attribute drift). Edit A is the existential one: if edit can't rewrite the
pause, the candidate is dead and arm-polish would be wasted.

## FIRE ORDER (Franco's strategic call — run both lanes at once)
1. **Fire 1 — Asset A v15 refire**, audio OFF (tests whether the leg-pump was prompt hierarchy vs audio confound)
2. **Fire 2 — Edit A below** on the candidate, audio OFF
3. Whichever lane first gives correct isolation + correct 128-BPM timing becomes the foundry winner.
4. Edit B (arm) fires only after Edit A proves the tool; if both pass separately, one combined edit from the original.

## CONTROLS — both edits
| control | value |
|---|---|
| model | **Seedance 2.5** |
| mode | **video_edit** |
| source | the ORIGINAL untouched candidate clip |
| audio attach | **`CARRIER_W2_CLIP2_V4GUITAR_8000_8s.wav`** |
| generate_audio | **OFF** (measured law — see Asset B v16 doc) |
| duration | inherited from source (8.04s) — do not set |
| Unlimited | **ON** |

---

## EDIT A — LANDING HIPBOUNCE ONLY

**ATTEMPT 1 (2026-08-07): NULL — returned the source unchanged.** Two confounds, so not a clean kill:
(1) the instruction was preservation-dominant — output=input scored perfectly against most of the text;
(2) Franco checked the Higgsfield history: the edit job ran `generate_audio: true`.
**Franco: "Retry once."** Text is the only strength lever — the registry exposes no edit-strength /
denoise / adherence control. If the change-dominant retry is also null, temporal motion replacement is
declared unreliable for this pipeline: choreography goes to the regeneration lane (v15-A + v16-B),
edit reserved for local spatial changes (arm, hand shape, expression, wardrobe fabric).

### RETRY INSTRUCTION (change-dominant — Franco's wording; audio OFF this time)

```
CHANGE THE MOTION AFTER THE PLANT. Beginning on the first frame where her left foot contacts the floor in the staggered stance, replace the existing pause and settling motion with continuous hip-bouncing. The landing itself is the first bounce accent: she lands and immediately bounces, with no held pose, no settle and no dead frames after contact.

From that landing through the end of the video, her hips and seat perform one fast complete UP-DOWN bounce on every beat of the attached carrier. Each full UP-DOWN cycle finishes inside one beat and the next begins immediately. The hip-bouncing never pauses.

Keep the existing staggered stance: the left front foot stays planted and weight-bearing, the right rear foot stays behind on the ball with the heel lifted. The right rear forefoot gives only a small elastic response to the seat bounce, never a large calf raise, marching motion or stepping pattern.

This edit must visibly replace the source video's post-landing pause with uninterrupted beat-locked hip-bouncing. Keep her identity, face, saree, framing, camera and background unchanged.
```

### ATTEMPT-1 INSTRUCTION (preservation-dominant — kept for lineage, do not reuse)

```
Preserve the existing performer, identity, saree, framing, camera, and all body motion exactly as they are. Change only the planted section. When the left foot lands into the existing staggered stance, there is no pause, settle or held pose — the landing itself immediately becomes the first seat bounce. Keep the left front foot fixed and weight-bearing; keep the right rear foot fixed behind on the ball with the heel lifted. From that landing onward, her hips and seat perform one fast complete UP-DOWN bounce on every beat of the attached carrier. The rear forefoot responds only as a small elastic spring — no stepping, no calf-raise pumping, no whole-body bobbing. Preserve everything else unchanged.
```

## EDIT B — ARM ONLY (hold until Edit A passes)

```
Preserve the entire source video exactly, including timing, body motion, legs, framing, camera, identity, saree and background. Change only the right arm. Replace the rigid held arm with a loose feminine high-diagonal arm response: the arm stays long up-and-back behind her body, elbow soft and nearly straight, wrist relaxed, fingers softly gathered. Each seat bounce carries the arm a small distance farther back-and-up, then it rebounds softly forward-and-down. The hips drive the arm — the arm never pumps, flaps, swings wide or becomes a separate dance move.
```

## PASS GATE
The edit-candidate lane is only promoted to motion authority if the result passes **movement timing**
(one complete bounce per 0.469s beat from the landing onward), not just the visual fix. An off-beat
motion source poisons every downstream 2.0 transfer.

## SYNC-CHECK WORKFLOW (replaces audio ON)
Every silent output → Pablo muxes the true carrier under it:
`ffmpeg -i render.mp4 -i CARRIER_W2_CLIP2_V4GUITAR_8000_8s.wav -map 0:v -map 1:a -c:v copy -shortest render_SYNCCHECK.mp4`
Nelson ear-checks against the real 128-BPM clock — same verification, zero generation contamination,
no invented foley muddying the beat.
