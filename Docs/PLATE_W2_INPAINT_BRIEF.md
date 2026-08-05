# W2 START PLATE — INPAINT BRIEF (Franco-wargamed 2026-08-04)

**Base:** `Docs/evidence/PLATE_BASE_A4_f017_NATIVE4K.png` — W2 A-4, frame 17, 3840×2160.
**Placement reference:** `Docs/evidence/PLATE_dancer_placement_zones.png`
**⚠ SPEND:** any inpaint pass costs credits. Unlimited is currently OFF and Generate showed 176 credits.
Nelson approves before anything fires.

## FRANCO'S RULING — the shape of the job
- Route VALID. A-4 f17 is the right base. **Do not use A-5 for anything.**
- 🔴 **DO NOT TOUCH THE FACE. The face pass is the trap.** The plate's value is exact identity + exact
  opening geometry. The mouth is no longer a contract frame one must solve — Nelson accepted a smile at
  the open; his objection was the smile *held wide over time*, which the video prompt owns after frame ***REMOVED***
- **Dancers and shadow are ONE inpaint problem, not two.** Solve them in a single composition pass so the
  scene resolves as one lighting system. Adding the shadow later as an abstract fix invites collage.
- **Density: sparse-to-moderate.** 2–3 readable indigo women near/mid ground, a few softer bodies deeper
  down the bazaar, clear depth staggering. Not the full crowd, not an empty street. Baking the whole
  ensemble in spends attempt budget on things frame one does not need.
- **Sticker mismatch is real, but do NOT fix it with a global regrain** — a full-frame wash taxes the face
  and weakens the identity anchor. Require the *additions* to match grain, compression softness, backlight
  bloom and motion cadence locally. Keep the edit localized.
- **Provenance is not the risk — pixel coherence is.** The corpus shows no penalty for edited stills as a
  class; the model responds to what the pixels show, not where they came from. The only question that
  matters: *does the edited plate still read as one coherent photograph?*

## PABLO'S PHYSICAL CONSTRAINT (independent corroboration of the density call)
The walkable stone corridor is NARROW — the stalls encroach from both sides. Six figures is roughly the
maximum that fits without standing them on the market tables. Sparse is not just safer here, it is forced
by the architecture of the shot. Note also two teal-clad women already exist at the extreme frame edges.

## ORDER OF OPERATIONS
1. **Pass 1 — environment only.** Add the dancers, their lighting, their ground contact, AND Paola's
   separated contact shadow. One pass.
2. **Pass 2 — only if needed.** Ground-only cleanup under/around her feet or shadow refinement.
3. **No face pass** unless Nelson explicitly rejects the still after seeing Pass 1.

## MASK
Mask the stone corridor and mid-ground per the placement zones. **Zero masked pixels on Paola** — not her
face, hair, the white flower, sunglasses, arms, hands, saree, dupatta or feet.

## THE INPAINT PROMPT
```
Women dancing in this same street, barefoot on the stone, in deep indigo-blue lehenga and choli with
silver-thread borders and silver anklets. Two or three read clearly in the near and middle ground,
staggered at different depths, with a few softer figures further down the bazaar implying the group
continues. Each stands in real contact with the stone, with a small contact shadow at the feet running
along the same axis as the low sun. The same centred low sun behind them throws a bright rim along hair
and fabric edges while warm stone bounce holds their faces, and their bodies sit one stop darker than the
bright sky at the end of the street. The same dust haze hangs between them and the camera, and they carry
the same fine grain, the same gentle backlight bloom and the same softness as the rest of the photograph.
A separated contact shadow sits on the stone beneath the airborne woman in crimson.
```

## REJECT CRITERIA — Franco's five, check every one before this plate seeds anything
1. Paola's face shifts **at all**
2. dancers read sharper or cleaner than the source frame
3. dancers do not share the same backlight logic
4. the crowd is too dense or visually noisy
5. her falling read weakens because the additions clutter the gap or ground cue beneath her

## AFTER APPROVAL
Attach as: `@Image 1 is the exact first frame and strict identity anchor.` No descent video.

