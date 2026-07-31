# RANGE REEL — MID-AUGUST WAR PLAN
### Drafted 2026-07-30 (Fable). Deadline: **picture lock Aug 12 · ship Aug 15 · buffer to Aug 17.**
### This is the execution authority until superseded. STATE.md points here.

---

## 0. THE HONEST POSITION

**16 days.** The reel has a fixed delivery date — treat the date as hard.

What is genuinely DONE and closed:
- **Music: 100%.** Master premaster level-ruled, all six worlds Franco-locked, lattice ratified in practice. Cut picture to `MASTER_90_v5_PREMASTER`. Nothing audio blocks anything.
- **Character system: 100%.** All six worlds have face + wardrobe elements. Props built (skateboard, gun, katana, both cars ext, one car interior).
- **Locations: ~90%.** Five locations plated; hotel corridor replaced the industrial corridor and has SIX plates including the purpose-built `@Loc-Hotel-Money`.
- **The prompt system: SOLVED this week.** This was the actual risk burning the schedule — four rejects on one shot. Now: register per model (narrative nano / template GPT2), global light model, photoreal integration block, film-anamorphic look spec, `REFERENCE ONLY` header, 2K iteration. Nelson is writing passing prompts himself; Franco QA's them at one round each. **The factory works.**
- **Boards:** W1 saved, W2 rendered (needs saving), W4 logic written, W3 logic superseded by the hotel work (effectively done at shot level), W5/W6 outstanding but derivable via `DIRECTING_SYSTEM.md`.

What is NOT done: **plates (the volume), the 720 test, the paid generation sprint, the edit.** All downstream of a prompt system that now works.

---

## 1. CRITICAL PATH (dates)

