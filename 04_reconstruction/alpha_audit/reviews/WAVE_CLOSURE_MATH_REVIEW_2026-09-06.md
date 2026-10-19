# Ring-wave closure: independent conditional mathematics review

Date: 2026-09-06. This review checks an explicitly introduced scalar
periodic ring problem and conditional energy/wavelength substitutions.
It does not inspect new source pages, identify an author's intended wave,
select a physical atomic state, fit a parameter, or validate a theory.

The existing `scripts/audit_energy_kinematics.py` and
`NORM-ENERGY-KINEMATICS-DIAGNOSTICS.md` were read to preserve the established
charge-energy normalization. No new wave implementation was supplied at
this stage; any later code review must be recorded separately.

## Periodic scalar ring problem

Take a prescribed R>0, angle `0<=phi<=2 pi`, a twice differentiable scalar
field, and periodic boundary conditions on both the field and its angular
derivative. For a nontrivial solution of

```text
d^2 psi/dphi^2 + kappa^2 psi = 0,
psi(2 pi)=psi(0),
psi'(2 pi)=psi'(0),
```

the allowed nonzero real spectral values are integer kappa. Equivalently
one may label the complex modes by signed integers n:

```text
psi_n(phi) = A exp(i n phi),  n in Z.
```

The nontrivial-field qualification matters: the identically zero solution
satisfies the equation and boundary conditions at every spectral value
and establishes no mode quantization. For nonzero kappa, the periodic
monodromy has a fixed vector only when `cos(2 pi kappa)=1`, giving the
integer condition. Equivalently `exp(2 pi i n)=1` is the periodicity of
each nonzero travelling spatial eigenfunction.

For n=0, the differential equation instead gives `psi=A+B phi`.
Periodicity forces B=0, leaving a valid constant mode. It has no finite
spatial wavelength on the ring. For `N=abs(n)>=1`, the spatial wavelength
and circumference are related by

```text
lambda = 2 pi R/N,
2 pi R = N lambda.
```

Periodicity permits every integer n, including zero. It does not select
`N=1`; that requires an additional nonzero-mode and lowest-mode selection.
It also does not determine R, a temporal frequency, a dispersion relation,
or a particle interpretation.

This prescribed S1 scalar problem is not a spherical hydrogen bound-state
problem. Excluding n zero from a later finite-wavelength diagnostic cannot
be reported as excluding a hydrogen s state or its physical ground state.

## Travelling and standing modes

Temporal behaviour is an extra assumption beyond the spatial equation.
For example, a component `exp(i(n phi-omega t))` with positive omega
travels with a signed angular phase direction fixed by n. The opposite
mode has label -n. Their equal-amplitude combinations can form standing
patterns, such as `cos(N phi) cos(omega t)` in a real-field convention.

A standing combination is not one travelling phase front. Any phase
speed/wavelength relation subsequently applied to it must refer to its
travelling constituents or be independently defined. The spatial boundary
condition alone does not choose standing versus travelling behaviour.

With the additionally introduced quantum phase-generator convention,
`-i hbar d/dphi` has eigenvalues `hbar n`. Dividing by the prescribed R
gives signed tangential mode momentum `p_wave=hbar n/R`; its magnitude is
`hbar N/R`. This is not automatically a global Cartesian momentum
eigenvalue, because the ring tangent changes direction around the circle.

A standing superposition of both signs has no single signed eigenvalue
of that generator. A balanced pair has zero mean generator under the
usual normalized periodic inner product, while its squared-generator
eigenvalue remains `hbar^2 N^2`. Zero signed mean must not be substituted
for its nonzero component wavenumber or momentum magnitude.

## Conditional energy and wavelength identification

Now explicitly assume the same frame and the identities

```text
E_tot = mc^2 = h nu = hbar omega > 0,
nu = v_phase/lambda,
zeta = v_phase/c > 0,
E_kin = g(beta) mc^2,
s = sqrt(1-beta^2),  0<beta<1.
```

