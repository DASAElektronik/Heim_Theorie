Verdict: conflict

Image page(s) used: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-09.png`

Accepted source-visible transcription
```text
3. Die Sommerfeld-Feinstrukturkonstante:

In ϕ und ß(0) ist die Feinstrukturkonstante α enthalten. Der in Kapitel D (Abschnitt 8)
berechnete Wert ist noch mit einem geringen Fehler behaftet. Heim gibt nun auch die genaue
Formel dafür an:

Nach Gl.8.21/Kapitel D ist mit C → C ':

α √(1-α²) = 9ϑ / (2π)⁵ · (1 - C')                               (B58)

oder

1 - C' = 1 - (1 + η₂,₂)/(ηη₁,₁η₁,₂) · ((1 - √η)/(1 + √η))² = Kα   (B59)

Für das reziproke Quadrat dieser Lösungen ergibt sich:

α(±)^-2 = ½ D'² (1 ± √(1 - 4 / D'²))                           (B60)

mit der Kürzung        D' = (2π)⁵ / (9ϑKα).                    (B61)

Mit (Gl.V Kapitel E)) ergibt sich dann für die beiden Zweige:

α(+) = 0.0072973525253328589 und α(-) = 0.999985890199089      (B62)
b.z.w.
1/α(+) = 137,03601,             1/α(-) = 1,0000142

was verglichen mit dem experimentellen Wert für die Feinstrukturkonstante (Nistler &
Weirauch 2002)
1/α+ = 137,0360114 ± 3.4 .10 - 8

einen Wert ergibt, der im Toleranzbereich der neuesten Messung liegt. Der negative Zweig
gibt eine starke Wechselwirkung an, die wahrscheinlich auf die inneren Bindungen der 4
Zonen in den Elementarteilchen zurückgeführt werden muß. Doch hat Heim noch keine
weiteren Untersuchungen dazu durchgeführt.
```

OCR corrections vs current formula file
- B58 numerator: source has `9ϑ` in the prefactor, not the normalized `9 * theta`; keep `C'` explicit.
- B59 relation: current file collapses this to `1 - K_alpha`; source keeps the full displayed fraction and only then ends at `= Kα`.
- B60 radical/branch notation: source is `α(±)^-2 = ½ D'^2 (1 ± √(1 - 4 / D'^2))`; current file’s generic `alpha_pm^(-2)` is acceptable as normalization, but the source branch notation is not.
- B61 denominator: source reads `D' = (2π)^5 / (9ϑKα)`; current file’s `9 * theta * K_alpha` loses the source glyph and spacing.
- B62 decimal/comma values: source uses comma decimals in the reciprocal line and a separate experimental comparison line; current file only keeps the branch values with dot decimals.

Unresolved glyph/notation risks
- `C'` vs `C’`: apostrophe style is visually fragile in the scan.
- Eta subscripts in B59: `η₂,₂`, `η₁,₁`, `η₁,₂` are legible but OCR-fragile.
- B59 scope: whether readers parse `= Kα` as attached to the whole displayed fraction or as a definition of the inner term should be kept explicit.
- Reciprocal branch notation: `α(±)`, `α(+)`, `α(-)`, and the later `1/α+` comparison line are distinct in the source and should not be merged.
- Post-1989 comparison context: the Nistler & Weirauch 2002 comparison belongs in the source-note layer, not in the formula core.

Implementation implications
- Do not update canonical formula/catalog/queue files from this packet.
- If this is later implemented, preserve the source-visible B59/B61 structure and keep the comparison block separate from the formula entry.
