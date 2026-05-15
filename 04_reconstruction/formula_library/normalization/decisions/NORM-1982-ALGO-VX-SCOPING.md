# NORM-1982-ALGO-VX-SCOPING

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-ALGO-003`

## Decision

For the 1982 occupation algorithm record, preserve the source-local distinction:

```text
Q = Q(0) of x_v
```

and later occurrences:

```text
W_vx, a_vx, b_vx, Phi_vx, x_vx, M_N(vx)
```

Do not harmonize `x_v` to `x_vx`, and do not harmonize `x_vx` to `x_v`.

## Boundary

This resolves only the local `HT-F-1982-SELECTION-ALGO` source spelling. The project-wide `vx` versus `nu x` convention remains governed by `NORM-1982-N-001`.
