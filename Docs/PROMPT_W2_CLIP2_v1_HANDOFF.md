# W2 CLIP 2 — v1 "HANDOFF" (2026-08-05) — Franco-wargamed, converged

**TARGET MODEL: SEEDANCE 2.0 via Higgsfield. NOT Stable Diffusion.**

## ATTACH ORDER IS LOAD-BEARING — AND THE PLATE IS GONE
1. **Video 1** → `Assets/Video/W2_CLIP1TAIL_2s000.mp4` (48 frames / 2.000s / 4K, cut from the LOCKED
   7.500s clip-1 edit, not from the raw render — frame-exact, no rounding disagreement)
2. **Element** → `@Pao-Face-Bolly` (face only, order-independent)
3. **Audio** → `Assets/Music/AUDIO_CARRIERS/CANDIDATE_CARRIER_W2_CLIP2_V16_14637_8s.wav`

🔴 **NO PLATE.** Franco's jurisdiction correction: the W2 opening plate must STOP being the
exact-first-frame authority in clip 2. `@Video 1` takes over opening motion, body geometry, ensemble
positions, camera registration and continuing momentum. A plate would reconstruct moving fabric from a
still and reset dancer positions mid-phrase.

**CONTROLS:** 16:9 · 4K · 8s · audio ON · Unlimited ARMED · never Auto

---

## THE CARRIER BUG THIS VERSION FIXES

The pre-existing `CARRIER_W2_CLIP2_V16_14900_8s.wav` was cut for the **superseded 7.400 clip-1
lineage**. Locked clip 1 starts at source **7.137** and delivers 7.500s of picture, ending at
**14.637** — so the old carrier skipped **0.263s of music at the seam**.

All four carriers verified against the V16_BOLLY_a master by FFT cross-correlation (corr 0.988–1.000):
filenames truthful, only the pairing was stale. Corrected carrier cut and verified at source
**14.6370, corr 1.000**. Tool: `tools/w2_clip2_carrier_audit.py`.

**Consequence never propagated: the W3 handoff moves from source 22.400 → 22.137.**

## MEASURED MAP OF THE CORRECTED CARRIER (times relative to its own start)
- **Onsets (45):** 0.309 0.427 0.571 0.672 0.773 1.008 1.237 1.413 1.547 1.632 1.723 1.883 2.171
  2.533 2.640 2.875 3.104 3.467 3.573 3.813 3.920 4.037 4.149 4.293 4.400 4.507 4.741 4.971 5.131
  5.333 5.440 5.616 5.696 5.845 6.267 6.373 6.608 6.837 7.200 7.307 7.536 7.653 7.771 7.861 7.979
- **Low-band ACTIVE (drums/bass):** 0.34–0.68 · 4.10–4.44 · 5.21–5.46
- **Low-band QUIET:** 0.04–0.34 · 2.43–2.90 · 3.20–3.84 · 6.14–6.61 · 6.95–7.55
- **Two full-scale bass peaks: 2.22 and 7.81.** 7.81 is the W3 launch.

## THE CONVERGED BEAT MAP
| beat | window | job |
|---|---|---|
| 1 | 0.000–0.773 | turn handoff becomes the first single |
| 2 | 0.773–2.171 | hook return, reversed and wider — ONE complete variation |
| 3 | 2.171–3.813 | counter-rotating lane exchange |
| 4 | 3.813–4.507 | the build cuts the exchange into power shapes |
| 5 | 4.507–6.267 | hero version; **the W3 trajectory begins here** |
| 6 | 6.267–8.000 | enlarge and finish — never invent |

## WHAT THE WARGAME CHANGED (Franco conceded all four, improved two)

**1. Tail truncation — he conceded and diagnosed it deeper than I did.**
> "My draft treated almost every beat block as another complete SINGLE, SINGLE, DOUBLE, DOUBLE phrase.
> Clip 2 does not need six full hook repetitions."

Density cut per beat, and **the draw initiation moved into beat 5** so beat 6 only enlarges an
already-visible gesture: *"if the final 0.5–0.8 seconds truncate, the audience has already seen the
hand crossing the torso, the ensemble opening the lane and Paola turning into the new sightline. W3
can still complete the gesture."*

**2. The unseen threat — conceded, and he went further than my fix.** My replacement (the ensemble
peels open a corridor and she turns down the new sightline) accepted. He then **also removed the
finger closure from W2 entirely** — it is the part most likely to read as gripping the saree or
starting a weapon draw. W2 keeps fingers together, palm rotating inward, elbow leading behind the
wrist, hand still travelling past the waist at the cut. **W3 owns the closure and the grip.**

