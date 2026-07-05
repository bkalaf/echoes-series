# Codex Task — Apply a Pre-Authored Edit Batch (Mechanical Only)

You are applying a batch of **pre-authored, mechanical text edits** to the *Echoes of Eidolon* manuscript repository. **All narrative has already been written.** Your job is *only* to locate exact anchors and apply the described operations. This keeps the repo the single source of truth.

## Hard rules

1. **Do not write, rewrite, rephrase, summarize, condense, "improve," or continue any prose.** If an operation cannot be applied exactly as specified, skip it and report it — never invent a fix.
2. **Anchors are byte-exact.** The `find` strings were sliced directly from the manuscript. They contain curly quotes (`“ ” ‘ ’`), em-dashes (`—`), and markdown italics (`*word*`). Match them **verbatim**, including punctuation and whitespace. **Never fuzzy-match.**
3. **One occurrence unless told otherwise.** Apply to exactly `expected_count` occurrences (default `1`). If `find` occurs a different number of times, **skip and report** — do not guess which one.
4. **Edit only within the `find` span.** Do not reflow, re-wrap, or touch surrounding text.
5. **Idempotent.** If `find` is absent but the `replace` text is already present, treat the op as already-applied and record it under `skipped_already_applied` (do not error).
6. **Encoding is UTF-8.** Preserve existing line endings and file structure.

## Input

A JSON file: `book1_edits.json` (schema below). Process every entry in `operations`. Do **not** act on entries in `deferred` — those need human input or a build-layer change; just list them in your report so nothing is lost.

```json
{
  "batch": "…",
  "encoding": "utf-8",
  "match_rules": "…",
  "operations": [
    {
      "id": "unique-id",
      "file": "01_04_the_weight_of_the_beacon.md",  // basename
      "type": "replace",            // replace | insert_after | insert_before | delete
      "expected_count": 1,
      "find": "exact anchor text",
      "replace": "new text",        // omit for delete
      "note": "human-readable description (context only; do not act on it)"
    }
  ],
  "deferred": [ { "id": "…", "file": "…", "reason": "…", "note": "…" } ]
}
```

## Procedure (per operation)

1. **Locate the file** by its `file` basename within the repo (chapters live under `drafts/`, interludes under `drafts/interludes/` — adjust to the actual tree). If **zero or more than one** file matches, skip → `unresolved` with reason `file-ambiguous`.
2. **Verify the anchor.** Count occurrences of `find` in the file.
   - If count `== expected_count`: apply.
   - If count `== 0`: check whether `replace` is already present → `skipped_already_applied`; otherwise → `unresolved` (`anchor-not-found`).
   - If count `> expected_count`: → `unresolved` (`anchor-ambiguous`).
3. **Apply by `type`:**
   - `replace` — swap `find` → `replace`.
   - `insert_after` / `insert_before` — insert `replace` (or `text`) immediately after/before `find`; if the inserted content is a paragraph, keep it as its own paragraph with a blank line.
   - `delete` — remove `find` (and clean up any doubled blank line it leaves).
4. Save the file.

## Output (report, do not commit blindly)

Return a summary with four lists, each as `{id, file}` (+ reason where relevant):

- `applied`
- `skipped_already_applied`
- `unresolved`  ← anything not applied exactly; **stop and surface these for human review**
- `deferred`    ← copied through from the JSON, untouched

Do **not** finalize/commit if anything is in `unresolved` — report it and wait. Every change must be exactly one of the pre-authored operations; if you feel the urge to write prose to make something fit, that is the signal to move it to `unresolved` instead.
