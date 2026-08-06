# W2 CLIP 2 — v2 "DRAPES" (2026-08-06) — Franco's 15-beat design, frame-corrected

**TARGET MODEL: SEEDANCE 2.0 via Higgsfield. NOT Stable Diffusion.**

Supersedes `PROMPT_W2_CLIP2_v1_HANDOFF.md`, which was built on the V16_BOLLY_a carrier and on a
7.500 + 7.500 split. Both are dead. v1 stays on disk.

## ATTACH ORDER

1. **Video 1** → `Assets/Video/W2_CLIP1_A16_EDIT_191f.mp4` (191 frames / 7.958333s / 3840x2160)
2. **Element** → `@Pao-Face-Bolly` (order-independent)
3. **Audio** → `Assets/Music/AUDIO_CARRIERS/CARRIER_W2_CLIP2_NELSONPICK_22063_8s.wav`

**CONTROLS:** 16:9 · 4K · 8s · audio ON · Unlimited ARMED · never Auto

## THE EDITORIAL MATH

Franco: *"use A-16 trimmed to 7.969s… an exact 17-beat first clip + 15-beat second clip = 32 beats
= 15.000s at 128 BPM."*

32 beats = 15.000000s = **360 frames at 24fps — exact.** But 17 beats = 191.25 frames and 15 beats =
168.75 frames — **neither is an integer frame.** Closest legal integer split:

| | frames | seconds | error vs Franco's beat mark |
|---|---|---|---|
| clip 1 | **191** | 7.958333 | −10.4 ms |
| clip 2 | **169** | 7.041667 | — |
| **W2** | **360** | **15.000000** | exact |

So clip 2's music starts at source **14.105 + 7.958333 = 22.063333**, not 21.605.

## MEASURED — the carrier at 22.063333, per beat

| beat | window | mid 200–2k | low 30–160 |
|---|---|---|---|
| 1 | 0.000–0.469 | 0.27 | 0.30 |
| 2 | 0.469–0.938 | 0.20 | 0.43 |
| 3 | 0.938–1.406 | 0.27 | 0.22 |
| 4 | 1.406–1.875 | 0.20 | 0.40 |
| 5 | 1.875–2.344 | 0.25 | 0.19 |
| 6 | 2.344–2.813 | 0.17 | 0.42 |
| 7 | 2.813–3.281 | 0.28 | **0.11** |
| 8 | 3.281–3.750 | 0.16 | 0.39 |
| 9 | 3.750–4.219 | 0.21 | 0.36 |
| 10 | 4.219–4.688 | 0.20 | 0.39 |
| 11 | 4.688–5.156 | 0.25 | 0.28 |
| 12 | 5.156–5.625 | 0.21 | 0.29 |
| 13 | 5.625–6.094 | 0.23 | 0.35 |
| 14 | 6.094–6.563 | 0.20 | 0.34 |
| 15 | 6.563–7.031 | 0.34 | **0.01** |
| 16 | 7.031–7.500 | 0.48 | **0.00** |

Only sustained pitched run in the whole window: **6.700–7.000s, 290 Hz, sharp 37.1.**

🟢 **The bass strips out on beat 15 — exactly the beat she goes through the drapes.** The bed empties
as the cloth fills the frame and W3 drops into the hole. Franco landed the DJ shape without seeing
these numbers.

🔴 **Franco's face-passage motivation is not in this music.** He wrote *"SOFT GUITAR ENTERS"* at beat
9 and had it grow through beat 13. Measured, mid band is flat at 0.20–0.25 across beats 9–13 and the
low band stays at 0.28–0.39 — the drums never let go. The one mid-clip opening is **beat 7 (low 0.11)**,
one beat wide. The face passage as written rides over a full drum bed. Open question for Nelson: does
it need musical air, or does it play over the groove?

🔴 **A-16 carries no carrier we hold.** Cross-correlation of A-16's audio, control = A-15 (known
carrier fire):

