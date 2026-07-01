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
5. `canon/05_CHARACTERS.md`.
6. `canon/15_SETTINGS.md`.
7. `canon/16_SCENES.md`.
8. Other attached canon files.
9. Older source or scratchpad files.

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
- specified insertions from standalone vision / interlude files;
- unresolved mysteries that the packet says should remain unresolved.

Compress only logistical beats.

Dramatize beats that change emotion, power, knowledge, relationship, danger, or setting.

---

# Output Format

Output format:

```md
# [CHAPTER TITLE]

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
6. The ending state matches the packet.
7. No later canon was revealed early.
8. No new plot mechanics were invented.

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
- canon/PROMPT_SUPPORT_CANON_LOCKS.md
- drafts/01_17_children_of_the_damned.md
- locales/images/analysis/PFN.analysis.json
```

# Example Required File List For A Vision-Insert Chapter

```md
REQUIRED FILES ATTACHED:
- claude.md
- canon/05_CHARACTERS.md
- canon/15_SETTINGS.md
- canon/16_SCENES.md
- canon/PROMPT_SUPPORT_CANON_LOCKS.md
- drafts/01_15_the_cities_that_disobeyed.md
- drafts/visions/01_03.md
- drafts/visions/01_04.md
```

# Example Required File List For Book 14 Architect Meeting

```md
REQUIRED FILES ATTACHED:
- claude.md
- canon/05_CHARACTERS.md
- canon/11_ARCHITECT_EXODUS_COMPROMISES.md
- canon/12_HANS_FILE_NOEL_EXILE.md
- canon/15_SETTINGS.md
- canon/16_SCENES.md
- canon/PROMPT_SUPPORT_CANON_LOCKS.md
- drafts/14_09_second_vision_parse.md
- drafts/14_09_second_vision_name_corrections.md
- scratchpad/14_09_the_unwound_core_beats.md
```
