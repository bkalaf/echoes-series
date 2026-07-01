# Book 1 Generation Packet Header Proposals

Purpose: proposed Generation Packet Header values for Book 1 chapter drafts before inserting them into the individual files.

This is a review file, not the final migration. After approval, the packet headers should be inserted into the actual `drafts/01_*.md` files and then mirrored into `drafts/README.md`, `canon/10_BOOK01_CHAPTER_OUTLINES.md`, `canon/12_BOOK01_CALENDAR_TIMELINE.md`, and `canon/16_SCENES.md` as needed.

---

# Shared Book 1 Required Attachments

Unless a chapter-specific note says otherwise, every Book 1 narrative generation packet should require:

- `claude.md`
- `canon/05_CHARACTERS.md`
- `canon/15_SETTINGS.md`
- `canon/16_SCENES.md`
- `canon/21_TIME_AND_HEADER_METADATA.md`
- `canon/PROMPT_SUPPORT_CANON_LOCKS.md`
- `canon/10_BOOK01_CHAPTER_OUTLINES.md`
- `canon/12_BOOK01_CALENDAR_TIMELINE.md`
- the primary chapter draft file
- any explicitly referenced vision, interlude, source, or city-analysis file

## Beacon State Field

Add this field to packet headers and scene metadata:

| Field | Value |
|---|---|
| Beacon State | `None / Purple / Blue / Green / Yellow / Orange / Red / Withheld / Not Applicable`; include transition notes when the beacon changes during the chapter. |

For Book 1 review, use the current chapter’s active beacon state, not the eventual bookwide state.

## Time Handling Note

Where the exact hour is now locked by user review, use the named hour. Where an exact hour is not already locked, use `Hour TBD` and mark `Time Certainty` as `TBD` or `Approximate`. Do not invent exact hours during packet insertion.

---

# Status Key

| Status | Meaning |
|---|---|
| Locked for header insertion | User has supplied enough metadata to insert the packet header, aside from possible later subchapter refinements. |
| Partial lock / needs subchapter breakdown | Chapter-level metadata is usable, but subchapter location/time rows should be added before prose generation. |
| Needs source/structure review | The file is a parent/support file or older parse that needs more careful cleanup before packet insertion. |
| Needs time pass | Chapter placement is clear, but exact hour/subchapter timing still needs cleanup. |

---

# Proposed Chapter Packet Summary

