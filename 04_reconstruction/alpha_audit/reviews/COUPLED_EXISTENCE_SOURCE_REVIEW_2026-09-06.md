# H004 coupled-existence domain: bounded source review

Stand: 2026-09-06. Focused visual review of Heim, *Elementarstrukturen
der Materie II* (1996 edition), local file
'01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf',
SHA-256 'F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849'.
Read in full: introduction printed 2--3 / PDF 13--14; printed 278 / PDF
284, 321--323 / PDF 327--329, 328--331 / PDF 334--337. Rendered images are
'tmp/pdfs/coupled_existence/edm2-013.png', '-014.png', '-284.png',
'-327.png' through '-337.png'. OCR was only a locator. This is a domain
and source-status review, not a search, mass calculation, fit, or new
selection algorithm.

## Result

For a deliberately overinclusive search of noncollapsed configurations, the
source supports

~~~text
N_(j) in integers,   N_(j) >= 0  (j=1,...,4),
beta_2, beta_3, beta_4 >= 1
~~~

on the unweighted (107)/(107a) layer. It does **not** require N_(4)>0.
Using the printed local difference identities and G_4=N_(4), these conditions
instead imply N_(1),N_(2),N_(3)>=1 and allow

~~~text
0 <= N_(4) <= N_(3)-1.
~~~

Thus N_(4)=0 belongs in a superset search. It is the empty/reference value
in one construction, while a separate transition paragraph writes
N_(j)(vx)>0 for a realised V6 state. That latter wording can motivate a
strict-positive *subcase*, but it is not a reason to silently remove N_(4)=0
from an over-set of formal noncollapsed integer candidates.

The introduction establishes an unfinished deduction programme for
metronische Strukturfunktionen and the coefficient matrix (110d); it does
not say the author knew of, deliberately left open, or later resolved the
specific post-exhaustion (107) question. The same limit applies to the
local statement that F_im was not yet deducible.

## 1. Integer and nonnegative zone domain

Printed 322 / PDF 328 states that N_(j) is an integer and requires

~~~text
N_(j) = n_j + Q_j >= 0,  (n_j)_min = -Q_j.
~~~

It labels N_(j)=0 as the empty R_3 / unreal V_6 reference point in that
construction; it is not written as an algebraically forbidden zone value.
The same page explicitly retains j=4 through delta_4N_(4)=1. Therefore a
domain that includes N_(4)=0 is source-compatible at this general level.

The local selection discussion, printed 323 / PDF 329, describes the
transition from the empty reference point to a realised grid point by

~~~text
N_(j)=0  ->  N_(j)(vx)>0.
~~~

This is positive evidence that the particular transition-to-realised-state
description uses strict positivity. It does not replace the printed general
nonnegative domain by a universal quantifier over every algebraic use of
(107), nor does it provide a different N_(4) domain for the requested
over-set.

The resonance integer N in (108)/(108a), printed 330 / PDF 336, is separate
from the four N_(j): the page gives 0 <= N <= L_N. It must not be used as a
claim that every zone occupation is positive.

Printed 322 / PDF 328 adds a relevant scope condition for the external
zone j=4: its displayed decay uses the approximations (79b)/(79c) in the
third validity range with infinitesimal tau->0, yielding the factor
mu_+ exp(-A N_(4)). Thus the later exponential in the scalar selection
formula is a source-stated, conditional approximation package; this review
does not treat it as proof of an exact, fully completed metronic theory.
For a conditional mathematical exclusion within that same package, the
needed fact is the ordinary bound 0<exp(-A N_(4))<=1 when A>=0 and
N_(4)>=0 (in the active k=1, Q_4=1 instance, A=(2k-1)/(3Q_4)=1/3).
That is a real-inequality premise, not merely a statement about decimal
rounding of the exponent. The derivation/error control of (79b)/(79c) is
outside this bounded review.

## 2. Noncollapsed (107a) layer

Equation (107a), printed 328 / PDF 334, gives for j>1 the active bandwidth
branch

~~~text
beta_j = delta_(j-1)G_(j-1) - G_j >= 1,
-Q_j <= n_j <= L_j < infinity,
~~~

and separately displays its beta_j=0, G_j=0 collapse/reset branch.
A noncollapsed over-set should retain the >=1 branch and not model the
collapse dynamically.

The source explicitly gives the relevant differences on printed 323 / PDF
329:

~~~text
delta_1G_1=N_(1)^3,  delta_2G_2=N_(2)^2,
delta_3G_3=N_(3),    delta_4G_4=1.
~~~

Together with G_4=N_(4) in (98e), printed 278 / PDF 284, this gives the
following **own algebraic unpacking** of the unweighted source gates:

~~~text
beta_2 = N_(1)^3 - G_2 >= 1,
beta_3 = N_(2)^2 - G_3 >= 1,
beta_4 = N_(3) - N_(4) >= 1.
~~~

Since the displayed G_2 and G_3 on (98e) are nonnegative for
nonnegative N_(2), N_(3), the gates imply N_(1)>=1, N_(2)>=1, and
N_(3)>=1. The last gate does not imply N_(4)>=1: it permits N_(4)=0
whenever N_(3)>=1. This is a consequence of the explicit source
equalities, not a new collapse or repair rule.

The later sigma-excitation expression (107b), printed 329 / PDF 335,

~~~text
beta_4 = delta_3G_3 - (n_4+Q_4)
       = alpha_3N_(3) - N_(4) > 0
~~~

also does not syntactically impose N_(4)>0. It supplies a separate
conditional inequality for its stated context; it is not silently
identified here with the complete earlier gate layer.

## 3. Scope of the over-set

The source thus supports two deliberately distinct domains:

| Domain | Source status | Correct use |
|---|---|---|
| General nonnegative zones, N_(j) in nonnegative integers | printed 322 / PDF 328 | Safe broad domain for a superset search |
| Noncollapsed gate subset, beta_2,beta_3,beta_4>=1 | (107a), with 323/278 identities | Narrow the broad domain without inventing collapse dynamics |
| Strict-positive N_(j)(vx)>0 transition wording | printed 323 / PDF 329 | Separate physical/realisability subcase, not a safe exclusion from the over-set |

No claim is made that every member of the broad domain is a realised
component, that the source has supplied all upper bounds, or that a
solution of the coupled equations would be a prediction. The inequalities
only define a source-supported screening domain.

## 4. Unfinished-work and author-knowledge boundary

Introduction printed 2 / PDF 13 says the work must not be regarded as
completed. The continuation, printed 3 / PDF 14, identifies an unresolved
task: to deduce metronische Strukturfunktionen of R_3 whose finite real
limits for tau->0 give the elements of coefficient matrix (110d); otherwise
(109)--(111) retain a heuristic character. It also defers listed physical
questions to a later study.

Separately, printed 331 / PDF 337 says the form of F_im cannot provisionally
be deduced, subject only to convergence to a finite constant limit. These
are genuine author statements of open work, but their stated objects are
the metronic functions/coefficient programme. They do not mention a
negative beta_j, a failed post-exhaustion (107) check, a rollback rule, or
the author’s awareness of such a case.

Within the inspected sources there is likewise no evidence of a later
authorised resolution of that exact issue. Absence from this bounded
review is not proof about every manuscript, the author’s private knowledge,
or what remained open until his death.

## Bounded conclusion

For an own coupled-existence diagnosis, use the nonnegative integer domain
with the explicit noncollapsed gates and retain N_(4)=0. Report any strict
positivity check as an additional, separately labelled subcase. Do not
infer an author intention or a lifetime conclusion from the unfinished
F_im/(110d) programme or from the local absence of a beta_j<0 branch.
