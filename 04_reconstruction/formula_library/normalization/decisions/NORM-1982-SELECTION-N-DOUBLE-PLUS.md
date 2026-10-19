# NORM-1982-SELECTION-N-DOUBLE-PLUS

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-N-002`

## Decision

The source transcription of `(XXIX)` preserves the visible doubled plus:

```text
... + + exp[(1-2k)(n_4+Q_4)/3Q_4] = W_vx(1+f)
```

For implementation-facing normalized real equations, parse this as:

```text
... + (+exp[(1-2k)(n_4+Q_4)/3Q_4]) = W_vx(1+f)
```

This is numerically equivalent to a single positive exponential term:

```text
... + exp[(1-2k)(n_4+Q_4)/3Q_4] = W_vx(1+f)
```

## Rules

- Do not delete the source-visible `+ +` from transcription.
- Do not call this a proven source typo unless using a separate emendation label.
- Do not feed raw transcription text directly to a parser or CAS.
- Implementation-facing code must cite this decision before collapsing the doubled plus to a single positive term.

## Scope

This decision applies only to the doubled plus in `(XXIX)`.

It does not resolve:

- Gamma/bandwidth semantics;
- `Q_N = Q(N)` versus `Q = Q(0)`;
- resonance filtering;
- `K_j` integer/decimal-place policy;
- `W_4` branch behavior;
- printed `K < 0` in ALGO case `(c)`.

## Critic Check

A read-only Critic check accepted this syntax-level normalization and confirmed that it must not imply full resonance-rule readiness.