| Draft | Title | Compile Slot | Header Status | Location Status | Date / Time Status | Beacon State | Scene IDs | Notes |
|---|---|---|---|---|---|---|---|---|
| `01_00_prologue.md` | Prologue — The Mother Who Started the War | B01.000 | Locked for header insertion | Specific + narrative frame | `Yearsend 29, Kindlemask`; Hour of the Gargoyle | None / blank | B01-S000 | Brickett/Mother scene in Skyrend Peak slums / poorest district; use `SET-SPK-SLUMS` and `SET-SPK-WAREHOUSE`. |
| `01_01_the_royal_astronomers_tower.md` | The Royal Astronomer’s Tower | B01.010 | Locked for header insertion | Specific | `Hearthwake 1, Dravenkar`; Hour of the Dew-Stalker | Purple activation during chapter | B01-S010; B01-S011 | Royal Observatory / Stormspire Aerie / Vharos sightline. |
| `01_02_the_nomination.md` | The Nomination | B01.020 | Locked for header insertion | Specific | `Hearthwake 1, Dravenkar`; Hour of the Star-Siren | None / blank per current review | B01-S020; B01-S021 | Starts at 6:00 PM in Skyrend Peak hotel / Gale Exposition route. |
| `01_03_the_witnesses.md` | The Witnesses | B01.030 | Locked for header insertion | Metaphysical | Time unknown / subjective | Purple active in main timeline, not visible in scene | B01-S030 | Location display: The scene between stories. |
| `01_04_the_weight_of_the_beacon.md` | The Weight of the Beacon | B01.040 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 2, Stonewake`; starts Hour of the Bishop; route through Sphinx / Singularity toward Star-Siren | Purple at start; blue transition by end | B01-S040; B01-S041; B01-S042 | Starts in Skyrend Peak academic/guild district / Meridian Accord Guildhall; moves through streets and pawn-shop refuge. |
| `01_05_the_core_of_the_conjunction.md` | The Core of the Conjunction | B01.050 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 2, Stonewake`; Hour of the Star-Siren at start | Blue just changed / blue active | B01-S050; B01-S051; B01-S052 | Starts in Skyrend Peak secure portal route and ends in Aquila Matara government/Seat of the 72 route. |
| `01_06_the_weight_of_the_roster.md` | The Weight of the Roster | B01.060 | Locked location; needs hour pass | Specific | `Hearthwake 2, Stonewake`; Hour TBD after Star-Siren | Blue active | B01-S060; B01-S061 | Entire chapter inside the Seat of the 72 / Conclave High Assembly in Aquila Matara. |
| `01_07_the_first_mirror.md` | The First Mirror | B01.070 | Needs source/structure review | Metaphysical + Historical / Vision + Specific | Time unknown / subjective mirror time | Blue active in main timeline; not visible in metaphysical layers | B01-S070 through B01-S076 | Parent outline; should reference standalone `drafts/visions/01_02.md` for Second Mirror where possible. |
| `01_08_the_weight_of_being_asked.md` | The Weight of Being Asked | B01.080 | Needs time pass | Specific | `Hearthwake 2, Stonewake`; late night / hour TBD | Blue active | B01-S080; B01-S081; B01-S082 | Mae estate arrival / kitchen / dining / care structure. |
| `01_09_day_one_architecture.md` | Day One Architecture | B01.090 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; morning / hour TBD | Green onset / active | B01-S090; B01-S091; B01-S092 | Mae estate morning / washroom / reporters / day-one launch. |
| `01_10_holes_in_the_wall.md` | Holes in the Wall | B01.100 | Needs time pass | Specific / route | `Hearthwake 3, Aegalor`; Day One / hour TBD | Green active | B01-S100 through B01-S104 | Team split across AQM, Luminthalas, and Aes Sidhal. |
| `01_11_the_bountiful_harvest.md` | The Bountiful Harvest | B01.110 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; Day One / hour TBD | Green active | B01-S110 | Luminthalas lower-quarter restaurant scene. |
| `01_12_the_unwound_core.md` | The Unwound Core | B01.120 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; green phase / hour TBD | Green active | B01-S120 | Mae estate family-room synthesis and green-beacon pivot. |
| `01_13_the_thread_back_out.md` | The Thread Back Out | B01.130 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; green phase / hour TBD | Green active | B01-S130 | Ariadne / Barnaby / comma-riddle chapter. |
| `01_14_the_law_telling_us_to_forget.md` | The Law Telling Us To Forget | B01.140 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 6, Eldrane`; Day Four / hour TBD | Green at start; yellow transition by end | B01-S140 proposed | Luminthalas Section 5 Portalport to Section 1 White Tower Archives. Requires `locales/images/analysis/LUM.analysis.json`. |
| `01_15_the_cities_that_disobeyed.md` | The Cities That Disobeyed | B01.150 | Ready for header insertion after review; needs hour pass | Metaphysical + Historical / Vision + Specific | `Hearthwake 6, Eldrane`; yellow beacon / hour TBD | Yellow active | B01-S150 proposed | Uses standalone `drafts/visions/01_03.md` and `drafts/visions/01_04.md`. |
| `01_16_rapid_acceptance.md` | Rapid Acceptance | B01.160 | Ready for header insertion after review; needs hour pass | Specific | `Hearthwake 6, Eldrane`; evening/night / hour TBD | Yellow active | B01-S160 proposed | Mae estate back porch / protected legal debrief with Tikket. |
| `01_17_children_of_the_damned.md` | Children of the Damned | B01.170 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 14, Eldrane`; Conjunction Day Twelve / multiple hours TBD | Green? / checkpoint turns Orange by end; confirm pre-orange beacon state | B01-S170 proposed | Mae estate to Pollyr Fen; requires `locales/images/analysis/PFN.analysis.json`. Formal company name: `Van'Kareth South Aurreth Shipping Co.` |

---

# Skyrend Peak Location Notes From Analysis

Skyrend Peak is a vertical raptorfolk fortress-civilization where height, wind, watchfulness, signal towers, cliff platforms, and defensive civic architecture are the grammar of daily life.

Useful location logic for early chapters:

- Poor / slum spaces should still feel vertical: sheltered lower ledges, stacked dwellings, windbreaks, service cuts, rotting tower interiors, and unsafe routes beneath official terraces.
- Hotels / inns fit the analysis as high-altitude inns, wind-sheltered balconies, tower bases, or ledge plazas near the Gale Exposition / transit route.
- The Meridian Accord Guildhall can sit in a guild / academic / civic-service district near formal tower infrastructure rather than a generic business district.
- The Royal Observatory and Stormspire Aerie sit naturally in the city’s watch/signal/beacon identity.

