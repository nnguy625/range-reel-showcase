"""
Franco's surgical subtraction on V8_SKATE_b, 2026-07-26. He explicitly said
DO NOT REGENERATE - subtract. His spec, verbatim intent:

  1. "remove or reduce the click/clap-like mid-band transient layer by about
     6-8 dB until the 300-2,000 Hz onset rate falls below 0.75/s"
  2. "remove the rapid ticking or roll from the final bar"
  3. "shorten only the ordinary 808 tails by roughly 80-120 ms so they stop
     breathing across E1's next kick. Preserve the featured slide at the end
     of every second bar."
  4. "a small 2-3 dB sidechain dip for approximately 60-90 ms under each E1
     kick is also appropriate"
  5. "Do not thin the 808 generally because that is the part finally matching
     the brief."

So: reduce mid-band TRANSIENTS only (not sustained mids, not the 808), duck
under the spine's kicks, and leave the low end's character al***REMOVED***
"""
import subprocess, os, sys, numpy as np

SR = 44100
BEAT = 60.0 / 128.0            # 0.46875 s
BAR = 4 * BEAT                 # 1.875 s
NFFT, HOP = 2048, 512
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"

SRC = "V8_SKATE_b.mp3"
OUT = "V9_SKATE_surgical.wav"

# Franco's numbers
MID_DUCK_DB   = -7.0     # "about 6-8 dB"
DUCK_MS       = 35       # width of the transient duck
TAIL_TRIM_MS  = 100      # "roughly 80-120 ms"
SC_DEPTH_DB   = -2.5     # "2-3 dB"
SC_MS         = 75       # "approximately 60-90 ms"
TARGET_ONSETS = 0.75     # the gate he is aiming at


def decode(path, stereo=True, hp=None):
    af = ["-af", f"highpass=f={hp}"] if hp else []
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                          "-ac", "2" if stereo else "1", "-ar", str(SR),
                          *af, "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32).astype(np.float64)
    return x.reshape(-1, 2) if stereo else x


def bandpass(x, lo, hi):
    """Zero-phase band split via FFT — no phase smear when recombining."""
    n = len(x)
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(n, 1 / SR)
    m = ((f >= lo) & (f <= hi)).astype(float)
    # soften the edges so the split does not ring
    k = max(1, int(len(f) * 0.0015))
    ker = np.hanning(2 * k + 1); ker /= ker.sum()
    m = np.convolve(m, ker, mode='same')
    if X.ndim == 2:
        m = m[:, None]
    return np.fft.irfft(X * m, n=n, axis=0)


def spectro(mono):
    w = np.hanning(NFFT)
    return np.array([np.abs(np.fft.rfft(mono[i:i + NFFT] * w))
                     for i in range(0, len(mono) - NFFT, HOP)])


f_ax = np.fft.rfftfreq(NFFT, 1 / SR)
MIDBAND = (f_ax > 300) & (f_ax < 2000)


def strict_onsets(mono):
    """The same strict detector the gate uses, so we optimise the real metric."""
    S = spectro(mono)
    e = S[:, MIDBAND].mean(axis=1)
    d = np.diff(e, prepend=e[0]); d[d < 0] = 0
    rel = d / (e + 1e-9)
    idx = [i for i in range(1, len(d) - 1)
           if rel[i] > 0.8 and d[i] >= d[i - 1] and d[i] > d[i + 1]]
    return np.array(idx) * HOP / SR, len(idx) / (len(mono) / SR)


def duck_envelope(n, times, depth_db, width_ms):
    """Cosine-shaped gain dips at the given times. Smooth, so no clicks."""
    env = np.ones(n)
    w = int(width_ms / 1000 * SR)
    if w < 4:
        return env
    g = 10 ** (depth_db / 20)
    shape = g + (1 - g) * (1 - np.cos(np.linspace(0, 2 * np.pi, w))) / 2
    for t in times:
        a = int(t * SR)
        b = min(n, a + w)
        if a < 0 or a >= n:
            continue
        env[a:b] = np.minimum(env[a:b], shape[:b - a])
    return env


src = os.path.join(MUS, SRC)
x = decode(src)
n = len(x)
mono = x.mean(axis=1)
dur = n / SR

