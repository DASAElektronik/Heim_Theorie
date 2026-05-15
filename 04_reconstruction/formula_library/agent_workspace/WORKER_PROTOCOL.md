# Worker Protocol

Workers are narrow transcription agents. They produce packets; they do not decide project status.

## Inputs

Each worker gets exactly one `task_id` from `TASK_QUEUE.csv`.

Required context:

- source image path(s)
- OCR text line range
- current formula file if one exists
- relevant queue entry

## Required Output

Create one Markdown packet in `worker_packets/` using this name:

```text
<task_id>__worker-<letter>.md
```

Example:

```text
OCR-1982-SELECTION-WVX__worker-a.md
```

## Packet Format

```markdown
# <task_id> Worker <letter>

## Scope

- Formula ID:
- Image pages:
- OCR lines:

## Transcription

Use plain text or LaTeX. Preserve line breaks from the source where helpful.

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|

## Ambiguities

List every unreadable or uncertain glyph. Do not guess.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|

## Do Not Integrate Yet

State any blocker that should prevent canonical edits.
```

## Worker Rules

- Cite image page and OCR line for every formula-relevant correction.
- Prefer `ambiguous` over a plausible guess.
- Do not normalize notation unless the task explicitly asks for a normalized rendering.
- If a bracket, exponent, root, subscript, or fraction bar is unclear, mark it.
- Do not use Excel, C, Pascal, or later 1989 material to repair a 1982 source reading.
- Do not edit files outside `worker_packets/`.

