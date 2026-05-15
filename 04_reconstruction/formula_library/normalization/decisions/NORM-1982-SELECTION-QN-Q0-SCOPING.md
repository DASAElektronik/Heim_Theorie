# NORM-1982-SELECTION-QN-Q0-SCOPING

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-N-004`

## Decision

For the source-specified page-9 numerical algorithm, use:

```text
Q_base_1982 = Q(0) of x_v
```

This applies to the numerical determination of:

```text
W_vx
a_vx
b_vx
Phi_vx
```

and to occupation tuple enumeration for:

```text
N = 0
N >= 2
```

The page-9 source explicitly says not to use:

```text
Q_N_1982 = Q(N)
```

for that calculation.

## Reserved Relation

`Q_N_1982 = Q(N)` remains a reserved unresolved resonance/bandwidth relation from the page-8 `SELECTION-N` record.

Do not infer:

```text
Q_N_1982 = Q_base_1982
```

and do not use this decision to define resonance-order filtering or bandwidth behavior.

## Rules

- Preserve source-local `x_v` in the `Q=Q(0)` statement.
- Preserve source-local `vx` forms in `W_vx`, `a_vx`, `b_vx`, `Phi_vx`, `x_vx`, and `M_N(vx)`.
- Do not harmonize with `nu_x` without a later alias decision.
- Do not enumerate an `N=1` spectral term.
- Do not implement Gamma bandwidth logic from this decision.

## Remaining Blockers

This decision does not resolve:

- `NORM-1982-N-003` Gamma/Q_N bandwidth relation;
- `NORM-1982-WVX-001` A-matrix slash binding;
- `NORM-1982-ALGO-001` integer/decimal-place policy;
- `NORM-1982-ALGO-002` W4 branch behavior;
- `NORM-1982-ALGO-004` printed `K < 0` versus surrounding `K4` prose.

## Critic Check

A read-only Critic check accepted this scoped Q convention and confirmed that it must not be treated as a full resonance implementation unblocker.
