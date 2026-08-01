# SD2 EXTENSION + AUDIO — the ruling and the test order
### Franco, 2026-07-31. **REWRITTEN against the real workflow.** Supersedes the first version entirely.

---

## ⚠ WHY THIS WAS REWRITTEN

The first version of this doc was built on a **wrong description of the workflow that I gave Franco**. I
implied a chain where identity is carried by inheritance alone and where a weak generation could propagate
downstream. **Neither is true.** Nelson's actual method:

- **8 seconds max, 4K.** Hard ceiling on every generation.
- **The FULL reference stack is attached to EVERY generation** — character, wardrobe, environment, props.
  The video reference carries motion and temporal state; the static authorities reassert who Paola is and
  what the world is. **Two separate channels, both present every time.**
- **Every clip is QA'd before anything extends from it.** A failed generation is regenerated. Nothing
  unapproved is ever built on.
- **Generation runs in timeline order**, so each clip extends from an already-approved one and nothing is
  ever matched backward.

Cost of the error: a round of argument on a deadline-critical project. Root cause and the standing fix:
`check-the-precondition-before-naming-a-risk`.

---

## 1. 🟢 THE RULING — **"The extension approach is sound under the actual workflow."**

> *"Re-attaching the full character, wardrobe, environment, and prop stack on every generation **removes the
> main reason for a blanket 'never extend twice' rule**. The video reference carries motion and temporal
> state; the static authorities reassert what Paola and the world are supposed to be. Seedance officially
> supports combining video, images, and audio in the same generation, including multiple reference inputs,
> so this is a **native multimodal use pattern rather than a workaround**."*

> **"There is no defensible fixed chain limit such as one extension or two extensions under these conditions."**

### The safe rule — quality-based, not count-based

> *"Continue the chain for as long as every new clip independently passes QA against **both** the previous
> approved video **and** the static authorities."*

| Chain length | Ruling |
|---|---|
| Base + 1 extension | normal and sound |
| Base + 2 extensions | also sound if both pass QA |
| Longer | permitted, unnecessary for this reel unless a world needs it |
| **Reset with a fresh generation** | only when the chain **fights the authorities**, or the next shot needs materially different camera grammar |

### What to actually watch for at the QA gate

Not decay — these four:

- **Join discontinuity** — even when both clips are independently good, velocity, focus, exposure, grain,
  hair motion or limb position may jump across the generated boundary.
- **Cumulative geography drift** — the character stays correct while the street, corridor, car cabin or
  garden gradually changes spatially.
- **Temporal simplification** — later extensions preserve the scene but become **less ambitious, slower or
  more generic**, because the model prioritises continuity over a new designed action.
- Geometry adjustment at the reconnect.

> *"These are all observable at the QA gate. **None justifies a preset numerical cap.**"*

---

## 2. THE SEAM TEST — now run in timeline order

**Forward-extend from an approved end-of-W3 clip.** Not standal***REMOVED***

> *"Do not spend accepted generations on the standalone version first. **The timeline-order extension is now
> both the more relevant and the cheaper decisive test.**"*

Standalone keeps value only as a **diagnostic fallback** — if the forward extension fails, a standalone
generation distinguishes *"cannot perform the world transformation at all"* from *"cannot reconcile the
approved W3 state with the new W4 authorities."*

### Pass criteria — two accepted forward-extension attempts from the same approved W3 source

- clean temporal continuation from W3
- no visible jump before the whiteout
- genuine full-frame coverage
- same Paola, same agent wardrobe
- preserved hand/shoulder gesture through the transition
- **gun absent after the reveal**
- correct specified car interior
- **no hotel residue**
- **no correction pulse immediately after the reveal**
- usable W4 motion after the transition

---

## 3. THE AUDIO TESTS — unchanged in substance, corrected in setup

**The visual reference stack stays attached throughout** — *"because that is the actual workflow. It does
not change the audio diagnosis."*

### Test A — audio base
One accepted 8s diagnostic clip: simple performer/environment stack + the **full 15-second diagnostic
audio**, built with three unmistakable sections (slow low kicks → fast high claps → sustained tone) and the
instruction to walk slowly / switch to rapid footwork / freeze arms-up.

**Answers:** does a base generation use the opening 8 seconds, or compress the whole 15?

### Test B — audio extension
Extend that approved clip once, re-attaching the previous video + **the same reference stack** + the same
complete 15-second audio.

| Result | Meaning |
|---|---|
| starts **fast**, then freezes ~2s later | ✅ **inherited audio clock** |
| restarts **slow** | audio clock restarted |
| stays fast, never freezes | video motion inherited, audio position ignored |

> *"**Only the first result supports feeding the full world audio to every extension.** Anything else means
> Pablo's trimmed per-clip audio remains the reliable method."*

---

## 4. RUN ORDER

1. **Test A** — audio base
2. **Test B** — audio extension *(A and B are cheap and answer the method question)*
3. **Seam test** — forward extension from approved W3, two accepted attempts
4. Standalone seam **only if** the forward extension fails, to isolate which half broke

🔴 **Moderation-refused jobs do not count as failed tests. Only accepted generations count.** With a ~50%
refusal rate this distinction decides whether a result is real.

---

## Our standing advantage

`SD2_GUIDE_FINDINGS.md`: *"Extension joins jump… **plan joins to land on our half-bar cuts, where a
discontinuity is invisible by design. Our lattice already gives us those.**"* At 128 BPM there is a bar
line every 1.875s. Join discontinuity — Franco's first named QA risk — is the one we are best positioned
to hide.

⚠ Syntax: write **`Extend @Video 1`**, never *"reference"* — that word reclassifies the job and breaks the
extend.
