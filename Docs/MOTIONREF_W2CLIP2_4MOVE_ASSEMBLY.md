# W2 CLIP 2 — FOUR-MOVE MOTION REFERENCE (Franco's cut list, executed)

**Built 2026-08-09.** Nelson: *"when I say assemble, i meant the arm swing + leg lift hip-bounce + plant leg
hip-bounce + punjab pump. Talk to Franco... have him assemble them."* Franco reviewed the four full
uncut sources in Drive and returned the cut list below; I executed it frame-exactly.

**File:** `Assets/Video/MOTION_REFS/W2CLIP2_MOTIONREF_4MOVE_7s500.mp4`
1280×720 · 24fps · **180 frames · 7.500000s** · silent · Drive copy in `SD2 DRAFT/`

## THE CUT LIST — 4 / 4 / 4 / 4 beats, one bar per move

| # | move | source | IN | OUT | src frames | out frames |
|---|---|---|---|---|---|---|
| 1 | arm swing | `armswing.mp4` (4K, 8.042s) | 0.500s | 2.375s | f12–f56 | 45 = 1.875s |
| 2 | leg-lift hip-bounce | `leg lift hip-bounce approve.mp4` | 0.917s | 3.083s | f22–f73 | 45 = 1.875s **(retimed ×0.8654)** |
| 3 | planted hip-bounce | `hip-bounce planted leg approve.mp4` | 0.000s | 1.875s | f0–f44 | 45 = 1.875s |
| 4 | punjab pump | `punjab pump.mp4` (4K, 8.042s) | 2.667s | 4.542s | f64–f108 | 45 = 1.875s |

**Franco's reasoning:** move 1 stays in the cleaner early full-body material before it drifts toward the
close-framed back-turn; move 2 is the smoothest middle stretch (not the opening, not the late part);
move 3 deliberately keeps **Nelson's liked opening** — neutral start, side step, entry into the
staggered hip-bounce; move 4 is the best travelling section, readable and advancing toward camera.

**Retime ruling:** he took the leg-lift retime — *"the leg-lift section is the only one visibly slow
enough to contaminate the phrase clock."* 2.166s of source × 0.8654 = 1.875s = exactly 4 beats.

**Seams:** hard cuts only, no dissolves — *"a dissolve teaches smear, not choreography."*

## VERIFIED AFTER BUILD
Per-bar bounce period (saree vertical-centroid tracking):

| bar | measured | note |
|---|---|---|
| 2 leg-lift | **0.458s = 131/min** | on beat — retime landed |
| 3 planted | **0.458s = 131/min** | on beat |
| 1 arm swing / 4 punjab | 0.208s | **metric not meaningful** — this tracks hip bounce; neither move is a hip bounce, so treat these as unmeasured, not as a tempo reading |

Target 0.469s / 128 BPM. The two bars where bounce tempo matters are both locked.

## SEAM GUARD — put this in the generation prompt (Franco's wording)

```
The motion reference contains four editorially cut excerpts used only to show the move sequence. Do not reproduce the cuts, jumps, resets, or scene discontinuities. Perform the four phrases as one continuous dance, inventing smooth natural transitions between them in a single uninterrupted take.

The move order is fixed: arm swing, leg-lift hip-bounce, planted hip-bounce, then traveling Punjabi pump.

The reference's cuts are not events in the generated shot.
```

## ⚠ OPEN — THIS ASSEMBLY IS DANCE-ONLY
Nelson also requires the shot to carry **her close-up** (the identity beat) and a **pass through the
drapes** (W3 opens inside crimson moving fabric). Franco's 4×4×4×4 fills all 16 beats with dance,
leaving zero beats for either. That allocation question went back to him: drop or shorten a move,
overlap the close-up with a dance move (camera pushes in *while* she hip-bounces — buys the beat free),
let the drape eat the final bar, or make the case that this is what the expiring 15-second window is
for. **Awaiting his ruling; this file may need re-cutting once it lands.**

Also note: mixed provenance is visible — bars 1 and 4 are market-street 4K, bars 2 and 3 are gray
studio. For a motion reference that is acceptable (movement vocabulary only), but the generation
prompt must own the setting so the studio bars do not pull the render out of the market.


---

## R2 — RESTITCH WITH THE FINAL APPROVED LEG LIFT (2026-08-09, FIRED LANE)

**File:** `Assets/Video/MOTION_REFS/W2CLIP2_MOTIONREF_4MOVE_R2_7s500.mp4` — 180 fr / 7.500000s exact.
Drive: [asset link removed from public mirror]

Franco re-picked after the new leg-lift approval (short-form list after his long stream wedged):
| bar | source | window | note |
|---|---|---|---|
| 1 | armswing.mp4 | 0.500–2.375s (f12–f56) | unchanged |
| 2 | **leg lift hip-bounce approve final.mp4** | **0.500–2.375s (f12–f56)** | NEW take, NO retime — native 131/min |
| 3 | hip-bounce planted leg approve.mp4 | 0.000–1.875s (f0–f44) | unchanged (neutral+sidestep open) |
| 4 | punjab pump.mp4 | 2.667–4.542s (f64–f108) | unchanged |

Verified in the finished file: bar 2 = 0.458s/131 per min, bar 3 = 0.458s/131 per min — both ON BEAT,
zero retimes anywhere in the assembly.

**Close-up + drape RULING (Franco):** the reference stays dance-only 4/4/4/4. In the GENERATION
prompt: the close-up develops during the Punjab phrase, and its final beat resolves directly into the
turn / pallu-drape exit. Camera language owns both; the motion ref owns only the moves.
