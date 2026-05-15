# OCR-1982-SELECTION-WVX Critic Review

## Verdict

critic_ready

## Findings

1. Page 6, eqs. XVI/XVIII: both workers mis-transcribe the epsilon fraction grouping. Worker A lines 38 and 67 place `q(q-1)` outside a denominator `8-A_{66}`; Worker B lines 29-30 and 48-49 split the source into `+\epsilon(P-Q)\eta(q+1)q/4` plus `q(q-1)/(8-A_{66})`. The image instead shows a single fraction with numerator `\epsilon(P-Q)\eta^{(q+1)q/4}` and denominator `8-A_{66}^{q(q-1)}`.

2. Page 6, eqs. XVII/XVIII: Worker A lines 46-69 drop formula-relevant plus signs in the rendered `w(1)` and `w(2)` formulas. The scan clearly has `+ \kappa Q\eta_{qk}A_{16}` in `w(1)` and plus signs before the later `w(2)` terms. Worker B preserves these plus signs.

3. Page 6, eq. XVI and later formulas: Worker A repeatedly renders `\eta q_k` where the image shows the compact subscripted symbol `\eta_{qk}`. This is formula-relevant and must not be normalized as a product.

4. Page 7, eq. XXIII: Worker A's denominator note at line 259 and transcription around lines 114-129 use `kP(1+P+Q+\kappa\eta^2-q)`. The scan resolves this in favor of Worker B line 86: `[k^P(1+P+Q+\kappa\eta^{2-q})]`.

5. Page 6, OCR line 277: Worker A omits the corrected programming form `w_{\nu x}(k) = [k-1+w(1)]^{2-k} + [2-k+w(2)]^{k-1}`. Worker B includes it at line 172, and the page image confirms the exponents.

6. Page 7/page 8, A-matrix continuation: Worker B correctly treats `A_{51}` through `A_{66}` as continuing on page 8. Worker A also includes `A_{51}` through `A_{66}` in its transcription, so this is not a blocker.

7. Page 7, A-matrix terms: Worker A line 143 adds a grouping in `A_{13}` that is not visible as written. The source reads `1-(\eta^2/5)(1-\sqrt{\eta})^2/(1+\sqrt{\eta})^2` inside the bracket.

## Accepted Transcription

This is accepted only as image transcription from `page-06.png`, `page-07.png`, and `page-08.png`; it is not normalized, derived, implemented, or validated.

Page 6 lead-in and structure potency:

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
\tag{XVI}
```

```math
w(1)
=
(1-Q)\left[A_{11}-P(A_{12}+A_{13}q\kappa/\eta_{qk})
-\binom{P}{2}(A_{14}-A_{15}q/\eta_{qk})\right]
+\kappa Q\eta_{qk}A_{16}
\tag{XVII}
```

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
\tag{XVIII}
```

```math
w_{\nu x} = [w(1)]^{2-k} + [w(2)]^{k-1}
\tag{XIX}
```

```math
w_{\nu x}(k) = [k-1+w(1)]^{2-k} + [2-k+w(2)]^{k-1}
```

Page 7 resonance basis and raster:

```math
a_{\nu x}=A_{41}(1+a_n a_q)/k
\tag{XX}
```

```math
a_n
=
PA_{42}\left[
1-\kappa A_{43}(1+A_{44}(-\alpha)^{2-k}A_{45}^{k-1})
(1-\kappa QA_{46}(2-k))
-A_{51}(k-1)(1-\kappa)
\right]
\tag{XXI}
```