Here zeta is a positive phase-speed magnitude, not a particle-speed
parameter or a group speed. These assumptions alone do not impose
`zeta<=1`. The label E_kin denotes the energy inserted in the diagnostic
balance; it is not a blanket identification with the comparator T. The
symbol g denotes the energy factor in this review; in the
earlier energy audit that energy factor was named f, while g there named
a wavelength factor. Those two naming conventions must not be silently
mixed in an implementation.

The assumed frequency identification gives

```text
lambda = zeta h/(mc).
```

Combining it with the nonzero ring mode gives

```text
R = N lambda/(2 pi) = N zeta hbar/(mc).
```

Thus `lambda=2 pi R` is recovered only for `N=1`. For higher modes,
inserting the source's one-wavelength circumference as though it held
unchanged would lose a factor N. This is an explicitly generalized ring
diagnostic, not a newly identified source formula.

At n zero, this finite-wavelength chain is unavailable. In particular,
positive `mc^2` cannot follow from a zero spatial wavenumber and a finite
linear phase-speed relation. That is a limitation of these extra
assumptions, not a claim that every spatially constant field has zero
energy or that zero modes are generally forbidden.

## Preserve the existing K normalization

The existing audit defines

```text
e^2(1-C) = 4 pi epsilon0 y E_kin,
alpha_prime = e^2/(4 pi epsilon0 hbar c),
K = alpha_prime(1-C)
  = e^2(1-C)/(4 pi epsilon0 hbar c)
  = e^2(1-C)/(2 epsilon0 h c).
```

C is the existing dimensionless correction; it is not an electric charge
or a newly defined dimensional constant. An initially transmitted
`K=2 pi epsilon0 C/h` was flagged as incompatible and dimensionally wrong
under this definition. The principal reviewer confirmed it was a typing
error; it must not enter the implementation or replace the existing K.

Retain the additional geometric assumption `y=R s`. Then

```text
y E_kin = N zeta hbar/(mc) * s * g mc^2
        = N zeta g hbar c s,
K = N zeta g(beta) s.
```

This is the requested closure, with no missing factor of 2 pi. All
quantities on its right are dimensionless. Before cancellation, both
`y E_kin` and `hbar c` have units `J m`; multiplying by epsilon0 gives
charge-squared units, matching the charge equation.

For N one, the previous three diagnostics are recovered by the distinct
choices `(g,zeta)=(beta,1)`, `(1-s,1)`, and `(1-s,1/beta)`. At beta 3/5,
these yield `12/25`, `4/25`, and `4/15`; any nonzero mode N multiplies
those values by N at the same beta. Mode sign changes propagation
direction, not this magnitude-based positive-energy closure.

## Same-wave momentum identification is an additional constraint

For the same travelling component with `omega=v_phase abs(k)` and
`abs(k)=N/R`, the above total-energy identification implies

```text
abs(p_wave) = hbar abs(k) = mc/zeta.
```

Identifying that quantity with `abs(p)=beta mc` at the same frame, mass,
and momentum convention therefore requires

```text
zeta = 1/beta.
```

For `0<beta<1`, zeta one fails that extra same-wave identification. The
mode integer cancels from this condition; selecting a different N cannot
fix the mismatch. No contradiction follows if the two quantities refer
to different waves, different energy assignments, or different momentum
observables. A standing superposition likewise cannot silently be given
one of its components' signed momenta as its total signed momentum.

The cases must stay separate: source-like `(g,zeta)=(beta,1)` gives
`K=N beta s`. Imposing the extra same-wave momentum condition while
retaining g beta instead gives `K=N s`. Changing both the energy factor
to `1-s` and zeta to `1/beta` gives `K=N s(1-s)/beta`. These are different
declared diagnostics; none is an automatic source repair.

## Conditional beta branches and underdetermination

For a specified positive K, specified N>=1, zeta one, and g beta, set

```text
kappa_closure = K/N,
beta sqrt(1-beta^2) = kappa_closure.
```

Positive solutions in `0<beta<1` require `0<kappa_closure<=1/2`.
There are two positive branches below the maximum and one coincident
branch at the maximum:

```text
beta_small^2 = (1-sqrt(1-4 kappa_closure^2))/2
beta_large^2 = (1+sqrt(1-4 kappa_closure^2))/2.
```

Numerically, computing the large root first and then
`beta_small=kappa_closure/beta_large` avoids small-root cancellation.
Zero or negative kappa_closure does not supply a positive interior root;
squaring must not introduce one. At `K=12/25,N=1`, the two exact beta
branches are `3/5` and `4/5`. Periodicity neither chooses between them
nor identifies beta with a physical coupling alpha.

The current source correction has the form `C=A1 A2 Y3`, hence

```text
K(Y3) = alpha_prime(1-A1 A2 Y3).
```

Its dependence on Y3 is affine, not simply multiplication by Y3. If a
further unspecified geometric factor chi were introduced through
`y=chi R s`, the conditional equation would instead be

```text
alpha_prime(1-A1 A2 Y3) = chi zeta N g(beta) s.
```

This last formula is an explanation of underdetermination, not a newly
authorized fitting family. Unspecified geometry, dispersion, mode
selection, Y3, and branch choice leave effective combinations undetermined.
One cannot claim a unique beta or alpha from periodicity alone, or treat
adjusting those quantities to a target as a prediction. Conversely, when
every such input and selection is fixed, the remaining algebraic branches
can be evaluated reproducibly at that explicitly conditional scope.

Only this review file was created. No source, canonical normalization,
script, data snapshot, other review, or Git state was changed.

## Independent implementation review - 2026-09-06

Reviewed `scripts/audit_wave_closure.py`, `tests/test_wave_closure.py`, and
`05_analysis/wave_closure_diagnostics.json`. This subsection supersedes
the earlier statement that no implementation had yet been supplied.
The review found two related numeric boundary defects in the initial
implementation. Both were reported to the principal reviewer, locally
fixed in the new script, and independently rechecked as described below.
The accepted snapshot examples were not affected by those defects.

### Implemented quantities and interpretation

`scalar_mode` retains the spatially valid zero mode, reporting no finite
wavelength for it. It rejects noninteger and boolean mode labels. Its
n-squared field now explicitly names the positive operator
`-d^2/dphi^2`; the unnegated second derivative would have eigenvalue
minus n squared. Travelling-generator signs and balanced-standing first
and second moments are stored separately. These are consequences of the
assumed scalar periodic problem, not a computational proof of that
problem or a model of a spherical hydrogen state.

`wave_ratios` correctly uses N=abs(n), a positive phase-speed magnitude,
the retained y=R s geometry, and separately named energy factors. It
implements

```text
lambda/(h/mc) = zeta
R/(hbar/mc) = N zeta
abs(p_wave)/(mc) = 1/zeta
abs(p_wave)/abs(p) = 1/(zeta beta)
K_pc = N zeta beta s
K_T_comparator = N zeta (1-s) s.
```

The momentum outputs are positive travelling tangential-component
magnitudes. They do not silently become the total signed momentum of a
standing superposition or a Cartesian momentum eigenvalue. The explicit
same-wave comparison still requires the common frame, energy, and
momentum conventions discussed above. The implemented energy-factor
metadata uses f, agreeing with the earlier energy audit; it does not
reuse the conflicting older wavelength-factor name.

An independent 100-digit check compared eight derived fields against
exact rational references for 24 combinations: beta/s pairs
`(3/5,4/5)` and `(7/25,24/25)`, modes `-3,-1,1,2`, and phase factors
`1,2,1/beta`. All 192 comparisons agreed within `1e-95`.

### Distinct branch constructions

`constant_phase_branches` solves the unsquared positive equation
`K=N zeta beta sqrt(1-beta^2)` for specified K, N, and constant zeta.
Its N=1, zeta=1 profile exactly reproduces the previously checked book
branch. At the fixed source K, the reported inverse small roots are
approximately `137.0359609952`, `274.0773953159`, and `411.1176132522`
for N=1,2,3. These are conditional roots of different prescribed ring
closures, not new measured-alpha predictions or a proof that one mode
is physically selected.

