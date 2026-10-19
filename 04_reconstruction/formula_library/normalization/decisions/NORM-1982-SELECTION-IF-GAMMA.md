# NORM-1982-SELECTION-IF-GAMMA

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-SELECTION-002`

## Decision

For mass-spectrum tuple enumeration, the source-visible `iF(Gamma)` term contributes zero in the real selection equation for the enumerated cases:

```text
N = 0
N >= 2
```

The basis is the source statement in `HT-F-1982-SELECTION-N`:

```text
F(Gamma) = 0 for all N != 1
```

and the tuple algorithm starts only for:

```text
N = 0 or N >= 2
```

Therefore the implementation-facing real selection equation for those enumerated states excludes an imaginary contribution from `iF(Gamma)`.

## N = 1 Boundary

`N = 1` is not a mass-spectrum tuple-enumeration case. The source states that there is no spectral term for `N = 1` and that `f(1)` is complex.

The separate real and imaginary relations for `N = 1` are preserved as source context. They are not used to enumerate mass tuples by default.

## What Remains Blocked

This decision does not resolve Gamma or bandwidth semantics.

The source states that `n_j`, `F(Gamma)`, full bandwidths `Gamma`, and `Q_N = Q(N)` still require a relation. That remains blocked under:

- `NORM-1982-N-003`

The page-9 `Q=Q(0)` convention for tuple enumeration is handled separately by `NORM-1982-SELECTION-QN-Q0-SCOPING`.

Do not infer a bandwidth formula or resonance filtering rule from this decision.

## Rules

- Preserve `+ iF(Gamma)` in the source transcription.
- For enumerated mass-spectrum states `N = 0` and `N >= 2`, use `F(Gamma)=0` and a real equation.
- Exclude `N = 1` from default mass tuple enumeration.
- Do not collapse `Q_N_1982 = Q(N)` and `Q_base_1982 = Q(0)`.

## Critic Check

A read-only Critic check accepted this narrow resolution and confirmed that the Gamma/Q_N relation remains separately blocked.
