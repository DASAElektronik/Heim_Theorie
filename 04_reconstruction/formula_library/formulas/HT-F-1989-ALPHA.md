# HT-F-1989-ALPHA: 1989 Exact Fine-Structure Constant

## Source-Visible Transcription

Introductory source context:

```text
In φ und β_(0) ist die Feinstrukturkonstante α enthalten.
```

The source formula block is:

```text
α sqrt(1 - α^2) = 9ϑ/(2π)^5 (1 - C')                               (B58)

1 - C' =
  1 - ((1 + η_{2,2})/(η η_{1,1} η_{1,2}))
      ((1 - sqrt(η))/(1 + sqrt(η)))^2
  = K_α                                                            (B59)

α_(±)^-2 = 1/2 D'^2 (1 ± sqrt(1 - 4 / D'^2))                        (B60)

D' = (2π)^5 / (9ϑK_α).                                              (B61)
```

For the two branches the source gives:

```text
α_(+) = 0.0072973525253328589 und α_(-) = 0.999985890199089         (B62)
b.z.w.
1/α_(+) = 137,03601,      1/α_(-) = 1,0000142
```

The source then compares against a later measurement:

```text
1/α_+ = 137,0360114 ± 3.4 · 10^-8
```

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt`
- Lines: 449-483
- Original labels: `(B58)` to `(B62)`

## Outputs

- `alpha_plus`
- `alpha_minus`

## Current Status

`source_checked`

## Audit Notes

- Source-checked against `1989_erweiterte_massenformel/page-09.png` by two worker packets plus Critic review.
- OCR `ß(0)` is corrected to source-visible Greek `β_(0)`.
- `(B58)` uses source-visible coefficient `9ϑ/(2π)^5`; do not read this as `99`.
- `(B59)` must preserve the full equality chain. The old shortcut `1 - C_prime = 1 - K_alpha` is structurally wrong.
- `(B60)`/`(B62)` use compact branch notation `α_(±)`, `α_(+)`, and `α_(-)` in the source layer.
- `(B61)` denominator is `9ϑK_α`.
- `NORM-1989-ALPHA-BRANCH-ALIASES` requires model-scoped numeric names such as `alpha_plus_1989` and `alpha_minus_1989`.
- `NORM-1989-ALPHA-VARTHETA-NAME` keeps `vartheta` as the canonical implementation name for the visible theta-like glyph.
- The 2002 Nistler & Weirauch comparison is source context only. It is not historical proof for a 1989 prediction.

## Risks

- `K_α` scope in `(B59)` is normalization-sensitive.
- `α_(+)`/`α_(-)` and later `α_+` are visibly distinct source notations and must not be silently merged.
- Decimal commas in reciprocal/comparison lines are parsed by `NORM-1989-DECIMAL-COMMAS` if used numerically.
- The comparison target is post-1989.
- Possible mismatch between alpha in 1982, 1989, XLSM and implementation outputs.
