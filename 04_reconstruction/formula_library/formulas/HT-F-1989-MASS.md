# HT-F-1989-MASS: 1989 Modified Mass Formula

## Source-Visible Transcription

The source introduces the modified mass formula as:

```text
Die modifizierte Massenformel der Elementarteilchen setzt sich - anders als in (XII)
aus folgenden Anteilen zusammen:
```

The source-visible formula is:

```text
M = µα+ [(G + S + F + Φ) + 4 q α_-]                                  (B3)
```

The line after `(B3)` states that `G` and `S` correspond to `G` and `K` in `(XII)`, with `n, m, p, σ` now written instead of `n1, n2, n3, n4`; `µ` remains the mass element from `(VI)`.

The adjacent `(B4)` alpha-constant definition is context/dependency for the alpha branches, not part of the normalized mass-formula body in this record. `NORM-1989-MASS-B4-DEPENDENCY-SCOPE` resolves the mass-record boundary: `HT-F-1989-MASS` consumes `alpha_plus_1989` and `alpha_minus_1989`, while executable alpha computation remains delegated to `NORM-1989-ALPHA-001`.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt`
- Lines: 70-87
- Source document: `Erweiterte_Massenformel_Nach_Heim_1989.pdf`.

## Dependencies

- `HT-F-1982-MU`
- `HT-F-1989-FPHI`
- `HT-F-1989-QX`
- `HT-F-1989-ALPHA`

## Current Status

`source_checked`

## Audit Notes

- Source-checked against `1989_erweiterte_massenformel/page-02.png` by two worker packets plus Critic review.
- The final `(B3)` term is image-confirmed as `4 q α_-`; the previous OCR uncertainty is resolved for visible transcription.
- The source uses juxtaposition for multiplication. Explicit operators may be introduced only in a later implementation notation, not in the source transcription.
- `(B4)` is dense and remains delegated to alpha-chain normalization; this mass record links it as context/dependency only.
- The source introduction explicitly says parts of the 1989 formulas were reprogrammed later and that missing brackets had to be estimated. This formula must therefore stay versioned separately from 1982.
- `NORM-1989-MASS-VERSIONING` requires separate `model_1982_from_text` and `model_1989_extension` implementations.

## Risks

- `(B4)` radical degree, denominator scope, bracket-square scope, and trailing `√2η` grouping are not implemented by this mass record; executable alpha computation remains under `NORM-1989-ALPHA-001`.
- Missing bracket corrections elsewhere in the 1989 source may be later inference rather than Heim text.
- We need to compare against the spreadsheet formulas but not treat spreadsheet logic as primary.