**3. Clip-1 edit — confirmed 0.000–7.500**, in-point immovable because the landing sits at 0.46. Tail
extracted from the exported locked edit, not the raw render, to avoid frame-rounding disagreement.

**4. Beat boundaries — he accepted five and beat one of mine with a better reason.** I proposed 3.467;
he rejected it because although it is a measured onset it sits inside the 3.20–3.84 low-band quiet, so
*"starting sharp power choreography there spends more than half a second performing the attack before
the music supplies it."* Moved to **3.813** — which lets the singles launch at 3.813 and ~4.037 and
puts the double burst inside the 4.10–4.44 low-band event.

**Also conceded by me:** my "1.5s blocks + audible anchoring" hypothesis for why the timecoded form
worked was overclaimed. His is better and falsifiable — **continuity topology: every block inherits
the previous block's body state, world and camera path instead of redefining a setup.** The law is not
"timecodes are safe," it is **"timecodes are safe when no block re-establishes anything."**

---

## THE PROMPT

One continuous 8-second take, real time, no internal cuts, no transitions, no dissolves. Normal speed
throughout — no slow motion, no ramping, no speed change.

Extend @Video 1. This shot begins on the exact frame @Video 1 ends on and continues its motion without
restarting. @Video 1 is the sole authority for the opening body geometry, the ensemble positions, the
camera registration and the momentum already in progress — the unfinished travelling turn, the skirt
still rotating, the dancers mid-phrase and the camera still retreating all continue without a reset and
without reconstructing the pose. The woman in crimson is Paola.

@Pao-Face-Bolly governs Paola's face and nothing else — it has no authority over her body, her costume,
the other dancers, or the location.

Every dancer visible at the end of @Video 1 is still present and still moving; no new person walks into
the shot at any point, and only one woman in crimson is ever in frame. A few onlookers remain on the
balcony railings above.

GEO SPATIAL LAYOUT (locked across every W2 shot — a spatial map only):
— One narrow bazaar corridor runs straight away from camera toward a bright opening at the far end.
— Spice sacks and brass tables sit along the left side of frame; textile stalls along the right side.
— The stone centre of the street is open ground with no stalls on it — this is where the dancing happens.
— Wooden balconies overhang both sides above the stalls.
— The sun sits low and centred in the far opening, behind the dancers and facing camera, so every shadow
  on the stone runs toward camera.
— The camera stays on the near side of the corridor for the whole shot and never travels around to the
  far side.

FRAME
The perspective, lens geometry, camera height and subject scale continue exactly from @Video 1. The
focal length never changes and the field of view never drifts — the only thing that changes is how far
the camera is from her. Paola stays large enough in frame that her feet and her hands are both clearly
readable for the whole shot. The stall lines, the overhead cloth lines and the lines of the stone paving
run to a single point at the far opening. Depth stays layered: cloth, dust and passing dancers move
close to camera in the foreground; Paola and the nearest dancers sharp in the middle distance; the
receding rows, the balconies and the sun behind her. Focus holds on Paola; close foreground bodies and
far rows fall soft.

CAMERA THROUGH-LINE
One unbroken handheld retreat continuing from @Video 1, carrying small operator drift and
micro-correction. It changes speed but never comes to a hard stop, never resets, and never begins a
second move. The retreat is restrained and never lets her get small. Per-beat camera behaviour is
specified in the beats below.

ACTION — SIX BEATS, ONE CONTINUOUS TAKE
The attached track is the only timing clock; the pulse is 128 beats per minute. Paola is in visible
motion in every single frame. Her arms and legs are one body: on every accent her step and her arm shape
arrive at the same instant, so her whole figure lands the shape together and reads as one clear
silhouette. Every hand shape appears as her hand travels through it and the next foot impulse
immediately pulls it onward — no hand parks, no body holds, nothing waits. Every beat begins from the
physical endpoint of the beat before it. The rhythmic signature stays SINGLE, SINGLE, DOUBLE, DOUBLE —
each single one springing step, each double two fast rebounds on the same foot, mirrored right then
left. The rhythm is the thing that repeats; the pathway through it is new every time.

