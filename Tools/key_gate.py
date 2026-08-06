"""
KEY GATE — Franco's three-part confidence gate, 2026-08-05.

A key measurement is only allowed to DECIDE anything if all three hold:
  1. WINDOW STABILITY  the same tonic family wins in >= 70% of two-bar windows
  2. SEPARATION        the winning key correlation beats the runner-up by >= 0.10
  3. TONAL EVIDENCE    multiple sustained/pitched events support the tonic;
                       a percussion-dominant passage is labelled AMBIGUOUS, never assigned

Built because a root detector at 53% window stability once produced a false
World 6 clash, and because the reverse error — rejecting a good take on a bad
measurement — is just as expensive.

Relative major/minor are folded into one family: they share every pitch class,
so C major and A minor are the SAME family. Bass and cadence decide the mode,
not the chromagram, and this tool does not pretend otherwise.

Spine = A minor (E1). Two bars at 128 BPM = 3.750s.
"""
import sys
import numpy as np

sys.path.insert(0, 'Tools')
from w2_clip2_carrier_audit import read

PITCH = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
KS_MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KS_MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
TWO_BARS = 3.750


def chroma(x, sr, hop=2048, win=8192, fmin=55.0, fmax=2000.0):
    """Pitch-class energy profile per frame."""
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1 / sr)
    band = (freqs >= fmin) & (freqs <= fmax)
    f = freqs[band]
    pc = np.round(12 * np.log2(np.maximum(f, 1e-9) / 440.0) + 69).astype(int) % 12
    frames = 1 + (len(x) - win) // hop
    out = np.zeros((frames, 12))
    for i in range(frames):
        S = np.abs(np.fft.rfft(x[i * hop:i * hop + win] * w))[band]
        for p in range(12):
            out[i, p] = S[pc == p].sum()
    t = (np.arange(frames) * hop + win / 2) / sr
    return out, t


def best_key(vec):
    """Correlate a 12-vector against all 24 KS profiles. Returns ranked list."""
    v = vec - vec.mean()
    if np.linalg.norm(v) < 1e-9:
        return []
    scores = []
    for tonic in range(12):
        for name, prof in (('maj', KS_MAJ), ('min', KS_MIN)):
            p = np.roll(prof, tonic)
            p = p - p.mean()
            r = float(np.dot(v, p) / (np.linalg.norm(v) * np.linalg.norm(p) + 1e-12))
            scores.append((r, f'{PITCH[tonic]} {name}'))
    scores.sort(reverse=True)
    return scores


def family(label):
    """Fold relative major/minor into one family, named by its minor tonic."""
    tonic, mode = label.split()
    i = PITCH.index(tonic)
    rel_min = i if mode == 'min' else (i + 9) % 12
    return PITCH[rel_min] + ' family'


def tonal_evidence(x, sr):
    """Fraction of frames where pitched (300-2000Hz) energy beats percussive (30-160Hz)."""
    hop, win = 2048, 4096
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1 / sr)
    lo = (freqs >= 30) & (freqs < 160)
    mid = (freqs >= 300) & (freqs < 2000)
    frames = 1 + (len(x) - win) // hop
    pitched = 0
    for i in range(frames):
        S = np.abs(np.fft.rfft(x[i * hop:i * hop + win] * w))
        if S[mid].sum() > S[lo].sum():
            pitched += 1
    return pitched / max(frames, 1)


def gate(path, label=''):
    x, sr = read(path)
    C, t = chroma(x, sr)

    overall = best_key(C.sum(axis=0))
    win_labels = []
    step = TWO_BARS
    a = 0.0
    while a + step <= t[-1]:
        sel = (t >= a) & (t < a + step)
        if sel.any():
            s = best_key(C[sel].sum(axis=0))
            if s:
                win_labels.append(family(s[0][1]))
        a += step

    top_fam = family(overall[0][1]) if overall else 'n/a'
    stability = win_labels.count(top_fam) / max(len(win_labels), 1)
    separation = overall[0][0] - overall[1][0] if len(overall) > 1 else 0.0
    tonal = tonal_evidence(x, sr)

    p1 = stability >= 0.70
    p2 = separation >= 0.10
    p3 = tonal >= 0.50
    verdict = 'CONFIDENT' if (p1 and p2 and p3) else 'AMBIGUOUS — not eligible to decide'

    print(f'{label or path}')
    print(f'   best key       {overall[0][1]}  (r={overall[0][0]:.3f})   family: {top_fam}')
    print(f'   runner-up      {overall[1][1]}  (r={overall[1][0]:.3f})')
    print(f'   1 stability    {stability*100:5.1f}%  of {len(win_labels)} two-bar windows   '
          f'{"PASS" if p1 else "FAIL"}  (need >=70%)')
    print(f'   2 separation   {separation:.3f}                             '
          f'{"PASS" if p2 else "FAIL"}  (need >=0.10)')
    print(f'   3 tonal evid.  {tonal*100:5.1f}%  pitched-dominant frames    '
          f'{"PASS" if p3 else "FAIL"}  (need >=50%)')
    print(f'   -> {verdict}')
    spine = 'A family'
    if p1 and p2 and p3:
        print(f'   -> vs spine (A minor): {"MATCH" if top_fam == spine else "CLASH — " + top_fam}')
    print()
    return dict(key=overall[0][1], fam=top_fam, stab=stability, sep=separation,
                tonal=tonal, confident=(p1 and p2 and p3))


if __name__ == '__main__':
    for p in sys.argv[1:]:
        gate(p)
