# COST MANAGEMENT PLAN

*Built 2026-07-25 from Nelson's actual Higgsfield transaction ledger, not from published pricing. Nothing was generated to produce this.*

---

## CURRENT POSITION

| | |
|---|---|
| Plan | **Plus** |
| Credit balance | (redacted) |

---

## OBSERVED RATES — from his own transactions

Read directly from 225+ ledger entries.

| Generation | Credits | Evidence |
|---|---|---|
| Nano Banana 2, **Unlimited toggle ON** | **0** | ~220 consecutive entries, all zero |
| Nano Banana Pro, **toggle OFF** | **−4** | One entry, 07-21 16:31. The only non-zero still in the whole history |
| Seedance 2.0 video | **−45** | Five entries across 07-20 and 07-21, all exactly 45 |

**Two things this proves.**

Stills are genuinely free with the toggle on, and cost 4 credits each the moment it is off. That single −4 entry is the whole argument for checking the toggle before every batch.

**Seedance has never been free on this account.** Not once in the visible history. Every video generation cost 45 credits. The flat-fee Unlimited that covers stills does not appear to cover video on the Plus plan.

45 credits corresponds to the published 1080p rate. The published 720p rate is 22 credits. **That 720p figure has not been observed on this account** and is the one number in this plan that still needs confirming — the generate bar displays cost before render, so it can be checked without spending anything.

---

## WHAT HAS TO BE GENERATED

18 shots. World 5 already has its kimono sheet and garden plates from the parked project.

### Stills — free with the toggle on

| Asset | Count |
|---|---|
| Body sheet | 1 |
| Wardrobe sheets | 4 *(kimono exists)* |
| Prop turnarounds | 3 |
| Environment plates | 5 *(Japan exists)* |
| Identity tests | 5 |
| Key stills, one per shot | 18 |
| **Total** | **36** |

At a 3× retry rate that is 108 generations. **Cost either way: 0 credits, toggle on. 432 credits, toggle off.**

The toggle is worth 432 credits on this project al***REMOVED***

### Video — the entire budget

18 shots is the floor. Retries are the variable.

---

## THE TWO OPTIONS

**Option A — generate 720p, finish with Topaz.**
**Option B — generate native 4K.**

The 4K rate is not in the ledger and Higgsfield does not publish it. Modelled at 4× the 1080p rate, since 3840×2160 is four times the pixels of 1920×1080 and every observed step on this platform has priced at the pixel ratio. **Treat the 4K column as an estimate until the generate bar confirms it.**

### Credits

| Retry rate | Generations | A · 720p @22 | 1080p @45 *(observed)* | B · 4K @~180 *(est.)* |
|---|---|---|---|---|
| 1× — never happens | 18 | 396 | 810 | 3,240 |
| **3× — realistic** | 54 | **1,188** | 2,430 | **9,720** |
| 5× — hard shots | 90 | 1,980 | 4,050 | 16,200 |

### Against the balance held

| | A · 720p | B · 4K |
|---|---|---|
| 1× | 13% of balance | **103% — over budget on the first pass** |
| **3×** | **38% of balance** | **308% — needs 3× the current balance** |
| 5× | 63% of balance | 514% |

### Dollars

Using the published anchor of roughly $2.00 per 45-credit generation on Plus, a credit is about **$0.044**.

| Retry rate | A · 720p + Topaz | B · 4K |
|---|---|---|
| 1× | ~$17 | ~$143 |
| **3×** | **~$52** | **~$428** |
| 5× | ~$87 | ~$713 |

Plus a one-time Topaz licence on Option A if not already owned.

---

## THE VERDICT

**Option A.** Not close.

At the realistic retry rate, 4K costs roughly **eight times** what 720p does and consumes three times the entire credit balance before a single frame is finished. Option A costs about a third of the balance and leaves headroom for the hard shots.

Three further reasons, all previously established:

**Nobody has tested whether generation resolution affects face stability.** That is the binding constraint on this project and the premium buys no evidence about it.

**A platform-side upscaler already destroyed this character's face once**, on the 2K pass. Topaz with face enhancement off did not. Native 4K hands the resolution step back to that vendor class.

**Delivery does not care.** Vimeo's 4K rendition gate is a pure source-pixel test with no provenance check. A Topaz upscale to 3840×2160 unlocks the same playback tier at no additional platform cost.

---

## CONTROLS

**Every batch starts with a toggle check.** The Unlimited toggle state is confirmed and reported before any still generates. One entry in the entire ledger shows what happens when it is off.

**Video is the only metered line.** Every video generation is a spend decision. Stills are not.

**Budget by stage, not in one lump.**

| Stage | Generations | Credits @22 | Running total |
|---|---|---|---|
| Pipeline proof | 1 shot, ~3 tries | 66 | 66 |
| Risk shots | 6 shots, ~3 tries | 396 | 462 |
| Transitions | 5 seams, ~3 tries | 330 | 792 |
| Remaining coverage | 11 shots, ~3 tries | 726 | 1,518 |
| Pickups | ~10 gens | 220 | 1,738 |

**1,738 credits against the balance held.** Roughly 45% of the balance, with the rest as cushion.

**Stop-loss.** If credits spent pass 2,200 before the rough cut passes its gate, the shot list gets cut rather than the budget extended. Fixed deadline, elastic shot list — the same rule, applied to money.

**Reforecast after the pipeline proof.** One shot taken all the way through gives a real retry rate for this material. Every number above is then rebuilt from that measurement instead of an assumption.

---

## OPEN

- [ ] Confirm the 720p credit rate on the generate bar. Published figure is 22; this account has only ever been observed at 45.
- [ ] Confirm the native 4K rate the same way. Modelled at ~180, unverified.
- [ ] Confirm whether Seedance 2.0 Fast at 720p bills differently from standard Seedance 2.0 on this plan.
