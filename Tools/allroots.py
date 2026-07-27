"""Bass root of every overlay vs the spine. The 808/bass root is what actually
clashes — full-spectrum key detection answers a different question."""
import subprocess, os, numpy as np

SR, NFFT, HOP = 22050, 16384, 4096
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
N = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


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


sr = root(os.path.join(MUS, "E1_MASTER_90.wav"))
print(f"E1 SPINE bass root = {N[sr]}   (fifth = {N[(sr+7)%12]})\n")
print(f"{'world':<10}{'take':<24}{'root':>6}{'semis':>7}  read")

PICKS = [("1 skate", "V4_SKATE_a.mp3"), ("2 bolly", "V3_OV2_BOLLY_b.mp3"),
         ("3 agent", "V3_OV3_AGENT_a.mp3"), ("4 car", "V5_CAR_b.mp3"),
         ("5 sword", "V3_OV5_SWORD_b.mp3"), ("6 runway", "V3_OV6_RUNWAY_b.mp3")]

for lbl, fn in PICKS:
    r = root(os.path.join(MUS, fn))
    d = abs(r - sr)
    d = min(d, 12 - d)
    tag = {0: "MATCH", 5: "fourth - consonant", 7: "fifth - consonant",
           6: "TRITONE - worst possible", 1: "SEMITONE CLASH",
           2: "whole tone - tense", 3: "minor third - usable",
           4: "major third - usable"}.get(d, "")
    print(f"{lbl:<10}{fn:<24}{N[r]:>6}{d:>7}  {tag}")
