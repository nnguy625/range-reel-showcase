# RANGE REEL — STATE

*Single source of truth for where this project is. Read this first on any resume, local or cloud. Update it whenever something lands.*

**Last updated:** 2026-07-25

---

## WHAT THIS IS

90-second genre-morph range reel. One woman, six worlds, her face holds throughout. Showcase piece, built to professional grade.

**Independent of the Paola short film** (parked). Only asset overlap is World 5, which reuses the Japan garden set.

---

## STATUS

| Phase | State |
|---|---|
| 0 — Beat map | **D***REMOVED***** 6 worlds, 24 shots, gesture chain locked. `Docs/BEAT_MAP.md` |
| 0b — Franco review | **In flight.** Brief sent 07-25. `Docs/FRANCO_BRIEF.md` |
| 0c — Music | **In progress.** 2 Suno variants generated, not yet selected |
| 1 — Wardrobe sheets | Not started. Blocked on Franco + track pick |
| 2 — Key stills | Not started |
| 3 — SD2 clips | Not started |
| 4 — Assembly | Not started |
| 5 — BTS piece | Not started |

**Nothing has been generated in Higgsfield yet.**

---

## LOCKED DECISIONS

| Item | Decision |
|---|---|
| Length | 88.6s master + ~40s vertical |
| Tempo | 130 BPM, half-time backbeat |
| Grid | 8 bars/world, 2 bars/shot = 3.7s per shot |
| Worlds | Skate → Bollywood → Gun-fu → Car chase → Japan sword → Gold couture, back to normal |
| Identity | `Paola_Face_Lock` element only. Nothing else describes her face |
| Wardrobe | 3-panel headless sheet per world |
| Props | Anything that changes state gets its own reference. Sword, sidearm, skateboard |
| Video res | 720p. Unlimited covers it; above 720p flips to metered |
| Still res | 4K, Unlimited on *(pending confirmation on first gen)* |
| Upscale | Topaz, face-enhance OFF. Never the platform upscaler |
| Music | One spine, six timbre swaps. Arc built in Resolve, not by Suno |
| Japan tone | Serious. Last Samurai choreography. The comedy/umbrella ruling does not travel here |

---

## ASSETS

### Have
- `Paola_Face_Lock` — Higgsfield character element, 20 generations, the identity anchor
- World 5 complete set, in `Documents/Paola JPG/`: kimono sheets, ninja refs, three garden-night angles, floorplan, approved two-hander composition
- Suno: 2 tracks "Iron and Silk" (variant 1), variant 2 generating
- Suno: `Paola's Theme` in 5 arrangements from June — proof the spine-plus-swap method works

### Need
- 5 wardrobe sheets (worlds 1, 2, 3, 4, 6)
- Props: skateboard, sidearm, sword
- Locations: SoCal street, Indian market street, cold corridor, road, runway/aisle
- 24 key stills
- 24+ SD2 clips

---

## HARD RULES

1. Three attempts per shot. No fourth.
2. One variable per retry.
3. Frame for the face — never write identity pressure and small scale into the same shot.
4. No shot is load-bearing.
5. Refs attached or don't send.
6. Zero ethnicity/nationality words in prompt text.
7. No real person's name in any prompt.
8. Never delete — stage to `_TO_DELETE_VERIFY`.

---

## VERIFIED TOOLING FACTS

- SD2 caps at 4–15s per generation. 90s is an assembly problem.
- Above 720p video = metered billing, retries stop being free.
- Comparable solo artifact (CATACOMBES, 20 min, same toolchain): **3,229 generations, 242 hours.** Its 4K was a Topaz upscale. Budget 240+ generations for this reel.
- Nobody has published a resolution-vs-face-stability test. Unknown in both directions.
- Higgsfield brands its own upscaler output "native 4K." The word is unreliable there.

---

## OPEN

- [ ] Franco's review, then reconcile
- [ ] Pick the track
- [ ] Confirm 4K stills are actually free under Unlimited (watch credit balance on gen 1)
- [ ] Confirm reading of "3-panel headless" wardrobe sheet spec
- [ ] Weakest cut by design: World 3 → World 4. Only hard cut between two adjacent modern-action worlds

---

## FOLDER MAP

```
Range Reel/
  Assets/
    Characters/     face lock, character elements
    Locations/      environment plates
    Music/          Suno output
    Props/          sword, sidearm, skateboard
    Wardobes/       3-panel headless sheets
  Docs/             all markdown
  Higgs Inspiration/
  Video Generations/
    Approve/
    Drafts/
```

Mirrors the Higgsfield Cinema Studio project structure. Assets by type, outputs by status, docs separate. One level deep.

`.git/` and `.gitignore` stay at root — git requires the repo root, and a root `.gitignore` is the only one that governs the whole tree.
