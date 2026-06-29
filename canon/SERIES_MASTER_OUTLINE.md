# Series Master Outline

This is the series-level compile and continuity outline for **Echoes of Eidolon**.

It is intentionally not a prose draft. It is the map that decides where drafted chapter files, subchapter groups, research interludes, hidden-theme stubs, scratchpad planning, scene indexes, setting indexes, and crosslinked canon pieces belong.

## Top Rules

### 1. Compile order lives here
Draft file names are working IDs, not final sequence authority. Manuscript compilation should follow this outline, not filename sorting.

A file named later can appear earlier in the compiled manuscript if the master outline places it there.

### 2. File routing rule: parsing vs prose

Use the repository directories consistently:

- `drafts/` = parsed chapter outlines, reconstruction outlines, draft-planning files, interlude drafts, protected fragments, and other author-facing planning that is not final prose.
- `scratchpad/` = rough master-planning documents, experimental beat systems, and future-book source conversations that may later be promoted into formal drafts or canon.
- `chapters/` = actual prose chapter text only. Temporary prose stubs are allowed only when explicitly marked as stubs.
- `canon/` = stable reference authority, continuity rules, rosters, settings, scenes, indexes, and cross-book structure.

Do not place beat outlines or parsing documents in `chapters/` unless they have been converted into prose or explicitly marked as temporary prose stubs.

### 3. Settings and scenes are tracked separately

Settings and scenes must stay distinct:

- **Settings** are reusable places: cities, sections, districts, landmarks, buildings, chambers, routes, and metaphysical spaces. They live in [`15_SETTINGS.md`](./15_SETTINGS.md).
- **Scenes** are specific narrative units: time/date + setting + cast + function. They live in [`16_SCENES.md`](./16_SCENES.md).

When a draft or scratchpad file changes location, date/time, or cast, update the setting/scene indexes and the relevant directory index:

- [`../drafts/README.md`](../drafts/README.md)
- [`../scratchpad/README.md`](../scratchpad/README.md)

### 4. Do not renumber casually
Do not rename or renumber draft files during active parsing unless there is a strong structural reason.

Renaming must be taken with care to ensure every reference, crosslink, chapter index, compile order entry, and canon pointer still matches.

### 5. Crosslinks are part of the architecture
Use crosslinks heavily. Drafts, canon files, research stubs, companion files, Witness files, settings, scenes, scratchpad files, and book-level outlines should point to each other wherever the connection matters.

The goal is not just organization. The goal is to make the hidden structure of the story visible to the author while preserving mystery for the reader.

### 6. Stubs are allowed and encouraged
Use intentional stubs for known future inserts.

A stub is a placeholder for a known structural element whose full prose may be written later or out of order. Stubs should be used for:

- WWII / historical parable chapters or Dear Reader interludes.
- Science chapters or science-theme inserts.
- Mythology / culture chapters or myth-theme inserts.
- Reward explanation chapters.
- Witness mirror scenes.
- Companion inheritance / hidden-theme scenes.
- Title-message / acrostic planning slots.
- Future-book council / Witness source scenes.

Stubs should be specific enough to preserve continuity and theme, but not so overdetermined that they block later discovery.

### 7. Hidden title messages are tracked here
Chapter titles may eventually encode hidden messages by first letter, last letter, or both.

Do not finalize title-message logic until the chapter list is stable enough to support it. Until then, titles may remain working titles.

### 8. Protected narrative fragments are edited separately
Some prose sections are preserved as protected narrative fragments. These should not be shortened or rewritten during ordinary chapter outline passes or broad prose passes.

A protected fragment may be tightened only during a dedicated pass for that fragment, with explicit attention to preserving meaning, emotional movement, structural function, and any hidden-theme logic.

## Crosslink Protocol

When a chapter references canon, add links where useful:

