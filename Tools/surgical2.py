"""
V10 — V9 with Franco's click fix.

His finding: "the WAV contains several hard sample discontinuities introduced
by the edits, likely at tail boundaries. The clearest occur around 23.429,
23.615, 27.934, 37.523, 38.232, 39.393, 49.099, 50.341, and 55.554 seconds.
Add 5-10 ms equal-power fades at every edit boundary."

MY BUG: the tail trim faded a note to zero and then the very next sample
resumed at full amplitude - a step discontinuity, i.e. a click. Fading down
is not enough; the envelope has to come BACK UP smoothly too.

THE FIX: build ONE continuous gain envelope for the low band across the whole
file, with equal-power (cosine) ramps in BOTH directions, then multiply once.
An envelope that is continuous everywhere cannot produce a step.

Everything else is unchanged - Franco: "Do not regenerate. The subtraction
itself went far enough without going too far."
"""
import subprocess, os, sys, numpy as np

SR = 44100
BEAT = 60.0 / 128.0
BAR = 4 * BEAT
NFFT, HOP = 2048, 512
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
# Franco ratified this exact chain on skate ("V10 landed. Keep the 55 ms window
# at 7 dB"), so it is now the standard subtraction for every world.
SRC = sys.argv[1] if len(sys.argv) > 1 else "V8_SKATE_b.mp3"
OUT = sys.argv[2] if len(sys.argv) > 2 else "V10_SKATE_locked.wav"

# Franco's dB range is 6-8; the equal-power ramps eat into a 35 ms window, so
# widen the window rather than exceed his depth spec.
MID_DUCK_DB, DUCK_MS = -7.0, 55
TAIL_TRIM_MS = 100
SC_DEPTH_DB, SC_MS = -2.5, 75
EDGE_MS = 8            # Franco: "5-10 ms equal-power fades"
TARGET = 0.75


def decode(path):
    raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","2","-ar",str(SR),
                          "-f","f32le","-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64).reshape(-1,2)


def bandpass(x, lo, hi):
    n = len(x); X = np.fft.rfft(x, axis=0); f = np.fft.rfftfreq(n, 1/SR)
    m = ((f >= lo) & (f <= hi)).astype(float)
    k = max(1, int(len(f)*0.0015)); ker = np.hanning(2*k+1); ker /= ker.sum()
    m = np.convolve(m, ker, mode='same')
    return np.fft.irfft(X * m[:,None], n=n, axis=0)


def spectro(mono):
    w = np.hanning(NFFT)
    return np.array([np.abs(np.fft.rfft(mono[i:i+NFFT]*w))
                     for i in range(0, len(mono)-NFFT, HOP)])


f_ax = np.fft.rfftfreq(NFFT, 1/SR)
MID = (f_ax > 300) & (f_ax < 2000)
LOWB = (f_ax > 40) & (f_ax < 120)


def strict(mono):
    S = spectro(mono); e = S[:,MID].mean(axis=1)
    d = np.diff(e, prepend=e[0]); d[d<0]=0
    rel = d/(e+1e-9)
    idx=[i for i in range(1,len(d)-1) if rel[i]>0.8 and d[i]>=d[i-1] and d[i]>d[i+1]]
    return np.array(idx)*HOP/SR, len(idx)/(len(mono)/SR)


def eq_power_dip(env, start_s, width_s, depth_db, edge_s):
    """Write a dip into `env` IN PLACE with cosine ramps both directions.
    Because we only ever multiply a continuous envelope, no step can occur."""
    n = len(env)
    g = 10 ** (depth_db/20)
    e = max(2, int(edge_s*SR))
    a = int(start_s*SR); b = int((start_s+width_s)*SR)
    a = max(0, a); b = min(n, b)
    if b - a < 2*e:
        return
    down = 1 - (1-g)*(1-np.cos(np.linspace(0,np.pi,e)))/2      # 1 -> g
    up   = g + (1-g)*(1-np.cos(np.linspace(0,np.pi,e)))/2      # g -> 1
    seg = np.concatenate([down, np.full(b-a-2*e, g), up])
    env[a:b] = np.minimum(env[a:b], seg)


x = decode(os.path.join(MUS, SRC)); n = len(x); dur = n/SR
mono = x.mean(axis=1)
_, before = strict(mono)
print(f"{SRC}  {dur:.1f}s   mid onset BEFORE {before:.2f}/s\n")

low  = bandpass(x, 0, 300)
mid  = bandpass(x, 300, 2000)
high = bandpass(x, 2000, SR/2)

