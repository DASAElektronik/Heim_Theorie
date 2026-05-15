# OCR-1989-ALPHA Worker a

## Verdict

`conflict`

## Source Used

- Image page: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-09.png`
- OCR source: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt` lines 449-483
- Current formula file: `04_reconstruction/formula_library/formulas/HT-F-1989-ALPHA.md`

## Accepted Source-Visible Transcription

```text
3. Die Sommerfeld-Feinstrukturkonstante:

In φ und β(0) ist die Feinstrukturkonstante α enthalten. Der in Kapitel D (Abschnitt 8)
berechnete Wert ist noch mit einem geringen Fehler behaftet. Heim gibt nun auch die genaue
Formel dafür an:

Nach Gl.8.21/Kapitel D ist mit C → C':
    α √(1 - α^2) = 9ϑ/(2π)^5 (1 - C')                              (B58)

oder
    1 - C' = 1 - ((1 + η_{2,2})/(η η_{1,1} η_{1,2})) ((1 - √η)/(1 + √η))^2 = K_α   (B59)

Für das reziproke Quadrat dieser Lösungen ergibt sich:

    α_(±)^-2 = 1/2 D'^2 (1 ± √(1 - 4 / D'^2))                    (B60)

mit der Kürzung
    D' = (2π)^5 / (9ϑ K_α).                                      (B61)

Mit (Gl. V Kapitel E)) ergibt sich dann für die beiden Zweige:

    α_(+) = 0.0072973525253328589 und α_(-) = 0.999985890199089   (B62)
b.z.w.
    1/α_(+) = 137,03601,      1/α_(-) = 1,0000142

was verglichen mit dem experimentellen Wert für die Feinstrukturkonstante (Nistler &
Weirauch 2002)
    1/α_+ = 137,0360114 ± 3.4·10^-8
```

## OCR Corrections vs Current Formula File

- OCR source line 450 reads `ß(0)`; the image reads `β(0)`.
- B58: source uses `9ϑ/(2π)^5`, not the normalized `9 * theta / (2 pi)^5`.
- B59: source is `1 - C' = 1 - (...) = K_α`; the current file collapses this to `1 - C' = 1 - K_alpha`, which drops the full bracketed term.
- B60: source keeps the branch notation on alpha itself, `α_(±)^-2`, with a literal radical `√(1 - 4 / D'^2)`.
- B61: source denominator is `9ϑ K_α`; the current file normalizes this to `9 * theta * K_alpha`.
- B62: source uses decimal commas and explicit branches `α_(+)` / `α_(-)`; the current file rewrites them as `alpha_plus` / `alpha_minus` and period decimals.
- Reciprocal lines: source has `1/α_(+)` and `1/α_(-)`, plus the post-1989 comparison `1/α_+ = 137,0360114 ± 3.4·10^-8`.

## Unresolved Glyph / Notation Risks

- B58 coefficient: the page reads as `9ϑ`, but the glyph is tight enough to be misread as a doubled `9` in poor OCR.
- `C'` and `D'`: primes are visible, but OCR can flatten them.
- `η` subscripts: `η_{2,2}`, `η_{1,1}`, `η_{1,2}` are cramped; the comma/subscript grouping needs care.
- B59 structure: the source reads as an equality chain ending in `= K_α`; it is not safe to reduce this to a simple definition `1 - K_alpha`.
- Branch notation: keep `α_(+)` / `α_(-)` and their reciprocals distinct from any `alpha_plus/minus` normalization.
- Comparison context: the `Nistler & Weirauch 2002` line is a later comparison, not part of the 1989 formula derivation.

## Implementation Implications

- Do not rewrite the canonical formula file from this packet.
- If this is integrated later, preserve the source glyph forms first, then decide separately whether any normalized working form belongs in a downstream representation.
