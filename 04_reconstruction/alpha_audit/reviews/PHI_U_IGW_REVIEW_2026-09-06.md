# phi/U in H007: bounded source review

Date: 2026-09-06  
Scope: visual transcription and dependency reconstruction only for H007
`Erweiterte_Massenformel_Nach_Heim_1989.pdf`, especially B3--B5,
B22--B28, and B47--B51.  The undated H013 scan is used once as an
independent handwriting/line-break comparison, not as a date or an
erratum.  No formula has been numerically evaluated or silently
normalised here.

## Source status and checked pages

H007 is headed *Einfuehrung in die Heimsche Massenformel*, IGW Innsbruck
2003.  Its introduction says that it presents a reported 1989 extension,
but also says that the original program is missing and that some brackets
in long manuscript equations had to be supplied by estimates.  The review
therefore treats the printed H007 glyphs as evidence for the 2003 IGW
edition; it does not attribute every typography decision directly to Heim
or infer a previously unknown 1989 manuscript reading.

The following full pages were visually inspected:

| H007 PDF folio | printed page | material |
| --- | ---: | --- |
| 2 | 11 | B3--B5 (mass formula and the two differently cased Phi/phi symbols) |
| 4 | 13 | B22--B28 (`W_{N=0}`, `H`, and the local `B`) |
| 7 | 16 | B47--B48 (existence-time relation and `y`) |
| 8 | 17 | B49--B51 (`phi`, `U`, and `Z`) |
| 11 | 20 | stated uncertainty/empirical-adjustment passage |

Rendered visual anchors used: `tmp/pdfs/eta22_roles_igw/h007-pre-04.png`,
`tmp/pdfs/eta22_roles_igw/h007-07.png`,
`tmp/pdfs/eta22_roles_igw/h007-08.png`, and
`tmp/pdfs/eta22_roles_igw/h007-11.png`.

## Literal local dependency chain

### Mass side

At H007 Druck 11/PDF 2, (B3) has the displayed structure

```text
M = mu alpha_+ [(G + S + F + Phi) + 4 q alpha_-].
```

(B4) then defines `alpha_+` and `alpha_-`; no lower-case `phi`, `U`, or
`W_{N=0}` occurs visibly in (B4).  The next displayed abbreviation, (B5),
ends in lower-case `phi * delta(N)`, while the other abbreviation in the
same block is capital `Phi`.  These are not interchangeable symbols.  The
text below the block defines `phi = phi(p,sigma)` and gives
`delta(0) = 1` and `delta(N) = 0` for `N != 0`.

Thus the narrowly source-supported mass connection is

```text
B50 -> U -> B49 -> phi -> [phi delta(N) in F, B5] -> M (B3).
```

In particular, the displayed direct contribution of B49's lower-case
`phi` to `M` through `F` is gated by `delta(N)`; it is not a statement that
capital `Phi` is B49's correction.  This does not establish any inverse
dependency of `U` on a measured mass.

### W0, U, phi, and lifetime side

H007 Druck 13/PDF 4 calls `W_N=0` the excitation-independent factor and
defines it in (B22).  Its immediately printed inputs are `A`, `x`,
`eta`, `L`, `P`, and `Q`; the adjacent (B23)--(B28) define, among others,
`H = Q_n + Q_m + Q_p + Q_sigma` and

```text
B = 3 H [k^2 (2k - 1)]^-1.                     (B28)
```

No literal `M`, existence time `T`, or lower-case `phi` argument is
displayed in this local definition of `W_N=0`.  That is only a statement
about the printed dependency list, not a claim of global independence in
the theory.

H007 Druck 16/PDF 7 makes two further uses explicit: (B47) takes `M` in
the existence-time relation, and (B48) defines the substitution `y` with
both `phi` and `b_2/W_N=0`.  The next page gives

```text
phi = (N_4 p^2/(1+p^2)) ((sigma+Q_sigma)/sqrt(1+sigma^2))
      * (fourth_root(2) - 4 B U W_(N=0)^(-1))
      + P(P-2)^2 (1 + kappa(1-q)/(2 alpha vartheta))
        (pi/e)^2 sqrt(eta_12)(Q_m-Q_n)
      - (P+1) choose(Q,3)/alpha .              (B49, normalized notation)
```

The normalised notation in this display only expands visible source
grouping and the vertical binomial stack; it does **not** decide B50's
sign.  Visual evidence attaches the inverse and the `N=0` subscript to
`W`, so the first B49 bracket is
`fourth_root(2) - 4*B*U*W_(N=0)^(-1)`, not an inverse of all three letters.
The prose immediately below B51 says that `B` is obtained from (B28).

