# EDM2 book derivation review - 2026-09-06

## Scope and source identity

This bounded source review traces the quantities in EDM2 Eq. (105), printed pp. 297-302, only as far backwards as the inspected primary volume permits. It makes no canonical-formula change, calibration, or predictive claim.

Inspected source: Burkhard Heim, *Elementarstrukturen der Materie: Einheitliche strukturelle Quantenfeldtheorie der Materie und Gravitation*, vol. 2. The title page is PDF folio 1. The imprint (PDF folio 4) says copyright 1984 by Andreas Resch Verlag, Innsbruck; total production Andreas Resch Verlag, Innsbruck 1996; ISBN 3-85 382-036-0; manuscript submitted 20 March 1981. The scan metadata alone is not treated as an edition date. “PDF folio” below means the one-based page number of the local 391-folio PDF.

## The uncertainty-factor policy

PDF folio 12 / printed p. 1 says that uncertainty factors `Y_k` are inserted in mathematical relations that are not yet completely clarified. It then says that, for the theoretical numerical data in the table appendix, **all** `Y_k = 1` were assumed.

Status: **explicit editorial/source statement**. It supports treating `Y_3` as an unresolved degree of freedom. It does not derive a theoretical value, a range, or a target-fitting rule for any particular `Y_k`.

## Dependency chain at Eq. (105)

| Source location | Source content | Status |
| --- | --- | --- |
| PDF 307 / printed p. 301 | Substitution of the “verified assertion (29)” gives `(2 pi)^5 alpha sqrt(1-alpha^2) = 9 vartheta (1-C)`. | Stated derivation, conditional on the earlier assertion (29). |
| PDF 307 / p. 301 | `C ~ A_1 A_2`; with `A = 4 A_1 A_2`, the text says `A ~ C` must hold. | Claimed proportionality, not an equality fixing `C`. |
| PDF 307 / p. 301 | For unit structures with `N=1`, `n_j=0`, and occupied configuration zones, the proportionality factor **could be assumed** to be 4: `A=4C`, or `C=A_1 A_2`. | Explicit assumption/candidate identification, not proved. |
| PDF 307 / p. 301 | An uncertainty then occurs, for which factor `Y_3`, in accordance with the preface, can account. | Explicit introduction of an unresolved factor. |
| PDF 308 / printed p. 302, Eq. (105) | `(2 pi)^5 alpha sqrt(1-alpha^2) = 9 vartheta (1-A_1 A_2 Y_3)`, `alpha>0`; also `(1+sqrt(eta_1k)) A_k = (1-sqrt(eta_1k))sqrt(eta_1k)`. | Printed working/defining equation. |
| PDF 308 / p. 302 | With `alpha=alpha'`, neglect of `alpha^2 << 1`, `A_1A_2 << 1`, and `Y_3=1`, (105) becomes approximation (29a). | Explicit approximations and selected input. |
| PDF 308 / p. 302 | “Mit `Y_3=1`” defines `2B=[(2pi)^5/(9 vartheta)]^2 (1-A_1A_2)^-2`, solves the quadratic, and prints reciprocal branches `137.03596147` and `1.00001363`. | Example calculation conditional on `Y_3=1`, not a determination of `Y_3`. |

```text
earlier assertion (29) + H-atom correlation argument
  -> 9 vartheta (1-C)
  -> C ~ A1 A2; candidate C = A1 A2
  -> unresolved proportionality represented by Y3
  -> Eq. (105): 1 - A1 A2 Y3
  -> selected numerical case Y3 = 1
  -> B and the two printed alpha branches
```

The arrows through `C ~ A_1 A_2` are not algebraic equalities until the candidate and `Y_3` specialization are made. A value of `Y_3` recovered from a target alpha is therefore an inverse/ex-post diagnostic of the displayed equation, not a book-derived prediction.

## `A_k`, eta, and vartheta

Equation (105) supplies the local `A_k` definition:

```math
(1+sqrt(eta_{1k})) A_k = (1-sqrt(eta_{1k}))sqrt(eta_{1k}).
```

