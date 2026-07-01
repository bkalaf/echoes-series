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
| `01_00_prologue.md` | Prologue — The Mother Who Started the War | B01.000 | Locked for header insertion | Specific | `Yearsend 29, Kindlemask`; Hour of the Gargoyle | None / blank | B01-S000 | Header may simply use the Brickett/Mother slums perspective; no need to split the Dear Reader frame unless prose later demands it. |
| `01_01_the_royal_astronomers_tower.md` | The Royal Astronomer’s Tower | B01.010 | Locked for header insertion | Specific | `Hearthwake 1, Dravenkar`; Hour of the Dew-Stalker | Purple activation during chapter | B01-S010; B01-S011 | Royal Observatory / Stormspire Aerie / Vharos sightline. |
| `01_02_the_nomination.md` | The Nomination | B01.020 | Locked for header insertion | Specific / route | `Hearthwake 1, Dravenkar`; Hour of the Star-Siren | None / blank per current review | B01-S020; B01-S021 | Starts at 6:00 PM in Skyrend Peak hotel / Gale Exposition route; moves toward Guildhall nomination. |
| `01_03_the_witnesses.md` | The Witnesses | B01.030 | Locked for header insertion | Metaphysical | Time unknown / subjective | Purple active in main timeline, not visible in scene | B01-S030 | Location display: The scene between stories. |
| `01_04_the_weight_of_the_beacon.md` | The Weight of the Beacon | B01.040 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 2, Stonewake`; starts Hour of the Bishop; route through Sphinx / Singularity toward Star-Siren | Purple at start; blue transition by end / into `01_05` | B01-S040; B01-S041; B01-S042 | Starts in Skyrend Peak academic-guild district / Meridian Accord Guildhall; moves through vertical route, brick-incident ramp, pawn-shop refuge, and post-pawn secure route. |
| `01_05_the_core_of_the_conjunction.md` | The Core of the Conjunction | B01.050 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 2, Stonewake`; Hour of the Star-Siren at start | Blue just changed / blue active | B01-S050; B01-S051; B01-S052 | Starts in Skyrend Peak secure portal route and ends in Aquila Matara government / Seat of the 72 route. |
| `01_06_the_weight_of_the_roster.md` | The Weight of the Roster | B01.060 | Locked location; needs hour pass | Specific | `Hearthwake 2, Stonewake`; Hour TBD after Star-Siren | Blue active | B01-S060; B01-S061 | Entire chapter inside the Seat of the 72 / Conclave High Assembly in Aquila Matara. |
| `01_07_the_first_mirror.md` | The First Mirror | B01.070 | Needs source/structure review | Metaphysical + Historical / Vision + Specific return layer | Time unknown / subjective mirror time | Blue active in main timeline; not visible in metaphysical layers | B01-S070 through B01-S076 | Parent outline; should reference standalone `drafts/visions/01_02.md` for Second Mirror where possible. |
| `01_08_the_weight_of_being_asked.md` | The Weight of Being Asked | B01.080 | Locked for header insertion; subchapter metadata useful | Specific / route | `Hearthwake 2, Stonewake`; Hour of the Pack-Runner | Blue active | B01-S080; B01-S081; B01-S082 | Starts at the Seat of the 72 / Conclave return layer after Addie was gone about two hours; moves to Mae's Manor in Aquila Matara Section 3. |
| `01_09_day_one_architecture.md` | Day One Architecture | B01.090 | Partial lock / needs draft alignment | Specific | `Hearthwake 3, Aegalor`; proposed chapter start Hour of the Griffin; existing draft currently labels Subchapter 1 as Hour of the Wyrm and says Addie exits bath near Hour of Iron Foundry | Blue active at start; green approaching | B01-S090; B01-S091; B01-S092 | Same Aquila Matara / Mae's Manor location. Need align draft title/beat if Griffin replaces Wyrm. |
| `01_10_holes_in_the_wall.md` | Holes in the Wall | B01.100 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 3, Aegalor`; depart Mae's Manor around Hour of the Aurora or Iron Foundry; Team Three reaches lower Luminthalas around Hour of the Chieftain / High Market after travel | Blue active; green approaching by end | B01-S100 through B01-S104 | Starts at Mae's Manor / Aquila Matara terminal route; splits teams to Luminthalas and Aes Sidhal. The three-hour restaurant line belongs here, not `01_11`. |
| `01_11_the_bountiful_harvest.md` | The Bountiful Harvest | B01.110 | Locked enough for header insertion after subchapter check | Specific | `Hearthwake 3, Aegalor`; after three-hour line/standoff; less than one hour before green phase; likely Hour of the Singularity | Blue active; green imminent / transition pressure | B01-S110 | Starts after Addie's white lunar-light flare at The Bountiful Harvest. This chapter resolves Brynn's scroll before portal-grid shutdown pressure. |
| `01_12_the_unwound_core.md` | The Unwound Core | B01.120 | Locked for header insertion | Specific | `Hearthwake 3, Aegalor`; Hour of the Waxing Crescent | Green active | B01-S120 | Back at Mae's Manor / high-fire family room in Aquila Matara Section 3. Use Mae's Manor wording, not Companion/Companions' Estate yet. |
| `01_13_the_thread_back_out.md` | The Thread Back Out | B01.130 | Locked for header insertion | Specific | `Hearthwake 3, Aegalor`; Hour of the Courier | Green active | B01-S130 | Same Mae's Manor family-room sequence; Barnaby / Ariadne / comma-riddle chapter. |
| `01_14_the_law_telling_us_to_forget.md` | The Law Telling Us To Forget | B01.140 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 6, Eldrane`; Day Four / hour TBD | Green at start; yellow transition by end | B01-S140 proposed | Luminthalas Section 5 Portalport to Section 1 White Tower Archives. Requires `locales/images/analysis/LUM.analysis.json`. |
| `01_15_the_cities_that_disobeyed.md` | The Cities That Disobeyed | B01.150 | Ready for header insertion after review; needs hour pass | Metaphysical + Historical / Vision + Specific | `Hearthwake 6, Eldrane`; yellow beacon / hour TBD | Yellow active | B01-S150 proposed | Uses standalone `drafts/visions/01_03.md` and `drafts/visions/01_04.md`. This is where Mae's “our manor” shift happens; do not call it the companions' place before this point. |
| `01_16_rapid_acceptance.md` | Rapid Acceptance | B01.160 | Ready for header insertion after review; needs hour pass | Specific | `Hearthwake 6, Eldrane`; evening/night / hour TBD | Yellow active | B01-S160 proposed | Mae estate back porch / protected legal debrief with Tikket. After `01_15`, “our manor” / shared operational household language is allowed when context supports it. |
| `01_17_children_of_the_damned.md` | Children of the Damned | B01.170 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 14, Eldrane`; Conjunction Day Twelve / multiple hours TBD | Green? / checkpoint turns Orange by end; confirm pre-orange beacon state | B01-S170 proposed | Mae estate to Pollyr Fen; requires `locales/images/analysis/PFN.analysis.json`. Formal company name: `Van'Kareth South Aurreth Shipping Co.` |

