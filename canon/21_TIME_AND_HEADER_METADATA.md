# Time, Calendar, And Header Metadata Standard

This file defines how chapter, subchapter, vision, and interlude metadata should record **location**, **date**, **weekday**, **hour**, **beacon state**, and **chapter-heading display** for prompt-ready drafts and prose output.

The goal is to make temporal and location continuity explicit enough for prose generation, Obsidian-style review, scene indexing, continuity repair, and final chapter heading layout.

---

# Core Rule

Every prompt-ready chapter must state location and temporal metadata.

Normal narrative prose chapters should render that metadata in a centered chapter-heading box unless the user explicitly asks for a different output format.

Chapter heading boxes begin on a **new page** and should sit about **one quarter of the way down the page** in final layout.

If a chapter has visible subheaders / subchapters, put the relevant metadata in the outline and prompt packet, but do **not** automatically put a visible header before every beat. Visible subchapters are controlled by the Subchapter Discipline rule below.

Do **not** use the Mark of the Orbs image on subheaders. The Mark belongs to the chapter heading box only.

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

# Chapter Heading Box Display Standard

Normal narrative prose chapters should begin with a centered, full-width heading box.

Final layout requirements:

- the heading begins on a **new page**;
- the box sits about **one quarter of the way down the page**;
- the box extends to the page margins;
- the box uses a genre-appropriate shadowed / bordered treatment;
- the Mark of the Orbs appears only here, not on subheaders.

In markdown-generation output, represent this as a stylable block. Use Font Awesome for the flame icon.

Required order:

1. Mark of the Orbs image.
2. `Chapter <CHAPTER NUMBER>: <CHAPTER TITLE>`.
3. Location line.
4. Date / weekday / hour line.
5. Font Awesome flame icon + beacon color + beacon day line.

Canonical markdown/HTML template:

```md
<div class="eidolon-chapter-heading page-break-before quarter-page" align="center">

![Mark of the Orbs](assets/mark_of_orbs.svg)

**Chapter <CHAPTER NUMBER>: <CHAPTER TITLE>**

<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>

<Weekday>, <ordinal day> of <Month>, <Hour Name> [<Midnight/Noon +/- hours>]

<i class="fa-solid fa-fire-flame-curved"></i> <BEACON COLOR> Beacon - Day <DAY NUMBER> of Conjunction #<CONJUNCTION NUMBER>

</div>
```

Example:

```md
<div class="eidolon-chapter-heading page-break-before quarter-page" align="center">

![Mark of the Orbs](assets/mark_of_orbs.svg)

**Chapter 14: The Law Telling Us To Forget**

The White Tower, The High Elf Ward, The Scriptoria, City of Luminthalas, State of Ascentia

Kindlemask, 5th of Hearthwake, Hour of the Wyrm [Midnight +5 hours]

<i class="fa-solid fa-fire-flame-curved"></i> White Beacon - Day 3 of Conjunction #1

</div>
```

Beacon colors may later receive CSS classes such as `beacon-red`, `beacon-orange`, or `beacon-white`, but do not omit the visible text.

The downstream renderer / CSS should attach page-break and quarter-page placement to `.page-break-before.quarter-page`; prose generation should preserve the classes rather than inline-faking final layout.

---

# Location Display Rule

Use a readable comma-separated location line.

Final prose chapter headings use **specific to broad** order:

```md
<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>
```

Only include values that are known and non-null.

Examples:

```md
The White Tower, The High Elf Ward, The Scriptoria, City of Luminthalas, State of Ascentia
```

```md
Dining Room, Van'kareth Estate, City of Aquila Matara
```

```md
The Ribbit Hole, Red Thread District, City of Pollyr Fen
```

```md
Witness Space
```

```md
No Location
```

Do not force all location fields to exist. Do force the absence to be explicit.

Older broad-to-specific lines may remain in rough notes, but prompt-ready chapter headers should use this specific-to-broad order.

---

# Date / Hour Display Rule

Use this prose-facing time line:

```md
<Weekday>, <ordinal day> of <Month>, <Hour Name> [<Midnight/Noon +/- hours>]
```

Examples:

```md
Kindlemask, 3rd of Hearthwake, Hour of the Wyrm [Midnight +5 hours]
```

```md
Dravenkar, 17th of Hearthwake, Hour of the High Market [Noon]
```

