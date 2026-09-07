# Lorentz boost and circle geometry: conditional mathematics review

Date: 2026-09-06. This review checks the specified Lorentz transformation
and the geometry of a static circle. It does not inspect source glyphs,
define the source operator `A_-`, reconstruct a rotating Heim shell, or
claim physical validation. The formulas under review were supplied by the
principal reviewer. No external criticism or modern measurement is used.

## Exact boost example

Assume positive fixed rest mass m0, positive c, vanishing transverse
momentum, and future-directed positive energy. Define

```text
epsilon = E_tot/(m0 c^2)
q = p_x/(m0 c)
b = u/c, with |b|<1
gamma_b = 1/sqrt(1-b^2).
```

Here b is the relative speed of two inertial frames. It is not silently
identified with any source alpha or another particle-speed parameter.
The supplied boost is

```text
epsilon' = gamma_b (epsilon-b q)
q'       = gamma_b (q-b epsilon).
```

Direct expansion gives

```text
epsilon'^2-q'^2
 = gamma_b^2 [(epsilon-bq)^2-(q-b epsilon)^2]
 = gamma_b^2 (1-b^2)(epsilon^2-q^2)
 = epsilon^2-q^2.
```

Thus a unit mass shell stays exactly one. At `b=3/5`, `gamma_b=5/4`,
all values in the following table are exact rationals:

| Initial (epsilon,q) | Boosted (epsilon',q') | Initial pc/(m0c^2) | Boosted pc/(m0c^2) | Initial T/(m0c^2) | Boosted T/(m0c^2) |
| --- | --- | --- | --- | --- | --- |
| (1,0) | (5/4,-3/4) | 0 | 3/4 | 0 | 1/4 |
| (5/4,3/4) | (1,0) | 3/4 | 0 | 1/4 | 0 |

The table uses the positive magnitude `pc/(m0c^2)=|q|` and the separately
defined comparator `T/(m0c^2)=epsilon-1`. A negative boosted q denotes
opposite motion, not negative pc. Both rows have mass shell one before
and after the boost. The first row observes an initially resting particle
from a moving frame; the second boosts into the particle's rest frame.

The inverse boost has parameter `-b`. The two displayed rows deliberately
use the same positive b but different initial states; the second is not
the inverse transformation applied to the first row's negative-q output.

## Scalar invariance versus equation form

For the ordinary four-momentum used here,
`E_tot^2-p_x^2 c^2=m0^2 c^4` is a scalar invariant in this one-dimensional
sector. The individual positive values pc, T, and E_tot are not scalar
invariants, as the exact table already demonstrates.

The identity

```text
(pc)^2 = E_tot^2-(m0 c^2)^2
```

nevertheless holds in each frame when every quantity is recalculated
in that frame. Retaining the form of an equation does not mean that
each side separately has the same numerical value before and after
a boost. A distinction between these two meanings of "invariant" is
therefore necessary before evaluating the source language.

This example neither supplies nor rules out a distinct source definition
of `A_-`. Any claim about that operator requires its actual definition,
arguments, and transformation rule. It cannot be settled by assigning
ordinary pc to an unspecified source object.

## Simultaneous image of a static circle

Take a circle at rest in S with R>0. Its material worldlines have constant
spatial coordinates

```text
x = R cos(theta)
y = R sin(theta),  0<=theta<2 pi,
```

at every S time t. For an x-direction boost,

```text
t' = gamma_b (t-u x/c^2)
x' = gamma_b (x-u t)
y' = y.
```

The equal-time section `t'=0` selects `t=u x/c^2`, which generally differs
between points around the circle. Substitution gives

```text
x' = x/gamma_b = (R/gamma_b) cos(theta)
y' = y         = R sin(theta).
```

This is an ellipse with semiaxes `R/gamma_b` and R. The conclusion uses
the circle's static worldlines; simply boosting events chosen at one
common S time would not yield a simultaneous S' shape.

Let `s_b=1/gamma_b=sqrt(1-b^2)`. Its perimeter is

```text
L' = R integral_0^(2 pi) sqrt(s_b^2 sin^2(theta)+cos^2(theta)) dtheta
   = R integral_0^(2 pi) sqrt(1-b^2 sin^2(theta)) dtheta.
```

For `0<|b|<1`, the integrand is between s_b and one, with strict
inequalities except at isolated angles. Consequently

```text
2 pi R/gamma_b < L' < 2 pi R.
```

In particular `L'` is not `L/gamma_b`, where `L=2 pi R` is the static
circle's original circumference. Applying one longitudinal contraction
factor uniformly to all tangent directions would not reproduce this
simultaneous ellipse.

## Independent perimeter bounds useful for numerical tests

The following stronger bounds require no numerical elliptic integral:

```text
(1+s_b)/2 < L'/(2 pi R) < sqrt((1+s_b^2)/2), for 0<|b|<1.
```