Current setting IDs already available:

- `SET-SPK-SLUMS`
- `SET-SPK-WAREHOUSE`
- `SET-SPK-ROYAL-OBS`
- `SET-SPK-STORMSPIRE`
- `SET-SPK-PORTALPORT`
- `SET-SPK-GALE-HOTEL`
- `SET-SPK-GALE-314`
- `SET-SPK-MERIDIAN-GUILDHALL`
- `SET-SPK-KWAME-OFFICE`
- `SET-SPK-GUILD-ELEVATOR`
- `SET-SPK-GUILD-LOBBY`
- `SET-SPK-PUBLIC-STREETS`
- `SET-SPK-PAWN-SHOP`
- `SET-SPK-SECURE-PORTAL`

Potential new setting to add during migration:

- `SET-SPK-GUILD-ACADEMIC-DISTRICT` — proposed district / section for Meridian Accord Guildhall, academic guild offices, and civic knowledge/labor institutions.

---

# Proposed Full Headers For Newly Locked Set: `01_00`–`01_07`

## `drafts/01_00_prologue.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Locked for header insertion; needs final subchapter metadata check |
| Intended Output | Narrative prose prologue |
| Compile Slot | B01.000 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_00_prologue.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_00_prologue.md`; `locales/images/analysis/SPK.analysis.json` |
| Optional Attachments | `canon/CITY_ANALYSISES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific + narrative frame |
| Location Display | Skyrend Peak, slums / poorest lower-perch district, rotting warehouse |
| City-State / Region | Erzengel / Skyrend Peak layer |
| City | Skyrend Peak |
| District / Section / Quarter | Slums / poorest lower-perch district |
| Specific Setting / Site | Rotting warehouse |
| Settings Used | `SET-META-NARRATOR`; `SET-SPK`; `SET-SPK-SLUMS`; `SET-SPK-WAREHOUSE` |
| Date / Time Status | Dated |
| Date | 29 Yearsend |
| Weekday | Kindlemask |
| Time / Hour | Hour of the Gargoyle (1 hour before midnight) |
| Time Certainty | Locked |
| Beacon State | None / blank |
| Visible Header Metadata | Subchapter-level if Dear Reader frame and Brickett scene are separated; chapter-level fallback uses Brickett scene metadata |
| Scene IDs | B01-S000 proposed |
| Cast | Brickett H.; Mother / Dianne; Dear Reader narrator if frame is visible |
| Continuity State In | Before the Book 1 beacon chain begins; Brickett is alone in the poorest part of Skyrend Peak. |
| Continuity State Out | Mother has prepared Brickett with the pack / note / blanket path that will place him into the Book 1 companion chain. |
```

## `drafts/01_01_the_royal_astronomers_tower.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Locked for header insertion |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.010 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_01_the_royal_astronomers_tower.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_01_the_royal_astronomers_tower.md`; `locales/images/analysis/SPK.analysis.json` |
| Optional Attachments | `canon/CITY_ANALYSISES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific |
| Location Display | Skyrend Peak, Royal Observatory / Stormspire Aerie sightline |
| City-State / Region | Erzengel / Skyrend Peak layer |
| City | Skyrend Peak |
| District / Section / Quarter | Beacon / watch / observatory height |
| Specific Setting / Site | Royal Observatory of Skyrend Peak; Stormspire Aerie; Vharos beacon sightline |
| Settings Used | `SET-SPK`; `SET-SPK-ROYAL-OBS`; `SET-SPK-STORMSPIRE`; `SET-VHAROS-BEACON` |
| Date / Time Status | Dated |
| Date | 1 Hearthwake |
| Weekday | Dravenkar |
| Time / Hour | Hour of the Dew-Stalker (2 hours after midnight) |
| Time Certainty | Locked |
| Beacon State | Purple activation during chapter |
| Visible Header Metadata | Chapter-level unless subchapters are used |
| Scene IDs | B01-S010; B01-S011 |
| Cast | Royal Astronomer Miriam G. Ben-Or; relevant assistants / signal chain as needed |
| Continuity State In | The Conjunction system has been dormant for a thousand years. |
| Continuity State Out | Miriam verifies the purple beacon activation and the warning chain begins. |
```

## `drafts/01_02_the_nomination.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Locked for header insertion; route subchapter metadata still useful |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.020 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_02_the_nomination.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_02_the_nomination.md`; `locales/images/analysis/SPK.analysis.json` |
| Optional Attachments | `canon/CITY_ANALYSISES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific / route |
| Location Display | Skyrend Peak, Gale Exposition hotel / high-altitude inn route |
| City-State / Region | Erzengel / Skyrend Peak layer |
| City | Skyrend Peak |
| District / Section / Quarter | Gale Exposition / hotel and Portalport route |
| Specific Setting / Site | Portalport Station; Gale Exposition hotel; Room 314; Meridian Accord Guildhall |
| Settings Used | `SET-SPK`; `SET-SPK-PORTALPORT`; `SET-SPK-GALE-STREETS`; `SET-SPK-GALE-HOTEL`; `SET-SPK-GALE-314`; `SET-SPK-MERIDIAN-GUILDHALL`; `SET-SPK-KWAME-OFFICE` |
| Date / Time Status | Dated |
| Date | 1 Hearthwake |
| Weekday | Dravenkar |
| Time / Hour | Hour of the Star-Siren (6 hours after noon) |
| Time Certainty | Locked at chapter start |
| Beacon State | None / blank per current user review |
| Visible Header Metadata | Subchapter-level preferred because the chapter moves from hotel/private room to Guildhall |
| Scene IDs | B01-S020; B01-S021 |
| Cast | Addie; Guildmaster Kwame Odion Mensah; hotel / guild figures as needed |
| Continuity State In | Addie is in Skyrend Peak for the Gale Exposition, not because it is her home city. |
| Continuity State Out | Addie has been pulled into the nomination crisis and becomes the center of institutional attention. |
```

## `drafts/01_03_the_witnesses.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Locked for header insertion |
| Intended Output | Narrative prose chapter / metaphysical Witness sequence |
| Compile Slot | B01.030 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_03_the_witnesses.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_03_the_witnesses.md` |
| Optional Attachments | `canon/13_ARCHITECT_WITNESS_CHARACTER_INDEX.md` if relevant |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Metaphysical |
| Location Display | The scene between stories |
| City-State / Region | Metaphysical / Witness layer |
| City | No physical city |
| District / Section / Quarter | N/A |
| Specific Setting / Site | Witness void / scene between stories |
| Settings Used | `SET-WITNESS-VOID` |
| Date / Time Status | Date/Time Withheld / subjective |
| Date | Time unknown |
| Weekday | Time unknown |
| Time / Hour | Time unknown |
| Time Certainty | Withheld / not applicable |
| Beacon State | Purple active in main timeline, but not visible in the metaphysical space |
| Visible Header Metadata | Chapter-level; use location + time unknown if displayed |
| Scene IDs | B01-S030 |
| Cast | Addie; Witnesses including Silence and Horror/Regret as applicable |
| Continuity State In | Addie has been pulled beyond ordinary institutional reality into Witness contact. |
| Continuity State Out | Addie returns from the Witness encounter carrying the first impossible pressure of the Conjunction. |
```

