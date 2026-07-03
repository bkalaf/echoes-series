# Claude Narrative Generation Prompt

Use this prompt when submitting Echoes of Eidolon chapter packets to Claude for narrative prose generation.

Replace bracketed fields before use.

---

# Copy/Paste Prompt

You are generating narrative prose for **Echoes of Eidolon**.

Read every attached file before writing.

The primary chapter / vision / interlude packet is:

- `[PRIMARY_PACKET_FILE]`

The intended output is:

- `[NARRATIVE_PROSE_CHAPTER / VISION_SEQUENCE / DEAR_READER_INTERLUDE / SCENE_FRAGMENT]`

Required attached files for this generation are:

- `[REQUIRED_FILE_1]`
- `[REQUIRED_FILE_2]`
- `[REQUIRED_FILE_3]`

Optional attached files, if present, are:

- `[OPTIONAL_FILE_1]`
- `[OPTIONAL_FILE_2]`

First, compare the attached files against the **Required Attachments** listed in the primary packet’s Generation Packet Header.

If any required file is missing, stop and output only:

```md
Missing Required Files

- <missing file path>
```

If all required files are present, generate the prose.

Use `claude.md` as your generation behavior contract.

---

# Canon Priority

Use this priority order:

1. This instruction prompt.
2. The current user instruction.
3. The primary packet file: `[PRIMARY_PACKET_FILE]`.
4. `canon/PROMPT_SUPPORT_CANON_LOCKS.md`, if attached.
5. `canon/21_TIME_AND_HEADER_METADATA.md`, if attached.
6. `canon/05_CHARACTERS.md`.
7. `canon/15_SETTINGS.md`.
8. `canon/16_SCENES.md`.
9. Other attached canon files.
10. Older source or scratchpad files.

Do not invent missing canon.

If a required detail is missing and cannot be inferred from attached files, flag it before generating prose.

---

# Generation Task

Generate the requested narrative prose from `[PRIMARY_PACKET_FILE]`.

Do not produce an outline.

Do not produce revision notes.

Do not produce a summary of the attachments.

Do not include maintenance commentary.

Write the scene / chapter as prose.

---

# Required Handling

Preserve:

- required beats;
- exact dialogue locks;
- POV instructions;
- setting IDs and setting identity;
- character names and titles;
- continuity state in;
- continuity state out;
- location metadata and certainty level;
- temporal metadata and certainty level;
- chapter heading box requirements;
- beacon metadata;
- visible subchapter discipline;
- specified insertions from standalone vision / interlude files;
- unresolved mysteries that the packet says should remain unresolved.

Compress only logistical beats.

Dramatize beats that change emotion, power, knowledge, relationship, danger, or setting.

---

# Chapter Heading Box

For normal narrative chapters, include the centered Echoes chapter-heading box unless the packet says not to.

The heading box should be a new-page element placed about one quarter of the way down the page in final layout. Preserve the class names so downstream CSS can style the page break, margin placement, full-width border, and shadow.

Use this format:

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

The location line uses specific-to-broad order and omits null values.

If the packet marks heading metadata as `None`, `Withheld`, `No Location`, or `No Date/Time`, preserve that status rather than inventing missing fields.

Do not use the Mark of the Orbs on subchapter headings.

---

# Location And Temporal Metadata Handling

Use `canon/21_TIME_AND_HEADER_METADATA.md` if attached.

Location display order for prose-facing chapter headings:

```md
<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>
```

Date/hour display:

```md
<Weekday>, <ordinal day> of <Month>, <Hour Name> [<Midnight/Noon +/- hours>]
```

Example:

```md
The White Tower, The High Elf Ward, The Scriptoria, City of Luminthalas, State of Ascentia
Kindlemask, 3rd of Hearthwake, Hour of the Wyrm [Midnight +5 hours]
<i class="fa-solid fa-fire-flame-curved"></i> White Beacon - Day 3 of Conjunction #1
```

If no location applies, use:

```md
No Location
```

If no date/time applies, use:

```md
No Date/Time
```

Do not invent exact locations or exact hours. If location or time is `Approximate`, `TBD`, `Withheld`, `No Location`, or `No Date/Time`, preserve that status.

---

# Visible Subchapter Handling

