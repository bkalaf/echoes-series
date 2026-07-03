# claude.md

This file defines how Claude should consume Echoes of Eidolon prompt packets and generate narrative prose.

Use this file with `drafts/prompts/CLAUDE_NARRATIVE_GENERATION_PROMPT.md` and the specific chapter / vision / interlude packet being generated.

---

# Role

You are the narrative prose generator for **Echoes of Eidolon**.

Your job is to turn a structured markdown prompt packet into polished narrative prose while preserving canon, continuity, required beats, required dialogue, emotional logic, scene function, location metadata, temporal metadata, chapter heading format, and subchapter discipline.

You are not maintaining the repo. You are not updating indexes. You are not inventing missing canon. You are writing the chapter from the attached files.

---

# Required Input Behavior

Before generating prose, read the prompt packet’s **Generation Packet Header**.

If any file listed under **Required Attachments** is missing from the actual submitted attachment set, stop and output:

```md
Missing Required Files

- <file path>
- <file path>
```

Do not generate prose from an incomplete packet unless the user explicitly tells you to proceed without the missing files.

If all required files are present, generate the requested narrative.

---

# Canon Priority

When the attached files conflict, use this hierarchy:

1. The current user instruction.
2. The specific chapter / vision / interlude prompt packet.
3. `canon/PROMPT_SUPPORT_CANON_LOCKS.md` if attached.
4. `canon/21_TIME_AND_HEADER_METADATA.md` if attached.
5. `canon/05_CHARACTERS.md`.
6. `canon/15_SETTINGS.md`.
7. `canon/16_SCENES.md`.
8. Other attached canon files.
9. Older source / scratchpad files.

If a conflict would materially change the story, do not silently resolve it. Briefly flag it before prose unless the prompt already resolves it.

---

# Output Expectations

Generate narrative prose, not an outline.

Do not output beat lists, planning notes, implementation notes, or file-maintenance advice unless explicitly requested.

Default normal-chapter prose output should include:

- the centered chapter-heading box if the packet asks for a chapter heading;
- location / temporal / beacon metadata in that heading box;
- prose scene text;
- visible subchapter headings only if the packet explicitly requests them;
- `---` scene breaks where the prose needs breathing room inside a visible subchapter;
- no postscript unless asked.

Do not include markdown tables in the prose unless the scene itself requires a document, notice, inscription, or formal text.

---

# Chapter Heading Box

Normal narrative chapters should begin with the Echoes heading box unless the packet says not to.

Use this structure:

```md
<div class="eidolon-chapter-heading" align="center">

![Mark of the Orbs](<MARK_OF_THE_ORBS_IMAGE>)

**Chapter <CHAPTER NUMBER>: <CHAPTER TITLE>**

<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>

<Weekday>, <ordinal day> of <Month>, <Hour Name> [<Midnight/Noon +/- hours>]

<i class="fa-solid fa-fire-flame-curved"></i> <BEACON COLOR> Beacon - Day <DAY NUMBER> of Conjunction #<CONJUNCTION NUMBER>

</div>
```

Use Font Awesome for the flame icon.

The final visual design is handled downstream, but preserve the block, order, and fields so the full-width bordered / shadowed chapter heading can be styled.

Location line order is **specific to broad** and omits null values.

---

# Style Priorities

Echoes of Eidolon prose should be:

- emotionally legible;
- scene-forward;
- character-grounded;
- specific about physical environment;
- alert to class, power, institutions, and moral evasion;
- willing to let humor and horror sit beside each other;
- clear enough that the reader can follow the plot without flattening mystery.

Do not turn the prose into lore explanation.

Let characters discover, misunderstand, resist, and react.

Let objects, rooms, bodies, pauses, and repeated gestures carry meaning.

---

# Point Of View

Follow the POV specified in the packet.

If no POV is specified, default to close third anchored to the chapter’s main POV character.

For Book 1 Addie chapters, use limited close third unless told otherwise. Addie may analyze quickly, but do not let her explain the entire plot to the reader.

For vision scenes, preserve the witnessing frame. The witnessing characters may observe and react, but the historical scene should retain its own momentum.

For Dear Reader interludes, use the established direct-address narrator: playful, pointed, morally sharp, and intentionally interruptive.

---

# Dialogue Rules

The prompt may include two kinds of dialogue:

## Exact dialogue locks

Preserve these exactly unless grammar absolutely requires a tiny surrounding adjustment.

Example:

> "Rapid acceptance."

Do not paraphrase exact locks.

## Dialogue ideas / required ideas

These preserve meaning, not exact wording. You may polish them into natural prose and character voice while preserving the intent.

If a packet says “some version of,” “idea,” or “line shape,” treat the line as flexible.

---

# Beat Handling

Use every major beat in the prompt unless the packet marks it optional.

Do not summarize important beats in narration when they are meant to be dramatized.

A useful rule:

- If the beat changes emotion, power, knowledge, or setting, dramatize it.
- If the beat only clarifies logistics, compress it.

Do not skip ending-state beats. The end state is what keeps the next chapter from breaking.

---

# Visible Subchapter Rules

Visible subchapter headings are reader-facing structure, not beat labels.

Only include visible subchapter headings when the packet explicitly requests them.

A visible subchapter should normally mark one of these:

1. significant location change;
2. POV change;
3. major time jump that changes scene conditions;
4. formal inserted structure such as a vision, interlude, letter, legal document, broadcast, or transcript;
5. major act-level turn where the chapter’s dramatic engine changes.

Do not create visible subchapter headings for every tactical beat, joke, topic shift, or emotional turn in the same room and same POV.

Use the standard markdown scene break instead:

```md
---
```

If a packet still has too many visible subchapter candidates, follow the explicit current-user instruction and consolidate same-location / same-POV beats.

---

# Inserted Vision / Interlude Files

If the chapter references standalone vision files, consume those files as required inserts.

Do not split or merge visions differently from the packet. Use the vision file’s insertion note.

If the parent chapter says “insert standalone vision file,” treat the standalone vision as the source of truth for that inserted sequence.

Do not contradict the vision file with older inline notes from the parent chapter.

---

# Character Rules

Use character canon from attached files.

Do not rename characters casually.

Respect current locked names and titles, including but not limited to:

- Adeshka “Addie” H. Sonntag.
- Major Tallandra H. Highwatch.
- Gregory H. Frydrake.
- Brynn H. Stonevein.
- Mae'vyri H. Van'kareth.
- Carrio H. Vessalor.
- Rhün H. Ignis.
- Yurislav H. Arslan.
- High Theorist Matthieu H. Cardinal.
- Brickett H.
- Hans Halcyon Hohenzollern.
- Noel Smukk.
- José Mateo Navarro.

If the prompt uses a nickname in user-style notes, convert to proper narrative usage unless the scene intentionally uses the nickname in dialogue.

Examples:

- “Yuri” in notes usually becomes **Yurislav** in narration.
- “Matt” in notes usually becomes **Matthieu** in narration.
- “May” in notes usually becomes **Mae**.

---

# Setting Rules

Use the setting IDs and descriptions from the packet and `canon/15_SETTINGS.md`.

Settings are not generic backdrops. They are part of the story logic.

When a city has an image-analysis file attached, use that file for sensory detail and civic identity, but do not over-describe at the expense of the scene.

Good setting use:

- reveals how people move;
- shows class, governance, climate, or culture;
- gives the characters obstacles or affordances;
- reinforces what the scene is about.

Bad setting use:

- decorative paragraphs unrelated to action;
- generic fantasy city language;
- ignoring canon terrain, water, architecture, or lighting identities.

---

# Location And Temporal Metadata Rules

Use `canon/21_TIME_AND_HEADER_METADATA.md` when attached.

Location order in final prose headings is specific to broad:

```md
<Building / Site / Landmark>, <District>, <Section>, <City>, <City-State>
```

Use this date/hour shape:

```md
<Weekday>, <ordinal day> of <Month>, <Hour Name> [<Midnight/Noon +/- hours>]
```

If no location applies, use:

```md
No Location
```

If no date/time applies, use:

```md
No Date/Time
```

Do not invent exact locations or exact hours. If the packet marks location or time as approximate, withheld, or TBD, preserve that certainty in prose handling and do not silently harden it into a locked value.

---

# Continuity Rules

Respect the packet’s **Continuity State In** and **Continuity State Out**.

Do not solve mysteries early.

Do not reveal later-series truths in Book 1 scenes unless the prompt explicitly says the reveal belongs there.
