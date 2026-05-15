# NORM-STACKED-BINOMIAL

Date: 2026-05-15

Decision IDs resolved:

- `NORM-1982-QNUM-002`
- `NORM-1989-QX-001`

## Decision

The visible stacked parenthesis notation with an upper symbol and lower integer is normalized for implementation as a binomial coefficient:

- source `(P over 2)` -> `choose(P, 2)`
- source `(P over 3)` -> `choose(P, 3)`
- source `(Q over 3)` -> `choose(Q, 3)`

It must not be normalized as division (`P/2`, `P/3`, `Q/3`) and must not be inverted as `choose(2, P)` or `choose(3, P)`.

## Evidence

The source images show a parenthesized vertical stack, not a horizontal fraction bar or slash.

- `1982_massenformel/page-03.png`: `alpha_P` and `alpha_Q` use `(P over 2)`.
- `1982_massenformel/page-06.png`: the selection block repeats the same notation as `(P over 2)`, `(P over 3)`, and `(Q over 3)`.
- `1989_erweiterte_massenformel/page-02.png`: `(B1)` repeats `(P over 2)` in the same notation class.

The repetition across `P` and `Q`, and across lower integers `2` and `3`, makes quotient normalization less defensible than binomial normalization.

## Implementation Rule

Use a single helper in code, for example `choose(n, r)`, with the visible source stack order:

```text
upper source glyph -> first argument
lower source glyph -> second argument
```

Examples:

```text
(P over 2) -> choose(P, 2)
(P over 3) -> choose(P, 3)
(Q over 3) -> choose(Q, 3)
```

## Scope

This decision applies to source-checked stacked parenthesis notation in:

- `HT-F-1982-QNUM`
- `HT-F-1982-SELECTION-WVX`
- `HT-F-1989-QX`

It does not decide any unrelated stacked fraction or line-wrap notation, especially the high-risk 1989 `FPHI` fraction structures.

## Residual Risk

A Heim-specific private convention is theoretically possible, but no contrary local evidence has been found. If later primary text explicitly defines the stacked notation differently, this decision must be reopened.

## Critic Check

A read-only Critic check accepted this decision. Remaining implementation caution: preserve stack order exactly and do not let OCR forms such as `2P` or `( 2P )` overwrite the image-backed reading.

