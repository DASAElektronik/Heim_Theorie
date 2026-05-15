# NORM-1982-ALGO-INTEGER-DECIMAL-RULE

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-ALGO-001`

## Decision

The occupation algorithm uses integer `K_j` values.

For `K_1`, `K_2`, and `K_3`, choose the maximum nonnegative integer satisfying the source residual condition:

```text
W_1 - alpha_1*K_1^3 >= 0
W_2 - alpha_2*K_2^2 >= 0
W_3 - alpha_3*K_3 >= 0
```

For `K_4`, decimal places are handled by the source `Vermerk`:

```text
K_4_integer =
  next integer, only if the decimal places are the source-recognized ,99...99 identity
  otherwise truncate/cut off decimal places
```

For nonnegative `K_4`, truncation is `floor(K_4_raw)`.

## Source Identity Exception

The `,99...99 = 1` rule is not ordinary rounding. It is a source identity exception.

An implementation must not promote values merely because they are epsilon-close to an integer unless the numeric precision profile explicitly classifies the decimal representation as the source-recognized `,99...99` case.

## Required Trace Fields

Any future implementation must record:

```text
numeric_precision_profile
raw_K_4
integerized_K_4
integerization_method = promoted_99_identity | truncated_decimal_places
decision_id = NORM-1982-ALGO-001
```

## Rules

- Do not round to nearest.
- Do not use a hidden floating-point epsilon.
- Do not choose a different integer because it improves a mass fit.
- Do not treat this decision as resolving `W_4` branch behavior.

## Remaining Blockers

This decision does not resolve:

- `NORM-1982-ALGO-002` W4 branch behavior;
- `NORM-1982-ALGO-004` printed `K < 0` versus surrounding `K4` prose;
- `NORM-1982-WVX-001` A-matrix slash binding;
- `NORM-1982-N-003` Gamma/Q_N bandwidth relation.

## Critic Check

A read-only Critic check accepted this source-faithful integer/decimal policy and warned that full tuple enumeration remains blocked by W4 and `K`/`K4` decisions.
