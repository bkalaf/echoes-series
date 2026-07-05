# ENHANCE-UPGRADE-v1

## Status

First-pass maintenance / enhancement audit for **Echoes of Eidolon**.

This is **not** a completed exhaustive one-by-one verification of every canon, draft, and chapter file. It records verified fixes, confirmed risks, and the next precise passes required before broad prose-generation or precision-revision automation should run.

Do not treat this file as prose-insertion instructions. This file does not invent narrative anchors. Any future prose pass must work from actual prose present in `chapters/`, not from outline beats alone.

---

# Standards Used

Primary maintenance rules come from `AGENTS.md`:

- update affected indexes when chapters / visions / interludes / meaningful scenes are materially changed;
- distinguish settings from scenes;
- use `canon/15_SETTINGS.md`, `canon/16_SCENES.md`, `canon/21_TIME_AND_HEADER_METADATA.md`, and Book 1 outline / calendar files for affected Book 1 changes;
- include concrete required attachments, especially character, setting, scene, time/header metadata, prompt-support canon, and relevant city visual-analysis files;
- avoid inventing canon or prose anchors where source is missing.

---

# Completed In This Pass

## 1. Claude instruction file aligned to AGENTS workflow

Updated:

- `claude.md`

Purpose:

- tailored Claude instructions to consume packet attachments explicitly;
- added AGENTS-style source-of-truth hierarchy;
- added required attachment expectations;
- added city-analysis consumption rules;
- added precision-revision warning: do not create precise insertions from outline beats alone;
- added current Max / Bellwether naming rules.

## 2. Canon folder index crosslinks updated

Updated:

- `canon/README.md`

Purpose:

- added missing current canon files to the folder index;
- documented `18_MAXIMILIAN_BELLWETHER_LORE.md` as a support-canon file, not the Book 18 master arc authority;
- added maintenance reminder to check AGENTS-indexed files after chapter / scene changes.

## 3. Non-anchored narrative insertion map removed

Deleted:

- `drafts/revision_passes/BOOK01_MAX_BELLWETHER_NARRATIVE_INSERTS.md`

Reason:

- the file contained prose-style insertion guidance based on outline beats rather than actual prose anchors;
- this was unsafe for a precision-revision workflow.

## 4. `01_11` outline restoration

Updated:

- `drafts/01_11_the_bountiful_harvest.md`

Reason:

- an earlier Roslin formalization pass accidentally truncated most of the outline after Subchapter 2;
- restored subchapters, required dialogue intentions, continuity locks, preserve skeleton, allowed / not-allowed changes, next-chapter relationship, and open flags;
- kept current locked name **Roslin L. Hearthstone**.

## 5. `01_13` preservation guardrails restored

Updated:

- `drafts/01_13_the_thread_back_out.md`

Reason:

- a prior Max/Bellwether seed pass preserved the main beats but damaged the bottom `Preserve Skeleton?` contract;
- restored the non-negotiable preserve list for Carrio’s answer test, Gregory’s almost-correct warning, the group’s riddle confusion, Brynn asking for the riddle, Brynn adding the comma, the corrected reading, and Mae closing the scene direction;
- kept the subtle Mae/Max moving-maze look seed as a later Bellwether house-magic breadcrumb.

---

# High-Priority Upgrade Queue

## UPGRADE-001 — Batch-fix chapter heading metadata

### Finding

Sampled chapter prose files already use the general chapter-heading box, but at least some headings still use older beacon markup and abbreviated locations.

Examples to check across all `chapters/01_*`:

- beacon line uses `<span class="beacon ...">` instead of the AGENTS / Claude Font Awesome flame standard;
- locations use forms like `Van'kareth Estate, City of Aquila Matara` instead of the full specific-to-broad display order;
- city-state / section / district fields may be omitted even when canon metadata exists.

### Required pass

Run a dedicated heading pass over every narrative chapter:

1. Compare each chapter heading to `canon/21_TIME_AND_HEADER_METADATA.md`.
2. Use specific-to-broad location order:
   - building / site / landmark;
   - district;
   - section;
   - city;
   - city-state.