If the exact hour is not known yet, use:

```md
Hour TBD
```

If no date/time applies:

```md
No Date/Time
```

Do not invent a precise hour just to fill the field. Mark it TBD, then resolve it during timeline cleanup.

---

# Beacon Display Rule

Normal Book 1 chapter headings should include beacon state when known.

Use this display shape:

```md
<i class="fa-solid fa-fire-flame-curved"></i> <BEACON COLOR> Beacon - Day <DAY NUMBER> of Conjunction #<CONJUNCTION NUMBER>
```

Examples:

```md
<i class="fa-solid fa-fire-flame-curved"></i> Orange Beacon - Day 15 of Conjunction #1
```

```md
<i class="fa-solid fa-fire-flame-curved"></i> Red Beacon - Day 17 of Conjunction #1
```

If beacon state is not applicable, use `Beacon State: Not Applicable` in metadata and omit the beacon line from final prose heading unless specifically requested.

If beacon state is withheld for spoiler reasons, mark `Beacon State: Withheld`.

---

# Subchapter Discipline

Visible subchapters are reader-facing structure. They are not beat labels.

A visible subchapter should normally mark one of these:

1. significant location change;
2. POV change;
3. major time jump that changes the scene conditions;
4. formal inserted structure such as a vision, interlude, letter, legal document, broadcast, or transcript;
5. major act-level turn where the dramatic engine changes.

Do not create visible subchapter headings for every small topic shift, tactical beat, joke, or emotional turn inside the same room and same POV.

Do not use the Mark of the Orbs on subchapter headings. Subchapters should be visually simpler than chapter headers.

Use the standard markdown scene break instead:

```md
---
```

Example: a dining-room lunch, strategy argument, and Mae entering to say “Nope. Nope nope.” should usually remain one visible subchapter if the location and POV are unchanged.

Scene IDs in `canon/16_SCENES.md` may remain more granular than visible subchapter headings. Scene indexing is for maintenance. Visible subchapters are for reader-facing structure.

---

# Generation Packet Header Fields

Prompt-ready drafts should include these fields in the **Generation Packet Header**:

| Field | Value |
|---|---|
| Chapter Number | Chapter number, or `Not Applicable` for interludes / visions. |
| Chapter Title | Display title. |
| Location Status | `Specific / Partial / No Location / Location Withheld / Metaphysical / Historical / Vision` |
| Location Display | Specific-to-broad comma-separated display line, or `No Location`. |
| Building / Site / Landmark | Building, room, landmark, route, or site if known. |
| District | District, ward, quarter, or neighborhood if known. |
| Section | Section or civic division if known. |
| City | City name if known. |
| City-State / Region | City-state, region, or broad source layer if known. |
| Setting IDs | Exact setting IDs from `canon/15_SETTINGS.md`. |
| Date / Time Status | `Dated / Approximate / TBD / No Date/Time / Date/Time Withheld` |
| Date | `<Day Number> <Month>`, `No Date/Time`, or `TBD`. |
| Weekday | `<Weekday>`, `No Date/Time`, or `TBD`. |
| Time / Hour | `<Hour Name> (<relative anchor note>)`, `Hour TBD`, or `No Date/Time`. |
| Time Certainty | `Locked / Approximate / TBD / Not Applicable / Withheld` |
| Beacon State | Color + meaning, or `Not Applicable` / `Withheld`. |
| Conjunction Day | Day number of current Conjunction, or `Not Applicable` / `TBD`. |
| Conjunction Number | Conjunction number, or `Not Applicable` / `TBD`. |
| Visible Header Metadata | `Chapter-level / Subchapter-level / Both / None / Withheld` |

If the chapter spans multiple locations or hours, use the start state in the header and list the movement in a small table under `## Location & Temporal Metadata`.

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

- `Hour of the Gargoyle [Midnight -1 hour]`
- `Hour of the Wyrm [Midnight +5 hours]`
- `Hour of the Chieftain [Noon -1 hour]`
- `Hour of the Wayfarer [Noon +1 hour]`
- `Hour of the Star-Siren [Noon +6 hours]`
- `Hour of the Waxing Crescent [Midnight -5 hours]`

Do not write:

- `Hour of the Waxing Crescent [Noon +7 hours]`
- `Hour of the Chieftain [Midnight +11 hours]`

---
