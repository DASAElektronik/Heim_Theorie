# H006 nu/x versus v/x: bounded alias-source review

Date: 2026-09-06

Scope: H006, *Die Massenformel nach Burkhard Heim (1982)*, only the
source-local relationship of W_nu_x/w_nu_x/a_nu_x/b_nu_x and the
previously registered W_vx/a_vx/b_vx and x_v/x_vx spellings. This review
does not calculate a mass, choose a state, alter a normalization, or infer
an alias into H007 or any manuscript edition.

## Result

H006 itself supplies a direct positive bridge. The character read earlier
as Latin v in the page-8/page-9 family is the same Greek nu used and
defined on printed page 3. In this H006 edition:

    nu = running digit of a multiplet x_nu
    x  = component of that multiplet
    W_nu_x = g(q,k) * w_nu_x

and the selection, structure-potency, resonance-basis, N=0, and tuple
algorithm passages use that one nu,x family. Thus the distinction
W_nu_x versus W_vx is not source-supported as a distinction of variables;
it originated in transcription/reading of a glyph whose serif form can
resemble v.

This is stronger than visual resemblance alone: H006 printed page 6
explicitly says that w_nu_x is the structure potency of the discussed
state, as component x of multiplet nu, immediately after defining
W_nu_x=g(q,k)w_nu_x. It provides the missing definition-and-dependency
chain.

The conclusion is deliberately narrow: it establishes the alias for the
H006 printed source. It does not validate every later implementation
choice, solve the selection algorithm, establish a source-independent
historical original, or authorize joining H006 to H007 symbols.

## Visual scope and source status

The complete H006 printed pages 1--9 (PDF folios 1--9) were rendered at
300 dpi and inspected full-page. Rendered working images are:

    tmp/pdfs/n0_alias/h006-01.png through h006-09.png

H006 calls itself a reproduction of Heim's 1982 original for programming
the mass formula (cover, printed/PDF 1); the running pages carry IGW 2003.
The source status here is therefore the visible H006 IGW-edition notation,
not an independently established author-manuscript glyph.

| H006 printed/PDF page | direct relevance |
| --- | --- |
| 1 | edition/reproduction title only |
| 2 | configuration and component-symbol definitions; no competing v variable |
| 3 | defines x_nu and nu; lists ground-state multiplets |
| 4--5 | auxiliary/mass material; no W-family redefinition |
| 6 | core selection equation, W_nu_x=g(q,k)w_nu_x, and prose definition of the nu,x pair |
| 7 | a_nu_x and b_nu_x resonance-basis formulas |
| 8 | N-rule, f(N), W_nu_x, x_nu_x, M0(nu x), and N>=2 spectrum |
| 9 | numerical tuple algorithm with W_nu_x/a_nu_x/b_nu_x/Phi_nu_x, x_nu, x_nu_x and M_N(nu x) |

The corresponding existing image anchors are also
07_outputs/source_check_images/1982_massenformel/page-03.png,
page-06.png, page-07.png, page-08.png and page-09.png.

## Exact source chain

### 1. nu is defined, not an undeclared Latin v

On H006 printed 3/PDF 3, under the possible ground-state multiplets, the
source visibly says:

    Multiplett x_nu der laufenden Ziffer nu for epsilon=+1
    and Antimultiplett x-bar_nu for epsilon=-1.

The general notation immediately below is x_nu followed by the
configuration and charge list. Thus nu has a stated role: the running
multiplet digit. The same page enumerates x_1, x_2, ... x_12. No Latin
variable v is introduced in this definition.

This page also defines q_x as the signed charge number of component x of
an isospin multiplet and constrains 0 <= x <= P. It therefore separates
the component index x from the running multiplet digit nu before any W
quantity occurs.

### 2. W, w, and the pair index are joined in one displayed block

On H006 printed 6/PDF 6:

- (XIV), the selection rule, has W_nu_x on the right and a_nu_x and
  b_nu_x inside its N-dependent factor.
- The immediately following (XV) defines:

      W_nu_x = g(q,k) w_nu_x.

- The following prose labels w_nu_x the structure potency of the
  discussed state and says it is the component x of multiplet nu.
- (XVI)--(XIX) continue the same w_nu_x family, including w_nu_x(k).

This is a direct semantic equation, rather than a conclusion from a
similar-looking subscript. It shows that the selection target W_nu_x and
the preceding structure-potency computation are intended to be connected
within the printed H006 construction.

### 3. The resonance basis and the N passage preserve the same family

H006 printed 7/PDF 7 defines a_nu_x in (XX) and b_nu_x in (XXIII).
The page has no definition of a separate a_vx or b_vx.

H006 printed 8/PDF 8 then writes the N-function f(N) with a_nu_x and
b_nu_x in (XXV), and gives the N=0 relation with W_nu_x in (XXVI). Its
prose names the state x_nu_x, calls x its component of multiplet x_nu,
and labels the mass M0(nu x). It uses the same forms in the real and
imaginary N=1 lines and in (XXIX).

H006 printed 9/PDF 9 begins: for numerical determination of
W_nu_x, a_nu_x, b_nu_x and Phi_nu_x, use Q=Q(0) of x_nu, not Q_N=Q(N).
It continues with W_nu_x(1+f(N)) and ends that the obtained quadrupel is
used with Phi_nu_x to give M_N(nu x) for x_nu_x.