## `drafts/01_04_the_weight_of_the_beacon.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Partial lock / needs subchapter location-time breakdown |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.040 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_04_the_weight_of_the_beacon.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_04_the_weight_of_the_beacon.md`; `locales/images/analysis/SPK.analysis.json` |
| Optional Attachments | `canon/CITY_ANALYSISES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific / route |
| Location Display | Skyrend Peak, Meridian Accord Guildhall / academic-guild district to public streets and pawn-shop refuge |
| City-State / Region | Erzengel / Skyrend Peak layer |
| City | Skyrend Peak |
| District / Section / Quarter | Academic-guild district proposed; public streets; pawn-shop refuge route |
| Specific Setting / Site | Kwame's office; Guildhall elevator/lobby; public streets; temporary pawn-shop refuge |
| Settings Used | `SET-SPK`; `SET-SPK-MERIDIAN-GUILDHALL`; `SET-SPK-KWAME-OFFICE`; `SET-SPK-GUILD-ELEVATOR`; `SET-SPK-GUILD-LOBBY`; `SET-SPK-PUBLIC-STREETS`; `SET-SPK-PAWN-SHOP` |
| Date / Time Status | Dated / multiple time blocks |
| Date | 2 Hearthwake |
| Weekday | Stonewake |
| Time / Hour | Starts Hour of the Bishop (2 hours after noon); pawn-shop refuge around Hour of the Sphinx (4 hours after noon); movement continues through Hour of the Singularity (5 hours after noon) toward Hour of the Star-Siren (6 hours after noon) |
| Time Certainty | User-locked sequence; subchapter exactness still to verify against draft text |
| Beacon State | Purple at start; blue transition by end / into next chapter |
| Visible Header Metadata | Subchapter-level required because the chapter moves through multiple locations and hours |
| Scene IDs | B01-S040; B01-S041; B01-S042 |
| Cast | Addie; Kwame; Major Tallandra; Concord detail; Brickett; guards/crowd figures as applicable |
| Continuity State In | Addie is still inside the Skyrend Peak institutional crisis, with the beacon pressure intensifying. |
| Continuity State Out | Addie has passed through public danger and proof-of-mark crisis and is being moved toward secure portal transfer. |
```

