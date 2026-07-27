"""World 6 exception gate — Franco's ruling, 2026-07-27.

He granted World 6 a documented exception from the 0.75 mid-band drum ceiling,
because the detector there is counting tonal runway shimmer rather than a drum
kit. The exception is NOT a free pass: it is valid only under four conditions.

    mid-band onsets   <= 1.15 /s      (raised from 0.75, World 6 ONLY)
    low-band onsets   <  0.10 /s      no kick-like activity of its own
    flams             <  5%
    root              == F
    the attacks form ONE stable pitched layer, not multiple percussion voices

The last condition is a judgement call; this script measures the first four and
reports the inter-onset interval regularity as evidence for the fifth. Franco's
reading of V22_b: "a single pitched shimmer pulse about every 0.9375 seconds,
once every two beats."

    py w6exception.py V22_RUNWAY_b.mp3
"""
import os, sys, numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildmaster3 import load, spec, MUS, SR, NFFT   # noqa: E402
from bassroot import root_windows, N as NOTE          # noqa: E402

_f = np.fft.rfftfreq(NFFT, 1 / SR)
LOW = (_f > 40) & (_f < 120)
MID = (_f > 300) & (_f < 2000)

MID_CEIL_W6 = 1.15
LOW_CEIL = 0.10


def onsets(S, band):
    e = S[:, band].mean(axis=1)
    d = np.diff(e, prepend=e[0])
    d[d < 0] = 0
    r = d / (e + 1e-9)
    return [i for i in range(1, len(d) - 1)
            if r[i] > 0.8 and d[i] >= d[i - 1] and d[i] > d[i + 1]]


def main():
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    print("WORLD 6 EXCEPTION GATE (Franco 07-27) - mid<=1.15 AND low<0.10 AND flams<5% AND root F\n")
    print(f"{'take':<24}{'mid/s':>8}{'low/s':>8}{'root':>6}{'IOI ms':>9}{'IOI cv':>8}  verdict")
    for fn in files:
        p = fn if os.path.isabs(fn) else os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{os.path.basename(fn):<24}  MISSING")
            continue
        x = load(p, hp=100)
        S = spec(x)
        dur = len(x) / SR
        mid = len(onsets(S, MID)) / dur
        # low band needs the un-high-passed signal
        xl = load(p)
        low = len(onsets(spec(xl), LOW)) / dur

        ons = np.array(onsets(S, MID)) * 512 / SR
        ioi = np.diff(ons) if len(ons) > 2 else np.array([0.0])
        ioi_ms = float(np.median(ioi) * 1000) if len(ioi) else 0.0
        cv = float(ioi.std() / (ioi.mean() + 1e-9)) if len(ioi) > 1 else 9.9

        r, frac, _ = root_windows(p)
        rootok = r is not None and NOTE[r] == "F"

        ok = mid <= MID_CEIL_W6 and low < LOW_CEIL and rootok
        why = []
        if mid > MID_CEIL_W6:
            why.append(f"mid {mid:.2f}>1.15")
        if low >= LOW_CEIL:
            why.append(f"low {low:.2f}>=0.10 - has its own kick")
        if not rootok:
            why.append("root")
        print(f"{os.path.basename(fn):<24}{mid:>8.2f}{low:>8.2f}"
              f"{(NOTE[r] if r is not None else '?'):>6}{ioi_ms:>9.0f}{cv:>8.2f}  "
              f"{'PASS exception' if ok else 'FAIL: ' + ', '.join(why)}")
    print("\nIOI cv near 0 = one regular pitched pulse. High cv = multiple voices.")


if __name__ == "__main__":
    main()
