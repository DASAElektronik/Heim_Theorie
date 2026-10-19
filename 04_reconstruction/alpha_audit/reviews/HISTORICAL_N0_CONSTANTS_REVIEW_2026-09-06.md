# Historical N=0 constants and provenance review — 2026-09-06

## Scope and method

This is a static audit only.  It reads H006 and the unpacked H010 Pascal/C
files plus the saved C output; neither program, macro, spreadsheet, nor an
external executable was run.  It asks which assignments are live in the
later implementation files and whether their printed output can be safely
joined to the conditional H006 N=0 reconstruction.  It is not a mass
calculation or a comparison with a current experimental value.

Inputs inspected:

* H006, *Massenformel nach B. Heim 1982*, printed/PDF pp. 4--5 for its
  displayed constant set; the project freezes its editorial provenance as
  1982 material in an IGW 2002/2003 rendering, not an original facsimile.
* H010 archive material under
  `01_sources/heim_primary_unpacked_untrusted/massformula/`: Pascal
  `Pascal 0.62/GPROG 0.62c.PAS`, C `C 0.66/gprog_0.66.c`, and saved
  `C 0.66/output_plus_neutrino.txt`.  This is extracted, later
  implementation material, not primary evidence for an original program.
* Project N=0 input/result records:
  `05_analysis/n0_electron_results.json` and
  `06_docs/N0_ELECTRON_2026-09-06.md`.

The exact H010 source hashes were already recorded in
`N0_OCCUPATION_SOURCE_REVIEW_2026-09-06.md`: Pascal 0.62c
`1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C`,
and C 0.66
`29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0`.

## Three different constant profiles

The following table reports source literals or live assignments, not a claim
that one profile is more physically appropriate.  “Math” means evaluation by
the language/library expression, not the displayed finite decimal.

| quantity | H006 conditional N=0 input profile | Pascal 0.62c live assignment | C 0.66 live assignment | saved C output header |
|---|---|---|---|---|
| hbar / `hq` (J s) | `1.0545887e-34` | `1.054571596e-34` after the earlier `(Sch)` assignment | `1.054571596e-34` | `1.05457159600000e-34` |
| c (m/s) | `2.99792458e8` | `2.99792458e8` | `299792458.0` | `2.99792458000000e+08` |
| gamma (m^3 kg^-1 s^-2) | `6.6732e-11` | final assignment `6.6733198e-11` | `6.6733198e-11` | `6.67331980000000e-11` |
| pi | Math in default profile; separate sensitivity profile uses `3.1415926535` | `4*arctan(1)` | `M_PI` | `3.14159265358979...` |
| e / `ebn` | Math in default profile; separate sensitivity profile uses `2.71828183` | `exp(1)` | `M_E` | `2.71828182845905...` |
| xi | default `1.61803399`; separate sensitivity uses the golden-ratio expression | `(1+sqrt(5))/2` | `(1+sqrt(5))/2` | `1.61803398874989...` |
| alpha | explicit project `1982_source_literal` branch; no H010 value is imported | `1/137.03599976` | `1/137.03599976` | reciprocal `137.03599976` |
| beta | computed only by the declared H006 branch; no H010 value is imported | `1/1.00001411` | `1/1.00001411` | reciprocal `1.00001411` |
| kg -> MeV | none: current conditional N=0 records are in kg | `5.6095892e29` | `5.6095892e29` | `5.6095892e29 MeV/kg` |

The first column is specifically the machine-readable N=0 record:
`dimensional_constants_profile = model_1982_igw2003_printed`, with
`hbar=1.0545887e-34`, `c=2.99792458e8`, `gamma=6.6732e-11`, and `s0=1`.
Its main pure-number profile is explicitly “mathematical pi/e, printed xi”; a
second profile makes xi algebraic, and a third tests all three printed
numerals.  The record has `comparison_or_fit_inputs: []` and
`target_fitting: false`.  Thus the H006 evaluation is not silently using the
H010 CODATA-labelled `hq`, alpha, gamma, or MeV conversion.

H006 prints finite values for pi (`3.1415926535`), e (`2.71828183`) and xi
(`1.61803399`) on its constants page.  Treating the mathematical pi/e runs
and the all-printed-numeral run as separate reconstruction choices is
therefore traceable.  It must not be relabelled as the H010 program profile.

## What is active in the H010 files

`GPROG 0.62c.PAS` lines 141--179 state that the last of multiple assignments
is active.  Consequently its live Pascal values are mathematical pi/e,
CODATA-'98-labelled `hq=1.054571596e-34`, final
`gam=6.6733198e-11` (commented “theory W.Droescher(2002)”),
`Rg=376.730313461`, and `fakMeV=0.056095892e31`.
`GInit` lines 197--215 then assigns golden-ratio xi,
`alfa=1/137.03599976` (commented CODATA 1998), and
`beta=1/1.00001411`.

The C file makes the distinction still sharper: its Pascal-looking sequence
is inside `#if 0` (lines 532--580), hence is **not C execution input**.  The
active `#if 1` block uses `M_PI`, `M_E`, C `double`,
`hq=1.054571596e-34`, `gam=6.6733198e-11`, `rg=376.730313461`,
`c=299792458.0`, `s0=1`, and `fakMeV=0.056095892e31` (lines 584--595).
`GInit` lines 606--625 supplies golden xi, alpha and beta as in the table.

In both, the source retains values labelled `(Sch)` in preceding assignments
(`pi=3.1415926535`, `hq=1.0545887e-34`, `gam=6.6732e-11`, and the older MeV
factor).  The labels are self-descriptions in a later transcription; because
each is overwritten in the live block, they are neither actual default input
to these files nor independent proof of the original 1982 FORTRAN constants.
The same precaution applies to the Pascal prose assertion about `REAL*16` and
to the commented list “values B. Heim used in the 1980s”: no original FORTRAN
source is packaged for verification.