---

## ROUND 1 RESULTS — MCP inpaint IS viable (2026-08-04)

**Method finding: the Higgsfield MCP has NO mask-based inpaint tool.** `outpaint_image` only expands a
canvas. What works is **instruction-based editing** via `generate_image` with the plate passed as a
reference media. Route: `media_upload` → curl PUT the bytes → `media_confirm` → `generate_image` with
`medias:[{role, value:media_id}]`. **Download the result immediately — MCP URLs expire.**

**Costs (preflighted with `get_cost:true`, which submits nothing):**
`seedream_v4_5` 4K = **1 credit** · `nano_banana_pro` 4K = **4 credits**. Balance (redacted), plan `plus`,
Unlimited allowance NOT currently available. A video fire is ~176 credits by comparison — image editing is
effectively free at this scale, so iterate freely.

| | Seedream 4.5 (1cr) | Nano Banana Pro (4cr) |
|---|---|---|
| output | 2560×1440 (**downscaled** from our 3840×2160) | **5504×3072** (upscaled, best) |
| face preserved | close, slight cleanup; variant B added a rim halo | **essentially identical at crop level** |
| environment preserved | re-rendered, brighter/more saturated | **closely preserved** |
| dancers | 3 near + depth, deep indigo + silver borders | 2 near + 1 mid + deeper figures, reads violet |
| contact shadows | **YES — dancers AND under Paola** | dancers yes, **NONE under Paola** |
| verdict | best shadow work | **best plate** |

### Franco's five reject criteria vs the Nano Banana plate
1. face shifts — **PASS**, verified on a matched crop: same features, flower, glasses, earring, tilt
2. dancers sharper than source — **PARTIAL**, whole frame is cleaner than the source video frame, but
   uniformly so, i.e. no internal seam
3. backlight logic — **PASS**, dancers rim-lit, bodies darker than the sky
4. density — **PASS**, matches "2-3 readable + softer deeper"
5. falling read — **PARTIAL**, the separated contact shadow under Paola was ordered and did NOT render;
   her feet also read slightly soft

### NEXT ITERATION (not yet run — awaiting Nelson)
Nano Banana Pro again, with the contact shadow under her promoted to its own emphatic clause, and the
dancers' colour pushed from violet toward deep indigo. Seedream proves the shadow is renderable.
Files: `INPAINT_v1_nanobanana.png` · `INPAINT_v1_seedream_A.png` · `INPAINT_v1_seedream_B.png` ·
`PLATE_3WAY_src_seedream_nano.png` · `FACE_src_vs_nano.png` · `FACE_COMPARE_src_A_B.png`

## ROUND 2 RESULTS — both fixes landed (2026-08-04, Nelson approved the run)
Nano Banana Pro, 2 variants, 8 credits. Both 5504×3072.
Changes from round 1: her shadow promoted to its own emphatic clause with the correct physics stated
(low sun BEHIND her, so the shadow falls FORWARD toward camera), and the costume pushed positively toward
"deep indigo blue, the dark saturated blue of midnight and dark denim".

**Both fixes worked.** Costume is now true indigo, not violet. The contact shadow renders in both.

| | v2 variant A | v2 variant B |
|---|---|---|
| ensemble | 2 near + 2 mid + softer deeper — best depth staggering | 2 near + 2 deeper, sparser |
| her shadow | present but SUBTLE, a soft dark smear under her feet | LONG and strong, stretches to camera |
| integration | best — dancers carry the same haze, softness and grain | good |
| my read | **best plate overall** | **best falling read** |

**Franco's five criteria vs v2A:** face — PASS (matched crop, identical features/flower/glasses/earring/
tilt) · sharper-than-source — PASS, native crop shows dancers carrying the same haze and softness, no
sticker edge · backlight logic — PASS · density — PASS, matches his 2-3-plus-depth spec · falling read —
PASS but soft; v2B is stronger here.

