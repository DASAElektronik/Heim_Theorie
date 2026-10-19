# NORM-1989-ALPHA-BRANCH-ALIASES

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-BRANCH-001`

## Decision

Alpha branch names must be model-scoped. For 1982, the branch names must also stay distinct from the unparenthesized AUX `alpha+` and `alpha-` coefficients.

Allowed implementation-facing names:

```text
alpha_branch_plus_1982
alpha_branch_minus_1982
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
- Do not use `alpha_branch_plus_1982` as the 1982 mass multiplier; `NORM-1982-MASS-MU-ALPHA-PLUS` assigns that role to `alpha_mass_plus_1982`.
- Do not treat `beta` as a separate 1989 branch name.
- Preserve source glyph notation in source-checked files.