0.000–0.773s · THE TURN HANDOFF BECOMES THE FIRST SINGLE
Action: The foot already travelling at the end of @Video 1 reaches the stone and redirects the remaining
rotational force forward-right. Her torso unwinds through front without pausing, the overhead arms
continue downward through the same circle, her left forearm passes across her sternum as her right hand
opens low, and her next foot is already leaving the ground before the turn has fully unwound. The
dancers around her complete their existing skirt turns and redirect into the same forward rhythm.
Camera: Continue the exact retreat and settling motion already in progress, preserving subject scale and
horizon. No opening reset and no new camera move.

0.773–2.171s · THE HOOK RETURNS, REVERSED AND WIDER
Action: Single right — her right foot springs laterally forward-right while her left forearm travels
from her sternum across her face into a high diagonal, rotating until the palm opens outward, her right
hand travelling low on the opposite diagonal. Single left — the same operation mirrored forward-left.
Double right — two fast rebounds carry her forward-right as both elbows pull in toward her ribs and the
forearms whip outward into unequal high and low lines, wrists rotating through the path. Double left —
the two rebounds mirrored, and the second launches her straight into the lane exchange. The near dancers
perform the same rhythmic code at different reaches, one starting from profile, one from three-quarter
and one from front, so the returning hook reads larger without copying the earlier silhouettes.
Camera: Retreating a fraction diagonally toward frame-left, holding Paola full-body while a near dancer
brushes the opposite frame edge.

2.171–3.813s · THE COUNTER-ROTATING LANE EXCHANGE
Action: Paola advances through two springing quarter-turn steps. On the first, her right foot crosses
forward-left and her torso rotates with it while her opposite arm sweeps horizontally across her body
and curves overhead. On the second, her left foot opens forward-right and unwinds her through centre
into the mirrored pathway, wrists circling continuously and her hips redirecting with each foot. At the
same time the frame-left dancers travel behind her toward frame-right in a shallow arc while the
frame-right dancers travel behind her toward frame-left, passing through different depths rather than
one flat line, and nobody crosses directly over her face.
Camera: Threading backward between the moving lanes. One dancer passes close across frame-left and then
clears, producing real parallax; the camera yields slightly but continues the same retreat.

3.813–4.507s · THE BUILD CUTS THE EXCHANGE INTO POWER SHAPES
Action: Single right — her right foot presses outward and rebounds, her right hip travels toward that
foot, her ribcage redirects left and her opposite shoulder gives one compact hit while her left wrist
rotates open at shoulder height. Single left — the entire operation mirrored. Then one fast double burst
— two rapid side-steps that stamp and rebound, each driving hip and opposite ribcage in different
directions while her left arm grows from a wrist snap into a complete overhead throw. The crossing
dancers arrive in their exchanged lanes on those same accents, and the very next foot impulse removes
every shape and continues the dance — nobody holds anything.
Camera: Slowing almost to Paola's speed and taking one short physical jolt on each stamp. It does not
lock.

4.507–6.267s · THE HERO VERSION, FULL BODY ACROSS THREE PLANES
Action: Single right — she drives her right knee diagonally across her body while her left elbow pulls
down toward it and her torso contracts around the diagonal; her right foot lands forward and her torso
unfurls immediately. Single left — the knee, elbow and unfolding pathway mirrored. Then one travelling
double — two quick cross-steps carrying her forward while her arms travel from low crossed lines through
rotating wrists into a broad open frame. During that double, her right hand begins a long diagonal
descent from her opposite shoulder across her chest, fingers together and the palm rotating inward, the
elbow leading behind the wrist. The near dancers complete broad half-turns in their new lanes, the
middle rows travel laterally at smaller scale and the far rows drive straight forward, so all three
planes stay active while Paola performs the largest and clearest operation.
Camera: Resuming the retreat and rising only slightly — enough to show the formation expanding without
shrinking Paola. Moving bodies repeatedly break the centred sun into brief flares.

6.267–8.000s · THE DANCE BECOMES THE DRAW
Action: The ensemble peels outward into two moving wings and opens a clear diagonal corridor toward
camera-right. Paola steps diagonally toward camera on her right foot, her right shoulder pulling back
while her left arm slices upward and outward into that opening space. Her left foot crosses through and
rotates her torso a quarter toward the newly exposed corridor, her head and sternum turning down that
sightline. Through two forward rebounds her right hand continues the descent it began in the previous
beat, travelling lower past her waist with the fingers together, the palm still rotating inward and the
elbow still leading behind the wrist. Two final rebounds carry her closer and enlarge the same
movement — the arm travelling further, the torso rotating further, the wings opening wider. The clip
cuts while her hand is still crossing the hip line, her torso is still rotating and her next foot is
already leaving the st***REMOVED***
Camera: Holding her scale by retreating with the final rebounds. Her arm crosses the centred sun and
throws a warm flare at the cut. The camera is still physically in motion when the clip ends.

