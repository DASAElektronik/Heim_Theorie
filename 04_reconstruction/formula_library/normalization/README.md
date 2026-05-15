# Normalization Review

Purpose: convert source-checked formula transcriptions into explicit implementation candidates without hiding source ambiguity.

This folder is the gate between `source_checked` and `implemented`.

## Rules

- Do not change a source transcription during normalization.
- Every implementation-facing rewrite needs a decision ID.
- Preserve a visible source form and a normalized candidate side by side.
- Mark uncertain choices as blocked or deferred, not silently resolved.
- Do not use spreadsheet, code, or target particle masses to choose among ambiguous source readings unless the decision is explicitly labelled as secondary or validation-only.

## Files

- `NORMALIZATION_REVIEW.md`: current review snapshot and blocker list.
- `NORMALIZATION_DECISIONS.csv`: queue of normalization decisions before implementation.

