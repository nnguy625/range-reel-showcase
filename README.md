# Range Reel — an AI Video Production System

One human director, two AI agents, and a written operating system that turns generative video
into a disciplined, measurable production pipeline. This repository is the working system for a
90-second, six-world AI performance reel (Seedance 2.5 / Higgsfield), beat-locked to an original
128 BPM track.

**What this mirror is:** a curated public copy of the working repository. The technical
production history — prompts, defects, rules, measurements, defect-linked commits — is
preserved intact. Private material (account data, third-party source copies, personal session
context) has been removed. The curation commits are visible; nothing technical was rewritten.

**Scope:** this repository showcases the *Performance Reel* production system. The *Original AI
Short Film* (and its 19-file agent-executable playbook) and the *REVEIL* local-generation
pipeline are separate private productions.

## Who's who (names you will see throughout the documents)

These documents are working production records, and they name their operators:

- **Nelson** — the human director and operator. Every creative decision and every credit spent
  is his call.
- **Pablo** — the executing AI agent (Claude). Writes prompt documents, runs QA measurements,
  maintains production state, and operates under the written rules in [CLAUDE.md](CLAUDE.md).
- **Franco** — a second, independent AI used as an adversarial reviewer. Prompts and plans are
  war-gamed against Franco before anything generates; his standing instruction is to refute,
  not agree.

Decisions flow one way: the agents advise and execute, the human decides. The documents record
those decisions as they happened.

## How the production works — the 60-second version

1. **Every shot has a written, versioned prompt document** (`Docs/PROMPT_*.md`): settings,
   attached references, and the full prompt text. Nothing is fired from memory.
2. **Every prompt is reviewed before it spends anything** — an adversarial review pass, plus a
   line-by-line audit of the prompt against the director's stated requirements.
3. **Every generated take is measured, not eyeballed** — motion tempo by per-frame centroid
   tracking, audio integrity by FFT cross-correlation, timing on a frame-exact 128 BPM grid
   (1 beat = 0.46875 s = 11.25 frames at 24 fps).
4. **Every failure becomes a written rule**, documented against the exact render that produced
   it. The rules accumulate in [CLAUDE.md](CLAUDE.md) and the prompt documents — the system
   gets permanently smarter and never re-learns the same lesson.
5. **State survives sessions.** [Docs/STATE.md](Docs/STATE.md) is the session-state anchor: any new
   session, human or agent, cold-starts from it without re-teaching.

## Where to look

- **[Docs/STATE.md](Docs/STATE.md)** — the production state anchor.
- **[Docs/PROMPT_W1_CLIP1.md](Docs/PROMPT_W1_CLIP1.md)** — a locked shot prompt document.
- **[Docs/SD2_GUIDE_FINDINGS.md](Docs/SD2_GUIDE_FINDINGS.md)** — the platform's published guidance versus
  the model's measured behavior in production.
- **[Docs/SD2_MODERATION_MODEL.md](Docs/SD2_MODERATION_MODEL.md)** — a controlled analysis
  across 13 logged generation jobs: how the platform's moderation behaves by lane, so rejection
  risk is priced before generating.
- **[Tools/](Tools)** — Python QA/DSP tooling: 128 BPM beat-grid audio assembly, 1 ms alignment
  sweeps, self-rejecting seam gates, FFT audio-lineage checks (numpy, ffmpeg). See
  [Tools/README.md](Tools/README.md) for a map.

## Method notes

- Workflow rules here were each derived from a failing render and documented against it —
  accept/reject decisions are numbers, not opinions.
- Tooling is built through AI-assisted development: requirements definition, testing, and
  iteration by the director; implementation with coding agents.
- The commit history is part of the work: defect-linked messages and preserved decisions, with
  private material curated out of the public mirror.
