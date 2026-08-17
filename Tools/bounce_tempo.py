"""bounce_tempo.py — motion-tempo gate for a dance take (the "saree-centroid" method).

Tracks the vertical centre of mass of the performer's costume frame by frame, reads the
up-and-down trace as the dance's waveform, and reports the interval between successive
bounces against the beat grid (128 BPM -> 0.46875 s). A take passes when the mean interval
sits on the beat and the slowest/fastest spread stays under the threshold (1.20x by default).

Usage:
    py Tools/bounce_tempo.py <clip.mp4> [--fps 24] [--bpm 128] [--hue-lo 340] [--hue-hi 20]
                              [--sat 0.35] [--val 0.25] [--start 0] [--dur 0]
                              [--min-period 0.30] [--max-spread 1.20]

Colour mask: HSV hue window (degrees, wraps through 0) with saturation/value floors — defaults
target the crimson sari; pass --hue-lo/--hue-hi for other costumes. Frames are pulled through
ffmpeg as raw RGB, so ffmpeg must be on PATH. Output: per-bounce intervals, mean, spread,
PASS/FAIL, and an optional CSV of the raw trace (--csv out.csv).
"""
import argparse, subprocess, sys, json
import numpy as np


def frames(path, fps, w, start=0.0, dur=0.0):
    cmd = ["ffmpeg", "-v", "error"]
    if start:
        cmd += ["-ss", str(start)]
    cmd += ["-i", path]
    if dur:
        cmd += ["-t", str(dur)]
    cmd += ["-vf", f"fps={fps},scale={w}:-2", "-pix_fmt", "rgb24", "-f", "rawvideo", "-"]
    p = subprocess.run(cmd, capture_output=True)
    if p.returncode != 0:
        sys.exit(p.stderr.decode(errors="replace"))
    # probe height by decoding one frame's size from ffprobe-free trick: use scale w and infer h
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height", "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    sw, sh = [int(x) for x in probe.strip().split(",")[:2]]
    h = int(round(sh * w / sw / 2) * 2)
    buf = np.frombuffer(p.stdout, dtype=np.uint8)
    n = buf.size // (w * h * 3)
    return buf[: n * w * h * 3].reshape(n, h, w, 3)


def hsv_mask(rgb, hue_lo, hue_hi, sat_min, val_min):
    x = rgb.astype(np.float32) / 255.0
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    mx = x.max(-1); mn = x.min(-1); d = mx - mn + 1e-6
    hue = np.zeros_like(mx)
    m = mx == r; hue[m] = ((g - b)[m] / d[m]) % 6
    m = mx == g; hue[m] = (b - r)[m] / d[m] + 2
    m = mx == b; hue[m] = (r - g)[m] / d[m] + 4
    hue = (hue * 60) % 360
    sat = d / (mx + 1e-6); val = mx
    if hue_lo <= hue_hi:
        hm = (hue >= hue_lo) & (hue <= hue_hi)
    else:  # wraps through 0 (e.g. 340..20)
        hm = (hue >= hue_lo) | (hue <= hue_hi)
    return hm & (sat >= sat_min) & (val >= val_min)


def centroid_trace(fr, **kw):
    ys = []
    for f in fr:
        mk = hsv_mask(f, **kw)
        if mk.sum() < 50:
            ys.append(np.nan); continue
        rows = np.where(mk)[0]
        ys.append(rows.mean())
    y = np.array(ys, dtype=np.float64)
    # fill gaps, smooth (3-frame), detrend with a moving mean of ~1 s
    idx = np.arange(len(y)); ok = ~np.isnan(y)
    if ok.sum() < 8:
        sys.exit("mask too sparse — adjust --hue/--sat/--val")
    y = np.interp(idx, idx[ok], y[ok])
    k = 3; ys_ = np.convolve(y, np.ones(k) / k, mode="same")
    return ys_


