# SD2.0 GUIDE — WHAT IT CHANGES FOR RANGE REEL
### Reviewed 2026-07-29 against our actual build. Three findings are serious.

---

# 🔴 THE THREE THAT MATTER

## 1. OUR CHARACTER SHEETS WILL CAUSE THE "TWINS" BUG

> *"**Do not add more angles.** A front/side/three-quarter turnaround makes identity drift worse, not
> better, because the model reads the angles as different people."*
>
> *"Seedance 2.0 frequently reads a multi-view sheet as several different people… it is a leading cause
> of the **'twins' bug**, where two identical copies of your character show up in the same frame."*
>
> *"**The mixed-reference mistake:** do not hand the model one composite image that crams the face, the
> pose, the outfit, and a detail crop into a single picture. The face ends up occupying a small fraction
> of the pixels, gets a correspondingly small share of the model's attention, and identity drifts."*

**Every character asset we built is exactly the thing it warns against.** `Pao-Bolly`, `Pao-Agent`,
`Pao-MessyBun`, `Pao-Gold`, `W5_Kimono_sheet` — all **3-panel composites** (front headless / back with
head / face CU). The face occupies roughly a third of a third of the frame.

### The fix — and it is cheap
SD2 wants **exactly two images with separated jobs:**
1. **A face-only headshot** — head only, neutral, minimal shoulders/background, face dominating frame.
2. **One full-body shot** for costume and proportion.

Then split the roles in the prompt, **face first**:
> `Define the woman in @Image 1 as Paola. Paola's facial features reference @Image 1 (the headshot).
> Her outfit and styling reference @Image 2 (the full-body photo).`

⚠ **This is an SD2 rule, not a Higgsfield rule.** The 3-panel sheets remain fine for *generating stills*.
They are wrong as *SD2 video inputs*. **We need to slice each sheet into a face crop + a full-body crop
before the 720 test day** — that is image editing, not generation, so it costs nothing.

> Extra reason to care: *"a drifting face can wander toward resembling a real public figure, and that can
> get the generation blocked at review."* Identity drift is also a rejection risk.

## 2. FAST ACTION IS THE MODEL'S WEAKEST AREA — AND IT NAMES OUR SHOTS

> *"**Go small and slow.** Seedance 2.0 handles gentle, continuous, small-scale movement far more
> reliably than high-energy motion. **Sprints, big jumps, and violent rolls** are where limbs deform and
> physics breaks."*
>
> *"Fast, high-impact action is the hardest thing to ask of this model."*

**Our reel is nothing but fast action.** A kickflip is a big jump. Nelson's W3 entry is a **violent roll** —
named explicitly. The W4 drift is high-energy vehicle motion.

### The fix the guide gives — and we should adopt it
> *"That is exactly why this prompt leans on a **choreography reference video** rather than trying to
> describe the kick in words: **showing the motion is far more reliable than describing it.**"*
>
> *"If a shot keeps failing, the fix is usually to **slow the action down or break it into two shots**,
> not to add more adjectives."*

**SD2 accepts up to 3 video clips (2–15 s each).** We should source short motion-reference clips for the
three hardest beats:
- **the kickflip** (W1 S3–S4)
- **the tumble roll into cover** (W3 S1)
- **the drift** (W4 S3)

That is a new asset class we had not planned for, and it is the single highest-leverage addition.

## 3. CROWDS OVER FOUR PEOPLE DESTABILISE — WORLD 2 IS AT RISK

> *"**A hard ceiling on characters:** when more than four reference people are involved, output stability
> drops sharply. You start seeing the wrong number of people in frame, or duplicates. If you need a crowd
> of six, **generate them as two grouped images of three first, then use those images as the reference**."*

**World 2 Shot 3 is "the whole ring locks to her"** — a synchronized Bollywood crowd. That is well over
four people, and the failure mode is exactly *wrong number of people / duplicates* — the thing that would
destroy a synchronized-choreography shot.

**Mitigation:** build the crowd as **grouped plates first** (3 dancers per image), then reference those
rather than asking SD2 to invent a ring. Worth putting to Franco before W2 boards are finalised.

---

# ✅ WHAT WE ALREADY GOT RIGHT

## Timecodes — our architecture is safe, but keep them out of prompts

> *"Seedance 2.0's support for precise timing is **unstable**, and forcing exact durations onto segments
> can actively break the generation. **Sequence the shots instead.**"*
>
> *"If the pacing genuinely matters, the reliable lever is to **generate fewer shots per clip**, not to
> write tighter timecodes."*