| clip | vs NELSONPICK 14105 | vs V16 7137 | vs V16 7400 |
|---|---|---|---|
| **A-15** (control) | 0.078 | **0.916** | **0.917** |
| **A-16** | 0.109 | 0.254 | 0.254 |

A real match reads ≈0.92 through SD2's re-encode. A-16 reads 0.25 against everything. Measured only —
whether that matters is Nelson's call.

## WHAT I COMPRESSED AND WHY

15 beats is roughly double v1's 6. To protect the tail — the drape burst IS the W3 handoff and cannot
truncate — WORLD, LIGHT, COLOUR and CAPTURE are cut to short continuity lines pointing at `@Video 1`,
which already owns all of them in an extend (P4). The beats got the words instead.

---

## THE PROMPT

One continuous 8-second take, real time, no internal cuts, no transitions, no dissolves. Normal speed
throughout — no slow motion, no ramping, no speed change.

Extend @Video 1. This shot begins on the exact frame @Video 1 ends on and continues its motion without
restarting. @Video 1 is the sole authority for the opening body position, the costume, the ensemble
positions, the market geometry, the light, the colour, the camera height and the momentum already in
progress — the step already travelling, the red fabric already moving from her left arm, the dancers
mid-phrase and the camera still retreating all continue without a reset and without rebuilding the pose.
The woman in crimson is Paola.

@Pao-Face-Bolly governs Paola's face and nothing else — it has no authority over her body, her costume,
the other dancers, or the location.

Every dancer visible at the end of @Video 1 is still present and still moving; no new person walks into
the shot at any point, and only one woman in crimson is ever in frame.

HAND SHAPES — named once here, referenced by name in the beats:
— FLAT PALM: four fingers straight and pressed together, thumb bent inward, palm turned outward.
— PINCH: middle fingertip meeting the thumb, index curled inward, ring and little fingers lifted apart.
— OPEN FAN: all five fingers separating, radiating outward, curving gently back.
— BLADE: fingers together, palm vertical, wrist straight.
Every shape appears while the hand is still travelling and the next foot impulse pulls it onward. No hand
parks. No body holds.

GEO SPATIAL LAYOUT (locked across every W2 shot — a spatial map only):
— One narrow bazaar corridor runs straight away from camera toward a bright opening at the far end.
— Spice sacks and brass tables sit along the left side of frame; textile stalls along the right side.
— The stone centre of the street is open ground with no stalls on it — this is where the dancing happens.
— Hanging saffron market drapes close the corridor at frame-right, near enough to reach.
— Wooden balconies overhang both sides above the stalls.
— The sun sits low and centred in the far opening, behind the dancers and facing camera.
— The camera stays on the near side of the corridor for the whole shot.

FRAME
The perspective, lens geometry, camera height and focal length continue exactly from @Video 1 and never
change — the only thing that changes is how far the camera is from her. Paola stays large enough that her
feet and her hands are both readable until the framing closes on her, and her face is never crossed by a
passing body. Depth stays layered: cloth, dust and passing dancers close to camera; Paola and the nearest
dancers sharp in the middle distance; the receding rows, the balconies and the sun behind her.

CAMERA THROUGH-LINE
One unbroken handheld retreat continuing from @Video 1, carrying small operator drift and micro-correction.
It never comes to a hard stop, never resets and never begins a second move. It slows enough that Paola
grows toward camera on her own travel, then yields toward frame-left as she crosses right, then follows
her into the drapes. Distance is the only variable. Per-beat behaviour is in the beats below.

ACTION — FIFTEEN BEATS, ONE CONTINUOUS TAKE
The attached track is the only timing clock; the pulse is 128 beats per minute, one beat every 0.469
seconds. Every beat begins from the physical endpoint of the beat before it. Paola is in visible motion in
every frame until the cloth covers the lens. Her feet, hips, torso, arms and hands arrive on each accent
together, so her whole figure reads as one silhouette.

