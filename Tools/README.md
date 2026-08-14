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
- `w2_clip2_carrier_audit.py` — FFT cross-correlation audio-lineage audit; caught the model
  layering invented percussion over the real track (per-second correlation 0.97 → 0.29).
- `lag2gate.py`, `key_gate.py`, `lineartest.py` — timing-lag, musical-key, and linearity gates.

**Measurement — deciding what a sound actually is**
- `attackweight.py` — attack-weight profiling (why energy = attack, not onset count).
- `pitchedtransient.py`, `bassroot.py`, `allroots.py` — pitched-transient and root-note
  analysis across stems.
- `candidates.py` — candidate take scoring/ranking.
