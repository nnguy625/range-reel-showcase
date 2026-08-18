# Range Reel — an AI Video Production System

One human director, two AI agents, and a written operating system that turns generative video
into a disciplined, measurable production pipeline. This repository is the working system for a
90-second, six-world AI performance reel (Seedance 2.0 / 2.5 via Higgsfield), beat-locked to an
original 128 BPM track. Status: in production — World 1 locked, World 2 in assembly, Worlds 3–6 at
the asset and prompt-test stage.

**What this mirror is:** a curated public copy of the working repository. The technical
production history — prompts, defects, rules, measurements, defect-linked commits — is
preserved. Curation was done by rewriting this mirror's history, and here is exactly what that
means: removed — private links and thread IDs, credit balances and the vendor project ID, session artifacts, two vendor access methods, a
community-render study and its reviewer ledgers (they quoted other users' prompts), the World 2
hip-bounce prompt family (24 versions of one motion asset), two dashboards with embedded images,
and a handful of words in old commit messages; left as they were — the operator's working files
(STATE.md, CLAUDE.md, the session ledgers), plan names, and every technical claim, number and
defect. Those files are part of the method, not polish, and
they read like it. See [Docs/README.md](Docs/README.md) for the map.

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
those decisions as they happened — so when a commit or a document says "locked by Franco" or
"Franco ruling", it means the reviewer's recommendation was adopted by the director; the reviewer
never had authority to decide.

## What I do and what the agents do

I set the creative direction, choose the references, define what each shot has to accomplish, decide
what gets generated, and make the final pass or kill decision. For the QA tools, I define what needs to
be measured, set the test cases and thresholds, and check the results.

Claude Code handles execution inside that system. It turns my decisions into working prompt documents,
maintains production state, runs measurements, and implements tooling from the requirements and tests I
give it. Franco is a separate reviewer I use to challenge plans and results before I make the final call.

The working logs preserve the agents' original first-person voice. When an old commit or ledger entry
says "I," it may be Claude describing what it did or got wrong. I left that history intact instead of
rewriting it to sound like I personally typed everything.

## How the production works — the 60-second version

1. **Every locked shot's prompt is on record** — World 1 clip 1 as `Docs/PROMPT_W1_CLIP1.md`; World 1
   clip 2 and the World 2 opener as fire records recovered from the platform's job history
   (`Docs/PROMPT_W1_CLIP2_FIRE_RECORD.md`, `Docs/PROMPT_W2_CLIP1_A16_FIRE_RECORD.md`): settings, attached
   references, full prompt text. Nothing is fired from memory.
2. **Every prompt is reviewed before it spends anything** — an adversarial review pass, plus a
   line-by-line audit of the prompt against the director's stated requirements.
3. **Take selection is gated by measurement wherever a gate exists** — motion tempo by
   per-frame centroid tracking of the costume mask, audio lineage by FFT alignment plus
   per-second correlation against the attached track, timing on a frame-exact 128 BPM grid
   (1 beat = 0.46875 s = 11.25 frames at 24 fps). Composition and performance are still judged
   by eye, and the record says which was which.
4. **Every failure becomes a written rule**, documented against the exact render that produced
   it. The rules accumulate in [CLAUDE.md](CLAUDE.md) and the prompt documents, so a lesson is
   re-learned less often — and the ledger records the times it was re-learned anyway.
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
  sweeps, self-rejecting seam gates, audio-lineage and motion-tempo gates (numpy, ffmpeg), with a
  test suite (`py -m pytest Tools/tests`) and the instruments' raw JSON output for the takes the
  case study cites in [Tools/results/](Tools/results). See [Tools/README.md](Tools/README.md) for
  the map and the known limits.

## Method notes

- Workflow rules here were each derived from a failing render and documented against it — on
  tempo, timing and audio lineage, accept/reject is a number, not an opinion. They are observed
  heuristics from this project's renders on Seedance 2.0 / 2.5, at the sample sizes the documents
  state; not claims about the models.
- Motion references: real skate and dance footage guided specific moves — text-only kickflips kept
  morphing the board, and text-only choreography produced invented dances — so short fragments of
  real motion, one move each, were attached as motion references and combined into the
  choreography. Nothing from them is rendered into the output, and no third-party media is
  included in this repository.
- Every likeness of the performer is generated from reference sheets she sat for, with her consent.
- Film titles appear in the design documents as tone and choreography references (the way a shot list
  says "a Bond-film look"); after the 2026-07-31 moderation finding no title appears in a fired prompt,
  and no third-party media or text is included in this repository.
- Tooling is built through AI-assisted development: requirements definition, testing, and
  iteration by the director; implementation with coding agents.
- The commit history is part of the work: defect-linked messages and preserved decisions, with
  private material curated out of the public mirror.
