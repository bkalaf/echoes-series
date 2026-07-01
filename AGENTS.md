# AGENTS.md

This repository is the working canon, outline, and generation-prep system for **Echoes of Eidolon**.

The goal is not just to collect notes. The goal is to maintain **prompt-ready markdown packets** that can reliably generate narrative prose without losing canon, settings, scene continuity, source beats, or cross-file accountability.

These rules apply to every agent or assistant working in this repo.

---

# Operating Principle

Do not treat draft files as casual scratchpads once they are part of the active chapter system.

A usable draft should be able to answer these questions without relying on chat memory:

1. What chapter / vision / interlude is this?
2. Where does it go?
3. What files must be attached when generating prose?
4. What settings does it use?
5. What characters does it use?
6. What canon files does it depend on?
7. What beats must be preserved?
8. What dialogue must be preserved exactly?
9. What state must the story be in when the chapter ends?

If a file cannot answer those questions, it is not prompt-ready.

---

# Source-of-Truth Hierarchy

When sources conflict, use this hierarchy unless the user explicitly overrides it in the current task:

1. Direct user instruction in the current conversation.
2. Active chapter / vision / interlude draft being edited.
3. Canon locks in `canon/`.
4. Character / setting / scene indexes.
5. Prior draft notes and scratchpad files.
6. Older memory or older source cards.

Never silently choose a lower-priority source over a higher-priority source. If a conflict is real, flag it.

---

# Required Maintenance After Narrative Insertions

Every time a narrative chapter, vision, interlude, or meaningful scene is added or materially changed, update the relevant indexes in the same work pass unless the user explicitly says not to.

## Always check

- `drafts/README.md`
- `canon/15_SETTINGS.md`
- `canon/16_SCENES.md`

## For Book 1 changes, also check

- `canon/10_BOOK01_CHAPTER_OUTLINES.md`
- `canon/12_BOOK01_CALENDAR_TIMELINE.md`

## For standalone vision changes, also check

- `drafts/visions/README.md`
- parent chapter file that references the vision
- relevant scene rows in `canon/16_SCENES.md`

## For Dear Reader / interlude changes, also check

- `canon/04_DEAR_READER_INTERLUDES.md`
- `drafts/interludes/source_material/README.md`
- `drafts/README.md`
- relevant book outline or master outline

## For Book 14 / full-memory / Architect material, also check

- `scratchpad/14_09_the_unwound_core_beats.md`
- `drafts/14_09_second_vision_parse.md`
- `drafts/14_09_second_vision_name_corrections.md`
- `canon/11_ARCHITECT_EXODUS_COMPROMISES.md`
- `canon/12_HANS_FILE_NOEL_EXILE.md`
- `canon/16_SCENES.md`

---

# Settings Are Not Optional

Any reusable place introduced by a chapter must have a setting row in `canon/15_SETTINGS.md`.

Do not leave chapter prompt language such as:

- “potential setting if indexed later”
- “maybe add setting”
- “setting TBD”

inside a prompt-ready draft.

If the setting exists, link it. If it does not exist, add it.

## Setting ID style

Use stable IDs:

- City: `SET-PFN`
- District / section: `SET-PFN-TEMPLE-WETLAND-QUARTER`
- Building / institution: `SET-LUM-WHITE-TOWER-ARCHIVES`
- Site / landmark: `SET-PFN-SWAMP-CHURCH`
- Route / transit: `SET-LUM-PORTALPORT`
- Metaphysical / historical: `SET-MIRROR-AQM-THRONE`, `SET-B14-COUNCIL`

Settings are reusable places. Scenes are time-bound events. Do not confuse them.

---

# Scenes Must Be Maintained

Every meaningful narrative unit needs a row in `canon/16_SCENES.md` with:

- Scene ID
- Source file
- Time / date
- Setting ID(s)
- Setting summary
- Primary cast / character links
- Scene function

For Book 1, scene IDs should follow the existing pattern:

- `B01-S140`, `B01-S150`, etc.
- Use subscene ranges when a chapter has multiple major locations or movements.

For Book 14, preserve the existing `B14-S090` style unless the scene index is refactored.

---

# Canon Locks And Corrections Belong In Central Files

Do not bury correction history inside chapter-generation prompts.

Move spelling corrections, name corrections, “use X not Y” notes, and global continuity warnings into central canon/support files.

Preferred locations:

- Global prompt/canon usage locks: `canon/PROMPT_SUPPORT_CANON_LOCKS.md`
- Character names / identity / current locks: `canon/05_CHARACTERS.md`
- Settings: `canon/15_SETTINGS.md`
- Scenes: `canon/16_SCENES.md`
- City allegiance / faction maps: `canon/20_CITY_ALLEGIANCES.md`
- Founding triads / capitals: `canon/19_CITY_STATE_FOUNDING_TRIADS.md`
- Architect name corrections: `drafts/14_09_second_vision_name_corrections.md` or canon equivalent if promoted

Chapter files may include chapter-specific constraints, but they should not carry old correction logs once the correction is resolved.

Bad prompt hygiene:

