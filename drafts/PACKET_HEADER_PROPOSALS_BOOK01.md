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

# Prose Timing Verification Pass

This pass prioritizes the current draft prose / parsed prose over earlier memory-based estimates.

Key verified correction:

- `01_05_the_core_of_the_conjunction.md` says Addie asks the time in the pawn shop, Rennick answers **Hour of the Sphinx, probably on the way to Singularity**, and the blue-beacon scroll deployment begins at the **first chime of Singularity**. Therefore the blue beacon transition belongs to **Hour of the Singularity**, not Hour of the Star-Siren.
- Since blue is the 24-hour warning, green should align to the same hour marker on Hearthwake 3 unless later prose explicitly contradicts it. Current header proposals therefore treat **Hour of the Singularity** as the likely green transition marker too.
- `01_02_the_nomination.md` currently states Addie exits Portalport at **Hour of the Singularity** and then sees the purple beacon already burning. The chapter header should not say Hour of the Star-Siren.
- `01_09_day_one_architecture.md` currently names Subchapter 1 **The Hour of the Wyrm** and says Addie steps out of the bath near **Hour of the Iron Foundry**. The header should follow that unless the chapter prose is intentionally revised later.

---

# Proposed Chapter Packet Summary

| Draft | Title | Compile Slot | Header Status | Location Status | Date / Time Status | Beacon State | Scene IDs | Notes |
|---|---|---|---|---|---|---|---|---|
| `01_00_prologue.md` | Prologue — The Mother Who Started the War | B01.000 | Locked for header insertion | Specific | `Yearsend 29, Kindlemask`; Hour of the Gargoyle | None / blank | B01-S000 | Header may simply use the Brickett/Mother slums perspective; no need to split the Dear Reader frame unless prose later demands it. |
| `01_01_the_royal_astronomers_tower.md` | The Royal Astronomer’s Tower | B01.010 | Needs time pass after prose verification | Specific | `Hearthwake 1, Dravenkar`; exact hour not stated in current parse; likely Hour of the Singularity if purple follows the same beacon-change marker as blue/green | Purple activation during chapter | B01-S010; B01-S011 | Royal Observatory / Stormspire Aerie / Vharos sightline. Previous Dew-Stalker lock is not visible in current parsed prose. |
| `01_02_the_nomination.md` | The Nomination | B01.020 | Locked to prose; subchapter metadata useful | Specific / route | `Hearthwake 1, Dravenkar`; starts Hour of the Singularity | Purple active / visible | B01-S020; B01-S021 | Starts in Skyrend Peak Portalport / Gale Exposition route at Hour of the Singularity; moves through hotel and Guildhall nomination. |
| `01_03_the_witnesses.md` | The Witnesses | B01.030 | Locked for header insertion | Metaphysical | Time unknown / subjective | Purple active in main timeline, not visible in scene | B01-S030 | Location display: The scene between stories. |
| `01_04_the_weight_of_the_beacon.md` | The Weight of the Beacon | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 2, Stonewake`; starts near High Market / high noon confinement; extraction reaches Hour of the Bishop; continues toward pawn-shop refuge | Purple active; blue-beacon deadline pending / imminent | B01-S040; B01-S041; B01-S042 | Starts in Skyrend Peak academic-guild district / Meridian Accord Guildhall; moves through vertical route, brick-incident ramp, pawn-shop refuge. Blue does not visibly transition here based on current `01_05` timing. |
| `01_05_the_core_of_the_conjunction.md` | The Core of the Conjunction | B01.050 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 2, Stonewake`; starts Hour of the Sphinx; blue changes at Hour of the Singularity | Purple at start; blue transition at Singularity; blue active afterward | B01-S050; B01-S051; B01-S052 | Starts in the Skyrend Peak pawn-shop aftermath, reaches public scroll deployment at Singularity, then moves through secure portal route to Aquila Matara government / Seat of the 72 route. |
| `01_06_the_weight_of_the_roster.md` | The Weight of the Roster | B01.060 | Locked location; needs hour pass | Specific | `Hearthwake 2, Stonewake`; after blue transition, likely evening after Hour of the Singularity / before mirror removal | Blue active | B01-S060; B01-S061 | Entire chapter inside the Seat of the 72 / Conclave High Assembly in Aquila Matara. |
| `01_07_the_first_mirror.md` | The First Mirror | B01.070 | Needs source/structure review | Metaphysical + Historical / Vision + Specific return layer | Time unknown / subjective mirror time; main timeline Stonewake evening/night | Blue active in main timeline; not visible in metaphysical layers | B01-S070 through B01-S076 | Parent outline; should reference standalone `drafts/visions/01_02.md` for Second Mirror where possible. |
| `01_08_the_weight_of_being_asked.md` | The Weight of Being Asked | B01.080 | Locked for header insertion; subchapter metadata useful | Specific / route | `Hearthwake 2, Stonewake`; Hour of the Pack-Runner | Blue active | B01-S080; B01-S081; B01-S082 | Starts at the Seat of the 72 / Conclave return layer after Addie was gone about two hours; moves to Mae's Manor in Aquila Matara Section 3. |
| `01_09_day_one_architecture.md` | Day One Architecture | B01.090 | Locked to current parsed prose; subchapter metadata useful | Specific | `Hearthwake 3, Aegalor`; starts Hour of the Wyrm; Addie exits bath near Hour of the Iron Foundry | Blue active at start; green approaching | B01-S090; B01-S091; B01-S092 | Same Aquila Matara / Mae's Manor location. Do not replace Wyrm with Griffin unless the chapter prose is intentionally revised. |
| `01_10_holes_in_the_wall.md` | Holes in the Wall | B01.100 | Partial lock / needs subchapter breakdown | Specific / route | `Hearthwake 3, Aegalor`; morning departure from Mae's Manor; lower Luminthalas line sequence runs toward Hour of the Sphinx / less than one hour before green | Blue active; green approaching by end | B01-S100 through B01-S104 | Starts at Mae's Manor / Aquila Matara terminal route; splits teams to Luminthalas and Aes Sidhal. The three-hour restaurant line belongs here, not `01_11`. |
| `01_11_the_bountiful_harvest.md` | The Bountiful Harvest | B01.110 | Locked enough for header insertion after subchapter check | Specific | `Hearthwake 3, Aegalor`; immediately after white flare; less than one hour before green phase; likely late Sphinx / pre-Singularity | Blue active; green imminent / transition pressure | B01-S110 | Starts after Addie's white lunar-light flare at The Bountiful Harvest. This chapter resolves Brynn's scroll before portal-grid shutdown pressure. |
| `01_12_the_unwound_core.md` | The Unwound Core | B01.120 | Locked for header insertion | Specific | `Hearthwake 3, Aegalor`; after green transition; Hour of the Waxing Crescent | Green active | B01-S120 | Back at Mae's Manor / high-fire family room in Aquila Matara Section 3. Use Mae's Manor wording, not Companion/Companions' Estate yet. |
| `01_13_the_thread_back_out.md` | The Thread Back Out | B01.130 | Locked for header insertion | Specific | `Hearthwake 3, Aegalor`; Hour of the Courier | Green active | B01-S130 | Same Mae's Manor family-room sequence; Barnaby / Ariadne / comma-riddle chapter. |
| `01_14_the_law_telling_us_to_forget.md` | The Law Telling Us To Forget | B01.140 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 6, Eldrane`; Day Four / hour TBD | Green at start; yellow transition by end | B01-S140 proposed | Luminthalas Section 5 Portalport to Section 1 White Tower Archives. Requires `locales/images/analysis/LUM.analysis.json`. |
| `01_15_the_cities_that_disobeyed.md` | The Cities That Disobeyed | B01.150 | Ready for header insertion after review; needs hour pass | Metaphysical + Historical / Vision + Specific | `Hearthwake 6, Eldrane`; yellow beacon / hour TBD | Yellow active | B01-S150 proposed | Uses standalone `drafts/visions/01_03.md` and `drafts/visions/01_04.md`. This is where Mae's “our manor” shift happens; do not call it the companions' place before this point. |
| `01_16_rapid_acceptance.md` | Rapid Acceptance | B01.160 | Ready for header insertion after review; needs hour pass | Specific | `Hearthwake 6, Eldrane`; evening/night / hour TBD | Yellow active | B01-S160 proposed | Mae estate back porch / protected legal debrief with Tikket. After `01_15`, “our manor” / shared operational household language is allowed when context supports it. |
| `01_17_children_of_the_damned.md` | Children of the Damned | B01.170 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 14, Eldrane`; Conjunction Day Twelve / multiple hours TBD | Green? / checkpoint turns Orange by end; confirm pre-orange beacon state | B01-S170 proposed | Mae estate to Pollyr Fen; requires `locales/images/analysis/PFN.analysis.json`. Formal company name: `Van'Kareth South Aurreth Shipping Co.` |

