# NORM-BOOK-ALPHA-Y3-DIAGNOSTICS

Date: 2026-09-06. Decision ID: `NORM-BOOK-ALPHA-001`.
Status: diagnostic implementation scope; independent review pending.

## Source and purpose

EDM2 book scan, printed pp.301-302 / PDF folios 307-308, equation (105):
`alpha*sqrt(1-alpha^2)=R0*(1-A1*A2*Y3)`, with
`R0=9*vartheta/(2*pi)^5`. The displayed example sets Y3=1. No general
first-principles determination of Y3 is inferred from that example.

This decision permits a separate diagnosis of what a target value would
require, and an examination of finite-precision cancellation. Target-derived
Y3 values are ex-post calibrations, never source inputs or predictions.
The existing alpha audit and its original source strings remain intact.

## Inversion

For a target inverse d=1/alpha, d>=1,

```text
R_required(d) = sqrt(d^2-1)/d^2
Y3_required(d) = (1-R_required(d)/R0)/(A1*A2)
```

For each fixed pi/index profile, compare the Y3 intervals implied by the
printed small- and large-branch inverses. Disjoint intervals cannot be repaired
by a common Y3. This is the same obstruction already established by the
complementary-root identity; it is not an additional independent experiment.

R_required increases on [1,sqrt(2)] and decreases on [sqrt(2),infinity).
The interval maximum is 1/2 if the d interval contains sqrt(2); otherwise
endpoint extrema suffice. Source tokens supply conditional half-last-place
printing intervals. CODATA's separate +/-standard-uncertainty input range is
reported descriptively and is not a theory uncertainty or probabilistic Y3 fit.

All source endpoints have few enough digits for their squares to be exact
at the minimum 50-digit diagnostic precision. Square-root/division and Y3
interval endpoints are rounded outwards with fixed computed R0 and A1*A2.
80/120-digit convergence checks control the numerical coefficient approximation.

## Arithmetic diagnosis

The book's inverse-square solution with B=1/(2R^2) gives the large-alpha
inverse as `sqrt(B*(1-sqrt(1-2/B)))`. Compare that cancellation-prone expression
to the stable complementary-root solver, in IEEE binary64 and declared
Decimal precisions 8,10,12,16,24. All profiles are reported; none is selected
because it happens to resemble a printed number. These simulations do not
establish how historical computations were performed.

## Model-development boundary

A corrected evaluation of the unchanged equation is an arithmetic correction.
Choosing Y3 from measured alpha adds a fitted degree of freedom. Neither is
by itself an improved physical theory. Future variants require a stated
reason and tests on information not used to select their parameters.
