# NORM-1989-QX-C-OVER-K

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-QX-002`

## Decision

For implementation, the 1989 correction defines a model-versioned structure distributor:

```text
C_1982 = 2(P eps_P + Q eps_Q)(k - 1 + kappa)/(1 + kappa)
C_1989 = C_1982 / k
```

The source-visible `(B2)` formula remains:

```text
q_x = 1/2[... + C]
```

In the normalized 1989 model, that `C` denotes `C_1989`.

## Implementation Rule

Use explicit versioned names in code:

```text
qx_1982 = 1/2 * (... + C_1982)
qx_1989 = 1/2 * (... + C_1989)
```

For 1982, this is equivalent to the source form `2q_x = ... + C_1982`.

Do not use an unversioned implementation variable named only `C` in charge-number code.

## What This Does Not Mean

- Do not rewrite the source transcription of `(B2)` to `+ C/k`.
- Do not apply division twice as `C_1982 / k / k`.
- Do not mix the 1982 and 1989 charge-number formulas in one unversioned implementation.

## Evidence

The 1989 source states as prose that the structure distributor `C` is to be divided by `k` relative to equation `(I)` and then prints `(B2)` with a visible `+ C` term.

- `HT-F-1982-QNUM`: defines the 1982 structure distributor `C`.
- `HT-F-1989-QX`: transcribes the 1989 prose rule and the visible `(B2)` expression.
- `OCR-1989-QX__critic.md`: explicitly keeps the `C/k` prose rule separate from the visible `(B2)` equation.

This supports treating `C/k` as a model-versioned definition of the distributor used by `(B2)`, not as an edit to the source-visible formula.

## Residual Risk

The source does not introduce a new symbol such as `C_1989`; that is our implementation name. The name is required to prevent silent double division or accidental reuse of the 1982 distributor.

## Critic Check

A read-only Critic check accepted this decision with these guardrails:

- keep the visible source form as `+ C`;
- use `C_1989 = C_1982 / k` only in normalized implementation;
- never divide `C_1989` by `k` again;
- keep 1982 and 1989 `q_x` implementations versioned separately.

