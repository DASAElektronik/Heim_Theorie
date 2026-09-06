# Model Card: alpha_audit_igw_v1

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

File hashes and public source URLs are in `inputs.json`. The IGW renderings
are from 2002/2003; labels 1982/1989 do not establish publication priority
of every printed number. Book OCR is only a future research lead.

## Constants and discrete choices

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
