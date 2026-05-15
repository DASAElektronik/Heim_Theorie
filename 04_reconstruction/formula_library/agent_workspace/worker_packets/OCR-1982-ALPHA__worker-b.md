# OCR-1982-ALPHA Worker b

## Scope

- Formula ID: HT-F-1982-ALPHA
- Image pages: `1982_massenformel/page-03.png`; `1982_massenformel/page-04.png`
- OCR lines: 117-147
- Queue note: `TASK_QUEUE.csv` currently lists `128-145`, which is incomplete for the current canonical `HT-F-1982-ALPHA.md` because it omits the page-03 abbreviation block and the Kürzung line at OCR 147.

## Transcription

```text
η = π/(π^4 + 4)^(1/4)
η_{kq} = π/[π^4 + (4+k)q^4]^(1/4)
ϑ = 5 η + 2 √η + 1                                                                  (V)
A1 = √η_11 (1 - √η_11)/ (1 + √η_11)
A2 = √η_12 (1 - √η_12)/ (1 + √η_12)

Plancksche Konstante: ħ = h/2π, Lichtgeschwindigkeit: c = (ε0µ0)^-1/2, Wellenwiderstand
des leeren R3 (elektromagnetisch): R_- = cµ0, mit ε0 und µ0 Konstanten der Influenz und
Induktion.

Elektrische Elementarladung: e± = 3C± mit

C± = ± √(2ϑh / R_-) / (4π)^2        (evtl. elektr. Quarkladung ?)

Feinstrukturkonstante: α√(1 - α^2) = [ambiguous coefficient]ϑ (1 - A1A2) / (2π)^5, α > 0.

Lösung: α_(+) (positiver Zweig) und α_(-) (negativer Zweig).

Numerisch: α_(+)^-1 = 137,03596147
           α_(-)^-1 = 1,00001363

Was bedeutet diese starke Kopplung α_(-) ?
Kürzung: α_(+) = α , α_(-) = β/ß ≈ 137 α .

Boundary only: next section begins `B) Massenspektrum der Grundzustände und ihrer Resonanzen`.
```

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| page 03, OCR 118 | `η = π/(π^4 + 4)^(1/4)` | 0.96 | The OCR loses the exponent formatting; the page shows the fourth power and fourth-root structure. |
| page 03, OCR 119 | `η_{kq} = π/[π^4 + (4+k)q^4]^(1/4)` | 0.96 | The subscript and all exponents are visible on the page; OCR flattens them. |
| page 03, OCR 121-122 | `η_11` / `η_12` | 0.94 | The page uses subscripted indices in both A1 and A2 definitions; OCR collapses them. |
| page 04, OCR 137 | `C± = ± √(2ϑh / R_-) / (4π)^2` | 0.74 | The radical scope is visible, but the exact bar extent is tight enough to keep as ambiguous. |
| page 04, OCR 139 | coefficient before `ϑ` | 0.55 | The printed coefficient looks ambiguous between `9` and `99`; do not resolve it from plausibility. |
| page 04, OCR 143-144 | `α(+)^-1`, `α(-)^-1` | 0.98 | The page clearly uses reciprocal notation, not subtraction by 1. |
| page 04, OCR 147 | `β/ß` | 0.60 | The Kürzung line shows a beta-like glyph; the OCR reads `ß`, so keep it ambiguous. |

## Ambiguities

- The coefficient before `ϑ` in the fine-structure equation is ambiguous on the page image.
- The `C±` radical scope is close enough to the text that it should stay marked uncertain until canonical integration.
- The Kürzung glyph on the right-hand branch is ambiguous between `β` and `ß`.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `η = π/(π4 + 4)1/4` | `η = π/(π^4 + 4)^(1/4)` | page 03 | 118 |
| `ηkq = π/[π4 + (4+k)q4]1/4` | `η_{kq} = π/[π^4 + (4+k)q^4]^(1/4)` | page 03 | 119 |
| `A1 = √η11 (1 - √η11)/ (1 + √η11)` | `A1 = √η_11 (1 - √η_11) / (1 + √η_11)` | page 03 | 121 |
| `A2 = √η12 (1 - √η12)/ (1 + √η12)` | `A2 = √η_12 (1 - √η_12) / (1 + √η_12)` | page 03 | 122 |
| `C± = ±    2ϑh / R− /(4 π)2` | `C± = ± √(2ϑh / R_-) / (4π)^2` | page 04 | 137 |
| `α√(1- α2) = 9ϑ (1 - A1A2) / (2π)5` | `α√(1 - α^2) = [ambiguous coefficient]ϑ (1 - A1A2) / (2π)^5` | page 04 | 139 |
| `α(+) - 1 = 137,03596147` | `α(+)^-1 = 137,03596147` | page 04 | 143 |
| `α(-) - 1 = 1,00001363` | `α(-)^-1 = 1,00001363` | page 04 | 144 |
| `Kürzung:           α(+) = α ,             α(-) = ß ≈ 137 α .` | `Kürzung: α(+) = α, α(-) = β/ß ≈ 137 α` | page 04 | 147 |

## Do Not Integrate Yet

Keep the canonical target unchanged until the scope is widened to include OCR 117-147, not just 128-145. The later `VI/VII/VIII` mass-spectrum constants and formulas start after the Kürzung boundary and remain out of scope for this packet.
