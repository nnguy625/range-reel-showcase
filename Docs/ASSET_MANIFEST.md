# ASSET MANIFEST — everything pulled from Higgsfield, 2026-07-28
### 43 source images, full resolution, named by world. The PNGs are gitignored; this file is the index.

**Local:** `Assets/<Type>/_HIGGSFIELD/`
**Drive (for remote review + Franco):** `GDRIVE:\RANGE_REEL_ASSETS\<Type>\`

Pulled from the Higgsfield project **`Paola Cinematic Demo`**. The proxied grid images are only ~314 px;
these are the **originals** saved at full resolution — 2880×2880 up to 5504×3072.

| Type | Files | Size |
|---|---|---|
| Characters | 12 | 167 MB |
| Locations | 23 | 518 MB |
| Props | 8 | 103 MB |
| **Total** | **43** | **789 MB** |

---

## By world — what exists for each

### World 1 · SoCal skate
`W1_Skate_urban_sheet` (3-panel, white tank over black, beanie, **curls**) ·
`W1_SoCal_MAP_aerial` · `W1_SoCal_street_A/B/C/D` · `W1_Skateboard_3view`
**Complete** — character, MAP, 4 street angles, prop.

### World 2 · Bollywood
`W2_Bollywood_sari_sheet_A/B/C` (3-panel red sari) · `W2_Bollywood_face_CU` (sunglasses) ·
`W2_Market_MAP_aerial` · `W2_Market_street_A/B/orange`
**Complete for boarding.** ⚠ The feet-gap fix (`Pao-Bolly-Full`, barefoot full-body) is **not among
these** — it was approved in the cloud session but never created as an element.

### World 3 · Gun-fu
`W3_GunFu_agent_sheet` (3-panel, bomber, **sleek**) · `W3_GunFu_face_CU` ·
`W3_Corridor_A/B/C` · `W3_Corridor_cool_lights` · `W3_Sidearm_3view`
**Complete.**

### World 4 · Car chase
`W4_CarChase_messybun_sheet` (3-panel, no bomber, **curls**) · `W4_CarChase_face_CU` ·
`W4_DesertRoad_curve_A/B` · `W4_DesertRoad_centreline` · `W4_DesertRoad_straight` ·
`W4_Car_INT_side_window` · `W4_Car_INT_forward_drive` · `W4_Car_INT_dash_2panel` ·
`W4_Car_EXT_hero_6view` · `W4_Car_EXT_chaser_6view`
**Richest world** — 3 interior views and both car exteriors as 6-view sheets.

### World 5 · Japan sword — ✅ **COMPLETE (corrected 2026-07-28)**

> ⚠ **My earlier "World 5 is asset-blocked" call was WRONG.** I only searched the reel project's
> *Assets* folders. The W5 material lives in **Elements**, which spans projects — `@Paola_Kimono` is in
> the reel project itself, and the garden set is in the kimono short-film project. **Lesson: Assets and
> Elements are different views, and Elements is the one that crosses projects.** Search Elements before
> declaring anything missing.

**Locations (9):** `W5_Garden_NIGHT_wide` (5504×3072) · `W5_Garden_NIGHT_shoji_POV` (5504×3072) ·
`W5_Garden_NIGHT_alt` · `W5_Garden_NIGHT_front_POV` · `W5_Garden_MAP_birdseye` (3168×1344) ·
`W5_Garden_DAY_wide` · `W5_Garden_GOLDEN_1POV` · `W5_Garden_GOLDEN_pano` · `W5_KimonoShop_interior`

**Characters (7):** `W5_Kimono_sheet` (5504×3072, front/back/face CU) ·
`W5_Kimono_night_fullbody` (**the hero frame** — Paola in the night garden, arms out, lit) ·
`W5_Kimono_loose_A` · `W5_Kimono_loose_B` (370×380 obi detail) · `W5_Kimono_glow` ·
`W5_Kimono_casual` · `W5_Kimono_casual_glow`

**Props (1):** `W5_Katana_pair`

**The four-POV night set is already covered** — MAP = birdseye, WIDE = NIGHT_wide,
WORK = NIGHT_shoji_POV, REVERSE = NIGHT_front_POV. **No new plates needed, so no credits spent.**

> ⚠ **WARDROBE CONFLICT — needs a ruling.** The **built** kimono is **pale pink/cream with a magenta
> obi**. The **written spec** (Franco's costume pass, carried into `ASSET_SPEC.md`) says **midnight
> indigo with a black-plum obi and restrained oxblood sleeve lining**. They are not the same garment.
> Several panels also carry the **pink flower Franco explicitly said to remove**. Franco has to pick:
> re-grade W5 around the pink that exists, or rebuild the kimono to the indigo spec.

### World 6 · Gold couture
`W6_Couture_gold_sheet` (3-panel) · `W6_Couture_face_CU` ·
`W6_Runway_wide` · `W6_Runway_wide_seats` · `W6_Runway_arch` · `W6_Runway_arch_seats` ·
`W6_Runway_angled` · `W6_Runway_light_detail`
**Complete** — six runway angles, the most of any location.

### Cross-world
`ID_Paola_face_master_CU` — the clean identity master, sleek, black tank. The `@face` anchor.

---

## Hair check against the 07-27 ruling — all consistent

Curls appear in exactly two character sheets, and they are the right two:
**`W1_Skate_urban_sheet`** and **`W4_CarChase_messybun_sheet`**. W2, W3, W6 and the identity master
are all sleek. The built assets already implement the ruling; nothing needs regenerating.

---

## ⚠ Gaps this pull exposed

1. **World 5 has no character or location assets in this project.** Everything else is boardable from
   Higgsfield; World 5 is not. Its kimono and garden must be located in the short-film set and pushed
   to Drive before Franco can board it.
2. **The Higgsfield `StoryBoards` folder is EMPTY.** The World 1 board (`SB_W1_lastframes.png`) is
   local only, and the World 2 board reported by the cloud session is not here either.
3. **Characters shows 15 in the sidebar but 12 have image files.** Verified stable across three
   scroll positions. Three assets are counted but not rendered as images — possibly non-image types.
   Worth a look before assuming the set is complete.
4. **`Pao-Bolly-Full`** — the barefoot full-body Bollywood reference approved in the cloud session was
   never created as an element, so the World 2 feet gap is still open in practice.

## How these were extracted

Full-resolution copies were saved from the platform's own asset pages (method not published here).
