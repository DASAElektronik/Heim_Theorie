# (79)/(79a), exponential approximation, and the p. 269 reference — 2026-09-06

Scope: a bounded, source-led reconstruction of the exact local reference
from Book II printed p. 269 back to (79), (79a), and the immediately derived
(79b).  The aim is to identify the function, parameters, domain, and the
meaning of `mu;n -> r`; it is **not** a reconstruction of the later general
definitions of `F_i`/`G_i`, a correction of the book, or a physics verdict.

## Result

The direct antecedent **states/claims** an asymptotic spatial exponential
decay in the book's third validity region.  It does not define
`F_i` or `G_i`, does not identify them with `V_i`/`Q_i`, and supplies no
sign convention that turns the later p. 269 condition into its printed
potential-ratio inequality.  It therefore explains why p. 269 invokes an
exponential profile, but does **not** close or repair the already-recorded
configuration-selection derivational knot.

The p. 178 / PDF 184 large-distance expression used verbatim in p. 269 is

```text
psi(r) ~ e^(lambda r)
  [ (1/2) sqrt((1+b)/(1-b)) (e^(lambda r)-b)^2 ]^(-a/(2 lambda))
  ~= exp((lambda-a) r) = e^(-alpha r),  alpha>0.
```

At p. 269 this is applied to the C-structure of the charge field on
`(+7)_d`, where `r` is explicitly an `R3` distance from the `(+7)_d` centre
and `mu;n -> r` is made in the third validity region.  This is a source
analogy/application; p. 177–179 do not call the earlier field itself that
specific C-structure.

## Source chain and the functions printed

| Location (PDF folio / printed page) | What is visibly printed | Evidentiary status |
| --- | --- | --- |
| 181 / 175 | The real solution is written as an exponential relation with `varphi=lambda_kl mu - ...`; it calls `a=a*` real.  It states that the following differential/integral discussion is only along `mu` in `R3`. | Local setup for the `mu` variable and real `a`; no p. 269 selection variables yet. |
| 182 / 176 | With `lambda=lambda_kl` as an abbreviation, it puts `b=cos(lambda T)=const(R3)`, after separating a complex quantity into real and imaginary parts.  It uses `x=lambda mu=ln w` and `u=(w-b)/sqrt(E-b^2)`.  The terminal displayed differential has a denominator `E+u^2`. | Direct definition of `b` and of the exponential variable `w`; `b` is not an independently fitted coefficient here.  The sign is retained as a source-check marker because p. 178's later transformed equation displays `E-u^2`; no metronical correction is made here. |
| 183 / 177, Eq. (79) | The relevant factor is of the form `a^i_kl e^(lambda_kl mu) [ (1/2)(E+cos K) {E+(e^(lambda_kl mu)-cos K)^2 sin^(-2)K} ]^(-a/(2 lambda_kl))`, with `K=lambda_kl T`, followed by definitions of `T`, `mu`, and `a`. | Source equation from which the later asymptotic expression is developed.  The tensor/prefactor notation is deliberately abbreviated here; its scalar exponential and bracket factors are retained. |
| 183 / 177, Eq. (79a) | It says nonzero real spatial condensation requires `K != 0`; integer `K;n=+-pi N` gives no condensation, while the maximal case is the half-integer spectrum `K;n=+-pi(2N+1)/2`, for which `cos K=0`, `sin K=+-E`. | The label `(79a)` is a maximal-condensation specialization, not itself the final `e^(-alpha r)` formula. |
| 184 / 178 | It considers the `R3` extremum for `0<|cos K|<E`, says the positive branch is selected because `cos K>0` and `w=e^(lambda mu)>0`, and obtains `A=lambda_kl/a` with `0<A<E`; it **prints the conclusion** “`A<E` bedeutet aber auch `a>lambda_kl`.” | The book's stated domain/sign selection before the large-distance limit.  This review does not certify that conclusion as a complete independent derivation. |
| 184 / 178 | For `tau -> 0`, it prints `lim(mu;n)=r`; inserting this in (79), for sufficiently large `r`, gives the displayed `psi(r)` formula and its exponential approximation.  It adds **`e^(lambda r) >> b`** and, still more, **`e^(lambda r) >> 1`** in this approximation region. | Direct source of the `mu;n -> r` step and of the stated asymptotics. |
| 185 / 179, Eq. (79b) | It names the result `psi(r) ~ e^(-alpha r), alpha>0`, calls it an exponentially steeply decaying `R3` structural field with near-action-field properties, and calls the region the third (infinitesimal) validity region `tau -> 0`. | The book's own interpretation of the approximation; still no `F_i`/`G_i` definitions. |
| 275 / 269 | For the C-structure on `(+7)_d`, `r` is an `R3` distance; it writes `mu;n -> r` in the third validity region and repeats the p. 178 approximation.  It then says that because of this exponential course one *could* assume an expression whose summands map to `F2-F1+G2-G1`, conditional on its energetic nature being positive. | Direct but conditional reuse.  The later identification `F_1,2=V_1,2`, `G_1,2=Q_1,2` is separately labelled speculative on this page. |

