# Gamma / Q_N and excitation-bandwidth relation: bounded source review

Date: 2026-09-06
Scope: H006's N, `F(Gamma)`, `Q_N`, and resonance-limit passages, with the
later H007 B37 and its closing remarks compared as a separate IGW edition.
This is a source reconstruction, not a modern decay-width interpretation
and not a numerical implementation.

## Sources and visual scope

H006 is *Die Massenformel nach Burkhard Heim (1982)*.  Its cover calls it
a reproduction of Heim's original document for programming his mass
formula; the reproduction is labelled Forschungskreis Heimsche Theorie,
IGW Innsbruck 2002, while running pages carry an IGW 2003 copyright.
The source's last page is dated and signed 25.2.1982.  These facts support
the label “1982 material in an IGW reproduction”; they do not turn the
reproduction's typesetting into an independent author manuscript.

Full-page visual checks:

| source | PDF folio | printed page | checked material |
| --- | ---: | ---: | --- |
| H006 | 8 | 8 | (XXV)--(XXIX): N, `f(N)`, `F(Gamma)`, explicit open question about Gamma and `Q_N` |
| H006 | 9 | 9 | `Q=Q(0)` numerical procedure, occupation restrictions, and start of resonance limits |
| H006 | 10 | 10 | limits of the resonance spectra |
| H007 | 5 | 14 | B32, the later excitation-function form |
| H007 | 6 | 15 | B37--B41, especially `Q(N)` and `K_B` |
| H007 | 11 | 20 | closing qualifications and the `z=0` approximation |

Visual anchors are `tmp/pdfs/gamma_qn_igw/h006-08.png`,
`h006-09.png`, `h006-10.png`, and
`tmp/pdfs/eta22_roles_igw/h007-pre-05.png`, `h007-06.png`, plus
`tmp/pdfs/gamma_qn_igw/h007-11.png`.

## H006: what Gamma and Q_N actually say

H006 Druck 8/PDF 8 calls `N >= 0` a resonance order and says it selects
allowed occupation quadruples `n_j`, `1 <= j <= 4`.  Its displayed
excitation function is

```text
f(N) = [1 - Q(2-k)(1-kappa)]
       [a_vx*N/(N+2) + b_vx*sqrt(N(N-2))].              (XXV)
```

Here the first `k` is Latin `k` and the last factor is Greek `kappa`.
This distinction is visible in the page image.

The next text makes the following source claims, without supplying the
missing relation:

* It says the “unknown function” `F(Gamma)` remains zero for every
  `N != 1`, because the right side is real.
* It says `f(0)=0`; `N=0` therefore describes the state and mass
  `M_0(vx)` through (XXVI).
* It assigns `N >= 2` a spectrum of occupation-parameter quadruples and
  hence resonance masses `M_N(vx)`.
* It says there is no spectral term for `N=1`, because `f(1)` is complex.
* Its immediately displayed imaginary-part equation is
  `F(Gamma) = W_vx [1-Q(2-k)(1-kappa)] b_vx`. (XXVIII)

Most importantly, the prose immediately after (XXVIII) says that `n_j`
and `F(Gamma)` stand “in irgendeiner Beziehung” with `N` to the **full
bandwidths** `Gamma`; it then says a relation `Q_N=Q(N)` between the
double spin quantum number `Q` and `N` must exist and asks how these
relations might be constituted.  It gives neither a functional form,
unit, domain, inversion rule, nor a relation to a lifetime.  Thus the
source fixes only the name “full bandwidths” for `Gamma` in this passage;
it does not support importing a modern decay-width convention.

The same page says that, after excluding `N=1`, `F=0` and the real
relation (XXIX), with right side `W_vx(1+f)`, may be discussed.  It says
generally `f>0` for `N>=2` and `f=0` for `N=0`; for the special multiplet
`x_2`, `f=0` for every `N>=0` because
`Q(2-k)(1-kappa)=1`.  This is a source-stated route for real
occupation/mass-spectrum calculation after the N=1 exclusion.  It is not
a solution for `F(Gamma)` or for `Q_N=Q(N)`.  The `x_2` statement is an
explicit source exception; it does not relax the source's separate rule
that N=1 supplies no spectral term, and this review derives no further
all-tuple conclusion from the radical in (XXV).

## H006 numerical route and resonance bounds

