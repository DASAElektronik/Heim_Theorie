# NORM-1982-AUX-SYMBOL-ROLES

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-AUX-002`

## Decision

The reused 1982 AUX symbols must be split into role-specific implementation names. The source transcription keeps the printed glyphs, but code must use typed names.

Required implementation names:

```text
P_isospin_1982
Q_spin_1982
q_abs_charge_1982
kappa_doublet_1982

Q1_aux_1982
Q2_aux_1982
Q3_aux_1982
Q4_aux_1982

alpha_branch_plus_1982
alpha_branch_minus_1982
alpha_bare_1982

alpha_mass_plus_1982
alpha_mass_minus_1982

alpha_selection_coeff_1_1982
alpha_selection_coeff_2_1982
alpha_selection_coeff_3_1982

K_aux_1982
G_aux_1982
H_aux_1982
Phi_aux_1982
```

## Alpha Roles

The following source forms are not interchangeable:

- `alpha_(+)` and `alpha_(-)` from `HT-F-1982-ALPHA` are the parenthesized fine-structure branch names. They normalize to `alpha_branch_plus_1982` and `alpha_branch_minus_1982`.
- Bare `alpha` in AUX expressions follows the source abbreviation `alpha_(+) = alpha`, so it normalizes to `alpha_bare_1982`, an explicit alias of `alpha_branch_plus_1982` in the 1982 branch context.
- Unparenthesized `alpha+` and `alpha-` in AUX `(VIII)` are separate AUX/mass coefficients. They normalize to `alpha_mass_plus_1982` and `alpha_mass_minus_1982`.
- `alpha_1`, `alpha_2`, and `alpha_3` in AUX `(IX)` are selection coefficients. They normalize to `alpha_selection_coeff_1_1982`, `alpha_selection_coeff_2_1982`, and `alpha_selection_coeff_3_1982`.

Do not numerically equate `alpha_mass_plus_1982` with `alpha_branch_plus_1982` unless a future decision explicitly introduces that alias.

## Q And Charge Roles

The following source forms are separate implementation roles:

- `P` in AUX/Phi is `P_isospin_1982`.
- `Q` in AUX/Phi is `Q_spin_1982`.
- `q` is `q_abs_charge_1982`.
- `Q_1` through `Q_4` are auxiliary distributor values `Q1_aux_1982` through `Q4_aux_1982`.
- `Q(P)`, `Q_N = Q(N)`, and `Q = Q(0)` are not covered by this AUX decision and must not be collapsed into `Q_spin_1982` or `Qj_aux_1982`.

## Scope

This decision resolves naming and role binding only. It does not resolve:

- the `Phi` precedence itself, which is governed by `NORM-1982-AUX-PHI-PRECEDENCE`;
- the `G` overload, which is governed by `NORM-1982-G-SYMBOL-ROLES`;
- occupation tuple selection;
- `NORM-1982-SELECTION-*`, `NORM-1982-N-*`, or `NORM-1982-ALGO-*` blockers.

## Critic Check

A read-only Critic check accepted this decision as a naming and role-binding resolution, with the guardrail that the alpha families must not be silently numerically merged.
