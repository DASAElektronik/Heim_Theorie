# Alpha Source Review - 2026-09-06

Reviewer model: `gpt-5.6-terra`
Scope: bounded source audit of the 1982/1989 alpha blocks and their eta-index provenance. This is an evidence review only; it makes no canonical-file change, implementation change, fit, or historical-validation claim.

## Material inspected

- Raster source pages inspected visually: **6**.
  - 1982: `07_outputs/source_check_images/1982_massenformel/page-03.png`, `page-04.png`, and the cross-reference page `page-05.png`.
  - 1989: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-03.png`, `page-04.png`, and `page-09.png`.
- Extracted-text files inspected: `Massenformel_nach_B_Heim_1982.txt`, `Erweiterte_Massenformel_Nach_Heim_1989.txt`, and the narrowly searched `Elementarstrukturen_der_Materie_2.txt`.
- The book evidence below is from its extracted text (printed book pp. 297 and 302-303); its page image was not independently inspected in this bounded review.

## 1982: confirmed source reading

`1982_massenformel/page-03.png`, label `(V)`, visibly gives:

```math
\eta = \pi/(\pi^4+4)^{1/4},\qquad
\eta_{kq}=\pi/[\pi^4+(4+k)q^4]^{1/4},\qquad
\vartheta=5\eta+2\sqrt{\eta}+1,
```

with `A_1` using `eta_11` and `A_2` using `eta_12`. `page-04.png` visibly gives:

```math
\alpha\sqrt{1-\alpha^2}=9\vartheta(1-A_1A_2)/(2\pi)^5,\quad \alpha>0.
```

The coefficient is **`9 vartheta`**, not `99`. The same page prints the reciprocal branch values exactly as

```text
alpha_(+)^-1 = 137,03596147
alpha_(-)^-1 = 1,00001363
```

and then identifies `alpha_(+) = alpha`, `alpha_(-) = beta approx. 137 alpha`. This agrees with `HT-F-1982-ALPHA.md` and its source-literal handling in `NORM-1982-ETA-INDEX`.

## 1989: equations, B62 values, and reciprocal-box check

On `1989_erweiterte_massenformel/page-09.png`, the source visibly gives:

```math
\alpha\sqrt{1-\alpha^2}=\frac{9\vartheta}{(2\pi)^5}(1-C') \tag{B58}
```

```math
1-C'=1-
\frac{1+\eta_{2,2}}{\eta\eta_{1,1}\eta_{1,2}}
\left(\frac{1-\sqrt{\eta}}{1+\sqrt{\eta}}\right)^2
=K_\alpha \tag{B59}
```

```math
\alpha_{(\pm)}^{-2}=\tfrac12D'^2\left(1\pm\sqrt{1-4/D'^2}\right),\qquad
D'=(2\pi)^5/(9\vartheta K_\alpha). \tag{B60--B61}
```

This directly supports the full-chain scope in `NORM-1989-ALPHA-B59-KALPHA-SCOPE`: `K_alpha` is the whole `1-C'`, not the inner eta term.

The printed `(B62)` decimals are exactly:

```text
alpha_(+) = 0.0072973525253328589
alpha_(-) = 0.999985890199089
```

The immediately following boxed reciprocal line is exactly:

```text
1/alpha_(+) = 137,03601,     1/alpha_(-) = 1,0000142
```

The box is therefore a separate printed assertion, not an exact reciprocal rendering of the preceding finite decimals. Direct reciprocal arithmetic on the printed B62 decimals gives:

```text
1 / 0.0072973525253328589 = 137.035999909348815...  (rounds to 137.03600 at 5 decimals)
1 / 0.999985890199089     = 1.000014110000000...    (rounds to 1.0000141 at 7 decimals)
```

Thus the boxed values differ from these displayed-decimal reciprocals by about `1.0091e-5` and `9.0e-8`, respectively. Do not use either box value as a regression target for an evaluation based only on the displayed B62 decimals; retain both source facts and the discrepancy. `HT-F-1989-ALPHA.md` correctly preserves both printings, but does not itself state this arithmetic non-identity.

## 1989 eta definitions and coordinate order

The 1989 alpha page (`page-09.png`) contains `eta_(2,2)`, `eta_(1,1)`, and `eta_(1,2)` in B59 but does **not** redefine eta locally.

The relevant earlier 1989 source page is `1989_erweiterte_massenformel/page-03.png`: it visibly says that the constants `eta_(q,k)`, `vartheta`, and `eta` (including `eta_(1,0)=eta` and `vartheta_(1,0)=vartheta`) "lauten wie in (IX)". This is a source cross-reference, not a new local definition.

The referenced `(IX)` is visibly available in `1982_massenformel/page-05.png` and defines:

```math
\eta_{qk}=\pi/[\pi^4+(4+k)q^4]^{1/4}.
```

Accordingly, the cross-source reading of the 1989 B59 symbols is **subscript order `(q,k)`**: `eta_(1,2)` denotes `q=1, k=2` under the formula inherited through `(IX)`. This must remain distinct from the source-local 1982 ALPHA abbreviation on `page-03.png`, which visibly writes `eta_(kq)` before using `eta_12`. The source materials establish a notation/order transition; they do not authorize silently applying the 1982 ALPHA `(k,q)` order to 1989 B59.

## Narrow book evidence on the IGW-value drift

The narrowly relevant extracted-book passage is `Elementarstrukturen_der_Materie_2.txt`, printed pp. 297 and 302-303:

- p. 297 characterizes the earlier theoretical approximation as numerically faulty and says internal structuring had not been accounted for.
- p. 302, following Eq. `(105)`, prints the older reciprocal pair `137,03596147` and `1,00001363`, identifies the positive value as approximately `0,007297354572`, and labels the other branch `beta = 0,99998637` (OCR formatting is imperfect, but the numerical sequence is readable).
- p. 302-303 then assigns the strong branch to possible internal correlations and writes the `beta approx. 137 alpha` relation.

This is consistent with the 1982/IGW presentation, not the 1989 B62 pair. Independently, the 1989 source introduction on `page-09.png` says that the value previously calculated in Chapter D section 8 still had a small error and presents B58 with `C -> C'` as the exact formula. These are documentary explanations for why the IGW/1982 and 1989 printed values differ. They do **not** establish that the later expression is derivable from the book OCR, nor do they resolve the B62-to-box arithmetic discrepancy.

## Unresolved gaps and boundaries

- No 1989 page inspected here independently derives the `(IX)` eta formula; page 03 explicitly delegates it to `(IX)`. The coordinate conclusion is therefore a documented cross-source reference-chain result, not a local B59 definition.
- The book equation typography around `(105)` is too degraded in extracted text for a fresh formula transcription. Only the printed page-numbered numerical/contextual evidence above is relied upon.
- No target fitting, third-party implementation, web lookup, or comparison to modern alpha data was performed.
- Canonical formula files and normalization decisions were read for comparison only and were not edited.
