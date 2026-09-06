# NORM-1982-ALPHA-RECONCILIATION

Date: 2026-05-15

Rechecked: 2026-09-06 with `scripts/audit_alpha.py` and independent review.

Decision ID resolved:

- `NORM-1982-ALPHA-002`

Follow-up residual policy:

- `NORM-1982-ALPHA-003`

## Decision

The discrepancy in the printed positive reciprocal is handled by documenting
two explicit variants. This resolves a documentation/implementation policy,
not the numerical discrepancy. Neither variant reproduces the printed value
within half of its last shown decimal place.

### Variant A: `source_transcription_variant`

This variant follows `NORM-1982-ETA-INDEX` literally:

```text
eta_11 = eta_k_q(1, 1)
eta_12 = eta_k_q(1, 2)
```

It is the only source-literal normalization of the visible ALPHA abbreviation block.

With the source-checked equation

```text
alpha * sqrt(1 - alpha^2)
  = 9 * vartheta * (1 - A1*A2) / (2*pi)^5
```

this gives:

```text
alpha_plus^-1 ~= 137.049188026664
alpha_minus^-1 ~= 1.000026621616
```

### Variant B: `printed_alpha_fit_variant`

This existing, target-motivated variant approaches the printed positive
reciprocal by reading the bare `eta_12` occurrence as:

```text
eta_12 = eta_k_q(2, 1)
```

This is not source-literal transcription. It is an `our_inference` / model variant motivated by the printed positive reciprocal.

It gives:

```text
alpha_plus^-1 ~= 137.035960995152
```

compared with printed:

```text
alpha_(+)^-1 = 137.03596147
```

The 80-digit audit with mathematical pi gives residual
`-4.7484842225779391e-7`, approximately 47.48 units of the last printed place
(`1e-8`). It lies outside the rounding interval `[137.035961465, 137.035961475]`.
Using the source's finite printed pi does not remove the discrepancy. The
historical variant name is retained for continuity; it does not mean a match.

## Unresolved Residual

The same branch equation does not reproduce the printed negative reciprocal:

```text
computed alpha_minus^-1 ~= 1.00002663
printed  alpha_(-)^-1  = 1.00001363
```

This residual is not solved by the `printed_alpha_fit_variant`. It is resolved as a source-literal residual policy in `NORM-1982-ALPHA-NEGATIVE-BRANCH`.

## Guardrails

- Do not overwrite the source transcription of `eta_12`.
- Do not treat `printed_alpha_fit_variant` as historical validation.
- Do not assert equality with the printed `alpha_plus` value in a regression
  test, even for `printed_alpha_fit_variant`. Test the independently derived
  result and report its nonzero source residual.
- Do not claim the negative branch is reconciled by this decision; `NORM-1982-ALPHA-NEGATIVE-BRANCH` only prevents the printed residual from becoming a false regression target.
- Keep reciprocal notation explicit: `alpha_(+)^-1` and `alpha_(-)^-1`.

## Critic Check

A read-only Critic check accepted this variants-based reconciliation and rejected a silent source rewrite.

The 2026-09-06 independent mathematical review clarified that this is a
variants/residual policy, not numerical reconciliation. See
`alpha_audit/reviews/MATH_REVIEW_2026-09-06.md` and the machine result.
