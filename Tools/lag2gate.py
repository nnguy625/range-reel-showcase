"""Lag-2 spectral gate — Franco's two-bar QA (locked 2026-07-26).

    #############################################################################
    ##  UNVALIDATED REBUILD — DO NOT MAKE DECISIONS ON THESE NUMBERS.          ##
    #############################################################################

    The original lag2gate.py was lost in the 07-27 crash. This is a reconstruction
    from the two-sentence spec in Docs/STATE.md, and it FAILS the calibration
    control, so by our own law (a metric that cannot separate a known control is
    broken) it is not yet an instrument.

    Recorded originals          this rebuild
      skate  lag2 0.636 d+0.272   lag2 0.509 d+0.103   closest, still off
      bolly  lag2 0.817 d+0.139   lag2 0.499 d-0.052   wrong sign
      the four manual-review takes: lag-1 recorded 0.85-0.89, rebuild 0.31-0.57

    Three attempts, each differing in kind, all failed to reproduce it:
      1. averaged log-mel per bar, mean-centred      -> everything ~0.51-0.57
      2. time-resolved log-mel, not centred          -> everything ~0.87-0.95
      3. time-resolved spectral flux, centred        -> current; skate close, rest not

    The spec underdetermines the implementation (band count, compression,
    normalization order, whether bars are onset-aligned). Rebuilding it properly
    needs a fresh derivation with Franco, not more guessing.

    WHAT TO USE MEANWHILE: the lag-2 results for all six current picks are already
    recorded in Docs/STATE.md and did not need re-measuring. And Franco's rule is
    that missing this gate is MANUAL-REVIEW, never auto-reject — Nelson's ear is
    the decider. So this gate is advisory and nothing is blocked on it.


Replaces onset-envelope self-similarity, which measured LOUDNESS. This measures TONE.

Method: bar-normalized log-mel spectral contour, everything below 120 Hz excluded,
each bar normalized to the same RMS, cosine-compare bar n vs n+1 and bar n vs n+2.

    PASS = lag-2 >= 0.60 AND (lag-2 - lag-1) >= 0.08

Missing it is MANUAL-REVIEW, not auto-reject. If it sounds call-and-response by ear,
it passes. Nelson's ear is the decider.

    py lag2gate.py V12_SWORD_locked.wav [more...]
"""
import subprocess, os, sys, numpy as np

SR, NFFT, HOP = 44100, 2048, 512
BEAT = 60.0 / 128.0
BAR = 4 * BEAT              # 1.875 s
FLOOR_HZ = 120.0            # the bass is excluded on purpose - it is not the tone
NBANDS = 40
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"

PASS_LAG2 = 0.60
PASS_DELTA = 0.08


def load(p, sr=SR):
    a = ["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(sr),
         "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(a, capture_output=True).stdout,
                         dtype=np.float32).astype(float)


def spec(x):
    w = np.hanning(NFFT)
    return np.array([np.abs(np.fft.rfft(x[i:i + NFFT] * w))
                     for i in range(0, len(x) - NFFT, HOP)])


def filterbank():
    """Log-spaced triangular bands from FLOOR_HZ up. No librosa dependency."""
    f = np.fft.rfftfreq(NFFT, 1 / SR)
    edges = np.geomspace(FLOOR_HZ, 8000.0, NBANDS + 2)
    fb = np.zeros((NBANDS, len(f)))
    for k in range(NBANDS):
        lo, mid, hi = edges[k], edges[k + 1], edges[k + 2]
        up = (f >= lo) & (f <= mid)
        dn = (f > mid) & (f <= hi)
        fb[k, up] = (f[up] - lo) / max(mid - lo, 1e-9)
        fb[k, dn] = (hi - f[dn]) / max(hi - mid, 1e-9)
    return fb


FB = filterbank()


SLOTS = 16                                     # sixteenth-note grid, one bar


def bar_contours(x):
    """One TIME-RESOLVED log-mel contour per bar: SLOTS x NBANDS, flattened,
    each bar normalized to the same RMS.

    The contour must keep its time axis. Collapsing a bar to a single averaged
    spectrum scores every take at ~0.98 and cannot separate a one-bar loop from a
    two-bar hook - which is the only thing this gate exists to do. Do not
    mean-centre either; that overshoots the other way to ~0.55.
    """
    S = spec(x)
    M = np.log1p(S @ FB.T)                     # frames x NBANDS
    # per-band spectral FLUX, not raw energy. Raw energy keeps every take pinned
    # at 0.87-0.95 (all-positive vectors) and cannot separate the controls.
    F = np.diff(M, axis=0, prepend=M[:1])
    F[F < 0] = 0
    fps = SR / HOP
    per = int(round(BAR * fps))
    n = len(F) // per
    out = []
    for b in range(n):
        blk = F[b * per:(b + 1) * per]
        # resample the bar onto a fixed sixteenth grid so bars are comparable
        idx = np.linspace(0, len(blk), SLOTS + 1).astype(int)
        v = np.concatenate([blk[idx[s]:max(idx[s] + 1, idx[s + 1])].mean(axis=0)
                            for s in range(SLOTS)])
        v = v - v.mean()
        r = np.sqrt((v ** 2).mean())
        out.append(v / (r + 1e-9))             # same RMS for every bar
    return np.array(out)


def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


def measure(path):
    C = bar_contours(load(path))
    if len(C) < 3:
        return None
    l1 = np.mean([cos(C[i], C[i + 1]) for i in range(len(C) - 1)])
    l2 = np.mean([cos(C[i], C[i + 2]) for i in range(len(C) - 2)])
    return l1, l2, len(C)


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    print(f"lag-2 gate  |  pass = lag2 >= {PASS_LAG2:.2f} AND (lag2 - lag1) >= {PASS_DELTA:.2f}")
    print("miss = MANUAL REVIEW, never auto-reject\n")
    print(f"{'take':<28}{'bars':>5}{'lag-1':>8}{'lag-2':>8}{'delta':>8}  verdict")
    for fn in files:
        p = fn if os.path.isabs(fn) else os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{os.path.basename(fn):<28}  MISSING")
            continue
        r = measure(p)
        if r is None:
            print(f"{os.path.basename(fn):<28}  too short")
            continue
        l1, l2, nb = r
        d = l2 - l1
        ok = l2 >= PASS_LAG2 and d >= PASS_DELTA
        print(f"{os.path.basename(fn):<28}{nb:>5}{l1:>8.3f}{l2:>8.3f}{d:>+8.3f}  "
              f"{'PASS' if ok else 'manual-review'}")
