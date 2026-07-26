# FRANCO_DECISIONS.md

Extracted verbatim from the reviewer thread
<[private thread]>
39 conversation turns / 23 text messages (the other 16 turns are image-generation outputs carrying no text beyond "Worked for Xs" and one caption, "Designed a feminine deck").
Extracted 2026-07-26. Roles: **Nelson** = director. **Franco** = adversarial reviewer (the assistant in-thread).

> **Quoting rule for this file:** every block marked *verbatim* is copied character-for-character. Do not reword before pasting into an image prompt.

---

## ⚠️ TOP FLAGS — READ BEFORE USING THIS FILE

### A. Four requests were made and NEVER answered in text

| # | Msg | Nelson asked for | What actually came back |
|---|-----|------------------|-------------------------|
| 1 | 3 | `"this is the look, desrcibe to pablo how to prompt this outfit."` — **URBAN** | Image only. **No written urban prompt exists anywhere in the thread.** |
| 2 | 15 | `"yeah, i think this is the best. give pablo the prompt"` — **KIMONO** | **Nothing.** No assistant turn at all. Nelson moved straight to music. |
| 3 | 19 | Skateboard redesign: aurora colours + stickers | Image only (turn 33). The text reply (msg 20) covers **sunglasses only** and opens by admitting the miss. |
| 4 | 22 | `"the one you generated & the one in this picture looks different"` — glasses prop mismatch | Image only. **Thread ends here, unresolved.** |

**Only two pasteable operator prompts were ever written: AGENT (msg 11) and SUNGLASSES (msg 20).**

### B. Live contradictions — resolve before generating

| Topic | Conflict | Current best reading |
|---|---|---|
| **Hair** | Msg 1: `"Keep the sleek center part and low bun as the permanent hair silhouette"` vs Msg 2 (Nelson): `"she has curly hair like this, but black"`. Msg 20 (latest) again says `"Keep the sleek center-part low bun"`. | **UNRESOLVED.** Franco never acknowledged the curly-hair note. Latest written word is the low bun, but Nelson's is the later *director* instruction on the urban look. Needs a ruling. |
| **Urban silhouette** | Msg 1: `"deep forest ribbed tank, washed-black wide carpenter jeans"` vs Msg 2 (Nelson): white outer tank / black inner / **leggings** / `"legs are fitted"`. | **Nelson wins.** Msg 2 is an explicit override ("Change up the outfit"). Msg 1's urban line is dead. |
| **Agent palette** | Msg 1: `"blackened-aubergine bodysuit under a structured graphite cropped jacket"`; Msg 8 board palette `"graphite, charcoal, blackened aubergine and soft black"` vs Msg 11 (locked): `"Palette and materials: all black, separated through texture."` | **Msg 11 wins** — it is the post-approval lock written off the image Nelson approved at msg 9. |
| **Kimono** | Msg 1 spec (midnight indigo / black-plum obi / oxblood lining) vs Msg 13 (Nelson): `"no, like none of the outfits at all"`. | **Msg 1 kimono text is NOT safe to use.** Nelson rejected the whole board. The approved kimono exists **only as an image**, never as words. See Kimono section. |
| **Sunglasses scope** | Msg 8 board rule `"no sunglasses"` and msg 11 `"Remove: flower, sunglasses"` vs the full sunglasses spec in msg 20. | Not a real conflict — **sunglasses belong to URBAN, and are banned from AGENT.** Noted so the exclusions don't get pasted into the wrong prompt. |

### C. Possibly-missed decisions buried in msg 1 (never followed up on)

- **Three-quarter identity refs** were ordered and, as far as this thread shows, never built: `"Also create matching left-three-quarter and right-three-quarter identity references from this exact face. A frontal image alone will not adequately police her nose, jaw and eye shape across all three wardrobe angles."`
- **Earring standard**: `"standardize them as small warm-gold huggies in the clean identity master."`
- **The gold ratio law** (Bollywood 5% gold → Couture 80% gold). See Couture.
- **Bollywood was never rejected on costume grounds.** The boards failed because the image tool kept recycling them (`"clinging to Bollywood like glitter in carpet"`) — that is a *tool* failure, not a wardrobe verdict. The msg 1 Bollywood spec is still live.