## `drafts/01_05_the_core_of_the_conjunction.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Partial lock / needs subchapter route breakdown |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.050 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_05_the_core_of_the_conjunction.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_05_the_core_of_the_conjunction.md`; `locales/images/analysis/SPK.analysis.json` |
| Optional Attachments | `locales/images/analysis/AQM.analysis.json`; `canon/CITY_ANALYSISES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific / route |
| Location Display | Skyrend Peak secure portal route to Aquila Matara, government / Seat of the 72 approach |
| City-State / Region | Skyrend Peak layer to Aquila Matara capital layer |
| City | Skyrend Peak; Aquila Matara |
| District / Section / Quarter | Skyrend Peak secure Portalport route; Aquila Matara civic/government core / Section 3 equivalent |
| Specific Setting / Site | Restricted transit corridor; portal to Aquila Matara; imperial avenue; Three Hundred Steps; Conclave threshold |
| Settings Used | `SET-SPK-SECURE-PORTAL`; `SET-PORTAL-AQM`; `SET-AQM`; `SET-AQM-IMPERIAL-AVENUE`; `SET-AQM-THREE-HUNDRED-STEPS`; `SET-AQM-CONCLAVE-THRESHOLD` |
| Date / Time Status | Dated / multiple locations |
| Date | 2 Hearthwake |
| Weekday | Stonewake |
| Time / Hour | Hour of the Star-Siren (6 hours after noon) at start |
| Time Certainty | Locked at start; route timing may need subchapter refinement |
| Beacon State | Blue just changed / blue active |
| Visible Header Metadata | Subchapter-level preferred because the chapter crosses cities |
| Scene IDs | B01-S050; B01-S051; B01-S052 |
| Cast | Addie; Major Tallandra; Concord escort; Aquila Matara crowd / Conclave figures as applicable |
| Continuity State In | The blue beacon has just changed and Addie is being moved out of Skyrend Peak toward the capital. |
| Continuity State Out | Addie reaches the Aquila Matara seat-of-power route and becomes publicly visible as the expected figure. |
```

## `drafts/01_06_the_weight_of_the_roster.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Locked location; needs hour pass |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.060 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_06_the_weight_of_the_roster.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_06_the_weight_of_the_roster.md`; `locales/images/analysis/AQM.analysis.json` |
| Optional Attachments | `canon/CITY_ANALYSISES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific |
| Location Display | Aquila Matara, Conclave High Assembly / Seat of the 72 |
| City-State / Region | Aquila Matara capital layer |
| City | Aquila Matara |
| District / Section / Quarter | Government / Seat of Power / Section 3 equivalent |
| Specific Setting / Site | Conclave High Assembly; Speaker's dais; High Sovereign's exception seat |
| Settings Used | `SET-AQM-CONCLAVE`; `SET-AQM-CONCLAVE-BRONZE-DOORS`; `SET-AQM-CONCLAVE-INTERIOR`; `SET-AQM-SPEAKERS-DAIS`; `SET-AQM-HIGH-SOVEREIGN-SEAT` |
| Date / Time Status | Approximate |
| Date | 2 Hearthwake |
| Weekday | Stonewake |
| Time / Hour | Hour TBD after Hour of the Star-Siren |
| Time Certainty | TBD |
| Beacon State | Blue active |
| Visible Header Metadata | Chapter-level unless visible subchapters are used |
| Scene IDs | B01-S060; B01-S061 |
| Cast | Addie; Mae; Dovren / High Sovereign presence; Overseer; Conclave figures; Major Tallandra / escort as applicable |
| Continuity State In | Addie has arrived at the Conclave / Seat of the 72 under blue-beacon pressure. |
| Continuity State Out | Addie has been forced into the roster / institutional machinery that leads directly into the mirror sequence. |
```

