# NORM-1982-SELECTION-XIII-ALPHA3

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-SELECTION-001`

## Decision

The rightmost factor in source formula `(XIII)` is preserved as `alpha_3` by default:

```text
n_4 + Q_4
<= (n_3 + Q_3) * alpha_3
<= (n_2 + Q_2)^2 * alpha_2
<= (n_1 + Q_1)^3 * alpha_3
```

This is a source-literal default. Do not silently change the final `alpha_3` to `alpha_1` in normalized code.

## Emendation Variant

The later selection equation and tuple algorithm strongly suggest the pattern:

```text
cubic term  -> alpha_1
square term -> alpha_2
linear term -> alpha_3
```

Therefore an implementation may define an explicit variant:

```text
selection_xiii_alpha1_emendation_variant
```

where the final term is:

```text
(n_1 + Q_1)^3 * alpha_1
```

This variant must be marked as an emendation or typo hypothesis. It is not the default source-literal normalization.

## Rules

- Preserve the source transcription in `HT-F-1982-SELECTION.md`.
- Default normalization uses `alpha_selection_coeff_3_1982` for the printed final factor.
- Any use of `alpha_selection_coeff_1_1982` in the final factor must carry the explicit emendation variant name.
- Do not use this decision to implement the full selection algorithm.

## Remaining Boundaries

This decision does not resolve:

- `iF(Gamma)` in `(XIV)`;
- `Q_N = Q(N)` versus `Q = Q(0)`;
- source-local `vx` convention across selection records;
- doubled `+ + exp[...]` in `(XXIX)`;
- `K_j` integer and decimal-place policy;
- `W_4` branch behavior.

Those remain separate normalization blockers.

## Critic Check

A read-only Critic check accepted this source-literal default and recommended `alpha_1` only as an explicit emendation variant.
