# H004 structure handling after exhaustion: bounded source review

Stand: 2026-09-06. Focused visual review of Heim, *Elementarstrukturen
der Materie II* (1996 edition), local file
'01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf',
SHA-256 'F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849'.
The complete relevant pages read were printed 321--330 / PDF 327--336 and
340--342 / PDF 346--348. Images rendered for this task are
'tmp/pdfs/structure_handling/edm2-327.png' through '-336.png' and
'-346.png' through '-348.png'. OCR was only a locator. This review makes
no mass calculation, Y-factor selection, fit, or statement about material
outside the stated pages.

## Result

The book **does** specify a local restructuring at the beta_j=0 boundary:
after the stated further increase from beta_j=1, zone j collapses to G_j=0
and the preceding occupancy increases by one. It also contains a narrow
k=2, negative-W_5 transfer from zone 3 to zone 4. Neither passage supplies
an explicit post-exhaustion test-and-retry
procedure for a violation of (107)/(107a) such as a calculated beta_3<0.
In particular, the displayed maximal/exhaustion sequence has no instruction
to reset an earlier N_(j), re-run the allocation, or redefine all
G_j/delta_j after such a result.

This is a local source finding, not a claim that no such procedure exists
elsewhere in the corpus or an assertion of a book-wide inconsistency.

## 1. The conditions are stated as structure conditions

Printed 321 / PDF 327 first derives the structural requirements using the
G_j of (98d)/(98e). For a change delta_j of N_(j) in zone j, with j running
only to 3, it prints

~~~text
delta_j G_j > G_(j+1),
delta_j G_j >= delta_(j+1) G_(j+1).                 (107)
~~~

The prose calls this a continuous structural relation: occupancy of a zone
by additional Protosimplex elements is governed by zone 1. This establishes
the role of (107) as a gate on the configurations; it is not yet an
algorithm for repairing a failed candidate.

Printed 323 / PDF 329 gives the selection equation in a prior construction
and explicitly keeps the alpha_j outside delta_jG_j:

~~~text
W = sum_(j=1)^4 alpha_j delta_j G_j + ... ,
delta_1G_1=N_(1)^3, delta_2G_2=N_(2)^2,
delta_3G_3=N_(3), delta_4G_4=1.
~~~

It then writes the cubic-plus-exponential equation in n_j+Q_j. This is
positive evidence for the unweighted local delta_jG_j identities; within
the read passage it is not a global redefinition
delta_jG_j := alpha_j delta_jG_j.

## 2. Explicit boundary restructuring, but only at beta=0

The intervening excitation discussion, printed 327--328 / PDF 333--334,
defines the integer bandwidth for zone j

~~~text
beta_j = delta_(j-1)G_(j-1) - G_j.
~~~

It says a rise of the excitation function can reduce a positive bandwidth
down to the occupancy maximum beta_j=1. If G_j is then increased by one
more unit, a restructuring occurs: the beta_j=0 boundary is reached, zone j
collapses to G_j=0, and n_(j-1) increases by one. Equation (107a), printed
328 / PDF 334, records this terminal/reset branch in the form

~~~text
j>1: beta_j=delta_(j-1)G_(j-1)-G_j >= 1,
beta_j=0, G_j=0  ->  n_(j-1) -> 1+n_(j-1),
-Q_j <= n_j <= L_j < infinity.
~~~

Thus the source does contain a **specific** collapse/restructuring
mechanism. The printed beta_j=0 and G_j=0 notation describes the
collapse/reset branch; it need not be read as preservation of the
pre-collapse G_j at the trigger. The source does not say that any negative
value is to be replaced by that collapse, nor does it prescribe a backwards
reset of an already exhausted tuple with beta_j<0. Treating a negative
bandwidth as this zero boundary would be an additional rule.

## 3. What the maximal procedure says -- and omits

Printed 340 / PDF 346 introduces the exhaustion procedure conditionally:
after setting W_1=W(1+f) and “under consideration of the structural
principle (107)”, the source says alpha_1 N_(1)^3 <= W_1 and applies
exhaustion to obtain N_(1) through N_(3).

Pages 341--342 / PDF 347--348 give the concrete sequence: maximize
N_(1), subtract its cubic contribution to get W_2, repeat for N_(2), then
for N_(3), and form W_4. They next select N_(4) through a logarithm and
TRC.

The displayed order contains no explicit instruction of the form:
evaluate every (107)/(107a) inequality on the completed
(N_(1),...,N_(4)), return to an earlier zone if one fails, or choose a
different allowed predecessor. Nor do these pages give a coupled
simultaneous alternative to the ordered exhaustion. The introductory
phrase “under consideration of (107)” is source evidence that (107) is
intended to constrain the process; by itself it is not a printed
implementation of a post-allocation repair.

## 4. Two narrow, non-general interventions

### 4.1 beta_4 correction during N_(4) selection

Printed 341 / PDF 347 applies beta_4=1 from (107a) only in a stated
rounding situation: on the maximal-N_(4) branch it uses
N_(4)=TRC(alpha_3N_(3))-1 when
TRC(alpha_3N_(3))>alpha_3N_(3). This is a local correction in the
zone-4 step. It is not a rule for a negative beta_3 or for reselecting
N_(1) through N_(3).

### 4.2 k=2, W_5<0 transfer

The same page admits, only for k=2 with W_5<0 and an occupied zone 3, a
Protosimplex transfer from j=3 to j=4. It repeatedly updates the displayed
W_6 until W_6>=0, retaining the condition W_6<=alpha_3N_(3) “gemäß (107)”
and requiring N_(3)>=0. Printed 342 / PDF 348 states why analogous
transfers j=2 -> j=3 and j=1 -> j=2 are impossible: the cited G_3 and G_2
include lower-degree summands, unlike the linear comparison of G_4 and
delta_3G_3.

Accordingly this is an explicit, limited redistribution for a particular
residual branch. It neither authorizes transfer from zone 2 to 3 nor
supplies a generic solution for a failed zone-2-to-zone-3 bandwidth.

## 5. A local beta_4 equality, not a global redefinition

Printed 329 / PDF 335 has a later, explicitly sigma-excitation-specific
relation

~~~text
beta_4 = delta_3G_3 - (n_4+Q_4)
       = alpha_3 N_(3) - N_(4) > 0.                (107b)
~~~

This is positive source evidence for that equality in the later,
sigma-excitation-specific beta_4 relation. It does **not** itself say that
all earlier unweighted (98e)/(107)/(107a) relations are replaced. In
particular, printed 323 / PDF 329 also gives the unweighted local identity
delta_3G_3=N_(3), without an explanation reconciling it with the weighted
right-hand expression in (107b). The directly read pages contain no
general G/delta redefinition that resolves this local notation issue. A
calculation may compare the source layers, but may not silently promote the
later equality to a universal redefinition.

## Bounded conclusion

Within printed 321--330 and 340--342, the positive source evidence is:
(1) mandatory structural inequalities, (2) an equality-boundary collapse,
(3) a zone-4 rounding adjustment, and (4) a k=2 zone-3-to-zone-4 transfer.
The pages do **not** provide an explicit treatment of beta_j<0, a generic
rollback/coupled re-selection after maximal allocation, or a universal
weighted redefinition of the structural quantities. This leaves a concrete
implementation question open; it does not identify a correction to Heim's
text.
