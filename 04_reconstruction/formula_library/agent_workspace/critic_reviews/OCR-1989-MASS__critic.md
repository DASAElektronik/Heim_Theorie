# OCR-1989-MASS Critic Review

verdict: `critic_ready`

## Accepted source-visible transcription

```text
1. Die Massen der Grundzustände und der angeregten Zustände der Elementarteilchen

Die modifizierte Massenformel der Elementarteilchen setzt sich - anders als in (XII)
aus folgenden Anteilen zusammen:

M = µα+ [(G + S + F + Φ) + 4 q α_-]                                  (B3)

Die Anteile G und S lauten wie G und K in (XII) (wobei jetzt n, m, p, σ anstelle von n1, n2,
n3 und n4 geschrieben werden), µ ist das Massenelement wie in (VI). Die Konstanten α±
haben die Gestalt:

α+ = ⁶√η / η² (1 - ϑ [2(1 - √η) / η(1 + √η)]² √2η) - 1,
α_- = (α+ + 1)η - 1                                                  (B4)

Die Rechenergebnisse für α+ und α_- in (B4) stehen in Tabelle VI/Kapitel G.
```

B3 is confidently `M = µα+ [(G + S + F + Φ) + 4 q α_-] (B3)`. B4 should be recorded as context/dependency for the alpha constants, not normalized inside the mass formula body.

## Required canonical edits

- Replace ASCII placeholders in B3 with source-visible symbols: `µ`, `α+`, `Φ`, `α_-`.
- Remove explicit multiplication stars from the raw source transcription.
- Remove the uncertainty note around the final B3 term; the source supports `4 q α_-`.
- Keep `HT-F-1989-MASS` focused on B3 and link B4 as dependency/context via the alpha-constant record.

## Unresolved normalization risks

- B4 is dense and should not be over-normalized in this mass record; radical degree, denominator scope, bracket-square scope, and trailing `√2η` grouping need a dedicated alpha-constant check.
- The source uses juxtaposition for multiplication; any inserted operators are implementation notation, not source transcription.
- The green table sentence is context for evaluated constants, not part of the mass formula body.

## Implementation red flags

- Do not fold B4 into the normalized mass formula body.
- Do not let spreadsheet or later program conventions override the source-visible B3 bracket structure.
