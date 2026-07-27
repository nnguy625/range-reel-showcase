"""Linearity gate against the E1 spine.

Franco's cover-architecture test. A take that is genuinely locked to the spine drifts
linearly and negligibly. A take with a structural groove change drifts and cannot be
stretched back — cover architecture died on exactly this: -1326 ms by bar 72, residual
362 ms against a 30 ms threshold.

    PASS = residual after best linear fit < 30 ms.  Otherwise discard, do not stretch.

Also the gate for the untested Suno "Edit instruments" route.

    py lineartest.py <candidate.mp3> [more...]
"""
import subprocess, os, sys, numpy as np

SR, NFFT, HOP = 44100, 2048, 512
BEAT = 60.0 / 128.0
BAR = 4 * BEAT
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
SPINE = "E1_MASTER_90.wav"
THRESH_MS = 30.0


def load(p, hp=None):
    af = [f"highpass=f={hp}"] if hp else []
    a = ["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR)]
    if af:
        a += ["-af", ",".join(af)]
    a += ["-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(a, capture_output=True).stdout,
                         dtype=np.float32).astype(float)


def onset_env(x):
    w = np.hanning(NFFT)
    f = np.fft.rfftfreq(NFFT, 1 / SR)
    band = (f > 40) & (f < 2000)
    S = np.array([np.abs(np.fft.rfft(x[i:i + NFFT] * w))[band].mean()
                  for i in range(0, len(x) - NFFT, HOP)])
    d = np.diff(S, prepend=S[0])
    d[d < 0] = 0
    return d / (d.max() + 1e-12)


def bar_lag(a, b, i, span_s=BAR, search_ms=400):
    """Cross-correlate one bar of the candidate against the spine, return lag in ms."""
    fps = SR / HOP
    n = int(span_s * fps)
    s = int(i * n)
    if s + n > len(a) or s + n > len(b):
        return None
    ea, eb = a[s:s + n], b[s:s + n]
    ea = ea - ea.mean()
    eb = eb - eb.mean()
    m = int(search_ms / 1000 * fps)
    best, bl = -2.0, 0
    for L in range(-m, m + 1):
        sh = np.roll(eb, L)
        v = float(ea @ sh / (np.linalg.norm(ea) * np.linalg.norm(sh) + 1e-12))
        if v > best:
            best, bl = v, L
    return bl / fps * 1000.0


def main():
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    se = onset_env(load(os.path.join(MUS, SPINE), hp=40))
    print(f"linearity gate vs {SPINE}   pass = residual < {THRESH_MS:.0f} ms\n")
    print(f"{'take':<28}{'drift/bar':>11}{'total':>10}{'residual':>10}  verdict")

    for fn in files:
        p = fn if os.path.isabs(fn) else os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{os.path.basename(fn):<28}  MISSING")
            continue
        ce = onset_env(load(p, hp=40))
        nbars = int(min(len(ce), len(se)) / (BAR * SR / HOP))
        xs, ys = [], []
        for i in range(nbars):
            L = bar_lag(se, ce, i)
            if L is not None:
                xs.append(i)
                ys.append(L)
        if len(xs) < 8:
            print(f"{os.path.basename(fn):<28}  too short to fit")
            continue
        xs, ys = np.array(xs, float), np.array(ys, float)
        slope, icept = np.polyfit(xs, ys, 1)
        resid = float(np.sqrt(((ys - (slope * xs + icept)) ** 2).mean()))
        total = slope * (nbars - 1)
        ok = resid < THRESH_MS
        print(f"{os.path.basename(fn):<28}{slope:>10.1f}m{total:>9.0f}m{resid:>9.1f}m  "
              f"{'PASS' if ok else 'DISCARD - not stretchable'}")


if __name__ == "__main__":
    main()
