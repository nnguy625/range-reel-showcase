# Range Reel — AI Performance-Reel Production System

Working repository for a 90-second, six-world AI performance reel (Seedance 2.5 / Higgsfield),
beat-locked to an original 128 BPM track. Published as a showcase of the production system
itself: locked prompt documents, measured QA tooling, and model-behavior findings — with the
full defect-linked commit history as the receipts.

## Where to look

- **[Docs/STATE.md](Docs/STATE.md)** — the production state anchor: how any session (human or
  agent) cold-starts into the project without re-teaching.
- **[Docs/PROMPT_W1_CLIP1.md](Docs/PROMPT_W1_CLIP1.md)** — a locked shot prompt document.
- **[Docs/SD2_GUIDE_FINDINGS.md](Docs/SD2_GUIDE_FINDINGS.md)** — vendor guide vs. measured
  behavior of the model in production.
- **[Docs/SD2_MODERATION_MODEL.md](Docs/SD2_MODERATION_MODEL.md)** — a 13-job controlled study
  of platform moderation, one variable per test, spend logged: rejection risk priced before
  generating.
- **[Tools/](Tools)** — Python QA/DSP tooling: 128 BPM beat-grid audio assembly, 1ms alignment
  sweeps, self-rejecting seam gates, FFT audio-lineage checks (numpy, ffmpeg).
- **[Inspiration/](Inspiration)** — prompt-vs-render study captures of publicly released
  community work (verbatim prompt, then measured delta between what was asked and what rendered).

## Method

- Every workflow rule in this repo was derived from a **failing render** and documented against
  it. Continuity, tempo, and audio integrity are **measured** (per-frame centroid tracking, FFT
  cross-correlation), not eyeballed.
- Tooling is built through AI-assisted development: requirements definition, testing, and
  iteration by me; implementation with coding agents.
- The commit history is part of the work: defect-linked messages, no squashed cover-ups.
