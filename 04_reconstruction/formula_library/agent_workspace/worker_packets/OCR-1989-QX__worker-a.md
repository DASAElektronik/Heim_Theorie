# OCR Source Check: HT-F-1989-QX

Verdict: `conflict`

Image page(s) used:
- `07_outputs/source_check_images/1989_erweiterte_massenformel/page-02.png`

Source-visible transcription:
- C/k note: `Der Strukturdistributor C (Strangeness) ist neu gegenüber Gl. (I) in Kapitel E durch k zu dividieren.`
- B1: `Einer der Winkel α_Q, durch den die Zeithelizität ε definiert wird, lautet:`
  `α_Q = π Q [Q + ( P`
  `              2 )] (B1)`
- B2: `Der Ausdruck für die Ladungsquantenzahl heißt anstelle von (II) jetzt:`
  `q_x = ½ [ (P - 2x + 2) [1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ] (B2)`
- trailing constants sentence: `Alle übrigen Konstanten sind in (I) definiert.`

OCR corrections vs current formula file `04_reconstruction/formula_library/formulas/HT-F-1989-QX.md`:
- `qx` should be `q_x`.
- `1/2 *` should be `½` with no explicit multiplication star.
- `kappa` should be `κ`.
- `epsilon` should be `ε`.
- The source page also includes the C/k prose note before B1; it is not part of B2 and should stay as a separate note, not folded into the equation text.
- The current formula file only captures B2; B1 is source-visible context and should not be inferred from the B2 entry.
- The current audit note overstates the page by implying the C/k instruction must be represented inside the 1989 model body; the page shows it as prose on the source page.

Unresolved glyph/notation risks:
- The stacked `P` over `2` in B1 is visually ambiguous. OCR rendered it as `2P`, but the source is not plain `2P`; it may be a fraction-like or special Heim notation.
- `C` vs `k` remains a prose instruction, not an inline formula mutation in B2. Implementation should treat it as a separate source note unless a later canonical rule says otherwise.
- Greek glyphs `κ` and `ε` are visually present; ASCII fallback is lossy.

Implementation implication, not normalized:
- Keep the C/k instruction separate from the B2 equation text.
- Preserve the stacked `P`/`2` glyph in B1 as an unresolved notation item until the canonical encoding rule is confirmed.