- Draft chapter file → relevant canon file.
- Master outline → draft chapter file.
- Book canon outline → draft chapter file.
- Research stub → book spine / theme file.
- Chapter with Witness material → Witness / Architect / Reward canon.
- Chapter with companion material → Character / Companion canon.
- Chapter with location material → Settings index.
- Chapter with time/place/cast material → Scenes index.
- Chapter containing protected prose → protected narrative fragment.
- Scratchpad source scene → adapted draft / canon index.

Use relative markdown where possible.

## Current Canon Links

- [Canon Priority](./00_CANON_PRIORITY.md)
- [World Rules](./01_WORLD_RULES.md)
- [Book Spine](./02_BOOK_SPINE.md)
- [Chapter Outline System](./03_CHAPTER_OUTLINE_SYSTEM.md)
- [Dear Reader Interludes](./04_DEAR_READER_INTERLUDES.md)
- [Characters](./05_CHARACTERS.md)
- [Witnesses / Architects / Rewards](./06_WITNESSES_ARCHITECTS_REWARDS.md)
- [Continuity Ledger](./07_CONTINUITY_LEDGER.md)
- [Research References](./08_RESEARCH_REFERENCES.md)
- [Style and Prose Rules](./09_STYLE_AND_PROSE_RULES.md)
- [Book 01 Chapter Outlines](./10_BOOK01_CHAPTER_OUTLINES.md)
- [Architect Exodus Compromises](./11_ARCHITECT_EXODUS_COMPROMISES.md)
- [Hans File / Noel Exile](./12_HANS_FILE_NOEL_EXILE.md)
- [Architect / Witness Character Index](./13_ARCHITECT_WITNESS_CHARACTER_INDEX.md)
- [Visual Bible — Image Pass Notes](./14_VISUAL_BIBLE_IMAGE_PASS.md)
- [Settings](./15_SETTINGS.md)
- [Scenes](./16_SCENES.md)

---

# Series-Level Book Map

| Book | Working Focus | Primary Companion / Day | Key Hidden Theme Slots |
|---|---|---|---|
| 01 | The Assistant. The Thread. The Torn. | Adeshka H. Sonntag / Sonntag | WWII oil embargo; Doomsday Shelf; oral tradition knots; Ariadne’s Thread; first public Moderator formation. |
| 02 | Gregory must breathe fire. | Gregory H. Frydrake / Dravenkar | Munich appeasement; ecological cascade; mono no aware; Sakura Branch. |
| 03 | Gregory accepts the spotlight. | Gregory H. Frydrake | Alan Turing wartime secrecy; legitimacy systems; divine kingship; Crownless King’s Coin. |
| 04 | Brynn owns royal lineage. | Brynn H. Stonevain / Stonewake | Romanov execution; epigenetic trauma; Fisher King; Yggdrasil Root. |
| 05 | Brynn comes out / accepts cost. | Brynn H. Stonevain | Turing persecution; biological sex spectrum; sacred androgyny; Spear of Destiny. |
| 06 | Tallandra must fly. | Major Tallandra H. Highwatch / Aegalor | Battle of Britain; aerodynamics; sky ascent myth; Dreaming Stone. |
| 07 | Tallandra puts honor aside. | Major Tallandra H. Highwatch | Bushido doctrine; game theory authority; warrior honor; Lion Tooth / Obsidian Mirror. |
| 08 | Carrio must shed skin. | Carrio H. Vessalor / Serpaday | Willem Arondeus / records; adaptive molting; serpent shedding; Bone Flute. |
| 09 | Carrio stops needing the center. | Carrio H. Vessalor | French Resistance couriers; attention economy; psychopomp guides; Lantern of Izanami. |
| 10 | Mattieu follows animal spirit. | High Theorimist Mattieu H. Cardinal / Maskwa | Navajo Code Talkers; animal cognition; totemic ancestors; White Stag Antler. |
| 11 | Mattieu becomes grounded. | Mattieu H. Cardinal | Nazi occultism; placebo/nocebo; false prophets; Salmon Scale. |
| 12 | Mae becomes selfless. | Mae’vyri H. Van’Kareth / Eldrane | Rosie the Riveter; distributed labor; hospitality rites; Jade Rabbit Mortar. |
| 13 | Mae spares a life. | Mae’vyri H. Van’Kareth | POW survival comparison; long-term consequence modeling; spared enemy myths; First Drum. |
| 14 | Yurislav confronts ruthlessness. | Yurislav H. Arslan / Karskov | Eastern Front attrition; predictive failure; fate weaving; Endless Loom Spindle. Includes the full historical council source scene and Second Vision full-memory parse. |
| 15 | Yurislav lineage with Mae. | Yurislav H. Arslan | Lorenz cipher; cryptography; hidden name myths; Serpent Mound Tablet. |
| 16 | Rhun must hold water. | Rhun H. Ignis / Stonewake | Atlantic convoys; water radiation shielding; flood myths; Feather of Ma’at. |
| 17 | Rhun replaces Brynn. | Rhun H. Ignis | Operation Paperclip; replacement psychology; successor myths; Black Tortoise Shell. |
| 18 | Addie completes the synthesis. | Adeshka H. Sonntag / Sonntag | Hiroshima deterrence; AI memory scale; Grail paradise; Holy Grail; final compassion synthesis. |