`same_wave_pc_branch` instead substitutes zeta=1/beta while retaining
the source-like pc energy, giving `K=N s`. It correctly requires
`0<K/N<1` and returns the sole positive interior root
`beta=sqrt(1-(K/N)^2)`. For N=1 and the source K, beta is approximately
`0.9999733753713582`. This is a different equation from the constant-c
phase case; it must not be presented as merely choosing the latter
equation's large branch or as a completed dispersion/bound-state model.

### Own proportionality diagnostic

The implemented `correction_family` is explicitly a further, separately
introduced construction:

```text
P = book A1 A2
C = rho P Y3
K = alpha_prime(1-rho P Y3).
```

Here rho is a new diagnostic multiplier in C. It is not the source
manuscript's differently defined Ak, the earlier charge-averaging rho,
or the optional geometric chi multiplying y in the preceding algebra.
Those distinct constructions are not silently equated by the code.

For fixed P and alpha_prime, only the product rho Y3 is identifiable
through C. Thus `(rho,Y3)=(1,1),(2,1/2),(1/2,2)` give the same C and K.
The implementation correctly preserves the affine dependence of K on
that product; it does not multiply all of K by Y3. Its use of the book
profile's C as P is valid here because that profile is expressly fixed
to Y3=1 and defines C=A1 A2.

The correction helper is algebraic and may return a nonpositive K for
other supplied coefficients. Such a result is not automatically an
admissible positive-energy branch; the separate branch solvers validate
their own K domains. No arbitrary parameter choices are used to fit a
target or relabel manuscript quantities as normalized book inputs.

### Initial boundary defects and confirmed fixes

The initial constant-phase helper had two real robustness defects:

1. At exactly `K/(N zeta)=1/2`, its two separate evaluations
   `sqrt(1/2)` and `(1/2)/sqrt(1/2)` could reverse their rounded ordering.
   For K=0.5, N=zeta=1, the helper wrongly raised ArithmeticError at
   40, 50, and 120 digits; at 200 digits it returned slightly different
   roots for the mathematically coincident branch.
2. It divided before checking the exact domain. With a 28-digit context,
   K specified as `0.5` followed by sixty zeros and a final one rounded
   to 0.5 and incorrectly returned a root, despite exact K>1/2. An input
   just below the maximum could likewise be silently changed into the
   coincident branch.

The final implementation compares exact `Fraction(Decimal)` values of
`K/(N zeta)` before any rounded-domain decision. Exact values above the
maximum raise ValueError. The exact maximum uses one square-root result
for both roots. If a valid submaximum value rounds onto the maximum, the
helper raises ArithmeticError to indicate insufficient precision rather
than inventing a coincident root. It also retains the checks that reject
rounded endpoint beta values.

The same-wave helper now distinguishes exact `K/N` domain violations
from a valid value rounded onto an endpoint. The new regressions include
inputs with eighty extra decimal digits on both sides of the relevant
boundaries, and coincident-root cases at 40,50,80,120,200 digits. They
passed independently. The corrections are local to the new script;
the shared earlier branch solver and its existing snapshots were not
changed as part of these fixes.

These guards establish the declared input-domain and unresolved-endpoint
behaviour; the Decimal results remain rounded numerical values rather
than certified interval enclosures for arbitrary caller contexts.

### Final execution and conclusion

Executed after the fixes:

```text
python -B scripts/audit_wave_closure.py --check --verify-sources
# Books, manuscript and historical phase-reference hashes verified.
# Wave closure snapshot matches fresh calculation.

python -B -m unittest discover -s tests -v
# Ran 69 tests, including 13 wave-closure tests; OK.
```

The snapshot now includes the explicit positive-Laplacian convention.
The source-profile and forward-example numerical values remain the
same reviewed values; all four source hashes match. Hash verification
does not itself verify a source interpretation, which remains a
separate review task.

No unresolved defect remains from this bounded code/snapshot review.
The tests appropriately check algebra, rational examples, branch
domains, convergence, normalization reduction, and metadata separation;
they do not purport to prove the spatial eigenproblem or physical
validity. Only the present review file was edited by this reviewer.