At first read this looks like it threatens the whole half-bar lattice. **It does not** — because we
already generate **one shot per clip** and cut on the lattice **in Resolve**, not inside SD2. That is
precisely the recommended pattern, and "fewer shots per clip" is maximally satisfied at ***REMOVED***

⚠ **But:** the timecodes printed on our storyboards are **our** trim plan. **They must not be pasted into
SD2 prompts.** Franco already said the same thing — *"describing what the progression MEANS beats listing
timestamps."* Two independent sources now agree.

## The 4-second floor — already handled
Generation range is **4–15 s**. Our shots run **1.875 s to 5.625 s**, so anything under 4 s generates at
4 s and gets trimmed. `BEAT_MAP.md` already states this. ✅

## Landscape — already right
> *"generate in landscape, because spurious subtitles appear significantly less often in landscape."*

We are 16:9 throughout. ✅ *(Note: there is **no 2.35:1** option — if scope is ever wanted, pick **21:9**.)*

## 720p + upscale — consistent
**4K is only on full Seedance 2.0; Fast and Mini cap at 720p.** Nelson's plan is a 720 unlimited day, and
our standing note is *"720p → Topaz"*. Consistent. ✅ *(4K output is H.265 10-bit and some players won't
preview it.)*

---

# ⚠ SMALLER THINGS TO FIX

| Finding | Action |
|---|---|
| **One camera move per shot.** *"Asking a single shot to push in, orbit, and pan at once is the fastest way to destabilise the image."* | Audit our compound moves. **W1 S4 "low tracking + upward tilt into slow-mo hold"** and **W1 S2 "wrapped tracking"** (accelerates, eases outward, settles into a lateral track) are multi-move. Simplify or split. |
| **Audio files must be ≥ 2 s.** | Our **1-bar shots are 1.875 s** — below the floor. Franco's *"one bar of pre-roll"* already fixes this (1 bar + 1 bar = 3.75 s). Keep the pre-roll mandatory, not optional. |
| **Audio can never be the only reference.** *"Text plus audio alone will not generate."* | Never send an audio-only job. Always pair with the start frame. |
| **4–5 assets total, not the ceiling.** Roles: character (1–2) · scene (1) · camera video (1) · audio (1). | Our planned stack — start frame + end frame + Paola + environment + audio — **is exactly 5, at the limit.** See the open question below. |
| **Reference aspect ratio must match output**, else distortion. Refs must be 0.4–2.5 ratio, 300–6000 px/side. | Our 16:9 plates (5504×3072 = 1.79) are fine. **Our square 2880×2880 character sheets are 1.0 and will be force-fit against a 16:9 output** — crop them when slicing for SD2. |
| **Bracket type-signals:** `( )` music · `< >` SFX · `{ }` dialogue · `【 】` subtitles | Use `< >` for our SFX beats — `<two rounds smack the wall>`, `<engine>`, `<tyres break traction>`. No dialogue in the reel. |
| **Define the subject before referencing it**, then reuse one label only. | Standardise on **"Paola"** in every prompt. Never mix "she" / "the woman" / "Paola". |
| **"reference @Video 1" breaks edit/extend jobs** — the word *reference* reclassifies the task. | If we ever extend a clip, write *"Extend @Video 1"*, never *"reference"*. |
| **Chained extensions decay**, showing first as mottled colour on faces. | Keep extension chains short. Prefer generating fresh over extending twice. |
| **Extension joins jump.** Fix in the edit: trim ~6 frames off the outgoing clip and 1 off the incoming. | Better — plan joins to land **on our half-bar cuts**, where a discontinuity is invisible by design. Our lattice already gives us those. |

---

# 🔲 ONE OPEN QUESTION FOR FRANCO

**Does the start frame make the separate character and environment references redundant?**

The guide's cut test is: *"Will removing this reference actually change the result? Is another asset
already doing this job?"*

Our planned 5-asset stack is **start frame + end frame + Paola ref + environment ref + audio**. But the
**start frame already contains Paola, in costume, in the environment.** So the Paola and environment refs
may be doing a job the start frame already does — which would put us at **3 assets (start + end + audio)**,
comfortably inside the recommended range instead of pinned at its ceiling.

Counter-argument: a face-only headshot carries identity far more strongly than a face inside a wide start
frame, and identity drift is our biggest named risk. So the likely answer is **start + end + face headshot
+ audio = 4**, dropping the environment ref and the full-body.

**Worth one question to Franco rather than guessing** — it decides the input recipe for all 24 shots.