Consequently the source-visible paths are

```text
B28 -> B; B22 -> W_N=0; B50 -> U
                         \         \
                          -> B49 phi -> B48 y -> B47 T
                                        \
                                         -> B5 F -> B3 M -> B47 T
```

This diagram records occurrences and substitutions only.  In particular,
it does not turn `b_2/W_N=0` in B48 into an independent mass term.  The
separate, delta-gated B49-phi-to-F-to-M route above is explicitly present.
Nor does the diagram turn either route into an empirical fit.

## B50: exact points that are and are not resolved

The H007 PDF 8/Druck 17 line begins visibly

```text
U = 2^Z [ P^2 + 3/2(P-Q) + P(1-q)
          + 4 kappa B(1-Q)/(3-2q)
          + (k-1){ P + 2Q -
                    - 4 pi(P-Q)(1-q)/fourth_root(2) } ] eta_qk^(-2).
                                                        (B50)
Z = k + P + Q + kappa.                                (B51)
```

`2^Z`, rather than `2 Z`, is visually clear.  This is a confirmation of
the already-correct transcription, not a new discovery or a new
normalisation decision.  The outer square bracket, the inner braces after
`(k-1)`, and the final multiplier `eta_qk^(-2)` are also visually present.

The inner expression retains **two visible minus marks**: one at the end
of the `P+2Q -` line and a second at the start of `- 4 pi...`.  The source
does not tell the reader whether that means a single continuation minus, a
double negative, or an editorial/typographic artefact.  It is therefore
not executable as a source-default sign.

H013, *Ausgewaehlte Ergebnisse* (undated author scan), Druck 30/PDF 33,
was visually consulted solely as an independent comparison.  Its (21b1)
also ends the first line with `P+2Q -` and begins the next with a minus
before the `4 pi` term.  The same page has a line-broken final minus in
the preceding phi expression.  That supplies a plausible **version-family
or line-continuation hypothesis**, but neither page labels it a correction
and the scan has no date that proves priority.  It is not evidence for an
erratum to H007 and cannot select a B50 sign.

Image used for that limited comparison:
`tmp/pdfs/eta22_roles/j0033-hi-33.png`.

## Reconciliation with existing normalisation decisions

| item | current finding | status for an implementation |
| --- | --- | --- |
| `NORM-1989-FPHI-B49-SCOPE-BLOCKER` / `...B49-SCOPE` | B49's `kappa(1-q)/(2 alpha vartheta)` is a denominator product; the Q-over-3 stack is a binomial; terms are three addends as recorded. | resolved scope only |
| `NORM-1989-FPHI-BUW-TOKEN-BLOCKER` / `...BUW-PRODUCT-SCOPE` | H007 again visibly supports `B * U * W_(N=0)^(-1)` and attaches the inverse to W. | resolved scope only |
| `NORM-1989-FPHI-B50-DOUBLE-MINUS-BLOCKER` | H007 literally retains two minus signs; H013 has an analogous line break but supplies no authorised correction. | unresolved; preserve literal, single-minus and double-negative variants separately |
| `2^Z` token | visible in H007 (B50), and compatible with H013's corresponding displayed exponent. | already resolved; do not manufacture a `2Z` alternative |

## What the edition itself says about adjustment and limits

H007 Druck 20/PDF 11 says that, in the expression for `phi` with (B50),
freely selectable parameters were adapted to empirical circumstances; it
lists `fourth_root(2)`, `(pi/e)^2`, and `4 pi fourth_root(1/2)`.  That is
an explicit editorial/source claim of empirical adjustment for those named
pieces.  It neither identifies a B50 sign nor proves that `eta_qk`, `U`,
or the mass path was fitted to a particular datum.

The same page calls the N>0 calculation uncertain because relations
(B33)--(B36) are not yet well secured and says existence times for such
states cannot yet be described.  These qualifications rule out presenting
the local dependency reconstruction as a completed predictive mass or
lifetime calculation.

## Bounded conclusion

The source supports a concrete dependency `U -> phi`, and supports both a
delta-gated mass route through B5/B3 and a lifetime route through B48/B47.
It also supports the local B49 product `B*U/W_N=0`, the B28 meaning of
this `B`, and the superscript reading `2^Z`.  It does not source-resolve
the B50 double-minus, infer a missing bracket, infer a numerical sign from
agreement, or establish an H013-to-H007 erratum.  Any numerical use of
B49 that depends on `U` must therefore retain the B50 sign blocker
explicitly.
