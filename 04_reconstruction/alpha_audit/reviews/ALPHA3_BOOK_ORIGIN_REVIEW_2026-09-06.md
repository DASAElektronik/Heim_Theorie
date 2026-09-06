# alpha3 / N3 book-origin review — 2026-09-06

## Scope and sources

Bounded source reconstruction only: whether the book supplies the alpha3
formula used by H006(IX), and what status it gives its construction.  No mass
calculation or empirical comparison was performed.

* H004: Heim, *Elementarstrukturen der Materie II* (1996 scan), SHA-256
  `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
  Full pages visually read: printed 270--278 / PDF 276--284, in particular
  printed 271--275 / PDF 277--281.  Rendered controls:
  `tmp/pdfs/alpha3_book_origin/edm2-277.png` through `edm2-281.png`.
* H003: *Elementarstrukturen der Materie I* (1998 scan), SHA-256
  `49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`.
  The supplied full text was searched only as a locator for `alpha3`,
  `eta_qk`, and the H006-style terms; it yielded no concrete alpha3 formula.
  That is a limited search result, not a claim about the entire book.

The Band-I imprint's manuscript date 17-09-1978 and later H010 header dates
are not used to infer that this Band-II formula is an unchanged 1978 or 1982
source.  Matching dates or symbols alone do not establish an edition chain.

## Direct result: H004 has the H010 form, not H006(IX)'s two readings

H004 printed 278 / PDF 284, equation (98c), visibly states

```text
2 alpha1 = 1 + sqrt(eta_qk),     alpha2*eta_qk = 1,
k alpha3 = e^(k-1) - k q F,     alpha4 = 1,     F = H + G,

3 H = alpha (1+sqrt(eta_qk)) (xi/eta_qk^2)^(2k+1) eta_qk^3,
e eta_qk G = eta_11 (2 xi eta_qk)^k
             ((1-sqrt(eta_qk))/(1+sqrt(eta_qk)))^2.
```

Equivalently, for this book's symbols,

```text
alpha3 = e^(k-1)/k - q {
  alpha/3*(1+sqrt(d))*(xi/d^2)^(2k+1)*d^3
  + eta_11/(e*d)*(2*xi*d)^k*((1-sqrt(d))/(1+sqrt(d)))^2 },
where d = eta_qk.
```

The page is unambiguous on the two disputed spellings: the factor
`1+sqrt(eta_qk)` stands outside the `2k+1` power, and the G factor is
`(2 xi eta_qk)^k`, with no root glyph.  It therefore matches the active H010
Pascal/C alpha3 lines, not H006(IX)'s bracketed first factor and visible root
glyph in its second factor.  This establishes a concrete **H004-to-H010
formula correspondence**, not identity of every surrounding notation,
editorial layer, or historical version.

## Book-local construction and its status

* Printed 270--271 / PDF 276--277 introduces zone coefficients alpha_j as
  functions of q and k rather than time-variable zone occupations.  For zone
  3 it proposes `alpha3(k,q)=f(k)-q F(k,q)`.
* Printed 271--272 / PDF 277--278 imposes `f(1)=1` and the stated condition
  `x delta f=(x-1)f`; its displayed integration yields `k f(k)=e^(k-1)`.
  This is the source's derivation of the first term, conditional on that
  functional condition.
* Printed 272--275 / PDF 278--281 sets `F=H+G` and develops H/G from
  metronic variations of internal potential components.  The text explicitly
  calls part of the G identification speculative (p.274), and says the
  coefficients A_i/B_i may be freely prescribed.  The displayed choice
  `A1=B1=B4=1`, `2A2=2k+1`, `2B2=B3=k`, `A3=1-4k` is said to be "der
  Empirie des Elektrons und Protons optimal angepaßt" (p.275/PDF281).
* Printed 275 / PDF 281 then sets the large-metron limit ratio `Y=xi^2` and
  gives the displayed H/G forms; printed 278 / PDF 284 collects them as
  (98c).  Printed 276 / PDF 282 explicitly says alpha occurs in H.

Thus H004 gives a real book-local construction, but it is a chain of source
conditions, proposed/"could" identifications, a stated speculative step, and
an explicitly empirically adjusted coefficient choice.  It is not, on these
pages, a deduction of alpha3 from definitions alone.

## N3 and remaining limits

H004(98c) defines alpha1/alpha2/alpha3/alpha4, but it does not label a
quantity `N3` on these pages.  The H006/H010 relation `N3=2*alpha3` therefore
remains a cross-document/formula correspondence, not a same-page book
definition established here.  Nor do the inspected pages explain why H006(IX)
has its different power scope and root glyph.

The requested narrow conclusion is consequently positive but limited: the
book supports H010's two disputed alpha3 spellings and supplies their stated
construction/motivation; it does not authorize silently replacing H006, prove
a 1978/1982 provenance chain, or settle the H006 scan's root-radicand limit.

## Addendum: elementary exponential check

For positive log arguments, put `d=eta_qk`, `s=sqrt(d)`, and `Y=xi^2` with `xi>0`.
The p.274 relations give exactly `H=xi^(2k+1)*alpha(1+s)/3*d^(1-4k)`
`=alpha(1+s)/3*(xi/d^2)^(2k+1)*d^3`, and
`G=xi^k*eta_11/(e*d)*d^k*2^k*R^2=eta_11/(e*d)*(2*xi*d)^k*R^2`.
So H004(98c)/H010's exponents and parentheses follow from this last algebraic
substitution only; the check does **not** validate the metronic integration,
speculative identification, or empirical coefficient choice.
