# OCR-1989-FPHI Critic Review

Verdict: `critic_ready`

## Accepted source-visible transcription

- B5:
  `F = 2 n Q_n [1 + 3(n + Q_n + n Q_n) + 2(n^2 + Q_n^2)] + 6 m Q_m (1 + m + Q_m)N_2 + 2 p Q_p N_3 + φ * δ(N)`

- B6:
  `Φ = P(-1)^(P+Q) (P + Q) N_5 + Q(P + 1) N_6`

- B7:
  `mit φ = φ(p,σ) und δ(0) = 1 (0 für N ≠ 0),`

- Self-coupling line, `vergl. (B49)`:
  `φ = (N_4 p^2)/(1 + p^2) · (σ + Q_σ)/sqrt(1 + σ^2) · (fourth_root(2) - 4BUW^{-1}_{N=0}) + P(P - 2)^2(1 + κ(1 - q)/2α ϑ) · (π/e)^2 sqrt(η_12)(Q_m - Q_n) - (P + 1)(Q/3)/α`

- Auxiliary `U`, `vergl.(B50)`:
  `U = 2^Z [P^2 + 3/2(P - Q) + P(1 - q) + 4κB(1 - Q)/(3 - 2q) + (k - 1){P + 2Q -- 4π(P - Q)(1 - q)/fourth_root(2)}] η_qk^-2`

- Auxiliary `Z`, `vergl.(B51)`:
  `Z = k + P + Q + κ`

- B8:
  `ln(N_3 k/2) = (k - 1)[1 - π (1 - η_q,k)/(1 + sqrt(η_q,1)) {1 - u η_q,1/ϑ_q,1 (1 - α_-/α_+)(1 - sqrt(η))^2}] - 2/(3π e)(1 - sqrt(η))^2(6π^2e^2/ϑ · (1 + sqrt(η_q,1))/(1 - η) - 1)`

- B9:
  `N_4 = (4/k)[1 + q(k - 1)]`

- B10:
  `N_5 = A[1 + k(k - 1) 2^(k^2+3) N(k) A ((1 - sqrt(η_q,k))/(1 + sqrt(η_q,k)))^2]`

- B11:
  `A = (8/η)(1 - α_-/α_+)(1 - 3η/4)`

- B12:
  `N(k) = Q_n + Q_m + Q_p + Q_σ + k(-1)^k 2^(k^2-1)`

- B13:
  `N_6 = 2k/(π e ϑ)[sqrt(k)(k^2 - 1) N(k)/sqrt(η_1,k) {q - (1 - q) N'(k)/(Q_n sqrt(η_1,k))} + (-1)^(k+1)] η(1 - α_-/α_+) (4(1 - sqrt(η))/(1 + sqrt(η)))^2 Q_σ`

- B14:
  `N'(k) = Q_n + Q_m + Q_p + Q_σ - 2k - 1`

## Disagreement resolution

- Self-coupling fraction after B7: source shows the full numerator `σ + Q_σ` over `sqrt(1 + σ^2)`; accept `(σ + Q_σ)/sqrt(1 + σ^2)`, not `σ + Q_σ/sqrt(...)`.
- Final stacked factor after `(P + 1)`: source-visible reading is `(Q/3)`, matching the OCR `Q3`; keep an explicit small-glyph risk rather than silently normalizing to lowercase `q`.
- `BUW`: transcribe source-visibly as `BUW^{-1}_{N=0}` / `BUW_{N=0}^{-1}`. Do not expand to `B*U*W`, do not decide whether the inverse applies to `W` alone or the whole token.
- B50: source visibly has `-- 4π(P - Q)(1 - q)/fourth_root(2)`. Preserve the double minus as a source anomaly until a normalization pass decides whether it is typographic.
- B8/B13: no image-readability conflict blocks `critic_ready`, but both have line-wrap-sensitive scopes listed below.

## Required canonical edits

- Expand `HT-F-1989-FPHI.md` beyond the current outline to include the source-visible B49/B50/B51 auxiliaries and B8-B14 definitions.
- Correct B49 to use `(σ + Q_σ)/sqrt(1 + σ^2)`, `fourth_root(2)`, source-visible `BUW^{-1}_{N=0}`, `sqrt(η_12)(Q_m - Q_n)`, and trailing `(Q/3)/α`.
- Preserve B50 as `P + 2Q -- 4π.../fourth_root(2)` with an anomaly note.
- Add the B13 factor `(4(1 - sqrt(η))/(1 + sqrt(η)))^2`; the `4` is inside the squared parenthesis.

## Unresolved normalization risks

- B49 `(Q/3)` is source-visible, but the capital/lowercase distinction is small and should remain flagged.
- `BUW^{-1}_{N=0}` is a transcription token only; inverse and product scope are not normalized.
- B50 double minus may be a source typo, print artifact, or intended sign cluster.
- B8 `u` may later need comparison against surrounding Heim notation before implementation.
- Subscript comma style varies visibly: keep source-level `η_q,k`, `η_q,1`, `η_1,k`, but do not infer a uniform implementation name here.

## Implementation red flags

- Do not turn the B50 double minus into a single minus during cleanup.
- Do not drop the B13 leading `4` inside the squared parenthesis.
- Do not flatten B8/B13 with regex OCR cleanup; both depend on stacked fractions and line-wrap closures.
- Do not implement numeric evaluation from this packet until the raw/source transcription and normalization notes are carried together.