---

## 1. URBAN SKATE

### Status: direction locked by Nelson, **no operator prompt written**

**Franco's original proposal (msg 1) — SUPERSEDED, do not use:**

> urban skate gets a deep forest ribbed tank, washed-black wide carpenter jeans, black-and-gum skate shoes and a faded black cap with the bun exiting low through the back

**Nelson's override (msg 2) — verbatim, this is the live direction:**

> this styling direction is wrong for her — rejected. I like this look better. I want outer tank top white, inner black, legginges, black cap or beanie look. she has curly hair like this, but black. Change up the outfit. I like that sleek ninja like look. where legs are fitted, top casual loose. wife likes beenie or black cap, not flat lid

**Decomposed (Nelson's exact words preserved):**
- Outer: `"outer tank top white"`
- Inner: `"inner black"`
- Legs: `"legginges"` / `"legs are fitted"`
- Head: `"black cap or beanie look"` — and `"wife likes beenie or black cap, not flat lid"`
- Hair: `"she has curly hair like this, but black"`
- Overall read: `"I like that sleek ninja like look. where legs are fitted, top casual loose."`

**Rejections (Nelson's own words):**
- `"this styling direction is wrong for her — rejected."` — rejection of Franco's first urban board.
- `"not flat lid"` — flat-brim caps are out.

**Open request, unfulfilled (msg 3):**

> this is the look, desrcibe to pablo how to prompt this outfit.

Answered with an image only. Nelson later confirmed (msg 10) `"higgsfield currently generating the urban on higgs"` — so it was generated without a written spec ever existing.

---

## 2. BOLLYWOOD

### Status: spec live, never rejected on merit, never prompted for Pablo

**Locked spec (msg 1) — verbatim:**

> Bollywood gets a pomegranate-red raw-silk blouse and fluid georgette sari with only a narrow antique-gold border against a dusty teal crowd

**Silhouette-collision rule (msg 1) — verbatim:**

> Bollywood and couture remain the silhouette collision. Both can become floor-length asymmetric drapery. Keep Bollywood visibly waist-baring, soft, diagonal and red; keep couture uninterrupted through the torso, vertical, metallic and architectural. Gold should occupy only about five percent of the Bollywood costume as trim, then become roughly eighty percent of the couture image. That makes world two whisper gold and world six detonate it.

**Rejections:** none on the costume itself. The failures were generator contamination, in Franco's words:

> The image tool is clinging to Bollywood like glitter in carpet. One clean restart: AGENT only, no sari, no dancers, no red, no sunglasses board.

> The generator is stuck recycling the Bollywood board despite three explicit resets, so those last outputs are invalid.

---

## 3. AGENT

### Status: ✅ **LOCKED — full operator prompt exists (msg 11)**

Nelson approved a look at msg 9: `"this the look, full body outfit of this, tactical black boots"`, then at msg 10: `"this is approved, not paola, but i'll let pablo handled that. just need prompt for this outfit."`

### 3a. THE DELIVERABLE — paste-ready agent outfit prompt (msg 11, verbatim)

```
Use the approved agent image as the exact wardrobe authority only. Do not copy its face, body, pose, lighting or corridor. Facial identity comes from Paola_Face_Lock.

Outfit: fitted black scoop-neck performance tank tucked into high-waisted matte black utility trousers. The trousers are slim through the hips and thighs, then relax slightly through the lower leg for movement. Subtle articulated knees, restrained side-seam utility detailing and one small low-profile thigh zipper pocket. No oversized cargo pockets.

Outer layer: lightweight cropped black bomber jacket with a compact silhouette, ribbed collar, ribbed cuffs and ribbed waistband. Soft matte technical nylon with very low sheen. Jacket worn open, sleeves lightly pushed toward the forearms. It should frame the waist without looking puffy.

Waist: narrow black leather belt with a small dark metal rectangular buckle.

Footwear: mid-calf black lace-up tactical boots with flat heavy tread, reinforced toe, compact ankle structure and no heel. Functional and grounded, not platform boots, fashion combat boots or military cosplay.

Palette and materials: all black, separated through texture. Matte cotton tank, low-sheen technical bomber, structured stretch utility twill trousers, matte leather boots. Avoid glossy leather trousers.

Silhouette: compact bomber and fitted torso over a long, clean leg line. Feminine, athletic, physically capable and quietly dangerous. The costume must work unchanged in both a cold corridor gunfight and a hot dusty car chase.

Remove: flower, sunglasses, holsters, body armor, harnesses, gloves, camouflage, visible weapons, logos, patches and excessive tactical hardware.
```

### 3b. Supporting board instruction (msg 8, verbatim) — for regenerating the selection board

Franco's framing: `"Best move is to generate it in a fresh image thread with only Paola's face lock attached, otherwise the current Bollywood references keep contaminating the board. Use this exact opening instruction:"`

```
Generate one AGENT wardrobe selection board only. Six full-body outfit options labeled A–F in a clean 2×3 studio grid. Same Paola face, same body, same sleek center-part low bun, same small gold hoop earrings, same neutral stance and lighting in all six panels. No sari, no Bollywood styling, no dancers, no red, no sunglasses, no Indian architecture.

The costume must work unchanged in two worlds: a cold desaturated corridor gunfight and a sunlit dusty car chase. Feminine, sleek, capable, confident, expensive, physically mobile. Avoid generic tactical cosplay, military uniforms, body armor, catsuits, trench coats and oversized blazers.

A: graphite cropped collarless jacket, fitted blackened-aubergine V-neck bodysuit, high-waisted straight charcoal trousers, slim matte ankle boots.

B: fitted charcoal mock-neck sleeveless top, cropped technical waistcoat, high-waisted tapered trousers, low black boots.

C: asymmetrical graphite wrap jacket over a fitted black tank, narrow high-rise trousers, matte leather boots.

D: short structured charcoal field jacket, fitted scoop-neck bodysuit, slim bootcut trousers, pointed low-heel boots.

E: fitted dark-plum long-sleeve top, cropped graphite harness-inspired vest without tactical pouches, straight trousers, ankle boots.

F: sleeveless charcoal jumpsuit with a defined waist, narrow leg, restrained front zip and matte boots.

Materials: stretch wool, matte technical nylon, dense jersey and soft leather. No shine, camouflage, logos, cargo overload, visible armor or excessive straps.

Palette: graphite, charcoal, blackened aubergine and soft black. Keep all six dark enough for the corridor but textured enough to remain readable in harsh sunlight.

Overall silhouette: long clean leg, defined waist, compact upper body, unrestricted shoulders. The woman should read as an elite civilian operative, not a soldier or superhero.
```

> ⚠️ This board's palette (graphite / aubergine / charcoal) is **superseded by the all-black lock in 3a**. Use 3b only to regenerate options, never as the final wardrobe.

### 3c. Earlier agent line (msg 1) — superseded

> agent gets a blackened-aubergine bodysuit under a structured graphite cropped jacket, high-waisted narrow trousers and matte boots

**Rejections / resets (Franco's words):**

> That generated the wrong board. Resetting to the next costume: AGENT, six outfit variations, same woman, built to survive both the cold corridor and the dusty car chase.

---

## 4. KIMONO

### Status: 🔴 **APPROVED AS AN IMAGE, NEVER WRITTEN. Highest-priority gap.**

**Franco's original spec (msg 1) — REJECTED by msg 13, do not paste:**

> kimono stays midnight indigo with a black-plum obi and restrained oxblood sleeve lining

**The reset (msg 12, verbatim):**

> Wrong carryover again. Resetting to KIMONO only: six serious sword-exchange options, no agent clothing, no corridor, no car.

**Nelson's rejections and steers, verbatim, in order:**

- Msg 13: `"no, like none of the outfits at all, pick one that looks best for paola, reuploading the face image"`
- Msg 14: `"better, i want multiple optinos in one panels please. again lose the flowers"`
- Msg 15: `"yeah, i think this is the best. give pablo the prompt"`

**What this means:** msg 13 kills every kimono option on the board, including the msg 1 indigo/black-plum/oxblood spec. Nelson then approved a *specific generated image* at msg 15 and asked for the prompt. **No prompt was ever written — the thread has no assistant turn between msg 15 and msg 16.**

**To recover this:** the only source of truth is the approved kimono image in the turn immediately preceding msg 15. Someone must open the thread, pull that image, and write the spec from it. Known constraints that survive: `"serious sword-exchange"`, `"no agent clothing, no corridor, no car"`, and **no flowers** (`"again lose the flowers"`, third flower rejection in the thread).

---

## 5. GOLD COUTURE

### Status: spec live from msg 1, never boarded, never prompted

**Locked spec (msg 1) — verbatim:**

> couture becomes burnished old gold rather than pale champagne, with a simple bias-cut column and one darker bronze pleated fan attached at the hip.

**Stability law (msg 1) — verbatim:**

> Gold couture is still the hardest sheet to stabilize. Limit it to one shoulder construction, one hip attachment, one pleated moving piece and one clean hem. No beads, cutouts, layered trains or extra folds for Nano Banana to breed between panels.

**Contrast law vs Bollywood (msg 1) — verbatim:**

> keep couture uninterrupted through the torso, vertical, metallic and architectural. Gold should occupy only about five percent of the Bollywood costume as trim, then become roughly eighty percent of the couture image. That makes world two whisper gold and world six detonate it.

**Rejection carried in the spec:** `"pale champagne"` is explicitly out — msg 1 also lists it among colours that flatten her (see Identity section).

---

## 6. SKATEBOARD

### Status: 🔴 direction given, **no written spec produced**

**Nelson's direction (msg 19) — verbatim:**

> the colors not feminine at all, something aurora like colors w/ stickers, she likes edc, yoga, bollywood, nike, different things like that.

**Decomposed (his exact terms):**
- Rejection: `"the colors not feminine at all"`
- Palette: `"something aurora like colors"`
- Surface: `"w/ stickers"`
- Sticker vocabulary: `"she likes edc, yoga, bollywood, nike, different things like that"`

**What came back:** an image only (turn 33). The one caption the generator produced for the earlier deck was `"Designed a feminine deck"`. Franco's text reply (msg 20) opens by conceding the miss:

> You're right. The sunglasses answer got buried under the skateboard generation.

**No written skateboard deck spec exists in this thread.** Needs to be authored.

---

## 7. SUNGLASSES

### Status: ✅ **LOCKED — full operator prompt exists (msg 20)**, but final prop image disputed

**Selection history (Nelson, verbatim):**
- Msg 4: `"i like B, give her sunglasses 2 that looks well w/ her face & this outfit. Reuploading pics for reference"`
- Msg 5: `"This one, make the tint a little lower so you can kind of recogniz her eyes,"`
- Msg 19: `"also pablo got higgs generated ugly seat glass , the small thumbnail has the one you designed, help pablo w/ the prompt for the correct design"`

**Franco's root-cause (msg 20) — verbatim:**

> Higgs made them ugly because "cat-eye sunglasses" is too broad. It defaults to thick retro frames, large lenses, or an exaggerated upward wing. Pablo needs to upload the large close-up as its own element and make it the sole eyewear authority.

### 7a. THE DELIVERABLE — paste-ready sunglasses prompt (msg 20, verbatim)

Franco's framing: `"Send Pablo this:"`

```
Use @Paola_Face_Lock for Paola's facial identity only.

Use @Glasses_Lock as the exact sunglasses design authority. Copy the sunglasses from @Glasses_Lock precisely. Do not reinterpret, beautify, modernize, enlarge, or redesign them.

The sunglasses are ultra-narrow rimless micro cat-eye glasses:

Very shallow, horizontally elongated lenses, approximately three times wider than they are tall.

Slim pointed outer corners with a subtle upward lift.

Narrow pointed inner corners.

Nearly straight upper lens edge.

Soft shallow curve along the lower edge.

Small scale relative to her face.

They sit low across the bridge of her nose, beneath the eyebrows.

Her brown eyes remain clearly recognizable above and through the lenses.

Warm translucent tobacco-brown lenses with a light 30–40% tint, never dark or opaque.

Hair-thin dark bronze metal bridge.

Hair-thin bronze temple arms.

Rimless construction with no thick border around the lenses.

Delicate, feminine, confident, sharp, expensive, and commanding.

Preserve Paola's exact eye shape, eyebrow shape, nose width, cheek structure, and face proportions underneath the glasses.

Remove the pink flower. Keep the sleek center-part low bun and small gold hoop earrings.

Never generate:

Thick black frames.

Chunky acetate cat-eye glasses.

Oversized sunglasses.

Tall or deep lenses.

Round, oval, butterfly, rectangular, or sporty wraparound lenses.

Heavy gold frames.

Opaque black tint.

1950s costume styling.

Glasses covering her eyebrows or most of her cheeks.

Most important line:

@Glasses_Lock controls the exact eyewear geometry. The words "cat-eye" are descriptive only and must not override the reference.
```

### 7b. Reference-handling rule (msg 20, verbatim) — do not skip

> Also tell him not to use the small thumbnail as the primary reference. Its low resolution lets Higgs invent thickness and lens shape. The large close-up should be uploaded separately and tightly cropped around the face and glasses.

### 7c. UNRESOLVED — prop mismatch

- Msg 21 (Nelson): `"franco generate the glass prop"` → image generated.
- Msg 22 (Nelson): `"the one you generated & the one in this picture looks different"` → image generated, **no text answer. Thread ends.**

The generated glasses prop does not match the reference. **This is the live open loop at the end of the conversation.**

---

## 8. MUSIC

Three review rounds happened: **A/B → C1/C2 → E1/E2**. Every round lands on the same architecture: **128 BPM, 4/4, exactly 90 seconds = 48 bars = six eight-bar worlds, uninterrupted rhythmic spine.** No "D" round exists in this thread.

### 8a. Round 1 — A vs B (msg 0 / msg 1)

Nelson (msg 0), verbatim:

> listen to both & tell me what you think A or B? Choose from one of these or make another draft?

Franco's verdict (msg 1), verbatim:

> My call is another draft, C, built from B. Forced to choose only A or B, I choose B. B has the cleaner pulse, sharper transient peaks and more consistent bar-to-bar groove, so movement has a simpler skeleton to grab. A is more complete at 82.6 seconds, but it is brighter, denser and more arranged, with several dropouts and sectional shifts. It behaves more like a finished song that already wants to edit the reel for you. B behaves more like a spine. One important catch: the uploaded B is only 15.4 seconds, so it is currently a loop concept, not a usable master.

> Make C at 128 BPM in 4/4, using B's core rhythm. At 128 BPM, exactly 90 seconds equals 48 bars, which divides perfectly into six eight-bar worlds. You still vary the three shot lengths within each world, but every world gets a clean rhythmic room. Your current groove measures around 131 BPM, so slowing it to 128 is only about a two-percent change.

**The two-mix law (msg 1) — verbatim:**

> Create two versions of C from the same MIDI or sample timing. The generation guide should be dry and almost rudely obvious: clean kick, snare and hat; stronger first beat of every bar; no reverb tails; minimal ghost notes; one controlled turnaround at each world boundary. The audience mix can use richer drums and all six melodic overlays, but every transient must remain sample-accurate with the guide. Feed Seedance the stripped guide, not the decorative final mix. The model needs fence posts, not stained glass.

### 8b. Round 2 — C1 vs C2 (msg 10 / msg 11)

Nelson (msg 10), verbatim: `"now the version c of the audio, qa it, & tell me what you think"`

Franco's verdict (msg 11), verbatim:

> Audio call: C1 is the stronger production spine. Both files sit essentially at 128 BPM, which is exactly the grid we wanted. C1's detected beat spacing is more stable, with roughly half the timing variance of C2. It also has sharper, more continuous transient information, which gives Seedance clearer rhythmic fence posts.

> C2 is more musical and more dramatically shaped, but that is the problem for the generation guide. Its middle section becomes fuller and more tonal, then the percussion returns harder later. That could make the model treat different sections as different movement instructions. C2 feels closer to an audience mix or world overlay stem than the universal motion anchor.

> C1 is not final yet. It is 75.64 seconds, not 90, and it contains several noticeable density drops. The biggest concern is that the groove alternates between strong drum sections and thinner passages. If those thinner passages are intentional shot or world boundaries, good. If not, Seedance may reduce motion energy there even when the picture needs continuity.

**Build instruction (msg 11) — verbatim, this is the how-to-build-the-track spec:**

> Build the final C from C1. Extend it to exactly 90 seconds at 128 BPM, which equals 48 bars. Give each of the six worlds exactly eight bars. Keep the kick and primary backbeat present throughout all 48 bars. Change energy using hats, percussion layers and small fills, not by removing the spine.

> Put one unmistakable but controlled boundary marker at bars 9, 17, 25, 33 and 41. A short fill or single accent is enough. Do not use silence, cymbal washes or large melodic transitions. Every world should feel different in the final soundtrack, but the generation reference should remain almost boringly dependable.

> For generation, export each shot's exact section from this master rather than feeding every clip the entire 90-second file. Include one bar of pre-roll where Higgsfield allows it, but make the requested visible movement start on a clearly identified transient. Otherwise the model may choose its own section of the rhythm and your "anchor" becomes a decorative suggestion.

> Final verdict: C1 passes as the foundation, not as the locked master. C2 is not the universal anchor. Make C3 from C1: 90 seconds, 48 bars, uninterrupted kick and backbeat, cleaner world-boundary accents, no tonal swell strong enough to compete with the drums. That version will be genuinely useful for the audio-motion experiment rather than merely sounding good.

### 8c. Round 3 — E1 vs E2 (msg 16, 17 / msg 18) — **the current live verdict**

Nelson uploaded E1/E2 twice (msg 16 `"qa this"`, then msg 17 `"what about the music?"` after being ignored).

Franco's verdict (msg 18) — **verbatim, complete:**

> You're right, I skipped the music. I checked both.

> E1 is the better Seedance motion anchor. Its pulse is more obvious and more consistently aligned to the 128 BPM grid. E2 is brighter and smoother, but its extra high-frequency activity muddies what the model should follow.

> Both files are about 180 seconds, not 90. The first 90 seconds do equal 48 bars at 128 BPM, but do not just chop the MP3. E1 has a strong new transient exactly at 90 seconds, so a blunt cut could capture the beginning of bar 49. Export exactly 48 bars from the source session.

> E1's main weakness is the repeated near-silence before some 15-second boundaries, especially around 15, 45 and 60 seconds. The boundary accents are useful, but the drum spine should not disappear. Seedance may interpret those holes as "slow down or stop moving."

> Keep E1's rhythm and section markers, but leave a quieter kick or rim pulse running through every breakdown. World changes should feel like the room changes while the clock keeps ticking.

> E2's biggest failure is around 43–45 seconds, where the energy collapses almost completely before returning. It is also less metrically explicit than E1. I would not use E2 as the universal reference.

> Verdict: E1 wins, but it needs one final C-style cleanup. Exactly 90 seconds, 128 BPM, 48 bars, continuous underlying pulse, five controlled world-boundary accents, and no full rhythmic dropouts. That is the version I would attach to the beat-critical Higgsfield generations.

### 8d. The energy-hole warning — stated three times, treat as law

| Round | Where the hole is | Franco's words |
|---|---|---|
| A/B | A's arrangement | `"several dropouts and sectional shifts"` |
| C1/C2 | C1's thin passages | `"Seedance may reduce motion energy there even when the picture needs continuity."` |
| E1/E2 | E1 @ ~15s, 45s, 60s | `"Seedance may interpret those holes as \"slow down or stop moving.\""` |
| E1/E2 | E2 @ 43–45s | `"the energy collapses almost completely before returning"` |

**The fix, constant across rounds:** keep the kick/backbeat running through *every* breakdown; change energy with hats, percussion and fills, never by removing the spine. Boundary markers = short fill or single accent only. **Never silence, cymbal washes, or large melodic transitions.**

### 8e. Consolidated music target (all three rounds agree)

- 128 BPM, 4/4
- Exactly 90 seconds = 48 bars = six worlds × 8 bars
- Boundary accents at **bars 9, 17, 25, 33, 41** (five markers)
- Kick + primary backbeat continuous across all 48 bars
- Two mixes: dry **generation guide** (fed to Seedance) + richer **audience mix** (sample-accurate transients with the guide)
- Export per-shot sections from the master, not the whole 90s file; one bar of pre-roll where Higgsfield allows
- Export 48 bars **from the source session**, never by chopping the MP3

---

## 9. CROSS-CUTTING — IDENTITY, HAIR, JEWELRY, COLOUR

Not one of the eight requested topics, but these msg-1 rulings govern every costume and would otherwise be lost.

**Face read (msg 1) — verbatim:**

> This is a strong face anchor. Paola has warm medium-tan skin, dark high-contrast hair and brows, warm brown eyes, an oval tapered face and defined collarbones.

**Colour law (msg 1) — verbatim:**

> Her best near-face colors are pomegranate red, midnight indigo, deep forest, blackened aubergine, warm ivory and burnished gold. Weak beige, pale champagne, dusty gray and washed pastel pink risk flattening her. Clean square necklines, open V shapes and precise asymmetry will frame her especially well.

**Flower + hair + reference ruling (msg 1) — verbatim:**

> I would remove the pink flower from the master reference. Keep the sleek center part and low bun as the permanent hair silhouette, but the flower will leak into the skate, agent and couture looks and make them feel dressed rather than inhabited. Also create matching left-three-quarter and right-three-quarter identity references from this exact face. A frontal image alone will not adequately police her nose, jaw and eye shape across all three wardrobe angles.

**Earrings (msg 1) — verbatim:**

> Use the tiny hoop earrings already present as the continuity anchor, but standardize them as small warm-gold huggies in the clean identity master. They survive every neckline, work with the sari and kimono without hijacking either, and remain visible during facial identity shots.

**Flower rejected three separate times:** msg 1 (`"I would remove the pink flower"`), msg 14 Nelson (`"again lose the flowers"`), msg 20 (`"Remove the pink flower."`). Treat as hard-banned.

**Named reference tokens used in the prompts:** `Paola_Face_Lock`, `@Paola_Face_Lock`, `@Glasses_Lock`.

---

## APPENDIX — message index map

| Msg | Role | Topic |
|-----|------|-------|
| 0 | Nelson | Uploads Unchanging Groove A/B + face close-up ref; asks A or B |
| 1 | Franco | Music verdict (pick B, build C) + full costume revision pass + identity/colour law |
| 2 | Nelson | Rejects urban board styling; specifies white-outer/black-inner/leggings/beanie/curly hair |
| 3 | Nelson | "describe to pablo how to prompt this outfit" (URBAN) — **never answered in text** |
| 4 | Nelson | Picks sunglasses B, asks for eyewear matched to face + outfit |
| 5 | Nelson | Lower the tint so her eyes are recognizable |
| 6 | Franco | Wrong board; reset to AGENT |
| 7 | Franco | Generator "clinging to Bollywood"; clean restart |
| 8 | Franco | Declares prior outputs invalid; full AGENT board instruction A–F |
| 9 | Nelson | Approves agent look; "tactical black boots" |
| 10 | Nelson | Uploads Rehearsal Room Dry C1/C2; approves outfit; asks for prompt; urban generating on Higgs |
| 11 | Franco | **AGENT outfit prompt for Pablo** + C1/C2 audio verdict + build-the-track spec |
| 12 | Franco | Wrong carryover; reset to KIMONO |
| 13 | Nelson | Rejects all kimono outfits; pick the best for Paola |
| 14 | Nelson | Wants multiple options in one panel; "lose the flowers" |
| 15 | Nelson | "give pablo the prompt" (KIMONO) — **never answered at all** |
| 16 | Nelson | Uploads Metronomic Loop E1/E2; "qa this" |
| 17 | Nelson | Re-uploads E1/E2; "what about the music?" |
| 18 | Franco | E1 vs E2 verdict; E1 wins with C-style cleanup |
| 19 | Nelson | Skateboard colours not feminine → aurora + stickers; Higgs glasses are ugly |
| 20 | Franco | **Sunglasses prompt for Pablo** + reference-handling rule (skateboard not addressed) |
| 21 | Nelson | "franco generate the glass prop" |
| 22 | Nelson | Generated prop ≠ reference picture — **thread ends unresolved** |