def bounces(y, fps, min_period):
    win = int(round(fps))  # ~1 s moving mean as trend
    trend = np.convolve(y, np.ones(win) / win, mode="same")
    d = y - trend  # positive = costume lower in frame (y grows downward)
    peaks = []
    minsep = max(1, int(round(min_period * fps)))
    for i in range(1, len(d) - 1):
        if d[i] > d[i - 1] and d[i] >= d[i + 1] and d[i] > 0:
            if not peaks or i - peaks[-1] >= minsep:
                peaks.append(i)
            elif d[i] > d[peaks[-1]]:
                peaks[-1] = i
    return peaks, d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip"); ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--bpm", type=float, default=128); ap.add_argument("--width", type=int, default=480)
    ap.add_argument("--hue-lo", type=float, default=340); ap.add_argument("--hue-hi", type=float, default=20)
    ap.add_argument("--sat", type=float, default=0.35); ap.add_argument("--val", type=float, default=0.25)
    ap.add_argument("--start", type=float, default=0); ap.add_argument("--dur", type=float, default=0)
    ap.add_argument("--min-period", type=float, default=0.30); ap.add_argument("--max-spread", type=float, default=1.20)
    ap.add_argument("--csv", default=None); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    fr = frames(a.clip, a.fps, a.width, a.start, a.dur)
    y = centroid_trace(fr, hue_lo=a.hue_lo, hue_hi=a.hue_hi, sat_min=a.sat, val_min=a.val)
    peaks, d = bounces(y, a.fps, a.min_period)
    beat = 60.0 / a.bpm
    iv = np.diff(peaks) / a.fps if len(peaks) > 1 else np.array([])
    out = {"clip": a.clip, "frames": int(len(y)), "bounces": int(len(peaks)),
           "beat_s": round(beat, 5),
           "intervals_s": [round(float(v), 3) for v in iv],
           "mean_interval_s": round(float(iv.mean()), 3) if iv.size else None,
           "spread_x": round(float(iv.max() / iv.min()), 2) if iv.size and iv.min() > 0 else None}
    # The bounce run: a take has an entry and an exit that are not bounces (a lead-in pose, a
    # settle). The gate is judged on the longest contiguous run of intervals near the median —
    # the bar where the bounce actually happens — and the full-clip numbers are reported alongside.
    run = []
    if iv.size >= 3:
        med = float(np.median(iv)); ok = (iv >= 0.7 * med) & (iv <= 1.3 * med)
        best, cur = (0, 0), None
        for i, flag in enumerate(ok):
            if flag:
                cur = i if cur is None else cur
                if i - cur + 1 > best[1] - best[0]:
                    best = (cur, i + 1)
            else:
                cur = None
        run = iv[best[0]:best[1]]
    if len(run) >= 2:
        out["bounce_run"] = {"intervals_s": [round(float(v), 3) for v in run],
                             "bounces": int(len(run) + 1),
                             "mean_interval_s": round(float(run.mean()), 3),
                             "spread_x": round(float(run.max() / run.min()), 2),
                             "mean_vs_beat": round(float(run.mean() / beat), 3)}
        r = out["bounce_run"]
        out["verdict"] = "PASS" if (r["spread_x"] <= a.max_spread and 0.85 <= r["mean_vs_beat"] <= 1.15) else "FAIL"
    elif iv.size:
        out["mean_vs_beat"] = round(float(iv.mean() / beat), 3)
        out["verdict"] = "PASS" if (out["spread_x"] <= a.max_spread and 0.85 <= out["mean_vs_beat"] <= 1.15) else "FAIL"
    else:
        out["verdict"] = "NO-BOUNCE"
    if a.csv:
        with open(a.csv, "w") as fh:
            fh.write("frame,t_s,centroid_y,detrended\n")
            for i, (yy, dd) in enumerate(zip(y, d)):
                fh.write(f"{i},{i / a.fps:.4f},{yy:.3f},{dd:.3f}\n")
    if a.json:
        print(json.dumps(out, indent=1))
    else:
        print(f"{a.clip}\n  frames={out['frames']} bounces={out['bounces']} beat={beat:.4f}s")
        print(f"  full clip: intervals={out['intervals_s']} mean={out['mean_interval_s']}s spread={out['spread_x']}x")
        if "bounce_run" in out:
            r = out["bounce_run"]
            print(f"  bounce run: {r['bounces']} bounces, intervals={r['intervals_s']} mean={r['mean_interval_s']}s "
                  f"spread={r['spread_x']}x mean/beat={r['mean_vs_beat']}")
        print(f"  -> {out['verdict']}")


if __name__ == "__main__":
    main()
