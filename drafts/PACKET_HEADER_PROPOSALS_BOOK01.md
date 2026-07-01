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

## Time Handling Note

Most existing chapter drafts predate the new time/header metadata standard. Where an exact hour is not already locked, use `Hour TBD` and mark `Time Certainty` as `TBD` or `Approximate`. Do not invent exact hours during packet insertion.

---

# Status Key

| Status | Meaning |
|---|---|
| Ready for header insertion after review | The proposed packet fields are strong enough to insert after user confirmation. |
| Needs time pass | Chapter placement is clear, but exact hour/subchapter timing still needs cleanup. |
| Needs source/structure review | The file is a parent/support file or older parse that needs more careful cleanup before packet insertion. |

---

# Proposed Chapter Packet Summary

| Draft | Title | Compile Slot | Header Status | Location Status | Date / Time Status | Scene IDs | Notes |
|---|---|---|---|---|---|---|---|
| `01_00_prologue.md` | Prologue — The Mother Who Started the War | B01.000 | Needs time pass | Specific + narrative frame | `Yearsend 29, Kindlemask`; hour TBD | B01-S000 | Mixed Dear Reader / Mother / Brickett frame; use subchapter-level metadata if visible subheaders exist. |
| `01_01_the_royal_astronomers_tower.md` | The Royal Astronomer’s Tower | B01.010 | Needs time pass | Specific | `Hearthwake 1, Dravenkar`; hour TBD | B01-S010; B01-S011 | Skyrend Peak observatory / Stormspire / Vharos sightline. |
| `01_02_the_nomination.md` | The Nomination | B01.020 | Needs time pass | Specific | `Hearthwake 1, Dravenkar`; night / hour TBD | B01-S020; B01-S021 | Qasr Siroth origin context plus Skyrend Peak Portalport / hotel / guildhall. |
| `01_03_the_witnesses.md` | The Witnesses | B01.030 | Needs time pass | Metaphysical | `Hearthwake 1, Dravenkar`; subjective / hour TBD | B01-S030 | Witness void; use `Metaphysical` location status. |
| `01_04_the_weight_of_the_beacon.md` | The Weight of the Beacon | B01.040 | Needs time pass | Specific | `Hearthwake 2, Stonewake`; hour TBD | B01-S040; B01-S041; B01-S042 | Skyrend Peak extraction / streets / pawn-shop refuge. |
| `01_05_the_core_of_the_conjunction.md` | The Core of the Conjunction | B01.050 | Needs time pass | Specific / route | `Hearthwake 2, Stonewake`; hour TBD | B01-S050; B01-S051; B01-S052 | Skyrend Peak to Aquila Matara transfer; Three Hundred Steps speech. |
| `01_06_the_weight_of_the_roster.md` | The Weight of the Roster | B01.060 | Needs time pass | Specific | `Hearthwake 2, Stonewake`; late day/evening / hour TBD | B01-S060; B01-S061 | Conclave roster / Addie institutionalization / Dovren and Overseer. |
| `01_07_the_first_mirror.md` | The First Mirror | B01.070 | Needs source/structure review | Metaphysical + Historical / Vision + Specific | `Hearthwake 2, Stonewake`; night / subjective mirror time / hour TBD | B01-S070 through B01-S076 | Parent outline; should reference standalone `drafts/visions/01_02.md` for Second Mirror where possible. |
| `01_08_the_weight_of_being_asked.md` | The Weight of Being Asked | B01.080 | Needs time pass | Specific | `Hearthwake 2, Stonewake`; late night / hour TBD | B01-S080; B01-S081; B01-S082 | Mae estate arrival / kitchen / dining / care structure. |
| `01_09_day_one_architecture.md` | Day One Architecture | B01.090 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; morning / hour TBD | B01-S090; B01-S091; B01-S092 | Mae estate morning / washroom / reporters / day-one launch. |
| `01_10_holes_in_the_wall.md` | Holes in the Wall | B01.100 | Needs time pass | Specific / route | `Hearthwake 3, Aegalor`; Day One / hour TBD | B01-S100 through B01-S104 | Team split across AQM, Luminthalas, and Aes Sidhal. |
| `01_11_the_bountiful_harvest.md` | The Bountiful Harvest | B01.110 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; Day One / hour TBD | B01-S110 | Luminthalas lower-quarter restaurant scene. |
| `01_12_the_unwound_core.md` | The Unwound Core | B01.120 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; green beacon active/activating / hour TBD | B01-S120 | Mae estate family-room synthesis and green-beacon pivot. |
| `01_13_the_thread_back_out.md` | The Thread Back Out | B01.130 | Needs time pass | Specific | `Hearthwake 3, Aegalor`; green phase active / hour TBD | B01-S130 | Ariadne / Barnaby / comma-riddle chapter. |
| `01_14_the_law_telling_us_to_forget.md` | The Law Telling Us To Forget | B01.140 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 6, Eldrane`; Day Four / hour TBD | B01-S140 proposed | Luminthalas Section 5 Portalport to Section 1 White Tower Archives. Requires `locales/images/analysis/LUM.analysis.json`. |
| `01_15_the_cities_that_disobeyed.md` | The Cities That Disobeyed | B01.150 | Ready for header insertion after review; needs hour pass | Metaphysical + Historical / Vision + Specific | `Hearthwake 6, Eldrane`; yellow beacon / hour TBD | B01-S150 proposed | Uses standalone `drafts/visions/01_03.md` and `drafts/visions/01_04.md`. |
| `01_16_rapid_acceptance.md` | Rapid Acceptance | B01.160 | Ready for header insertion after review; needs hour pass | Specific | `Hearthwake 6, Eldrane`; evening/night / hour TBD | B01-S160 proposed | Mae estate back porch / protected legal debrief with Tikket. |
| `01_17_children_of_the_damned.md` | Children of the Damned | B01.170 | Ready for header insertion after review; needs hour pass | Specific / route | `Hearthwake 14, Eldrane`; Conjunction Day Twelve / multiple hours TBD | B01-S170 proposed | Mae estate to Pollyr Fen; requires `locales/images/analysis/PFN.analysis.json`. Formal company name: `Van'Kareth South Aurreth Shipping Co.` |

