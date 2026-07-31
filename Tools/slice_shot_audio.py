"""Slice a per-shot SD2 audio ref from the E1 spine, with a 1-bar pre-roll.

Usage:  py Tools/slice_shot_audio.py <world 1-6> <start_bar 1-8> <bars>
        py Tools/slice_shot_audio.py 3 4 3     -> W3, bars 4-6 of its 8, +1 bar preroll

Grid: 128 BPM, 4/4 -> 1 bar = 1.875 s, world = 8 bars = 15.000 s.
Pre-roll: 1 bar BEFORE the shot (Franco: mandatory, also clears SD2's 2 s audio floor).
SD2 audio refs cap at 15 s total (community-reported, verify on the 720 test day) --
this script refuses to emit a slice longer than 15 s.

Calibration control: world 1, start_bar 1, bars 8 must report src 0.000 len 15.000
(no preroll exists before 0) and emit a file ffprobe measures at 15.000000 s.

Source: Assets/Music/E1_MASTER_90.wav (the stripped guide -- NEVER the premaster;
Franco: "the model needs fence posts, not stained glass").
Output: Assets/Music/SD2_GUIDE_REFS/W{w}_S{start}-{end}_guide.wav
"""
import subprocess, sys, os

BAR = 1.875
ROOT = os.path.join(os.path.dirname(__file__), "..", "Assets", "Music")
SRC = os.path.join(ROOT, "E1_MASTER_90.wav")
OUT = os.path.join(ROOT, "SD2_GUIDE_REFS")

def main():
    w, start_bar, bars = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    assert 1 <= w <= 6 and 1 <= start_bar <= 8 and 1 <= bars <= 8, "world 1-6, start_bar 1-8, bars 1-8"
    world_t0 = (w - 1) * 15.0
    shot_t0 = world_t0 + (start_bar - 1) * BAR
    src_t0 = max(0.0, shot_t0 - BAR)              # 1-bar preroll, floored at file start
    length = (shot_t0 - src_t0) + bars * BAR
    assert length <= 15.0, f"slice {length:.3f}s exceeds the 15s SD2 audio cap - split the shot"
    os.makedirs(OUT, exist_ok=True)
    name = f"W{w}_S{start_bar}-{start_bar + bars - 1}_guide.wav"
    dst = os.path.join(OUT, name)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", SRC,
                    "-ss", f"{src_t0:.3f}", "-t", f"{length:.3f}",
                    "-c:a", "pcm_s16le", dst], check=True)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", dst], capture_output=True, text=True).stdout.strip()
    print(f"{name}  src {src_t0:.3f}  len {length:.3f}  ffprobe {dur}")

if __name__ == "__main__":
    main()
