# Chapter Outline System

This file defines how chapter outlines should be written so they can support both new drafting and reconstruction of previously drafted chapters.

## Core Principle

Not every chapter needs the same level of detail.

Some chapters are only conceptual. Others have already been written and need enough beat detail that they can be reconstructed with the same skeleton while allowing prose and dialogue to change.

A chapter may also contain **visible subchapter titles** when several scenes clearly belong under one parent chapter. This is different from ordinary horizontal breaks. Use this structure when adjacent scenes share the same setting, local conflict, or escalation sequence and would read better as one longer chapter with named internal movements.

## Detail Levels

| Level | Name | Use Case |
|---|---|---|
| L1 | Summary Only | Placeholder chapters, early planning, loose future books. |
| L2 | Standard Beat Outline | Normal new chapter drafting. |
| L3 | Scene-by-Scene Outline | Multi-location, multi-POV, or structurally complex chapters. |
| L4 | Reconstruction Outline | Previously drafted chapters whose skeleton must be preserved. |
| L4+Subchapters | Reconstruction with Visible Subchapters | Previously drafted adjacent scenes grouped into one parent chapter with reader-visible internal titles. |

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

## L4 + Visible Subchapters — Parent Chapter Reconstruction

Use this when two or more adjacent drafted scenes should become one longer chapter with named, reader-visible internal movements.

This is now the preferred structure for scenes like the Royal Observatory / Royal Astronomer’s Tower opening, where the mathematical discovery and the factional reaction occur in the same setting and should keep connective tissue.

```md
# Chapter X — Parent Chapter Title

## Detail Level
L4 Reconstruction Outline with Visible Subchapters

## Chapter Structure
This parent chapter contains visible subchapter titles.

## Visible Subchapters
1. Subchapter Title One
2. Subchapter Title Two

## Purpose

## POV / Narrative Mode

## Timeline Position

## Parent Location

## Cast Present

## Required Objects / Systems

## Preserve Skeleton?
Yes. Preserve the skeletons of the grouped scenes, but draft them as connected subchapter sections under one parent chapter.

## Allowed Changes
- Smooth transitions between subchapters.
- Add connective tissue where needed.
- Maintain chapter momentum.
- Dialogue wording may be tightened if intent remains intact.

## Not Allowed Changes
- Do not remove required beats from any subchapter.
- Do not flatten subchapters into one undifferentiated block.
- Do not split the grouped sequence back into separate chapters unless explicitly requested.
- Do not invent new canon to justify the grouping.

---

# Subchapter 1 — Subchapter Title One

## Subchapter Function

## Beat-by-Beat Skeleton
1.
2.
3.

## Subchapter Exit Condition

---

# Subchapter 2 — Subchapter Title Two

## Subchapter Function

## Beat-by-Beat Skeleton
1.
2.
3.

## Subchapter Exit Condition

---

## Parent Chapter Emotional Movement

## Continuity Notes

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
| Chapter title | Yes | Formal parent chapter label. |
| Visible subchapter title | Yes, when explicitly defined | Groups major internal movements beneath a parent chapter. |
| Horizontal break | Yes | Pause / shift / breath. |
| Internal section label | No | Drafting scaffold. |
| Subchapter title | Only when explicitly requested or structurally useful | Named movement within a parent chapter. |

## Grouping Heuristic

Group adjacent manuscript units under one parent chapter when most of these are true:

- They occur in the same location or immediate local setting.
- They share the same POV or central observer.
- The second scene is a direct consequence of the first.
- The emotional escalation is continuous.
- Separating them would make the narrative feel artificially chopped.
- Combining them improves connective tissue without erasing a clear internal break.

Do not group when:

- The POV changes in a way that creates a new chapter-level promise.
- The setting changes substantially.
- The timeline jumps.
- The emotional question resets.
- The next section needs its own opening hook and final image.

## Chapter Verification Checklist

Before accepting a generated chapter:

- Required canon preserved.
- Detail level obeyed.
- Section breaks preserved.
- Visible subchapter titles used only when intended.
- POV preserved.
- Beat order preserved.
- Ending hook preserved.
- Character voice and role preserved.
- No superseded names introduced.
- No invented ships, cities, Witnesses, or rewards.
- Dialogue changes remain within allowed scope.
