# ASSET REGISTRY — every Higgsfield element, with what it actually contains

**Why this file exists (2026-08-04):** Nelson: *"We already made backup dancers plate. Dancers one and
dancers two. Did you forget that this happened because of the compression?"* — He was right. `dancers1`
and `dancers2` existed since 2026-08-03 and I proposed spending credits to generate what we already had.
They lived ONLY inside Higgsfield: not in git, not in memory, not in `CLAUDE.md`, not in `STATE.md`.
The only trace was the words "dancer sheets" in a do-not-attach list — a category, not a record.

**THE RULE THIS CREATES: an element does not exist until it is in this file.** Name + id + what is
actually in the picture. A one-word mention in a prompt doc is not a record. This is the
"one dictionary of names for the whole project" rule we had read the same day and not implemented.

Refresh with the Higgsfield MCP: `show_reference_elements action=list size=100`.
Last synced: **2026-08-04**.

---

## 🔴 W2 ENSEMBLE — THE ASSETS I FORGOT

| tag | id | what is actually in it |
|---|---|---|
| **`dancers1`** | `6026c73e-1a61-47ee-b7bf-c8480474fe81` | **7-woman casting sheet**, full-body frontal, flat light, neutral grey seamless. Genuine variety: long single braid / bun with white flower band / loose curls / grey-streaked older woman / twin braids young / centre-part / short bob. Wardrobe: navy, cobalt, teal, slate, powder-blue lehenga + choli, silver-thread borders, bare feet, heavy silver anklets, bangles. |
| **`dancers2`** | `630dd633-4df4-4dfb-a884-9118e3e4e950` | **Second 7-woman casting sheet**, same register and palette, different faces/drapes — deeper teal and layered navy variants, more sari-style drapes. Companion set to `dancers1`. |

Created 2026-08-03, 21:19:52 and 21:26:25. Both `character`, both `completed`, both 3840×1648.
**14 approved, visually distinct women.** This is the anti-clone asset for the W2 ensemble.

## PAOLA — identity and wardrobe states
| tag | id | contents |
|---|---|---|
| `Pao-Face-Bolly` | `91bf27d0-a1a9-455f-9441-f35da3777b69` | face-only identity anchor, Bollywood state — the ONLY face authority in v15/v16 |
| `Pao-Bolly` | `2033ec46-97eb-400a-8b64-dc4f86dc8ea0` | crimson saree wardrobe state |
| `Pao-Urban` | `28ad6024-ba8a-4f66-a09c-1967481b15ed` | W1 skate state |
| `Pao-Face-MessyBun` / `Pao-MessyBun` | `f1d90201-…` / `d4d9197f-…` | messy-bun state pair |
| `Pao-Face-Strut` | `ff30166f-08d8-46a6-977b-779d48fb9f68` | strut state face |
| `Pao-Face-CU` | `ad02f114-b91d-4e8b-b9fc-3e7b5e26d768` | close-up face |
| `Pao-Gold` | `b0cbc249-799e-4ef4-8dc6-afa59fa121e6` | W6 gold couture state |
| `Pao-Agent` / `Pao-CU-Agent` | `b52df016-…` / `e21a86da-…` | agent-world states |
| `Hair-Lock` | `a9c65bef-6db5-44bd-bd4a-591539cc54bd` | hair continuity reference |

## W2 LOCATION AND POSE
| tag | id | note |
|---|---|---|
| `Loc-Market-Street-FIX-2` | `aef2ddde-ab3d-4ee3-9d75-367d2e78d6e0` | **the live W2 location** |
| `Loc-Market-Street-FIX` | `8adb2738-9b78-46d4-bf4a-917537b81c94` | superseded duplicate — rename/retire still open |
| `Pose-W2-Landin` | `06ef8c9c-6058-496c-999d-49f9e78143e0` | pose diagram. **RETIRED** — diagrams leak into pixels (seq41) |
| `W1-Seam-Fram` | `e20c9505-7219-44c3-9347-0663d2b75ac5` | W1 seam frame |

## OTHER WORLDS / EARLIER FILM
`Loc-SoCal-Street` + `-Aerial-FIX` · `Loc-Runway` · `Loc-Desert-Road` · `Loc-Corridor` ·
`Loc-Hotel` (+ `-Cover`, `-Entrance`, `-Money`, `-OTS`, `-Reverse`, `-Tumble`) ·
`Car-Pao-Int-*` (4 POVs) · `Pao-Car-Ext` · `car-chaser-ext` · `Skateboard` · `katana` · `gun` ·
`Ninja` · `Ninja-bag` · `burglar` · `Paola` / `Paola_Anchor` / `Paola_Expr_CU` ·
`Standoff-*` / `Blueprint-*` / `Plate-Final*` (Paola short film, earlier project) ·
`Garden-Shoji-POV-Night` · `Garden_Night_EnvPlate` · `Blocking_Ref` · `Swap_B`

---

## HOW `dancers1` / `dancers2` CHANGE THE CLONE FIX
Franco's ruling was to replace one near dancer via a localized patch, and I had scoped that as a paid
generation of a brand-new face. With these sheets the task changes: we are no longer inventing a woman,
we are **directing the patch to an already-approved casting choice.**

Honest constraint: the sheets are frontal, flat-lit, grey-background full-bodies. The plate dancers are
backlit, three-quarter, mid-motion. So this is **not** a straight pixel paste — the face angle, lighting
and scale do not match. The sheets serve as the *identity reference* for a small regenerated patch,
which is cheaper, safer and more directable than a blind new face, but likely still one small model call.
