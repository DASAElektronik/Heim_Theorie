# Energy and wavelength kinematics: conditional mathematics review

Date: 2026-09-06. This independent algebra review uses equations supplied by
the principal reviewer. It does not verify source glyphs, assign an author's
intended physical meanings, fit parameters, or test physical validity.
Source reviewers are checking the book notation separately. No external
criticism or modern reference measurement enters the calculation.

## Assumptions and supplied equations

Assume `m0>0`, `c>0`, `h=2 pi hbar>0`, and

```text
0 < beta = v/c < 1
s = sqrt(1-beta^2)
gamma = 1/s
m = gamma m0
p = mv = beta mc.
```

The supplied EDM1 printed-page 81/288 relation is

```text
E^2 = (m^2-m0^2)c^4 = beta^2 m^2 c^4 = p^2 c^2.
```

The supplied EDM2 printed-page 301 relations are

```text
E_k = m v_H c = beta mc^2
mc^2 = ch/lambda_H
lambda_H = 2 pi r_H
y = r_H sqrt(1-beta^2).
```

Using the same beta across these equations includes the supplied
identification `v_H/c=beta`. Its validity as a source identification must
be checked independently; it is not established by this algebra.

## Energy distinction

For positive energy, the supplied squared relation gives `E=pc`, because
`m0=ms` implies `m^2-m0^2=m^2 beta^2`. This is not the same expression as
the separately introduced kinetic-energy comparator `T=(m-m0)c^2`:

```text
E_pc = beta mc^2 = (beta/s)m0c^2
T = (1-s)mc^2 = (1/s-1)m0c^2
E_pc/T = beta/(1-s) = (1+s)/beta > 1.
```

Thus equating the source quantity to this comparator would require an
additional interpretation or a changed model. The source label `E_k`
does not by itself license silently replacing its displayed formula.
The squared energy equation also permits a negative root before a positive
energy convention is imposed; that convention is explicit here.

At the exact rational case `beta=3/5`, `s=4/5` and `gamma=5/4`:

```text
m = (5/4)m0
p = (3/4)m0c
E_pc = (3/4)m0c^2
T = (1/4)m0c^2
E_pc/T = 3.
```

For beta approaching zero from above,

```text
E_pc/(m0c^2) = beta + beta^3/2 + O(beta^5)
T/(m0c^2) = beta^2/2 + 3 beta^4/8 + O(beta^6).
```

Their leading orders therefore differ. Both energies tend to zero, but
their ratio diverges as `2/beta`; they cannot be identified by that shared
zero limit. No physical conclusion about what the source intended follows
without resolving its terminology and assumptions.

## Wavelength and radius distinction

The supplied wavelength equation gives

```text
lambda_H = h/(mc).
```

If one additionally introduces a de Broglie reading `lambda_dB=h/p`, then

```text
lambda_dB = h/(beta mc) = lambda_H/beta
lambda_dB/lambda_H = 1/beta > 1.
```

The two expressions are incompatible only if they are asserted to describe
the same wavelength at the same beta, m, and p. Distinct wavelengths may
coexist without an algebraic contradiction. Equality would require beta
one, which is excluded by the present massive-particle domain; approaching
that endpoint is a limit, not a valid finite-gamma substitution.

With `L0=hbar/(m0c)` as the length unit, the source relations imply

```text
r_H = hbar/(mc) = L0 s
y = r_H s = L0 s^2 = L0(1-beta^2).
```

At `beta=3/5`, `r_H/L0=4/5`, `y/L0=16/25`, and the additionally introduced
wavelength ratio is `lambda_dB/lambda_H=5/3`.

If the radius relation is also deliberately applied to lambda_dB, that
alternative construction has `r_dB/L0=s/beta` and `y_dB/L0=s^2/beta`.
It is a changed diagnostic construction, not another name for source y.

## General dimensionless closure

Take the supplied charge-energy relation and explicitly define alpha_prime:

```text
e^2(1-C) = 4 pi epsilon0 y E
alpha_prime = e^2/(4 pi epsilon0 hbar c).
```

Parameterize the two independently selectable diagnostic substitutions as

```text
E = f(beta)mc^2
lambda = g(beta)h/(mc)
r = lambda/(2 pi)
y = r s.
```

Then

```text
y = g(beta) hbar s/(mc)
y E = g(beta) f(beta) hbar c s
K := alpha_prime(1-C) = g(beta) f(beta) s.
```

This cancellation is exact and requires no mass calibration. It does
require retaining the same radius/length relation while making the chosen
energy and wavelength substitutions. The quantities f, g, beta, s, K, C,
and alpha_prime are dimensionless. In SI units `y E` has units `J m`,
matching `hbar c`; `epsilon0 y E` has units `Coulomb^2`, matching e squared.
For positive f, g, and nonzero charge, positive K additionally requires
`1-C>0`. The algebra does not supply a numerical C or a fitting rule.

