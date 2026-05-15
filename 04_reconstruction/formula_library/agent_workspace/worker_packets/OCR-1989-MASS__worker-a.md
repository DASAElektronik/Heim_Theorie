# OCR Source Check: HT-F-1989-MASS

- verdict: ready
- image page(s) used: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-02.png`
- OCR source used: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt` lines 70-87
- current formula file inspected: `04_reconstruction/formula_library/formulas/HT-F-1989-MASS.md`

## Source-visible transcription

```text
1. Die Massen der Grundzustände und der angeregten Zustände der Elementarteilchen

Die modifizierte Massenformel der Elementarteilchen setzt sich - anders als in (XII)
aus folgenden Anteilen zusammen:

M = µα+ [(G + S + F + Φ) + 4 q α_-]                                    (B3)

Die Anteile G und S lauten wie G und K in (XII) (wobei jetzt n, m, p, σ anstelle von n1, n2,
n3 und n4 geschrieben werden), µ ist das Massenelement wie in (VI). Die Konstanten α±
haben die Gestalt:

α+ = 6√η / η² (1 - ϑ [ 2(1 - √η) / η(1 + √η) ]² √2η ) - 1, α_- = (α_+ + 1)η - 1    B4)

Die Rechenergebnisse für α+ und α_- in (B4) stehen in Tabelle VI/Kapitel G.
```

## OCR corrections vs current formula file

- Remove explicit `*` markers from the mass formula; the source prints juxtaposition only.
- Normalize the source-visible symbols in the record to `µ`, `α+`, `Φ`, and `α_-`.
- The B3 tail is printed as `4 q α_-`; there is no visible `alpha_minus` text and no extra binding mark beyond the surrounding brackets.
- Keep the overall B3 bracket nesting as-is; the source does not show any additional parentheses around the final product term.

## Unresolved glyph / notation risks

- B4 is visually dense: the left-hand `α+` definition contains nested radical/fraction grouping that OCR does not capture reliably.
- The `ϑ`/fraction-scope/radical-scope cluster in B4 should stay flagged until a dedicated alpha-constants record is checked.
- B4 is source-adjacent but conceptually a local alpha-constant definition; implementation should cross-link it to `HT-F-1989-ALPHA` rather than folding it into the mass-body record.

## Implementation implication

- `HT-F-1989-MASS` should stay focused on the B3 mass formula.
- Treat B4 as dependency/context for the alpha constants record, not as a separate normalized body entry here.
