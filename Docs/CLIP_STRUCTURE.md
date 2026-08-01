# CLIP STRUCTURE — three clips per world
### Franco's ruling, 2026-07-31, on Nelson's 8-second-clip proposal. **This replaces the 4-shot editorial skeleton.**

---

## THE RULING: **three clips per world. 18 generations, not 24 and not 12.**

Nelson's proposal was to stop thinking in four short shots and generate 8-second clips instead, combining
them to 15s per world — because the unlimited window gives **8-second 4K generations**, so anything
shorter wastes the tier.

Right instinct. The arithmetic pushed it to three rather than two.

### Why not two clips (4+4 bars = 7.5 + 7.5s)

> *"The studio author showed that SD2 can preserve one broad 7–15-second journey while **quietly deleting, merging, or
> replacing the individual beats inside it.** A 7.5-second clip carrying two designed actions is therefore
> likely to return **one strong action plus improvised connective tissue**."*

That leaves a bad three-way choice: one idea per clip (only two visual ideas per world), two ideas and
accept one vanishes, or regenerate until both land — which destroys the efficiency argument.

Plus: **8+7 doesn't even land on the grid.** At 128 BPM one bar = 1.875s, so 8s = 4.267 bars — a mid-bar
cut. And 4+4 is the *only* two-clip split where both halves fit under 8s, so:

> *"Six consecutive worlds divided exactly in half will create a detectable inhale/exhale rhythm. It is
> not as busy as four equal shots, but it is still **a template stamped six times.**"*

---

## 1. THE SPLIT VARIES BY DRAMATIC FUNCTION — not to avoid repetition

> *"Do not force all six worlds to have unique arithmetic purely to avoid repetition. That becomes
> **another mechanical system wearing a fake moustache.**"*

**Position the SHORT clip according to what the world does:**

| Split | Bars | Seconds | Use when |
|---|---|---|---|
| **2 + 3 + 3** | | 3.75 · 5.625 · 5.625 | the world needs an **immediate impact or transition arrival** |
| **3 + 2 + 3** | | 5.625 · 3.75 · 5.625 | the **central beat is the punctuation** |
| **3 + 3 + 2** | | 5.625 · 5.625 · 3.75 | the world **builds toward a compressed exit or seam** |
| **2.5 + 3 + 2.5** | | 4.6875 · 5.625 · 4.6875 | **only** when a half-bar cut genuinely improves the music or match geometry |

⚠ **His arithmetic correction:** 2.5 bars = **4.6875s**, which lands on the **half-bar lattice, not a bar
line**. Valid under the ratified lattice, but it is a deliberate half-bar cut — not a default.

---

## 2. 🔑 THE THREE-ZONE GENERATION MODEL — the most useful part of the ruling

Generating 8s and trimming afterwards **hurts** if done naively:

> *"It hurts when you ask SD2 to choreograph across all eight seconds and then arbitrarily remove 2.375
> seconds. The model may **place the payoff in the discarded section** or stretch the action across the
> entire runtime."*

**So name the editorial window BEFORE generating.** Every 8-second generation is defined in three zones:

```
lead-in handle  →  FINAL EXTRACTION WINDOW  →  continuation handle
```

### For a 3-bar shot (5.625s)
| Zone | Timecode |
|---|---|
| one-bar lead-in | `0.000 – 1.875` |
| **the exact shot — extract this** | **`1.875 – 7.500`** |
| continuation handle | `7.500 – 8.000` |

### For a 2-bar shot (3.750s)
| Zone | Timecode |
|---|---|
| one-bar lead-in | `0.000 – 1.875` |
| **the exact shot — extract this** | **`1.875 – 5.625`** |
| continuation handle | `5.625 – 8.000` |

> *"This is better than telling the model 'make an eight-second action and I'll find something inside it.'
> The desired editorial section is **named before generation**. The extra footage gives you handles
> without changing where the designed beat belongs."*

⚠ **The lead-in must not contain another action** — it is a stable state, not a second beat.

🔑 **Note how this rhymes with the audio.** The one-bar lead-in is the same 1.875s pre-roll the audio
slicer already emits, so **video lead-in and audio pre-roll are the same bar.** They align by construction.

---

## 3. PLATE CONSEQUENCE

> *"Build around **three shot obligations per world, 18 total**, not two and not four. Seam plates remain
> additional transition authorities where required, but the editorial skeleton becomes three clips per world."*

**This changes the manifest.** The readiness audit counted against a 24-shot plan; the skeleton is now 18.
Seam frames stay as separate transition authorities on top.

---

## 4. Supporting finding — trim headroom (measured, `Tools/slice_shot_audio.py`)

| Structure | Clip content | Headroom inside an 8s generation |
|---|---|---|
| 2 clips (4+4 bars) | 7.5s each | **0.5s** — effectively no handles |
| **3 clips (3+3+2)** | 5.625 / 5.625 / 3.75s | **2.375s** — real handles |

With 7.5s of content in an 8s generation every cut must land exactly where SD2 put it. At 5.625s there is
over two seconds of slack to find the right frame — which matters precisely *because* SD2 compresses beats
and drops listed actions. **Independent second argument for three.**

Audio is already solved: the slicer cuts any bar range with a one-bar pre-roll, verified sample-exact
(W3 as 3+3+2 → 7.500 / 7.500 / 5.625s files). **The pre-roll lives in the audio reference, not the video
duration**, so it does not eat the 8s cap.