For the lower bound, the weighted root-mean-square inequality gives
`sqrt(s_b^2 sin^2(theta)+cos^2(theta)) >= s_b sin^2(theta)+cos^2(theta)`.
The inequality is strict for a nonzero set of angles when s_b differs
from one. Integrating gives `(1+s_b)/2`. The upper bound follows from
strict concavity of the square root applied to the varying integrand's
squared expression, whose angular mean is `(1+s_b^2)/2`.

At `b=3/5`, these yield

```text
9/10 < L'/(2 pi R) < sqrt(41/50),
```

which in particular excludes the proposed uniform factor `4/5` without
relying on a fitted or imported numerical perimeter value. At b zero
the bounds meet at one; that is a separate non-contracted limit.

## Interpretation boundary

This is a counterexample to a universal assertion that a Lorentz boost
alone contracts every circle's whole circumference by `1/gamma_b`.
It shows why the frame, simultaneity section, directions, and definition
of geometric length matter.

The static circle is not a rotating ring, not a source shell with unknown
internal structure, and not a direct replacement for a Heim geometry.
No conclusion about that particular shell's correct circumference follows
until its worldlines, reference frame, time slicing, and intended length
are defined. The present algebra therefore diagnoses an underdetermined
general inference; it does not complete the missing source construction.

No implementation was supplied at this stage; a later code review will
be recorded separately. Only this review file was created. No canonical
source, equation, implementation, output snapshot, or Git state was changed.

## Additional conditional source-block algebra - 2026-09-06

The principal reviewer supplied a provisional transcription of an EDM1
printed-page 21 two-dimensional block:

```text
A = [[cos(psi),  i sin(psi)],
     [-i sin(psi), cos(psi)]]
tan(psi) = i beta
claimed relation: A A^T = I.
```

Source glyph verification is pending. This subsection uses ordinary
analytic sine, cosine, and tangent, real `|beta|<1`, `i^2=-1`, and T
meaning ordinary transpose. It does not establish the source notation or
authorial intent, and it does not repair a canonical source expression.

Writing `c_psi=cos(psi)` and `s_psi=sin(psi)`, direct multiplication gives

```text
A A^T = (c_psi^2-s_psi^2) I.
```

There are no surviving off-diagonal terms. The trigonometric identity and
the supplied tangent condition imply

```text
c_psi^2+s_psi^2 = 1
s_psi^2/c_psi^2 = -beta^2
c_psi^2 = 1/(1-beta^2)
s_psi^2 = -beta^2/(1-beta^2).
```

Consequently

```text
A A^T = [(1+beta^2)/(1-beta^2)] I
A A^T-I = [2 beta^2/(1-beta^2)] I.
```

The block is therefore not orthogonal at any nonzero beta in this domain.
At `beta=3/5`, its product is exactly `(17/8) I`, with defect `(9/8) I`.
This conclusion concerns the specified 2x2 block, not a claim that every
entry of a surrounding 4x4 product has that same factor.

For the branch continuous from the identity at beta zero,
`c_psi=gamma` and `s_psi=i gamma beta`, giving

```text
A = [[gamma, -gamma beta],
     [gamma beta, gamma]].
```

At beta 3/5 this is `[[5/4,-3/4],[3/4,5/4]]`. For example, it maps
the vector `(1,0)` to `(5/4,3/4)`, whose bilinear squared norm is `17/8`
rather than one. Choosing the common opposite sign of cosine and sine
negates A and leaves `A A^T` unchanged; a trigonometric branch-sign choice
therefore does not remove the defect.

For comparison only, the different block without the two additional i
factors is

```text
B = [[cos(psi), sin(psi)],
     [-sin(psi), cos(psi)]],
B B^T = (cos(psi)^2+sin(psi)^2) I = I.
```

Under the same tangent condition and identity-connected branch, this is

```text
B = [[gamma, i gamma beta],
     [-i gamma beta, gamma]],
```

the conventional boost in coordinates `(x,ict)`. It preserves the complex
bilinear expression `x^2+(ict)^2=x^2-c^2 t^2`. Complex orthogonality uses
transpose and is not the same as unitarity using conjugate transpose;
B is not generally unitary. For the conditionally substituted real A,
ordinary and conjugate transpose coincide, so switching between those
operations would not restore orthogonality in this example.

Removing the additional i factors is one algebraically consistent
comparison, not a verified correction or established authorial intent.
Any nonstandard source definition of the trigonometric symbols, product,
or coordinates would need to be sourced before using it to reinterpret
this calculation. Pending glyph review, the finding remains strictly:
the supplied literal block, tangent relation, ordinary analytic
trigonometry, and claimed orthogonality cannot all hold for nonzero beta.

Only this review file was amended. No source equation was changed.

## Independent implementation review - 2026-09-06

Reviewed `scripts/audit_lorentz_meaning.py`,
`tests/test_lorentz_meaning.py`, the diagnostic JSON,
`NORM-LORENTZ-MEANING-DIAGNOSTICS.md`, and the separately produced
`INVARIANCE_RATIONALE_SOURCE_REVIEW_2026-09-06.md`.

