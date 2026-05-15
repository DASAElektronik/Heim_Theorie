# HT-F-1982-SELECTION-WVX: 1982 Structure Potency And Resonance Basis

## Formula Group

Source-checked image transcription from `page-06.png`, `page-07.png`, and `page-08.png`.

```math
w_{\nu x} = (kPQ\kappa)_\varepsilon C(q_x)
```

```math
w_{\nu x}
=
\left\{
(1-Q)\left[A_{11}-P(A_{12}+A_{13}q\kappa/\eta_{qk})
-\binom{P}{2}(A_{14}-A_{15}q/\eta_{qk})\right]
+\kappa Q\eta_{qk}A_{16}
\right\}^{2-k}
+
\left\{
(q-1)A_{21}+(1-P)A_{22}
+\binom{P}{2}\left[A_{23}-q_x\eta_{qk}(1+A_{24}(+q_x))^{-1}A_{25}\right]
+\kappa(A_{26}+q\eta_{qk}^{2}A_{31})
+\binom{Q}{3}\eta_{qk}A_{32}
+\binom{P}{3}\left[
A_{33}q^3\frac{q_x-(-1)^q}{3-q}
+\frac{\varepsilon(P-Q)\eta^{(q+1)q/4}}{8-A_{66}^{q(q-1)}}
\left(1-q(2-q)A_{34}^{1-q_x}A_{35}/\eta_{qk}\right)\eta_{qk}/\eta^2
-A_{36}
\right]
\right\}^{k-1}
```

Original label: `(XVI)`.

```math
w(1)
=
(1-Q)\left[A_{11}-P(A_{12}+A_{13}q\kappa/\eta_{qk})
-\binom{P}{2}(A_{14}-A_{15}q/\eta_{qk})\right]
+\kappa Q\eta_{qk}A_{16}
```

Original label: `(XVII)`.

```math
w(2)
=
(q-1)A_{21}+(1-P)A_{22}
+\binom{P}{2}\left[A_{23}-A_{25}q_x\eta_{qk}(1+A_{24}(1+q_x))^{-1}\right]
+\kappa(A_{26}+q\eta_{qk}^{2}A_{31})
+\binom{Q}{3}\eta_{qk}A_{32}
+\binom{P}{3}\left\{
A_{33}q^3\left[\frac{q_x-(-1)^q}{3-q}\right]
+\frac{\varepsilon(P-Q)\eta^{(q+1)q/4}}{8-A_{66}^{q(q-1)}}
\left[1-q(2-q)A_{34}^{1-q_x}A_{35}/\eta_{qk}\right]\eta_{qk}/\eta^2
-A_{36}
\right\}
```

Original label: `(XVIII)`.

```math
w_{\nu x} = [w(1)]^{2-k} + [w(2)]^{k-1}
```

Original label: `(XIX)`.

```math
w_{\nu x}(k) = [k-1+w(1)]^{2-k} + [2-k+w(2)]^{k-1}
```

Printed programming correction below `(XIX)` to avoid improper `0^0` terms.

```math
a_{\nu x}=A_{41}(1+a_n a_q)/k
```

Original label: `(XX)`.

```math
a_n
=
PA_{42}\left[
1-\kappa A_{43}(1+A_{44}(-\alpha)^{2-k}A_{45}^{k-1})
(1-\kappa QA_{46}(2-k))
-A_{51}(k-1)(1-\kappa)
\right]
```

Original label: `(XXI)`.

```math
a_q
=
1-qA_{52}(1-2A_{53}^{k})
\left[1+q_x(3-q_x)(k-1)(1-\kappa)/6\right]
```

Original label: `(XXII)`.

```math
b_{\nu x}
=
\frac{
\left\{
A_{54}A_{55}^{k-1}
\left[1-PA_{56}(1-\kappa A_{61}A_{62}^{1-k})(1+qA_{63}(1+\kappa A_{64}))\right]
\left(1-k^{-1}(A_{65}(q+k-1))^{2-k}\binom{P}{2}\left(1-\binom{P}{3}\right)\right)
\right\}
}{
k^P(1+P+Q+\kappa\eta^{2-q})
}
```

Original label: `(XXIII)`.

```math
\hat A=(A_{rs})_6,\qquad A_{rs}\ne A_{sr},\qquad \operatorname{Im}A_{rs}=0
```