Only include visible subchapter headings if the packet explicitly requests visible subchapters.

Visible subchapter headings should mark significant location changes, POV changes, major time jumps, formal inserted structures, or major act-level turns.

Do not create visible subchapter headings for every tactical beat, joke, topic shift, or emotional turn inside the same room and same POV.

Do not put the Mark of the Orbs on subchapter headings. Subchapter headings must remain visually simpler than the chapter heading.

Use the standard markdown scene break when a beat needs breathing room inside the same visible subchapter:

```md
---
```

If the packet contains older over-split subchapter notes, consolidate same-location / same-POV material according to the current user instruction.

---

# Output Format

Output format for a normal chapter:

```md
<div class="eidolon-chapter-heading page-break-before quarter-page" align="center">

![Mark of the Orbs](assets/mark_of_orbs.svg)

**Chapter [NUMBER]: [TITLE]**

[LOCATION LINE]

[DATE / HOUR LINE]

<i class="fa-solid fa-fire-flame-curved"></i> [BEACON LINE]

</div>

[PROSE]
```

Only include visible subchapter headings if the packet explicitly requests visible subchapters.

If the output must stop because of length, stop at a clean scene break and write:

```md
[CONTINUES]
```

Do not rush or summarize the ending just to fit.

---

# Final Check Before Responding

Before finalizing, silently verify:

1. All required files were attached.
2. All required beats were used.
3. Exact dialogue locks stayed exact.
4. The setting matches the setting files.
5. Character names match canon.
6. The location metadata matches the packet.
7. The temporal metadata matches the packet.
8. The heading box includes required chapter / location / time / beacon fields when applicable.
9. The heading box uses `assets/mark_of_orbs.svg` and appears only at chapter level.
10. Visible subchapter headings are not overused.
11. The ending state matches the packet.
12. No later canon was revealed early.
13. No new plot mechanics were invented.

Then output the prose only.

---

# Fill-In Checklist For The Human Submitting To Claude

Before submitting, fill these in:

```md
PRIMARY_PACKET_FILE:

INTENDED_OUTPUT:

REQUIRED FILES ATTACHED:
- claude.md
- canon/05_CHARACTERS.md
- canon/15_SETTINGS.md
- canon/16_SCENES.md
- canon/21_TIME_AND_HEADER_METADATA.md
- canon/PROMPT_SUPPORT_CANON_LOCKS.md
- <primary packet file>
- <chapter-specific file>
- <vision/interlude/source file if referenced>

OPTIONAL FILES ATTACHED:
- <city image analysis file if relevant>
- <master outline or book outline if helpful>
- <reward/witness/theme file if relevant>

TARGET LENGTH / STOPPING RULE:

VISIBLE SUBCHAPTER HEADINGS? yes/no

HEADER METADATA? chapter-level / subchapter-level / both / no

LOCATION METADATA STATUS? Specific / Partial / No Location / Location Withheld / Metaphysical / Historical / Vision

DATE/TIME METADATA STATUS? Dated / Approximate / TBD / No Date/Time / Date/Time Withheld

SPECIAL USER INSTRUCTION FOR THIS RUN:
```

---

# Example Required File List For A Book 1 Chapter

```md
REQUIRED FILES ATTACHED:
- claude.md
- canon/05_CHARACTERS.md
- canon/15_SETTINGS.md
- canon/16_SCENES.md
- canon/10_BOOK01_CHAPTER_OUTLINES.md
- canon/12_BOOK01_CALENDAR_TIMELINE.md
- canon/21_TIME_AND_HEADER_METADATA.md
- canon/PROMPT_SUPPORT_CANON_LOCKS.md
- drafts/01_21_the_stupid_thread.md
- locales/images/analysis/PFN.analysis.json
```

# Example Required File List For A Vision-Insert Chapter

```md
REQUIRED FILES ATTACHED:
- claude.md
- canon/05_CHARACTERS.md
- canon/15_SETTINGS.md
- canon/16_SCENES.md
- canon/21_TIME_AND_HEADER_METADATA.md
- canon/PROMPT_SUPPORT_CANON_LOCKS.md
- drafts/01_15_the_cities_that_disobeyed.md
- drafts/visions/01_03.md
- drafts/visions/01_04.md
```