# ---- 1. mid-band transient duck (continuous envelope) ------------------
t_mid, _ = strict(mono)
# Escalate the WINDOW, not the depth — Franco specified 6-8 dB and the final
# measurement must be taken on the finished chain, not the mid band al***REMOVED***
width = DUCK_MS
for _ in range(6):
    env = np.ones(n)
    for t in t_mid:
        eq_power_dip(env, t, width/1000, MID_DUCK_DB, EDGE_MS/1000)
    _, r = strict((low + mid*env[:,None] + high).mean(axis=1))
    print(f"  mid duck {MID_DUCK_DB:.1f} dB x {width:3.0f} ms -> {r:.2f}/s")
    if r < TARGET - 0.08: break     # headroom, since sidechain nudges it up
    width += 15
mid = mid * env[:,None]

# ---- 2. final bar rolloff, with a ramp INTO it ------------------------
# Franco called this the one borderline move; keep 9 dB for now but ramp in
# over 40 ms so the boundary itself is not a step.
fb = np.ones(n)
start = max(0, n - int(BAR*SR))
ramp = int(0.040*SR)
tgt = 10 ** (-9/20)
fb[start:start+ramp] = np.linspace(1, tgt, min(ramp, n-start))
fb[start+ramp:] = tgt
mid  *= fb[:,None]
high *= fb[:,None]
print(f"\nfinal bar: -9 dB with a {ramp/SR*1000:.0f} ms ramp in")

# ---- 3. 808 tails — ONE continuous envelope, both edges ramped --------
lowmono = low.mean(axis=1)
Sl = spectro(lowmono); el = Sl[:,LOWB].mean(axis=1)
dl = np.diff(el, prepend=el[0]); dl[dl<0]=0
cut = np.percentile(dl[dl>0], 90) if (dl>0).any() else 0
gap = int(0.12*SR/HOP)
notes, last = [], -gap
for i in range(1, len(dl)-1):
    if dl[i]>cut and dl[i]>=dl[i-1] and dl[i]>dl[i+1] and i-last>=gap:
        notes.append(i*HOP/SR); last=i

tail_env = np.ones(n)
trimmed = kept = 0
for j, t in enumerate(notes):
    nxt = notes[j+1] if j+1 < len(notes) else dur
    if (t % (2*BAR)) > (2*BAR - 0.35):     # featured slide — preserve
        kept += 1; continue
    # dip the last TAIL_TRIM_MS before the next note, ramped both ways,
    # and finish clear of the next onset so the attack is untouched
    w = TAIL_TRIM_MS/1000
    st = max(t, nxt - w - EDGE_MS/1000)
    if nxt - st < 2*EDGE_MS/1000: continue
    eq_power_dip(tail_env, st, nxt - st - 0.002, -60, EDGE_MS/1000)
    trimmed += 1
low = low * tail_env[:,None]
print(f"808 tails: {len(notes)} notes, {trimmed} trimmed with {EDGE_MS} ms "
      f"equal-power fades both ends, {kept} featured slides preserved")

# ---- 4. sidechain -----------------------------------------------------
sc = np.ones(n)
kicks = np.arange(0, dur, BEAT)
for k in kicks:
    eq_power_dip(sc, k, SC_MS/1000, SC_DEPTH_DB, EDGE_MS/1000)
out = (low + mid + high) * sc[:,None]
print(f"sidechain: {len(kicks)} dips, {SC_DEPTH_DB} dB / {SC_MS} ms, ramped")

# ---- verify NO discontinuities remain ---------------------------------
d1 = np.abs(np.diff(out.mean(axis=1)))
thr = np.percentile(d1, 99.995) * 4
bad = np.where(d1 > thr)[0]
print(f"\ndiscontinuity scan: {len(bad)} samples exceed 4x the 99.995th pct")
if len(bad):
    print("  at:", ", ".join(f"{b/SR:.3f}s" for b in bad[:12]))

peak = np.abs(out).max()
if peak > 0.99: out *= 0.99/peak

dst = os.path.join(MUS, OUT)
p = subprocess.Popen(["ffmpeg","-y","-v","error","-f","f32le","-ar",str(SR),
                      "-ac","2","-i","-","-c:a","pcm_s24le",dst], stdin=subprocess.PIPE)
p.communicate(out.astype(np.float32).tobytes())
subprocess.run(["ffmpeg","-y","-v","error","-i",dst,"-b:a","192k",
                os.path.join(MUS, OUT.replace('.wav','.mp3'))])
_, after = strict(out.mean(axis=1))
print(f"\nmid onset AFTER {after:.2f}/s  {'PASS' if after<TARGET else 'FAIL'}")
print(f"wrote {OUT} + .mp3")
