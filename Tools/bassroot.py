"""Bass root of one or more files against the E1 spine.

The 808/bass root is what actually collides. A full-spectrum key check answers a
different question and flagged five takes when only two were bad — do not act on it.

    E1 spine bass root = F  (fifth = C)

    py bassroot.py V11_SWORD_a.mp3 [more...]
"""
import subprocess, os, sys, numpy as np

SR, NFFT, HOP = 22050, 16384, 4096
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
SPINE = "E1_MASTER_90.wav"
N = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

READ = {0: "MATCH", 1: "SEMITONE CLASH", 2: "whole tone - tense",
        3: "minor third - usable", 4: "major third - usable",
        5: "fourth - consonant", 6: "TRITONE - worst possible"}


def load(p, lo, hi):
    a = ["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR),
         "-af", f"highpass=f={lo},lowpass=f={hi}", "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(a, capture_output=True).stdout,
                         dtype=np.float32).astype(float)


def hist(x, lo, hi):
    w = np.hanning(NFFT)
    f = np.fft.rfftfreq(NFFT, 1 / SR)
    ok = (f > lo) & (f < hi)
    pc = np.round(69 + 12 * np.log2(f[ok] / 440.0)).astype(int) % 12
    acc = np.zeros(12)
    for i in range(0, max(1, len(x) - NFFT), HOP):
        S = np.abs(np.fft.rfft(x[i:i + NFFT] * w)) ** 2
        s = S[ok]
        for k in range(12):
            acc[k] += s[pc == k].sum()
    return acc / (acc.sum() + 1e-12)


def root(p):
    t = np.zeros(12)
    for lo, hi in [(30, 80), (40, 160)]:
        t += hist(load(p, lo, hi), lo, hi)
    return int(np.argmax(t))


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    sr = root(os.path.join(MUS, SPINE))
    print(f"E1 SPINE bass root = {N[sr]}   (fifth = {N[(sr + 7) % 12]})\n")
    print(f"{'take':<28}{'root':>6}{'semis':>7}  read")
    for fn in files:
        p = fn if os.path.isabs(fn) else os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{os.path.basename(fn):<28}  MISSING")
            continue
        r = root(p)
        d = abs(r - sr)
        d = min(d, 12 - d)
        print(f"{os.path.basename(fn):<28}{N[r]:>6}{d:>7}  {READ.get(d, '')}")
