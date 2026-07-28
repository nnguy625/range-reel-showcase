"""MASTER_90 assembler — executes Franco's locked build spec (2026-07-26).

Every number in here is his. Do not re-derive them; see Docs/STATE.md
"FRANCO'S LOCKED BUILD SPEC".

    grid          128 BPM, 4/4, 6 worlds x 8 bars x 15.000 s = 90.000 s
    spine         E1_MASTER_90.wav, NEVER touched, never stretched, never re-rendered
    overlay HP    ~100 Hz, applied BEFORE trimming (the filter shifts level 1.5-2.6 dB,
                  so trimming first gives the wrong number)
    downbeat      detect the overlay's first onset, snap FORWARD to the next whole bar
    flam sweep    +/-117 ms (one 16th @128) in 1 ms steps; widen ONCE to +/-234 ms if
                  still >5%; beyond that reject rather than shift further
    overlay level ~4 dB under the spine
    seam fades    40 ms both ends of every overlay slice
    micro gap     117 ms, cosine 10 ms down / 97 ms hold at -18 dB / 10 ms up, landing
                  at unity EXACTLY on the next downbeat. Outgoing overlay + FX bus ONLY.
                  "Leave E1 completely unchanged."
    master trim   ONE fixed -7.5 dB across the reel. Per-world gain would audibly pump
                  E1; balance per-world on the overlay bus only.

    py buildmaster3.py [out_stem]        default stem: MASTER_90_v4
"""
import subprocess, os, sys, numpy as np

SR, NFFT, HOP = 44100, 2048, 512
BEAT = 60.0 / 128.0
BAR = 4 * BEAT                 # 1.875 s
WORLD = 8 * BAR                # 15.000 s
SIX = BEAT / 4                 # 117 ms, one 16th
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
SPINE = "E1_MASTER_90.wav"

OVERLAY_HP = 100               # Hz
OVERLAY_UNDER_DB = 4.0         # overlay sits this far under the spine
SEAM_FADE = 0.040              # 40 ms
GAP_DOWN, GAP_HOLD, GAP_UP = 0.010, 0.097, 0.010   # = 117 ms
GAP_FLOOR_DB = -18.0
MASTER_TRIM_DB = -7.5
FLAM_CEIL = 5.0

# THE FINAL SIX — all Franco-locked 2026-07-27. Do not substitute without a ruling.
PICKS = [
    ("1 skate",  "V10_SKATE_locked.wav"),    # surgical chain, 55ms @ 7dB
    ("2 bolly",  "V16_BOLLY_a.mp3"),         # tumbi/santoor, 49 deliberate attacks
    ("3 agent",  "V18_AGENT_b.mp3"),         # "pass, no margin" - drums exactly 0.75
    ("4 car",    "V25_CAR_b.mp3"),           # pitched-transient allowance, root F
    ("5 sword",  "V12_SWORD_locked.wav"),    # surgical chain
    ("6 runway", "V22_RUNWAY_b.mp3"),        # pitched-transient allowance + manual harmonic pass
]


