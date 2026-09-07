# NORM-1989-NEUTRINO-FIELD-MASS-BOUNDARY

Date: 2026-05-18

Decision ID resolved:

- `NORM-1989-NEUTRINO-001`

## Decision

Resolve the neutrino interpretation boundary as a model-card rule.

`HT-F-1989-NEUTRINO` may be implemented only as Heim's internal 1989 field-mass construct:

```text
M_nu = mu * alpha_plus_1989 * (Phi_1989 + phi_0_B49)
```

It must not be presented as a modern neutrino mass prediction or as modern validation of the Heim model.

## Source Boundary

The source states that, under `(B63)`, the mass formula can still yield a nonzero `Feldmasse` if `Phi + phi != 0`. It then explicitly says this mass is not interpretable as a ponderable corpuscle, but as a Heim-internal `Spinpotenz` / `Feldkatalyt` construct.

The source also gives historical interpretation candidates for `beta` and `mu` neutrinos and leaves the natural realization of the remaining listed states undecided.

## Implementation Rules

- Use `M_nu` as a Heim-internal field-mass output only.
- Keep `Phi_1989` and `phi_0_B49` as separate inputs; do not collapse uppercase `Phi` into lowercase `phi`.
- Do not compare `M_nu` to modern neutrino constraints inside the formula implementation.
- Any modern comparison must live in a separate comparison profile with its constants, assumptions, data date, and source citations.
- Do not treat Heim's historical interpretation paragraph as empirical validation.

## Dependencies

This decision does not resolve executable `phi_0_B49` evaluation. The `phi_0` input still depends on the B49 normalization blockers:

- `NORM-1989-FPHI-001`
- `NORM-1989-FPHI-002`
- `NORM-1989-FPHI-003`

## Critic Check

The formula card, worker packets, and Critic review already carry this boundary. This decision makes the existing guardrail explicit in the normalization tracker and removes the P0 blocker caused by possible mislabeling.
