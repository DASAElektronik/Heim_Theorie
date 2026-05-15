# OCR-1989-QX Worker b

## Scope

- Formula ID: HT-F-1989-QX
- Image page: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-02.png`
- OCR lines: 61-66

## Verdict

ready

## Transcription

```text
Der Strukturdistributor C (Strangeness) ist neu gegenüber Gl. (I ) in Kapitel E durch k zu dividieren.

Einer der Winkel α_Q, durch den die Zeithelizität ε definiert wird, lautet:
α_Q = π Q [Q + ( P/2 )]                                                   (B1)

Der Ausdruck für die Ladungsquantenzahl heißt anstelle von (II) jetzt:
q_x = ½ [ (P - 2x + 2) [1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ] (B2)

Alle übrigen Konstanten sind in (I) definiert.
```

## OCR Corrections

| OCR text | Source reading | Note |
|---|---|---|
| `Der Strukturdistributor C (Strangeness) ist neu gegenüber Gl. (I ) in Kapitel E durch k zu` / `dividieren.` | `Der Strukturdistributor C (Strangeness) ist neu gegenüber Gl. (I ) in Kapitel E durch k zu dividieren.` | Keep the prose note separate from the equation. |
| `αQ = π Q [Q + ( 2P ) ]` | `α_Q = π Q [Q + ( P/2 )]` | Source shows stacked `P` over `2`, not `2P`. |
| `qx = 1/2 [ (P - 2x + 2) [1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ]` | `q_x = ½ [ (P - 2x + 2) [1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ]` | Preserve the subscripted output label. |
| missing | `Einer der Winkel α_Q, durch den die Zeithelizität ε definiert wird, lautet:` | Add the missing B1 lead-in. |
| missing | `Alle übrigen Konstanten sind in (I) definiert.` | Add the trailing constants sentence. |

## Unresolved Glyph / Notation Risks

- The `P/2` in `α_Q` is visually stacked in the source; do not collapse it to `2P`.
- `κ` in `q_x` is a compact Greek glyph; keep it distinct from the prose `k` in the note.
- The `C`/`k` statement reads as prose, not as an inline algebraic edit to B2.
- The output label is `q_x` in the source, but the OCR source file currently normalizes it to `qx`.

## Implementation Implications

- Keep the `C`/`k` statement as a separate source note unless a downstream reconstruction step explicitly folds it into the model.
- Treat `(B1)` as its own equation, independent of the modified charge-number line `(B2)`.
- Do not normalize the visible stacked fraction or the `q_x` subscript away when updating any derived representation.
