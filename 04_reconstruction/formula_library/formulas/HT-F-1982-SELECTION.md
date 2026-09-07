# HT-F-1982-SELECTION-core: 1982 Occupation Selection Rule Core

## Formula Group

Source-checked transcription from page image:

```math
n_4 + Q_4
\le (n_3+Q_3)\alpha_3
\le (n_2+Q_2)^2\alpha_2
\le (n_1+Q_1)^3\alpha_3
```

Original label: `(XIII)`.

```math
(n_1+Q_1)^3\alpha_1
+ (n_2+Q_2)^2\alpha_2
+ (n_3+Q_3)\alpha_3
+ \exp\left[1-\frac{2k(n_4+Q_4)}{3Q_4}\right]
+ iF(\Gamma)
=
W_{\nu x}
\left\{
1 + [1-Q(2-k)(1-\kappa)]
\left[
\frac{a_{\nu x}N}{N+2}
+ b_{\nu x}\sqrt{N(N-2)}
\right]
\right\}

W_{\nu x} = g(qk)w_{\nu x}

g(qk) =
Q_1^3\alpha_1
+ Q_2^2\alpha_2
+ Q_3\alpha_3
+ \exp[(1-2k)/3]
\quad\text{for } n_j = 0
```

Original labels: `(XIV)` and `(XV)`.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 226-248
- Source image: `07_outputs/source_check_images/1982_massenformel/page-06.png`
- Original labels: `(XIII)` to `(XV)`

## Outputs

- Selection-equation constraint for occupation tuple `(n1,n2,n3,n4)`.
- Basis ascent `g(qk)`.
- Selection target `W_nu_x`.

## Current Status

`source_checked`

## Audit Notes

- This is probably the most important non-obvious formula group. If the selection rule is ambiguous, apparent mass matches can be produced by choosing favorable occupation tuples.
- `(XIII)` is transcribed as printed: the rightmost factor is `alpha_3`, not `alpha_1`. `NORM-1982-SELECTION-XIII-ALPHA3` preserves `alpha_3` as the source-literal default and permits `alpha_1` only as an explicit emendation variant.
- OCR line 244 lost the square root over `N(N-2)`; the page image shows `b_nu_x sqrt(N(N-2))`.
- `(XV)` is included here because `W_nu_x = g(qk)w_nu_x` is part of the selection equation.
- `NORM-1982-SELECTION-IF-GAMMA` resolves `iF(Gamma)` only for mass-spectrum tuple enumeration: for `N=0` and `N>=2`, `F(Gamma)=0`; for `N=1`, there is no default spectral term.
- `NORM-1982-SELECTION-VX-NUX-SCOPING` preserves this record's `nu_x` notation and forbids silent harmonization with the later page-8/page-9 `vx` family.
- The full state-selection workflow continues beyond this entry with `w_nu_x`, `a_nu_x`, `b_nu_x`, resonance-order rules, and algorithmic occupation choices on later pages. Those later formulas are not source-checked here.
- This is a source transcription only. It is not normalized or implementation-ready.

## Risks

- `W_nu_x`, `a_nu_x`, `b_nu_x` depend on later formulas not yet normalized.
- `iF(Gamma)` is resolved only for enumerated mass states by `NORM-1982-SELECTION-IF-GAMMA`; Gamma/bandwidth semantics remain blocked separately.
- Resonance order `N` and missing rules around `N=1` need exact treatment.
- The apparent `alpha_3` in the rightmost term of `(XIII)` is resolved by `NORM-1982-SELECTION-XIII-ALPHA3`; do not silently emend it to `alpha_1`.
- Do not treat this entry alone as a complete valid/invalid tuple algorithm.
