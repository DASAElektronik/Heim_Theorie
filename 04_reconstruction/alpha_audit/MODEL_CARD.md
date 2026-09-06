# Model Card: alpha_audit_igw_v1

Third-stage source update (2026-09-06): EDM2 printed266/267, (98), explicitly
defines the book eta(q,k) family and eta(q,0)=eta_q, eta(1,0)=eta. Thus the
book-only index gap described in the second-stage section below is now closed
by NORM-BOOK-ETA-001. IGW1982(V) and the stored diagnostic profiles remain
unchanged; locating a definition does not prove its physical derivation.

Separate third-stage tool: `audit_charge_averaging.py`, NORM-CHARGE-001,
reconstructs preliminary EDM1(29a) and an unfitted lambda interpolation.
No modern data or Y3 enters that tool. Ten additional tests bring the suite
to33; independent review accepted. `BOOK_ENERGY_ORDER_ISSUE.md` records a
separate source conflict, not a silent correction to v1.

Date: 2026-09-06.

## Scope

Implement only the scoped 1982/1989 ALPHA equations, paired roots, and
printed-number consistency checks. No particle masses are calculated.

## Source basis

| Formula | Source and location | Scope |
|---|---|---|
| HT-F-1982-ALPHA | IGW 1982 rendering, PDF pp. 3-4, V and alpha block | Existing source-checked formula and two explicit eta variants |
| HT-F-1982-AUX | Same PDF p. 5, IX | Indexed eta dependency only |
| HT-F-1989-ALPHA | IGW 1989 rendering, PDF p. 9 / printed p. 18, B58-B62 | Equation and printed pairs; source numbers stored independently |
| 1989 continuation | PDF p. 3 / printed p. 12, before B8 | Cross-reference to earlier eta/vartheta definitions |
| EDM2 book (105) | PDF folios 307-309 / printed pp.301-303 | Same left-hand equation and printed branch pair; Y3=1 specialization |

File hashes and public source URLs are in `inputs.json`. The IGW renderings
are from 2002/2003; labels 1982/1989 do not establish publication priority
of every printed number. The narrow book passage was subsequently checked
visually by the source agent and (pp.301-302) by the main agent.

Book equation (105) includes `1-A1*A2*Y3`. The prose explicitly takes `Y3=1`
for the following numerical example, after introducing Y3 as an uncertainty
factor. That specialization is compatible with the implemented 1982 right-hand
form; it is not evidence that the general book model has no adjustable Y3.
The book prints the same inconsistent reciprocal pair. Changing a common
right-hand factor cannot change the complementary-root identity.

## Constants and discrete choices

Sixth-stage addition (2026-09-06): `audit_wave_closure.py` introduces an
explicitly separate scalar periodic S1 problem, signed modes and a spatial
zero mode. Periodicity does not choose N=1, radius, dispersion or a beta
branch. Conditional K=N*zeta*f*s retains unproved geometry and energy.
The same-wave momentum substitution zeta=1/beta retains pc and changes the
equation to K=N*s; it is not a completed bound-state or dispersion solution.
Own effective rho*P_book*Y3 examples demonstrate product degeneracy, no fit.
Manuscript Ak and Y are not normalized onto the book. Independent review
found and confirmed fixes for two branch-boundary rounding defects;69 tests
pass,13 new. Old calculators/snapshots unchanged; no physics validation.

Fifth-stage addition (2026-09-06): `audit_lorentz_meaning.py` uses exact
Fraction arithmetic at preselected rational boosts, no experimental input.
The passive real-coordinate reference, static-circle geometry and literal
EDM1-p21 imaginary-time block are explicitly distinct. Rational-gamma
restriction is numerical scope, not a physical selection rule. The p21
orthogonality failure is conditional on ordinary complex trigonometry and
transpose. Later p56 is contextual evidence, not a source-authorized repair.
12 new tests and independent reviews passed;56 total. Physics and author
intent are not inferred from software-test success.

Fourth-stage addition (2026-09-06): `audit_energy_kinematics.py` is separate
from the historical profiles. It uses the now source-checked book eta(q,k)
chain, Y3=1 and mathematical pi for its illustrative small branch. Neither
measured alpha nor mass values are inputs. The two substitution profiles
are unfitted forward diagnostics, not physically consistent replacement
atom models or an uncertainty interval. The m=gamma*m0 bridge from EDM1 to
EDM2 is conditional; pc, T, h/(mc) and h/p are not silently equated.
All11 new tests and independent source/mathematics reviews passed;44 total.

All quantities are dimensionless. Mathematical pi is computed at the declared
Decimal precision. The separate 3.1415926535 profile tests the 1982 printed pi;
its use for 1989 is explicitly a sensitivity calculation. No mass, hbar, c,
Newtonian constant, or CODATA value is fed into either equation.

| Model | eta_12 helper arguments | Interpretation |
|---|---|---|
| 1982_source_literal | k=1, q=2 | Local (V) index reading |
| 1982_printed_alpha_fit_variant | k=2, q=1 | Existing target-motivated hypothesis, not a literal reading |
| 1989_source_cross_reference | k=2, q=1 | (q,k) via explicit source continuation and IX |
| 1989_kq_counterfactual | k=1, q=2 | Index sensitivity only, contrary to the adopted source chain |

1989 eta/vartheta inherit the earlier definitions. The reference to IX is
imprecise for vartheta, whose explicit expression is in V; this is documented
in `NORM-1989-ALPHA-ETA-CROSSREF`. No additional factor or correction is fitted.

## Validation targets and uncertainty

- Table reproduction: calculate and report residuals, including failed matches.
- Internal consistency: test complementary roots and displayed reciprocals.
- Modern comparison: use NIST CODATA 2022 only after evaluating formulas.
- Historical prediction: not established by this audit.

Printed last-place half-intervals assume rounding to nearest, include endpoints,
and are not statistical uncertainty. Endpoint propagation uses outward Decimal
rounding for inverse and squared-sum bounds. CODATA's standard uncertainty is
stored, but no theory significance or exclusion sigma is calculated: theory
uncertainty, correlations, and source variants are not a probability model.

## Excluded material and remaining work

No XLSM macros or C/Pascal programs are executed or used to choose expressions.
Full mass dependencies, B50, Gamma/Q_N, neutrino interpretation, historic
priority, and the reason for inconsistent IGW numbers remain outside this
model. Successful software tests do not validate Heim's physics.

## Separate book-structure diagnostics, 2026-09-06

`audit_alpha_book.py` is a separate ex-post model, not a change to v1.
It combines Eq. (105)'s Y3 structure with explicit IGW1982 eta profiles;
the two-index bridge has not been reconstructed from the book alone.
Source review located the all-Y_k=1 numerical policy at EDM2 printed p.1
and the unindexed eta/vartheta definitions in EDM1 printed pp.247-248.
Neither establishes a theoretical closure for Y3 or the index ambiguity.

The historical branch targets and CODATA are explicit inputs to this
inversion. Every inferred Y3 is calibrated; no fitted alpha may be called a
prediction. Input uncertainty ranges are not a theoretical error model.
R0 and A1*A2 interval coefficients are fixed high-precision approximations;
convergence is checked, not an exact transcendental interval proof.

Reviewed and tested (10 additional tests). Generic insufficient-precision
inputs are rejected. The binary64 cancellation conclusion excludes only
that arithmetic profile, not low-precision historical computation.
See `EXTENSION_CANDIDATES.md` and the two book review files.
