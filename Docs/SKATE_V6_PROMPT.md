# WORLD 1 SKATE — v6 prompt (Franco's trap-cadence rewrite, 2026-07-26)

**Franco rejected the current skate section outright:** *"Its rhythm is too straight and
electronically busy, with continuous upper-mid attacks riding the four-on-the-floor spine. That
combination reads EDM or video-game music. The low end also appears split across neighboring pitch
centers, which supports the dissonance you are hearing."*

---

## THE ONE THING TO DO FIRST

**Upload `Assets/Music/E1_SPINE_90.mp3` into Suno** (Create → **+ Audio** → **Upload**) so the
generation runs against the real timing reference.

A text mention of E1 does **nothing** — Franco confirmed it: *"No."* Every earlier "use E1 as the
timing authority" line was decorative.

---

## THE MEASURED NUMBER FRANCO DID NOT HAVE

He said *"tune the 808 to one clear root"* without naming it. Measured from E1's own low end
(pitch-class histogram, 30–80 Hz and 40–160 Hz bands, both agree):

| | |
|---|---|
| **E1 bass root** | **F** |
| **Fifth above it** | **C** |
| Current skate take's bass root | **B** — a **tritone** from F |

A tritone is the most dissonant interval in Western music. That is the clash Franco heard by ear and
Nelson heard on the master. **The prompt must name F.**

---

## PASTE-READY STYLES TEXT

```
High-energy SoCal trap and hip-hop overlay, exactly 128 BPM, 4/4, Instrumental.
Six-attack chant cadence with no vocals and no lyrics: eighth-note triplets across two beats,
accented strong-light-strong-light-strong-light, repeated as a one-bar rhythmic cell.
A deep tuned 808 lands on the accented positions with clear gaps between hits, and one restrained
808 slide at the end of every second bar. The 808 is tuned to F, using only F and the occasional C
a fifth above. Sparse dark keyboard stabs and chopped soul-sample accents answer the same cadence.
The low end is separated: the existing track supplies the short kick attack, the 808 supplies only
the sustained bass tail. Dark, cocky, spacious and trappy, the vocal-like cadence expressed
instrumentally.
```

**NEVER list** (Franco's, verbatim): no four-on-the-floor bassline, arpeggiator, bright pluck loop,
supersaw, synthwave, house rhythm, EDM build, riser, arcade sound, cinematic melody, rock guitar,
extra kick pattern, or dense continuous sixteenth notes.

⚠ **Do not put the 808 on all four quarter notes** — Franco: *"or it will become house music again."*

---

## TIMING IS UNCHANGED

Franco confirmed: **128 BPM, 4/4, 48 bars, six worlds × 8 bars, 15.000 s per world.** The triplet is
a *subdivision inside* the same grid, not a tempo change. E1 keeps the constant quarter-note pulse.
Every overlay, cut, build and transition stays locked to the same timeline.

---

## GATES THIS MUST PASS AFTER GENERATION

| Gate | Threshold | Script |
|---|---|---|
| Drums | mid-band ≤ **0.75** onsets/s | `candidates.py` |
| Flams | ≤ **5%**, swept ±117 ms in 1 ms steps | `buildmaster3.py` |
| Bass root | must read **F**, not a neighbour | `bassroot.py` |
| Two-bar macro variation | lag-2 ≥ 0.60 and lag-2 − lag-1 ≥ 0.08 | `lag2gate.py` |