## Saved output: useful audit artefact, not a version certificate

The saved `output_plus_neutrino.txt` prints exactly the C/Pascal later
constant set tabulated above, including the MeV conversion, and it contains a
local e-, N=0 calculation line with `0.510998846703200` MeV.  It also prints a
source-table reference `0.51099892` and a percent-difference line.  Those are
implementation comparator fields, not inputs to the current H006 record and
not evidence about a modern empirical value.

Its banner, however, says “C version 0.62”, whereas the extant source
`gprog_0.66.c` would print “C version 0.66” (lines 1126--1129).  The source
also permits command-line overrides after initialization, while the saved
text does not preserve an invocation.  The matching constants support only a
limited statement: the output is compatible with the later default profile.
They do **not** establish that the displayed result was executed from the
present C 0.66 file, from an unmodified source, or from the claimed 1982
program.

There is a further provenance discontinuity.  The Pascal header self-reports
a 17-03-1982 Schulz program, a 1978 Heim-formula date, 2001 MS-Fortran
transcription, and 2006 Pascal transcription (lines 3--7); its output banner
instead carries “H.D. Schulz, 26/07/82 DESY” (lines 632--635).  These are
retained as file claims, not reconciled into a single verified historical
version.

## Permissible separated reconstruction profiles

Two profiles can be maintained without mixing their provenance:

1. **H006 conditional reconstruction.**  Freeze the H006 dimensional
   constants, `s0`, pure-number policy, alpha-branch convention and unit
   (currently kg) together.  Label it as an editorial H006-based conditional
   reconstruction, including its stated XIV exclusion; it is not a replay of
   H010 or an original-1982 executable.
2. **H010 later implementation comparison.**  If needed, freeze the active
   C 0.66/Pascal defaults, compiler/library behavior, MeV conversion and any
   supplied run parameters as a distinct comparison profile.  It must be
   called a static/later implementation profile.  A saved header alone cannot
   certify the exact executable or command-line overrides.

Crossing the profiles (for example H006 `hq` and gamma with H010 alpha,
`fakMeV`, or reference table) creates an undocumented hybrid.  Choosing a
profile because it improves agreement with a known particle mass would be a
fit, not a provenance-preserving reconstruction.

## Bottom line

The current e-, N=0 H006 result file records a deliberately separate,
non-fitted constant profile.  The static H010 Pascal/C files and their saved
output use a later, internally different profile with CODATA-labelled values,
golden xi, hard-coded alpha/beta, and a MeV conversion.  Their historical
comments and banners are worth preserving as claims, but the archive lacks
the original 1982 FORTRAN source needed to prove a direct implementation or
constant lineage.

## Follow-up: the two specific alpha3 differences, and no rationale found

**Question corrected.**  This follow-up concerns only the two alpha3 changes
identified in the H006/H010 formula comparison, not `q3*alf3`, `sqrt(alf3)`,
or any other occurrence of alpha3:

```text
H006 first correction: [(1+sqrt(eta_qk))*(xi/eta_qk^2)]^(2k+1)
H010 first correction:  (1+sqrt(eta_qk))*(xi/eta_qk^2)^(2k+1)

H006 second correction: (2 sqrt-glyph xi eta_qk)^k
H010 second correction: (2*xi*eta_qk)^k.
```

The H006 scan securely shows the root glyph but not a sufficiently bounded
vinculum.  Its existing profile therefore freezes `sqrt(xi*eta_qk)`, while
`sqrt(xi)*eta_qk` remains a separately documented reading sensitivity.  That
internal H006 ambiguity does not affect the narrow comparison: the H010
Pascal/C text has no root operator anywhere in the corresponding factor.

### Literal implementation evidence

Pascal 0.62c lines 382--385 and C 0.66 lines 806--810 make both H010
choices unambiguous.  In their first correction, `po`/`pow` takes only
`xi/(zw1*zw1)` as its base; `(1+sqrt(zw1))` occurs outside it.  In their
second correction, the base is `2*xi*zw1`, with no `sqrt`.  Those lines are
evidence only for a later implementation spelling; they do not explain why
the two changes were made.

The only nearby C comment says after `an3=2*alf3` that `N3(2,2)=2.007.. !=
table` and asks whether a selected-results value is wrong (lines 809--810).
It offers no derivation of either the exponent's scope or the rootless second
factor.  Pascal has no corresponding explanatory comment.

### What the ancillary files do and do not say

Both H010 readmes list later corrections to different expressions: missing
brackets in `a[2,2]` and at the end of `wg2`, plus a wrong closing bracket in
`aq`.  They never name alpha3/`alf3`, the `(1+sqrt(eta_qk))` power scope, or
the factor `(2 sqrt-glyph xi eta_qk)^k`.  The general speculation that too few
digits in a historic programming language could affect some values is not a
formula-level rationale.

The two comparison-output files list numerical `N3`, `K3`, and resonance
differences, but contain no symbolic derivation or statement selecting either
of these two alpha3 conventions.  The saved C output contains only numerical
run material and its version-mismatched banner; it adds no explanation.

### Bounded conclusion

Within the inspected H010 text sources, **no explicit reason for either
specific alpha3 alteration was found**.  H010 supports only the limited
provenance statement that its later Pascal/C implementations use the two
literal expressions above.  It does not establish that the H006 power
bracket was intentionally changed, that the H006 root was deliberately
dropped, or that either H010 spelling is an author-authorized emendation.
The self-reported dates and claimed historical chain remain insufficient to
improve this conclusion or prove a connection to an original FORTRAN source.
