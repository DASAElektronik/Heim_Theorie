# OCR-1982-MASS Worker B

## Scope

- Formula ID: HT-F-1982-MASS
- Image pages: 07_outputs/source_check_images/1982_massenformel/page-05.png
- OCR lines: 222-224

## Transcription

```text
Einheitliches Massenspektrum:

M = µα+ (K + G + H + Φ)                                 (XII)
```

Source notes:
- The formula line is red in the image.
- `G` is underlined in the source image.
- The heading is included only as context; the preceding `Φ` block and the later selection-rule prose are excluded from this packet.

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| Formula line, left side | `µ` | 0.98 | Page 05 image shows a Greek mu in the multiplier position; OCR line 224 uses the same glyph. |
| Formula line, after `µ` | `α+` | 0.62 | The source image shows alpha followed by a plus glyph; placement of the plus is not fully stable at this resolution, so I keep it as-is rather than normalizing. |
| Sum term inside parentheses | `G` underlined | 0.99 | The underline is visible in the image and is not preserved by OCR line 224. |
| Right margin label | `(XII)` | 0.99 | The label is clearly visible on page 05 and matches OCR line 224. |

## Ambiguities

- The `α+` cluster is not fully crisp in the source image. It may read as baseline `α+` or a subscripted plus placement, but I did not infer beyond what is visible.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `Einheitliches Massenspektrum:` | `Einheitliches Massenspektrum:` | page-05.png | 222 |
| `M = µα+ (K + G + H + Φ)                                 (XII)` | `M = µα+ (K + <u>G</u> + H + Φ)                                 (XII)` | page-05.png | 224 |

## Do Not Integrate Yet

- Keep this packet limited to the page-05 heading and the central unified mass spectrum expression `(XII)`.
- Do not pull in the surrounding `Φ` formula block or the later selection-rule prose from adjacent pages.
