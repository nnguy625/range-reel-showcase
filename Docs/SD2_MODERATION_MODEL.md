# SD2 MODERATION — THE LANE-THRESHOLD MODEL (Franco-aligned, 2026-08-01)

Nelson called it: *"something's there in the prompt that's not allowing it. I'm standing firm w/ this."*
He was right. Two of my diagnoses died on the way here (location-element theory: my own truncated read;
nondeterminism claim: I conflated lanes — prompt A's one pass was on CREDITS, so inputs were never identical).

## The full table — all 13 SD2 jobs, verbatim prompts pulled from API params

| Prompt class | ~chars | Unlimited lane | Credit lane |
|---|---|---|---|
| **Ref-roles only** (accidental truncation; NO action/phases/camera/look) | 1.3k | **1/1 PASS** | — |
| **Lean A** (refs + board + first frame + timed phases + camera + look) | 2.0k | 0/3 | **1/1 PASS** |
| **Full contract** (+ physics + positive locks) | 4k+ | 0/~6 | 0/2 |

Constant across ALL jobs: `@Pao-Urban` + `@Loc-SoCal-Street` elements, same audio file, mode=std,
generate_audio=true, speedramp=auto, genre=auto, 4K, 8s, 16:9. **Assets and audio are not separating
variables. The elements are cleared.**

## The model (operating model, not proven mechanism)

**Prompt content sets a score; the lane sets the threshold; Unlimited is stricter than credits.**

```
score(ref-only)  <  UNLIMITED bar  <  score(lean A)  <  CREDITS bar  <  score(full contract)
```

Fits all 13 outcomes with zero noise. Franco's record wording: *"In observed tests, the unlimited route
accepts the reference-only prompt but rejects Lean A and the full prompt. The credit route accepts Lean A
but rejects the full prompt. This supports **lane-dependent prompt-complexity thresholds**, pending repeated
baseline confirmation."* NOT proven: same classifier vs separate pipelines; monotonic-in-length; full
determinism.

## Theories this table killed

- **Legal-vocab scrubbing.** The ONLY strict-lane pass carries ALL of it — "unbranded, no logos, no brand
  marks, sole authority, exact." It passed in the full contract costume. The scrub did nothing.
- **Nondeterminism under identical inputs.** Never demonstrated; lane was conflated.
- **Location element / audio / Paola element as triggers.** Identical across passes and refusals.

## Suspect ranking (Franco)

1. **Cumulative operative density** — total actionable content the moderator must score. The full contract
   failing on CREDITS while lean A passed there says added Physics+Locks can push over even the loose bar.
2. **Explicit action-to-audio synchronization** — ref-only says "timing authority" but stages no action to
   musical events; lean A adds "on the music" + timed phases. Could route into a stricter music-use check.
3. **The action body itself** — media-production shape; but generic skating, not recognizable choreography.
4. **Bare timecodes** — common production notation; weakest al***REMOVED***

## THE ADAPTIVE STRICT-LANE LADDER

Fire each step TWICE on Unlimited. Base = the verbatim ref-only prompt (the known pass).

- **Step 0** — base, verbatim, twice. Any refusal → threshold model weakens; fire a third; split after
  three → stop block attribution.
- **Step 1** — + plain FORMAT only ("One continuous 8-second shot, 16:9, no cuts."). No timecodes.
- **Step 2** — + the action in ordinary prose, UNTIMED, no "on the music."
- **Step 3** — + one sync line: "The carve lands on the strongest musical accent."
- **Step 4** — swap untimed action for the TIMED phase structure (no camera/look yet).
- **Step 5** — + concise camera path + one look line (= lean A, known 0/3, to close the loop).

**Interpretation:** first step that flips pass→refuse names the threshold-crossing block. If every isolated
addition passes but lean A still refuses → **cumulative score / interaction**, not one poisoned block.

## Production posture (Franco-confirmed)

- **Credits run Lean A for hero production NOW.** Diagnostics never block clips.
- **Unlimited runs the ladder** in parallel at zero cost.
- **Never submit full-contract prompts on credits** (observed 0/2).
- Arithmetic corrected: refusals REFUND, so the balance ≈ **29 COMPLETED 4K generations**, not 29
  attempts. The real burn is completions that are creatively unusable — sibling QA matters more than
  refusal rate on the credit lane.

## Meta

Two false diagnoses in one day, same root: **analysis from a partial read** (a 300-char-truncated array;
a lane-blind table). The fix that worked both times: pull the PRIMARY record (API params, ledger),
verbatim, before claiming a cause.
