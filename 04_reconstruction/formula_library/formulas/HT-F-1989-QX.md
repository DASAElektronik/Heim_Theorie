# HT-F-1989-QX: 1989 Modified Charge Number

## Source-Visible Transcription

The source states the 1989 correction to the structure distributor as prose:

```text
Der Strukturdistributor C (Strangeness) ist neu gegenüber Gl. (I) in Kapitel E durch k zu dividieren.
```

The same source block gives the angle definition:

```text
α_Q = π Q [Q + (P/2)]                                               (B1)
```

`(P/2)` is a compact transcription of the visibly stacked `P` over `2`; normalization decision `NORM-STACKED-BINOMIAL` maps this notation to `choose(P, 2)` for implementation.

The modified charge-number expression is:

```text
q_x = ½ [ (P - 2x + 2) [1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ]  (B2)
```

The source then states:

```text
Alle übrigen Konstanten sind in (I) definiert.
```

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt`
- Lines: 61-66

## Dependencies

- `HT-F-1982-QNUM`

## Outputs

- `q_x`

## Current Status

`source_checked`

## Audit Notes

- Source-checked against `1989_erweiterte_massenformel/page-02.png` by two worker packets plus Critic review.
- The `C/k` instruction is printed as prose before `(B1)` and stays separate from the visible `+ C` source transcription in `(B2)`.
- Normalization decision `NORM-1989-QX-C-OVER-K` defines `C_1989 = C_1982 / k`; the normalized 1989 `(B2)` implementation uses `+ C_1989` without rewriting the source transcription to `+ C/k`.
- OCR rendered the stacked `(P/2)` glyph in `(B1)` as `2P`; the image supports stacked `P` over `2`, not plain `2P`.
- The source distinguishes Greek `κ` from Latin `k`; implementation must preserve that distinction.

## Risks

- This formula modifies the 1982 charge expression.
- A mixed 1982/1989 implementation would be invalid unless explicitly versioned.
- The canonical encoding of the stacked `P` over `2` in `(B1)` is resolved by `NORM-STACKED-BINOMIAL`.
- The 1989 `C/k` rule is resolved by `NORM-1989-QX-C-OVER-K`; code must prevent double division of `C_1989`.
