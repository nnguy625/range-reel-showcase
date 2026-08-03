# W2 AUDIO MAP — V16_BOLLY_a windowing (LOCKED 2026-08-03)

Source: `Assets/Music/V16_BOLLY_a.mp3` · 24.040s · autocorrelates 127.00 BPM · 0.0% silence.

## THE WINDOW

```
W2 world  =  source 7.400 -> 22.400  =  15.000s EXACTLY
```

| | source | reel | rms | low% | |
|---|---|---|---|---|---|
| **W2 frame 0** | 7.400 | 15.000 | 0.1200 | 11.4 | first low-end arrival — carries the W1 kickflip landing |
| **W2 clip 2** | 14.900 | 22.500 | 0.2239 | 20.0 | largest internal escalation |
| **W3 frame 0** | **22.400** | **30.000** | **0.3477→0.3748** | **17→60** | **THE SLAM** |

## WHY 22.400 AND NOT FRANCO'S 22.460

Franco picked 22.460 by ear and ruled *"the track stays hot; cut dry and let W3 supply the impact."*
Nelson pushed back: *"I don't feel there's a natural drop or transition opportunity."* He was right.
A 50ms fine scan found the track does **not** stay hot — it has a real drop:

```
22.000s  rms 0.0557  low  0.2%
22.050s  rms 0.0178  low 10.8%   <- 100ms HOLE, 6x drop. the breath.
22.100s  rms 0.0206  low 33.3%
22.150s  rms 0.1452
22.400s  rms 0.3477  low 17.3%   <- SLAM
22.450s  rms 0.3748  low 46.1%
22.500s  rms 0.3534  low 59.8%   <- sub-bass at 60%
```

**22.460 lands 40ms INSIDE the transient** — you get the attack and lose the body. 22.400 puts
W3's first frame on the slam, with the 100ms hole sitting in W2's last half-second as the breath.
Front cost of the 60ms shift: **zero** (7.400 = 0.1200/11.4% vs 7.460 = 0.1189/11.2%).

**Climax runs 22.400–24.040 = 1.640s of usable slam past the seam.** W3's opening rides it.

## FILES — `Assets/Music/AUDIO_CARRIERS/`

| file | dur | use |
|---|---|---|
| `W2_WORLD_15s_V16_7400.wav` | 15.000 | stereo master for the edit |
| `CARRIER_W2_CLIP1_V16_7400_8s.wav` | 8.000 | **SD2 attachment, clip 1** |
| `CARRIER_W2_CLIP2_V16_14900_8s.wav` | 8.000 | SD2 attachment, clip 2 |
| `W3_ENTRY_SLAM_from_22400.wav` | 1.640 | the W3 entry impact |

Superseded 7.460 versions → `Assets/Music/_TO_DELETE_VERIFY/`. Nothing deleted.

## WHY THE CLICK IS RETIRED

| | `GUIDE_CLICK_W2_CLIP1_8s.wav` | `CARRIER_W2_CLIP1_V16_7400_8s.wav` |
|---|---|---|
| silence | **93.0%** | **0.0%** |
| events | 16 × **7.0 ms** | continuous |
| sub/low | **1.0%** | **13.2%** |
| RMS | 0.0257 | 0.1300 |

Franco: *"The click was effectively an empty file with microscopic transients. This track supplies
continuous energy, low-frequency body and clear phrase structure, so it is **the first legitimate
audio-conditioning test.**"*

## OPEN — the internal clock

Across A-3/A-4/A-5, motion accents land on exact thirds of a second and on whole seconds.
vs our 128 grid: 17% / 13% within one frame (chance 18%). **Density is promptable; phase is not.**
Whether real music moves the phase is what the next fire tests.
