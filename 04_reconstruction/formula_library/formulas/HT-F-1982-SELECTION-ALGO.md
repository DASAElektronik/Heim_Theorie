# HT-F-1982-SELECTION-ALGO: 1982 Occupation Tuple Algorithm

## Formula Group

Source-checked image transcription from `page-09.png`.

The source states that, for numerical determination of `W_{vx}`, `a_{vx}`, `b_{vx}` and `Phi_{vx}`, the calculation should use:

```math
Q = Q(0)
```

of `x_v`, not:

```math
Q_N = Q(N)
```

For a resonance order `N = 0` or `N >= 2`, determine numerically:

```math
W_{vx}(1+f(N)) = W_1
```

Then choose the maximum cubic number `K_1^3` whose product with `alpha_1` is still contained in `W_1`, and set:

```math
W_1 - \alpha_1K_1^3 = W_2 \ge 0
```

Insert `W_2` into:

```math
(n_2 + Q_2)^2\alpha_2
+ (n_3 + Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_2
```

Original label: `(XXX)`.

Next choose the maximum square number `K_2^2` such that `alpha_2K_2^2` is still contained in `W_2`, so:

```math
W_2 - \alpha_2K_2^2 = W_3 \ge 0
```

Then use:

```math
(n_3 + Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_3
```

Original label: `(XXXI)`.

Choose the maximum number `K_3` in the sense:

```math
W_3 - \alpha_3K_3 = W_4 \ge 0
```

For `W_4`, the source gives three cases:

```text
(a): W_4 = 0,
(b): 0 < W_4 <= 1,
(c): W_4 > 1.
```

For the general case `(b)`:

```math
\ln W_4 \le 0
```

and:

```math
K_4(2k-1) = -3Q_4\ln W_4
```

For case `(c)`, the source visibly states:

```text
lnW_4 > 0 and K < 0
```

The printed `K < 0` is preserved as source transcription. The following sentence separately refers to adding `alpha_3K_3` to `K_4 < 0`, producing a new value `K_4 >= 0`, provided `K_3 > 0`. If `K_3 = 0`, the source says this dilation cannot occur because of the quadratic increase of `j = 2`, and this resonance order `N` for `x_{vx}` does not exist.

For case `(a)`, the source states that `W_4 -> 0` would imply `K_4 -> infinity`, but this is impossible because:

```math
K_4 \le \alpha_3K_3
```

Therefore in case `(a)` the maximal value is computed as:

```math
K_4 = \alpha_3K_3
```

The occupation numbers follow from:

```math
n_j = K_j - Q_j
```

The source notes that `n_j >= 0` and `n_j < 0` are both possible, but always:

```math
K_j \ge 0,\qquad n_j \ge -Q_j
```

The resulting quadruple `n_j` is inserted with `Phi_{vx}` into the mass spectrum, giving numerically `M_N(vx)` as spectral term of the mass spectrum for `x_{vx}`.

## Integer And Decimal-Place Rule

The source `Vermerk` states that the `K_j` are always integer. In determining `K_4`, decimal places occur regularly.

If the decimal places are printed as:

```text
,99...99
```

then the identity:

```text
,99...99 = 1
```

must be used. If the decimal-place sequence differs from this value, the source says not to round up; the decimal places are to be cut off because the `K_j` are counts of structure entities.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 395-435
- Source image: `07_outputs/source_check_images/1982_massenformel/page-09.png`
- Original labels: `(XXX)` and `(XXXI)`
- Worker packets:
  - `agent_workspace/worker_packets/OCR-1982-SELECTION-ALGO__worker-a.md`
  - `agent_workspace/worker_packets/OCR-1982-SELECTION-ALGO__worker-b.md`
- Critic review:
  - `agent_workspace/critic_reviews/OCR-1982-SELECTION-ALGO__critic.md`

## Outputs

- `W_1`, `W_2`, `W_3`, `W_4`
- `K_1`, `K_2`, `K_3`, `K_4`
- occupation tuple `n_j`
- `W_4` cases `(a)`, `(b)`, `(c)`
- integer/decimal-place rule for `K_j`

## Current Status

`source_checked`

## Audit Notes

- This is only an image-vs-OCR source check. It is not normalized, derived, implemented, or validated.
- The source line range is `395-435`; the earlier queue range `395-431` cut off part of the `Vermerk`.
- The next heading `Grenzen der Resonanzspektren` and formula `(XXXII)` are not part of this formula entry.
- The top-line state is preserved as `Q = Q(0)` of `x_v`, not harmonized to `x_{vx}`.
- The repeated source-local `vx` glyph family is preserved for `W_{vx}`, `a_{vx}`, `b_{vx}`, `Phi_{vx}`, terminal `x_{vx}`, and `M_N(vx)`. This is not a project-wide normalization decision.
- `NORM-1982-ALGO-VX-SCOPING` resolves this record locally: preserve `x_v` in the top-line state and preserve the later `vx`/`x_vx` family as printed.
- The printed line-417 distinction `K < 0` is preserved. Any later replacement with `K_4 < 0` must be marked as normalization or interpretation, not source transcription.
- The final noun in the `Vermerk` is preserved as `Strukturentitäten`.

## Risks

- The algorithm is source-checked only as visible transcription; implementation still requires a separate normalization pass for logarithm notation, inequality handling, integer truncation, and branch/case behavior.
- The source-local `vx` notation must be reconciled later with nearby `nu/x` notation during normalization.
- The decimal-place rule is a discrete free choice and must remain visible in any later numerical reproduction.
