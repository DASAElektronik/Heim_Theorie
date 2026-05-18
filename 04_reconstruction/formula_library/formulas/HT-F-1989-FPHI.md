# HT-F-1989-FPHI: 1989 F, Phi and Self-Coupling Terms

## Source-Visible Transcription

The source introduces the quantization-dependent abbreviations for `F` and `Φ`:

```text
F = 2 n Q_n [1 + 3(n + Q_n + n Q_n) + 2(n^2 + Q_n^2)]
  + 6 m Q_m (1 + m + Q_m)N_2
  + 2 p Q_p N_3
  + φ * δ(N)                                                        (B5)

Φ = P(-1)^(P+Q) (P + Q) N_5 + Q(P + 1) N_6                         (B6)

mit φ = φ(p,σ) und δ(0) = 1 (0 für N ≠ 0),                         (B7)
```

The source then gives the self-coupling line with references to later equations:

```text
φ =
  (N_4 p^2)/(1 + p^2)
  * (σ + Q_σ)/sqrt(1 + σ^2)
  * (fourth_root(2) - 4BUW^{-1}_{N=0})
  + P(P - 2)^2(1 + κ(1 - q)/2α ϑ)
    * (π/e)^2 sqrt(η_12)(Q_m - Q_n)
  - (P + 1)(Q/3)/α                                      vergl. (B49)

U = 2^Z [
      P^2 + 3/2(P - Q) + P(1 - q)
      + 4κB(1 - Q)/(3 - 2q)
      + (k - 1){P + 2Q -- 4π(P - Q)(1 - q)/fourth_root(2)}
    ] η_qk^-2                                           vergl.(B50)

Z = k + P + Q + κ                                       vergl.(B51)
```

The remaining `N_i` definitions are:

```text
ln(N_3 k/2) =
  (k - 1)[
    1 - π (1 - η_q,k)/(1 + sqrt(η_q,1))
      {1 - u η_q,1/ϑ_q,1 (1 - α_-/α_+)(1 - sqrt(η))^2}
  ]
  - 2/(3π e)(1 - sqrt(η))^2
    (6π^2e^2/ϑ * (1 + sqrt(η_q,1))/(1 - η) - 1)          (B8)

N_4 = (4/k)[1 + q(k - 1)]                                (B9)

N_5 =
  A[1 + k(k - 1) 2^(k^2+3) N(k) A
    ((1 - sqrt(η_q,k))/(1 + sqrt(η_q,k)))^2]              (B10)

A = (8/η)(1 - α_-/α_+)(1 - 3η/4)                         (B11)

N(k) = Q_n + Q_m + Q_p + Q_σ + k(-1)^k 2^(k^2-1)         (B12)

N_6 =
  2k/(π e ϑ)[
    sqrt(k)(k^2 - 1) N(k)/sqrt(η_1,k)
      {q - (1 - q) N'(k)/(Q_n sqrt(η_1,k))}
    + (-1)^(k+1)
  ]
  η(1 - α_-/α_+) (4(1 - sqrt(η))/(1 + sqrt(η)))^2 Q_σ     (B13)

N'(k) = Q_n + Q_m + Q_p + Q_σ - 2k - 1                   (B14)
```

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt`
- Lines: 87-147
- Original labels: `(B5)` to `(B14)`

## Outputs

- `F`
- `Phi`
- `phi`
- auxiliary `N_i`

## Current Status

`source_checked`

## Audit Notes

- Source-checked against `1989_erweiterte_massenformel/page-02.png` and `page-03.png` by two worker packets plus Critic review.
- The self-coupling line after `(B7)` uses source-visible `(σ + Q_σ)/sqrt(1 + σ^2)`, not `σ + Q_σ/sqrt(...)`.
- The final stacked factor in the self-coupling line is source-visible `(Q/3)`; capital/lowercase distinction remains flagged.
- `BUW^{-1}_{N=0}` is a source token only. `NORM-1989-FPHI-BUW-TOKEN-BLOCKER` keeps it opaque because neither local full-text search nor web search found a source-backed definition or inverse scope.
- `NORM-1989-FPHI-B49-SCOPE-BLOCKER` documents the outer three-term B49 decomposition but keeps `kappa(1-q)/2 alpha vartheta` and the final stacked `(Q over 3)` factor blocked for executable implementation.
- In `(B50)`, the visible double minus before `4π` and the `fourth_root(2)` denominator are preserved as source transcription; `NORM-1989-FPHI-B50-DOUBLE-MINUS-BLOCKER` keeps sign normalization blocked.
- In `(B13)`, the leading `4` is inside the squared parenthesis: `(4(1 - sqrt(η))/(1 + sqrt(η)))^2`; `NORM-1989-FPHI-B8-B13-LINE-WRAP-SCOPE` resolves B8/B13 implementation parentheses.
- The same source says long equations in the manuscript had missing brackets that were corrected by best estimates. This formula group must carry that caveat until checked against all available manuscript/table evidence.

## Risks

- High bracket ambiguity.
- `(B49)` outer terms are documented, but compact inner scopes still block numerical implementation.
- `(B8)` and `(B13)` line-wrap scopes are resolved for implementation by `NORM-1989-FPHI-B8-B13-LINE-WRAP-SCOPE`.
- The glyph `u` in `(B8)` may later need comparison against surrounding Heim notation.
- Subscript comma style varies visibly (`η_q,k`, `η_q,1`, `η_1,k`); `NORM-1989-FPHI-NAMING` defines stable implementation names for these source forms without resolving expression scope.
- Later reconstruction may have silently corrected Heim's expression.
- `phi` includes empirically adjusted terms per the closing remarks in the 1989 text.
