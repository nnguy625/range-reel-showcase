"""
W2 CLIP-2 CARRIER AUDIT + MUSIC MAP
====================================
Two questions:

1. ALIGNMENT. Clip 1 is LOCKED on CANDIDATE_CARRIER_W2_CLIP1_V16_7137_8s.wav (source 7.137).
   The existing clip-2 carrier is CARRIER_W2_CLIP2_V16_14900_8s.wav (source 14.900), which was
   cut to pair with the SUPERSEDED 7.400 clip-1 cut (14.900 - 7.400 = 7.500 exactly).
   If clip 1 is really at 7.137 and delivers 7.500s of picture, clip 2 must start at
   7.137 + 7.500 = 14.637 -- so the existing carrier would be 0.263s LATE.
   Verified here by cross-correlation, not by arithmetic al***REMOVED***

2. MUSIC MAP for whichever clip-2 carrier is correct, so the six timecoded beats can be
   anchored to audible events (the condition that made A-15 work) rather than to arbitrary
   slices.

numpy only -- no librosa on this machine. Onsets via half-wave-rectified spectral flux.
"""
import wave, numpy as np

CAR = 'Assets/Music/AUDIO_CARRIERS/'


def read(path):
    w = wave.open(path)
    sr, n, ch = w.getframerate(), w.getnframes(), w.getnchannels()
    x = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float64)
    w.close()
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x / 32768.0, sr


def best_offset(needle, hay, sr, probe_s=2.0):
    """Lag in seconds aligning `needle` inside `hay`, via FFT cross-correlation.

    Normalised by a sliding-window RMS of `hay` so a loud passage cannot win on
    amplitude al***REMOVED*** Sample-accurate (1/48000 s) and effectively instant.
    """
    n = needle[:int(probe_s * sr)]
    n = n - n.mean()
    nn = np.sqrt(np.dot(n, n)) + 1e-12
    L = len(hay) + len(n)
    N = 1 << int(np.ceil(np.log2(L)))
    corr = np.fft.irfft(np.fft.rfft(hay, N) * np.conj(np.fft.rfft(n, N)), N)[:len(hay) - len(n) + 1]
    # sliding energy of hay over the probe length
    cs = np.concatenate([[0.0], np.cumsum(hay * hay)])
    seg_e = cs[len(n):] - cs[:-len(n)]
    denom = np.sqrt(np.maximum(seg_e[:len(corr)], 1e-12)) * nn
    r = corr / denom
    lag = int(np.argmax(r))
    return lag / sr, float(r[lag])


def flux(x, sr, hop=256, win=1024):
    """Half-wave-rectified spectral flux onset envelope + its time base."""
    w = np.hanning(win)
    frames = 1 + (len(x) - win) // hop
    S = np.empty((frames, win // 2 + 1))
    for i in range(frames):
        S[i] = np.abs(np.fft.rfft(x[i * hop:i * hop + win] * w))
    d = np.diff(S, axis=0)
    env = np.maximum(d, 0).sum(axis=1)
    env = env / (env.max() + 1e-12)
    return env, (np.arange(len(env)) * hop + win / 2) / sr


def onsets(env, t, thresh=0.18, min_gap=0.08):
    """Peak-pick the envelope; returns onset times in seconds."""
    out = []
    for i in range(1, len(env) - 1):
        if env[i] >= thresh and env[i] > env[i - 1] and env[i] >= env[i + 1]:
            if not out or t[i] - out[-1] >= min_gap:
                out.append(float(t[i]))
    return out


def band_energy(x, sr, lo, hi, hop=2048):
    """Mean magnitude in a frequency band per hop -- used to find section boundaries."""
    win = 4096
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1 / sr)
    sel = (freqs >= lo) & (freqs < hi)
    frames = 1 + (len(x) - win) // hop
    e = np.empty(frames)
    for i in range(frames):
        e[i] = np.abs(np.fft.rfft(x[i * hop:i * hop + win] * w))[sel].mean()
    e = e / (e.max() + 1e-12)
    return e, (np.arange(frames) * hop + win / 2) / sr


if __name__ == '__main__':
    world, sr = read(CAR + 'W2_WORLD_15s_V16_7400.wav')      # source[7.400 : 22.400]
    c1_lock, _ = read(CAR + 'CANDIDATE_CARRIER_W2_CLIP1_V16_7137_8s.wav')
    c1_old, _ = read(CAR + 'CARRIER_W2_CLIP1_V16_7400_8s.wav')
    c2, _ = read(CAR + 'CARRIER_W2_CLIP2_V16_14900_8s.wav')

    print('=== 1. ALIGNMENT (offsets measured INSIDE the 15s world, which starts at source 7.400) ===')
    for name, sig in [('clip1 LOCKED (7137)', c1_lock),
                      ('clip1 old    (7400)', c1_old),
                      ('clip2 exist  (14900)', c2)]:
        lag, r = best_offset(sig, world, sr)
        print(f'  {name}: world-offset {lag:+.4f}s  (source {7.400 + lag:.4f})  corr {r:.3f}')

    lag1, _ = best_offset(c1_lock, world, sr)
    lag2, _ = best_offset(c2, world, sr)
    gap = lag2 - lag1
    print(f'\n  measured clip1 -> clip2 spacing: {gap:.4f}s')
    print(f'  required spacing (clip 1 delivers 7.500s of picture): 7.5000s')
    print(f'  ERROR: {gap - 7.5:+.4f}s   -> correct clip-2 source start = {7.400 + lag1 + 7.5:.4f}')

    print('\n=== 2. MUSIC MAP of the EXISTING clip-2 carrier (14900) ===')
    env, t = flux(c2, sr)
    ons = onsets(env, t)
    print(f'  onsets ({len(ons)}): ' + ', '.join(f'{o:.3f}' for o in ons))

    lowe, lt = band_energy(c2, sr, 30, 160)
    mide, _ = band_energy(c2, sr, 300, 2000)
    print('\n  low-band (30-160Hz, drums/bass) by 0.25s:')
    print('   ' + ' '.join(f'{v:.2f}' for v in lowe))
    print('  mid-band (300-2000Hz, strings/plucks) by 0.25s:')
    print('   ' + ' '.join(f'{v:.2f}' for v in mide))
    print('   time base: ' + ' '.join(f'{v:.2f}' for v in lt))

    gaps = []
    for a, b in zip(ons, ons[1:]):
        if b - a >= 0.20:
            gaps.append((a, b))
    print(f'\n  attack-free gaps >=0.20s ({len(gaps)}): ' +
          ', '.join(f'{a:.2f}-{b:.2f}' for a, b in gaps))