---

# Book 14 Planning Anchors

| Planning Slot | Working Title | File | Status | Function | Scene Links |
|---|---|---|---|---|---|
| B14.090 | The Unwound Core | [master council beats](../scratchpad/14_09_the_unwound_core_beats.md); [Second Vision parse](../drafts/14_09_second_vision_parse.md); [prose baseline](../chapters/17_00_the_original_architects.md) | Scratchpad expanded / draft parsed / prose baseline saved | Complete historical council meeting; canonical source conversation for Book 01 First Mirror adaptation. The Second Vision parse preserves the prose-derived full-memory lane, including the six-ark start state, consciousness-interface failure, Mother’s active simulation proposal, Noel’s watcher-seat origin, and twenty-four city-state architecture. Final placement may move later in the series. | B14-S090 through B14-S097 in [Scenes](./16_SCENES.md). |

---

# Book 01 Compile Order

Book 01 draft files are compiled in the order below. Draft filenames are stable working identifiers and do not need to be renamed just because the compile order changes.

| Compile Slot | Draft ID | Title | File | Status | Notes / Crosslinks |
|---|---|---|---|---|
| B01.000 | 01_00 | Prologue — The Mother Who Started the War | [draft](../drafts/01_00_prologue.md) | Parsed | Establishes Mother, Brickett, number sequence, first act of war. See [Book 01 Chapter Outlines](./10_BOOK01_CHAPTER_OUTLINES.md), [Settings](./15_SETTINGS.md), and [Scenes](./16_SCENES.md). |
| B01.010 | 01_01 | The Royal Astronomer’s Tower | [draft](../drafts/01_01_the_royal_astronomers_tower.md) | Parsed | Parent chapter with visible subchapters: The Zero-Variance Solstice; Factional Mistrust. Introduces Miriam, the purple beacon, Overseer, faction triangle, Moderator nomination crisis. Scene IDs B01-S010/B01-S011. |
| B01.020 | 01_02 | The Nomination | [draft](../drafts/01_02_the_nomination.md) | Parsed | Parent chapter with visible subchapters: The Gale Exposition; With Kwame. Introduces Addie’s private life, hair clip / Mark of the Orbs, purple dispatch, and Kwame’s signed nomination reveal. Scene IDs B01-S020/B01-S021. |
| B01.030 | 01_03 | The Witnesses | [draft](../drafts/01_03_the_witnesses.md) | Parsed | Standalone metaphysical parent chapter with visible subchapters: The Scene Between Stories; The Addendums; The Ballot; The First Shot. Mother’s shot is intentionally vague here; the consequence becomes readable after the Dear Reader interlude. Scene ID B01-S030. |
| B01.035 | DR_01 | Interlude: The Choice to Do Nothing | [draft](../drafts/interludes/01_interlude_the_choice_to_do_nothing.md) | Prose saved | Dear Reader / WWII interlude from `embargo.md`. Uses the oil embargo parable to frame inaction as action, foreshadows Brickett’s “My life for you,” and exits back to Addie alone in Kwame’s office before Concord collects her. |
| B01.040 | 01_04 | The Weight of the Beacon | [draft](../drafts/01_04_the_weight_of_the_beacon.md) | Parsed | Parent chapter folding old manuscript movements: The Weight of the Beacon; The Logic of the Unbelievable; Geometry and Mathematics. Introduces Tallandra’s detail, Boss/Barry, Brickett, the impossible brick, pawn-shop proof, and the Mark of the Orbs match. Scene IDs B01-S040/B01-S041/B01-S042. |
| B01.050 | 01_05 | The Core of the Conjunction | [draft](../drafts/01_05_the_core_of_the_conjunction.md) | Parsed | Parent chapter folding old manuscript movements: The Core of the Conjunction; The Three Hundred Steps. Includes blue-beacon activation, public scrolls, Addie/Brickett slot reveal, Verrick/Ruin intervention, Aquila Matara arrival, protected Addie speech, silent applause, and cosmic beacon response. Scene IDs B01-S050/B01-S051/B01-S052. |
| B01.060 | 01_06 | The Weight of the Roster | [draft](../drafts/01_06_the_weight_of_the_roster.md) | Parsed | Standalone Conclave chamber chapter. Reveals wall roster architecture, Mae’s Speaker role, Overseer/Dovren confrontation, scroll openings for Mae/Carrio/Rhün/Yurislav, power-transfer lockdown, Addie’s collection into the mirror, Gregory reveal, and Mae’s Brickett no-last-name question. Scene IDs B01-S060/B01-S061. |
| B01.070 | 01_07 | The First Mirror | [draft](../drafts/01_07_the_first_mirror.md); [prose stub](../chapters/01_07_the_first_mirror.md) | Parsed + prose stub | Parent chapter folding old manuscript movements: The First Mirror; The Second Mirror; Return to Normal. Applies First Mirror obfuscation as a one-time trust-sensitive device, preserves second-mirror Dovren/symbol logic, gives Horror’s three-thread riddle, and returns Addie to Rhün / Mae’s Aquila Matara estate. Full historical source for the council meeting is [Book 14 scratchpad beats](../scratchpad/14_09_the_unwound_core_beats.md), with the late-series full-memory lane parsed in [Second Vision parse](../drafts/14_09_second_vision_parse.md). Scene IDs B01-S070 through B01-S076. Expanded council beats saved at [expanded beats](../drafts/01_07_the_first_mirror_expanded_council_beats.md), with local correction layer at [name corrections](../drafts/01_07_first_mirror_name_corrections.md). |
| B01.080 | 01_08 | The Weight of Being Asked | [draft](../drafts/01_08_the_weight_of_being_asked.md) | Parsed | Parent chapter folding old manuscript movements: The Weight of Being Asked; The Weight of What He Wouldn’t Give. Introduces Max and Mae’s household ethic, consolidates the companion table, reveals Matthieu, Brynn’s refused scroll, Luminthalas / Bountiful Harvest, the H-pattern, Law of Threes, Overseer suffering, Yurislav’s node question, and Brickett’s carrot-diagram roster logic. Scene IDs B01-S080/B01-S081/B01-S082. |

## Book 01 Protected Narrative Fragments

These fragments are preserved prose baselines. Do not shorten or rewrite them during ordinary chapter passes.

| Fragment ID | Protected Text | File | Placement | Rule |
|---|---|---|---|---|
| B01.PROTECT.SPEECH.01 | Addie’s Three Hundred Steps speech | [protected fragment](../drafts/protected/01_05_addie_three_hundred_steps_speech.md) | Inside B01.050 / `01_05_the_core_of_the_conjunction.md` | Preserve as long-form public speech anchored by “I honestly don’t know.” |