The source reviewer now reports visual confirmation of the printed p.21
block and tangent condition. It also records the p.56/PDF63 R6 matrix with
its different off-diagonal notation. These are source-review findings,
not page images independently inspected by this mathematics reviewer.
The latter matrix is in a different six-dimensional construction and
does not authorize replacing the earlier four-dimensional source matrix.
The algebra remains conditional on ordinary analytic trigonometry and
ordinary transpose, even though the glyph uncertainty has been addressed
by the separate source review.

### Execution evidence

Run from the repository root:

```text
python -B scripts/audit_lorentz_meaning.py --check --verify-sources
# Book and historical reference hashes verified.
# Lorentz meaning snapshot matches fresh exact calculation.

python -B -m unittest discover -s tests -v
# Ran 56 tests, including 12 Lorentz-meaning tests; OK.
```

The new calculation uses exact Fraction values throughout its generated
numeric fields. Shared module imports supply path/hash helpers and source
metadata without executing another audit's model or reading measured
reference inputs. No rounding tolerance or fitted numerical target is
needed for the displayed examples.

### Bases and matrix identities

The standard reference correctly uses the real ordered pair `(ct,x)`,
or analogously `(epsilon,q)`, with metric `J=diag(1,-1)`. The implemented
matrix `L=[[gamma,-gamma b],[-gamma b,gamma]]` obeys `L^T J L=J`.
The source-literal block is separately labeled in `(x1,x4)` with `x4=ict`
and is tested against its own claimed complex-orthogonality condition.

These distinct bases must not be compared entry-by-entry as if equality
of entries were a physical equivalence criterion. For example, with

```text
P = [[0,1],[i,0]],
(x,ict)^T = P (ct,x)^T,
```

the conventional reference expressed in the complex basis is

```text
P L P^-1 = [[gamma,i gamma b],[-i gamma b,gamma]].
```

This is the B block derived above, not the literal substituted A. The
implementation avoids relying on a cross-basis comparison: the reported
source issue follows from the literal block's own exact `A A^T` product.
Its factor `17/8` and surrounding four-dimensional diagonal
`[17/8,1,1,17/8]` are correct for the stated 1-4 block with untouched
identity entries in directions 2 and 3.

Ordinary transpose and conjugate transpose remain distinct. The script
performs the intended ordinary transpose on the real substituted block;
it does not silently replace the source product with a Hermitian norm.
No claim of unitarity is needed or made.

### Momentum and simultaneous circle events

The two exact momentum cases reproduce the initial algebra. Signed q is
retained, positive pc uses `abs(q)`, and the T comparator is `epsilon-1`.
The summary validates the future unit massive shell. The general pair
transformation intentionally imposes no mass-shell condition because it
also transforms spacetime coordinates; those are different uses of the
same linear algebra, explicitly named in the helper documentation.

For each circle sample, `ct_selected=b*x` selects a simultaneous target
event with `ct_prime=0`. The exact output `x_prime=x/gamma`, `y_prime=y`
lies on the ellipse derived above. The separate test transforming
`ct=0,x=1` correctly obtains `ct_prime=-3/4`, demonstrating why a common
source-time selection is not the target frame's instantaneous shape.

### Perimeter scope and numerical domain

The perimeter fields store the analytical lower bound and the square of
the analytical upper bound. They do not claim to have integrated the
ellipse circumference. For b 3/5 the values `9/10` and `41/50` therefore
mean `9/10<P<sqrt(41/50)`, as correctly rendered by the script. The bounds
follow from the inequalities proved earlier in this review; testing the
stored fractions alone is not their mathematical proof.

The zero-speed case correctly returns coincident non-strict bounds of
one. Negative speeds give the same geometry because the bounds depend
on b squared. The static-circle scope is explicit in both normalization
and JSON; no rotating or structural source shell is substituted.

`gamma_exact` accepts exact Fraction speeds with `|b|<1` only when gamma
is also rational. Testing numerator and denominator integer squares is
correct for reduced Fractions. Rejecting, for example, `b=1/2` is a
declared exact-arithmetic limitation, not a physical speed restriction.
The internal 2x2 multiplication and coordinate helpers are not advertised
as general shape-validating or arbitrary-input physics APIs.

### Finding

The 12 new tests cover exact examples, inverse boosts, metric
preservation, energy values, admissible summaries, simultaneity, the
ellipse, analytic-bound coefficients, zero speed, both signs of the
literal matrix diagnostic, and report separation. No implementation,
matrix-sign, basis, simultaneity, or stated-bound defect was found.

The source claim's literal orthogonality problem remains a conditional
source-algebra finding, not a software failure and not a whole-theory
judgment. Its p.56 context does not establish an intended correction.
This implementation review changed only the present review file; no
canonical source, script, test, snapshot, or Git state was changed.
