# Metronic operator chain behind H004 alpha3 -- 2026-09-06

## Scope and sources

This is a bounded primary-source check of the operations used on H004 II
printed pp.273--274 / PDF279--280.  It reads the directly relevant H003 I
definitions on printed pp.102--111 / PDF108--117, not the whole metronic
programme.  Visual checks used
`tmp/pdfs/metronic_operator/edm1-108.png`--`edm1-117.png` and the already
checked `tmp/pdfs/alpha3_book_origin/edm2-279.png`--`edm2-281.png`.

* H003 I, SHA-256
  `49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`.
* H004 II, SHA-256
  `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

## What the earlier book defines

H003 I103 / PDF109 labels the metronic differential (M2)

```text
delta phi = phi(n) - phi(n-1),       0 <= n <= N.
```

as the backward, unit-step operation on an integer metron index.  This is
presented as a definition of the author's own discrete operation, not as a
differential limit.  The accompanying discussion excludes a forward quotient
at the upper boundary and selects the minimum positive step v=1.

For an integrand that is itself a metron differential, H003 I104 / PDF110
defines the bounded Metronintegral (M2a), with `n1 >= 1`, `n2 > n1`, as a
sum and obtains exactly in that formalism

```text
S(n1..n2) delta Phi(n) = Phi(n2) - Phi(n1-1).
```

Thus the lower endpoint is shifted by one discrete step.  H003 I107--108 /
PDF113--114 reiterates the asymmetric endpoint behaviour and the condition
that an integrand has a primitive `Phi` with `delta Phi = phi` (M5).  It also
gives a non-ordinary product rule on I105/PDF111,
`delta(uv)=u delta v+v delta u-(delta u)(delta v)`, and says on I111/PDF117
that an analogue of a general chain rule is only rarely usable; delta must
generally be carried out individually.  Ordinary differential rules therefore
cannot be silently substituted here.

## Logarithms: explicitly a small-variation regime

H003 I109 / PDF115 (M7) introduces a *scaled* variation
`delta_e = a delta` with `0 < |delta_e| << 1` (the stated sufficient
metron-scale condition is also given there).  Only under that condition it
writes, with approximation signs,

```text
delta_e phi ~= phi delta_e ln(phi),
delta_e exp(phi) ~= exp(phi) delta_e phi.
```

Accordingly, the familiar-looking replacement
`delta_e ln(V) ~= delta_e V / V` is an M7 approximation, not an exact
consequence of M2/M2a for a finite metron step.  M2/M2a exactly define a
backward finite difference and its telescoping sum; they do not turn that
difference into an ordinary logarithmic differential without M7's stated
small-variation regime.

## Direct connection to H004 II273--274

H004 II273/PDF279 first writes the H/G ratio variations using
`delta_e V/V` and then rewrites them as additive `delta ln` expressions.
It calls `delta_e` a metronic variation of the charge-field components and
says that X has very large metron indices at the boundary between zones 3
and 4.  This supports the discrete-index setting, but the checked H004 pages
do not separately demonstrate M7's quantitative condition
`0 < |delta_e| << 1` for every logged potential.  The logarithmic rewrite is
therefore source-supported as an invoked approximation/regime step, not as a
verified exact identity of the basic operator.

The following line is a clean direct use of the exact endpoint convention.
H004 integrates across the layer from `z` to `z+1` and prints

```text
S(z..z+1) delta ln X
  = ln X(z+1) - ln X(z-1)
  = ln[X(z+1)/X(z-1)] = ln Y.
```

Taking `Phi(n)=ln X(n)`, this has precisely the M2a shape with
`n1=z`, `n2=z+1`: the `z-1` term is the prescribed lower-end correction,
not an ordinary two-step integral rule.  The local M2a domain requires
`z >= 1`; H004 subsequently describes z in this transition as very large,
so that requirement is compatible with, but not independently numerically
proved by, the checked passage.  The last equality uses the usual algebra of
the logarithm after the discrete endpoint identity.

H004 II274/PDF280 separately says that, when carrying out its metronic
potential integrals, the metronic variation of the relevant potential is to
be added at the lower limit because it is compensated only in execution of
the integral.  That is qualitatively consistent with the M2a `n1-1`
endpoint.  It remains an H004 application prescription: this review does not
establish a one-to-one identification between every named potential limit and
an H003 metron-indexed primitive.

## Status and limits

* **Defined exactly within the source calculus:** M2's discrete backward
  difference and M2a's telescoping bounded sum, including the one-step lower
  endpoint shift, subject to their displayed index/primitive conditions.
* **Approximate/regime-dependent:** converting the finite variation ratios to
  logarithmic variations via M7; H003 marks it with `~=` and requires a small
  scaled variation.  H004's large-z statement is not by itself a derivation
  of that condition for all of H and G.
* **Asymptotic rather than an operator identity:** after defining the local
  ratio Y, H004 II275/PDF281 uses the recurrence and high-z transition to set
  `Y=xi^2`.  That is additional recurrence/limit reasoning, not a consequence
  of M2a alone.

No conclusion is drawn here about physical validity, missing rules elsewhere,
or a mass result.  The source chain does establish why H004 has the unusual
`z-1` lower endpoint; it does not license replacing its operators wholesale
by ordinary differential calculus.
