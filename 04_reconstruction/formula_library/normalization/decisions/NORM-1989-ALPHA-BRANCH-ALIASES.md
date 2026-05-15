# NORM-1989-ALPHA-BRANCH-ALIASES

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-BRANCH-001`

## Decision

Alpha branch names must be model-scoped.

Allowed implementation-facing names:

```text
alpha_plus_1982
alpha_minus_1982
alpha_plus_1989
alpha_minus_1989
```

Readable formula records may use `alpha_plus` and `alpha_minus` only when the formula ID already fixes the model context.

## Source Alias Table

```text
1982 source: alpha_(+), alpha_(-), beta
1989 source: alpha_(+), alpha_+, alpha_(-), alpha_-
```

## Rules

- Do not use an unversioned numeric alpha branch across 1982 and 1989.
- Do not treat `beta` as a separate 1989 branch name.
- Preserve source glyph notation in source-checked files.
