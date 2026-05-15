# HT-F-1989-NEUTRINO: Neutrino Field-Mass Formula

## Source-Visible Transcription

The section starts by assuming a Euclidean metric in the central region of an elementary structure. For the mass formula `(B3)`, the source then sets:

```text
n = - Q_n,     m = - Q_m,     p = - Q_p     und     σ = - Q_σ        (B63)
```

This gives:

```text
G + F + S = φ                                                        (B64)
```

The source-visible field-mass formula is:

```text
M_ν = µα_+ (Φ + φ_0)                                                (B65)
```

Here `φ_0` refers `(B49)` to the lower bounds of `n, m, p, σ`; the source states that `M_ν` is then determined only by `k, κ, P, Q`.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt`
- Lines: 491-554

## Dependencies

- `HT-F-1989-MASS`
- `HT-F-1989-FPHI`
- `HT-F-1982-QNUM`

## Conditions In Source

Source-checked notes:

- If `Φ + φ ≠ 0`, because `P > 0` or `Q > 0`, `(B3)` gives a nonzero field mass even under `(B63)`.
- The source explicitly says this is not interpretable as a ponderable corpuscle, but as a Heim-internal `Spinpotenz` / `Feldkatalyt` construct.
- Positive-mass possibilities are:
  - `M_ν(1110) = M_ν(1111)` and `M_ν(1200)` in the mesonic range.
  - `M_ν(2110)` and `M_ν(2111)` in the baryonic range.
- For the `β`-transition neutrino only `M_ν(2010)` or `M_ν(1010)` are listed; since `(2010)` would give `M_ν < 0`, the source keeps `M_ν(1010)` as the `β`-Neutrino possibility.
- Possible states are listed in source order:

```text
für k = 1: ν_1(1010), ν_2(1110), ν_3(1200),
für k = 2: ν_4(2110), ν_5(2111).
```

- For each `ν_i`, the source states that the mirror-symmetric antistructure `\bar{ν}_i` exists.
- Results are in Table II and masses are given in electronvolts.
- The source says the empirical `β`-Neutrino can be interpreted by `ν_1` and the empirical `µ`-Neutrino by `ν_2`, but it remains undecided whether the other neutrinos are realized in nature or only logical possibilities.

## Current Status

`source_checked`

## Audit Notes

- Source-checked against `1989_erweiterte_massenformel/page-09.png` and `page-10.png` by two worker packets plus Critic review.
- Source range was extended from `491-552` to `491-554` to include the complete final interpretation sentence.
- `M_ν`, `ν_i`, `α_+`, and `φ_0` use readable subscript notation while preserving source glyphs.
- `NORM-1989-NEUTRINO-PHI-GLYPH` maps source phi glyph variants to canonical `phi` / `phi_0` while keeping uppercase `Phi` separate.
- `NORM-1989-NEUTRINO-STATE-TUPLES` defines the four-digit labels as `(k,P,Q,kappa)` and preserves source state order.
- OCR `ß` is corrected to source-visible Greek `β` in `β-Übergang` and `β-Neutrino`.
- The antistructure notation is barred `\bar{ν}_i`; it must not be flattened to plain `ν_i`.
- This is not automatically a modern neutrino mass prediction. It must be treated first as Heim's internal field-mass construct, then compared to historical and modern neutrino constraints only after the interpretation is explicit.

## Risks

- `φ` versus variant phi maps to canonical `phi`; B49 scope remains a separate normalization concern.
- Juxtaposition in `µα_+` is source-visible multiplication, not implementation notation.
- State order and grouping by `k = 1` / `k = 2` must not be reordered by later interpretation.
