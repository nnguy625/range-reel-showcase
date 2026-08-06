"""
W2 WINDOW BUILDER — give it X, it emits everything.

Usage:  py Tools/w2_build_from_X.py 9.040

Emits, for a chosen W2 start offset X in V16_BOLLY_a:
  - clip 1 carrier (8.000s), verified by cross-correlation against the master
  - clip 2 carrier (8.000s; auto-pads phase-continuously if X pushes past the track end)
  - the full 15.000s W2 world cut
  - the measured onset/drum map for each clip
  - six beat boundaries for each clip, every one snapped to a real onset

Written after a day in which every music decision I made by eye was wrong.
Nothing here is asserted; every cut is verified against the source before it is reported.
"""
import sys, subprocess, wave
import numpy as np

sys.path.insert(0, 'Tools')
from w2_clip2_carrier_audit import read, best_offset, flux, onsets, band_energy

SRC_MP3 = 'Assets/Music/V16_BOLLY_a.mp3'
SRC_WAV = ('Assets/Music/V16_BOLLY_a.wav')
CAR = 'Assets/Music/AUDIO_CARRIERS/'
BAR = 1.875          # 128 BPM, 4/4
PICTURE = 7.500      # kept picture per clip
GEN = 8.000          # generation length


def cut(dst, start, dur):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{start:.4f}', '-i', SRC_MP3,
                    '-t', f'{dur:.4f}', '-ac', '2', '-ar', '48000',
                    '-c:a', 'pcm_s16le', dst], check=True)


def concat(dst, parts):
    lst = CAR + '_bx_list.txt'
    with open(lst, 'w') as f:
        for p in parts:
            f.write(f"file '{p.split('/')[-1]}'\n")
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
                    '-i', lst, '-c', 'copy', dst], check=True)


def snap(targets, ons):
    """snap each target time to the nearest measured onset"""
    return [float(min(ons, key=lambda o: abs(o - t))) for t in targets]


def report(path, label):
    x, sr = read(path)
    env, t = flux(x, sr)
    ons = onsets(env, t)
    lo, tl = band_energy(x, sr, 30, 160, hop=1024)
    dur = len(x) / sr
    print(f'\n--- {label}  ({dur:.3f}s)')
    print('  sec   : ' + ' '.join(f'{s:5d}' for s in range(int(dur))))
    print('  onsets: ' + ' '.join(f'{sum(1 for o in ons if s <= o < s+1):5d}' for s in range(int(dur))))
    print('  drums : ' + ' '.join(f'{lo[(tl>=s)&(tl<s+1)].mean():5.2f}' for s in range(int(dur))))
    head = lo[tl < 0.8]
    print(f'  landing bass peak in first 0.8s: {head.max():.3f}' if len(head) else '')
    # six evenly-spaced beat targets, snapped to real onsets
    tg = [PICTURE * k / 6 for k in range(6)] + [GEN]
    sn = snap(tg[:6], ons) + [GEN]
    print('  SIX BEATS (snapped to measured onsets):')
    for i in range(6):
        print(f'    {sn[i]:6.3f} - {sn[i+1]:6.3f}')
    return ons


if __name__ == '__main__':
    X = float(sys.argv[1])
    src, sr = read(SRC_WAV)
    DUR = len(src) / sr
    print(f'V16_BOLLY_a = {DUR:.4f}s     W2 = {X:.3f} -> {X+15.0:.3f}')
    print(f'clip1 picture {X:.3f}-{X+PICTURE:.3f}   clip2 picture {X+PICTURE:.3f}-{X+15.0:.3f}')
    print(f'W3 handoff at source {X+15.0:.3f}')

    c1 = CAR + f'CARRIER_W2_CLIP1_V16a_{int(X*1000):05d}_8s.wav'
    cut(c1, X, GEN)

    c2_start = X + PICTURE
    c2 = CAR + f'CARRIER_W2_CLIP2_V16a_{int(c2_start*1000):05d}_8s.wav'
    avail = DUR - c2_start
    if avail >= GEN:
        cut(c2, c2_start, GEN)
        print(f'clip2 carrier: {GEN:.3f}s of real music, no padding needed')
    else:
        short = GEN - avail
        # pad phase-continuously from exactly one bar earlier
        cut(CAR + '_bx_main.wav', c2_start, avail)
        cut(CAR + '_bx_tail.wav', DUR - BAR, short)
        concat(c2, [CAR + '_bx_main.wav', CAR + '_bx_tail.wav'])
        print(f'clip2 carrier: {avail:.3f}s real + {short:.3f}s padded from one bar earlier '
              f'(source {DUR-BAR:.3f}); pad sits past the {PICTURE:.3f}s keep-point')

    w = CAR + f'W2_WORLD_15s_V16a_{int(X*1000):05d}.wav'
    cut(w, X, 15.0)

    for p, want in [(c1, X), (c2, c2_start), (w, X)]:
        y, _ = read(p)
        lag, r = best_offset(y, src, sr)
        ok = 'OK' if abs(lag - want) < 0.01 else 'MISMATCH'
        print(f'  verify {p.split("/")[-1]:<44} src {lag:.4f} want {want:.4f} corr {r:.3f}  {ok}')

    report(c1, 'CLIP 1')
    report(c2, 'CLIP 2')
