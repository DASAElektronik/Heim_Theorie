# H003's scaled metronic step `delta_e = a delta` -- 2026-09-06

## Scope

This review asks only whether the `a` in H003 I109/PDF115's
`delta_e = a delta` is defined as a scalar operator scale or as an argument
shift/grid change.  H003 I printed pp.106--111 / PDF112--117 were visually
read in `tmp/pdfs/metronic_operator/edm1-112.png`--`edm1-117.png`, with M2/M2a
on I103--104 / PDF109--110 retained only as direct context.  Source SHA-256:
`49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`.

## Direct definitions and contrast

1. H003 I103/PDF109 (M2) defines the unscaled elementary operation by the
   actual backward argument step

   ```text
   delta phi = phi(n) - phi(n-1).
   ```

   I106/PDF112 again explains it as the change between two metronic values
   when the integer argument changes by one.

2. H003 I109/PDF115 (M7) first says that delta occurs with a **factor**
   small `a` in the form `a delta = delta_e`, with
   `0 < |delta_e| << 1`, so that small infinitesimal ratios can be
   approximated.  It gives the metron-scale expression for `a` in the
   p-dimensional case.  This is the printed scalar-factor introduction.

   On the same page, however, the explicitly approximate transcendental
   construction does more than write `a delta f`: for `f=exp(phi)` it prints

   ```text
   delta_e f = exp(phi) - exp(phi-delta_e phi).
   ```

   Thus M7 evaluates the exponential at an argument shifted by the *value*
   `delta_e phi`.  The source introduces this with conditional wording
   ("would", "under this prerequisite") and then obtains the logarithmic and
   exponential relations with `~=`.  The checked page does not derive this
   shifted-argument evaluation from M2 or prove it equals `a` times the basic
   finite difference `delta f`.  It is therefore an M7 approximation rule,
   not a demonstrated exact consequence of merely multiplying M2 by a.
   It still supplies neither `n -> n+a`, a new integer-index set, nor a
   coordinate/grid transformation.

3. The same source shows what an explicit argument-change construction looks
   like.  H003 I110/PDF116 (M8), only when `phi(n)` can be used as a new
   variable, defines a *different* labelled operation

   ```text
   delta_phi f = [f(phi)-f(phi-delta phi)] / delta phi,
   delta_phi f delta phi = f(phi)-f(phi-delta phi).
   ```

   Its argument shift is printed in the formula.  I110--111/PDF116--117 then
   develops a conditional chain-rule analogue (M9/M9a), and expressly warns
   that such a chain rule is only rarely usable because delta has no general
   infinitesimal-analysis analogue; it must generally be performed
   individually.  M8/M9 are consequently not a hidden definition of M7's
   `delta_e`.

## Consequence for the H004 logarithm step

Relative to the prior operator review, the source now positively distinguishes
two mechanisms:

| Source mechanism | What is printed | Status for `delta_e=a delta` |
| --- | --- | --- |
| M2 | backward unit index step `n -> n-1` | base operation |
| M7 | factor `a` multiplying delta, then `exp(phi-delta_e phi)` in its transcendental approximation | scalar-factor introduction plus an explicitly approximate shift of the inner function value phi |
| M8/M9 | an explicitly displayed shifted argument and conditional transformed operator | separate construction, not shown for M7 |

Thus H003 locally supports two distinct statements about H004's `delta_e`:
M7 begins with a scalar factor and, for its approximate transcendental rule,
uses a displayed shift of the inner value phi.  It does not, within the checked
definitions, support interpreting that as an independently defined fractional
index step, a different metronic grid, or an automatic potential-limit shift.
Nor is the equality of the shifted exponential expression with `a` times the
basic finite difference derived there.  Such stronger claims need an explicit
source map from the relevant potential/index to M8 or another definition.

## Open, deliberately limited points

* M7 calls `a` a factor and gives its p/tau scale expression, but the checked
  pages do not provide a derivation that identifies the subsequent
  `phi-delta_e phi` evaluation with `a delta f`, or a global typing declaration
  for `a` across all later applications.  This review therefore reports the
  local operator role, not a whole-work uniqueness claim.
* M7's `0 < |delta_e| << 1` is an asserted condition for its approximations;
  no numerical verification for H004's individual charge-field potentials is
  made here.
* The source's exact finite-sum endpoint convention remains M2a's indexed
  rule.  Scaling delta in M7 does not itself supply an index-free rule for a
  lower-potential correction.