**Open choice for Nelson:** A's integration vs B's stronger shadow. A third pass could take A's ensemble
with B's shadow strength for 4 more credits.
Files: `INPAINT_v2_nano_A.png` · `INPAINT_v2_nano_B.png` · `v2A_FACE_vs_src.png` · `v2A_shadowQA.png`

## ✅ FINAL PLATE — `Docs/evidence/PLATE_W2_CLIP1_FINAL_3840x2160.png`
v2 variant A, crop-corrected. **3840×2160, exactly our delivery format.**

🔴 **GEOMETRY GATE CAUGHT A DRIFT — run this check on every future plate edit.** The inpaint SHRANK her:
head-to-foot span fell from ~53% of frame height in the source to ~40% in the v2 output, even though her
feet still landed near W1's line. A scale drift like that pops on the cut. Because Nano Banana returns
5504×3072 we had surplus resolution to crop back in for free: `crop=4155:2337:674:250` then
`scale=3840:2160`. Post-crop she spans ~60% against W1's ~58%, feet on the line, and the whole ensemble
survived the crop. **Lesson: an instruction-edit can silently re-frame. Always re-overlay W1's foot line
on the output — passing the face check is not passing the geometry check.**

Remaining known imperfections, accepted: her raised hand is slightly clipped at the top edge, and the
contact shadow is subtler than v2B's. Neither blocks the fire.

**USE AS:** `@Image 1 is the exact first frame and strict identity anchor.` No descent video.
Controls before firing: 16:9 · 8s · audio ON · Unlimited ARMED · never Auto.

---

## ✅ PLATE v3 — MASK COMPOSITE BUILT (2026-08-04, mask-composite method, ZERO credits)

`Docs/evidence/PLATE_W2_v3_MASKCOMP_3840x2160.png` — 3840×2160, the fire-ready plate.

**Method correction:** the mask step is NOT a model call and needs no browser. the model makes the point edit, then the change is brought onto the original by hand in a mask-capable graphics editor. We had already paid for the model half (v2A). Compositing is local and free.
Scripts archived: local align/mask-composite scripts (not in this repo).

**Pipeline that produced it:**
1. **Align** the 5504×3072 model edit to the 3840×2160 original by similarity-transform search,
   scored on the top 45% of frame only (no dancers added there, so it measures registration not content).
   Converged f=0.985, centre (0.500, 0.502). Registration verified on static features — stall sacks,
   crate and table legs land in the same place.
2. **Grade-match** the edit to the ORIGINAL using per-channel mean/std from the top 32% band. The model
   edit came back measurably darker and contrastier; without this the dancers would sit in a different
   grade from the street they stand on. Residual per-channel delta after matching: 0.00.
3. **Mask** only what we want: four dancer regions + the ground-shadow patch, feathered.
4. **Protect Paola**: subtract a feathered silhouette (head/torso, raised arm, legs, streaming dupatta)
   so the mask can never reach her.
5. **Composite** original × (1−α) + edit × α.

**MEASURED RESULT — the guarantee this method exists for:**
| region | MAE vs original |
|---|---|
| **FACE (head, glasses, flower)** | **0.000 — pixel-identical** |
| **Upper buildings** | **0.000** |
| dupatta | 1.26 |
| torso + saree | 1.74 |
| legs + feet | 7.47 (dancers arriving *around* her; her feet verified untouched on a native crop) |
| left / right dancer zones | 34.9 / 41.4 — the intended new content |

**69.8% of the frame is bit-identical to the original.**

**Franco's five reject criteria:** (1) face shifts — PASS, provably 0.000 · (2) dancers sharper/cleaner
than source — PASS, grade-matched, no seam visible at native res · (3) backlight logic — PASS, dancers
rim from the same centred sun · (4) density — PASS, 2 near + 2 mid + deeper figures · (5) falling read —
**SOFT**: the gap and the dust plume read, but the separated cast shadow is weaker than Franco specified.
Not blocking; strengthenable locally if Nelson wants it.

**Geometry gate: passes by construction.** Paola is original pixels, so her head-to-foot span and screen
position are the original's — already measured at feet 64% vs W1's 63%.
