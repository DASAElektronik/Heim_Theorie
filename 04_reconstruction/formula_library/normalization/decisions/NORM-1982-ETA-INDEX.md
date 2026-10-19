# NORM-1982-ETA-INDEX

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-ALPHA-001`

Follow-up blocker created:

- `NORM-1982-ALPHA-002`

## Decision

Define one canonical implementation helper by the variables in the printed formula body:

```text
eta_k_q(k, q) = pi / [pi^4 + (4 + k) q^4]^(1/4)
```

Keep the source aliases distinct:

- ALPHA source alias `eta_{kq}` maps to `eta_k_q(k, q)`.
- AUX/SELECTION source alias `eta_{qk}` maps to the same helper by the formula variables `k` and `q`, not by the visual subscript order.

Bare ALPHA subscripts remain source-literal within the ALPHA block:

```text
eta_11 = eta_k_q(1, 1)
eta_12 = eta_k_q(1, 2)
```

Do not silently flip `eta_12` to `eta_k_q(2, 1)` during normalization.

## Evidence

- The ALPHA abbreviation block visibly defines `eta_{kq}` with formula body `(4+k)q^4`.
- The AUX block visibly defines `eta_{qk}` with the same formula body `(4+k)q^4`.
- SELECTION-WVX uses `eta_{qk}` repeatedly but does not introduce a competing definition.
- The ALPHA Critic review explicitly warns not to let later AUX notation silently overwrite the ALPHA source-local spelling.

## Implementation Rule

Implementation may expose readable source aliases, but charge/mass formula code must call the canonical helper with named arguments:

```text
eta_k_q(k=<configuration k>, q=<absolute charge q>)
```

Avoid positional calls such as `eta(1, 2)` unless the call site states which source alias and argument meaning is intended.

## Residual Risk

The printed ALPHA reciprocal values are handled by separate decisions. `NORM-1982-ALPHA-RECONCILIATION` records the positive-branch source-literal and printed-fit variants, and `NORM-1982-ALPHA-NEGATIVE-BRANCH` records the negative-branch source residual. Those decisions do not reverse the source-visible index order inside the ALPHA transcription.

## Critic Check

A read-only Critic check accepted this decision with these guardrails:

- keep source aliases `eta_{kq}` and `eta_{qk}` visible;
- use a single semantic helper `eta_k_q(k,q)`;
- keep ALPHA `eta_12` source-literal as `eta_k_q(1,2)`;
- do not use the printed alpha reciprocal value to force an index flip without a separate documented decision.
