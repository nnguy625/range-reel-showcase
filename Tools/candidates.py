"""Run EVERY candidate in the working folder through all three numeric gates.

This is how the six picks were chosen — not by ear-first, but by gating every a/b pair
and letting Nelson's ear decide only among the passers.

    gates   drums <= 0.75 onsets/s (mid 300-2k)
            flams <= 5% swept +/-117 ms, widened once to +/-234 ms
            bass root = F, or a consonant relation to it

Superseded takes in _TO_DELETE_VERIFY/ are skipped. The spine and _CALIBRATION/ are
never candidates.

    py candidates.py            all live takes
    py candidates.py SWORD      only takes matching a substring
"""
import os, sys, glob, numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bassroot import root as bass_root, N as NOTE, READ           # noqa: E402
from buildmaster3 import (load, spec, events, best_offset,        # noqa: E402
                          MUS, SPINE, BAR, WORLD, SIX)

SR = 44100
NFFT = 2048
_f = np.fft.rfftfreq(NFFT, 1 / SR)
MID = (_f > 300) & (_f < 2000)

DRUM_CEIL = 0.75
FLAM_CEIL = 5.0
SKIP = {"E1_MASTER_90.wav", "E1_SPINE_90.mp3"}


def strict(S):
    """The strict drum detector. It gates for a DRUM KIT — it CANNOT measure density
    and must never be used to reject energy."""
    e = S[:, MID].mean(axis=1)
    d = np.diff(e, prepend=e[0])
    d[d < 0] = 0
    r = d / (e + 1e-9)
    return sum(1 for i in range(1, len(d) - 1)
               if r[i] > 0.8 and d[i] >= d[i - 1] and d[i] > d[i + 1])


def main():
    filt = sys.argv[1].upper() if len(sys.argv) > 1 else None

    spine_root = bass_root(os.path.join(MUS, SPINE))
    sp_all = events(spec(load(os.path.join(MUS, SPINE))))
    sp = sp_all[sp_all < WORLD]

    files = sorted(glob.glob(os.path.join(MUS, "*.mp3")) +
                   glob.glob(os.path.join(MUS, "*.wav")))
    files = [f for f in files if os.path.basename(f) not in SKIP
             and not os.path.basename(f).startswith("MASTER_")]
    if filt:
        files = [f for f in files if filt in os.path.basename(f).upper()]

    print(f"spine bass root {NOTE[spine_root]}   |  drums<={DRUM_CEIL}/s  "
          f"flams<={FLAM_CEIL}%  root={NOTE[spine_root]}\n")
    print(f"{'take':<28}{'drums/s':>9}{'flams':>8}{'root':>6}{'semis':>7}  verdict")

    passing = []
    for p in files:
        fn = os.path.basename(p)
        x = load(p, hp=100)
        S = spec(x)
        dur = len(x) / SR
        drums = strict(S) / dur

        ev = events(S)
        centre = float(np.ceil(ev[0] / BAR) * BAR) if len(ev) else 0.0
        if centre + WORLD > dur:
            centre = max(0.0, dur - WORLD - 2 * SIX - 0.01)
        flams, _ = best_offset(ev, sp, centre, dur)

        r = bass_root(p)
        d = abs(r - spine_root)
        d = min(d, 12 - d)

        ok = (drums <= DRUM_CEIL and flams is not None and flams <= FLAM_CEIL
              and d <= 4 and d != 1)
        fl = f"{flams:.1f}%" if flams is not None else "n/a"
        why = ""
        if drums > DRUM_CEIL:
            why = "drums"
        elif flams is None or flams > FLAM_CEIL:
            why = "flams"
        elif d == 6:
            why = "TRITONE"
        elif d == 1:
            why = "semitone clash"
        elif d > 4:
            why = "root"
        print(f"{fn:<28}{drums:8.2f} {fl:>7}{NOTE[r]:>6}{d:>7}  "
              f"{'PASS' if ok else 'FAIL ' + why}")
        if ok:
            passing.append(fn)

    print(f"\n{len(passing)}/{len(files)} pass all three gates")
    for f in passing:
        print(f"  {f}")


if __name__ == "__main__":
    main()
