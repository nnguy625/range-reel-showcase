# RANGE REEL — MUSIC METHOD

*How the six world arrangements get built and how they get judged. Written 2026-07-26.*

---

## THE ARCHITECTURE

One spine, six overlays. The spine is `Assets/Music/E1_MASTER_90.wav` — 90.000s, 128 BPM, drums only,
never re-rendered. Each world gets a **melodic overlay with no drums in it**, layered over the
unchanged spine.

**Cover was tried and killed.** Franco's linearity test on the world-1 cover found the offsets going
0 → +67 → +20 → −154 → −255 → −360 → **−1326 ms** by bar 72, residual std 362 ms against a 30 ms
threshold. Cover changes the groove *structurally*, not just its tempo, so time-stretching would have
painted over the problem rather than fixed it.

This does not contradict the June result where Cover worked fine for the five `Paola's Theme`
arrangements. **Cover is safe for independent arrangements and unsafe when versions must share one
timeline.** June's five never had to cut against each other; these six do.

---

## THE DRUM DETECTOR — THREE INSTRUMENTS, ONLY ONE OF THEM GOOD

An overlay is only usable if it has no drum kit of its own. Judging that by ear across a dozen takes
is slow and drifts, so it gets measured. Three instruments were built, in this order. **The third one
is the answer; the first two are kept only as history.**

| Instrument | What it measures | Script | Verdict |
|---|---|---|---|
| Transient rate | broadband attacks/sec | `drumcheck.py` | **misleading — retired** |
| Low-band burstiness | 40–120 Hz variation | `drumcheck.py` | **useless — retired** |
| Grid-lock | attacks landing on 128 BPM subdivisions | `gridlock.py` | indirect, kept as a cross-check |
| **Mid-band onset rate** | **attacks/sec in 300–2000 Hz** | **`bandsplit.py`** | **THE TEST** |

### THE TEST — mid-band onset rate

Snare and drum body live in the mids. Split the onset detector by frequency band and drums separate
from everything else by **an order of magnitude, with no overlap at all**:

| Source | mid 300–2k onsets/sec |
|---|---|
| `E1_MASTER_90` spine — known drums | **1.83** |
| `W1_SKATE_(W1a)` cover — known drums | **1.23** |
| every accepted overlay | **0.01 – 0.52** |

There is no threshold-tuning judgment call here. The gap between 0.52 and 1.23 is the whole decision.

### What the first two instruments got wrong

**Broadband transient rate produced one false failure and one false alarm.** It counts every attack
regardless of frequency, so it cannot tell a snare from a brass stab or from high-frequency shimmer:

- **World 3 was wrongly failed** at 4.1 and 5.7 attacks/sec against an arbitrary 4.0 threshold. Its
  mid-band rate is **0.08**. Clean by a wide margin. The attacks were muted brass and plucked barit***REMOVED***
- **World 4 was wrongly suspected** at 5.1 and 4.6 attacks/sec — the densest overlays in the set, from
  a prompt that had explicitly asked for sustained phrases. Its mid-band rate is **0.02 and 0.01**, the
  *cleanest in the entire set*. The density was the distorted baritone's overtones sitting in the
  4–10 kHz band.

**Low-band burstiness measures nothing.** It reads 40–120 Hz variation as a kick signature, but the
accepted `OV2_BOLLY_a` scored 27.6 dB — the highest of anything measured — while the known drum
tracks scored 17.5 and 15.0. Sparse bass notes with gaps between them look exactly like kicks to it.
The same applies to the low-band onset rate and decay figures in `bandsplit.py`: they return ~0.0x
onsets/sec and 35–116 ms decay for *known drum tracks and clean overlays alike*.

> **An instrument that returns the same answer for the positive and negative cases is not measuring
> anything.** Check every instrument against a known positive AND a known negative before trusting a
> single verdict from it. Two of the three built here failed that check, and both failures pointed at
> a real take.

### Calibration (run against known-drum tracks before trusting any verdict)

| File | Transients/sec | Low band 40–120 Hz | On-grid | Truth |
|---|---|---|---|---|
| `E1_MASTER_90` spine | 8.7 | mean 32.9, var 17.5 dB | 37.7% | drums |
| `W1_SKATE_(W1a)` cover | 7.7 | mean 35.2, var 15.0 dB | 38.2% | drums |
| `OV1_SKATE_a` | 3.8 | mean 32.4, var 15.4 dB | 47.9% | clean |
| `OV2_BOLLY_a` | 2.3 | mean 20.3, var 27.6 dB | 27.3% | clean |
| `OV2_BOLLY_b` | 1.9 | mean 28.3, var 18.3 dB | 20.7% | clean |
| `OV3_AGENT_a` | 4.1 | mean 34.4, var 12.9 dB | 26.0% | **clean** |
| `OV3_AGENT_b` | 5.7 | mean 36.5, var 10.9 dB | 24.6% | clean |

### The correction

World 3 was first called a **failure** on transient rate alone — 4.1 and 5.7 against an arbitrary
4.0 threshold. That verdict was wrong. Two things exposed it:

1. Its low-band variation (12.9 and 10.9 dB) was *lower* than the takes already accepted, so whatever
   was making those attacks wasn't a kick.
2. Its onsets are **off**-grid (26.0%, 24.6%) — the same neighborhood as clean Bollywood (27.3%), far
   from the known-drum tracks (37.7%, 38.2%).

The attacks were **muted brass stabs and plucked baritone guitar** — percussive-attack instruments my
first detector could not tell from a snare.

### The rule that came out of it

> **Drums need high attack density AND grid-lock. Either one alone means nothing.**

`OV1_SKATE_a` proves the other direction: 47.9% on-grid — *higher* than both drum tracks — but only
3.8 attacks/sec. That is a rhythmic arpeggio locked to the beat, which is exactly what a good overlay
should be. Grid-lock alone is not incriminating; density alone is not incriminating.

**Do not ship a single-number threshold on a musical judgment.** The first one produced a false
failure inside two takes.

---

## PROMPT DESIGN

Every overlay prompt is built from the same four parts:

1. **Grid** — `128 BPM, 4/4`
2. **Exclusion block** — `melodic overlay layer only, NO DRUMS, NO PERCUSSION, no kick, no snare,
   no hi-hat, no cymbals, no drum machine`
3. **Instrumentation** — the world's signature voices, described as *sustained* wherever possible
4. **Motif + mood + `Instrumental, no vocals`**

### Two lessons that change the wording

**Each world's genre summons its own drum family, so the exclusion block must be genre-specific.**
A generic "no drums" does not cover the instrument that particular genre reaches for first:

| World | Extra exclusion needed | Why |
|---|---|---|
| 5 — Japan sword | `no taiko` | Japanese instrumentation framing summons taiko |
| 6 — Gold couture | `no clap`, `no four-on-the-floor` | deep house summons both by definition |

**Action-genre framing raises attack density even when it doesn't produce drums.** World 3's
"cold neo-noir spy action, controlled danger, forward pressure" returned 4.1 and 5.7 attacks/sec
against Bollywood's 2.3 and 1.9. It passed — but an overlay sits *under* a percussion spine, so lower
density is strictly better. **Describe sustained texture, not an action genre.** Worlds 4–6 were
written that way deliberately.

---

## STATUS

**All six worlds are built and all twelve takes measured clean.** Selection is by mid-band rate first,
then by sparseness (an overlay sits *under* the spine, so less is better), then by length.

| World | Selected file | mid 300–2k | Length | Why this take |
|---|---|---|---|---|
| 1 SoCal skate | `OV1_SKATE_a.mp3` | 0.52 | 128.5s | densest of the six but still 2.4× under drums |
| 2 Bollywood | `OV2_BOLLY_a.mp3` | 0.02 | 179.8s | b also clean |
| 3 Gun-fu | `OV3_AGENT_a.mp3` | 0.08 | 178.0s | take a is sparser than b |
| 4 Car chase | `OV4_CAR_a.mp3` | 0.02 | 89.1s | b is equally clean but only 68.6s |
| 5 Japan sword | `OV5_SWORD_a.mp3` | 0.01 | 178.6s | sparsest broadband of the pair, 1.1 vs 2.7/s |
| 6 Gold couture | `OV6_GOLD_b.mp3` | 0.01 | 179.6s | **b beats a** — 0.01 vs 0.07 mid, and sparser |

Every world only needs to cover its own 15.000s, so all lengths are sufficient — world 4's shorter
takes are not a defect.

Rejected takes stay on disk as fallbacks. Nothing is deleted.

---

## OPEN — THE EDIT-INSTRUMENTS UPGRADE

Suno's **Edit instruments** mode ("add or replace the song's instrumentation", Pro-tier, inside the
existing subscription) is a structurally better mechanism for this exact architecture: it returns the
uploaded spine *with instruments added*, so the result is **phase-locked to E1 by construction**. No
alignment step, no patch, no comb-filter question, no "did the tempo match."

`E1_MASTER_90.wav` is uploaded to Suno and classified as Rhythm / Percussion, so the mode is ready to
test. Not yet run — the tab's renderer froze mid-setup, and a working half-finished pipeline does not
get stalled for an unproven improvement.

**The gate when it is tested:** run `lineartest.py` on the returned mix against E1. If the spine
survives with residuals under 30 ms, this replaces the blind-overlay method for all six worlds. If
the spine is re-rendered and drifts, it is discarded exactly as Cover was, and the blind overlays
stand.

---

## SCRIPTS

Live in the session scratchpad; copy into the repo if they need to outlive it.

- `drumcheck.py <file>` — transient rate + low-band burstiness
- `gridlock.py <file>` — percentage of inter-onset intervals landing on 128 BPM subdivisions
- `lineartest.py <ref> <test>` — is drift linear (stretchable) or structural (reject)
- `bpm2.py <file>` — high-resolution tempo, parabolic peak interpolation, HOP=128

**Instrument note:** the first BPM reading said 129.20 and was wrong — autocorrelation at HOP=256 has
roughly ±3 BPM resolution near 128. At HOP=128 with interpolation, E1 measures **128.289**. A tempo
reading without its hop size is not a measurement.
