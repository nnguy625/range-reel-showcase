"""THE PITCHED-TRANSIENT ALLOWANCE — Franco's ratified rule, 2026-07-27.

Supersedes w6exception.py, which scoped this to World 6. Franco generalised it:

    "World 4 gets the same allowance, but document it as a MATERIAL-TYPE rule, not
     a World 4 or World 6 exception. Call it the pitched-transient allowance. A take
     may exceed the normal 0.75 mid-band ceiling up to 1.15 when ALL of these are
     true: low-band activity is minimal, flams stay below 5%, the harmony is
     compatible, and the counted attacks form one pitched musical voice rather than
     multiple drum or percussion layers."

And he refined the low-band test, correcting an overclaim of mine:

    "0.12 low-band onsets per second does not prove V5 carried a second kick. That
     is only about one low event every 8.3 seconds. A true competing quarter-note
     kick would be around 2.13 events per second at 128 BPM."

    "Raw low-band onset rate alone should not define a second skeleton. Add a
     PERIODICITY condition: fail only when low attacks repeat consistently at one
     fixed beat phase across the eight-bar section. Occasional syncopated 808
     accents are allowed; a recurring kick on every beat, half-bar, or bar is not."

So the low band fails on RHYTHM, not on COUNT. 0.12/s is ~18x below a real kick.

Finally, gate the SLICE, not the file:

    "Choose the exact strongest eight-bar, 15-second window and rerun every gate on
     that selected slice, not only on the full take."

    py pitchedtransient.py V25_CAR_b.mp3
"""
import os, sys, subprocess, numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from buildmaster3 import load, spec, events, best_offset, MUS, SR, NFFT, BAR, WORLD  # noqa: E402
from bassroot import root_windows, N as NOTE                                          # noqa: E402

BEAT = 60.0 / 128.0
_f = np.fft.rfftfreq(NFFT, 1 / SR)
LOW = (_f > 40) & (_f < 120)
MID = (_f > 300) & (_f < 2000)

MID_NORMAL = 0.75          # the ordinary ceiling
MID_ALLOWANCE = 1.15       # the pitched-transient allowance
FLAM_CEIL = 5.0
PHASE_CONC_FAIL = 0.75     # circular concentration above this = one fixed beat phase
MIN_LOW_FOR_PERIODICITY = 6   # below this, too few events to call it a skeleton


def onsets(S, band):
    e = S[:, band].mean(axis=1)
    d = np.diff(e, prepend=e[0])
    d[d < 0] = 0
    r = d / (e + 1e-9)
    return np.array([i for i in range(1, len(d) - 1)
                     if r[i] > 0.8 and d[i] >= d[i - 1] and d[i] > d[i + 1]]) * 512 / SR


def strongest_window(x):
    """Franco: 'the exact strongest eight-bar, 15-second window'. Slide in whole-bar
    steps and take the window with the highest mid-band attack energy — the section
    that actually carries the world, not an arbitrary head slice."""
    dur = len(x) / SR
    if dur <= WORLD + 0.01:
        return 0.0, dur
    S = spec(x)
    fps = SR / 512
    e = S[:, MID].mean(axis=1)
    d = np.diff(e, prepend=e[0])
    d[d < 0] = 0
    best_t, best_v = 0.0, -1.0
    t = 0.0
    while t + WORLD <= dur:
        a, b = int(t * fps), int((t + WORLD) * fps)
        v = float(d[a:b].sum())
        if v > best_v:
            best_v, best_t = v, t
        t += BAR
    return best_t, best_t + WORLD


def low_periodicity(times):
    """Franco's condition: fail only when low attacks repeat at ONE FIXED beat phase.
    Returns (concentration, verdict_text). Occasional syncopation is fine."""
    if len(times) < MIN_LOW_FOR_PERIODICITY:
        return 0.0, f"sparse ({len(times)} events) - not a skeleton"
    phase = (np.asarray(times) % BEAT) / BEAT * 2 * np.pi
    conc = float(abs(np.exp(1j * phase).mean()))     # 0 = scattered, 1 = one fixed phase
    if conc >= PHASE_CONC_FAIL:
        return conc, "RECURRING KICK - one fixed beat phase"
    return conc, "syncopated / scattered - allowed"


def main():
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    print("PITCHED-TRANSIENT ALLOWANCE (Franco 07-27) - gated on the strongest 8-bar slice")
    print(f"mid <= {MID_ALLOWANCE} (normal {MID_NORMAL}) AND flams < {FLAM_CEIL}% "
          f"AND harmony compatible AND low band not a recurring kick\n")

    spine = load(os.path.join(MUS, "E1_MASTER_90.wav"))
    sp_all = events(spec(spine))
    sp = sp_all[sp_all < WORLD]

    for fn in files:
        p = fn if os.path.isabs(fn) else os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{os.path.basename(fn)}: MISSING")
            continue

        xf = load(p, hp=100)
        t0, t1 = strongest_window(xf)
        sl = xf[int(t0 * SR):int(t1 * SR)]
        S = spec(sl)
        dur = len(sl) / SR
        mid = len(onsets(S, MID)) / dur

        xl = load(p)[int(t0 * SR):int(t1 * SR)]
        lows = onsets(spec(xl), LOW)
        low_rate = len(lows) / dur
        conc, low_read = low_periodicity(lows)

        # Flams are PLACEMENT, not content. The sweep needs room either side, so
        # measure on the slice PLUS a margin and let best_offset find the minimum.
        # Extracting exactly 15.000s and sweeping inside it leaves zero room and
        # silently reports the bar-snapped number (51.5% vs a true 0.0% on V25_b).
        MARGIN = 2 * (BEAT / 4)                       # +/-234 ms, the widened sweep
        fa = max(0.0, t0 - MARGIN)
        fb = min(len(xf) / SR, t1 + MARGIN)
        fx = xf[int(fa * SR):int(fb * SR)]
        fev = events(spec(fx))
        fdur = len(fx) / SR
        centre = t0 - fa                              # where the chosen slice starts
        flams, _ = best_offset(fev, sp, centre, fdur) if len(fev) else (None, 0)

        r, frac, _ = root_windows(p)
        root = NOTE[r] if r is not None else "?"

        ok_mid = mid <= MID_ALLOWANCE
        ok_flam = flams is not None and flams < FLAM_CEIL
        ok_low = "RECURRING" not in low_read
        verdict = ("LOCK - passes the allowance" if (ok_mid and ok_flam and ok_low)
                   else "FAIL: " + ", ".join(
                       ([] if ok_mid else [f"mid {mid:.2f}>{MID_ALLOWANCE}"]) +
                       ([] if ok_flam else ["flams"]) +
                       ([] if ok_low else ["recurring low kick"])))

        print(f"{os.path.basename(fn)}")
        print(f"   strongest slice   {t0:6.3f} - {t1:6.3f} s   ({(t1-t0):.3f}s)")
        print(f"   mid-band          {mid:.2f}/s   {'within allowance' if ok_mid else 'OVER'}"
              f"{'  (also under the normal 0.75)' if mid <= MID_NORMAL else ''}")
        print(f"   low-band          {low_rate:.2f}/s   phase-conc {conc:.2f}   {low_read}")
        print(f"   flams             {flams if flams is None else round(flams,1)}%")
        print(f"   harmony           root {root}, {frac:.0%} window-stable"
              f"   ({'manual harmonic pass required' if frac < 0.75 else 'automated'})")
        print(f"   VERDICT           {verdict}\n")

    print(f"reference: a true competing quarter-note kick at 128 BPM is ~2.13 low events/s.")


if __name__ == "__main__":
    main()