## `drafts/01_07_the_first_mirror.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Needs source/structure review before final insertion |
| Intended Output | Narrative prose chapter / metaphysical mirror sequence |
| Compile Slot | B01.070 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_07_the_first_mirror.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_07_the_first_mirror.md`; `drafts/01_07_the_first_mirror_expanded_council_beats.md`; `drafts/visions/01_02.md`; `drafts/01_07_return_to_witness_space_parse.md` |
| Optional Attachments | `drafts/01_07_second_mirror_parse.md` for source comparison only; `scratchpad/14_09_the_unwound_core_beats.md`; `drafts/14_09_second_vision_parse.md`; `drafts/14_09_second_vision_name_corrections.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/11_ARCHITECT_EXODUS_COMPROMISES.md`; `canon/12_HANS_FILE_NOEL_EXILE.md`; `canon/13_ARCHITECT_WITNESS_CHARACTER_INDEX.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Metaphysical + Historical / Vision + Specific return layer |
| Location Display | Mirror seam; wrong-sky council chamber; half-built Aquila Matara throne room; Witness space; Aquila Matara Conclave return |
| City-State / Region | Metaphysical / historical vision layer; Aquila Matara active layer |
| City | No ordinary city during mirror layers; Aquila Matara on return |
| District / Section / Quarter | N/A for mirror layers; Conclave / civic route on return |
| Specific Setting / Site | Grey seam; First Mirror council chamber; Second Mirror throne room; Witness space; Conclave bronze doors; Aquila Matara plaza / Mae estate gate |
| Settings Used | `SET-MIRROR-SEAM`; `SET-MIRROR-COUNCIL`; `SET-MIRROR-AQM-THRONE`; `SET-WITNESS-VOID`; `SET-AQM-CONCLAVE-BRONZE-DOORS`; `SET-AQM-PLAZA`; `SET-AQM-MAE-GATE` |
| Date / Time Status | Date/Time Withheld / subjective |
| Date | Time unknown in metaphysical layer; main timeline is 2 Hearthwake |
| Weekday | Time unknown in metaphysical layer; main timeline is Stonewake |
| Time / Hour | Time unknown / subjective mirror time |
| Time Certainty | Withheld / not applicable |
| Beacon State | Blue active in main timeline; not visible in metaphysical layers unless return scene shows it |
| Visible Header Metadata | Subchapter-level required if generated as one chapter; each mirror/return layer differs |
| Scene IDs | B01-S070 through B01-S076 proposed / existing range |
| Cast | Addie; Silence; Horror/Regret; first mirror council figures; Dovren; Geoffrik Vayne; Overseer; Rhün; Mae offstage at end |
| Continuity State In | Addie is pulled out of ordinary Conclave time into the mirror sequence after the roster/institutional pressure. |
| Continuity State Out | Addie returns to ordinary time with Horror's three-thread riddle and goes toward Mae's Aquila Matara estate. |
```

---

# Proposed Full Headers For Current Active Cleanup Set: `01_14`–`01_17`

## `drafts/01_14_the_law_telling_us_to_forget.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Cleaned L4; needs hour pass before prompt-ready |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.140 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_14_the_law_telling_us_to_forget.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_14_the_law_telling_us_to_forget.md`; `locales/images/analysis/LUM.analysis.json` |
| Optional Attachments | `drafts/PACKET_HEADER_PROPOSALS_BOOK01.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific / route |
| Location Display | Luminthalas, Section 5 Portalport to Section 1 White Tower Archives |
| City-State / Region | Ascentia / Luminthalas region |
| City | Luminthalas |
| District / Section / Quarter | Section 5 to Section 1 |
| Specific Setting / Site | Luminthalas Portalport; White Tower Archives |
| Settings Used | `SET-LUM-PORTALPORT`; `SET-LUM-WHITE-TOWER-ARCHIVES` |
| Date / Time Status | Approximate |
| Date | 6 Hearthwake |
| Weekday | Eldrane |
| Time / Hour | Hour TBD |
| Time Certainty | TBD |
| Beacon State | Green at start; yellow transition by end |
| Visible Header Metadata | Subchapter-level preferred; chapter-level fallback |
| Scene IDs | B01-S140 proposed |
| Cast | Addie; Mae; Carrio; Brynn; Gregory; Brickett; Rhün; Matthieu; Yurislav; Major Tallandra; elder High Elven reference scholar; Luminthalas civilians and archive staff |
| Continuity State In | Two offscreen research days have narrowed the thread candidates to Norns, Red Thread, and Ariadne; the group returns to Luminthalas to ask a better founding-history question. |
| Continuity State Out | Yellow beacon activates; the companions leave the White Tower together to meet the Witnesses. |
```

## `drafts/01_15_the_cities_that_disobeyed.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Cleaned L4 with standalone vision inserts; needs hour pass before prompt-ready |
| Intended Output | Narrative prose chapter with inserted vision sequences |
| Compile Slot | B01.150 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_15_the_cities_that_disobeyed.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_15_the_cities_that_disobeyed.md`; `drafts/visions/01_03.md`; `drafts/visions/01_04.md` |
| Optional Attachments | `canon/19_CITY_STATE_FOUNDING_TRIADS.md`; `canon/20_CITY_ALLEGIANCES.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/19_CITY_STATE_FOUNDING_TRIADS.md`; `canon/20_CITY_ALLEGIANCES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Metaphysical + Historical / Vision + Specific |
| Location Display | Luminthalas beacon / Witness sequence; historical evacuation port; First Dovren civic ceremony; return route toward Mae's Aquila Matara estate |
| City-State / Region | Luminthalas active layer; historical Earth / Dovren vision layers; Aquila Matara return layer |
| City | Luminthalas / Aquila Matara / historical vision spaces |
| District / Section / Quarter | TBD |
| Specific Setting / Site | Yellow Witness transition; José evacuation site; Dovren civic ceremony; Mae estate route |
| Settings Used | `SET-WITNESS-VOID` or yellow Witness space TBD; historical vision setting IDs TBD; `SET-AQM-MAE-ESTATE` for ending route |
| Date / Time Status | Approximate |
| Date | 6 Hearthwake |
| Weekday | Eldrane |
| Time / Hour | Hour TBD |
| Time Certainty | TBD |
| Beacon State | Yellow active |
| Visible Header Metadata | Subchapter-level preferred because active layer and vision layers differ |
| Scene IDs | B01-S150 proposed |
| Cast | Full companion group; José Mateo Navarro; Dovren I / First Dovren; obedient representatives; early Van'Kareth figure |
| Continuity State In | Yellow beacon has just activated in Luminthalas after Addie identifies Ariadne's Thread as the preserved story guiding them out. |
| Continuity State Out | The companions are shaken by the José wave vision and Dovren civic-punishment vision and return toward Mae's estate for controlled debrief. |
```

## `drafts/01_16_rapid_acceptance.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Cleaned L4; needs hour pass before prompt-ready |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.160 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_16_rapid_acceptance.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_16_rapid_acceptance.md` |
| Optional Attachments | `drafts/visions/01_03.md`; `drafts/visions/01_04.md` for reference only, not reinsertion |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific |
| Location Display | Aquila Matara, Mae's Estate, Back Porch |
| City-State / Region | Erzengel / Aquila Matara capital layer |
| City | Aquila Matara |
| District / Section / Quarter | Mae's estate |
| Specific Setting / Site | Back porch / terrace |
| Settings Used | `SET-AQM-MAE-ESTATE`; `SET-AQM-MAE-FAMILY-ROOM`; `SET-AQM-MAE-BACK-PORCH` |
| Date / Time Status | Approximate |
| Date | 6 Hearthwake |
| Weekday | Eldrane |
| Time / Hour | Hour TBD; evening/night mood |
| Time Certainty | TBD |
| Beacon State | Yellow active |
| Visible Header Metadata | Chapter-level unless visible subchapters are used |
| Scene IDs | B01-S160 proposed |
| Cast | Addie; Mae; Carrio; Brynn; Gregory; Brickett; Rhün; Matthieu; Yurislav; Major Tallandra; Tikket |
| Continuity State In | The group has returned from the yellow Witness visions and is too shaken to speak. |
| Continuity State Out | The group identifies the dam as the actionable thread and plans a Jadefall River city search; Yurislav names their survival logic as “Rapid acceptance.” |
```

