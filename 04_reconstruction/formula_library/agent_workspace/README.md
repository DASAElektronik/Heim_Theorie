# OCR Agent Workspace

Purpose: run cheap OCR/transcription workers in parallel without letting unreviewed output contaminate the canonical formula library.

## Roles

### Worker agents

Worker agents produce evidence packets only. They may read source images, OCR text, formula files, and queue entries. They must not edit canonical files.

Expected model tier: cheaper/faster model is acceptable if the task is narrow and mechanical.

Output location:

- `worker_packets/`

### Critic agent

The Critic reviews worker packets against page images and project guardrails. It decides whether a packet is ready for human/main-agent integration.

Expected model tier: current strongest model.

Output location:

- `critic_reviews/`

### Main integrator

The main integrator is the only role that edits canonical files:

- `formula_catalog.csv`
- `SOURCE_CHECK_QUEUE.csv`
- `formulas/*.md`
- `symbols/symbol_register.csv`
- `derivations/DERIVATION_INDEX.md`
- admin progress docs

## Rule

No worker packet becomes `source_checked` by itself. A formula can move forward only after:

1. at least two independent worker readings or one worker plus direct main-agent reading,
2. Critic review,
3. explicit integration into canonical files with retained risk notes.

## Status Meanings

- `worker_draft`: one or more worker readings exist.
- `worker_conflict`: worker readings disagree on a formula-relevant glyph.
- `critic_blocked`: Critic found a blocker.
- `critic_ready`: Critic says the transcription can be integrated as source-checked.
- `integrated`: canonical files were updated.

## Hard Boundaries

- Workers must not use spreadsheet/code output to correct source formulas.
- Workers must not infer missing brackets from mathematical plausibility.
- Ambiguous glyphs stay ambiguous.
- Every proposed correction must cite image page and OCR line.
- `source_checked` means image transcription only. It does not mean normalized, derived, implemented, or validated.

## Running Agents

Use `PROMPT_TEMPLATES.md` to launch worker and critic agents consistently.

