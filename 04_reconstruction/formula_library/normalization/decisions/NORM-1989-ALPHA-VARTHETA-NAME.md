# NORM-1989-ALPHA-VARTHETA-NAME

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-ALPHA-002`

## Decision

Use `vartheta` as the canonical implementation name for the visible theta-like Heim glyph in the 1982 and 1989 alpha records.

`theta` is allowed only as an external-code alias that maps explicitly to `vartheta`.

## Rules

- Preserve source-visible glyph notes in source records.
- Do not silently rename `vartheta` to `theta` in formulas.
- If an implementation exposes `theta`, it must document `theta = vartheta`.
