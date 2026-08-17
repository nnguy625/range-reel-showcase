# Tools — Python QA / DSP production tooling

Working production scripts, ~2,000 lines total. Built through AI-assisted development:
requirements, test cases, and acceptance thresholds defined by the director; implementation
iterated with coding agents; every tool validated against known-good and known-bad cases
before its numbers were trusted. These are working instruments with absolute local paths,
not packaged software — by design.

## Map (what proves what)

**Carrier assembly — the 128 BPM beat-grid audio pipeline**
- `buildmaster3.py` — assembles the guide carrier on the beat grid: gain-staged stem mix,
  cosine seam fades, exact-duration render.
- `slice_shot_audio.py`, `w2_build_from_X.py` — clip/carrier cutting utilities on the same
  frame-exact grid (1 beat = 0.46875 s = 11.25 frames at 24 fps).

**Alignment — the 1 ms sweep**
- `surgical.py`, `surgical2.py` — flam/overlay alignment: sweeps candidate offsets across a
  ±117 ms window in 1 ms steps and scores each against the target grid.

**Gates — self-rejecting quality checks (a render fails on numbers, not opinion)**
- `gatev6.py` — FFT spectrogram gate for carrier QA.
- `w2_clip2_carrier_audit.py` — FFT cross-correlation carrier-alignment audit plus a music map
  (onset envelope) so timecoded beats can be anchored to audible events; it verified the 0.263 s
  clip-2 carrier misalignment by correlation rather than arithmetic.
- `audio_lineage.py` — did the render keep the attached track? Extracts the render's audio, aligns
  it to the carrier, and scores the two second by second. Positive control: the A-16 render scores
  1.00 in every window; audio-ON hip-bounce asset renders (A-17/A-18) score ≤ 0.3. The 2026-08-07
  session measurement that set the law (per-second correlation 0.97 → 0.29 where the model layered
  its own percussion) is logged in Docs; this is the published, re-runnable form of that check.
- `lag2gate.py`, `key_gate.py`, `lineartest.py` — timing-lag, musical-key, and linearity gates.

**Measurement — motion tempo (the sari-centroid method)**
- `bounce_tempo.py` — tracks the vertical centroid of the costume mask frame by frame, finds the
  bounces, and gates the take on interval vs the 128 BPM beat (0.46875 s) and slowest/fastest
  spread (≤1.20×). Reports full-clip and bounce-run numbers; approved leg-lift and planted takes
  read 0.45–0.458 s / 1.2× PASS, the rejected first leg-lift take 1.8× FAIL.

**Measurement — deciding what a sound actually is**
- `attackweight.py` — attack-weight profiling (why energy = attack, not onset count).
- `pitchedtransient.py`, `bassroot.py`, `allroots.py` — pitched-transient and root-note
  analysis across stems.
- `candidates.py` — candidate take scoring/ranking.
