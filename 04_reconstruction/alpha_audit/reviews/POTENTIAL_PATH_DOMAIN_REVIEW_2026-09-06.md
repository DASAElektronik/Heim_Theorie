# H004 (98): potential components, q/k domain, and variation path -- 2026-09-06

## Scope

This compact source review reads H004 II printed pp.263--269 / PDF269--275,
with pp.266--269 / PDF272--275 providing the direct (98) chain.  All seven
pages were visually inspected in
`tmp/pdfs/configuration_selection/edm2-269.png`--`edm2-275.png`.
H004 SHA-256 is
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
The question is one of source-domain and dependency statements only; no
continuous path, fit, or physics conclusion is supplied here.

## What (98) actually defines

H004 II266/PDF272 introduces the internal factor by

```text
eta_qk * [pi^4 + q^4(4+k)]^(1/4) = pi.                 (98 precursor)
```

It says `eta_0k=1`; `k=0` in `eta_q0` is **only formal**, indicating that
the resulting `eta_q` belongs solely to the external R3 action region.  The
text contrasts this with `k>0`, which determines the configurative-metric
internal structuring.  II267/PDF273 collects the same relation in (98), after
the listed internal charge-field components:

```text
e_rho    = epsilon_± sqrt(eta_qk)
2 e_omega= epsilon_± [1 + sqrt(eta_qk)]
e_delta  = epsilon_± [1 - sqrt(eta_qk)]
e_C      = epsilon_± sqrt(v_qk/8)
v_qk     = 5 eta_qk + 2 sqrt(eta_qk) + 1.
```

The source uses `q>0` earlier in the construction and states on II268/PDF274
that only for `q>=1` can k appear in `eta_qk` under (98).  Here “external”
and “internal” refer to the R3 volume of the structure, not to a new
continuous coordinate.

## What follows if named quantities are held fixed

Let `s=sqrt(eta_qk)`.  This is an **algebraic inference**, not a sentence
from H004: with epsilon_± fixed, the four displayed component magnitudes are
functions of s alone (and `sqrt(v_qk/8)` is a function of s because
`v_qk=5s^2+2s+1`).  H004 II267/PDF273 gives for arbitrary static field
components x,y at a distance r from the metric simplex centre

```text
4 pi epsilon_0 V_xy = e_x e_y f(r).
```

For the four pairs used in the H/G construction --
`V_omega-epsilon`, `V_rho-rho`, `V_omega-omega`, and `V_delta-delta` --
this inference is direct: if r and epsilon_± are fixed, each is algebraically
a function of s (times fixed common factors).  This is the appropriate narrow
answer for those H/G potentials; `x,y` in the general law remain generic
component labels.

Separately, in its V1/V2/Q1/Q2 ratio construction, II268/PDF274
defines/chooses reference potentials including

```text
V_RR ~ q^2 e_R^2(q=1) f(r),
V_ee ~ q^2 epsilon_±^2 f(r),
```

and constructs ratios V1, V2 and Q1, Q2.  Here external reference `V_ee` is
not the internal (98) component potential `V_rho-rho`.  It explicitly says
that `f q^2`
and a proportionality factor cancel **in these ratios**.  These are external
reference quantities in the separate ratio argument, not an additional
q-dependence asserted for the four H/G pairs above.  Conversely, their
cancellation cannot by itself define a variation path for those pairs.

## q, k, and the variation question

* **k:** H004 calls k>0 the configuration number/internal metric
  structuring, and II263--264/PDF269--270 describes it as time-constant
  (`k=const(R6)`) for the discussed configuration.  The later comparison of
  V(k=1) and V(k=2) is a comparison of labelled cases, not a source-defined
  differential in k.
* **q:** The checked text uses q as a positive/natural charge/configuration
  label in eta_qk and as an argument of E(N,q), E_k(N,q,k); II268 explicitly
  uses q>=1.  It changes between described configurations and reference cases
  (for example q=1), but no checked line defines q as the running parameter
  of a metronic variation, or authorizes a variation path q -> q+dq.
* **delta_e:** The direct later continuation II273/PDF279 says it concerns
  metronic variations of the internal charge-field components (98), while it
  treats the R3 distance boundary as constant.  That describes what varies;
  it does not identify q as a dummy variable or provide a q-indexed path.
  Holding k,r,epsilon fixed therefore does not by itself make “q varies along
  delta_e” a source statement.

The explicitly defined geometric dummy/argument in the potential law is r,
the arbitrary distance from the metric centre; x and y are the generic static
field-component labels.  The symbols q and k have the substantive roles above,
not the role of an explicitly defined integration/variation dummy parameter.

## Boundary at (98a)

II269/PDF275 obtains its q/k selection discussion only after an explicitly
“spekulativ” identification of F1,2 with V1,2 and G1,2 with Q1,2.  The page
then states numerical q cases and conditionally presents (98a),
`k_max=2, q_max=3`.  This is not a rule permitting q to flow during the
preceding potential variation; it is a conditional selection statement about
allowed labelled cases.

## Result

The source supports s-only reduction for the four H/G potential pairs
`V_omega-epsilon`, `V_rho-rho`, `V_omega-omega`, and `V_delta-delta`, with
fixed epsilon_± and fixed r.  The separate V1/V2/Q1/Q2 reference-potential
argument has its own displayed q^2 factors and ratio cancellations; it does
not enlarge or invalidate that narrow H/G statement.  Nor does the examined
text define q as the variation parameter.  Any continuous or discrete q-path
must be separately specified rather than inferred from delta_e.
