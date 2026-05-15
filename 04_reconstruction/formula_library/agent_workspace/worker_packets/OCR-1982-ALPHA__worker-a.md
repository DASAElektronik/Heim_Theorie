# OCR-1982-ALPHA Worker a

## Scope

- Formula ID: HT-F-1982-ALPHA
- Image pages: 1982_massenformel/page-03.png; 1982_massenformel/page-04.png
- OCR lines: 117-147
- Queue note: `TASK_QUEUE.csv` currently lists `128-145`, but the source block continues through the `Kürzung` line at OCR 147, so that range is incomplete for the current canonical target.

## Transcription

```text
η = π/(π^4 + 4)^(1/4)
η_kq = π/[π^4 + (4+k)q^4]^(1/4)
ϑ = 5 η + 2 √η + 1
A1 = √η_11 (1 - √η_11)/(1 + √η_11)
A2 = √η_12 (1 - √η_12)/(1 + √η_12)

Feinstrukturkonstante:
α √(1 - α^2) = 9ϑ (1 - A1 A2) / (2π)^5, α > 0.

Lösung: α_(+) (positiver Zweig) und α_(-) (negativer Zweig).

Numerisch:
α_(+)^-1 = 137,03596147
α_(-)^-1 = 1,00001363

Kürzung:
α_(+) = α, α_(-) = β ≈ 137 α.
```

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| page 03 / OCR 118 | `η = π/(π^4 + 4)^(1/4)` | 0.95 | Image shows a fourth power on `π` and a fourth-root exponent; OCR line flattens the typography. |
| page 03 / OCR 119 | `η_kq = π/[π^4 + (4+k)q^4]^(1/4)` | 0.93 | The `q4` grouping is a fourth power of `q`, not a literal `q4` token. |
| page 03 / OCR 121-122 | `η_11` and `η_12` as subscripts | 0.84 | Tight typography makes the indices easy to flatten; image reads as subscripted two-digit indices. |
| page 04 / OCR 139 | `9ϑ` in the coefficient | 0.88 | The symbol after `9` matches the same vartheta-like glyph used above; not `99`. |
| page 04 / OCR 141 | `α_(+)` and `α_(-)` | 0.96 | Branch names are printed with parenthesized subscripts, not `alpha_plus/minus`. |
| page 04 / OCR 143-144 | `α_(+)^-1` and `α_(-)^-1` | 0.97 | The numeric lines use reciprocal notation with superscript `-1`, not a dash following the term. |
| page 04 / OCR 147 | `β` | 0.62 | The glyph is beta-like but can be confused with `ß` in this scan. |

## Ambiguities

- Page 04 line 139: the coefficient is read as `9ϑ`, but the vartheta-like glyph is visually close to a second `9`.
- Page 04 line 147: the final symbol in `α_(-) = β ≈ 137 α` is ambiguous between `β` and `ß`.
- Page 03 lines 121-122: the `η_11` and `η_12` indices are compressed enough that a flat `η11`/`η12` reading is possible from OCR alone.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `η = π/(π4 + 4)1/4` | `η = π/(π^4 + 4)^(1/4)` | page 03 | 118 |
| `ηkq = π/[π4 + (4+k)q4]1/4` | `η_kq = π/[π^4 + (4+k)q^4]^(1/4)` | page 03 | 119 |
| `A1 = √η11 (1 - √η11)/ (1 + √η11)` | `A1 = √η_11 (1 - √η_11)/(1 + √η_11)` | page 03 | 121 |
| `A2 = √η12 (1 - √η12)/ (1 + √η12)` | `A2 = √η_12 (1 - √η_12)/(1 + √η_12)` | page 03 | 122 |
| `α√(1- α2) = 9ϑ (1 - A1A2) / (2π)5, α>0.` | `α √(1 - α^2) = 9ϑ (1 - A1 A2) / (2π)^5, α > 0.` | page 04 | 139 |
| `Lösung: α(+) (positiver Zweig) und α(-) (negativer Zweig).` | `Lösung: α_(+) (positiver Zweig) und α_(-) (negativer Zweig).` | page 04 | 141 |
| `α(+) - 1 = 137,03596147` | `α_(+)^-1 = 137,03596147` | page 04 | 143 |
| `α(-) - 1 = 1,00001363` | `α_(-)^-1 = 1,00001363` | page 04 | 144 |
| `α(+) = α ,             α(-) = ß ≈ 137 α .` | `α_(+) = α, α_(-) = β ≈ 137 α.` | page 04 | 147 |

## Do Not Integrate Yet

- Do not update the canonical target from the queue range alone; OCR 147 is required to capture the `Kürzung` line.
- Do not pull in the later `B) Massenspektrum` block or formulas `VI/VII/VIII` from page 04.
- Treat the `β/ß` glyph on OCR 147 as unresolved unless the image is rechecked at higher resolution.
