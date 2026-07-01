# Prompt Readiness Audit

Last audit pass: after creation of `AGENTS.md`, `claude.md`, `canon/21_TIME_AND_HEADER_METADATA.md`, and `canon/PROMPT_SUPPORT_CANON_LOCKS.md`.

This file records whether current draft files conform to the new prompt-packet standards.

---

# Standard Being Audited Against

A prompt-ready draft must include:

- a `## Generation Packet Header`;
- exact required attachments;
- required canon links;
- location metadata;
- date / time metadata or an explicit `No Date/Time` / `Date/Time Withheld` flag;
- setting IDs;
- scene IDs;
- cast;
- beat sequence;
- dialogue locks where applicable;
- ending state;
- no unresolved correction clutter inside the chapter prompt.

See:

- `AGENTS.md`
- `claude.md`
- `canon/21_TIME_AND_HEADER_METADATA.md`
- `canon/PROMPT_SUPPORT_CANON_LOCKS.md`

---

# Audit Summary

## Cleaned But Not Fully Prompt-Ready Yet

The following active Book 1 files have had obvious correction clutter removed or reduced, but still need full Generation Packet Headers and explicit location/date/hour metadata before they should be submitted as prompt-ready packets:

| File | Current Status | Notes |
|---|---|---|
| `drafts/01_14_the_law_telling_us_to_forget.md` | Cleaned L4 | Has required canon links and cleaned route/settings logic. Needs Generation Packet Header and location/time metadata table. |
| `drafts/01_15_the_cities_that_disobeyed.md` | Cleaned L4 with vision inserts | Uses standalone vision inserts `01_03` and `01_04`. Needs Generation Packet Header and location/time metadata table. |
| `drafts/01_16_rapid_acceptance.md` | Cleaned L4 | Back porch setting now indexed. Needs Generation Packet Header and location/time metadata table. |
| `drafts/01_17_children_of_the_damned.md` | Cleaned L4 | Company name updated to `Van'Kareth South Aurreth Shipping Co.`; Pollyr Fen settings indexed. Needs Generation Packet Header and location/time metadata table. |

## Not Yet Updated To New Standard

These files predate `AGENTS.md` and should be treated as parsed outlines / planning files, not prompt-ready packets, until a cleanup pass adds the new packet header and metadata:

| File / Group | Status | Needed Work |
|---|---|---|
| `drafts/01_00_prologue.md` through `drafts/01_13_the_thread_back_out.md` | Pre-standard parsed outlines | Add Generation Packet Header, required attachments, location metadata, time metadata, setting IDs, and clean any remaining correction notes. |
| `drafts/01_07_the_first_mirror.md` | Pre-standard parent outline | Move or centralize remaining Architect-name correction table; add packet header; clarify required attached subfiles. |
| `drafts/01_07_the_first_mirror_expanded_council_beats.md` | Pre-standard expanded insert | Move or centralize remaining Architect-name correction table; add packet header or mark as supporting insert. |
| `drafts/01_07_second_mirror_parse.md` | Pre-standard supporting parse | Consider replacing direct generation use with `drafts/visions/01_02.md` where possible. Add header if still used directly. |
| `drafts/01_07_return_to_witness_space_parse.md` | Pre-standard supporting parse | Add header if used directly; otherwise mark as support-only. |
| `drafts/01_07_first_mirror_name_corrections.md` | Correction/support file | Keep as support file or migrate into `canon/PROMPT_SUPPORT_CANON_LOCKS.md` / Book 14 name correction file. Do not submit as narrative prompt. |
| `drafts/14_09_second_vision_parse.md` | Strong planning file, not clean prompt packet | Good source material, but should be converted into a clean `drafts/prompts/...` packet before Claude generation. |
| `drafts/14_09_second_vision_name_corrections.md` | Correction/support file | Keep as support attachment unless promoted to canon. Do not submit as narrative prompt alone. |

## Standalone Vision Files

| File | Current Status | Needed Work |
|---|---|---|
| `drafts/visions/01_01.md` | Stub | Needs source / beats. |
| `drafts/visions/01_02.md` | Corrected extracted L4 | Needs Generation Packet Header and location/time status. |
| `drafts/visions/01_03.md` | Corrected extracted L4 | Needs Generation Packet Header and location/time status. |
| `drafts/visions/01_04.md` | Cleaned extracted L4 | Needs Generation Packet Header and location/time status. |
| `drafts/visions/01_05.md` | Drafted L4 | Needs Generation Packet Header and location/time status. |
| `drafts/visions/01_06.md` | Stub | Needs source / beats. |
| `drafts/visions/17_01.md` | Stub | Future stub; no generation readiness expected. |
| `drafts/visions/18_01.md` | Stub | Future stub; no generation readiness expected. |

## Interlude Files

| File / Group | Current Status | Needed Work |
|---|---|---|
| `drafts/interludes/01_interlude_the_choice_to_do_nothing.md` | Existing interlude draft | Needs explicit `No Location` / `No Date/Time` metadata if used as a prompt packet. |
| `drafts/interludes/02_interlude_the_doomsday_shelf.md` | Current Book 1 prose/interlude draft | Needs explicit `No Location` / `No Date/Time` metadata if used as a prompt packet. |
| `drafts/interludes/03_interlude_the_knots_and_the_nots.md` | Current Book 1 prose/interlude draft | Needs explicit `No Location` / `No Date/Time` metadata if used as a prompt packet. |
| `drafts/interludes/source_material/*` | Mixed quality | Several Book 2+ files are source cards only; do not use as complete prompt packets until source recovery is done. |

---

# Current Confidence

The repo is now cleaner, but the active drafts are **not yet all prompt-ready under the new standard**.

The immediate safe statement is:

- `01_14`–`01_17` have had first-pass correction clutter cleanup.
- `01_15` now correctly references standalone vision inserts.
- `01_17` now uses `Van'Kareth South Aurreth Shipping Co.` as the formal company name.
- The older active draft set still needs a formal packet-header migration pass.
- The Book 14 generation should use a clean derived prompt packet, not the raw parse file.

---

# Recommended Next Pass

1. Create `drafts/prompts/14_09_first_architect_meeting_prompt.md` as the first clean Claude packet.
2. Add Generation Packet Headers to `01_14`–`01_17` first because they are closest to current work.
3. Add location/time metadata tables to `01_14`–`01_17`.
4. Update `drafts/README.md`, `canon/10_BOOK01_CHAPTER_OUTLINES.md`, `canon/12_BOOK01_CALENDAR_TIMELINE.md`, and `canon/16_SCENES.md` for `01_14`–`01_17` and interludes 02/03.
5. Then migrate earlier `01_00`–`01_13` files in batches instead of trying to fix the whole book at once.