| Date | Milestone | Owner | Gate |
|---|---|---|---|
| **Jul 31** | W3 money shot LANDS (rounds 07/08 verdict + sibling picks) · harvest Franco's **5 SD2 patches** + **W1-continuous ruling** · Nelson answers **D1–D6** | Both | D-batch |
| **Aug 1–5** | **PLATE FACTORY.** Seam-first: ① W1-S4-end + W2-S1-start ② W3-S4-end + W4-S1-start ③ W2-S4-end + W3-S1-start (needs D1) ④ W4-S4 neutral exit. Then per-world starts/ends W1→W4, W5 grade round + W5/W6 plates. I pre-draft every prompt; Nelson fires in ~40-min batch sessions, ×4 siblings | Pablo drafts / Nelson fires | plate-gate QA |
| **Aug 6** | 🚧 **720 TEST DAY** (Franco's ruling, step 5): one seam pair + one normal shot + protocol tests — first-frame literalness, 15s audio cap, beat-follow, ref-count recipe (3 vs 5 assets) | Nelson | **THE gate** |
| **Aug 7** | Patch the input recipe from test results · finish remaining plates under corrected recipe | Both | — |
| **Aug 8–10** | **SD2 GENERATION SPRINT** — the one paid window (720 unlimited day(s), D5). W1-continuous test FIRST (if one 15s take works, W1 = 1 generation instead of 4). All 24 shots, 2–4 takes, keeper-select same day | Nelson | keeper bank full |
| **Aug 11–12** | **EDIT.** Resolve assembly on the half-bar lattice against the premaster. J/L seams on world cuts, micro-gap alignment, speed ramps. **Picture lock Aug 12** | Nelson (Pablo: cut list) | lock |
| **Aug 13** | Topaz upscale pass · grade-consistency pass · final loudness (premaster → delivery level) | Both | — |
| **Aug 14** | Export + the landing page (reel + 6 stills + one-paragraph method note) | Both | — |
| **Aug 15** | **DELIVER.** Final export handed off | Nelson | 🚢 |
| Aug 16–17 | Buffer (assume something eats it) | — | — |

**Math check:** ~36 plates over 5 factory days ≈ 7–8 approvals/day at ×4 siblings ≈ 30 generations/day on Unlimited ≈ one 40-min session + one QA pass. Tight but real — **the constraint is Nelson's firing/QA minutes, not credits or prompts.** Everything I can pre-stage, I pre-stage.

---

## 2. THE DECISION BATCH — D1–D6 (≈5 minutes, unblocks the factory)

| # | Decision | Blocks | Default if silent |
|---|---|---|---|
| **D1** | Drape entry: **head-on toward camera in BOTH W2 and W3**, or 3/4 in both? | Seam ③ | head-on (your W2→W3 travel note implies it) |
| **D2** | Save the 4 boards from the Franco thread (only you can — renderer blocks me) | board refs | one 15-min save session |
| **D3** | SD2 identity refs: I draft **single-panel** face-crop + full-body prompts per world (free, no grid slicing, no lineage taint) — approve the batch? | twins-bug prevention | yes |
| **D4** | Skill-store sync (`robocopy` desktop→CLI, `/XO`) | my prompt fidelity | run it |
| **D5** | **720 unlimited day = Aug 8?** (test day Aug 6 runs on per-gen credits or same window — your call on budget shape) | the sprint | Aug 8 |
| **D6** | Motion refs for kickflip / tumble / drift: film yourself on phone (best) or I source generic clips? | the 3 hardest shots | phone, 10 min |

---

## 3. MODEL PLAYBOOK (settled this week — the research is done, stop re-litigating)

| Job | Model | Register |
|---|---|---|
| Environment/plate builds, camera-geometry shots | **Nano Pro, 2K** | narrative sentences, global light (sources+reach+falloff), positives only, film-anamorphic close |
| Identity-critical face CUs, fine markers | **GPT2 (now Unlimited)** | template, indexed refs by tag, invariant list restated per iteration, "photorealistic" literal |
| Video | **SD2** | my ratified structure + Franco's 5 patches (harvest Jul 31) · per-shot audio slice w/ 1-bar preroll (`Tools/slice_shot_audio.py`) · start frame is the literal frame 1 — feed 2K→Topaz-4K plates only |
| Beat matching | **SD2 native** | it choreographs to the audio's beat structure — feed the **spine slice** (fence posts), never the premaster |

Docs: `MODEL_PROMPT_REGISTERS.md` · the World 3 plate review loop (kept private) · memory: `spec-causes-not-appearances`, `photoreal-plate-levers`, `prompt-register-differs-per-model`.

---

## 4. RISK REGISTER (top 6)

| Risk | P× impact | Mitigation |
|---|---|---|
| Plate volume slips | HIGH | pre-drafted prompts + batch sessions + **W5/W6 boards derived from DIRECTING_SYSTEM instead of new Franco rounds if he stays degraded** |
| W2 crowd shot (ring of dancers) destabilises | HIGH | grouped 3-dancer plates first (SD2 guide law); if still unstable, choreo reads on **her + 2** |
| Fast-action trio (kickflip/tumble/drift) breaks physics | MED | D6 motion refs + slow-in-shot + split beats; the 720 test includes one |
| Franco stays blind (can't see images) | MED | Nelson attaches in-thread; **Pablo is the image-QA lane**, Franco rules on text/structure |
| First-frame assumption wrong (SD2 re-renders frame 1) | MED | explicit Aug 6 test; if conditioning-only, plates still work as strong refs |
| The 3→4 cut (weakest by design) | MED | OTS grip→wheel match already ruled; protect: nothing else changes across that seam |

**Cut from critical path:** the BTS piece (phase 5) and the ~40s vertical — post-ship work. The animatic-as-gate is **superseded** by the seam-first + 720-test method (Franco's own later ruling); noting it so STATE stops pointing at it.

---

## 5. FREE AUTOMATION — DONE TODAY
- Repo pushed (was **8 commits ahead**, never pushed — now verified in the loop).
- Six 15.000s world guide refs sliced sample-exact: `Assets/Music/SD2_GUIDE_REFS/`.
- `Tools/slice_shot_audio.py` — per-shot slice + preroll, calibration control in the docstring, 15s-cap guard.
- STATE.md re-anchored to this plan.
- Tracker artifact (Gantt) published + emailed.

## 6. MY STANDING QUEUE (no ask needed)
1. Harvest Franco msgs 105–114 verbatim → `FRANCO_DECISIONS.md` (the 5 patches, W1-continuous, his register verification).
2. Pre-draft the four seam-plate prompts (nano register) + the D3 single-panel batch + W1-continuous SD2 prompt.
3. Nightly: commit + **push** + memory mirror + tracker refresh.
4. QA lane for every sibling set you drop.

## 7. PATTERNS (the improvement notes you asked for)

**Yours — keep/adjust:**
- **Your simplify-instinct is reliably right** (global light, "concise it more", ELI5 register — all yours, all wins). Codified into the skill lane. Trust it earlier; when output fights, simplify before adding.
- **Decisions arrive scattered** across voice notes and mid-turn messages → they now come back to you as **D-batches**. Answer once, factory runs.
- **You-only bottlenecks** (board saves, audio drag-ins, generation firing) — batch them into one session per day rather than interleaving; context-switching is your scarcest resource.
- **Sibling discipline:** judge on 4, not 2. Identical prompts measured 0.23 vs 0.90 — a verdict on 2 takes is a coin read.

**Mine — fixed autonomously:**
- Two "answer was already in memory" failures in one day (lighting law, Gmail traps) → **file-first law re-tattooed**; this plan exists partly so neither of us re-derives settled things.
- The unpushed-repo gap → push is now part of every commit loop.
- STATE.md had gone two pivots stale → re-anchored; it now points here.
