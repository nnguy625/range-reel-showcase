# Tools/results — raw tool output for the takes the case study cites

Media is not in this repository; these are the instruments' own JSON outputs, produced by re-running the
published tools on the actual takes (2026-08-18). File paths inside the JSON are replaced by the take's name.

| file | command | what it shows |
|---|---|---|
| `bounce_tempo_planted_take_approved.json` | `py Tools/bounce_tempo.py <planted take> --json` | bounce run 0.458 s mean interval, spread 1.2×, mean/beat 0.978 → PASS (the "0.458 s · 1.20×" on the case-study page) |
| `bounce_tempo_leglift_take_approved.json` | `py Tools/bounce_tempo.py <leg-lift final take> --json` | bounce run 0.45 s, spread 1.2× → PASS |
| `bounce_tempo_leglift_first_take_rejected.json` | `py Tools/bounce_tempo.py <leg-lift first take> --json` | intervals 0.75 / 0.5 / 0.417 / 0.417 / 0.583 / 0.583 / 0.667 s, spread 1.8× → FAIL (the session-time measurement of the same take read 1.92× with the earlier script; the published tool reads 1.8×) |
| `audio_lineage_A16_vs_world2_track.json` | `py Tools/audio_lineage.py <A-16 render> <World 2 track> --json` | offset 0.000 s, per-second correlation 1.00 in all seven windows → PASS (positive control: the render kept the attached track) |
| `audio_lineage_A17_audioON_vs_world2_track.json` | same, A-17 (fired with model audio ON) | best window 0.86, the rest ≤ 0.32, several negative → FAIL |
| `audio_lineage_A18_audioON_vs_world2_track.json` | same, A-18 (fired with model audio ON) | all windows ≤ 0.41 → FAIL |

The 0.97 → 0.29 series quoted on the page (0.97 / 0.68 / 0.68 / 0.29 / 0.66 / 0.80 / 0.60) is the 2026-08-07
session measurement of an audio-ON edit candidate against its carrier, logged in the commit history; the
session script is not the published tool, and that exact pair is not reproduced here.