```md
Correction:
- The line belongs to Yurislav, not Rhün.
```

Better:

```md
Yurislav gives the line “Rapid acceptance.” Rhün remains quiet physical support.
```

---

# Prompt-Ready Draft Structure

Every prompt-ready narrative draft should begin with a **Generation Packet Header**.

Use this structure:

```md
# <Draft ID> — <Title>

## Generation Packet Header

| Field | Value |
|---|---|
| Status | Prompt-ready / L4 / Stub / Needs source recovery |
| Intended Output | Narrative prose chapter / interlude / vision / scene fragment |
| Compile Slot | B01.140 / B14.090 / TBD |
| Parent File | path/to/parent.md |
| Primary Draft File | path/to/this-file.md |
| Required Attachments | List exact files to submit with the prose-generation prompt |
| Optional Attachments | List helpful but non-required files |
| Required Canon | List canon files this draft depends on |
| Settings Used | List setting IDs |
| Scene IDs | List scene IDs |
| Cast | Link or list major cast |
| Continuity State In | One-line state at chapter start |
| Continuity State Out | One-line state at chapter end |
```

Then use these sections:

```md
## Generation Brief
## Placement
## POV / Tone
## Settings
## Cast
## Chapter Function
## Beat Sequence
## Required Dialogue
## Required Inserts / Referenced Vision Files
## Ending State
## Do Not Include / Avoid
```

Only include sections that help generate prose. Remove meta-process notes from prompt-ready files.

---

# Required Attachments Rule

Every prompt-ready chapter must explicitly state which files should be attached when generating prose.

Minimum expected attachments for normal chapter generation:

- The chapter draft file itself.
- `canon/05_CHARACTERS.md`
- `canon/15_SETTINGS.md`
- `canon/16_SCENES.md`
- `canon/PROMPT_SUPPORT_CANON_LOCKS.md` once created.
- Any directly referenced vision/interlude/source file.

If a chapter uses a city visual-analysis file, list the exact file, for example:

- `locales/images/analysis/PFN.analysis.json`

If a chapter references standalone visions, list each one explicitly:

- `drafts/visions/01_02.md`
- `drafts/visions/01_03.md`
- `drafts/visions/01_04.md`

Do not make the prose generator infer attachments from vague references.

---

# Draft Types And Expected Content

## `drafts/01_XX_*.md`

Book 1 chapter prompt / parsed outline files.

Expected content:

- placement
- settings
- cast
- function
- beat sequence
- dialogue locks
- ending state
- required inserts
- dependency list

Not expected:

- unresolved correction history
- “potential setting” notes
- old spelling mistakes
- source-loss disclaimers unless the file is actually incomplete

## `drafts/visions/*.md`

Standalone vision files used as inserts.

Expected content:

- vision number
- source
- parent chapter / insertion point
- setting
- cast
- purpose
- beat sequence
- exact dialogue locks
- transition in / transition out

## `drafts/interludes/*.md`

Dear Reader prose or prompt-ready interlude files.

Expected content depends on status:

- final prose files should read like prose;
- prompt files should have beats and dependencies;
- source cards must clearly say they are not enough for final generation.

## `drafts/prompts/*.md`

Reusable generation prompts and clean prompt packets.

These are intended to be copy-pasted into external models.

## `scratchpad/*.md`

Raw or semi-structured working material.

Scratchpad files are allowed to be messy, but active drafts should not depend on scratchpad files unless the dependency is listed in the Generation Packet Header.

---

# Source Preservation Rule

Do not summarize away user-provided source material unless a clean source file already exists.

When the user uploads or dictates source material:

1. Save the raw or near-raw source where practical.
2. Create a structured parse / prompt file from it.
3. Crosslink both files.
4. Mark whether the parse is complete, partial, or needs source recovery.

Never claim “source saved” when only a short source card or fingerprint exists.

Status labels must be honest:

- `Raw source saved`
- `Source card only`
- `Parsed L4`
- `Prompt-ready`
- `Needs source recovery`
- `Prose generated`

---

# Model-Use Boundary

This repo supports two different workflows:

1. **Structured markdown / canon maintenance** — use this `AGENTS.md`.
2. **Narrative prose generation** — use `claude.md` and `drafts/prompts/CLAUDE_NARRATIVE_GENERATION_PROMPT.md`.

Do not ask a narrative model to maintain repository indexes unless the task is explicitly framed that way.

Do not ask a canon-maintenance pass to invent prose unless the task is explicitly framed that way.

---

# Pre-Commit Checklist For Agents

Before finishing a repo change, answer these:

1. Did I update every affected index?
2. Did I add every new setting to `canon/15_SETTINGS.md`?
3. Did I add or update every affected scene in `canon/16_SCENES.md`?
4. Did I remove correction clutter from prompt-ready chapter files?
5. Did I list exact required attachments in the draft header?
6. Did I preserve raw source or clearly mark that source recovery is needed?
7. Did I avoid inventing canon where the source is missing?
8. Did I cite or report the commit SHA and verification lines back to the user?

If the answer to any of these is no, say so directly.
