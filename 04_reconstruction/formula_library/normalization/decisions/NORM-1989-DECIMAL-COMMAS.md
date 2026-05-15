# NORM-1989-DECIMAL-COMMAS

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-ALPHA-003`

## Decision

German decimal commas in source numeric comparison values are parsed as decimal points for machine-readable reference values.

Example:

```text
source literal: 137,03601
numeric value:  137.03601
```

## Rules

- Preserve the source literal string.
- Store a parsed numeric value separately if needed.
- Do not parse comma as thousands separator in Heim source numeric fields.
- Apply this rule only to numeric literals, not to comma-separated subscripts.
