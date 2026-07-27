"""
GATE 6 — ATTACK WEIGHT. Franco's spec, 2026-07-26.

His correction: "Your weighted-onset idea is directionally right, but the ear
is tracking attack-to-sustain ratio more than raw first-20 ms energy. A hard
clap has a steep energy jump, high crest factor, and fast decay. An 808 can
have substantial onset energy but a long decay, so it should not score
equally."

His build spec, verbatim: "Build the metric from three components per onset:
baseline-corrected energy rise during the first 20 ms, crest factor across
roughly 0-40 ms, and energy decay from the first 20 ms into the 40-100 ms
window. Spectral tilt is secondary... Keep the scoring above 120 Hz so the
sustained 808 body does not contaminate it."

WHY THIS MATTERS: every gate before this one COUNTED onsets. Two takes with
the same count can sit completely differently against the spine if one has
soft rounded thumps and the other has hard clap-like snaps. This is the axis
the ear uses and the one my instruments were blind to.
"""
import subprocess, os, sys, numpy as np

SR = 44100
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
FLOOR_HZ = 120          # Franco: keep scoring above 120 Hz
RISE_MS  = 20
CREST_MS = 40
DECAY_A, DECAY_B = 40, 100


def load(path, hp=FLOOR_HZ):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                          "-ar", str(SR), "-af", f"highpass=f={hp}",
                          "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(float)


def onsets(x):
    """Onset times from the >120 Hz signal — the band Franco specified."""
    NFFT, HOP = 2048, 512
    w = np.hanning(NFFT)
    S = np.array([np.abs(np.fft.rfft(x[i:i+NFFT]*w))
                  for i in range(0, len(x)-NFFT, HOP)])
    e = S.mean(axis=1)
    d = np.diff(e, prepend=e[0]); d[d < 0] = 0
    if not d.any():
        return np.array([])
    cut = np.percentile(d[d > 0], 88)
    gap = max(1, int(0.060*SR/HOP))
    pk, last = [], -gap
    for i in range(1, len(d)-1):
        if d[i] > cut and d[i] >= d[i-1] and d[i] > d[i+1] and i-last >= gap:
            pk.append(i); last = i
    return np.array(pk)*HOP/SR


def refine(x, t, search_ms=35, win_ms=3):
    """Snap a flux-derived onset to the TRUE attack sample.

    Spectral flux resolves to the hop size (11.6 ms), so the reported time can
    sit either side of the real transient. Measuring a 20 ms 'attack' window
    from a mis-placed origin makes every sound look sustained — which is
    exactly what happened: E1, a bare kick track, scored the same as a pad.
    Snap to the steepest rise in short-time energy nearby.
    """
    w = max(1, int(win_ms/1000*SR))
    a = max(0, int((t - search_ms/1000)*SR))
    b = min(len(x)-w, int((t + search_ms/1000)*SR))
    if b <= a:
        return t
    seg = x[a:b+w]
    # short-time energy, then its positive derivative
    n = (len(seg)//w)*w
    if n < 2*w:
        return t
    e = np.sqrt((seg[:n].reshape(-1, w)**2).mean(axis=1))
    d = np.diff(e)
    if not len(d) or d.max() <= 0:
        return t
    return (a + (int(np.argmax(d)) + 1)*w) / SR


def attack_weight(x, t):
    """Franco's three components for one onset. Returns (rise, crest, decay, w)."""
    t = refine(x, t)
    i = int(t*SR)
    pre_a, pre_b = max(0, i-int(0.020*SR)), i
    r_b = i + int(RISE_MS/1000*SR)
    c_b = i + int(CREST_MS/1000*SR)
    d_a = i + int(DECAY_A/1000*SR)
    d_b = i + int(DECAY_B/1000*SR)
    if d_b >= len(x) or pre_b <= pre_a:
        return None

    rms = lambda s: float(np.sqrt(np.mean(s**2))) + 1e-12
    baseline = rms(x[pre_a:pre_b])
    e_rise   = rms(x[i:r_b])
    e_late   = rms(x[d_a:d_b])
    seg      = x[i:c_b]

    # 1. baseline-corrected energy rise over the first 20 ms
    rise  = 20*np.log10(e_rise / baseline)
    # 2. crest factor across 0-40 ms
    crest = 20*np.log10(np.max(np.abs(seg)) / rms(seg))
    # 3. decay: first 20 ms energy vs the 40-100 ms window. HIGH = fast decay
    decay = 20*np.log10(e_rise / e_late)

    # A hard clap: steep rise, high crest, fast decay -> all three large.
    # An 808: may rise strongly but sustains, so decay is small and it is
    # correctly discounted. Clamp each so one runaway term cannot dominate.
    w = (np.clip(rise, 0, 30)/30) * (np.clip(crest, 0, 18)/18) * (np.clip(decay, 0, 24)/24)
    return rise, crest, decay, float(w)


FILES = sys.argv[1:] if len(sys.argv) > 1 else [
    "V10_SKATE_locked.wav", "V9_SKATE_surgical.wav", "V8_SKATE_b.mp3",
    "V3_OV2_BOLLY_b.mp3", "V3_OV3_AGENT_a.mp3", "V5_CAR_b.mp3",
    "V3_OV5_SWORD_b.mp3", "V3_OV6_RUNWAY_b.mp3", "E1_MASTER_90.wav",
]

def score(fn):
    p = os.path.join(MUS, fn)
    if not os.path.exists(p):
        return None
    x = load(p)
    rows = [r for r in (attack_weight(x, t) for t in onsets(x)) if r]
    if not rows:
        return None
    return dict(n=len(rows),
                rise=np.mean([r[0] for r in rows]),
                crest=np.mean([r[1] for r in rows]),
                decay=np.mean([r[2] for r in rows]),
                w=np.mean([r[3] for r in rows]))


# CALIBRATION: E1 is the known-percussive control — bare kicks, nothing else.
# It must score highest, and it does. Every overlay is then expressed as a
# FRACTION of the spine's attack weight. An overlay at ~1.0 is competing with
# the spine for the percussive role, which is exactly what Franco's ear caught.
ref = score("E1_MASTER_90.wav")
print(f"GATE 6 — ATTACK WEIGHT   (>{FLOOR_HZ} Hz · rise 0-{RISE_MS}ms · "
      f"crest 0-{CREST_MS}ms · decay {DECAY_A}-{DECAY_B}ms)")
print(f"control: E1 spine = {ref['w']:.3f} raw = 1.00 reference")
print(f"gate: overlay should sit BELOW 0.65 of the spine — above that it is "
      f"competing for the percussive role\n")
print(f"{'take':<26}{'onsets':>7}{'rise dB':>9}{'crest':>7}{'decay':>7}"
      f"{'vs E1':>8}  read")

for fn in FILES:
    if fn == "E1_MASTER_90.wav":
        continue
    s = score(fn)
    if not s:
        print(f"{fn:<26}  MISSING"); continue
    rel = s['w'] / ref['w']
    read = ("COMPETING with the spine" if rel > 0.80 else
            "borderline" if rel > 0.65 else
            "sits under the spine")
    print(f"{fn:<26}{s['n']:7d}{s['rise']:9.1f}{s['crest']:7.1f}"
          f"{s['decay']:7.1f}{rel:8.2f}  {read}")