3. Replace older beacon spans with the current Font Awesome flame icon standard, unless a downstream renderer requires the old span.
4. Do not invent exact time or location where canon still marks it approximate / withheld / TBD.

## UPGRADE-002 — City-analysis attachment and use pass

### Finding

`canon/CITY_ANALYSISES.md` and `locales/images/analysis/*.analysis.json` exist, but chapter prose and draft packets do not consistently force their use as required attachments.

### Required pass

For each chapter / draft packet, add or verify required city-analysis attachments based on setting IDs:

| City / Location | Likely files |
|---|---|
| Aquila Matara | `canon/CITY_ANALYSISES.md`; `locales/images/analysis/AQM.analysis.json` |
| Skyrend Peak | `canon/CITY_ANALYSISES.md`; `locales/images/analysis/SPK.analysis.json` if present / otherwise source-limited SPK section in city analysis |
| Luminthalas | `canon/CITY_ANALYSISES.md`; `locales/images/analysis/LUM.analysis.json` |
| Pollyr Fen | `canon/CITY_ANALYSISES.md`; `locales/images/analysis/PFN.analysis.json` |
| Aes Sidhal | `canon/CITY_ANALYSISES.md`; `locales/images/analysis/ASL.analysis.json` |
| Nox Vaelor | `canon/CITY_ANALYSISES.md`; `locales/images/analysis/NVR.analysis.json` |

Use city analysis to support movement, class pressure, crowd behavior, civic architecture, weather, water, terrain, and institutional logic. Do not add decorative city paragraphs.

## UPGRADE-003 — Fold late-Horror scene addendum into master scene index

### Finding

Late Book 1 rows for `01_22` through `01_24` currently live in:

- `canon/16_SCENES_BOOK01_LATE_HORROR.md`

The file states it is an addendum until rows are folded into:

- `canon/16_SCENES.md`

### Required pass

Fold B01-S220 through B01-S246 into `canon/16_SCENES.md` in order, or keep the addendum but make every relevant prompt packet attach both the master scene index and the addendum explicitly.

Do not duplicate scene rows in both files unless the addendum is clearly marked as deprecated after folding.

## UPGRADE-004 — Canon crosslink cleanup for settings / scenes / time metadata

### Finding

`canon/15_SETTINGS.md` has crosslinks to characters, scenes, master outline, gesture signals, and prompt locks, but should also crosslink:

- `canon/CITY_ANALYSISES.md`;
- `canon/21_TIME_AND_HEADER_METADATA.md`;
- `canon/20_CITY_ALLEGIANCES.md` where city faction status matters.

### Required pass

Update `canon/15_SETTINGS.md` only after fetching the full current file and preserving all rows. Do not use partial fetches for full-file replacement.

## UPGRADE-005 — Character-name drift cleanup

### Finding

Known old or risky forms remain likely in prose / scene rows / older drafts:

- `Rosalind` / `Rosalind-Roslin` should become **Roslin L. Hearthstone** except where explicitly discussing old source text.
- `Geoffrik Vayne` should be reviewed against the current supporting-cast row **Geoffrik T. Vayne**.
- `Max` / `Bellwether` / `Maximilian` need context-aware review only where Mae speaks directly.
- `May` / `Mei` should become **Mae** unless quoted as an error.
- `Talandra` / `Captain` forms should stay corrected to **Major Tallandra H. Highwatch**.

### Required pass

Run a search-driven character drift pass, but do not auto-replace dialogue without reading context.

## UPGRADE-006 — Canon file numbering / duplication simplification

### Finding

There are now two `18_` canon files:

- `18_MOTHER_SYSTEM_ARC.md`
- `18_MAXIMILIAN_BELLWETHER_LORE.md`

The Max file is intentionally support canon, not the Book 18 master arc authority, but the duplicated number can confuse tools and humans.

### Required pass

Do **not** rename casually. If cleanup is desired, do a dedicated rename pass:

1. choose a stable filename, such as `19_MAXIMILIAN_BELLWETHER_LORE.md` or `SUPPORT_MAXIMILIAN_BELLWETHER_LORE.md`;
2. update every reference in `canon/05_CHARACTERS.md`, `canon/README.md`, affected drafts, and revision-pass files;
3. verify no stale reference to the old name remains.

## UPGRADE-007 — Duplicate / suspicious chapter artifacts

### Finding

Search results show both:

- `chapters/01_07_the_first_mirror.md`
- `chapters/01_07_the_first_mirror (1).md`

### Required pass

Compare both files before any deletion. If one is stale, move it to an archive folder or delete it only after confirming no unique material exists.

## UPGRADE-008 — Chapter-vs-draft alignment matrix

### Finding

Several chapters were generated from draft outlines, but the current repo needs a precise matrix showing whether each `chapters/01_*` prose file reflects its matching `drafts/01_*` outline.

### Required pass

Create a line-anchored alignment matrix for `01_00` through `01_24`:

| Chapter | Prose file | Draft file | Status | Missing / drift |
|---|---|---|---|---|
| 01_08 | `chapters/01_08...` | `drafts/01_08...` | sampled aligned for Max intro / first bell | heading metadata still needs pass |
| 01_09 | `chapters/01_09...` | `drafts/01_09...` | sampled aligned for repeated bells | heading metadata still needs pass |
| 01_13 | `chapters/01_13...` | `drafts/01_13...` | sampled aligned for Mae/Max look and Brynn comma | heading metadata still needs pass |

Do not fill this table by assumption. Fetch the prose and draft files before assigning status.

## UPGRADE-009 — Prompt-ready packet required links

### Finding

Many draft packets predate the current AGENTS attachment standard.

### Required pass

For every prompt-ready chapter draft, verify a `Required Canon Links` / attachments area includes:

- `canon/05_CHARACTERS.md`;
- `canon/15_SETTINGS.md`;
- `canon/16_SCENES.md` and any scene addendum needed;
- `canon/21_TIME_AND_HEADER_METADATA.md`;
- `canon/PROMPT_SUPPORT_CANON_LOCKS.md`;
- relevant city analysis files;
- direct source / vision / interlude files.

Remove correction clutter from prompt-ready packets only after the correction has been centralized in canon.

---

# Chapter-Specific Sampled Findings

## `chapters/01_08_the_weight_of_being_asked.md`

Sampled prose already includes:

- Max formally introducing himself as **Maximilian T. Bellwether**;
- the first muted service-bell seed;
- Mae estate household warmth and staff living in the house.

Needed upgrades:

- heading metadata pass;
- city-analysis attachment / AQM texture audit;
- verify against the full `drafts/01_08...` outline before any prose revision.

## `chapters/01_09_day_one_architecture.md`

Sampled prose already includes:

- the second disabled-bell sighting;
- Addie recognizing multiple bells as policy, not damage;
- breakfast / field-clothes / Barnaby household logic.

Needed upgrades:

- heading metadata pass;
- required city-analysis attachment check;
- verify all draft beats against prose before revision.

## `chapters/01_13_the_thread_back_out.md`

Sampled prose already includes:

- Mae / Max silent look during moving-maze logic;
- Addie filing the look with the house’s other unexplained details;
- Brynn’s comma explanation and corrected reading.

Needed upgrades:

- heading metadata pass;
- do not reinsert or duplicate the Mae/Max look unless actual prose later loses it;
- ensure draft preserve-guardrails stay restored.

---

# Do-Not-Repeat Rules

1. Do not create pseudo-precise insertion maps from outline beats.
2. Do not invent prose anchors.
3. Do not update a full file from a partial fetch.
4. Do not remove preserve-skeleton guardrails while adding one new seed.
5. Do not treat city analysis as optional decoration when the chapter’s location is a named city.
6. Do not rename support-canon files without updating every reference in one pass.
7. Do not declare a full repo-wide audit complete unless every target file has actually been fetched and checked.