---

# Current Chapter-Level Outstanding Items

| Draft | Needed Decision |
|---|---|
| `01_01_the_royal_astronomers_tower.md` | Current parsed prose does not expose an exact hour. If purple aligns with the blue/green marker, use Hour of the Singularity; if there is another source for Dew-Stalker, attach/record it before locking. |
| `01_06_the_weight_of_the_roster.md` | Exact hour after blue/Singularity, if known. |
| `01_07_the_first_mirror.md` | Keep as one parent packet, or assemble from subfiles / standalone vision inserts? |
| `01_10_holes_in_the_wall.md` | Subchapter time route: departure from Mae's Manor, terminal split, lower Luminthalas arrival, three-hour line, white flare before Singularity. |
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

## `01_02`

Current parse says the opening Portalport / Gale Exposition movement establishes **Hour of the Singularity** and the final segment of old/legacy Brindlemask language. Use the current Book 1 calendar date but preserve the prose-timing clue as the hour source.

## `01_04` and `01_05`

Current `01_04` parse says Addie notices it is close to high noon, then Boss names **Hour of the Bishop** during extraction. The chapter ends in the pawn-shop proof sequence without the visible blue transition.

Current `01_05` parse gives the decisive timing:

1. Addie asks the time in the pawn shop.
2. Rennick answers **Hour of the Sphinx, probably on the way to Singularity**.
3. At the first chime of **Singularity**, the ground trembles, scrolls appear, and the blue-beacon operational rule reveal begins.

Therefore, the header sequence should be:

- `01_04`: purple active / blue pending.
- `01_05`: Sphinx at start, blue transition at Singularity, blue active afterward.

## `01_09`

Current parse explicitly names visible subchapter 1 as **The Hour of the Wyrm**, says Addie slept only about three and a half hours, and says she steps out of the bath area near **Hour of the Iron Foundry**.

Do not change the header to Griffin unless the chapter prose is intentionally revised.

## `01_10` and `01_11`

Current parse says `01_10` is Day One after breakfast/departure, with the green beacon approaching and the group within roughly an hour of green phase by the end.

Current parse says `01_11` starts immediately after `01_10`, less than one hour before green phase / portal-grid shutdown pressure.

Therefore, the three-hour line/wait belongs structurally in `01_10`, while `01_11` resolves the post-flare Brynn scroll acceptance and movement out.

If green follows the same marker established by the blue-beacon transition, it should become active at **Hour of the Singularity** on Hearthwake 3.

## `01_12` and `01_13`

Current parses place both chapters at Mae's Aquila Matara estate / high-fire family room during the green phase.

Use Mae's Manor wording through these chapters.
