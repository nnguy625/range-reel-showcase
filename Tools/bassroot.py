"""Bass root of one or more files against the E1 spine.

    CALIBRATION STATE, 2026-07-27 — read before trusting the stability column.

    Franco's ruling: root is an EARLY gate, applied only when stable across >=75%
    of two-bar windows; stable F passes, stable F#/B fails immediately, and an
    unstable estimate goes to MANUAL HARMONIC REVIEW rather than auto-reject.

    Measured against the known controls:
      V16_BOLLY_a  (Franco LOCKED)   F   100%  PASS      <- correct
      V21_RUNWAY_a                   F    90%  PASS      <- correct
      V20_RUNWAY_a                   F#   75%  FAIL      <- correctly caught
      V10_SKATE_locked (LOCKED)      F    69%  review
      V12_SWORD_locked (passes)      F    57%  review
      V18_AGENT_b      (LOCKED)      F    53%  review

    The two ends behave correctly. The middle does not discriminate: three takes
    Franco has approved land in manual review, because these overlays are sparse
    and many two-bar windows carry almost no bass to vote with. Windows below 25%
    of the file's median bass energy are already excluded; without that filter
    EVERY take read unstable at 56-67%, including both locked references.

    So: trust PASS and FAIL. Treat "review" as "not enough bass to call it",
    not as a defect in the take. Franco set the 75% figure - my windowing may not
    match what he had in mind, and that is worth asking him before this gate is
    allowed to block anything.


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


# --- Franco's stability gate, 2026-07-27 -----------------------------------
# "Apply the gate only when the result is stable across at least 75 percent of
#  two-bar windows. Stable F passes. Stable F-sharp or B fails immediately. If
#  the root estimate is unstable because the overlay has little low-frequency
#  information, send it to manual harmonic review instead of auto-rejecting it."
BAR = 4 * 60.0 / 128.0
WIN = 2 * BAR              # 3.75 s
STABLE_FRAC = 0.75


def root_windows(p):
    """Root per two-bar window. Returns (modal_root, stable_fraction, n_windows)."""
    chans = [(lo, hi, load(p, lo, hi)) for lo, hi in [(30, 80), (40, 160)]]
    n = int(min(len(x) for _, _, x in chans) / SR / WIN)
    if n < 2:
        return None, 0.0, n
    votes, energies = [], []
    step = int(WIN * SR)
    for w in range(n):
        acc = np.zeros(12)
        e = 0.0
        for lo, hi, x in chans:
            seg = x[w * step:(w + 1) * step]
            acc += hist(seg, lo, hi)
            e += float((seg ** 2).sum())
        votes.append(int(np.argmax(acc)))
        energies.append(e)
    votes, energies = np.array(votes), np.array(energies)

    # Only windows carrying real bass may vote. A sparse overlay has windows with
    # almost no low-frequency content, and those vote on noise - which made every
    # take, including Franco's two locked references, read "unstable" at 56-67%.
    # Franco: "if the root estimate is unstable because the overlay has little
    # low-frequency information, send it to manual harmonic review."  That is
    # about the WHOLE take, not about silent windows inside a good ***REMOVED***
    keep = energies >= 0.25 * np.median(energies[energies > 0]) if (energies > 0).any() else energies > 0
    if keep.sum() < 2:
        return None, 0.0, n
    v = votes[keep]
    modal = int(np.bincount(v, minlength=12).argmax())
    return modal, float((v == modal).mean()), int(keep.sum())


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    sr = root(os.path.join(MUS, SPINE))
    print(f"E1 SPINE bass root = {N[sr]}   (fifth = {N[(sr + 7) % 12]})")
    print(f"gate applies only when the root is stable across >= {STABLE_FRAC:.0%} of two-bar windows\n")
    print(f"{'take':<28}{'root':>6}{'semis':>7}{'stable':>8}  verdict")
    for fn in files:
        p = fn if os.path.isabs(fn) else os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{os.path.basename(fn):<28}  MISSING")
            continue
        r, frac, nwin = root_windows(p)
        if r is None:
            print(f"{os.path.basename(fn):<28}  too short to window")
            continue
        d = abs(r - sr)
        d = min(d, 12 - d)
        if frac < STABLE_FRAC:
            verdict = "MANUAL HARMONIC REVIEW - root unstable, do not auto-reject"
        elif d == 0:
            verdict = "PASS"
        elif d in (1, 6):
            verdict = f"FAIL - {READ[d]}"
        else:
            verdict = READ.get(d, "")
        print(f"{os.path.basename(fn):<28}{N[r]:>6}{d:>7}{frac:>8.0%}  {verdict}")
