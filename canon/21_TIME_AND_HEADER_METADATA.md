# Time And Header Metadata Standard

This file defines how chapter and subchapter temporal metadata should be recorded for prompt-ready drafts and prose output.

The goal is to make date, weekday, and hour information explicit enough for prose generation, Obsidian review, scene indexing, and continuity repair.

---

# Core Rule

Every prompt-ready chapter must state its temporal metadata.

If a chapter has visible subheaders / subchapters, put the temporal metadata on the relevant subheader entries as well as in the Generation Packet Header.

If a chapter does **not** have subheaders, put the temporal metadata directly under the chapter title / chapter header.

This metadata is not decoration. It is part of continuity.

---

# Display Format

Use this two-line display format for chapter or subchapter headers:

```md
# <Chapter Title>

<Weekday>, <Day Number> <Month>
<Hour Name> (<relative anchor note>)
```

Example:

```md
# The Example Chapter

Kindlemask, 1 Hearthwake
Hour of the Gargoyle (1 hour before midnight)
```

For subchapters:

```md
## Subchapter 4 — The City Made Of Water

Eldrane, 14 Hearthwake
Hour of the Sphinx (4 hours after noon)
```

If the exact hour is not known yet, use:

```md
Hour TBD
```

Do not invent a precise hour just to fill the field. Mark it TBD, then resolve it during timeline cleanup.

---

# Generation Packet Header Fields

Prompt-ready drafts should include these fields in the **Generation Packet Header**:

| Field | Value |
|---|---|
| Date | `<Day Number> <Month>` |
| Weekday | `<Weekday>` |
| Time / Hour | `<Hour Name> (<relative anchor note>)` |
| Time Certainty | `Locked / Approximate / TBD` |
| Visible Header Metadata | `Chapter-level / Subchapter-level / Both / None yet` |

If the chapter spans multiple hours, use the start hour in the header and list the movement in a small timeline table under `## Temporal Metadata`.

---

# Relative Anchor Rule

Each named hour should be paired with a human-readable anchor note.

Use only **midnight** and **noon** as anchors.

Use the closest anchor and never use more than **6 hours** in the note.

Examples:

- `Hour of the Gargoyle (1 hour before midnight)`
- `Hour of the Wyrm (5 hours after midnight)`
- `Hour of the Chieftain (1 hour before noon)`
- `Hour of the Wayfarer (1 hour after noon)`
- `Hour of the Star-Siren (6 hours after noon)`
- `Hour of the Waxing Crescent (5 hours before midnight)`

Do not write:

- `Hour of the Waxing Crescent (7 hours after noon)`
- `Hour of the Chieftain (11 hours after midnight)`

---

# Anchor Tie Rule

For exact 6-hour distances:

- 6:00 AM / Hour of the Griffin = `6 hours after midnight`.
- 6:00 PM / Hour of the Star-Siren = `6 hours after noon`.

This keeps morning hours anchored to midnight and evening hours anchored to noon until the note would exceed six hours.

---

# Eidolon Hour Table

| Earth-Clock Range | Hour Name | Relative Anchor Note |
|---|---|---|
| 12:00 AM – 1:00 AM | Hour of the Restless Souls | midnight |
| 1:00 AM – 2:00 AM | Hour of the Sentry | 1 hour after midnight |
| 2:00 AM – 3:00 AM | Hour of the Dew-Stalker | 2 hours after midnight |
| 3:00 AM – 4:00 AM | Hour of the Vanguard | 3 hours after midnight |
| 4:00 AM – 5:00 AM | Hour of the Chimera | 4 hours after midnight |
| 5:00 AM – 6:00 AM | Hour of the Wyrm | 5 hours after midnight |
| 6:00 AM – 7:00 AM | Hour of the Griffin | 6 hours after midnight |
| 7:00 AM – 8:00 AM | Hour of the Phoenix | 5 hours before noon |
| 8:00 AM – 9:00 AM | Hour of the Waning Crescent | 4 hours before noon |
| 9:00 AM – 10:00 AM | Hour of the Iron Foundry | 3 hours before noon |
| 10:00 AM – 11:00 AM | Hour of the Aurora | 2 hours before noon |
| 11:00 AM – 12:00 PM | Hour of the Chieftain | 1 hour before noon |
| 12:00 PM – 1:00 PM | Hour of the High Market | noon |
| 1:00 PM – 2:00 PM | Hour of the Wayfarer | 1 hour after noon |
| 2:00 PM – 3:00 PM | Hour of the Bishop | 2 hours after noon |
| 3:00 PM – 4:00 PM | Hour of the Alchemist | 3 hours after noon |
| 4:00 PM – 5:00 PM | Hour of the Sphinx | 4 hours after noon |
| 5:00 PM – 6:00 PM | Hour of the Singularity | 5 hours after noon |
| 6:00 PM – 7:00 PM | Hour of the Star-Siren | 6 hours after noon |
| 7:00 PM – 8:00 PM | Hour of the Waxing Crescent | 5 hours before midnight |
| 8:00 PM – 9:00 PM | Hour of the Pack-Runner | 4 hours before midnight |
| 9:00 PM – 10:00 PM | Hour of the Courier | 3 hours before midnight |
| 10:00 PM – 11:00 PM | Hour of the Prowler | 2 hours before midnight |
| 11:00 PM – 12:00 AM | Hour of the Gargoyle | 1 hour before midnight |

---

# Obsidian / Metadata-Friendly Block

When useful, a prompt-ready draft may include a compact metadata block near the top:

```md
## Temporal Metadata

| Unit | Weekday | Date | Hour | Certainty |
|---|---|---|---|---|
| Chapter | Eldrane | 14 Hearthwake | Hour of the Wyrm (5 hours after midnight) | Approximate |
| Subchapter 1 | Eldrane | 14 Hearthwake | Hour of the Wyrm (5 hours after midnight) | Approximate |
| Subchapter 7 | Eldrane | 14 Hearthwake | Hour of the Aurora (2 hours before noon) | Approximate |
| Subchapter 17 | Eldrane | 14 Hearthwake | Hour of the Star-Siren (6 hours after noon) | Approximate |
```

Use `Unit` values that match the actual chapter or subchapter headings.

---

# Prose Output Rule

If the generation packet asks for header metadata in the prose output, the prose generator should place the two-line display metadata under the chapter title or under the relevant visible subchapter heading.

Example output:

```md
# Children of the Damned

Eldrane, 14 Hearthwake
Hour of the Wyrm (5 hours after midnight)

[Prose begins...]
```

For subchapters:

```md
## The City Made Of Water

Eldrane, 14 Hearthwake
Hour of the Aurora (2 hours before noon)

[Prose begins...]
```

---

# Review / Cleanup Requirement

Existing drafts created before this standard may lack explicit hour metadata.

During cleanup passes:

1. Add `Date`, `Weekday`, `Time / Hour`, `Time Certainty`, and `Visible Header Metadata` to the Generation Packet Header.
2. Add a `## Temporal Metadata` table when the chapter spans multiple time blocks.
3. Update `canon/16_SCENES.md` with matching time language.
4. Do not guess exact times if the source only supports approximate timing.
5. Use descriptive hour names in chapter/subchapter headers where appropriate.
