# Echoes of Eidolon Canon

This folder is the working source of truth for the **Echoes of Eidolon** series bible.

The current goal is not only to preserve world canon, but also to make chapter construction repeatable. Some chapters only need high-level summaries. Others need reconstruction-grade beat maps so a previously drafted chapter can be rewritten with the same skeleton, altered dialogue, and preserved continuity.

## Canon Folder Shape

- `00_CANON_PRIORITY.md` — source-of-truth hierarchy, user-edit protection, and superseded terms.
- `01_WORLD_RULES.md` — global world, nation, conjunction, ship, city, board, setting, constellation, and technology rules.
- `02_BOOK_SPINE.md` — 18-book master structure.
- `03_CHAPTER_OUTLINE_SYSTEM.md` — chapter detail levels, section-break rules, and reconstruction templates.
- `04_DEAR_READER_INTERLUDES.md` — standardized interlude format.
- `04_DEAR_READER_BOOK01_PLACEMENT.md` — Book 01 interlude placement, including post-`01_23` / pre-`01_24` placement.
- `05_CHARACTERS.md` — character naming authority, locked character notes, and supporting-cast index.
- `06_WITNESSES_ARCHITECTS_REWARDS.md` — Witness, Architect, domain, reward, and constellation-transformation authority.
- `07_CONTINUITY_LEDGER.md` — continuity warnings and unresolved items.
- `08_RESEARCH_REFERENCES.md` — WWII, science, myth, and atrocity reference structure.
- `09_STYLE_AND_PROSE_RULES.md` — prose and drafting rules.
- `10_BOOK01_CHAPTER_OUTLINES.md` — Book 01 chapter-outline index and parse-state map.
- `11_ARCHITECT_EXODUS_COMPROMISES.md` — Architect compromise-chain logic.
- `12_BOOK01_CALENDAR_TIMELINE.md` — Book 01 date / weekday / visible-subchapter calendar mapping.
- `13_ARCHITECT_WITNESS_CHARACTER_INDEX.md` — Architect / Witness character index.
- `14_VISUAL_BIBLE_IMAGE_PASS.md` — synthesized visual-reference layer for characters, settings, Witnesses, constellations, and symbolic object language. This file does not replace character/world/reward canon; it links into those sections.
- `15_SETTINGS.md` — setting registry with reusable place IDs and source files.
- `15_IMAGE_UPLOAD_REGISTER.md` — comprehensive ledger of uploaded image batches so visual references are not lost or reduced to only the highlighted examples.
- `15_UPLOADED_IMAGE_REFERENCE_INVENTORY.md` — uploaded image reference inventory.
- `16_SCENES.md` — master scene registry with source, date/time, setting, cast, and function.
- `16_SCENES_BOOK01_LATE_HORROR.md` — Book 01 late-Horror scene-registry addendum for `01_22` through `01_24` until folded into `16_SCENES.md`.
- `17_CHARACTER_GESTURE_SIGNALS.md` — recurring physical habits, fidgets, eye-mail communication rules, Addie pendant authority, and reader-signal behavior.
- `18_MOTHER_SYSTEM_ARC.md` — Mother / Dianne’s long-term system-character arc, including the reciprocal-simulation realization and concept-art-derived city-analysis hypotheses.
- `18_MAXIMILIAN_BELLWETHER_LORE.md` — Max / Mae / Bellwether support lore lock. This is a support file, not the Book 18 master arc authority; if this duplicate number becomes confusing, rename in a dedicated cleanup pass and update all references together.
- `20_CITY_ALLEGIANCES.md` — city allegiance tracking / faction declarations.
- `21_TIME_AND_HEADER_METADATA.md` — chapter-heading, date/time, location, and beacon metadata authority.
- `CITY_ANALYSISES.md` — writer-facing synthesis of image-derived city analysis files under `locales/images/analysis/*.analysis.json`.
- `PROMPT_SUPPORT_CANON_LOCKS.md` — compact prompt-support canon lock bundle.

## Top Rule

When generating or revising chapters, preserve the newest explicit correction unless the user explicitly removes it.

## Maintenance Rule

When a chapter, vision, interlude, or meaningful scene changes, check and update the affected index files named in `AGENTS.md`, especially `drafts/README.md`, `canon/15_SETTINGS.md`, `canon/16_SCENES.md`, `canon/21_TIME_AND_HEADER_METADATA.md`, and Book 1-specific outline/timeline files.
