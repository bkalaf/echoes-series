# Time, Calendar, And Header Metadata Standard

This file defines how chapter, subchapter, vision, and interlude metadata should record **location**, **date**, **weekday**, and **hour** for prompt-ready drafts and prose output.

The goal is to make temporal and location continuity explicit enough for prose generation, Obsidian-style review, scene indexing, and continuity repair.

---

# Core Rule

Every prompt-ready chapter must state location and temporal metadata.

If a chapter has visible subheaders / subchapters, put the metadata on the relevant subheader entries as well as in the Generation Packet Header.

If a chapter does **not** have subheaders, put the metadata directly under the chapter title / chapter header.

This metadata is not decoration. It is part of continuity.

---

# Metadata Status Flags

Metadata should never be silently absent.

Use explicit status flags when location or time is unavailable, intentionally withheld, or non-diegetic.

## Date / Time Status

Allowed values:

| Status | Meaning | Use Case |
|---|---|---|
| `Dated` | The scene has a specific in-world date and time/hour. | Normal narrative chapters and subchapters. |
| `Approximate` | The scene has a known date and approximate time block. | Travel, fieldwork, uncertain transition scenes. |
| `TBD` | The source requires a date/time, but it has not been resolved yet. | Cleanup pass before final prompt readiness. |
| `No Date/Time` | The unit deliberately has no applicable in-world date/time. | Dear Reader interludes, some visions, abstract frames. |
| `Date/Time Withheld` | The story has a date/time, but the header should not expose it yet. | Mystery, reveal, or spoiler-sensitive scenes. |

Normal narrative chapters should not remain `TBD` when marked prompt-ready.

Dear Reader interludes may use `No Date/Time`.

Visions may use `No Date/Time` for the main-timeline header while still listing a historical / subjective context note in the metadata table.

## Location Status

Allowed values:

| Status | Meaning | Use Case |
|---|---|---|
| `Specific` | City-state / region, city, and specific setting are known. | Most grounded narrative scenes. |
| `Partial` | At least one location field is known, but not all. | Travel, mystery, subjective spaces, broad city movement. |
| `No Location` | No physical or meaningful narrative location applies. | Dear Reader interludes, abstract narration. |
| `Location Withheld` | The location exists but should not be exposed yet. | Spoiler-sensitive scenes or mystery reveals. |
| `Metaphysical` | The unit occurs in a non-ordinary space. | Witness space, mirror space, memory seams. |
| `Historical / Vision` | The unit occurs inside a remembered / witnessed historical scene. | Standalone visions and mirror sequences. |

Location fields are not all required. But if `Location Status` is not `No Location`, at least one location field must be populated.

---

# Display Format

Use this three-line display format for chapter or subchapter headers when both location and time are meant to appear in the prose output:

```md
# <Chapter Title>

<Location Display>
<Weekday>, <Day Number> <Month>
<Hour Name> (<relative anchor note>)
```

Example:

```md
# The Example Chapter

Aquila Matara, Mae's Estate, Back Porch
Kindlemask, 1 Hearthwake
Hour of the Gargoyle (1 hour before midnight)
```

For subchapters:

```md
## Subchapter 4 — The City Made Of Water

Pollyr Fen, Temple Wetland Quarter
Eldrane, 14 Hearthwake
Hour of the Sphinx (4 hours after noon)
```

If the exact hour is not known yet, use:

```md
Hour TBD
```

If no date/time applies:

```md
No Date/Time
```

If no location applies:

```md
No Location
```

Do not invent a precise hour just to fill the field. Mark it TBD, then resolve it during timeline cleanup.

---

# Generation Packet Header Fields

Prompt-ready drafts should include these fields in the **Generation Packet Header**:

| Field | Value |
|---|---|
| Location Status | `Specific / Partial / No Location / Location Withheld / Metaphysical / Historical / Vision` |
| Location Display | Human-readable comma-separated display line, or `No Location`. |
| City-State / Region | City-state, region, or broad source layer if known. |
| City | City name if known. |
| District / Section / Quarter | District, section, quarter, or neighborhood if known. |
| Specific Setting / Site | Building, room, landmark, route, or site if known. |
| Setting IDs | Exact setting IDs from `canon/15_SETTINGS.md`. |
| Date / Time Status | `Dated / Approximate / TBD / No Date/Time / Date/Time Withheld` |
| Date | `<Day Number> <Month>`, `No Date/Time`, or `TBD`. |
| Weekday | `<Weekday>`, `No Date/Time`, or `TBD`. |
| Time / Hour | `<Hour Name> (<relative anchor note>)`, `Hour TBD`, or `No Date/Time`. |
| Time Certainty | `Locked / Approximate / TBD / Not Applicable / Withheld` |
| Visible Header Metadata | `Chapter-level / Subchapter-level / Both / None / Withheld` |

If the chapter spans multiple locations or hours, use the start state in the header and list the movement in a small table under `## Location & Temporal Metadata`.

---

# Location Display Rule

Use a readable comma-separated location line.

Order from broad to specific:

```md
<City-State / Region>, <City>, <District / Section / Quarter>, <Specific Setting / Site>
```

Only include fields that are useful and known.

Examples:

```md
Aquila Matara, Mae's Estate, Back Porch
```

```md
Luminthalas, Section 1, White Tower Archives
```

```md
Pollyr Fen, Temple Wetland Quarter
```

```md
Historical Earth, Metropolis, Architect Council Chamber
```

```md
Witness Space
```

```md
No Location
```

Do not force all location fields to exist. Do force the absence to be explicit.

---

# Active Calendar Authority

Use this file as the calendar reference for prompt-header metadata unless a more specific book timeline overrides it.

