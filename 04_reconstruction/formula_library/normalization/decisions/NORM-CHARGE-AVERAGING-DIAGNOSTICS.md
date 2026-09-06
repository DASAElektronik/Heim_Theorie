# NORM-CHARGE-AVERAGING-DIAGNOSTICS

Decision ID: `NORM-CHARGE-001`. Date:2026-09-06.
Status: scoped diagnostic implementation; independent review pending.

## Inspected source and source boundary

EDM1 1998 third changed edition: PDF251/printed245 (27b), PDF253/printed247
(28)/(28a), PDF254/printed248 (29)/(29a). Source hash and edition qualifiers
are recorded in `03_notes/EDM1_ALPHA_DEPENDENCIES_2026-09-06.md`.

Use unsigned E0=abs(epsilon_pm)>0, E=abs(e_pm), t=sqrt(eta),
eta=pi/(pi^4+4)^(1/4). Book-defined component magnitudes:

```text
e_r/E0=t; e_d/E0=1-t; e_w/E0=(1+t)/2.
```

With common nonzero radial factor f(r), the source assumption
`2*V_ee=V_rr+V_ww` yields `E^2=(e_r^2+e_w^2)/2`.
The original signed charges belong to the same sign branch; E0 itself
denotes only their positive raw magnitude throughout this diagnostic.
This is not an addition of opposite charges. For the displayed product
V_xy=e_x*e_y*f(r) with Coulomb-type f, V_xy has energy units, not volts.

Source (27b) gives E0^2=9*hbar/(pi^4*R_vacuum). With the standard
dimensionless alpha relation E^2/(4*pi*epsilon0*hbar*c) and
R_vacuum*epsilon0*c=1, this gives alpha_prime=9*rho/(4*pi^5),
rho=E^2/E0^2. The book's equal mean has rho=vartheta/8 and hence (29a).
No independent proof of (27b), the physical mean, or the source spectrum
is claimed by this local substitution.

## Our diagnostic family, not a source formula

Replace only the second, potential/energy mean by

```text
rho(lambda)=lambda*eta+(1-lambda)*(1+sqrt(eta))^2/4
0<=lambda<=1; source specialization lambda=1/2
vartheta_diagnostic(lambda)=8*rho(lambda)
alpha_prime_diagnostic(lambda)=9*rho(lambda)/(4*pi^5)
```

This artificial interpolation holds the already assumed e_w mean fixed.
It neither derives a physical degree of freedom nor samples every possible
alternative. Predeclare grid 0,1/4,1/2,3/4,1; do not fit lambda to any value.
No CODATA, mass, or target alpha enters the numeric diagnostic. The printed
approximate inverse137.038 is stored separately as a reproduction check.
The model contains neither Y3 nor the later alpha*sqrt(1-alpha^2) correction.

For t in(0,1), d(rho)/d(lambda)=(3*t+1)*(t-1)/4<0.
Thus equal weighting is a substantive selection in this constructed family,
not a consequence of units alone. Positivity/units do not establish that any
member, including source lambda1/2, is physically correct.

## Numerical and review requirements

Default80 digits and120-digit convergence. Independently known rational case
t=1/2: e_r/E0=1/2, e_w/E0=3/4, equal-energy rho=13/32.
Do not replace the energy mean with an arithmetic charge mean: their squared
ratio difference is (e_r/E0-e_w/E0)^2/4.
Tests cover endpoints, domain, source specialization, monotonicity, scale
cancellation and this distinct-mean identity. Source values remain unchanged.
