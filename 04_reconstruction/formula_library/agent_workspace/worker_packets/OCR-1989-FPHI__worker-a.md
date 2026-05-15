# OCR source-check: HT-F-1989-FPHI

Verdict: ready

Image pages used:
- `07_outputs/source_check_images/1989_erweiterte_massenformel/page-02.png` for B5 start
- `07_outputs/source_check_images/1989_erweiterte_massenformel/page-03.png` for B6-B14

Accepted source-visible transcription

- B5:
  `F = 2 n Q_n [1 + 3(n + Q_n + n Q_n) + 2(n^2 + Q_n^2)] + 6 m Q_m (1 + m + Q_m)N_2 + 2 p Q_p N_3 + \phi * \delta(N)`

- B6:
  `\Phi = P(-1)^(P+Q) (P + Q) N_5 + Q(P + 1) N_6`

- B7:
  `mit \phi = \phi(p,\sigma) und \delta(0) = 1 (0 für N \neq 0),`

- self-coupling / source line after B7:
  `\phi = [N_4 p^2/(1+p^2)] [(\sigma + Q_\sigma)/\sqrt{1+\sigma^2}] (4\sqrt{2} - 4 B U W_{N=0}^{-1}) + P(P - 2)^2(1 + \kappa(1-q)/(2\alpha)\,\vartheta)\cdot(\pi/e)^2\sqrt{\eta_{12}}(Q_m-Q_n) - (P + 1)(Q/3)/\alpha`
  `vergl. (B49)`

- U / Z:
  `U = 2^Z [P^2 + 3/2 (P - Q) + P(1-q) + 4\kappa B (1-Q)/(3 - 2q) + (k - 1){P + 2Q - 4\pi(P - Q)(1 - q)/\sqrt{2}}] \eta_{qk}^{-2}`
  `Z = k + P + Q + \kappa`

- B8:
  `\ln(N_3 k/2) = (k - 1)\left[1 - \pi \frac{1 - \eta_{q,k}}{1 + \sqrt{\eta_{q,1}}}\left\{1 - u\,\frac{\eta_{q,1}}{\vartheta_{q,1}}(1 - \alpha_- / \alpha_+)(1 - \sqrt{\eta})^2\right\}\right] - \frac{2}{3\pi e}(1 - \sqrt{\eta})^2\left(\frac{6\pi^2 e^2}{\vartheta}\frac{1+\sqrt{\eta_{q,1}}}{1-\eta} - 1\right)`

- B9:
  `N_4 = (4/k) [1 + q(k - 1)]`

- B10:
  `N_5 = A[1 + k(k - 1) 2^{k^2+3} N(k) A \left(\frac{1 - \sqrt{\eta_{q,k}}}{1 + \sqrt{\eta_{q,k}}}\right)^2]`

- B11:
  `A = (8/\eta)(1 - \alpha_- / \alpha_+)(1 - 3\eta/4)`

- B12:
  `N(k) = Q_n + Q_m + Q_p + Q_\sigma + k(-1)^k 2^{k^2-1}`

- B13:
  `N_6 = 2k/(\pi e \vartheta)\left[\sqrt{k}(k^2 - 1)\frac{N(k)}{\sqrt{\eta_{1,k}}}\left\{q - (1-q)\frac{N'(k)}{Q_n\sqrt{\eta_{1,k}}}\right\} + (-1)^{k+1}\right]\eta(1 - \alpha_- / \alpha_+)\left(\frac{1 - \sqrt{\eta}}{1 + \sqrt{\eta}}\right)^2 Q_\sigma`

- B14:
  `N'(k) = Q_n + Q_m + Q_p + Q_\sigma - 2k - 1`

OCR corrections vs current formula file

- B6: the source confirms the exponent is `(-1)^(P+Q)`; keep the full exponent scope on `-1`.
- B7: the source line is `\phi = \phi(p,\sigma)` and `\delta(0) = 1 (0 für N \neq 0),` with the parenthetical limit note.
- self-coupling line: the current file does not carry the source-visible structure for `N_4`, `Q_\sigma`, `\sqrt{1+\sigma^2}`, `U W_{N=0}^{-1}` / `BUW` reading, `\eta_{12}`, or `(Q/3)/\alpha`; these need to stay literal until the glyphs are resolved.
- U/Z: the source has `U = 2^Z ... \eta_{qk}^{-2}` and `Z = k + P + Q + \kappa`; the current file omits both lines entirely.
- B8-B14: the current file is only a normalized outline; the source adds `N_3`, `N_4`, `N_5`, `A`, `N(k)`, `N_6`, and `N'(k)` with the exact powers, radicals, and nested fractions above.

Unresolved glyph / notation risks

- B7/B8: `u` may be a literal `u` or a Greek `\nu`; do not normalize it yet.
- self-coupling line: `BUW_{N=0}^{-1}` is the best source-visible reading, but the glyph grouping around `B U W` and the `N=0` placement is still fragile.
- B8: the `\sqrt{\eta}` scope in the last factor and the `\vartheta` placement inside the trailing parentheses are source-visible but line-wrap sensitive.
- B10/B13: confirm the exponent scopes `2^{k^2+3}` and `(-1)^{k+1}` before any implementation pass.
- page break: B5 ends cleanly on page 02 and B6 starts after the page 03 header; no cross-page carry-over is required, but keep the page break in mind when reconciling OCR line numbers.

Implementation implications

- No implementation in this packet.
- If this is used for reconstruction, keep the source literal forms above and resolve the ambiguous glyphs before touching canonical formula or queue files.
