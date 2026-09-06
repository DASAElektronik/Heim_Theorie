# H015 archive scan: historical exponent reading (2026-09-06)

## Scope and source status

This is a literal, visual reading of the local archival scan
`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`
(H015), SHA-256
`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.
The checked full-page images are:

- `tmp/pdfs/alpha3_origin/desy-39.png` — PDF 39, printed `- 4 -`;
- `tmp/pdfs/alpha3_origin/desy-40.png` — PDF 40, printed `- 4a -`;
- `tmp/pdfs/alpha3_origin/desy-41.png` — PDF 41, printed `- 5 -`;
- `tmp/pdfs/alpha3_origin/desy-42.png` — PDF 42, printed `- 6 -`;
- `tmp/pdfs/alpha3_origin/desy-43.png` — PDF 43, printed `- 7 -`.

The scan itself has no printed equation labels `(XIV)` or `(XXVI)` on
these pages. Those labels below name structurally corresponding locations
in separately inspected H006; they are not retrospective H015 labels.

PDF 43 / printed 7 visibly carries `NORTHEIM den 25.2.1982`, a signature
mark, and `(Heim)`. This records the visible date/signature line of the
scan; it does not establish chain of custody or prove authorship of every
page. The PDF's 2026 OCR/PDF metadata records digital processing, not the
date of the typescript.

## Independent transcription: exponent term

On PDF 39 / printed 4, under **"Auswahlregel der
Konfigurationszonenbesetzungen"**, the fourth term is set as:

```text
exp[ ((1 - 2 k) / (3 Q4)) (n4 + Q4) ] .
```

The fraction bar lies under `1 - 2k` and over `3 Q4`; the following
`(n4+Q4)` is outside that fraction. Its literal product is therefore
`((1-2k)(n4+Q4))/(3Q4)`.

The basis-increment line on the same page has the special `n_j=0` term
`exp[(1-2k)/3]`. It helps identify the symbols, but does not separately
define the general fourth-zone exponent. PDF 40 / printed 4a is an
*Anmerkung zu Seite 4, Zeile 9 bis Zeile 12* about `w(1)`, `w(2)`, and
`0^0`; it does not change this exponential term.

On PDF 41 / printed 5, the `N=0` sentence (`Im Fall N=0 wird f=0`) repeats:

```text
... + exp[ ((1 - 2 k) / (3 Q4)) (n4 + Q4) ] = W_vx .
```

PDF 42 / printed 6 repeats the same grouping in the staged `W2` and `W3`
relations; PDF 43 / printed 7 repeats it in the resonance-bound relation.
Thus the reading is corroborated by several H015 occurrences.

## Narrow comparison to H006

Only after that transcription, H006 was visually checked at
`tmp/pdfs/n0_alias/h006-06.png` (printed 6) and
`tmp/pdfs/n0_alias/h006-08.png` (printed 8).

| location | literal exponent typography / normalized reading |
| --- | --- |
| H015 PDF 39 / print 4 | `((1-2k)/(3Q4))(n4+Q4)` |
| H015 PDF 41 / print 5 | `((1-2k)/(3Q4))(n4+Q4)` |
| H006 print 6, `(XIV)` | printed line: `1-2k(n4+Q4)/3Q4`; existing explicit normalization: `1 - 2k(n4+Q4)/(3Q4)` |
| H006 print 8, `(XXVI)` | `((1-2k)(n4+Q4))/(3Q4)` |

The isolated `1` in H006 `(XIV)` is **not** printed in a numerator
parenthesis. On the stated H006 normalization, the H015 occurrences agree
with H006 `(XXVI)`, but not with that H006 `(XIV)` reading. This is solely
a bounded text/edition observation: it identifies neither a cause for the
difference nor an authorized correction of any edition.

## Limits

No mass calculation, parameter choice, empirical comparison, or claim that
one expression was intended in every historical version was made here. The
scan's formula appearance is not a proof of the selection rule's validity.