---

# Current Chapter-Level Outstanding Items

| Draft | Needed Decision |
|---|---|
| `01_06_the_weight_of_the_roster.md` | Exact hour after Star-Siren, if known. |
| `01_07_the_first_mirror.md` | Keep as one parent packet, or assemble from subfiles / standalone vision inserts? |
| `01_09_day_one_architecture.md` | Confirm whether to change the existing Subchapter 1 lock from Hour of the Wyrm to Hour of the Griffin. The current draft explicitly uses “The Hour of the Wyrm.” |
| `01_10_holes_in_the_wall.md` | Confirm whether departure from Mae's Manor is Hour of the Aurora or Hour of the Iron Foundry. The current file makes the day operational but does not lock the start hour in the header. |
| `01_14_the_law_telling_us_to_forget.md` | Start hour / rough duration. |
| `01_15_the_cities_that_disobeyed.md` | Hour handling for yellow Witness / vision sequence. |
| `01_16_rapid_acceptance.md` | Exact evening/night hour for porch debrief. |
| `01_17_children_of_the_damned.md` | Start hour, pre-orange beacon state, and rough time blocks. |

---

# Naming / Location Wording Lock

Use **Mae's Manor** / **Mae's Aquila Matara estate** for chapters before the “our manor” shift in `01_15_the_cities_that_disobeyed.md`.

Do not use **Companion's Estate**, **Companions' Estate**, or similar shared-place language before Mae's accidental pronoun shift in `01_15`.

After `01_15`, shared-household language is allowed when the scene context supports it, but the formal setting ID remains `SET-AQM-MAE-ESTATE` unless the setting registry is intentionally renamed later.

---

# Skyrend Peak Location Notes From Analysis

Skyrend Peak is a vertical raptorfolk fortress-civilization where height, wind, watchfulness, signal towers, cliff platforms, and defensive civic architecture are the grammar of daily life.

Useful location logic for early chapters:

- Poor / slum spaces should still feel vertical: sheltered lower ledges, stacked dwellings, windbreaks, service cuts, rotting tower interiors, and unsafe routes beneath official terraces.
- Hotels / inns fit the analysis as high-altitude inns, wind-sheltered balconies, tower bases, or ledge plazas near the Gale Exposition / transit route.
- The Meridian Accord Guildhall can sit in a guild / academic / civic-service district near formal tower infrastructure rather than a generic business district.
- The Royal Observatory and Stormspire Aerie sit naturally in the city's watch/signal/beacon identity.

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
- `SET-SPK-GUILD-ACADEMIC-DISTRICT`
- `SET-SPK-GUILD-ELEVATOR`
- `SET-SPK-GUILD-LOBBY`
- `SET-SPK-GUILD-TO-PAWN-RAMP`
- `SET-SPK-BRICK-INCIDENT-RAMP`
- `SET-SPK-PUBLIC-STREETS`
- `SET-SPK-PAWN-SHOP`
- `SET-SPK-POST-PAWN-SECURE-ROUTE`
- `SET-SPK-SECURE-PORTAL`

---

# Source Verification Notes From Current Drafts

## `01_08`

Current parse confirms this is one continuous evening inside Mae's estate after the mirror sequence and before `01_09`.

It does not currently expose the “gone two hours” line in the parsed outline, but `01_07_return_to_witness_space_parse.md` confirms the return movement from Witness space back to Conclave and then toward Mae's estate.

## `01_09`

Current parse explicitly names visible subchapter 1 as **The Hour of the Wyrm**, says Addie slept only about three and a half hours, and says she steps out of the bath area near **Hour of the Iron Foundry**.

If the intended lock is **Hour of the Griffin** for Addie crawling out of bed, the chapter draft should be updated to align the visible subchapter heading and opening beats.

## `01_10` and `01_11`

Current parse says `01_10` is Day One after breakfast/departure, with the green beacon approaching and the group within roughly an hour of green phase by the end.

Current parse says `01_11` starts immediately after `01_10`, less than one hour before green phase / portal-grid shutdown pressure.

Therefore, the three-hour line/wait belongs structurally in `01_10`, while `01_11` resolves the post-flare Brynn scroll acceptance and movement out.

## `01_12` and `01_13`

Current parses place both chapters at Mae's Aquila Matara estate / high-fire family room during the green phase.

Use Mae's Manor wording through these chapters.