The local source chain is consequently:

    x_nu (multiplet; nu = running digit), x (component)
      -> w_nu_x(k,P,Q,kappa,epsilon,C,q_x)
      -> W_nu_x = g(q,k) w_nu_x
      -> a_nu_x, b_nu_x and f(N)
      -> N=0 / N>=2 selection equation
      -> n_j and Phi_nu_x -> M_N(nu x) for x_nu_x.

This does not assert that n_j has been determined, only that the apparent
W-family spelling break is absent from the source.

## Assessment of the existing normalization records

The three inspected records did useful harm-reduction work at the time:
they preserved uncertain source-local forms and forbade a silent
implementation alias. The new full-page reading provides evidence that
their premise about two spelling families is incorrect for H006.

| existing record | what remains sound | what this source review changes |
| --- | --- | --- |
| NORM-1982-SELECTION-VX-NUX-SCOPING | do not join unrelated editions or silently change an index merely for a numerical result | Its page-8/page-9 claim of Latin vx conflicts with the full H006 chain. H006 has one Greek-nu/x family, not two semantic families. |
| NORM-1982-ALGO-VX-SCOPING | Q=Q(0) of x_nu has a source-local scope | The displayed x_v / x_vx transcription should be reread as x_nu / x_nu_x. There is no source evidence of a separate Latin-v state name on this page. |
| NORM-1982-WVX-SYMBOL-FAMILIES | w_nu_x, a_nu_x, b_nu_x and the A matrix are correctly isolated as H006 source constructs | It is not merely a preliminary family that lacks a page-8/page-9 counterpart: (XIV)--(XXIX) and the page-9 algorithm visibly reuse it. |

No existing normalization file was edited in this task. A later authorized
normalization change may replace the H006-only vx/nu_x blocker with one
canonical Greek-nu/x family, but should preserve the original visible
transcriptions and cite this review. It should not extend that result to
another document merely because its glyphs look similar.

## Negative findings and residual limits

- Across complete H006 pages 1--9, no source definition, equation, or
  prose passage introduced a separate Latin v index whose role differs
  from nu.
- The source does not define W_nu_x by a table of numerical values; it
  gives the formula W_nu_x=g(q,k)w_nu_x and the downstream tuple procedure.
  The alias result does not make the full mass calculation ready.
- The source still leaves the Gamma/Q_N relationship open and retains the
  documented W4 and integerization questions. Those are independent of
  this glyph correction.
- The review does not infer that x_nu's ground-state label is an
  occupation quadruple n1..n4.
- H006 is an IGW reproduction. The result is a high-confidence reading of
  this edition's internal notation, not a claim that every historical
  manuscript used the same typesetting.

## Narrow x2/e- base-case consequence (no mass evaluation)

The alias result permits one limited source-algebra check for the H006 x2
electron component.  From printed 3/PDF 3, use the already visible
configuration values k=1, P=1, Q=1, kappa=0, epsilon=+1, C=0, and choose
the printed e- component x=1.  Equation (II) then gives q_x=-1 and q=1.
This is not an occupation tuple.

On printed 6/PDF 6, (XVII) has w(1)=0 because (1-Q)=0 and kappa=0.
In (XVIII), every addend of w(2) has one of the vanishing factors
q-1, 1-P, choose(P,2), kappa, choose(Q,3), or choose(P,3); hence w(2)=0.
The potentially hidden local domains do not obstruct that reduction:
eta_qk is positive at k=q=1; the denominator in the choose(P,2) term is
1+A24(1+q_x)=1; 3-q=2; and
8-A66^(q(q-1))=8-A66^0=7.  This checks the local displayed brackets, not
every independent numerical property of the A-matrix proposal.

The uncorrected (XIX) would contain w(2)^0=0^0 at k=1.  The prose printed
immediately below (XIX) explicitly says such improper 0^0 structural
potency terms must have value 1 and supplies the programming form
w_nu_x(k).  Its next sentence specializes the mesonic case to
w_nu_x(k=1)=1+w(1), so the source-directed value here is w_nu_x=1.  With
(XV), therefore, W_nu_x=g(q,k), where that same equation explicitly calls
g the base ascent for n_j=0.

For N=0, printed 8/PDF 8 gives f=0 and (XXVI).  Substitution n_j=0 into
**(XXVI)** has left side g(q,k): for k=1, Q4=1 from (X), so its exponential
is exp[(1-2k)/3], exactly the exponential in (XV).  Hence n=(0,0,0,0) is
a source-consistent base solution of the N=0 equality for this component,
without a mass fit.

This deliberately does **not** use (XIV) for that equality.  Its printed
exponent visually reads exp[1-2k(n4+Q4)/(3Q4)], whereas (XV), (XXVI), and
the page-9 algorithm display the parenthesized (1-2k) form.  No silent
repair of (XIV) is made here.  Nor does the base-solution identity by
itself prove that the page-9 maximal-remainder procedure has this tuple as
its unique output; that still needs its own inequality and algorithm audit.

## Bounded conclusion

A H006-only calculation may no longer cite a source-level vx versus nu_x
mismatch as a reason to disconnect the structure-potency formula from the
N=0 selection target. The printed source explicitly connects them through
the single Greek-nu/x index pair. It remains necessary to retain other
selection and provenance limits, and no mass-fit criterion has been used
to reach this result.
