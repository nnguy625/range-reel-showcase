"""Tests for Tools/audio_lineage.py -- pure numpy, no ffmpeg, no media files.

audio_lineage's only I/O is load_mono() (an ffmpeg pipe). The tests call best_offset() and
per_window() directly on synthetic 48 kHz signals, and run main() end to end with load_mono
monkeypatched to serve those signals, so the offset, the per-window scores, the PASS/FAIL
verdict and the failing-window list are asserted exactly as the tool prints them (--json).

The synthetic "carrier" is what the real carriers are made of: band-limited noise (80-6000 Hz)
plus decaying two-tone bursts (220 + 880 Hz) on the 128 BPM grid (one every 0.46875 s).
Everything is seeded, so the numbers are reproducible.
"""
import json
import sys

import numpy as np
import pytest

import audio_lineage

SR = 48000
BEAT_S = 60.0 / 128.0          # 0.46875 s -- the reel's beat grid
FLOOR = 0.6                    # the tool's default --floor
RENDER_S = 6.0                 # length of the synthetic render (6 x 1 s windows)


# ---------------------------------------------------------------- synthetic signals

def make_carrier(dur_s=7.0, seed=1):
    """Band-limited noise + tone bursts on the beat grid, RMS ~0.12, deterministic."""
    rng = np.random.default_rng(seed)
    n = int(round(dur_s * SR))
    white = rng.standard_normal(n)
    spec = np.fft.rfft(white)
    f = np.fft.rfftfreq(n, 1.0 / SR)
    spec[(f < 80.0) | (f > 6000.0)] = 0.0
    x = np.fft.irfft(spec, n)
    x *= 0.1 / (np.sqrt(np.mean(x * x)) + 1e-12)
    burst_len = int(0.12 * SR)
    seg = np.arange(burst_len) / SR
    burst = np.exp(-seg / 0.03) * (np.sin(2 * np.pi * 220 * seg) + 0.5 * np.sin(2 * np.pi * 880 * seg))
    for k in range(int(dur_s / BEAT_S)):
        i0 = int(round(k * BEAT_S * SR))
        if i0 + burst_len <= n:
            x[i0:i0 + burst_len] += 0.5 * burst
    return x


def rms(x):
    return float(np.sqrt(np.mean(x * x)))


def run_tool(monkeypatch, capsys, signals, *cli):
    """Run audio_lineage.main() with load_mono() serving `signals` (name -> array); return the JSON."""
    monkeypatch.setattr(audio_lineage, "load_mono", lambda path, sr: signals[path])
    monkeypatch.setattr(sys, "argv", ["audio_lineage.py", *cli, "--json"])
    audio_lineage.main()
    return json.loads(capsys.readouterr().out)


# ---------------------------------------------------------------- (a) identical signals

def test_identical_signal_scores_one_in_every_window_and_passes(monkeypatch, capsys):
    carrier = make_carrier()
    render = carrier[: int(RENDER_S * SR)].copy()      # the carrier passed straight through

    scores = audio_lineage.per_window(render, carrier, SR, 1.0)
    assert len(scores) == 6
    assert min(scores) >= 0.999                          # ~1.0 in every window

    off, peak = audio_lineage.best_offset(render, carrier, SR)
    assert off == 0.0
    assert peak >= 0.99

    out = run_tool(monkeypatch, capsys, {"render.mp4": render, "carrier.wav": carrier},
                   "render.mp4", "carrier.wav", "--floor", str(FLOOR))
    assert out["verdict"] == "PASS"
    assert out["failing_windows"] == []
    assert out["offset_s"] == 0.0
    assert len(out["per_window"]) == 6
    assert out["min"] >= 0.999 and out["max"] <= 1.0


# ---------------------------------------------------------------- (b) known lag

