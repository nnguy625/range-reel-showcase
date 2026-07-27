# SD2 GENERATION PLAN — how the 24 clips actually get made

*Written 2026-07-26 overnight. Research-verified where marked. Franco cross-check pending.*

---

## ELI5 — the whole thing in six sentences

We already have the music, the locations, and the costumes. Next we draw **48 rough sketches** — the
first and last frame of all 24 shots — and cut them to the real song to prove the timing works before
spending anything. Then we make those 48 sketches into **real photographs**. Then we hand Seedance
**two photos per shot** — the start and the end — and it invents the movement in between. Because the
last photo of one shot is the first photo of the next, the shots hook together and the woman never
teleports. Finally we lay all 24 clips on the song and cut on the beat.

**The one sentence that matters:** Seedance's own input format is *first frame + last frame*, which is
exactly the structure Franco specified for the storyboard — so the boards, the stills, and the video
inputs are all the same artifact at three levels of finish.

---

## THE FOUR STAGES

| # | Stage | Output | Cost | Blocked by |
|---|---|---|---|---|
| A | Grayscale proxies | 48 rough frames | free (Franco) | nothing |
| B | Animatic | 90 s slideshow cut to E1 | free | stage A |
| C | Key stills | 48 real photographs | Higgsfield, $0 on unlimited | stage B proving handoffs |
| D | Motion | 24 clips | **Seedance — the only paid step** | stage C |

**Do not skip B.** It is the only step that proves the rhythm and the handoffs before money is spent.
The predecessor project died by going straight to polished stills and burning two weeks on one frame.

---

## ✅ VERIFIED SD2 CAPABILITIES (my research, 2026-07-26)

| Capability | Finding | Why it matters here |
|---|---|---|
| **First + last frame anchoring** | **REAL.** Set `first_frame_url` + `last_frame_url` → model switches to *interpolation*, generating a path between two known states instead of extrapolating from one | **This is the whole architecture.** Franco's 48-keyframe spec IS SD2's native input format |
| Max duration | 15 s per generation (Dreamina web), 10 s (Doubao app) | our shots are 3.75 s — huge margin |
| Resolution | **up to 2K**, native audio in the same pass | ⚠ our 4K plates are *reference*, not a 4K deliverable |
| Reference assets | up to 12: **9 images**, 3 videos, 3 audio | character + location + prop can ride together |
| Reference priority | character → face → style/scene | attach in that order |
| Video Extension | appends 4–15 s segments repeatedly | length is not a hard ceiling |
| **Known weakness** | on-screen **text renders unreliably** | ⚠ affects the end card — design it as image, not rendered text |

Sources: Segmind API docs · ComfyUI FLF2V workflow · Atlas Cloud API guide · Magic Hour settings guide ·
seedance.tv first/last-frame guide.

**Still to reconcile with Franco** (he is researching independently): whether last-frame anchoring
degrades at short durations, real identity-hold limits across 9 refs, and which prompt structures
measurably outperform vs. folklore.

---

## THE PER-SHOT RECIPE

For each of the 24 shots:

```
first_frame  = the approved key still for this shot
last_frame   = the approved key still for THIS shot's end
               (which, at a world boundary, IS the next shot's first frame)
references   = character element + location element (+ prop if held)
duration     = 4 s generated, trimmed to 3.75 s on the bar grid
prompt       = ONE motion beat only. Not a scene description.
audio        = diegetic only, or silent. Music is added in the edit.
```

**One motion beat per clip.** "She pushes off and the board rolls forward" — not "she pushes off,
carves past cars, then whips past a pole." Three beats in one clip is how you get soup.

### Which cuts need true anchoring (Franco's ruling)

| Cut | Method |
|---|---|
| 1→2 skate → Bollywood | **ANCHORED** — last frame of W1-S4 IS first frame of W2-S1 |
| 2→3 Bollywood → gun-fu | independent, hidden by the fabric wipe |
| 3→4 gun-fu → car | **ANCHORED** — arms-extended → hands-on-wheel, pose match |
| 4→5 car → katana | independent, hidden by impact / hard downbeat |
| 5→6 katana → runway | independent, hidden by the particle dissolve |
| 6→end runway → sidewalk | **ANCHORED** — continuous stride behind a full-frame occluder |

Three anchored pairs, three independent. Anchored pairs are generated **as a pair**, never separately.

---

## THE PAID STEP — how to spend the least

Nelson buys Seedance unlimited **once**, and we want that window used well.

**Do not generate 24 clips on day ***REMOVED***** Run the **vertical slice**: World 1 only, all four shots,
cut together against its own music. Four generations answer every question that matters — does her
face hold, does FLF2V actually interpolate cleanly, does 3.75 s read on the grid, does the anchored
cut into World 2 work.

- **If it works** → the other five worlds are mechanical, and we run them in parallel.
- **If it breaks** → we lost four generations, not twenty-four.

**Three-attempt cap per shot, unchanged.** Three failures → change the framing or cut the shot. There
is no v4.

---

## OPS CHECKLIST — pre-flight before every SD2 generation

Same discipline as the Higgsfield gate. Verify **all** of it in the same action that fires:

- [ ] first frame = the approved still, not a lookalike
- [ ] last frame set (and for anchored cuts, identical to the neighbour's frame)
- [ ] character element attached · location element attached · prop if held
- [ ] reference order: character → face → style/scene
- [ ] **exactly one** motion beat in the prompt
- [ ] duration 4 s
- [ ] resolution at max available (2K)
- [ ] audio diegetic or none
- [ ] screen direction matches the world's axis (L→R except World 5)
- [ ] no on-screen text expected in frame
- [ ] cost confirmed against the unlimited window before firing

---

## OPEN QUESTIONS FOR FRANCO

1. Does last-frame anchoring hold at 3.75 s, or does it need a longer generation trimmed down?
2. With 9 reference slots, does identity hold better with more refs or fewer-and-cleaner?
3. For the three anchored pairs, generate as one continuous 8 s and cut, or two 4 s clips?
4. Does 2K output survive the 1080p delivery, or should shots be framed looser for reframing room?
