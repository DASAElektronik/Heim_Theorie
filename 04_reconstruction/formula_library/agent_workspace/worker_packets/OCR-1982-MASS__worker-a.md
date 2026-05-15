# OCR-1982-MASS Worker a

## Scope

- Formula ID: OCR-1982-MASS / (XII)
- Image pages: `07_outputs/source_check_images/1982_massenformel/page-05.png`
- OCR lines: 222-224

## Transcription

```text
Einheitliches Massenspektrum:

M = µα+ (K + G + H + Φ)                                   (XII)
```

Source formatting notes: the formula is printed in red in the image; `G` is underlined in the source; `(XII)` is set at the far right.

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| `M` at formula start | `M` | high | Matches the image and OCR line 224. |
| `µ` before `α+` | Greek mu (`µ`) | high | Source glyph is mu, not `m` or `u`; OCR line 224 also reads `µ`. |
| `α+` after `µ` | `α+` | medium | The plus is attached to alpha in the source; exact baseline/subscript placement is visually tight. |
| `K + G + H + Φ` | `K + G + H + Φ` | high | Parenthesized sum matches the source layout. |
| `G` in the sum | underlined `G` | medium | The `G` is visibly underlined in the image. |
| label at right | `(XII)` | high | The label is present on the right of the formula line in the source image and OCR text. |

## Ambiguities

- The `α+` glyph is visually close to a plain `α+` in plain text, but the source placement leaves its exact subscript/superscript intent ambiguous.
- The underlined `G` is clear as formatting in the image, but its semantic weight is unclear and should not be normalized here.
- The source uses a Greek mu glyph; OCR workflows may confuse it with `m` or `u`, so that character should stay explicit as `µ`.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `M = µα+ (K + G + H + Φ) (XII)` | Same formula content, with source formatting notes: red formula text, underlined `G`, and `(XII)` aligned at the right margin | 05 | 224 |

## Do Not Integrate Yet

Do not promote this to the canonical formula file until the `α+` glyph placement and the underlined `G` formatting are confirmed against the source image.
