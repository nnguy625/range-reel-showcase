# W2 CLIP 2 — COMBINED MOTION REFERENCE (both approved hip-bounces, one phrase)

**Built 2026-08-09** from Nelson's two approved foundry assets. Both banked in Drive:
`APPROVED_W2_HIPBOUNCE_LIFT_A2.mp4` (leg lift) · `APPROVED_W2_HIPBOUNCE_PLANTED_A1.mp4` (planted).

## THE MEASUREMENT THAT SHAPED THE BUILD

Tracked the vertical centroid of the saree mass per frame (position tracking — the actual bounce
waveform; my first pass used a fixed crop that caught the wrong body part on one clip and reported
the two backwards, and a motion-energy pass was ambiguous at the tempo octave):

| clip | bounce period | rate | vs 128 BPM (0.469s) |
|---|---|---|---|
| leg lift (A2) | 0.542s | 111/min | **15% SLOW** |
| planted (A1) | 0.458s | 131/min | **on beat** |

So the planted take was already locked; the leg-lift take — approved on look — still ran slow.
Fix: retime A by **×0.8654** (video only, no reframe, no crop, no look change) → 0.458s period.
Both halves re-verified inside the finished file: **0.458s = 131/min, on beat.**

## THE SPLICE

Searched every (A-end, B-start) pair that totals exactly 180 frames, scoring value + slope mismatch
of the bounce waveform at the seam, and took the minimum:

```
retimed A frames 0–82   (83 fr = 3.458s)
planted B frames 0–96   (97 fr = 4.042s)
                        ---------------
                        180 fr = 7.500000s exact = 16 beats at 128 BPM
```

## FILES
| file | use |
|---|---|
| `Assets/Video/MOTION_REFS/MOTIONREF_W2CLIP2_PHRASE_BEATLOCK_7s500.mp4` | **recommended** — 1280×720, 180 fr, 7.500000s, silent, both halves on beat |
| `Assets/Video/MOTION_REFS/MOTIONREF_W2CLIP2_PHRASE_NATIVE_8s08.mp4` | straight concat at native speeds (8.083s) — lineage / A-B compare |

Drive copy of the beat-locked file is in `SD2 DRAFT/`.

## ⚠ KNOWN DEFECT — THE SEAM IS A VISIBLE HARD CUT
Frame-checked frames 77–88: at the join the pallu drape position, the arm arrangement and the stance
all change discontinuously. Unavoidable — the halves are two independent generations. Two consequences
to decide before firing:
1. It may teach SD2 to **cut** mid-shot, which breaks the continuous-take contract. Mitigation is a
   prompt line: the reference is two moves shown in sequence; perform them as ONE continuous phrase,
   no cut, no jump, with a smooth transition invented between them.
2. The reference does not show the **transition itself** — the plant. SD2 must invent the handoff from
   lifted-leg to planted stance. That is the one beat no approved footage covers.

Open with Franco: whether to ship the seam as-is with the prompt guard, or hold and generate a
dedicated transition asset first.
