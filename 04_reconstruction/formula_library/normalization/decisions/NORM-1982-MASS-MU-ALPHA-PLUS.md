# NORM-1982-MASS-MU-ALPHA-PLUS

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-MASS-001`

## Decision

The source-visible `mu alpha+` cluster in the 1982 mass formula is normalized as a juxtaposition product:

```text
M_1982 =
  mu_mass_element_1982
  * alpha_mass_plus_1982
  * (K_aux_1982 + G_aux_1982 + H_aux_1982 + Phi_aux_1982)
```

The plus binding is resolved by the local 1982 AUX block: unparenthesized `alpha+` is defined in AUX `(VIII)` and is distinct from the parenthesized branch `alpha_(+)` in `HT-F-1982-ALPHA`.

## Rules

- Preserve the source transcription `M = µα+ (K + G + H + Φ)` in formula files.
- Use `mu_mass_element_1982 * alpha_mass_plus_1982` in implementation-facing normalized formulas.
- Do not use `alpha_branch_plus_1982` for the 1982 mass multiplier unless a future alias decision explicitly permits it.
- The mass sum uses `K_aux_1982`, `G_aux_1982`, `H_aux_1982`, and `Phi_aux_1982`.
- The underlined source `G` remains typography-only per `NORM-1982-MASS-UNDERLINED-G`.

## Remaining Boundaries

This decision does not make the 1982 mass formula implementation-ready. The occupation tuple selection rules and downstream selection/resonance blockers remain unresolved.

It also does not normalize the 1989 mass formula or neutrino formula. Those retain their separate 1989 blockers and model-version decisions.

## Critic Check

A read-only Critic check accepted this narrow binding decision and confirmed that it must be paired with `NORM-1982-AUX-SYMBOL-ROLES`.