The three deliberately distinct constructions are:

| Construction | f(beta) | g(beta) | K(beta) | Exact K at beta=3/5 |
| --- | --- | --- | --- | --- |
| Supplied source equations | beta | 1 | beta s | 12/25 |
| Energy replacement only | 1-s | 1 | s(1-s) | 4/25 |
| Energy and wavelength replacement | 1-s | 1/beta | s(1-s)/beta | 4/15 |

The last expression can also be written `beta s/(1+s)`, avoiding
subtraction of near-equal values for small beta. In particular,

```text
K_energy_only/K_source = beta/(1+s)
K_combined/K_source = 1/(1+s)
K_energy_only < K_combined < K_source, for 0<beta<1.
```

Near beta zero their respective leading behaviors are `beta`, `beta^2/2`,
and `beta/2`. Although the combined expression has a continuous zero limit,
its chosen `g=1/beta` is singular there. That limit does not make the full
wavelength/radius construction defined at beta zero.

These are comparisons of different declared assumptions. None is a fit,
an uncertainty envelope, an experimentally preferred model, or a proof of
the physical assumptions behind the source relations. No implementation
was supplied for this stage, so no script or test review is claimed yet.

Only this review file was created. No canonical equation, diagnostic
script, data snapshot, source record, or Git state was modified.

## Implementation review - 2026-09-06

Independently reviewed `scripts/audit_energy_kinematics.py`,
`tests/test_energy_kinematics.py`, the stored diagnostic JSON, and
`NORM-ENERGY-KINEMATICS-DIAGNOSTICS.md`. The earlier statement that no
implementation had yet been supplied applies only to the preceding
algebra stage. This follow-up accepts the present implementation within
its stated conditional scope; no numerical defect was found.

The principal reviewer reports that the source agent confirmed the `pc`
relation at EDM1 printed81/PDF88 and printed288/PDF294, and that the
principal reviewer visually checked the historical comparator formula in
Einstein1905, printed920. Those are reported source checks, not page-image
inspections performed in this mathematical review. The precise transfer
of `m=gamma m0` and the same velocity into EDM2 remains an explicit
assumption rather than an independently established physical bridge.

### Reproduced output and meaning

Executed from the repository root:

```text
python -B scripts/audit_energy_kinematics.py --check --verify-sources
# Both Heim book source hashes verified.
# Energy/wavelength diagnostic snapshot matches fresh calculation.

python -B -m unittest discover -s tests -v
# Ran 43 tests, including 10 energy-kinematics tests; OK.
```

Every field of `kinematic_ratios` implements the conditional formulas
derived above. The three K functions retain separate names and do not
silently equate source pc with T, or lambda_H with h/p. The JSON records
the mass/velocity bridge, dimensionless normalization, separate
substitution statuses, and limitations on interpreting the lengths.

The book example gives

```text
small beta = 0.00729735459756713536...
pc/T       = 274.068273264428799...
lambda_dB/lambda_H = 137.0359609951515777422...
```

These are derived from the selected source-formula branch, not imported
experimental alpha values. The coincidence of the wavelength ratio with
the inverse of this beta follows identically from `1/beta`; it is not a
second independent numerical prediction. The source closure residual
`-2e-82` is ordinary rounding at 80-digit precision, not a physical residual.

### Source K and existing profiles

The implemented book index mapping follows the separately documented
`NORM-BOOK-ETA-INDEX-BRIDGE.md`. With the helper's keyword order made
explicit, its two inputs are

```text
eta11 = eta_k_q(k=1,q=1) = pi/(pi^4+5)^(1/4)
eta12 = eta_k_q(k=2,q=1) = pi/(pi^4+6)^(1/4).
```

The unindexed vartheta is computed from `eta=pi/(pi^4+4)^(1/4)`;
the implementation does not replace it by either indexed vartheta.
With `Y3=1`, `C=A1 A2` and
`K=9 vartheta(1-C)/(2 pi)^5` are correct. The returned small and large
positive roots solve `beta sqrt(1-beta^2)=K`; the source example explicitly
uses the small root while retaining both in the profile data.

At 100 digits, an independent direct fourth-root evaluation of the two
eta expressions agreed to better than `1e-95`. The resulting K matched
the existing `1982_printed_alpha_fit_variant` arithmetic exactly at the
same pi/context, while differing from the existing `1982_source_literal`
profile. This is a shared mathematical expression with distinct source
provenance: the new book mapping does not retroactively convert the old
IGW diagnostic into an IGW source-literal reconstruction.