print(f"{SRC}  {dur:.1f}s")
_, before = strict_onsets(mono)
print(f"mid-band onset rate BEFORE  {before:.2f}/s   (gate {TARGET_ONSETS})\n")

# ---- 1. duck the mid-band TRANSIENTS only -----------------------------
low  = bandpass(x, 0, 300)        # the 808 lives here - Franco: do not thin it
mid  = bandpass(x, 300, 2000)     # the click/clap layer he wants reduced
high = bandpass(x, 2000, SR / 2)

t_mid, _ = strict_onsets(mono)
print(f"transients found in the mid band: {len(t_mid)}")

# escalate the duck until the strict detector drops under Franco's gate
depth = MID_DUCK_DB
for attempt in range(6):
    env = duck_envelope(n, t_mid, depth, DUCK_MS)[:, None]
    test = low + mid * env + high
    _, rate = strict_onsets(test.mean(axis=1))
    print(f"  duck {depth:5.1f} dB -> {rate:.2f}/s")
    if rate < TARGET_ONSETS:
        break
    depth -= 1.5
mid = mid * env

# ---- 2. the final bar: kill the ticking/roll --------------------------
# Franco: "remove the rapid ticking or roll from the final bar"
last_bar_start = max(0, n - int(BAR * SR))
fade = np.linspace(1.0, 10 ** (-9 / 20), n - last_bar_start)[:, None]
mid[last_bar_start:] *= fade
high[last_bar_start:] *= fade
print(f"\nfinal bar: mid+high rolled off to -9 dB across the last {BAR:.3f}s")

# ---- 3. shorten the ordinary 808 tails --------------------------------
# Detect low-band note starts; trim the tail of each EXCEPT the one that
# lands at the end of an even bar (Franco: "preserve the featured slide").
lowmono = low.mean(axis=1)
Slow = spectro(lowmono)
el = Slow[:, (f_ax > 40) & (f_ax < 120)].mean(axis=1)
dl = np.diff(el, prepend=el[0]); dl[dl < 0] = 0
cut = np.percentile(dl[dl > 0], 90) if (dl > 0).any() else 0
gap = int(0.12 * SR / HOP)
notes, last = [], -gap
for i in range(1, len(dl) - 1):
    if dl[i] > cut and dl[i] >= dl[i - 1] and dl[i] > dl[i + 1] and i - last >= gap:
        notes.append(i * HOP / SR); last = i

trim = int(TAIL_TRIM_MS / 1000 * SR)
kept = 0
for j, t in enumerate(notes):
    nxt = notes[j + 1] if j + 1 < len(notes) else dur
    # featured slide = a note landing near the end of an even-numbered bar
    pos_in_two_bars = t % (2 * BAR)
    if pos_in_two_bars > (2 * BAR - 0.35):
        kept += 1
        continue
    end = int(min(nxt, t + (nxt - t)) * SR)
    a = max(0, end - trim)
    if a < end <= n:
        low[a:end] *= np.linspace(1, 0, end - a)[:, None]
print(f"808 tails: {len(notes)} notes, trimmed {len(notes)-kept} by {TAIL_TRIM_MS} ms, "
      f"preserved {kept} featured slides")

# ---- 4. sidechain dip under every E1 kick -----------------------------
kicks = np.arange(0, dur, BEAT)
sc = duck_envelope(n, kicks, SC_DEPTH_DB, SC_MS)[:, None]
out = (low + mid + high) * sc
print(f"sidechain: {len(kicks)} kicks, {SC_DEPTH_DB} dB for {SC_MS} ms")

# ---- render -----------------------------------------------------------
peak = np.abs(out).max()
if peak > 0.99:
    out *= 0.99 / peak
    print(f"limited by {20*np.log10(0.99/peak):.2f} dB")

dst = os.path.join(MUS, OUT)
p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR),
                      "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", dst], stdin=subprocess.PIPE)
p.communicate(out.astype(np.float32).tobytes())
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", dst, "-b:a", "192k",
                os.path.join(MUS, OUT.replace('.wav', '.mp3'))])

_, after = strict_onsets(out.mean(axis=1))
print(f"\nmid-band onset rate AFTER   {after:.2f}/s   "
      f"{'PASS' if after < TARGET_ONSETS else 'still above gate'}")
print(f"wrote {OUT} and .mp3")
