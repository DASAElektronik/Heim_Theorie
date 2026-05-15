# NORM-1982-ALPHA-RECONCILIATION

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-ALPHA-002`

Follow-up residual policy:

- `NORM-1982-ALPHA-003`

## Decision

The printed positive reciprocal value for the 1982 fine-structure branch is reconciled by documenting two explicit variants rather than silently changing the source transcription.

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
alpha_plus^-1 ~= 137.049188026668
alpha_minus^-1 ~= 1.000026621616
```

### Variant B: `printed_alpha_fit_variant`

This variant fits the printed positive reciprocal value by reading the bare `eta_12` occurrence as:

```text
eta_12 = eta_k_q(2, 1)
```

This is not source-literal transcription. It is an `our_inference` / model variant motivated by the printed positive reciprocal.

It gives:

```text
alpha_plus^-1 ~= 137.035960995197
```

compared with printed:

```text
alpha_(+)^-1 = 137.03596147
```

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
- Do not use the printed `alpha_plus` value as a regression target unless the model explicitly declares the `printed_alpha_fit_variant`.
- Do not claim the negative branch is reconciled by this decision; `NORM-1982-ALPHA-NEGATIVE-BRANCH` only prevents the printed residual from becoming a false regression target.
- Keep reciprocal notation explicit: `alpha_(+)^-1` and `alpha_(-)^-1`.

## Critic Check

A read-only Critic check accepted this variants-based reconciliation and rejected a silent source rewrite.
