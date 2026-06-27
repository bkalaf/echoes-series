# Chapter Outline System

This file defines how chapter outlines should be written so they can support both new drafting and reconstruction of previously drafted chapters.

## Core Principle

Not every chapter needs the same level of detail.

Some chapters are only conceptual. Others have already been written and need enough beat detail that they can be reconstructed with the same skeleton while allowing prose and dialogue to change.

## Detail Levels

| Level | Name | Use Case |
|---|---|---|
| L1 | Summary Only | Placeholder chapters, early planning, loose future books. |
| L2 | Standard Beat Outline | Normal new chapter drafting. |
| L3 | Scene-by-Scene Outline | Multi-location, multi-POV, or structurally complex chapters. |
| L4 | Reconstruction Outline | Previously drafted chapters whose skeleton must be preserved. |

## L1 — Summary Only

Use this only when the chapter is not yet developed.

```md
# Chapter X — Title

## Detail Level
L1 Summary Only

## Purpose

## POV

## Setting

## Required Canon

## Summary

## Ending Hook
```

## L2 — Standard Beat Outline

Use for ordinary chapter generation.

```md
# Chapter X — Title

## Detail Level
L2 Standard Beat Outline

## Purpose

## POV

## Location

## Cast Present

## Timeline Position

## Starting Emotional State

## Ending Emotional State

## Emotional Turn

## Plot Turn

## Required Reveals

## Chapter Beats
1.
2.
3.
4.
5.

## Ending State

## Next Chapter Handoff
```

## L3 — Scene-by-Scene Outline

Use for chapters with meaningful breaks, location shifts, POV shifts, memory transitions, or nested story structures.

```md
# Chapter X — Title

## Detail Level
L3 Scene-by-Scene Outline

## Purpose

## POV

## Timeline Position

## Cast Present

## Section Breaks
This chapter contains horizontal section breaks.

## Scene Sections

### Section 1 — Internal Label Only
- Visible to reader: No
- Location:
- Cast:
- Scene goal:
- Conflict:
- Emotional function:
- Plot function:
- Beat list:
  1.
  2.
  3.
- Exit condition:

---

### Section 2 — Internal Label Only
- Visible to reader: No
- Location:
- Cast:
- Scene goal:
- Conflict:
- Emotional function:
- Plot function:
- Beat list:
  1.
  2.
  3.
- Exit condition:

## Final Image

## Next Chapter Handoff
```

## L4 — Reconstruction Outline

Use for chapters that were already drafted and need to be preserved structurally.

```md
# Chapter X — Title

## Detail Level
L4 Reconstruction

## Preserve Skeleton?
Yes

## Allowed Changes
- Dialogue wording may change.
- Prose may tighten.
- Transitions may smooth.
- Repetition may be reduced if the same beat remains intact.

## Not Allowed Changes
- Do not remove beats.
- Do not reorder beats unless explicitly requested.
- Do not change who discovers information.
- Do not change who speaks the key line.
- Do not change the chapter ending.
- Do not merge section breaks.
- Do not invent new canon.
- Do not solve pacing by cutting required mechanics.

## POV

## Timeline Position

## Starting Emotional State

## Ending Emotional State

## Cast Present

## Locations

## Required Objects

## Required Gestures

## Required Lines / Dialogue Intentions
These do not need to be exact wording unless marked `verbatim`.

| Speaker | Dialogue Intention | Verbatim? |
|---|---|---|
|  |  | No |

## Section Map

### Section 1 — Internal Label Only
- Visible to reader: No
- Starts with:
- Ends with:
- Location:
- Characters:
- Emotional function:
- Plot function:
- Required objects:
- Required gestures:
- Required dialogue intentions:
- Beat-by-beat skeleton:
  1.
  2.
  3.
  4.

---

### Section 2 — Internal Label Only
- Visible to reader: No
- Starts with:
- Ends with:
- Location:
- Characters:
- Emotional function:
- Plot function:
- Required objects:
- Required gestures:
- Required dialogue intentions:
- Beat-by-beat skeleton:
  1.
  2.
  3.
  4.

## Final Image

## Next Chapter Handoff
```

## Horizontal Break Rule

Horizontal breaks are not automatically subchapters.

Use manuscript-visible horizontal breaks when a chapter needs a pause, location shift, POV shift, memory shift, or nested-story transition.

In manuscript text:

```md
---
```

In outline text:

```md
### Section 1 — Internal Label Only

---

### Section 2 — Internal Label Only
```

The section labels are drafting scaffolds only. They are not printed as subchapter headers unless a later outline explicitly says they should be visible.

## Subchapter Rule

| Element | Visible to Reader? | Purpose |
|---|---:|---|
| Chapter title | Yes | Formal chapter label. |
| Horizontal break | Yes | Pause / shift / breath. |
| Internal section label | No | Drafting scaffold. |
| Subchapter title | Rare | Only if explicitly requested. |

## Chapter Verification Checklist

Before accepting a generated chapter:

- Required canon preserved.
- Detail level obeyed.
- Section breaks preserved.
- POV preserved.
- Beat order preserved.
- Ending hook preserved.
- Character voice and role preserved.
- No superseded names introduced.
- No invented ships, cities, Witnesses, or rewards.
- Dialogue changes remain within allowed scope.