def test_known_lag_is_recovered_within_1ms_and_aligned_windows_stay_high(monkeypatch, capsys):
    lag_s = 0.137                                        # render starts 137 ms later than the carrier
    carrier = make_carrier(dur_s=7.0)
    s = int(round(lag_s * SR))                           # 6576 samples at 48 kHz
    rng = np.random.default_rng(7)
    render = carrier[s:s + int(RENDER_S * SR)] + 0.001 * rng.standard_normal(int(RENDER_S * SR))
    assert rms(render - carrier[s:s + int(RENDER_S * SR)]) < 0.02 * rms(render)   # light (~-40 dB) noise only

    off, peak = audio_lineage.best_offset(render, carrier, SR)
    assert abs(off - lag_s) <= 0.001                     # within +/-1 ms
    assert peak >= 0.9

    # without the alignment the same two signals decorrelate -- that is why the sweep exists
    unaligned = audio_lineage.per_window(render, carrier, SR, 1.0)
    assert max(unaligned) < FLOOR

    aligned = audio_lineage.per_window(render, carrier[s:], SR, 1.0)
    assert len(aligned) == 6
    assert min(aligned) >= 0.95

    out = run_tool(monkeypatch, capsys, {"render.mp4": render, "carrier.wav": carrier},
                   "render.mp4", "carrier.wav", "--offset", "auto", "--floor", str(FLOOR))
    assert out["offset_s"] == pytest.approx(lag_s, abs=0.001)
    assert out["align_peak"] >= 0.9
    assert len(out["per_window"]) == 6
    assert min(out["per_window"]) >= 0.95
    assert out["verdict"] == "PASS"
    assert out["failing_windows"] == []


# ---------------------------------------------------------------- (c) one contaminated window

def test_contaminated_window_drops_below_floor_and_is_listed(monkeypatch, capsys):
    bad_window = 3                                       # seconds 3.0-4.0 of the render
    carrier = make_carrier()
    render = carrier[: int(RENDER_S * SR)].copy()
    rng = np.random.default_rng(3)
    w0 = bad_window * SR
    burst_len = int(0.03 * SR)                           # six 30 ms percussive noise bursts,
    for k in range(6):                                   # ~8x the carrier's RMS -- "the model
        i0 = w0 + int(round((0.08 + k * 0.15) * SR))     #  layered its own hits"
        render[i0:i0 + burst_len] += 1.0 * rng.standard_normal(burst_len)

    scores = audio_lineage.per_window(render, carrier, SR, 1.0)
    assert len(scores) == 6
    assert scores[bad_window] < FLOOR
    assert all(v >= 0.99 for i, v in enumerate(scores) if i != bad_window)

    # the contamination sits outside the 3 s alignment probe, so auto-offset still finds 0
    off, _ = audio_lineage.best_offset(render, carrier, SR)
    assert off == 0.0

    out = run_tool(monkeypatch, capsys, {"render.mp4": render, "carrier.wav": carrier},
                   "render.mp4", "carrier.wav", "--floor", str(FLOOR))
    assert out["verdict"] == "FAIL"
    assert out["failing_windows"] == [bad_window]
    assert out["per_window"][bad_window] < FLOOR
    assert out["min"] == out["per_window"][bad_window]
    assert all(v >= 0.99 for i, v in enumerate(out["per_window"]) if i != bad_window)


# ---------------------------------------------------------------- (d) different track entirely

def test_independent_track_fails_every_window(monkeypatch, capsys):
    carrier = make_carrier(seed=1)
    other = make_carrier(dur_s=RENDER_S, seed=99)        # same grid, same recipe, different material
    out = run_tool(monkeypatch, capsys, {"render.mp4": other, "carrier.wav": carrier},
                   "render.mp4", "carrier.wav", "--offset", "0", "--floor", str(FLOOR))
    assert len(out["per_window"]) == 6
    assert out["max"] < FLOOR
    assert out["verdict"] == "FAIL"
    assert out["failing_windows"] == list(range(6))
    assert out["align_peak"] is None                     # manual --offset: no alignment peak reported
