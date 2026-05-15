# NORM-1989-FPHI-BUW-TOKEN-BLOCKER

Date: 2026-05-15

Decision ID triaged:

- `NORM-1989-FPHI-002`

## Triage Result

Do not mark `NORM-1989-FPHI-002` resolved.

`BUW^{-1}_{N=0}` is a source-visible token in `(B49)`, but the current local corpus does not define it. It must remain opaque.

## Evidence Checked

Local full-text and repository search found `BUW` only in:

- the source-visible `(B49)` self-coupling line;
- source-check worker and Critic notes;
- normalization and symbol-register notes created from that line;
- later prose that refers back to `(B49)` and says parameters in the phi expression were adjusted to empirical conditions.

No local definition was found for:

```text
BUW
B*U*W
B U W
W_{N=0}
inverse scope for W or BUW
```

A web search for Heim-specific `BUW`/`B49` combinations did not return a relevant primary or reliable secondary definition.

## Rules

- Preserve `BUW_N0_inverse_source_token` as an opaque source token.
- Do not expand it to `B * U * W`.
- Do not decide whether the inverse applies to `W`, `UW`, or the whole `BUW` cluster.
- Do not substitute `W_{N=0}` from the 1982 selection system unless a later source-backed decision explicitly establishes that alias.
- Do not implement numeric `phi_B49` while this token remains unresolved.

## Open Research Target

To resolve this blocker, find a primary or near-primary source that defines one of:

```text
BUW^{-1}_{N=0}
B U W_{N=0}^{-1}
W_{N=0} in the 1989 phi/lifetime context
```

or a source-backed implementation note that explains how the 2002/2003 reprogramming treated the token.