## Parameters and the permitted branch

The notation is dense; the bounded evidence supports the following, without
adding a conventional physical interpretation.

| Symbol | Source-local meaning / condition |
| --- | --- |
| `lambda=lambda_kl` | Abbreviation on p. 176.  It occurs in denominators in (79), so the displayed construction excludes `lambda=0`.  P. 178 asserts `e^(lambda r)>>1` for sufficiently large positive `R3` distance.  On the ordinary real large-`r` reading this selects **`lambda>0`**; the book does not separately typeset that strict inequality. |
| `a` | A real quantity in the p. 175 setup.  P. 178 defines the uppercase ratio `A=lambda/a`, requires `0<A<E`, and **states** that this means `a>lambda`.  This report records that source assertion; it does not pre-empt the separate mathematical check of that implication.  Conditional on `lambda>0` and the printed `a>lambda`, the asymptotic exponent has positive decay rate `a-lambda`. |
| `b` | `b=cos(lambda T)=const(R3)` (p. 176).  The nonzero/positive p. 178 branch has `0<cos K<E`; with `K=lambda T` and the scalar square-root form later used, this is the finite real branch normally rendered `0<b<1`.  The endpoints are excluded in the source's nonzero-condensation discussion: `sin K=0` at the integer spectrum.  Separately, the large-distance approximation states `e^(lambda r)>>b` and `>>1`. |
| `A` | The p. 178 uppercase ratio `A=lambda/a`, used in the extremum discussion.  It is not the later proportionality factor called `A` on p. 269; the book reuses the letter in different local roles. |
| `alpha` in `e^(-alpha r)` | The equality `exp((lambda-a)r)=e^(-alpha r)` makes the decay rate read as `a-lambda>0` in that line.  The same printed page also used a lower-case alpha-like glyph in the ratio condition `lambda/a=A`; this review does not silently identify those two roles beyond what the adjacent equalities force. |
| `mu;n -> r` | P. 178 takes the `tau -> 0` limit of the book's `mu;n` parametrisation and writes its limit as `r`; p. 269 applies it to an `R3` distance.  The source does not equate `n` with laboratory time or with the later configuration number `k` in this chain. |

The formal square root in the large-`r` expression also shows why the branch
restriction matters.  It is not enough merely to copy an exponential:
the source first chooses the positive `cos K` branch and then employs the
finite, real `b` range before taking the asymptotic form.

## What this context says about the p. 269 selection step

1. The antecedent provides the book's stated rationale for p. 269's phrase
   “wegen dieses exponentiellen Verlaufes”: it reports
   `psi(r)~e^(-alpha r)` in an `R3` limit.  Independently, the displayed
   large-`r` algebra has that decaying form if `lambda>0` and `a>lambda` are
   imposed; this is a conditional mathematical observation, not validation
   of the book's extremum argument.
2. It does not introduce the p. 269 `F_1,F_2,G_1,G_2` labels, nor `V_1,V_2,
   Q_1,Q_2`.  The earlier positive-root and extremum conditions concern
   `w`, `cos K`, and the spatial profile, not an inequality between those
   later pairs.
3. Consequently the preceding pages do not source-authorise changing the
   p. 269 ordering of `F`/`G`, its speculative identification, or the
   subsequent potential-ratio inequality.  At most they establish the
   decay premise to which p. 269 explicitly refers.

This conclusion is deliberately narrow.  A separate review of the general
`F/G` definitions and sign conventions would be needed to investigate any
further bridge; it is outside this source slice.

## Visual record and boundaries

Visually inspected primary-PDF renders, all in the ignored scratch area:

- `tmp/pdfs/exponential/edm2-181.png` through `edm2-185.png`
  (printed pp. 175–179 / PDF folios 181–185)
- `tmp/pdfs/exponential/edm2-275.png`
  (printed p. 269 / PDF folio 275).
- `tmp/pdfs/exponential/p178-hi-184.png`
  (500-dpi check of p. 178's `>>` glyphs and parameter statements).

No numerical evaluation, formula modification, historical emendation,
modern literature search, or edit outside this review file was performed.

## Root visual supplement: (79c)

Root independently inspected the full printed p. 179 / PDF folio 185
(`tmp/pdfs/exponential_context/edm2-185.png`). Below (79b) it explicitly
prints `r=r(nu), delta r -> beta=const>0` as (79c). The preceding text
places this near the upper limit of the second validity region at high
metron numbers, with tau>0 and an approximately constant radial increment.
This supplements the source review's direct (79b) chain; it is not a
derivation of that metronic transition or an identification of nu with
the later configuration index k. Root's stage report therefore retains
the visually confirmed (79c) reference.
