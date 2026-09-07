# EDM1 charge averaging: independent mathematics review

Date: 2026-09-06. Scope: the supplied EDM1 (27b)-(29a) source structure,
`scripts/audit_charge_averaging.py`, `tests/test_charge_averaging.py`,
`05_analysis/charge_averaging_diagnostics.json`, and
`NORM-CHARGE-AVERAGING-DIAGNOSTICS.md`. The imported standard-library helpers
in `scripts/audit_alpha.py` were inspected before execution.

This is a conditional algebra/code review. It does not independently inspect
the book page images, establish a physical averaging law, compare modern
measurements, or reconstruct a mass model. No source program or macro was
executed. Only this review file was written.

## Finding

The implemented diagnostic is mathematically correct within its declared
domain. The stored JSON reproduces the calculation, and all eight dedicated
tests pass. No numerical or algebraic defect was found. One minor sign-notation
inconsistency in the normalization text and two small test-coverage gaps are
recorded below; neither changes the checked results.

## Independent algebra

Let `t=sqrt(eta)`, `a=e_r/E0=t`, and `b=e_w/E0=(1+t)/2`, with positive
`E0` and `0<t<=1`. Cancellation of the common nonzero factor in
`2 V_ee=V_rr+V_ww` gives the squared charge ratio

```text
rho(1/2) = (a^2+b^2)/2
         = (5 t^2+2 t+1)/8 = vartheta/8.
```

This matches `component_ratios`, `energy_mean_ratio`, and the report identity
in `scripts/audit_charge_averaging.py:26`, `:33`, and `:81`.

Keeping `b` fixed while changing only the energy weight gives

```text
rho(lambda) = lambda t^2+(1-lambda)(1+t)^2/4
8 rho(lambda) = (2+6 lambda)t^2+4(1-lambda)t+2(1-lambda)
d rho/d lambda = t^2-(1+t)^2/4 = (3t+1)(t-1)/4.
```

For `0<t<1`, the derivative is negative. The positive convex-combination
bounds are `t^2<=rho<=(1+t)^2/4`. At `t=1`, both components coincide, all
weights give `rho=1`, and the derivative vanishes. The implementation and
its monotonicity/endpoint tests agree with these facts.

For equal weighting, the square of the arithmetic charge mean is a different
quantity:

```text
(a^2+b^2)/2 - ((a+b)/2)^2 = (a-b)^2/4 = (1-t)^2/16.
```

The report therefore correctly distinguishes the mean of squared charges
from the squared mean charge (`scripts/audit_charge_averaging.py:69`). At the
independent rational case `t=1/2`, these are `13/32` and `25/64`, with gap
`1/64`. The stored source-case gap is approximately `1.57362510214318e-6`.
The nonzero gap is a mathematical distinction, not a physical uncertainty.

## Alpha substitution, units, and signs

The supplied equation `E0^2=9 hbar/(pi^4 R)` and the stated definition of
dimensionless alpha imply

```text
alpha_prime = rho E0^2/(4 pi epsilon0 hbar c)
            = 9 rho/(4 pi^5 R epsilon0 c)
            = 9 rho/(4 pi^5), assuming R epsilon0 c=1.
```

Consequently `inverse_alpha_prime=4 pi^5/(9 rho)` in
`scripts/audit_charge_averaging.py:41` is correct. Since `rho` decreases with
lambda, the reciprocal increases for `0<t<1`.

In SI dimensions, `hbar/R` has units `C^2`, so `E0` has charge units. All
implemented component ratios, `eta`, `rho`, lambda, vartheta, and alpha are
dimensionless. For the specified product `V_xy=e_x e_y f(r)` with a
Coulomb energy factor, `V_xy` has energy units. The cancellation requires
the same nonzero factor; it does not use an equality of electric potentials
in volts.

