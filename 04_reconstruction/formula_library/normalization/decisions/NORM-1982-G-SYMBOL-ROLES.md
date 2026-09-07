# NORM-1982-G-SYMBOL-ROLES

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-G-001`

## Decision

The overloaded 1982 source symbol `G` must be split into implementation names by formula role:

```text
G_count = k + 1
```

from `HT-F-1982-QNUM`, and:

```text
G_aux_1982 = Q1_aux_1982^2*(1+Q1_aux_1982)^2*N1
           + Q2_aux_1982*(2*Q2_aux_1982^2+3*Q2_aux_1982+1)*N2
           + Q3_aux_1982*(1+Q3_aux_1982)*N3
           + 4*Q4_aux_1982
```

from `HT-F-1982-AUX`.

The source-visible mass sum `(K + G + H + Phi)` refers to `G_aux_1982`, not to `G_count`.

## Rules

- Preserve source glyph `G` in formula transcriptions.
- Use role-specific implementation names.
- Do not import `G_count` into the mass sum.
- Do not use the underlined mass-formula `G` as a new third mathematical object without separate evidence.

## Remaining Boundary

The source formatting underline on `G` is handled separately by `NORM-1982-MASS-UNDERLINED-G`.