---

# Proposed Full Headers For Current Active Cleanup Set

These are the first headers recommended for insertion because `01_14`–`01_17` are closest to current work.

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
| Visible Header Metadata | Subchapter-level preferred because the chapter changes city, location, and time block |
| Scene IDs | B01-S170 proposed |
| Cast | Addie; Mae; Carrio; Brynn; Gregory; Brickett; Rhün; Matthieu; Yurislav; Major Tallandra; Max; Tikket; Barnaby; Brother Tallowmire G. Reedfen; Pollyr Fen guards/family/worshippers |
| Continuity State In | After eight more days of failed searching, the companions are exhausted and still have not found the dam's actionable truth. |
| Continuity State Out | Orange checkpoint triggers; Brother Tallowmire / Pollyr Fen receives Van'Kareth South Aurreth Shipping Co.; Carrio and Mae offer protection; Brickett names the company Children of the Damned. |
```

---

# Open Review Questions Before Insertion

1. Should `01_00` use `No Date/Time` for the Dear Reader frame and `Yearsend 29, Kindlemask` only for the Brickett/Mother scene, or should the prologue header carry the Brickett scene date?
2. Should `01_03_the_witnesses.md` show main timeline date/time, or should the header say `Witness Space / Date-Time Withheld`?
3. Should `01_07_the_first_mirror.md` remain a parent chapter packet, or should generation use its movement files plus standalone `drafts/visions/01_02.md` instead?
4. Should `01_14`–`01_17` get proposed scene IDs `B01-S140`, `B01-S150`, `B01-S160`, and `B01-S170`, or should we reserve multi-row ranges before inserting headers?
5. Do you want visible subchapter metadata in the generated prose for `01_14`–`01_17`, or chapter-level metadata only until the prose pass breaks them into final sections?
