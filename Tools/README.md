# Tools — Python QA / DSP production tooling

Working production scripts, ~2,000 lines total. Built through AI-assisted development:
requirements, test cases, and acceptance thresholds defined by the director; implementation
iterated with coding agents; every tool validated against known-good and known-bad cases
before its numbers were trusted. These are working instruments, not packaged software: the two
measurement gates take any path on the command line and ship with tests (below); the carrier-
assembly scripts still carry the absolute local paths they were used with.

## Map (what proves what)

**Carrier assembly — the 128 BPM beat-grid audio pipeline**
- `buildmaster3.py` — assembles the 90.000 s guide carrier on the beat grid: six overlay takes
  high-passed at ~100 Hz before trimming, placed by the flam sweep below, gain-staged ~4 dB
  under the untouched E1 spine, 40 ms seam fades on every slice, a 117 ms cosine micro-gap
  (10 ms down / 97 ms hold at −18 dB / 10 ms up) on the outgoing overlay that lands at unity
  exactly on the next downbeat, one fixed −7.5 dB master trim, exact-duration render.
- `slice_shot_audio.py`, `w2_build_from_X.py` — clip/carrier cutting utilities on the same
  frame-exact grid (1 beat = 0.46875 s = 11.25 frames at 24 fps).

**Alignment — the 1 ms sweep**
- `buildmaster3.best_offset()` — for each overlay take, snaps the take's first onset forward
  to the next whole bar, then sweeps the start of its 15 s world window across ±117 ms (one
  16th at 128 BPM) in 1 ms steps. Each candidate is scored by the percentage of overlay
  onsets that land 15–60 ms from the nearest spine onset — a flam — and the minimum wins.
  If the best is still over the 5% ceiling it widens ONCE to ±234 ms and stops there:
  reject rather than shift further. Snapping to the bar line measured 43% flams vs 0.0% at
  the best offset 15 ms away.

**Subtraction — transient ducking and click repair (Franco's "do not regenerate" chain)**
- `surgical.py` — the V9 surgical subtraction on the skate overlay: zero-phase FFT band
  split (0–300 / 300–2000 / 2000+ Hz), −7 dB cosine ducks (35 ms) on every detected mid-band
  transient, escalated 1.5 dB at a time until the strict 300–2000 Hz onset rate falls under
  the 0.75/s gate; final-bar mid/high roll-off to −9 dB; 100 ms trims on the ordinary 808
  tails, preserving the featured slide at the end of every second bar; a −2.5 dB / 75 ms
  sidechain dip under every beat.
- `surgical2.py` — V10, the ratified chain ("V10 landed. Keep the 55 ms window at 7 dB"), now
  the standard subtraction for every world (source and output names are its two arguments):
  the same subtraction rebuilt so every edit is ONE continuous gain envelope with 8 ms
  equal-power ramps in both directions — the V9 tail trims faded to zero and resumed at full
  amplitude, a step, i.e. a click at each boundary. Escalates the duck window rather than the
  depth, ramps into the final-bar roll-off, and closes with a discontinuity scan of the output.

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
- `key_gate.py`, `lineartest.py` — Franco's three-part key-confidence gate (window stability
  ≥ 70%, separation ≥ 0.10, tonal evidence — a percussion-dominant passage is AMBIGUOUS, never
  assigned) and the linearity gate against the E1 spine (residual after the best linear fit
  < 30 ms, otherwise discard, do not stretch).
