# AGENTS.md

This repository is the working canon, outline, and generation-prep system for **Echoes of Eidolon**.

The goal is to maintain prompt-ready markdown packets that can generate narrative prose without losing canon, setting identity, scene continuity, source beats, temporal metadata, location metadata, or cross-file accountability.

---

# Source-of-Truth Hierarchy

When sources conflict, use this hierarchy unless the user explicitly overrides it in the current task:

1. Direct user instruction in the current conversation.
2. Active chapter / vision / interlude draft being edited.
3. Canon locks in `canon/`.
4. Character / setting / scene indexes.
5. Prior draft notes and scratchpad files.
6. Older memory or older source cards.

Flag real conflicts. Do not silently choose a lower-priority source.

---

# Required Maintenance After Narrative Insertions

Every time a narrative chapter, vision, interlude, or meaningful scene is added or materially changed, update the relevant indexes in the same work pass unless the user explicitly says not to.

Always check:

- `drafts/README.md`
- `canon/15_SETTINGS.md`
- `canon/16_SCENES.md`
- `canon/21_TIME_AND_HEADER_METADATA.md`

For Book 1 changes, also check:

- `canon/10_BOOK01_CHAPTER_OUTLINES.md`
- `canon/12_BOOK01_CALENDAR_TIMELINE.md`

For standalone vision changes, also check:

- `drafts/visions/README.md`
- parent chapter file that references the vision
- relevant scene rows in `canon/16_SCENES.md`

For Dear Reader / interlude changes, also check:

- `canon/04_DEAR_READER_INTERLUDES.md`
- `drafts/interludes/source_material/README.md`
- `drafts/README.md`
- relevant book outline or master outline

---

# Settings, Scenes, And Metadata

Settings are reusable places. Scenes are time-bound narrative events. Do not confuse them.

Any reusable place introduced by a chapter must have a setting row in `canon/15_SETTINGS.md`.

Every meaningful narrative unit needs a row in `canon/16_SCENES.md` with scene ID, source file, time/date, setting ID(s), setting summary, cast, and scene function.

Every prompt-ready normal narrative chapter must explicitly carry location and date/time metadata using `canon/21_TIME_AND_HEADER_METADATA.md`.

If no location or time applies, say so explicitly with values like `No Location`, `No Date/Time`, `Location Withheld`, `Date/Time Withheld`, or `Hour TBD`.

Normal narrative chapters should not be marked prompt-ready while required date/time remains `TBD`.

---

# Chapter Heading Box Standard

Normal narrative prose chapters use a centered, full-width chapter-heading box at the top of the chapter.

Final layout requirements:

- the heading begins on a **new page**;
- the box sits about **one quarter of the way down the page**;
- the box extends to the page margins;
- the box uses a genre-appropriate shadowed / bordered treatment;
- the Mark of the Orbs appears only here, not on subheaders.

The Mark of the Orbs asset is:

```md
assets/mark_of_orbs.svg
```

Canonical heading template:

```md
<div class="eidolon-chapter-heading page-break-before quarter-page" align="center">

![Mark of the Orbs](assets/mark_of_orbs.svg)

**Chapter <CHAPTER NUMBER>: <CHAPTER TITLE>**

<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>

<Weekday>, <ordinal day> of <Month>, <Hour Name> [<Midnight/Noon +/- hours>]

<i class="fa-solid fa-fire-flame-curved"></i> <BEACON COLOR> Beacon - Day <DAY NUMBER> of Conjunction #<CONJUNCTION NUMBER>

</div>
```

Use Font Awesome for the flame icon.

Location display order is **specific to broad**, omitting null values:

```md
<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>
```

---

# Subchapter Discipline

Do not overuse visible subchapter headings.

A visible subchapter heading should normally mark one of these:

1. significant location change;
2. POV change;
3. major time jump that changes scene conditions;
4. formal inserted structure such as a vision, interlude, letter, legal document, broadcast, or transcript;
5. major act-level turn where the chapter’s dramatic engine changes.

Do **not** create visible subchapter headings for every tactical beat, every topic shift, every joke, or every small emotional turn inside the same room and same POV.

Do **not** use the Mark of the Orbs on visible subchapter headings. Subheaders must stay visually simpler than chapter headers.

Use the standard markdown scene break instead:

```md
---
```

Scene IDs in `canon/16_SCENES.md` may remain more granular than visible subchapter headings. Scene indexing is for maintenance. Visible subchapters are for reader-facing structure.

---

# Prompt-Ready Draft Structure

A prompt-ready narrative draft should include:

- status and intended output;
- compile slot, chapter number, and chapter title;
- required and optional attachments;
- required canon;
- location status and specific-to-broad location display;
- building/site/landmark, district, section, city, and city-state;
- setting IDs;
- date/time status, date, weekday, hour, and certainty;
- beacon state, conjunction day, and conjunction number;
- visible header metadata;
- scene IDs;
- cast;
- continuity state in and out;
- chapter function;
- beat sequence;
- required dialogue;
- ending state;
- do-not-include rules.

Remove correction clutter from prompt-ready files. Keep corrections in central canon/support files.

---

# Required Attachments Rule

Minimum expected attachments for normal chapter generation:

- the chapter draft file itself;
- `canon/05_CHARACTERS.md`;
- `canon/15_SETTINGS.md`;
- `canon/16_SCENES.md`;
- `canon/21_TIME_AND_HEADER_METADATA.md`;
- `canon/PROMPT_SUPPORT_CANON_LOCKS.md`;
- any directly referenced vision/interlude/source file;
- any relevant city visual-analysis file.

Do not make the prose generator infer attachments from vague references.

---

# Source Preservation Rule

When the user uploads or dictates source material:

1. Save the raw or near-raw source where practical.
2. Create a structured parse / prompt file from it.
3. Crosslink both files.
4. Mark whether the parse is complete, partial, or needs source recovery.

Status labels must be honest: `Raw source saved`, `Source card only`, `Parsed L4`, `Prompt-ready`, `Needs source recovery`, or `Prose generated`.

---

# Pre-Commit Checklist For Agents

Before finishing a repo change, answer these:

1. Did I update every affected index?
2. Did I add every new setting to `canon/15_SETTINGS.md`?
3. Did I add or update every affected scene in `canon/16_SCENES.md`?
4. Did I add or validate location and temporal metadata under `canon/21_TIME_AND_HEADER_METADATA.md`?
5. Did I remove correction clutter from prompt-ready chapter files?
6. Did I list exact required attachments in the draft header?
7. Did I preserve raw source or clearly mark that source recovery is needed?
8. Did I avoid inventing canon where the source is missing?
9. Did I avoid unnecessary visible subchapter headings when `---` would be enough?
10. Did I cite or report the commit SHA and verification lines back to the user?