```math
A_{11}=(\xi^2\pi e)^2(1-4\pi\alpha^2)/2\eta^2
A_{12}=2\pi\xi^2(\vartheta/24-e\pi\eta\alpha^2/9)
A_{13}=3(4+\eta\alpha)\left[1-(\eta^2/5)(1-\sqrt{\eta})^2/(1+\sqrt{\eta})^2\right]
A_{14}=\left[1+3\eta(2\eta\alpha-e^2\xi)(1-\sqrt{\eta})^2/\{(1+\sqrt{\eta})^2 4\xi\}\right]/\alpha

A_{15}=e^2(1-2e\alpha^2/\eta)/3
A_{16}=(\pi e)^2[1+\alpha(1+6\alpha/\pi)/5\eta]
A_{21}=2(e\alpha/2\eta)^2(1-\alpha/2\xi^2)
A_{22}=\xi[1-\xi(\alpha\xi/\eta^2)^2]/12

A_{23}=(\eta^2+6\xi\alpha^2)/e
A_{24}=2\xi^2/3\eta
A_{25}=\xi(\pi e)^2(1-\beta^2)
A_{26}=2\{1-[\pi(e\xi\alpha)^2\sqrt{\eta}]/2\}/e\xi^2

A_{31}=(\pi e\alpha)^2[1-(\pi e)^2(1-\beta^2)]
A_{32}=\xi^2[1+(2e\alpha/\eta)^2]/6
A_{33}=(\pi e\xi\alpha)^2[1-2\pi(e\xi)^2(1-\beta^2)]
A_{34}=\eta\sqrt{2\pi\eta}

A_{35}=3\alpha/e\xi^2
A_{36}=[1-\pi e(\xi e)^2(1-\beta^2)]^{-1}
A_{41}=\{\xi[2+(\xi\alpha)^2]-2\beta\}/(2\beta-\alpha)
A_{42}=[\pi\xi^2\eta(\beta-3\alpha)]/2

A_{43}=\xi/2
A_{44}=2(\eta/\xi)^2
A_{45}=(3\beta-\alpha)/6\xi
A_{46}=\pi e/\xi\eta-e\eta^2\alpha/2

A_{51}=(2\alpha+1)^2
A_{52}=6\alpha/\eta^2
A_{53}=(\xi/\eta)^3
A_{54}=\alpha(\beta-\alpha)\sqrt{3/2}

A_{55}=\xi^2
A_{56}=(\xi/\eta)^4
A_{61}=\pi\xi(2\beta-\alpha)/12\beta
A_{62}=\pi^2(\beta-2\alpha)/12

A_{63}=(\sqrt{\eta})/9
A_{64}=\pi/3\eta
A_{65}=\pi/3\xi
A_{66}=\xi\eta
```

Original label: `(XXIV)` applies to the matrix coefficient proposal.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 250-356
- Source images:
  - `07_outputs/source_check_images/1982_massenformel/page-06.png`
  - `07_outputs/source_check_images/1982_massenformel/page-07.png`
  - `07_outputs/source_check_images/1982_massenformel/page-08.png`
- Original labels: `(XVI)` to `(XXIV)`
- Worker packets:
  - `agent_workspace/worker_packets/OCR-1982-SELECTION-WVX__worker-a.md`
  - `agent_workspace/worker_packets/OCR-1982-SELECTION-WVX__worker-b.md`
- Critic review:
  - `agent_workspace/critic_reviews/OCR-1982-SELECTION-WVX__critic.md`

## Outputs

- `w_nu_x`
- `w(1)`, `w(2)`
- corrected printed `w_nu_x(k)` form
- `a_nu_x`
- `a_n`, `a_q`
- `b_nu_x`
- coefficient matrix terms `A11..A66`

## Current Status

`source_checked`

## Audit Notes

- This is only an image-vs-OCR source check. It is not normalized, derived, implemented, or validated.
- Do not integrate either worker packet verbatim; this file follows the accepted Critic transcription.
- The direct multiline display of `(XVI)` has cramped brace layout near the source label. Use `(XVII)` to `(XIX)` as the safer source for the `w(1)`/`w(2)` decomposition.
- The printed line break with `* *` in `a_n` is treated as multiplication in the source transcription.
- The exponent `A34^(1-q_x)` is visually tight but visible on the scan.

## Risks

- Slash binding in terms such as `A16`, `A24`, `A35`, `A46`, `A64`, and `A65` still needs a normalization decision.
- `k^P(1+P+Q+kappa eta^(2-q))` in `b_nu_x` is source transcription only; do not silently change it to `kP(1+P+Q+kappa eta^2-q)`.
- `A_rs` matrix terms introduce many new symbols and should be cross-linked in the symbol register before implementation.

