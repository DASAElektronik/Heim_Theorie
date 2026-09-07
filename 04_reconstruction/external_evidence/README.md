# External Evidence Review

Purpose: collect online or secondary-source claims that may explain numerical drifts without allowing them to overwrite source-checked formula transcriptions.

External evidence is advisory. It can suggest a follow-up source check, a model-version split, or a new normalization decision, but it cannot directly change a formula record.

## Rules

- Source-checked formula files remain the implementation foundation.
- Raw OCR and online snippets are never implementation inputs.
- External evidence must be classified by source type and linked to a formula ID or normalization decision.
- Version claims must stay versioned, for example 1982, 1989, 1992, or secondary summary.
- A drift is considered resolved only after a local source check or normalization decision records the rule.
- Secondary mirrors and snippets can create research tasks, not formula corrections.

## Files

- `EXTERNAL_EVIDENCE.csv`: machine-readable queue of external claims and how they relate to known drifts.
- `ALPHA_DRIFT_EVIDENCE.md`: current evidence notes for the 1982/1989/1992 alpha-branch drift.