- `w6exception.py` — the World 6 exception gate (Franco's 2026-07-27 ruling): World 6 alone
  gets a 1.15/s mid-band onset ceiling instead of 0.75/s, because the detector there counts
  tonal runway shimmer rather than a drum kit — valid only with low-band onsets < 0.10/s (no
  kick of its own), flams < 5%, root F, and one stable pitched layer. The script measures
  the mid- and low-band onset rates and the root, and reports inter-onset-interval regularity
  (median + CV) as evidence for the single-layer condition; the flam figure is not measured
  here — the sweep in `buildmaster3` reports it per world.
- `lag2gate.py` — not a gate. An unvalidated rebuild of the lag-2 (two-bar hook vs one-bar
  loop) spectral-contour check lost in the 07-27 crash; its banner reads "UNVALIDATED REBUILD
  — DO NOT MAKE DECISIONS ON THESE NUMBERS" and it fails its own calibration control after
  three attempts that differ in kind. Kept as the record of the attempt: the recorded lag-2
  numbers live in Docs/STATE.md, and a miss on this check was always manual-review, never
  auto-reject.

**Measurement — motion tempo (the sari-centroid method)**
- `bounce_tempo.py` — tracks the vertical centroid of the costume mask frame by frame, finds the
  bounces, and gates the take on interval vs the 128 BPM beat (0.46875 s) and slowest/fastest
  spread (≤1.20×). The verdict is judged on the bounce run — the longest contiguous stretch of
  intervals within 0.7–1.3× of the median, i.e. the bar where the bounce actually happens — with
  the full-clip numbers (lead-in and settle included) reported alongside; approved leg-lift and
  planted takes read 0.45–0.458 s / 1.2× PASS, the rejected first leg-lift take 1.8× FAIL.

**Measurement — deciding what a sound actually is**
- `attackweight.py` — attack-weight profiling (why energy = attack, not onset count).
- `pitchedtransient.py`, `bassroot.py`, `allroots.py` — pitched-transient and root-note
  analysis across stems.
- `candidates.py` — candidate take scoring/ranking.

## Run the tests

`py -m pip install -r requirements.txt` then `py -m pytest Tools/tests -q` (13 tests, ~7 s, no media
needed — the suites feed synthetic signals and synthetic frames through the real code paths).
`test_audio_lineage.py`: identical audio scores 1.000 in every window (PASS); a render delayed by
0.137 s is realigned to the millisecond and still passes; contamination injected into a one-second
window drops that window to ~0.27 and fails it by index; an unrelated track fails every window.
`test_bounce_tempo.py`: an on-beat 128 BPM costume trace reads 0.469–0.471 s per bounce, spread
1.09 (PASS); an alternating 0.35 / 0.62 s trace reads spread 1.7–2.3 (FAIL); the mask, the centroid
trace and the bounce-finding logic are exercised directly.

## Results on the real takes

`results/` holds the JSON the two measurement tools emit when re-run on the actual takes the case
study cites (media not included; see `results/README.md`): planted take 0.458 s / 1.2× PASS, leg-lift
take 0.45 s / 1.2× PASS, the first leg-lift take 1.8× FAIL; A-16 render 1.00 in every window against
its track, the two audio-ON takes ≤ 0.86 with most windows under 0.3.

## Known limits (read before trusting a number)

- `audio_lineage.py` is a lineage gate, not an "any added sound" detector: at the 0.6 floor it
  catches material contamination (the 0.29 case), but a quiet added tone that the original track
  still dominates will pass. Lower `--floor` or shorten `--window` to make it stricter.
- `bounce_tempo.py` measures the vertical centroid of an HSV color mask — it needs a costume the
  threshold can isolate, and camera motion, occlusion and cloth area move the centroid too. Its
  detrend + smoothing can produce edge peaks on a clip with no lead-in; a take with a still lead-in
  and settle (as the approved takes have) measures cleanly. Its thresholds are project-set, not
  universal: the ≤1.20× spread ceiling was set at the approved planted take's own spread, and the
  mean-interval tolerance is ±15% of the beat. Both tools carry the thresholds they were used with;
  they are instruments, not products.
- The audio floor of 0.6 sits close to the 0.60–0.68 windows of the very clip that set the rule; it
  separates the 0.29 class of failure from a clean pass, and is not a fine discriminator between
  slightly altered mixes.
