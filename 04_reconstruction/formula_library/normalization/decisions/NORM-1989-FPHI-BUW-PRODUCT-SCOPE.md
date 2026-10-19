# NORM-1989-FPHI-BUW-PRODUCT-SCOPE

Date: 2026-05-18

Decision ID resolved:

- `NORM-1989-FPHI-002`

## Decision

Resolve the compact B49 cluster `BUW^{-1}_{N=0}` as a product of local 1989 quantities:

```text
B_1989_B28 * U_B50 * W_N0_1989^(-1)
```

The inverse and `N = 0` subscript attach to `W`, not to the whole `B U W` product.

## Evidence

- `1989_erweiterte_massenformel/page-03.png` shows the compact B49 cluster with the superscript/subscript visually attached to `W`.
- `1989_erweiterte_massenformel/page-08.png` repeats the same B49 cluster in the lifetime section.
- `(B22)` defines `W_{N=0}` as the excitation-independent factor.
- `(B48)` uses `b_2/W_{N=0}`, confirming `W_{N=0}` as a denominator quantity in the same lifetime context.
- `(B50)` immediately defines `U`.
- The prose after B49 says `B` is computed from `(B28)`.

## Implementation Rule

Use:

```text
fourth_root(2) - 4 * B_1989_B28 * U_B50 * reciprocal(W_N0_1989)
```

inside B49.

Do not keep `BUW` as a standalone unknown token in normalized implementation.

## Dependencies

This decision resolves only product and inverse scope. It does not resolve the B50 sign anomaly inside `U_B50`; therefore numerical B49 evaluation remains blocked by:

- `NORM-1989-FPHI-003`

## Rejected Parses

Do not use:

```text
(B*U*W_N0)^(-1)
B*(U*W_N0)^(-1)
opaque_BUW_N0_inverse_source_token
```

as the normalized default.

These may be kept only as explicit regression variants if future source comparison requires them.