def load(p, hp=None):
    af = [f"highpass=f={hp}"] if hp else []
    a = ["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR)]
    if af:
        a += ["-af", ",".join(af)]
    a += ["-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(a, capture_output=True).stdout,
                         dtype=np.float32).astype(float)


def spec(x):
    w = np.hanning(NFFT)
    return np.array([np.abs(np.fft.rfft(x[i:i + NFFT] * w))
                     for i in range(0, len(x) - NFFT, HOP)])


_f = np.fft.rfftfreq(NFFT, 1 / SR)
BAND = ((_f > 40) & (_f < 120)) | ((_f > 300) & (_f < 2000))


def events(S):
    e = S[:, BAND].mean(axis=1)
    d = np.diff(e, prepend=e[0])
    d[d < 0] = 0
    if not d.any():
        return np.array([])
    cut = np.percentile(d[d > 0], 88)
    gap = max(1, int(0.060 * SR / HOP))
    pk, last = [], -gap
    for i in range(1, len(d) - 1):
        if d[i] > cut and d[i] >= d[i - 1] and d[i] > d[i + 1] and i - last >= gap:
            pk.append(i)
            last = i
    return np.array(pk) * HOP / SR


def rms(x):
    return float(np.sqrt((x ** 2).mean())) if len(x) else 0.0


def best_offset(ev, spine_ev, centre, dur):
    """Sweep the bar for the minimum-flam placement. Snapping to the bar line is
    the wrong step - measured 43% snapped vs 0.0% at the best offset 15 ms away."""
    best, best_t = None, centre
    for lim in (SIX, 2 * SIX):
        for ms in range(-int(lim * 1000), int(lim * 1000) + 1):
            t0 = centre + ms / 1000.0
            if t0 < 0 or t0 + WORLD > dur:
                continue
            seg = ev[(ev >= t0) & (ev < t0 + WORLD)] - t0
            if len(seg) < 6:
                continue
            d = np.abs(seg[:, None] - spine_ev[None, :]).min(axis=1) * 1000
            r = float(((d >= 15) & (d <= 60)).mean() * 100)
            if best is None or r < best:
                best, best_t = r, t0
        if best is not None and best <= FLAM_CEIL:
            break          # widen ONCE, then stop
    return best, best_t


def micro_gap_env(n):
    """117 ms cosine dip landing at unity exactly on the next downbeat."""
    env = np.ones(n)
    floor = 10 ** (GAP_FLOOR_DB / 20.0)
    nd, nh, nu = (int(round(t * SR)) for t in (GAP_DOWN, GAP_HOLD, GAP_UP))
    tail = nd + nh + nu
    if tail > n:
        return env
    s = n - tail
    ramp = 0.5 * (1 + np.cos(np.linspace(0, np.pi, nd)))          # 1 -> 0
    env[s:s + nd] = floor + (1 - floor) * ramp
    env[s + nd:s + nd + nh] = floor
    ramp = 0.5 * (1 - np.cos(np.linspace(0, np.pi, nu)))          # 0 -> 1
    env[s + nd + nh:s + nd + nh + nu] = floor + (1 - floor) * ramp
    return env


def main():
    stem = sys.argv[1] if len(sys.argv) > 1 else "MASTER_90_v4"

    spine = load(os.path.join(MUS, SPINE))
    total = int(round(90.0 * SR))
    spine = spine[:total] if len(spine) >= total else np.pad(spine, (0, total - len(spine)))
    spine_ev_all = events(spec(spine))
    spine_ev = spine_ev_all[spine_ev_all < WORLD]
    spine_rms = rms(spine)

    print(f"spine {SPINE}  {len(spine)/SR:.3f}s  rms {20*np.log10(spine_rms+1e-12):.1f} dB")
    print(f"{'world':<10}{'take':<26}{'flams':>8}{'gain dB':>9}  note")

    bus = np.zeros(total)
    target = spine_rms * 10 ** (-OVERLAY_UNDER_DB / 20.0)
    ok_all = True

    for i, (lbl, fn) in enumerate(PICKS):
        p = os.path.join(MUS, fn)
        if not os.path.exists(p):
            print(f"{lbl:<10}{fn:<26}{'':>8}{'':>9}  MISSING - slot left silent")
            ok_all = False
            continue

        x = load(p, hp=OVERLAY_HP)                 # high-pass BEFORE trimming
        dur = len(x) / SR
        ev = events(spec(x))
        centre = float(np.ceil(ev[0] / BAR) * BAR) if len(ev) else 0.0
        if centre + WORLD > dur:
            centre = max(0.0, dur - WORLD - 2 * SIX - 0.01)

        flams, t0 = best_offset(ev, spine_ev, centre, dur)
        a = int(round(t0 * SR))
        seg = x[a:a + int(round(WORLD * SR))]
        if len(seg) < int(round(WORLD * SR)):
            seg = np.pad(seg, (0, int(round(WORLD * SR)) - len(seg)))

        g = target / (rms(seg) + 1e-12)
        seg = seg * g

        nf = int(SEAM_FADE * SR)
        seg[:nf] *= np.linspace(0, 1, nf)
        seg[-nf:] *= np.linspace(1, 0, nf)

        # the beat gap belongs to the OUTGOING world - never the incoming one
        if i < len(PICKS) - 1:
            seg *= micro_gap_env(len(seg))

        s = i * int(round(WORLD * SR))
        bus[s:s + len(seg)] += seg

        note = "" if (flams is not None and flams <= FLAM_CEIL) else "OVER CEILING"
        if note:
            ok_all = False
        fl = f"{flams:.1f}%" if flams is not None else "n/a"
        print(f"{lbl:<10}{fn:<26}{fl:>8}{20*np.log10(g+1e-12):>9.1f}  {note}")

    mix = (spine + bus) * (10 ** (MASTER_TRIM_DB / 20.0))
    peak = float(np.abs(mix).max())
    print(f"\nlength {len(mix)/SR:.3f}s   peak {20*np.log10(peak+1e-12):.1f} dBFS   "
          f"mean {20*np.log10(rms(mix)+1e-12):.1f} dB")
    if peak >= 1.0:
        print("!! CLIPPING - do not ship this build")

    wav = os.path.join(MUS, stem + ".wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR),
                    "-ac", "1", "-i", "-", wav],
                   input=mix.astype(np.float32).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-b:a", "192k",
                    os.path.join(MUS, stem + ".mp3")])
    print(f"wrote {stem}.wav / .mp3")
    if not ok_all:
        print("\nNOT CLEAN - a slot was missing or over the flam ceiling. Fix before Franco.")


if __name__ == "__main__":
    main()