```math
a_q
=
1-qA_{52}(1-2A_{53}^{k})
\left[1+q_x(3-q_x)(k-1)(1-\kappa)/6\right].
\tag{XXII}
```

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
\tag{XXIII}
```

Matrix statement:

```math
\hat A=(A_{rs})_6,\qquad A_{rs}\ne A_{sr},\qquad \operatorname{Im}A_{rs}=0.
```

Page 7/page 8 coefficient matrix proposal:

```math
A_{11}=(\xi^2\pi e)^2(1-4\pi\alpha^2)/2\eta^2
```

```math
A_{12}=2\pi\xi^2(\vartheta/24-e\pi\eta\alpha^2/9)
```

```math
A_{13}=3(4+\eta\alpha)\left[1-(\eta^2/5)(1-\sqrt{\eta})^2/(1+\sqrt{\eta})^2\right]
```

```math
A_{14}=\left[1+3\eta(2\eta\alpha-e^2\xi)(1-\sqrt{\eta})^2/\{(1+\sqrt{\eta})^2 4\xi\}\right]/\alpha
```

```math
A_{15}=e^2(1-2e\alpha^2/\eta)/3
```

```math
A_{16}=(\pi e)^2[1+\alpha(1+6\alpha/\pi)/5\eta]
```

```math
A_{21}=2(e\alpha/2\eta)^2(1-\alpha/2\xi^2)
```

```math
A_{22}=\xi[1-\xi(\alpha\xi/\eta^2)^2]/12
```

```math
A_{23}=(\eta^2+6\xi\alpha^2)/e
```

```math
A_{24}=2\xi^2/3\eta
```

```math
A_{25}=\xi(\pi e)^2(1-\beta^2)
```

```math
A_{26}=2\{1-[\pi(e\xi\alpha)^2\sqrt{\eta}]/2\}/e\xi^2
```

```math
A_{31}=(\pi e\alpha)^2[1-(\pi e)^2(1-\beta^2)]
```

```math
A_{32}=\xi^2[1+(2e\alpha/\eta)^2]/6
```

```math
A_{33}=(\pi e\xi\alpha)^2[1-2\pi(e\xi)^2(1-\beta^2)]
```

```math
A_{34}=\eta\sqrt{2\pi\eta}
\tag{XXIV}
```

```math
A_{35}=3\alpha/e\xi^2
```

```math
A_{36}=[1-\pi e(\xi e)^2(1-\beta^2)]^{-1}
```

```math
A_{41}=\{\xi[2+(\xi\alpha)^2]-2\beta\}/(2\beta-\alpha)
```

```math
A_{42}=[\pi\xi^2\eta(\beta-3\alpha)]/2
```

```math
A_{43}=\xi/2
```

```math
A_{44}=2(\eta/\xi)^2
```

```math
A_{45}=(3\beta-\alpha)/6\xi
```

```math
A_{46}=\pi e/\xi\eta-e\eta^2\alpha/2
```

```math
A_{51}=(2\alpha+1)^2
```

```math
A_{52}=6\alpha/\eta^2
```

```math
A_{53}=(\xi/\eta)^3
```

```math
A_{54}=\alpha(\beta-\alpha)\sqrt{3/2}
```

```math
A_{55}=\xi^2
```

```math
A_{56}=(\xi/\eta)^4
```

```math
A_{61}=\pi\xi(2\beta-\alpha)/12\beta
```

```math
A_{62}=\pi^2(\beta-2\alpha)/12
```

```math
A_{63}=(\sqrt{\eta})/9
```

```math
A_{64}=\pi/3\eta
```

```math
A_{65}=\pi/3\xi
```

```math
A_{66}=\xi\eta
```

## Blockers

None for source-image transcription. Do not integrate either worker packet verbatim.

## Required Canonical Changes

- `04_reconstruction/formula_library/SOURCE_CHECK_QUEUE.csv`: set `HT-F-1982-SELECTION-WVX` to checked/source-checked after integration, with a note that this covers only image transcription for OCR lines 250-356.
- `04_reconstruction/formula_library/formula_catalog.csv`: add or update a catalog entry for `HT-F-1982-SELECTION-WVX` with status `source_checked`, implementation status `not_implemented`, source image pages 6-8, and the same transcription-only caveat.
- Add the accepted transcription to the future canonical formula file or split entries named by the integrator. Preserve the original line labels `(XVI)` through `(XXIV)` and the corrected programming form for `w_{\nu x}(k)`.

## Risk Notes To Preserve

- This approval is only an image-vs-OCR source check. It is not normalization, derivation, implementation, or validation.
- The slash binding in terms such as `A_{16}`, `A_{24}`, `A_{35}`, `A_{46}`, `A_{64}`, and `A_{65}` is transcribed as printed and still needs a separate normalization decision.
- The printed `* *` line break in `a_n` is treated as multiplication; preserve the source-layout note if normalized later.
- The direct multiline display of eq. XVI has cramped brace layout near the `(XVI)` label. Use eqs. XVII-XIX as the safer source for the decomposition into `w(1)` and `w(2)`.
- The exponent `A_{34}^{1-q_x}` is visually tight, but the exponent placement is visible on the source scan.
- `k^P(1+P+Q+\kappa\eta^{2-q})` in `b_{\nu x}` is source transcription only; do not silently change it to `kP(1+P+Q+\kappa\eta^2-q)`.