Book-specific files, especially `canon/12_BOOK01_CALENDAR_TIMELINE.md`, may provide chapter-specific date mapping.

## Weekdays

Book 1 uses the active 8-day weekday cycle. **Sonntag is hidden until Book 18 and is not an active Book 1 weekday.**

| Cycle Position | Weekday | Legacy Earth Anchor / Substitute | Meaning |
|---:|---|---|---|
| 1 | Dravenkar | Monday | Dragonkin |
| 2 | Stonewake | Tuesday | Dwarves / Elementals |
| 3 | Aegalor | Wednesday | Avian |
| 4 | Sepraday | Thursday | Reptiles |
| 5 | Maskwa | Friday | Indigenous Americans |
| 6 | Eldrane | Saturday | Elves |
| 7 | Karskov | Sunday | Russian |
| 8 | Kindlemask | Extra active weekday | Fire / kindling irony; Brickett association after current canon shift. |
| Hidden | Sonntag | Hidden Day | Savior; not active until Book 18. |

## Months / Constellation Cycle

Use these month names unless superseded by a later canon calendar file.

| # | Month | Season Label | Zodiac / Constellation | Witness |
|---:|---|---|---|---|
| 01 | Hearthwake | Hearth's Rest | The Widow Spider | Horror / Regret |
| 02 | Whisperwane | Hearth's Rest | The Laughing Tree | Revel |
| 03 | Embercrown | Thawmarch | The Ember Dragon | Crown |
| 04 | Redharvest | Thawmarch | The Stonekeeper | Stone |
| 05 | Mourningtide | Thawmarch | The Empty Crucible | Mercy |
| 06 | Stormtide | Thawmarch | The Tempest Serpent | Tempest |
| 07 | Goldwake | Sunwanderer's Route | The Twin Thrones / The Veilmasked One | Dominion / Veils |
| 08 | Duskwane | Sunwanderer's Route | The River King | Tides |
| 09 | Highsun | Sunwanderer's Route | The Veiled Navigator | Lanterns |
| 10 | Dawnmere | Sunwanderer's Route | The Dawn Stag | Harvest |
| 11 | Bastionhold | Sunwanderer's Route | The Raven's Chain | Echoes |
| 12 | Ravenmere | Veilfall | The Open Boar | Hearth |
| 13 | Deepnight | Veilfall | The Moon Tortoise | Sand |
| 14 | Lanternmere | Veilfall | The Celestial Archer | Omen |
| 15 | Frostveil | Veilfall | The Solar Eagle | Meridian |
| 16 | Ashfall | Hearth's Rest | The Hollow Elf | Ash |
| 17 | Revelwake | Hearth's Rest | The Iron Rhino | Bastion |
| 18 | Yearsend | Hearth's Rest | The Silent Fox | Silence |

## Book 1 Month-Length Lock

Book 1 currently uses the 29-day month model from `canon/12_BOOK01_CALENDAR_TIMELINE.md`.

Do not use older 25-day / 28-day notes for Book 1 prompt metadata unless the user explicitly reopens the calendar model.

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

# Metadata-Friendly Block

When useful, a prompt-ready draft may include a compact metadata block near the top:

```md
## Location & Temporal Metadata

| Unit | Location Status | Location Display | Weekday | Date | Hour | Certainty |
|---|---|---|---|---|---|---|
| Chapter | Specific | Pollyr Fen, Temple Wetland Quarter | Eldrane | 14 Hearthwake | Hour of the Wyrm (5 hours after midnight) | Approximate |
| Subchapter 1 | Specific | Aquila Matara, Mae's Estate, Dining Room | Eldrane | 14 Hearthwake | Hour of the Wyrm (5 hours after midnight) | Approximate |
| Subchapter 7 | Partial | Pollyr Fen | Eldrane | 14 Hearthwake | Hour of the Aurora (2 hours before noon) | Approximate |
| Subchapter 17 | Specific | Pollyr Fen, Temple Wetland Quarter | Eldrane | 14 Hearthwake | Hour of the Star-Siren (6 hours after noon) | Approximate |
```

Use `Unit` values that match the actual chapter or subchapter headings.

---

# Prose Output Rule

If the generation packet asks for header metadata in the prose output, the prose generator should place the location/date/hour block under the chapter title or under the relevant visible subchapter heading.

Example output:

```md
# Children of the Damned

Pollyr Fen, Temple Wetland Quarter
Eldrane, 14 Hearthwake
Hour of the Wyrm (5 hours after midnight)

[Prose begins...]
```

For subchapters:

```md
## The City Made Of Water

Pollyr Fen, Canal Market Approach
Eldrane, 14 Hearthwake
Hour of the Aurora (2 hours before noon)

[Prose begins...]
```

For interludes:

```md
# Interlude: The Doomsday Shelf

No Location
No Date/Time

[Prose begins...]
```

---

# Review / Cleanup Requirement

Existing drafts created before this standard may lack explicit location and hour metadata.

During cleanup passes:

1. Add location fields to the Generation Packet Header.
2. Add `Date`, `Weekday`, `Time / Hour`, `Time Certainty`, and `Visible Header Metadata` to the Generation Packet Header.
3. Add a `## Location & Temporal Metadata` table when the chapter spans multiple locations or time blocks.
4. Update `canon/16_SCENES.md` with matching location and time language.
5. Do not guess exact times if the source only supports approximate timing.
6. Use descriptive hour names in chapter/subchapter headers where appropriate.
7. Do not mark a normal narrative chapter prompt-ready while its required date/time remains `TBD`.
8. Use `No Date/Time` and `No Location` intentionally for interludes, abstract frames, or visions where those fields do not apply.