Paola starts every new movement first and performs the largest, clearest version of it — her steps
travel further and her arms reach wider than anyone else's in frame. The other dancers share her rhythm
with visible differences in step length, elbow height, rotation and recovery. They are visibly working:
chests rising, loose strands of hair stuck to damp temples, skirts swinging with real weight. Above them
the onlookers lean on the balcony railings and watch her.

WORLD
The street moves with the dancing: the saffron and orange cloth strung overhead lifts and swings as
bodies pass under it, the brass and copper on the stalls flares as figures cross the light, the cloth on
the tables stirs in the moving air, and every time a dancer crosses in front of the sun it breaks into a
brief flare that washes across the frame — so the light pulses in time with the dance.

ACTING
Paola dances with easy command: chin level, faintly amused, the look of someone who knows the street is
hers. Nothing about it looks strained, even when the movement is big. She never performs toward the
camera and never plays coy, and her eyes stay level and forward, never on the lens. Each of the other
dancers wears her own expression; none of them copy Paola's face.

PHYSICS
Real weight throughout: the balls of her feet meet the stone and push off it, her weight rebounding
upward out of every landing. Her skirt and dupatta trail a moment behind every movement and snap out on
every sharp ***REMOVED*** Her anklets swing with real weight and catch the light as they ring. Dust lifts wherever
feet strike the stone and hangs glowing in the raking sunlight.

LIGHT
The sun sits behind the dancers and rims every figure from behind. The only fill is soft cool bounce from
the open sky, sitting against that warm rim so every body carries a warm edge and a cool shadow side.
Exposure is set for the bright sky, so faces sit two to three exposure stops below it and are lifted only
by warm bounce coming off the sunlit stone, and the stalls fall darker still while keeping texture inside
their highlights. The hanging dust makes the sunlight arrive in visible beams between the bodies. The
rows furthest from camera read lighter and lower in contrast than the near ones. No frontal key light and
no beauty fill. The sky in the far opening stays exactly the colour it already is in @Video 1.

COLOUR
The frame is mostly warm sandstone and ochre, with deep indigo and teal running through the other
dancers' costumes; Paola's crimson is the only strong red anywhere in the shot, so she is the single
accent in the frame. Saturation is rich and comes from the objects themselves, and the blacks are deep
but still hold detail. This is colour negative shot into the sun: highlights roll off gently instead of
clipping, the bright opening blooms and keeps a soft edge, and warm halation glows around every rim-lit
shoulder, hairline, dust mote and brass surface. A faint cool cast sits in the shadows of the figures and
stalls against those warm highlights — the overall colour of the scene stays as it is in @Video 1. Skin
carries real tonal variation, warm brown and olive with a natural flush at the cheeks and a light sheen
of sweat catching the rim light; no two areas of a face sit at the same value.

AUDIO
The attached track is the only music, and no music is added to it. No dialogue and no singing. Any sound
from feet, anklets, fabric or the street sits quietly underneath the track.

FINAL FRAME
No on-screen text anywhere in frame — no lettering, no signage, no logos, no captions, no overlays.

CAPTURE
A big-budget Indian film dance sequence, photographed on real film. Wide-latitude colour negative with a
Kodak Vision3 250D rendition, 24 frames per second at a 1/48-second exposure, so every fast limb and
every flare of fabric carries real photographic motion blur. Fine 35mm grain in the midtones, heavier in
the shadows, gone in the highlights. Preserve the flare, the bokeh and the optical character already
present in @Video 1, with slight softness and gentle colour fringing toward the frame edges.
Photographed, not generated — real people dancing in a real street, with no CGI, no game-engine look, no
frame interpolation, no plastic skin and no frozen posing.

---

## WHAT TO JUDGE
1. **Does frame one continue the turn**, or does it reset / rebuild the pose? That is the whole
   extend-vs-plate bet.
2. **Does the tail survive to 8.000s?** Density was cut specifically to protect it. If it truncates,
   the trajectory still started in beat 5, so check whether the hand-across-torso is visible before the loss.
3. **The lane exchange at 2.171–3.813** — do the two groups actually swap sides through different
   depths, or does it flatten into one line?
4. **Does anything read as a weapon or as skirt-gathering** in the final beat? Finger closure was
   deliberately withheld for W3.
5. Any clapping. Any sky colour shift. Any frozen ensemble.
