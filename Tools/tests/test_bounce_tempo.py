"""Tests for Tools/bounce_tempo.py -- the peak / interval / bounce-run logic, without video.

bounce_tempo's only I/O is frames() (an ffmpeg rawvideo pipe plus an ffprobe size query).
The tests build synthetic frames in numpy -- a crimson block on a gray field whose vertical
position follows a chosen bounce trace at 24 fps -- monkeypatch frames() to return them, and
run main() with --json, so the numbers asserted are exactly the ones the tool reports:
intervals_s, mean_interval_s, spread_x, bounce_run.{mean_interval_s, spread_x, mean_vs_beat}
and verdict. hsv_mask() and bounces() are also exercised directly.

Every synthetic take has a still 0.75 s lead-in and settle around ~8 s of bouncing -- the
entry/exit the tool's own bounce-run logic exists for. (Without them the tool's ~1 s
moving-mean detrend produces an edge peak whose interval can land inside the 0.7-1.3x
median band; that is a property of the tool, not of these tests.)

One optional end-to-end test writes a real clip with cv2.VideoWriter and lets the tool
decode it through ffmpeg; it skips cleanly when cv2 or ffmpeg is missing (see conftest.py).
"""
import json
import sys

import numpy as np
import pytest

import bounce_tempo

FPS = 24
W, H = 240, 136                # tiny frames; even height so the e2e clip encodes cleanly
BEAT_S = 60.0 / 128.0          # 0.46875 s = 11.25 frames at 24 fps
CRIMSON = (220, 20, 60)        # hue ~348 deg, sat 0.91, val 0.86 -> inside the default 340..20 window
GRAY = (60, 60, 60)            # sat 0 -> outside every mask
BLOCK_W, BLOCK_H = 40, 30
CENTER, AMP = 68.0, 25.0       # centroid rest row and bounce amplitude (px)
LEAD_S = SETTLE_S = 0.75


# ---------------------------------------------------------------- synthetic takes

def render(y_centers):
    """Frames (n, H, W, 3) uint8: gray field, crimson block centered on row y_centers[i]."""
    n = len(y_centers)
    fr = np.empty((n, H, W, 3), dtype=np.uint8)
    fr[...] = GRAY
    x0 = (W - BLOCK_W) // 2
    for i, yc in enumerate(y_centers):
        top = int(round(yc - BLOCK_H / 2.0))
        top = min(max(top, 0), H - BLOCK_H)
        fr[i, top:top + BLOCK_H, x0:x0 + BLOCK_W] = CRIMSON
    return fr


def on_beat_trace(bounce_s=8.0, period=BEAT_S, phase=0.0):
    """Still lead-in, `bounce_s` of a sinusoid at `period`, still settle. Centroid rows per frame."""
    n = int(round((LEAD_S + bounce_s + SETTLE_S) * FPS))
    t = np.arange(n) / FPS
    y = np.empty(n)
    a, b, c = t < LEAD_S, (t >= LEAD_S) & (t < LEAD_S + bounce_s), t >= LEAD_S + bounce_s
    y[b] = CENTER + AMP * np.sin(2 * np.pi * (t[b] - LEAD_S) / period + phase)
    y[a] = CENTER + AMP * np.sin(phase)
    y[c] = CENTER + AMP * np.sin(2 * np.pi * bounce_s / period + phase)
    return y


def irregular_trace(bounce_s=8.0, periods=(0.35, 0.62), first=0):
    """Bounces whose successive periods alternate 0.35 s / 0.62 s (bottom-of-bounce at each
    boundary), with the same still lead-in and settle."""
    n = int(round((LEAD_S + bounce_s + SETTLE_S) * FPS))
    t = np.arange(n) / FPS
    y = np.full(n, CENTER + AMP)
    bottoms = [LEAD_S]
    k = first
    while bottoms[-1] < LEAD_S + bounce_s:
        bottoms.append(bottoms[-1] + periods[k % 2])
        k += 1
    for a, b in zip(bottoms, bottoms[1:]):
        m = (t >= a) & (t < b)
        y[m] = CENTER + AMP * np.cos(2 * np.pi * (t[m] - a) / (b - a))
    y[t >= bottoms[-1]] = CENTER + AMP
    return y


def run_tool(monkeypatch, capsys, frames, *cli):
    """Run bounce_tempo.main() with frames() serving `frames`; return the --json report."""
    monkeypatch.setattr(bounce_tempo, "frames", lambda path, fps, w, start=0.0, dur=0.0: frames)
    monkeypatch.setattr(sys, "argv", ["bounce_tempo.py", "synthetic.mp4", "--json", *cli])
    bounce_tempo.main()
    return json.loads(capsys.readouterr().out)


# ---------------------------------------------------------------- pure functions

def test_hsv_mask_selects_crimson_and_wraps_through_zero():
    px = np.array([[CRIMSON, GRAY, (30, 40, 220), (40, 5, 10)]], dtype=np.uint8)  # 1 x 4 x 3
    #                crimson  gray   saturated blue  too-dark red
    default = bounce_tempo.hsv_mask(px, 340, 20, 0.35, 0.25)      # the tool's default sari window
    assert default.tolist() == [[True, False, False, False]]
    blue_window = bounce_tempo.hsv_mask(px, 200, 260, 0.35, 0.25)  # non-wrapping window
    assert blue_window.tolist() == [[False, False, True, False]]


