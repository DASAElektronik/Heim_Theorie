# HT-F-1982-SELECTION-N: 1982 Resonance Order Rule

## Formula Group

Source-checked image transcription from `page-08.png`, with high-resolution supplement for the repeated `vx` subscript.

```math
N \ge 0,\qquad N \in \mathbb{Z}
```

The source states that the resonance order `N` selects allowed occupation quadruples `n_j` with `1 <= j <= 4`.

```math
f(N)
=
[1-Q(2-k)(1-\kappa)]
\left[
a_{vx}\frac{N}{N+2}
+ b_{vx}\sqrt{N(N-2)}
\right]
```

Original label: `(XXV)`.

The source states:

```text
F(Gamma) = 0 for all N != 1, because the right-hand side is real.
```

For `N = 0`, the source states `f = 0`, giving:

```math
(n_1+Q_1)^3\alpha_1
+ (n_2+Q_2)^2\alpha_2
+ (n_3+Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_{vx}
```

Original label: `(XXVI)`.

The source states that this describes the `n_j` of state `x_{vx}` and the mass `M_0(vx)` of component `x` of multiplet `x_v`. For `N >= 2`, it assigns a spectrum of occupation-parameter quadruples and resonance masses `M_N(vx)`. For `N = 1`, there is no spectral term; `f(1)` is complex.

Real part for `N = 1`:

```math
(n_1+Q_1)^3\alpha_1
+ (n_2+Q_2)^2\alpha_2
+ (n_3+Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_{vx}\{1+[1-Q(2-k)(1-\kappa)]a_{vx}/3\}
```

Original label as printed: `(XVII)`.

Imaginary part:

```math
F(\Gamma) = W_{vx}[1-Q(2-k)(1-\kappa)]b_{vx}
```

Original label: `(XXVIII)`.

The source then notes that `n_j` and `F(Gamma)` have some relationship to the full bandwidths `Gamma`, and that a relation `Q_N = Q(N)` between double spin quantum number `Q` and `N` is also needed.

If `N = 1` is excluded, then `F = 0`, and the real relation is:

```math
(n_1+Q_1)^3\alpha_1
+ (n_2+Q_2)^2\alpha_2
+ (n_3+Q_3)\alpha_3
+ + \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_{vx}(1+f)
```

Original label: `(XXIX)`.

The source visibly prints the doubled `+ +` before the exponential term. This is preserved as source transcription and must not be normalized away during source check.

The source states that generally `f > 0` for `N >= 2` and `f = 0` for `N = 0`. For multiplet `x_2`, however, `f = 0` for all `N >= 0`, because `Q(2-k)(1-\kappa) = 1`; the source note says electrons are not excitable in this picture.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 357-388
- Source image: `07_outputs/source_check_images/1982_massenformel/page-08.png`
- High-resolution check:
  - `07_outputs/source_check_images/1982_massenformel_hi/page-08.png`
  - `07_outputs/source_check_images/1982_massenformel_hi/page-08-hi-fN-subscript.png`
  - `07_outputs/source_check_images/1982_massenformel_hi/page-08-hi-W-lines.png`
  - `07_outputs/source_check_images/1982_massenformel_hi/page-08-hi-XXIX.png`
- Original labels: `(XXV)` to `(XXIX)`, with `(XVII)` printed on the real-part equation
- Worker packets:
  - `agent_workspace/worker_packets/OCR-1982-SELECTION-N__worker-a.md`
  - `agent_workspace/worker_packets/OCR-1982-SELECTION-N__worker-b.md`
- Critic reviews:
  - `agent_workspace/critic_reviews/OCR-1982-SELECTION-N__critic.md`
  - `agent_workspace/critic_reviews/OCR-1982-SELECTION-N__resolver.md`

## Outputs

- `f(N)`
- resonance-order cases `N = 0`, `N = 1`, `N >= 2`
- real and imaginary relations for `N = 1`
- unresolved relation requirements involving `Gamma` and `Q_N = Q(N)`

## Current Status

`source_checked`

## Audit Notes

- This is only an image-vs-OCR source check. It is not normalized, derived, implemented, or validated.
- Initial worker conflict over Greek `nu x` versus Latin `vx` was resolved by high-resolution page-8 crops. For this page-8 selection block, use source-local `vx` notation.
- Do not use this `vx` decision to rewrite other reviewed formulas unless a later normalization pass explicitly adopts a project-wide symbol policy.
- The radical over `N(N-2)` is visible and restored from OCR.
- The doubled `+ + exp[...]` in `(XXIX)` is preserved as printed.
- The real-part label is preserved as printed `(XVII)`, even though it is anomalous in sequence.

## Risks

- `N = 1` handling is explicitly problematic because `f(1)` is complex.
- The relation between `n_j`, `F(Gamma)`, full bandwidths `Gamma`, and `Q_N = Q(N)` is stated as unresolved in the source and is blocked by `NORM-1982-N-GAMMA-QN-BLOCKER`.
- The source-local `vx` notation must be reconciled later with nearby `nu/x` notation during normalization.
