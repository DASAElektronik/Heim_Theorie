# OCR-1989-QX Critic Review

verdict: `critic_ready`

## Accepted source-visible transcription

```text
Der Strukturdistributor C (Strangeness) ist neu gegenüber Gl. (I) in Kapitel E durch k zu dividieren.

Einer der Winkel α_Q, durch den die Zeithelizität ε definiert wird, lautet:
α_Q = π Q [Q + (P/2)]                                               (B1)

Der Ausdruck für die Ladungsquantenzahl heißt anstelle von (II) jetzt:
q_x = ½ [ (P - 2x + 2) [1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ]  (B2)

Alle übrigen Konstanten sind in (I) definiert.
```

For B1, `(P/2)` is an acceptable compact transcription of the visibly stacked `P` over `2`; keep the stacked-source risk explicit.

## Required canonical edits

- Change `qx` to `q_x`.
- Replace ASCII/expanded symbols with source-visible glyphs where the canonical layer permits it: `½`, `κ`, `ε`.
- Remove explicit multiplication stars from the raw source transcription of B2.
- Record B1 as source-visible context for this packet, but do not merge it into B2.
- Keep the C/k prose rule separate from B2; it is a source note about `C`, not an inline rewrite of the B2 equation.

## Unresolved normalization risks

- B1's stacked `P` over `2` must not be normalized to `2P`; whether the canonical encoding is `P/2`, `\frac{P}{2}`, or a Heim-specific notation remains a normalization choice.
- The source distinguishes Greek `κ` from Latin `k`; implementation must not collapse them.
- The C/k rule is source-visible but its downstream algebraic application is not shown inside B2.

## Implementation red flags

- Do not apply the C/k division by editing the visible `+ C` term in B2 unless a later canonical rule explicitly requires that derived form.
- Do not treat OCR `2P` as confirmed source text for B1.