H006 Druck 9/PDF 9 makes the scope of its numerical procedure unusually
explicit.  To determine `W_vx`, `a_vx`, `b_vx`, and `Phi_vx`, it says to
use **not** `Q_N=Q(N)`, but `Q=Q(0)` of the local component `x_v`.
It then starts the algorithm only at `N=0` or `N>=2`, calculates
`W_1=W_vx(1+f(N))`, and selects successive occupation quantities through
non-negative remainders.  This is the precise source basis for using
`Q(0)` in that enumeration; it does not define `Q(N)`.

The same page supplies occupancy/configuration constraints, including
`n_j+Q_j >= 0`, the outside-to-inside rise condition, and the three
`W_4` cases.  It rejects an impossible negative final occupation value
and marks a resulting N as a forbidden term; the source also says to
truncate, not round, non-special decimal tails when calculating the
integer `K_j` quantities.  H006 Druck 9--10/PDF 9--10 then gives finite
configuration and resonance limits (XXII)--(XXXV), including
`0 <= N <= L < infinity`.  These are bounds on the admissible
occupation/resonance construction.  They do not supply a Gamma formula.

This maintains both previous normalization decisions:

| decision | source-supported result |
| --- | --- |
| `NORM-1982-N-GAMMA-QN-BLOCKER` | remains blocked: the source itself asks for the `n_j`, `F(Gamma)`, `N`, full-`Gamma`, and `Q_N` relation rather than giving it. |
| `NORM-1982-SELECTION-QN-Q0-SCOPING` | remains resolved and narrow: the page-9 enumeration uses `Q=Q(0)` of `x_v`; it must not be promoted to `Q_N=Q(0)`. |

## H007: a later, still incomplete Q(N) form

H007 is a different IGW edition with a different formula family and
numbering.  On H007 Druck 14/PDF 5 its excitation function is visibly

```text
f(N) = a*N/(N+1) + b*N.                              (B32)
```

That is not H006 (XXV); neither expression should be silently substituted
for the other.

On H007 Druck 15/PDF 6, the text says excitations **could** also appear as
a change in angular momentum.  Calling `Q` the doubled angular-momentum
quantum number, it offers

```text
Q(N) = Q(N=0) + 2*z(N),                              (B37)
```

and calls `z(N)` an unknown integer-valued function.  It specifies no
non-negative or positive range and no value-selection rule for `N>0`.
If B37 is evaluated at `N=0`, `z(0)=0` follows algebraically; the source
does not state this as an independent rule.  Similarly, the formula
preserves the parity of `Q(N)` relative to `Q(0)`, but does not select a
particular `Q(N)`.

H007's B39 is important terminology but not a repair of H006 Gamma:

```text
K_B = L_(sigma)(p) - sigma_N.                        (B39)
```

The accompanying prose calls `K_B` an integer “Bandbreite”, namely the
number of possible external-field excitations of an excitation state
`M(N)`; `K_B <= 0` permits none.  This is a different, explicitly counted
external-field quantity.  H007 does not identify it with H006's “vollen
Bandbreiten Gamma”, nor does it mention `F(Gamma)` in B37--B41.

Finally H007 Druck 20/PDF 11 repeats that `z(N)` is still to be found and
therefore `Q(N)` for `N>0` remains unknown.  It calls the associated
spectral masses strongly approximate and says existence times `T_N` for
those states cannot yet be described.  It then describes

```text
z(N) = 0 for all N, hence Q(N)=Q(0)=Q
```

as an **approximation**, and claims an approximation error below 0.1 MeV.
This is the later edition's stated practical route for calculating an
approximate spectrum; it is not a derivation of `z`, an exact `Q_N`
assignment, or a Gamma/lifetime relationship.

## Bounded conclusion

H006 supports a real-spectrum enumeration for `N=0` and `N>=2` once its
own N=1 exclusion and `Q(0)` enumeration convention are used.  Its
configuration/range equations constrain which occupancy terms may occur.
But H006 expressly leaves the relation of `n_j`, `F(Gamma)`, `N`, full
bandwidths `Gamma`, and `Q_N=Q(N)` open.  H007 later supplies only an
unknown-integer even-shift form for Q and a declared `z=0` approximation;
its `K_B` bandwidth is a distinct count of external-field excitations.
Neither edition authorizes a Gamma formula, a general N>0 lifetime formula
or Gamma/lifetime bridge, an invertible `F`, or a modern-width
interpretation.