The arithmetic uses nonnegative component magnitudes of one charge branch.
It neither mixes opposite charge branches nor derives a signed charge from
the positive square root. The normalization correctly limits the scope,
but its sign wording should be clarified: line 12 defines `E0=abs(epsilon_pm)`
as unsigned, while line 21 says that signs are carried by `E0`. Those cannot
both be literal definitions. The signed source charge is `epsilon_pm`, or
equivalently `s E0` for `s=+/-1`; `E0` itself remains positive. This is a
documentation defect only, with no effect on the unsigned calculation.

## Parameter and domain boundaries

Lambda is explicitly our predeclared interpolation, not a Heim parameter,
an inferred physical freedom, a fitted value, or an error bar. The grid is
fixed to `0,1/4,1/2,3/4,1`. Only its midpoint is labeled as the source mean.
The existing definition of `e_w` stays fixed throughout. No empirical input,
Y3, or later complementary-branch correction enters this script. Although
the shared `audit_alpha` module also contains other audit functions, its
import does not execute those functions or load their reference inputs.

The component domain `0<eta<=1` is consistent with the positive ratios; the
actual pi-derived eta is strictly below one. Excluding eta zero also avoids
the singular inverse at the endpoint `lambda=1`. Finite weights in `[0,1]`
and positive finite `pi,rho` are validated before evaluation. The inverse
helper accepts positive rho beyond the diagnostic convex-combination range;
that is a broader algebraic helper domain, not an assertion that such rho
belongs to the constructed family.

The printed `137,038` is used only after calculation, as a conditional
rounding check. At the source mean the reciprocal is
`137.0380300128048132955...`, strictly inside the stored interval
`[137.0375,137.0385]`. Thus endpoint tie conventions do not affect this
particular reproduction. This check does not establish physical validity.

## Execution and coverage

Run from the repository root:

```text
python -B scripts/audit_charge_averaging.py --check --verify-sources
# EDM1 source hash verified.
# Charge diagnostic snapshot matches fresh calculation.

python -B -m unittest discover -s tests -p test_charge_averaging.py -v
# Ran 8 tests; OK.
```

The tests include exact rational component/mean cases, independent
polynomial coefficients, an exact rational scale cancellation, boundary
weights, eta one, invalid eta/weight cases, source specialization,
monotonicity, and 80/120-digit convergence. The JSON identity residual
`-2e-79` is compatible with the 80-digit arithmetic; it is not a source
discrepancy.

Additional read-only probes compared 20 combinations of
`t=1/8,1/2,7/8,1` and all five weights against independently evaluated exact
Fractions. Every value matched. Twelve inverse-helper domain probes
(`0,-1,NaN,sNaN,+Infinity,-Infinity` separately for pi and rho) and precision
39/201 were all rejected with `ValueError` as expected.

These supplementary checks expose two coverage gaps rather than defects:
the committed test suite does not yet exercise the inverse-helper invalid
domains or the report precision bounds. The rational polynomial test also
checks algebra independently of the implementation; the additional 20-case
probe supplies that direct implementation connection. No canonical script,
test, normalization decision, snapshot, or Git state was changed by this
review.

## Follow-up verification - 2026-09-06

The minor sign-notation defect is resolved. The normalization now assigns
the common branch sign to the original signed charges and consistently
defines `E0` as their positive raw magnitude. Its lines 12 and 21-22 are
therefore compatible.

The two new tests address the reported coverage gaps:
`test_inverse_helper_invalid_domain` rejects zero, negative, NaN, and
infinite pi/rho inputs; `test_precision_limits` rejects 39/201 digits and
successfully evaluates the supported endpoints 40/200 digits. Both passed.

Independent follow-up execution:

```text
python -B scripts/audit_charge_averaging.py --check --verify-sources
# EDM1 source hash verified; diagnostic snapshot matches.

python -B -m unittest discover -s tests -v
# Ran 33 tests, including 10 charge-averaging tests; OK.
```

No unresolved defect remains from this review. The accepted result is still
the declared conditional arithmetic diagnostic, with the physical and
source-validation boundaries stated above. This follow-up changed only
this review file.
