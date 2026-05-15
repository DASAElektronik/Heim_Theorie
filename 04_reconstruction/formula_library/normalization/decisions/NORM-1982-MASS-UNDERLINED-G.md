# NORM-1982-MASS-UNDERLINED-G

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-MASS-002`

## Decision

The underline on `G` in the 1982 mass formula is preserved as source formatting. It does not create a separate implementation term by default.

Normalized implementation-facing reading:

```text
M_1982 = mu_mass_element * alpha_plus_1982 * (K + G_aux + H + Phi_1982)
```

The `mu * alpha_plus` binding still remains governed by `NORM-1982-MASS-001`; this decision resolves only the underlined `G` formatting.

## Rules

- Do not drop the underline note from source transcription.
- Do not treat underlined `G` as `G_count`.
- Do not assign special numeric weight to underlined `G` without a new source-backed decision.
