# OCR Source Check: HT-F-1989-MASS

Verdict: `conflict`

Image page(s) used:
- `07_outputs/source_check_images/1989_erweiterte_massenformel/page-02.png`

OCR source:
- `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt`, lines 70-87

Source-visible transcription:
- Heading/context: `1. Die Massen der Grundzustände und der angeregten Zustände der Elementarteilchen`
- Intro line: `Die modifizierte Massenformel der Elementarteilchen setzt sich - anders als in (XII) aus folgenden Anteilen zusammen:`
- B3: `M = µα+ [(G + S + F + Φ) + 4 q α_-]                                   (B3)`
- Context to B4: `Die Anteile G und S lauten wie G und K in (XII) (wobei jetzt n, m, p, σ anstelle von n1, n2, n3 und n4 geschrieben werden), µ ist das Massenelement wie in (VI). Die Konstanten α± haben die Gestalt:`
- B4: `α+ = \sqrt[6]{η}/η² (1 - ϑ [2(1 - \sqrt{η}) / η(1 + \sqrt{η})]^2 \sqrt{2η}) - 1, α_- = (α+ + 1)η - 1   (B4)`
- Green result sentence: `Die Rechenergebnisse für α+ und α- in (B4) stehen in Tabelle VI/Kapitel G.`

OCR corrections vs current formula file `04_reconstruction/formula_library/formulas/HT-F-1989-MASS.md`:
- `mu` should be `µ`.
- `alpha_plus` should be `α+`.
- `Phi` should be `Φ`.
- `alpha_minus` should be `α_-`.
- The source prints the B3 term as `4 q α_-`; no explicit `*` is visible, and the binding is only by spacing plus the surrounding brackets.
- The current formula file does not carry the printed B4 constant definition; that block should stay cross-linked to the alpha-constant record rather than being normalized into the mass line.

Unresolved glyph/notation risks:
- B4 is visually cramped. The sixth-root / denominator / bracketed-square grouping is readable in outline, but the exact nesting around `\sqrt[6]{η}`, `η²`, the bracketed ratio, and the trailing `\sqrt{2η}` factor should stay source-faithful.
- The `α±` line is clearly a paired constant definition, but it is not safe to normalize its internal grouping beyond what the page visibly shows.
- `B4` looks like shared alpha-constant context, not a mass-formula body term; implementation should treat it as a linked dependency unless the canonical schema explicitly wants the constants embedded here.

Implementation implication:
- Keep the mass record limited to B3 content and link B4 out to the alpha-constant formula record; do not fold the green table note or the alpha-constant definition into the normalized mass equation.