0.000–0.469s · BEAT 1 — CONTINUE THE SWEEP, SINGLE RIGHT
Action: Her weight stays over the planted left leg exactly as inherited. Her already-free right foot springs
diagonally forward-right. The left arm and the red fabric continue their travel toward frame-right and then
arc downward across the front of her torso instead of resetting. Her right hand rises from the low right hip
to a high diagonal beside her head through FLAT PALM. Foot and hand land the accent together; the ankle
rebounds at once.
Ensemble: the nearest dancers take the same rightward spring at smaller reach, each keeping her own elbow
height and step length.
Camera: continue the exact retreat inherited from @Video 1, preserving her scale and the horizon.

0.469–0.938s · BEAT 2 — MIRROR, SINGLE LEFT
Action: Weight transfers onto the right foot and the left foot springs diagonally forward-left. The right arm
continues over its high point and starts down; the left hand rebounds from the opposite hip across the torso
into a high-left diagonal. The torso rotates toward the stepping leg while the ribcage redirects the other
way. The left palm opens to the light on the instant the foot lands.
Ensemble: all dancers mirror left on the same accent with small natural differences in rotation.
Camera: the same retreat continues; no change of setup.

0.938–1.406s · BEAT 3 — DOUBLE RIGHT, CHEST THEN SHOULDER
Action, first rebound: her right foot rebounds and drives the chest forward once while both elbows pull in
toward her ribs; the left hand descends toward the sternum and the right forearm whips outward.
Action, second rebound: the right foot rebounds again; the left shoulder hits forward as the chest releases
and the right wrist rolls through OPEN FAN, the hand travelling on through it.
Ensemble: near dancers take the same two accents a fraction behind her; middle rows use smaller chest and
shoulder range.
Camera: one soft operator jolt follows the two rebounds.

1.406–1.875s · BEAT 4 — DOUBLE LEFT, MIRROR AND LAUNCH
Action, first rebound: two left-foot rebounds mirror the previous beat; the first drives the chest forward
while both forearms cross low in front of the waist.
Action, second rebound: the left shoulder strikes forward and both forearms whip apart into unequal high and
low diagonals, wrists rotating throughout. The second rebound sends her straight into the next right-leg
pathway.
Ensemble: the whole group completes the mirrored double and immediately continues — nobody arrives in a
tableau.
Camera: the retreat continues while she gains a little screen size.

1.875–2.344s · BEAT 5 — KNEE-ELBOW CROSS, SINGLE RIGHT
Action: She drives her right knee diagonally across her body while her left elbow pulls down toward it and her
torso contracts around the diagonal. Her left hand passes near the shoulder through PINCH. Her right foot then
lands forward-right and the torso opens immediately, releasing the elbow away from the knee.
Ensemble: frame-left dancers perform the same diagonal cross; frame-right dancers prepare the mirrored answer.
Camera: keep retreating down the centre lane.

2.344–2.813s · BEAT 6 — KNEE-ELBOW CROSS, SINGLE LEFT
Action: Her left knee drives diagonally upward while her right elbow pulls toward it; her right hand passes
through the mirrored PINCH. Her left foot lands forward-left, the chest opens, the shoulders separate and the
skirt keeps swinging from the previous step.
Ensemble: all dancers complete the mirrored cross, each at a slightly different knee height.
Camera: she stays full-body and centred.

2.813–3.281s · BEAT 7 — DOUBLE RIGHT, HEEL-TOE AND THE EXCHANGE BEGINS
Action, first rebound: her right heel swivels outward while her left foot slides a fraction forward; her hips
rotate with the heel and the opposite shoulder counters. Her left arm circles up from waist level.
Action, second rebound: the feet switch quickly, her right foot travels forward-right and both arms expand
into a broad diagonal, one overhead and one lateral, wrists still rotating.
Ensemble: frame-left dancers start travelling behind her toward frame-right through the middle-depth lane;
frame-right dancers take the opposite route through the far lane.
Camera: the retreat angles a fraction toward frame-left so the crossing bodies make parallax without covering
her.