The inverse small root also agrees with the earlier independently pinned
value `137.0359609951515777422060897...`. None of the older profiles or
their provenance needs to be changed to perform this comparison.

### Numerical stability and domain

Using `s=sqrt((1-beta)(1+beta))` preserves a resolved Decimal distance
from beta to one. The rationalized expression `beta^2/(1+s)` for `1-s`
and `beta s/(1+s)` for the combined K avoid small-beta cancellation.
These are algebraically the same functions already derived above.

All actual report inputs are finite and strictly between zero and one;
the helper rejects the excluded endpoints and nonfinite inputs. The
report's 40-200-digit limits are enforced. The helper uses the caller's
Decimal context, so its returned values are rounded approximations, not
interval enclosures or guarantees about a much smaller difference between
two nearly equal returned values. In particular, an s printed as one at
tiny positive beta is not a claim that beta is zero or that T vanishes.

Independent supplementary probes used 200-digit direct reference formulas
at `beta=1e-40` and `beta=0.` followed by eighty nines. Their 30-digit
helper results agreed within relative error `1e-28` for s, gamma, both
energy ratios to `m0c^2`, pc/T, y/L0, and both substituted K functions.
The maximum observed errors were about `1e-80` and `2.14e-31`, respectively.

Another independent check used four exact rational Pythagorean pairs
`(beta,s)=(3/5,4/5),(4/5,3/5),(7/25,24/25),(44/125,117/125)`.
All 52 comparisons of the 13 derived fields against Fraction-based
reference expressions agreed to better than `1e-95` at 100 digits.

### Test strength and remaining coverage limitation

The ten committed tests meaningfully cover the known rational case,
independent scale cancellation, ordering, invalid beta, near-zero and
near-one stability, the energy-squared identity, precision limits,
convergence, and declared profile metadata.

One targeted gap remains: the new book-source calculation is tested for
self-consistency of its solved closure, but no dedicated new regression
independently pins its source indexing and unindexed vartheta. Changing
the eta12 arguments while solving the changed K again could still pass
that closure test. A regression based on the explicit `pi^4+5`,
`pi^4+6`, unindexed `pi^4+4` definitions and the independently known inverse
small-root value would protect the source mapping. The supplementary
review checks above establish that the current mapping is correct; this
is a coverage recommendation, not a present arithmetic defect.

Likewise, `target_fitting=False` and an empty reference-input list are
metadata assertions, not by themselves a proof of data independence.
Static inspection supplies the additional evidence here: the new script
never reads empirical reference inputs and calls only the mathematical
helpers and source-hash verifier from the shared module.

No code change was made or required by this review. The remaining
physical/source-meaning qualifications must accompany any use of these
numbers; substituting two expressions does not construct a complete
alternative physical model. This follow-up changed only this review file.

## Final regression and report review - 2026-09-06

The new `test_book_source_index_regression` closes the targeted coverage
gap. It independently spells out the `pi^4+4`, `pi^4+5`, and `pi^4+6`
denominators, checks the unindexed vartheta, and checks the inverse small
root against the previously verified formula value. Its reference number
is explicitly a regression value, not an experimental target.

Independent rerun: all 44 tests passed, including the 11 energy-kinematics
tests. `audit_energy_kinematics.py --check --verify-sources` also passed;
the stored numeric snapshot and both book hashes remain consistent.

Reviewed `06_docs/ENERGY_KINEMATICS_2026-09-06.md` for mathematical
overinterpretation. The factors approximately 274 and 137 correctly refer
to the calculated small source branch under the documented common
mass/velocity interpretation. They are neither measured discrepancies
nor independent successes of the model. The report explicitly identifies
the second ratio as `1/beta`, treats the two wavelength expressions as
conflicting only if they denote the same wave, and preserves the
conditional transfer of `m=gamma m0` into the EDM2 passage.

The differential comparison is correct under its stated mechanical
definitions, with fixed rest mass and c and scalar momentum magnitude
`p=gamma m0 v`:

```text
dp/dv = m0 gamma^3
dT/dv = m0 gamma^3 v
dT = v dp
d(pc) = c dp.
```

For vector momentum, the mechanical statement is `dT = v_vector dot
dp_vector`; a change of direction at fixed speed does not imply added
kinetic energy. The report uses scalar p and conditional mechanical
language, so it does not silently establish a new source dynamics or
extend the scalar comparison to such a vector claim. The identity follows
from the defined energy/momentum functions; applying it to a source
work/potential balance still requires the physical interpretation that
the report expressly leaves open.

No unresolved arithmetic or mathematical-interpretation defect remains
from this bounded review. The report does not turn a source transcription,
a numerical closure, or the proposed substitutions into physical
validation. This final follow-up changed only the present review file.
