# OVERLAY PROMPTS — WORLDS 2–6
### Built on the locked skate recipe. Ready to fire the moment Franco approves V9.

---

## THE LOCKED RECIPE — identical for every world

**Suno control surface — verify ALL of it before every fire:**

| Control | Value | Why |
|---|---|---|
| Audio condition | **Sample**, E1_MASTER_90 attached | Cover drifts (measured −1326 ms by bar 72) |
| Selection window | 00:00.0 – 01:00.0 | 32 bars, bar-aligned |
| **Lyrics mode** | **Instrumental** | ⚠ the word "Instrumental" in the prompt does NOT set this control |
| **Exclude Styles** | the ban list (below) | ⚠ bans NEVER go in the positive prompt |
| Audio Influence | **25–35** | 80 imports E1's own kick (drums 0.47 → 1.24/s); flams are 0.0% at every level so high buys nothing |
| Style Influence | **85** | 50 = "Moderate" = prompt only half-weighted |
| Weirdness | **10** | we want spec compliance, not surprise |
| Duration | **60 s** | 32 bars; 180 s invites song structure |
| Model | v5.5 | |

**Exclude Styles field — paste into the exclusion box, never the style box:**
```
rock guitar, electric guitar, acoustic guitar, supersaw, arpeggiator, riser, arcade, chiptune, house, EDM, synthwave, four-on-the-floor bassline, continuous sixteenth notes
```

**Every prompt is positive-only.** Franco confirmed: *"naming it inside the creative prompt gives that
concept positive semantic attention, which your own tests have already caught red-handed."*

**Every prompt names the root.** The spine's bass sits on **F**. Overlays use **F, with C a fifth
above** — or F's relative minor **D** where the world wants a darker colour. Never a neighbouring
semitone; skate and sword both generated on B (a tritone) and that was the dissonance Nelson heard.

**Gates before anything goes to Franco:** drums ≤ 0.75/s · flams ≤ 5% swept ±117 ms · bass root = F
or a consonant relation · lag-2 spectral ≥ 0.60 and lag-2 − lag-1 ≥ 0.08 (manual-review if missed).

---

## WORLD 2 — INDIA / BOLLYWOOD · 0:15–0:30

⚠ **REWRITTEN 2026-07-27 on Franco's ruling.** The old wording asked for *"a dry double-headed
hand-drum accent"* — a dholak. That is mid-band percussion, which is exactly what the drum gate
rejects, so the prompt and the gate contradicted each other and **all six V13 takes failed at
0.92–1.14/s.** The surgical chain could not rescue it; the duck plateaued at 0.87–0.89.

Franco: *"Regenerate World 2 without the hand drum. Do not carve out an exception… Keep the 0.75
ceiling because E1 is supposed to be the only rhythmic skeleton."* Any dholak goes in the **audience
mix later as a separate stem**, never in the overlay.

```
Modern Bollywood club record, exactly 128 BPM, 4/4. This is the PEAK SECTION and it
opens on the hook in bar one, no intro and no build. A bright plucked tumbi figure and a clipped
santoor strike trade a two-bar call and answer, placed off the beat with clear air between phrases.
The bass sits on F, using F and the occasional C a fifth above, short and dry rather than sustained.
Everything above the bass is a short pitched attack that stops before the next one lands. The
uploaded reference supplies the steady kick underneath; this layer sits on top of it. Celebratory,
warm, saturated, physical, crowded with joy. The space between phrases carries as much weight as the
phrases.
```

## WORLD 3 — GUN-FU · 0:30–0:45

```
Modern cinematic club record, exactly 128 BPM, 4/4. This is the PEAK SECTION and it
opens on the hook in bar one, no intro and no build. Low muted brass stabs and struck-steel accents
answer each other across a two-bar cell, placed off the beat, sparse and cold with long silences
between hits. The bass sits on D, the relative minor of the reference's F, using D and the occasional
A a fifth above, short and tight. Everything above the bass is a short attack that stops before the
next one lands. The uploaded reference supplies the steady kick underneath. Desaturated, tense,
controlled, expensive. Restraint is the character - the silence between hits is the threat.
```

