# NORM-1982-ALGO-W4-CASES

Date: 2026-05-15

Decision IDs resolved:

- `NORM-1982-ALGO-002`
- `NORM-1982-ALGO-004`

## Decision

The `W_4` case behavior is normalized as source-literal pseudocode with an explicit case `(c)` interpretation variant.

Input after maximal `K_3` selection:

```text
W_4 = W_3 - alpha_3*K_3 >= 0
```

## Case (a): `W_4 = 0`

The source states that `W_4 -> 0` would imply `K_4 -> infinity`, which is impossible, and therefore:

```text
K4_raw = alpha_3*K_3
K_4 = integerize_K4(K4_raw)
```

If `alpha_3*K_3` is non-integer, reconcile it only through `NORM-1982-ALGO-INTEGER-DECIMAL-RULE`. Do not invent a separate rounding rule.

## Case (b): `0 < W_4 <= 1`

Use the source logarithmic equation:

```text
K4_raw = (-3*Q_4*ln(W_4)) / (2*k - 1)
K_4 = integerize_K4(K4_raw)
```

`integerize_K4` is governed by `NORM-1982-ALGO-INTEGER-DECIMAL-RULE`.

## Case (c): `W_4 > 1`

Preserve the source-visible statement:

```text
ln W_4 > 0 and K < 0
```

Do not silently rewrite that printed `K < 0` to `K_4 < 0`.

The default implementation-facing interpretation is named:

```text
w4_case_c_k4_negative_context_post_decrement
```

because the following source prose refers to adding `alpha_3*K_3` to `K_4 < 0`.

Default pseudocode:

```text
K4_raw = (-3*Q_4*ln(W_4)) / (2*k - 1)

if K_3 == 0:
    forbidden_term
else:
    K_3_adjusted = K_3 - 1
    K4_raw_adjusted = K4_raw + alpha_3*K_3_adjusted

    if K4_raw_adjusted < 0:
        forbidden_term
    else:
        K_3 = K_3_adjusted
        K_4 = integerize_K4(K4_raw_adjusted)
```

## Non-Default Variant

The phrase about adding `alpha_3*K_3` can be read with pre-decrement `K_3`. That is not the default because the source prose first says `K_3` is decreased by 1 and then says `alpha_3*K_3` is added.

If used, it must be labeled:

```text
w4_case_c_k4_negative_context_pre_decrement_variant
```

This variant must be fixed before numerical evaluation and recorded in result metadata.

## Required Trace Fields

Any future implementation using case `(c)` must record:

```text
w4_case
w4_case_c_variant
K3_before_case_c
K3_after_case_c
K4_raw
K4_raw_adjusted
K4_integerization_method
decision_id = NORM-1982-ALGO-002/NORM-1982-ALGO-004
```

## Guardrails

- Do not choose the case `(c)` variant based on mass-fit quality.
- Do not erase the printed `K < 0` anomaly from source notes.
- Do not bypass `NORM-1982-ALGO-INTEGER-DECIMAL-RULE`.
- Do not treat this as validating the tuple algorithm numerically.

## Remaining Blockers

This decision does not resolve:

- `NORM-1982-WVX-001` A-matrix slash binding;
- `NORM-1982-N-003` Gamma/Q_N bandwidth relation.

## Critic Check

A read-only Critic check accepted this pseudocode-scoped normalization and required explicit variant labeling for case `(c)`.
