# NORM-1982-MASS-UNDERLINED-G

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-MASS-002`

## Decision

The underline on `G` in the 1982 mass formula is preserved as source formatting. It does not create a separate implementation term by default.

Normalized implementation-facing reading:

```text
M_1982 = mu_mass_element_1982 * alpha_mass_plus_1982 * (K_aux_1982 + G_aux_1982 + H_aux_1982 + Phi_aux_1982)
```

The `mu * alpha_mass_plus` binding is governed by `NORM-1982-MASS-MU-ALPHA-PLUS`; this decision resolves only the underlined `G` formatting.

## Rules

- Do not drop the underline note from source transcription.
- Do not treat underlined `G` as `G_count`.
- Do not assign special numeric weight to underlined `G` without a new source-backed decision.