def test_bounces_finds_beat_spaced_peaks_and_min_period_thins_them():
    y = on_beat_trace()                                            # centroid rows, 24 fps
    peaks, d = bounce_tempo.bounces(y, FPS, min_period=0.30)      # the tool's default min-period
    assert len(d) == len(y)
    iv = np.diff(peaks)                                            # frames between bounces
    assert 17 <= len(peaks) <= 20                                  # ~8 s / 0.46875 s = 17 bounces + edges
    interior = iv[1:-1]                                            # first/last touch the lead-in / settle
    assert set(interior.tolist()) <= {11, 12}                      # 11.25-frame period at frame resolution
    assert abs(interior.mean() / FPS - BEAT_S) <= 0.05 * BEAT_S

    thinned, _ = bounce_tempo.bounces(y, FPS, min_period=0.60)    # guard wider than the true period
    assert len(thinned) < len(peaks)
    assert np.diff(thinned).min() >= int(round(0.60 * FPS))        # no two peaks closer than 14 frames


# ---------------------------------------------------------------- (a) on the beat -> PASS

@pytest.mark.parametrize("phase", [0.0, 2.09, 4.19])
def test_on_beat_sinusoid_passes(monkeypatch, capsys, phase):
    out = run_tool(monkeypatch, capsys, render(on_beat_trace(phase=phase)))
    assert out["beat_s"] == 0.46875
    assert out["frames"] == int(round((LEAD_S + 8.0 + SETTLE_S) * FPS))
    assert 17 <= out["bounces"] <= 21
    run = out["bounce_run"]                                        # the bar where the bounce happens
    assert run["bounces"] >= 15
    assert abs(run["mean_interval_s"] - BEAT_S) <= 0.05 * BEAT_S  # within +/-5% of the beat
    assert 0.95 <= run["mean_vs_beat"] <= 1.05
    assert run["spread_x"] <= 1.20                                 # slowest/fastest under the gate
    assert out["verdict"] == "PASS"
    # the full-clip figures include the lead-in / settle intervals and are reported alongside
    assert len(out["intervals_s"]) == out["bounces"] - 1
    assert out["mean_interval_s"] > 0 and out["spread_x"] >= run["spread_x"]


# ---------------------------------------------------------------- (b) irregular -> FAIL

@pytest.mark.parametrize("first", [0, 1])                        # start on the short or the long period
def test_irregular_alternation_fails_on_spread(monkeypatch, capsys, first):
    out = run_tool(monkeypatch, capsys, render(irregular_trace(first=first)))
    assert out["bounces"] >= 15
    assert out["spread_x"] >= 1.5                                  # 0.62 / 0.35 = 1.77 at frame resolution
    assert 0.85 <= out["mean_interval_s"] / BEAT_S <= 1.15         # the mean alone would not catch it ...
    assert out["verdict"] == "FAIL"                                # ... the spread does
    if "bounce_run" in out:
        assert out["bounce_run"]["spread_x"] > 1.20


def test_max_spread_is_a_control(monkeypatch, capsys):
    """Same irregular take; a --max-spread wide enough to admit 1.77x turns the verdict."""
    out = run_tool(monkeypatch, capsys, render(irregular_trace(first=0)), "--max-spread", "1.9")
    assert out["spread_x"] >= 1.5
    assert out["verdict"] == "PASS"


# ---------------------------------------------------------------- optional end-to-end (cv2 + ffmpeg)

@pytest.mark.video
def test_end_to_end_synthetic_clip(cv2, ffmpeg_on_path, tmp_path, monkeypatch, capsys):
    """Write the on-beat take as a real .mp4 and let the tool decode it itself (frames -> ffmpeg)."""
    clip = tmp_path / "bounce_128bpm.mp4"
    writer = cv2.VideoWriter(str(clip), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
    if not writer.isOpened():
        pytest.skip("cv2.VideoWriter could not open an mp4v encoder")
    for f in render(on_beat_trace(phase=0.0)):
        writer.write(np.ascontiguousarray(f[..., ::-1]))           # RGB -> BGR for OpenCV
    writer.release()
    if not clip.exists() or clip.stat().st_size < 1000:
        pytest.skip("cv2 wrote no usable clip (codec unavailable)")

    monkeypatch.setattr(sys, "argv", ["bounce_tempo.py", str(clip), "--json", "--width", str(W)])
    bounce_tempo.main()                                            # frames() NOT patched: real ffmpeg path
    out = json.loads(capsys.readouterr().out)
    assert out["frames"] == int(round((LEAD_S + 8.0 + SETTLE_S) * FPS))
    run = out["bounce_run"]
    assert abs(run["mean_interval_s"] - BEAT_S) <= 0.05 * BEAT_S
    assert run["spread_x"] <= 1.20
    assert out["verdict"] == "PASS"
