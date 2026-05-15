# OCR-1989-FPHI Worker B

## Verdict
ready

## Scope
- Formula ID: HT-F-1989-FPHI
- Image pages used: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-02.png`, `07_outputs/source_check_images/1989_erweiterte_massenformel/page-03.png`
- OCR source: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt` lines 87-147
- Current file checked: `04_reconstruction/formula_library/formulas/HT-F-1989-FPHI.md`

## Accepted Source-Visible Transcription

```text
(B5) F = 2 n Q_n [1 + 3(n + Q_n + n Q_n) + 2(n^2 + Q_n^2)]
     + 6 m Q_m (1 + m + Q_m)N_2 + 2 p Q_p N_3 + φ * δ(N)

(B6) Φ = P(-1)^(P+Q) (P + Q) N_5 + Q(P + 1) N_6

(B7) mit  φ = φ(p,σ) und δ(0) = 1 (0 für N ≠ 0),

(B49) wobei
      φ = (N_4 p^2)/(1 + p^2) * (σ + Q_σ/√(1 + σ^2)) * (4√2 - 4BUW_{N=0}^{-1})
          + P(P - 2)^2(1 + κ(1 - q)/2α ϑ) · (π/e)^2 √η_{12}(Q_m - Q_n) - (P + 1)(q/3)/α,
      vergl. (B49)

(B50) U = 2^Z [P^2 + 3/2 (P - Q) + P(1 - q) + 4κB (1 - Q)/(3 - 2q)
          + (k - 1){P + 2Q -- 4π(P - Q)(1 - q)/√2}] η_{qk}^{-2}
      vergl.(B50)

(B51) Z = k + P + Q + κ
      vergl.(B51)

(B8) ln(N_3 k/2) = (k - 1) [1 - π (1 - η_{q,k})/(1 + √η_{q,1}) {1 - u η_{q,1}/ϑ_{q,1}
      (1 - α_/α_+)(1 - √η)^2}] -
      2/(3π e) (1 - √η)^2 (6 π^2 e^2/ϑ (1 + √η_{q,1})/(1 - η) - 1)

(B9) N_4 = (4/k) [1 + q(k - 1)]

(B10) N_5 = A[1 + k(k - 1) 2^(k^2 + 3) N(k) A ((1 - √η_{q,k})/(1 + √η_{q,k}))^2]

(B11) A = (8/η) (1 - α_-/α_+)(1 - 3η/4)

(B12) N(k) = Q_n + Q_m + Q_p + Q_σ + k(-1)^k 2^(k^2 - 1)

(B13) N_6 = 2k/(π e ϑ) [√k (k^2 - 1) N(k)/√η_{1,k} {q - (1 - q) N'(k)/(Q_n √η_{1,k})}
      + (-1)^(k+1)] η(1 - α_-/α_+) ((1 - √η)/(1 + √η))^2 Q_σ

(B14) N'(k) = Q_n + Q_m + Q_p + Q_σ - 2k - 1
```

## OCR Corrections vs Current Formula File

- `B6`: OCR drops the exponent braces; source is `P(-1)^(P+Q)`, not `P(-1)P+Q`.
- `B7`: source reads `δ(0) = 1 (0 für N ≠ 0)`, not the generic `otherwise 0` wording in the working draft.
- `B49`: the current file has no self-coupling expansion; source adds the full `φ` line with `N_4`, `Q_σ`, `BUW_{N=0}^{-1}`, `η_12(Q_m - Q_n)`, and the trailing `-(P + 1)(q/3)/α`.
- `B50/B51`: the current file has no `U`/`Z` block; source uses `U = 2^Z ... η_qk^-2` and `Z = k + P + Q + κ`.
- `B8-B14`: the current file stops at a high-level outline; source explicitly gives `N_3`, `N_4`, `N_5`, `A`, `N(k)`, `N_6`, and `N'(k)`.
- `B5`: the working draft uses flat ASCII names; source keeps the subscripted forms `Q_n`, `Q_m`, `Q_p`, `N_2`, `N_3`, and `δ(N)`.

## Unresolved Glyph / Notation Risks

- `B49`: the product scope after `P(P - 2)^2(1 + κ(1 - q)/2α ϑ)` is not fully crisp; the `·(π/e)^2...` continuation is visible, but the exact multiplication grouping should stay provisional.
- `B50`: the `--` cluster before `4π(P - Q)(1 - q)/√2` is visually ambiguous; keep the bracket scope open until a cleaner source pass confirms whether this is a minus plus line-wrap artifact.
- `B8`: the `u` glyph inside `{1 - u η_{q,1}/ϑ_{q,1} ...}` is readable, but the enclosing fraction/bracket scope is tight.
- `B10`: the exponent on `2` is read as `k^2 + 3`; keep that as a source reading, not a normalized rewrite.
- `B13`: the tail `η(1 - α_-/α_+) ... Q_σ` is visible, but whether the preceding bracket closes before the multiplier is still line-wrap sensitive.
- `B5 -> B6`: the formula continues across the page break, but there is no extra mathematical carryover beyond the labeled block; do not use the page break as a structural boundary.

## Implementation Implications

- Do not normalize any of these terms yet.
- Keep the source glyphs and bracket layout intact until the canonical pass can reconcile B49-B51 and the long B8/B13 blocks.
- Treat `Q_n`/`Q_σ`/`α_-` as source-level readings, not as a request to rewrite the working file now.
