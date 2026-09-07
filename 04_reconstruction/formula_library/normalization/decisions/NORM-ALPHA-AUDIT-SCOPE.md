# NORM-ALPHA-AUDIT-SCOPE

Date: 2026-09-06. Decision ID: `NORM-ALPHA-AUDIT-001`.

Status: resolved for the isolated audit; independent mathematical review accepted.

## Scope

Authorize an isolated, versioned numerical audit of the existing 1982 ALPHA
normalizations and 1989 B58-B61 scope. This does not authorize a complete mass
implementation or resolve B50/Gamma dependencies. Source transcriptions remain
unchanged. Code: `scripts/audit_alpha.py`; inputs: `alpha_audit/inputs.json`.

## Mathematical normalization

For `a*sqrt(1-a^2)=R` with `0<R<=1/2`, put `t=a^2`. Then
`t^2-t+R^2=0`, so the two real positive branches obey
`a_small^2+a_large^2=1` and `a_small*a_large=R`.

Compute `t_large=(1+sqrt(1-4R^2))/2`, `a_large=sqrt(t_large)`,
`a_small=R/a_large`. This avoids subtraction cancellation in the small root.
The source's alpha_(+) is the small alpha (large inverse); alpha_(-) is the
large alpha. In B60 the signs apply to the inverse squares. At R=1/2 the
branches coincide. Other R values are outside this solver's declared domain.

## Variants and constants

- 1982 `source_literal`: eta_12=eta_k_q(k=1,q=2).
- 1982 existing `printed_alpha_fit_variant`: eta_12=eta_k_q(k=2,q=1).
  It is an already documented target-motivated interpretation; do not select
  it as a default because it is numerically closer to the printed value.
- 1989: B59 uses the full `K_alpha=1-C_prime` expression. The source reference
  chain in `NORM-1989-ALPHA-ETA-CROSSREF` supports `(q,k)` and hence
  `eta_12=eta_k_q(k=2,q=1)`. The `(k,q)` interpretation is retained only as
  a counterfactual sensitivity case. Eta and vartheta are inherited through
  the IGW text's stated continuation; this is not a new physical derivation.
- Compute mathematical pi using Gauss-Legendre at declared Decimal precision.
- Separately evaluate printed pi=3.1415926535 (1982 PDF page 4). Its use in
  1989 is a sensitivity experiment only. Other physical constants are absent
  from this limited alpha block. All quantities are dimensionless.

## Printed values and rounding

Preserve the original decimal strings, including commas and trailing zeros.
For a token with d decimal places, a hypothetical rounding-to-nearest envelope
is value +/- 0.5*10^(-d). Propagate positive endpoint intervals through inverse
and square operations. Use closed endpoints conservatively; this grants both
ties and therefore cannot create a false incompatibility at a rounding tie.

These are conditional printing envelopes, not statistical uncertainties.
No Gaussian sigma or theory-exclusion claim follows from them. A disjoint
interval proves incompatibility even if every printed value was independently
rounded to its last shown place. It does not locate the historical cause.

The pair and reciprocal checks do not depend on eta, pi, or experimental data.
The modern CODATA reference is consumed only after equation evaluation.

## Numerical safeguards and status

Use standard-library Decimal, default 80 significant digits, and a separate
120-digit convergence check. More arithmetic digits do not imply more physical
accuracy. Tests use independent root pairs and bounds, not agreement with
inconsistent printed targets. Source hashes must be checkable independently.

An implemented audit is not an implemented full theory. Catalogue ALPHA rows
may become `audit_implemented` after independent review; all other statuses
remain scoped to their existing work.
