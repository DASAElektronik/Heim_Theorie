# Critic Protocol

The Critic reviews worker packets and decides whether a source-check can be integrated.

## Inputs

For one task:

- `TASK_QUEUE.csv` row
- all available worker packets for that task
- source image(s)
- OCR text line range
- current canonical formula file(s)
- `00_admin/GUARDRAILS.md`

## Required Output

Create one Markdown review in `critic_reviews/`:

```text
<task_id>__critic.md
```

## Review Format

```markdown
# <task_id> Critic Review

## Verdict

One of:

- critic_ready
- critic_blocked
- worker_conflict

## Findings

Order by severity. Each finding must cite source page and file/line when possible.

## Accepted Transcription

Only include this section if verdict is `critic_ready`.

## Blockers

List blockers that prevent canonical integration.

## Required Canonical Changes

List exact files and fields that the main integrator should update.

## Risk Notes To Preserve

List warnings that must remain after integration.
```

## Critic Rules

- The Critic may approve a transcription, not a theory.
- `critic_ready` still does not mean normalized, derived, implemented, or validated.
- If workers disagree on a formula-relevant glyph, the verdict is `worker_conflict` unless the image resolves it clearly.
- If a visible source glyph is transcribed but its mathematical binding is unclear, approve only as visible-glyph transcription and require normalization notes.
- Do not let clean LaTeX hide source ambiguity.

