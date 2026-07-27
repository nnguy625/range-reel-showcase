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

```
Modern Bollywood club record, exactly 128 BPM, 4/4, Instrumental. This is the PEAK SECTION and it
opens on the hook in bar one, no intro and no build. A bright plucked string figure and a dry
double-headed hand-drum accent trade a two-bar call and answer, placed off the beat with clear air
between phrases. The bass sits on F, using F and the occasional C a fifth above, short and dry rather
than sustained. Everything above the bass is short and percussive and stops before the next attack
lands. The uploaded reference supplies the steady kick underneath; this layer sits on top of it.
Celebratory, warm, saturated, physical, crowded with joy. The space between phrases carries as much
weight as the phrases.
```

## WORLD 3 — GUN-FU · 0:30–0:45

```
Modern cinematic club record, exactly 128 BPM, 4/4, Instrumental. This is the PEAK SECTION and it
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
Modern cinematic club record with a traditional East Asian string colour, exactly 128 BPM, 4/4,
Instrumental. This is the PEAK SECTION and it opens on the hook in bar one, no intro and no build. A
plucked three-string figure and a single struck wooden accent trade a two-bar call and answer, placed
off the beat, with long deliberate gaps between phrases. The bass sits on F, using F and the
occasional C a fifth above, short and dry. Everything above the bass is a single committed attack
that decays before the next one lands. The uploaded reference supplies the steady kick underneath.
Serious, weighted, unhurried, dangerous. Single committed strikes with air between them - never a
flurry.
```

## WORLD 6 — GOLD COUTURE · 1:15–1:30

```
Modern fashion-house club record, exactly 128 BPM, 4/4, Instrumental. This is the PEAK SECTION and it
opens on the hook in bar one, no intro and no build. A glassy bell figure and a warm sustained pad
chord answer each other across two bars, and every second beat lands hard enough to walk to. The bass
sits on F, using F and the occasional C a fifth above, deep and confident. Gold, expensive, glossy,
unhurried, self-assured. Built so a model's step lands on every accent.
```

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