## WORLD 4 — CAR CHASE · 0:45–1:00 · already generated, keep V5_CAR_b

*Franco's ruling: one-bar Latin cell is acceptable here. Take b is the stronger base. Re-run only if
the bass root drifts off F — currently reads A, a major third, which is consonant and usable.*

## WORLD 5 — JAPAN / SWORD · 1:00–1:15 · ⚠ MUST REGENERATE — currently a tritone

```
Modern cinematic club record with a traditional East Asian string colour, exactly 128 BPM, 4/4.
This is the PEAK SECTION and it opens on the hook in bar one, no intro and no build. A
plucked three-string figure and a single struck wooden accent trade a two-bar call and answer, placed
off the beat, with long deliberate gaps between phrases. The bass sits on F, using F and the
occasional C a fifth above, short and dry. Everything above the bass is a single committed attack
that decays before the next one lands. The uploaded reference supplies the steady kick underneath.
Serious, weighted, unhurried, dangerous. Single committed strikes with air between them - never a
flurry.
```

## WORLD 6 — GOLD COUTURE · 1:15–1:30

```
Modern fashion-house club record, exactly 128 BPM, 4/4. This is the PEAK SECTION and it
opens on the hook in bar one, no intro and no build. A glassy bell figure and a warm sustained pad
chord answer each other across two bars. The bell attacks are compact and dry with a hard front edge
and immediate release, leaving a clear pocket of silence before the next subdivision; the pad
underneath stays warm and sustained. The bass sits on F, using F and the occasional C a fifth above,
deep and confident. The uploaded reference supplies the steady pulse underneath; this layer sits on
top of it and never doubles it. Gold, expensive, glossy, unhurried, self-assured.
```

⚠ **REWRITTEN 2026-07-27 — second instance of the World 2 defect.** The old wording said *"every
second beat lands hard enough to walk to"* and *"Built so a model's step lands on every accent."*
The first asks the OVERLAY to supply the walking pulse, which is E1's job — Franco: *"E1 is supposed
to be the only rhythmic skeleton."* The second names the on-screen action, which
`describe-the-record-not-the-activity` forbids. Result: **V19_a/b measured drums 1.36 and 1.46**
against the 0.75 ceiling, and V19_a landed on **F#**, a semitone clash.

**⚠ PRE-FIRE CHECK — Franco's exact formulation (he corrected mine, which was too broad):**

> *"Scan for combinations rather than banning every attack-capable instrument. The danger pattern is
> an attacky source **plus repeated-timing language**: 'every beat,' 'each step,' 'running pattern,'
> 'constant ostinato,' 'repeating stabs,' or 'walking pulse.' A tumbi used in 49 deliberate attacks
> passed; a bell asked to drive the walk did not. **The rhythmic assignment is the poison, not always
> the instrument noun.**"*

So the banned thing is **attacky source × recurring rhythmic duty** — not the instrument itself.
E1 owns all rhythmic motion.

⚠ **Suno ignores numeric constraints.** "Only two or three deliberate bell strikes per two-bar phrase,
never a running bell pattern" moved onset count not at all (152/158, same as unconstrained). Buy
sparseness by changing the KIND of source, never by naming a number.

⚠ **The old closing line was *"Built so a model's step lands on every accent."*** That names the
on-screen action, which is precisely what Franco's describe-the-record law forbids — the scene
reference is the mechanism that produced the "really corny" rejects. The take fired at 02:10 on
07-27 still carried it; if that pair reads cliché, this is the first suspect.

## — OUTRO TAG · after the final drop · already generated

*`V5_RUNWAY_OUTRO_a/b` — drum-free at 0.26 and 0.34/s. Keep.*

---

## ORDER OF WORK

1. Franco approves V9 skate → recipe is ratified.
2. Fire **World 5 first** — it is the only remaining tritone and therefore the only known defect.
3. Then worlds 2, 3, 6.
4. Gate every pair before it goes to Franco. Push to
   `GDRIVE:\RANGE_REEL_MUSIC\` and give him the exact filenames.
5. Rotate superseded takes to `_TO_DELETE_VERIFY/` in the same pass.
6. Rebuild `MASTER_90_v4` once all six are approved, then re-run all four gates on the master.