Ordinary algebra therefore gives `A_k=sqrt(eta_1k)(1-sqrt(eta_1k))/(1+sqrt(eta_1k))`, where the denominator is nonzero. This is a derived rearrangement, not an extra book assertion. It establishes the literal inputs `eta_11` and `eta_12` for `A_1A_2`, but not their numerical values.

PDF folio 42 / printed p. 33 gives:

```math
vartheta = 5 eta + 2 sqrt(eta) + 1.
```

That page introduces this while deriving numerical factors from relations (29) and (32), calling (29) the “exact presentation” of the elementary field. Hence `vartheta` is explicitly dependent on unindexed `eta`, but the inspected material does not explicitly identify that `eta` with `eta_11` or another indexed term.

Status summary:

- `A_k` in literal `eta_1k`: **defined in Eq. (105)**.
- `vartheta` in unindexed `eta`: **explicitly given on p. 33**.
- Functional definition of `eta_ik`/`eta_1k`, including which coordinate each slot represents: **not located in this volume during this bounded review**.
- Identification of unindexed `eta` with a particular indexed eta: **not established**.

The gap is expected from the source architecture: the introduction says this volume frequently refers to physical numbered relations from volume 1 and that they are listed in a separate accompanying booklet. Neither was inspected here. A reference to (29) inside this PDF is not an explicit eta-index definition in this PDF.

## Does the book fix, exemplify, or fit `Y_3`?

The observed answer is **exemplify/specialize, not fix and not invite fitting**. The text introduces `Y_3` at an acknowledged uncertainty in moving from proportionality to `C=A_1A_2`; it then sets `Y_3=1` for the approximation and branch calculation. The preface gives the same general all-`Y_k=1` numerical policy. No inspected line derives `Y_3=1`, supplies a range, or permits fitting it to measured alpha.

Any reconstructed model must therefore retain `Y_3` as an unresolved, explicitly chosen parameter unless it adds and labels a new theoretical closure. A target-derived value must be marked ex-post fitting, even when used only to diagnose the printed equation.

## Eta index order and the 1982 swapped variant

Eq. (105) uses `eta_1k`, so its immediate inputs are syntactically `eta_11` and `eta_12`. It does **not** state which coordinate occupies the first or second position, or provide an `eta_ik` function. The separate `SOURCE_REVIEW_2026-09-06.md` visually establishes that the 1982 alpha source explicitly writes `eta_kq=pi/[pi^4+(4+k)q^4]^(1/4)` and then uses `eta_11` and `eta_12`.

EDM2’s bare `eta_1k` does not resolve that source-local `(k,q)` order. Treating the positions as swapped when evaluating the 1982 `eta_12` needs an extra convention, not a silent reading of Eq. (105).

Conclusion: **No.** The original book’s `eta_1k` occurrence is insufficient to source-support the IGW1982 swapped-index variant. It supports two eta-indexed inputs but leaves their semantic order unresolved. Literal and swapped 1982 evaluations must remain separate variants unless an explicit eta-definition source bridges them.

## Boundaries and rendered-image record

- No modern alpha value, target fit, numerical reconstruction, web source, or external formula booklet was used.
- The book equation is not source-identical to the 1989 `1-C'` chain; this review does not assign the numerical drift to one term.
- Next source target: volume-1 relation (29) or the accompanying formula booklet, specifically a page defining the eta function and both index coordinates.

Rendered, ignored intermediates:

- `tmp/pdfs/book_derivation/imprint-001.png` (title, PDF 1) and `imprint-004.png` (imprint, PDF 4)
- `tmp/pdfs/book_derivation/intro_start-012.png` (policy, PDF 12 / p. 1)
- `tmp/pdfs/book_derivation/theta_def-042.png` (vartheta, PDF 42 / p. 33)
- `tmp/pdfs/book_derivation/detail-307.png` (Y3 introduced, PDF 307 / p. 301)
- `tmp/pdfs/book_derivation/detail-308.png` (Eq. 105 and Y3=1, PDF 308 / p. 302)
