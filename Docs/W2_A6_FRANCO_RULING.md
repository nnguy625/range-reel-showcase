# W2 A-6 — FRANCO'S REVIEW (2026-08-04, 9,315 chars, full clip + 5 frame files + audio)

**Final call:** "A-6 proves the seam architecture. Do not reopen the seam. The next round is a
choreography round with a cleaner cast plate and better guide timing."

## WHERE HE SAYS MY DIAGNOSIS WAS WRONG
1. **7.137s is not a uniquely clean audio solution** once full-band accents are considered — there is a
   later accent ~0.261s after landing. My "zero competing accents" claim held only for my low-band kick
   detector, not the full-band rhythmic picture. He notes that accent may be fine, since it lands during
   her rebound rather than impersonating a second landing.
2. **The marching is primarily LOWER-BODY choreography, not an arm defect.** The arm sentence contributed
   to the lock, but alternating straight-ahead steps + upright torso + minimal lateral loading + minimal
   hip/shoulder counter-rotation is what reads as procession. Fixing only the hand sentence leaves the march.
3. **The figurine note is not primarily grain or pores.** Rigid movement and frozen facial behaviour do
   more damage than skin texture.
4. **0.458s is not a physical constant** — the next sibling may not contact on frame 11. Treat it as this
   keeper's measurement only.

## A. AUDIO — THE CORRECT THIRD ROUTE (neither of my two options)
Do NOT shift the 15s W2 editorial window. Do NOT slide the video — he confirms my worry: the handle
cannot create negative pre-roll, and sliding would displace the exact opening plate.
Instead: **use the shifted guide for generation, then fix the master audio locally after the keeper is
picked** — duck only the low-frequency body of the early kick around reel 15.195, copy or rebuild that
low kick at the selected clip's ACTUAL contact frame, and leave the existing broadband contact accent in
place. Editorial window stays 7.400–22.400. W3 untouched.

## B. CHOREOGRAPHY — his replacement sentence, verbatim
> The landing rebound carries Paola into one diagonal garba cross-step rather than a straight forward
> walk: weight shifts visibly left to right, hips and shoulders counter-rotate, and one knee lifts
> briefly on the rebound. Her right hand gathers toward the sternum while the left opens diagonally; on
> the next weight transfer they exchange roles through one continuous wrist-led circle, fingers
> articulating precise classical Indian hand shapes throughout. Elbows remain soft and asymmetric, and
> the phrase cuts before it repeats or settles into a held line.

**The line between arm soup and T-pose:** one finite exchange · two coupled weight transfers · wrists
continuously active · fingers continuously active · asymmetry · no endless improvisation · no list of
disconnected poses. Also: **remove any surviving "throne-room glide" wording** — elegant on paper, but it
invites the regal walk Nelson is calling marching.

## C. DANCER CLONES — plate defect, localized fix
Confirmed: the two near dancers share facial structure, centre-parted hairline, bun silhouette, body
proportions, blouse construction, smile and movement profile. The colour difference is doing almost all
the identity work. The exact-first-frame grammar did its job by faithfully preserving the defect.
**Fix: replace ONE near dancer through a localized patch** — different source face, hairline or braid,
jaw and cheek structure, shoulder-to-hip ratio, neckline and jewellery; SAME pose, scale, rim light,
shadow, softness, perspective — then mask-composite onto the existing plate. **No second full-frame
inpaint.** Warping her face or recolouring the costume is not enough: she needs to read as a separate
casting choice, not the same performer in wardrobe B.

## D. THE FIGURINE PROBLEM — his ranking of my three candidates
1. **Sunglasses + backlight + flat facial fill — most important.** The glasses hide eye movement, eyelid
   behaviour and catchlights; the centred sun removes frontal modelling; SD2 replaces the missing facial
   information with smooth symmetrical synthetic planes. The later face has measurably less human
   irregularity than frame zero — more symmetrical mouth, uniform cheek tone, weak nasolabial variation,
   little pore-scale highlight breakup, nearly unchanged smile.
2. **Once-cooked plate — contributor, not main cause.** The face gets CLEANER after motion begins, so
   this is downstream re-synthesis, not merely inherited damage.
3. **Grain / film-stock placement — least important.** "Grain can disguise smoothness. It cannot generate
   believable cheek tension, eyelid behavior, pore breakup or asymmetrical light."

🔴 **THE DIAGNOSIS I MISSED:** "Moving AI figurine" is not just a skin note. It is the combined effect of
fixed smile + hidden eyes + smooth skin + rigid shoulders + extended arms + straight-ahead marching +
cloned ensemble faces + near-identical ensemble timing. **"The body is selling figurine before the pores
get a vote."** Fix the choreography first — it attacks arm lock, marching and puppet motion at once.

**Face line to test only AFTER movement improves** (works inside the backlit grade instead of fighting it):
> Warm stone bounce reaches her face from camera-left rather than evenly from the front, preserving an
> asymmetric cheek and nose shadow beneath the sunglasses; skin keeps small irregular highlights, pore
> breakup and natural tonal variation, never uniform matte beauty fill.

## NEXT-FIRE PACKAGE — exactly three deterministic changes
1. one localized dancer replacement in the plate
2. generation guide starts at 7.137s
3. one rewritten travelling-choreography sentence

**Keep unchanged:** exact first-frame grammar · landing sentence · camera retreat · face anchor · smile
arc · market and grade · no descent video · no camera sidestep.
"That is more than one production input, but only one prompt variable. The other two are corrections to
proven asset defects, not exploratory prompt tuning."

## PABLO'S NOTE ON THE GUIDE NUMBER
Franco ruled 7.137 without seeing my later re-measurement. The region has no crisp kick — it is a ~0.7s
low-end SWELL peaking at source 7.64, which my peak-picker had collapsed into a phantom single kick.
By the swell-peak criterion the ideal start is **7.182** (peak lands 0.002s from her contact). The 45ms
difference is almost certainly below sibling landing variance — and Franco's post-production kick
transplant makes final sync independent of the guide anyway. Both candidates are built:
`CANDIDATE_CARRIER_W2_CLIP1_V16_7137_8s.wav` and `CANDIDATE_CARRIER_W2_CLIP1_V16_7182_8s.wav`.
Nelson picks; I lean 7.182.

## OPEN QUESTION FOR NELSON (surfaced, not resolved)
Nelson said "everyone's kind of doing the same thing." His ORIGINAL W2 requirement was the ensemble hitting
in exact unison with her, and Franco has previously warned that staggered ensemble waves fight deliberate
unison. My read is that the complaint is about the MARCHING quality making the unison look mechanical,
not a request to break unison — so v16 keeps unison and fixes the movement. **If he actually wants the
dancers varied from each other, that is a different change and it needs his word.**
