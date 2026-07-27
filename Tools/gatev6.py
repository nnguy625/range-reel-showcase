"""All four gates on the V6 skate takes."""
import subprocess, os, numpy as np

SR, NFFT, HOP = 44100, 2048, 512
BEAT = 60.0 / 128.0
BAR = 4 * BEAT
WORLD = 8 * BAR
SIX = BEAT / 4
MUS = r"C:\Users\Nelson\Documents\Range Reel\Assets\Music"
NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]


def load(p, hp=None, sr=SR, lo=None, hi=None):
    af = []
    if hp: af.append(f"highpass=f={hp}")
    if lo: af.append(f"highpass=f={lo}")
    if hi: af.append(f"lowpass=f={hi}")
    a = ["ffmpeg","-v","error","-i",p,"-ac","1","-ar",str(sr)]
    if af: a += ["-af", ",".join(af)]
    a += ["-f","f32le","-"]
    return np.frombuffer(subprocess.run(a,capture_output=True).stdout,dtype=np.float32).astype(float)


def spec(x):
    w = np.hanning(NFFT)
    return np.array([np.abs(np.fft.rfft(x[i:i+NFFT]*w)) for i in range(0,len(x)-NFFT,HOP)])


f = np.fft.rfftfreq(NFFT,1/SR)
LOW,MID = (f>40)&(f<120), (f>300)&(f<2000)
BAND = LOW|MID


def strict(S):
    e = S[:,MID].mean(axis=1); d = np.diff(e,prepend=e[0]); d[d<0]=0
    r = d/(e+1e-9)
    return sum(1 for i in range(1,len(d)-1) if r[i]>0.8 and d[i]>=d[i-1] and d[i]>d[i+1])


def events(S):
    e = S[:,BAND].mean(axis=1); d = np.diff(e,prepend=e[0]); d[d<0]=0
    if not d.any(): return np.array([])
    cut = np.percentile(d[d>0],88); gap = max(1,int(0.060*SR/HOP))
    pk,last = [],-gap
    for i in range(1,len(d)-1):
        if d[i]>cut and d[i]>=d[i-1] and d[i]>d[i+1] and i-last>=gap: pk.append(i); last=i
    return np.array(pk)*HOP/SR


# bass root, 16k window
def bassroot(p):
    S2,H2 = 22050,4096; N2=16384
    tot=np.zeros(12)
    for lo,hi in [(30,80),(40,160)]:
        x=load(p,sr=S2,lo=lo,hi=hi)
        w=np.hanning(N2); ff=np.fft.rfftfreq(N2,1/S2); ok=(ff>lo)&(ff<hi)
        pc=np.round(69+12*np.log2(ff[ok]/440.0)).astype(int)%12
        for i in range(0,max(1,len(x)-N2),H2):
            Sx=np.abs(np.fft.rfft(x[i:i+N2]*w))**2; s=Sx[ok]
            for k in range(12): tot[k]+=s[pc==k].sum()
    return int(np.argmax(tot))


spine_root = bassroot(os.path.join(MUS,"E1_MASTER_90.wav"))
sp_ev = events(spec(load(os.path.join(MUS,"E1_MASTER_90.wav"))))
sp = sp_ev[sp_ev<WORLD]
print(f"spine bass root {NAMES[spine_root]}   |  gates: drums<=0.75/s, flams<=5% @ +/-117ms, root=F\n")
print(f"{'take':<18}{'drums/s':>9}{'flams':>8}{'root':>7}{'vs F':>6}  verdict")

import sys
FILES = sys.argv[1:] if len(sys.argv) > 1 else ["V6_SKATE_a.mp3","V6_SKATE_b.mp3"]
for fn in FILES:
    p = os.path.join(MUS,fn)
    x = load(p,hp=100); S = spec(x); dur=len(x)/SR
    drums = strict(S)/dur
    ev = events(S)
    centre = float(np.ceil(ev[0]/BAR)*BAR) if len(ev) else 0.0
    if centre+WORLD>dur: centre=max(0.0,dur-WORLD-2*SIX-0.01)
    best=None
    for lim in (SIX,2*SIX):
        for ms in range(-int(lim*1000),int(lim*1000)+1):
            t0=centre+ms/1000
            if t0<0 or t0+WORLD>dur: continue
            seg=ev[(ev>=t0)&(ev<t0+WORLD)]-t0
            if len(seg)<6: continue
            d=np.abs(seg[:,None]-sp[None,:]).min(axis=1)*1000
            r=float(((d>=15)&(d<=60)).mean()*100)
            if best is None or r<best: best=r
        if best is not None and best<=5.0: break
    r = bassroot(p); dist=abs(r-spine_root); dist=min(dist,12-dist)
    ok = drums<=0.75 and best is not None and best<=5.0 and dist<=1
    print(f"{fn:<18}{drums:8.2f} {best:7.1f}%{NAMES[r]:>7}{dist:>6}  {'PASS' if ok else 'check'}")