## `drafts/01_17_children_of_the_damned.md`

```md
## Generation Packet Header

| Field | Value |
|---|---|
| Status | Cleaned L4; needs hour pass before prompt-ready |
| Intended Output | Narrative prose chapter |
| Compile Slot | B01.170 |
| Parent File | `canon/10_BOOK01_CHAPTER_OUTLINES.md` |
| Primary Draft File | `drafts/01_17_children_of_the_damned.md` |
| Required Attachments | `claude.md`; `canon/05_CHARACTERS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md`; `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/10_BOOK01_CHAPTER_OUTLINES.md`; `canon/12_BOOK01_CALENDAR_TIMELINE.md`; `drafts/01_17_children_of_the_damned.md`; `locales/images/analysis/PFN.analysis.json` |
| Optional Attachments | `drafts/PACKET_HEADER_PROPOSALS_BOOK01.md` |
| Required Canon | `canon/PROMPT_SUPPORT_CANON_LOCKS.md`; `canon/15_SETTINGS.md`; `canon/16_SCENES.md`; `canon/21_TIME_AND_HEADER_METADATA.md` |
| Location Status | Specific / route |
| Location Display | Aquila Matara, Mae's Estate; Pollyr Fen, Temple Wetland Quarter; Drowned Swamp-Church of Bountiful |
| City-State / Region | Aquila Matara capital layer; Hellgate River-Mire / Pollyr Fen layer |
| City | Aquila Matara; Pollyr Fen |
| District / Section / Quarter | Mae's estate; Pollyr Fen temple wetland quarter; outer wetland / swamp-church route |
| Specific Setting / Site | Mae estate breakfast room; Pollyr Fen Portalport; temple wetland quarter; Drowned Swamp-Church; calcified-young graveyard |
| Settings Used | `SET-AQM-MAE-ESTATE`; `SET-AQM-MAE-DINING`; `SET-AQM-MAE-KITCHEN`; `SET-PFN`; `SET-PFN-PORTALPORT`; `SET-PFN-TEMPLE-WETLAND-QUARTER`; `SET-PFN-SWAMP-CHURCH`; `SET-PFN-CALCIFIED-YOUNG-GRAVEYARD` |
| Date / Time Status | Approximate / multiple time blocks |
| Date | 14 Hearthwake |
| Weekday | Eldrane |
| Time / Hour | Hour TBD; begins at breakfast and runs through dusk/evening |
| Time Certainty | TBD |
| Beacon State | Green? / checkpoint turns Orange by end; confirm pre-orange beacon state |
| Visible Header Metadata | Subchapter-level preferred because the chapter changes city, location, and time block |
| Scene IDs | B01-S170 proposed |
| Cast | Addie; Mae; Carrio; Brynn; Gregory; Brickett; Rhün; Matthieu; Yurislav; Major Tallandra; Max; Tikket; Barnaby; Brother Tallowmire G. Reedfen; Pollyr Fen guards/family/worshippers |
| Continuity State In | After eight more days of failed searching, the companions are exhausted and still have not found the dam's actionable truth. |
| Continuity State Out | Orange checkpoint triggers; Brother Tallowmire / Pollyr Fen receives Van'Kareth South Aurreth Shipping Co.; Carrio and Mae offer protection; Brickett names the company Children of the Damned. |
```

---

# Open Review Questions Before Insertion

1. `01_04`: confirm whether the blue transition happens within `01_04` or exactly at the opening of `01_05`. Current proposal treats it as purple at `01_04` start and blue active at `01_05` start.
2. `01_04`: should we add `SET-SPK-GUILD-ACADEMIC-DISTRICT` to `canon/15_SETTINGS.md` now, or use the existing Guildhall / Kwame office settings only?
3. `01_05`: confirm that “Section 3” language for Aquila Matara should become a formal district/section setting or remain descriptive as the government / Seat of Power route.
4. `01_06`: lock the actual hour if known, or leave as `Hour TBD after Hour of the Star-Siren`.
5. `01_07`: confirm whether this stays a parent packet or whether the final generation packet should assemble from the movement files plus standalone `drafts/visions/01_02.md`.
6. `01_17`: confirm pre-orange beacon state at chapter start. Current proposal leaves it as `Green? / checkpoint turns Orange by end` because the color between yellow and orange needs a final continuity choice.
7. For generated prose, confirm whether beacon state should be visible in the prose header or remain packet/scene metadata only.