3.281–3.750s · BEAT 8 — DOUBLE LEFT, COMPLETE THE EXCHANGE
Action, first rebound: her left heel swivels outward while her right foot glides forward; her torso
quarter-turns toward screen-left and her right arm circles overhead.
Action, second rebound: her left foot travels forward-left, her torso returns through front and both hands open
into opposing diagonals. She finishes facing forward, still advancing.
Ensemble: both groups pass behind her and arrive in exchanged lanes, staying clear of her silhouette.
Camera: slow the retreat slightly; she begins closing the distance to the lens.

3.750–4.219s · BEAT 9 — THE FACE FRAME, SINGLE RIGHT
Action: Her right foot crosses lightly forward-right. Her left hand starts at the right hip and travels slowly
across the waist, ribs and collarbone toward her left cheek, the wrist rotating the whole way, arriving near
the cheek through PINCH. Her right hand stays low and open near her waist. Her hips and ribcage keep a small
counter-rotation running underneath the hand path.
Expression: her smile narrows into cool, lightly amused control; her gaze stays just past the lens.
Ensemble: the dancers keep the springing base rhythm behind her at smaller arm reach.
Camera: the same retreat, slowed enough that she grows from full-body into a moving medium shot on her own
travel.

4.219–4.688s · BEAT 10 — MIRRORED FACE FRAME, SINGLE LEFT
Action: Her left foot crosses forward-left. Her right hand mirrors the path from the left hip through waist,
ribs and collarbone toward her right cheek, while her left hand descends from the face through a rotating wrist
and opens low. Her hips travel with the stepping foot and her shoulders counter, keeping the whole body active.
Expression: her chin turns a fraction after the hand arrives — a delayed finish that never stops the step.
Ensemble: a near dancer passes softly through the frame edge, giving foreground motion while her face stays
unobscured.
Camera: she closes into a chest-up three-quarter view; the camera never locks.

4.688–5.156s · BEAT 11 — RISING BODY WAVE, DOUBLE RIGHT
Action, first rebound: her right foot rebounds under her; her hips tucks forward and her lower stomach
contracts while both hands begin low beside her hips.
Action, second rebound: the same impulse rises through her lower ribs, sternum and shoulders. Her sternum
travels slightly past the supporting foot while both hands trace upward from hips toward ribs, wrists turning.
Before she can appear to fall, her free foot reaches forward and catches her weight.
Expression: composed and confident as her upper body arrives closest to camera.
Ensemble: dancers keep travelling behind her, their larger skirt motion making a moving background.
Camera: the closest point — a moving chest-up hero frame, the centred backlight outlining her bun, her flower
and her glasses.

5.156–5.625s · BEAT 12 — RELEASE AND TURN, DOUBLE LEFT
Action, first rebound: her left foot catches the body wave and rebounds; her left hip redirects outward while
her ribcage snaps the other way and her right shoulder answers.
Action, second rebound: her left foot presses again and rotates her a quarter-turn toward frame-right. Her right
arm sweeps from beside her face across her chest into a forward-right diagonal while her left arm opens behind
her, pulling the red fabric into a long trailing line. The close framing converts into travel.
Ensemble: the nearest dancers reverse outward and begin peeling into two moving wings, opening the route toward
frame-right.
Camera: yield toward frame-left and begin opening the framing as she travels right — still one continuous path.

5.625–6.094s · BEAT 13 — SINGLE RIGHT TOWARD THE DRAPES
Action: Her right foot drives diagonally toward the hanging saffron drapes at frame-right. Her torso leans into
the travel while staying lifted. Her right arm extends forward at shoulder height through BLADE; her left arm
sweeps back with the red fabric streaming behind. Her right foot lands and rebounds without losing speed.
Ensemble: dancers on both sides continue outward, widening the corridor she is entering.
Camera: track backward and left, holding her three-quarter profile with the drapes visible ahead.

