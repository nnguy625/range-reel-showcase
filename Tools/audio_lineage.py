"""audio_lineage.py — did the render keep the attached track, or did the model add its own?

Extracts the audio of a rendered clip (ffmpeg), aligns it to the carrier that was attached at
generation time (FFT cross-correlation on the first seconds), then scores the two second by
second with a normalized cross-correlation. A render whose audio is the carrier passed through
scores close to 1.0 in every window; a render where the model layered its own percussion or
foley over the track drops sharply in the windows where the invented hits sit — the pattern that
was logged on 2026-08-07 as 0.97 -> 0.29 and became the standing law "model audio stays OFF
when a real track is attached".

Usage:
    py Tools/audio_lineage.py <render.mp4> <carrier.wav|mp3> [--sr 48000] [--window 1.0]
                              [--offset auto|<seconds>] [--floor 0.6] [--json]

Verdict: PASS if every window >= --floor, FAIL otherwise, with the offending windows listed.
"""
import argparse, subprocess, sys, json
import numpy as np


def load_mono(path, sr):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"]
    p = subprocess.run(cmd, capture_output=True)
    if p.returncode != 0:
        sys.exit(p.stderr.decode(errors="replace"))
    return np.frombuffer(p.stdout, dtype=np.float32).astype(np.float64)


def best_offset(a, b, sr, probe_s=3.0, max_lag_s=2.0):
    """Lag (s) of a inside b by FFT cross-correlation on the first probe_s of a. Positive = a starts
    later than b."""
    n = a[: int(probe_s * sr)]; n = n - n.mean()
    m = int(max_lag_s * sr)
    hay = b[: len(n) + 2 * m]
    N = 1 << int(np.ceil(np.log2(len(hay) + len(n))))
    corr = np.fft.irfft(np.fft.rfft(hay, N) * np.conj(np.fft.rfft(n, N)), N)[: len(hay) - len(n) + 1]
    cs = np.concatenate([[0.0], np.cumsum(hay * hay)])
    seg = cs[len(n):] - cs[: -len(n)]
    r = corr / (np.sqrt(np.maximum(seg[: len(corr)], 1e-12)) * (np.sqrt(np.dot(n, n)) + 1e-12))
    lag = int(np.argmax(r))
    return lag / sr, float(r[lag])


def per_window(a, b, sr, win_s):
    w = int(win_s * sr); n = min(len(a), len(b)) // w
    out = []
    for i in range(n):
        x = a[i * w:(i + 1) * w]; y = b[i * w:(i + 1) * w]
        x = x - x.mean(); y = y - y.mean()
        d = np.sqrt(np.dot(x, x) * np.dot(y, y)) + 1e-12
        out.append(float(np.dot(x, y) / d))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("render"); ap.add_argument("carrier")
    ap.add_argument("--sr", type=int, default=48000); ap.add_argument("--window", type=float, default=1.0)
    ap.add_argument("--offset", default="auto"); ap.add_argument("--floor", type=float, default=0.6)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = load_mono(a.render, a.sr); c = load_mono(a.carrier, a.sr)
    if a.offset == "auto":
        off, peak = best_offset(r, c, a.sr)
    else:
        off, peak = float(a.offset), None
    s = int(round(off * a.sr))
    c_al = c[s:] if s >= 0 else np.concatenate([np.zeros(-s), c])
    scores = per_window(r, c_al, a.sr, a.window)
    bad = [i for i, v in enumerate(scores) if v < a.floor]
    out = {"render": a.render, "carrier": a.carrier, "offset_s": round(off, 4), "align_peak": None if peak is None else round(peak, 3),
           "window_s": a.window, "per_window": [round(v, 3) for v in scores],
           "min": round(min(scores), 3) if scores else None, "max": round(max(scores), 3) if scores else None,
           "verdict": "PASS" if scores and not bad else "FAIL", "failing_windows": bad}
    if a.json:
        print(json.dumps(out, indent=1))
    else:
        print(f"{a.render}\n  vs {a.carrier}\n  offset={out['offset_s']}s align_peak={out['align_peak']}")
        print("  per-second corr: " + " ".join(f"{v:.2f}" for v in scores))
        print(f"  min={out['min']} max={out['max']} -> {out['verdict']}" + (f" (windows {bad})" if bad else ""))


if __name__ == "__main__":
    main()
