# NORM-1989-FPHI-BUW-TOKEN-BLOCKER

Date: 2026-05-15

Last updated: 2026-05-18

Decision ID triaged:

- `NORM-1989-FPHI-002`

## Triage Result

Historical blocker note. `NORM-1989-FPHI-002` is now resolved by `NORM-1989-FPHI-BUW-PRODUCT-SCOPE.md`; this file preserves the original uncertainty.

`BUW^{-1}_{N=0}` is a source-visible compact cluster in `(B49)`. The later recheck found enough local context to normalize it as `B_1989_B28 * U_B50 * W_N0_1989^(-1)`.

## Evidence Checked

The original search found `BUW` only in:

- the source-visible `(B49)` self-coupling line;
- source-check worker and Critic notes;
- normalization and symbol-register notes created from that line;
- later prose that refers back to `(B49)` and says parameters in the phi expression were adjusted to empirical conditions.

The later 2026-05-18 recheck added local evidence for the component parse:

- `(B22)` defines `W_{N=0}` as the excitation-independent factor;
- `(B48)` uses `b_2/W_{N=0}` in the same lifetime context;
- `(B50)` defines `U`;
- prose after `(B49)` says `B` is computed from `(B28)`;
- source images `page-03.png` and `page-08.png` attach `^{-1}_{N=0}` visually to `W`.

The original unresolved search targets were:

```text
BUW
B*U*W
B U W
W_{N=0}
inverse scope for W or BUW
```

A web search for Heim-specific `BUW`/`B49` combinations did not return a relevant primary or reliable secondary definition.

## Superseded Rules

- Preserve `BUW_N0_inverse_source_token` only as a raw source token.
- The normalized default is `B_1989_B28 * U_B50 * reciprocal(W_N0_1989)`.
- Do not substitute `W_{N=0}` from the 1982 selection system unless a later source-backed decision explicitly establishes that alias.
- Do not implement numeric `phi_B49` while the B50 sign remains unresolved.

## Open Research Target

To resolve this blocker, find a primary or near-primary source that defines one of:

```text
BUW^{-1}_{N=0}
B U W_{N=0}^{-1}
W_{N=0} in the 1989 phi/lifetime context
```

or a source-backed implementation note that explains how the 2002/2003 reprogramming treated the token. This target is now closed for product scope; it remains useful only for independent confirmation.