6.094–6.563s · BEAT 14 — SINGLE LEFT, REACH AND OPEN THE ROUTE
Action: Her left foot crosses through and lands closer to the drapes; her torso rotates further toward
frame-right. Her left arm rises from behind and travels overhead toward the second curtain edge while her right
hand continues toward the first edge. Both hands stay in motion — neither reaches early and waits.
Ensemble: the two wings keep dancing in place after clearing the centre, holding the rhythm while she exits
their formation.
Camera: keep yielding left so her approach makes strong lateral parallax and the fabric grows in frame.

6.563–7.031s · BEAT 15 — DOUBLE IMPULSE THROUGH THE DRAPES
Action, first rebound: her right foot takes one fast springing step; both hands contact separate curtain edges
and drive them apart, elbows bending then extending as the fabric opens. Her head, right shoulder and leading
foot enter the opening together.
Action, second rebound: her left foot rebounds through the gap and pulls her hips, torso and trailing leg after
it. Her arms keep separating the cloth as her body passes. The drapes whip inward behind her and surge toward
camera from both sides.
Ensemble: dancers stay active in the bazaar behind her, then disappear as the fabric closes across the view.
Camera: follow directly into the opening. By 7.031 seconds moving fabric covers the entire frame and she is no
longer visible.

7.031–8.000s · FULL-FRAME FABRIC
Action: The drapes keep rippling, twisting and sliding across the lens from her passage. The frame stays
completely filled with moving cloth.
Camera: momentum continues forward beneath the cloth, never settling.

Paola starts every new movement first and performs the largest, clearest version of it. The other dancers share
her rhythm with visible differences in step length, elbow height, rotation and recovery. They are visibly
working: chests rising, loose strands of hair stuck to damp temples, skirts swinging with real weight.

CONTINUITY
The light, the colour, the costume, the street and the grade all continue exactly as they are in @Video 1 and
never shift. Dust keeps lifting where feet strike the stone and hanging in the raking sunlight; the overhead
cloth keeps swinging as bodies pass under it; every dancer crossing the sun breaks it into a brief warm flare.

PHYSICS
Real weight throughout: the balls of her feet meet the stone and push off it, her weight rebounding upward out
of every landing. Her skirt and dupatta trail a moment behind every movement and snap out on every sharp ***REMOVED***
Her anklets swing with real weight. The drapes carry real cloth weight — heavy, slow to start, fast once moving.

ACTING
Paola dances with easy command: chin level, faintly amused, the look of someone who knows the street is hers.
She never performs toward the camera and never plays coy, and her eyes stay level and forward, never on the
lens. Each of the other dancers wears her own expression.

AUDIO
The attached track is the only music, and no music is added to it. No dialogue and no singing. Any sound from
feet, anklets, fabric or the street sits quietly underneath the track.

FINAL FRAME
No on-screen text anywhere in frame — no lettering, no signage, no logos, no captions, no overlays.

CAPTURE
A big-budget Indian film dance sequence, photographed on real film, matching @Video 1 exactly: wide-latitude
colour negative, 24 frames per second at a 1/48-second exposure, so every
fast limb and every flare of fabric carries real photographic motion blur. Fine 35mm grain. Preserve the flare,
the bokeh and the optical character already present in @Video 1. Photographed, not generated — real people
dancing in a real street, with no CGI, no game-engine look, no frame interpolation, no plastic skin and no
frozen posing.

---

## WHAT TO JUDGE
1. **Does frame one continue the step**, or reset? That is the extend bet.
2. **Does the tail survive to 7.031s?** The drape burst IS the W3 handoff. If it truncates, everything
   after beat 13 is lost and there is no transition.
3. **Do both hands actually part the cloth**, or does she walk through it?
4. **Does the framing close to chest-up and reopen** without the camera reading as two moves?
5. Any frozen ensemble. Any face crossed by a passing body. Any sky or grade shift off @Video 1.
