# Configuration dependency review: selection of `q` and `k` — 2026-09-06

## Scope and result

This is a bounded source review of the configuration choices feeding the
fine-structure equation in *Elementarstrukturen der Materie II*, especially
Eq. (98a) and its later use in Eq. (105). It is not a reconstruction of the
full mass model, an alpha fit, or a test of physical validity.

The Book-II chain can be connected internally, but its links do not all have
the same status:

1. Book I explicitly defines `q >= 0` as an integer electric charge quantum
   number and writes `Q_± = q epsilon_±`.
2. Book II introduces `k > 0` as an integer configuration number. It initially
   considers `k=1,2` because it wants to infer two stable scaffold structures
   from the empirical electron and proton.
3. The upper limits `k_max=2, q_max=3` in (98a) follow only if an immediately
   preceding, expressly “mehr spekulative” potential identification is
   accepted. They are conditional upper bounds, not an existence proof for
   every pair and not the later selection of `q=1` for the hydrogen atom.
4. The later electron/proton assignment is explicit but heuristic:
   `(k,q)=(1,1)` is assigned to the electron and `(2,1)` to the proton. The
   Eq. (105) factors `A_1,A_2` consequently use `eta_(1,1),eta_(1,2)` in the
   book's own `(q,k)` index order.
5. The editor-produced 1982 reproduction contains a positive semantic bridge
   (`k=1` mesons including the electron multiplet; `k=2` baryons including the
   proton multiplet; `q=|q_x|`) but not a license to merge formula versions.
   In particular, it prints `eta_kq` on p. 3 and `eta_qk` on p. 5 without an
   explicit correction. That source-local index collision remains open.

## Sources and provenance

| Short name | Local source | Provenance used here |
| --- | --- | --- |
| Book I | `01_sources/heim_primary/Burkhard Heim - 1998 - Elementarstrukuren der Materie 1.pdf` | Burkhard Heim, *Elementarstrukturen der Materie*, Band I, 3., veränderte Auflage (1998); primary book edition. |
| Book II | `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf` | Burkhard Heim, *Elementarstrukturen der Materie*, Band II (1996); primary book edition. |
| 1982/IGW reproduction | `01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf` | Near-primary editor reproduction, not treated as a facsimile manuscript. Its cover says “Wiedergabe der Urschrift von Burkhard Heim”, Forschungskreis Heimsche Theorie, IGW Innsbruck, 2002; the running header says © IGW Innsbruck 2003; p. 2 attributes the enclosed text “Zur Beschreibung der Elementarkorpuskeln (Ausgewählte Ergebnisse)” to Burkhard Heim and dates it 25.2.1982. PDF metadata identifies a Word/PDFWriter production in 2003. |
| 1989/IGW reproduction | `01_sources/heim_primary/Erweiterte_Massenformel_Nach_Heim_1989.pdf` | Near-primary editor reproduction, not a facsimile. Its cover says *Die erweiterte Massenformel nach Burkhard Heim (1989)*, “Nach einem Manuskript von Burkhard Heim”, Forschungskreis Heimsche Theorie, IGW Innsbruck, 2002; its running header is © IGW Innsbruck 2003 and the PDF metadata identifies a 2003 Word/PDFWriter production. Only the narrow `eta`/B58–B62 bridge is used below. |

The existing 1982 QNUM catalog was checked against the source images, but the
source images, not that catalog, are the evidence for the findings below.
Colored parenthetical comments visible in the IGW layouts were not used as
Heim source statements.

## Dependency map

```text
Book I p.244: q is a non-negative integer; Q_± = q epsilon_±
       |
       +--> q=0: neutral / eta_q=1
       |
       +--> q>=1: charged case
                    |
Book II pp.262-264: integer k>0 -> configuration number;
                    e-/p empiricism motivates considering k=1,2
                    |
Book II pp.266-267: eta_(q,k), first index q and second index k
                    |
Book II pp.268-269: conditional potential argument
                    -> if accepted: k_max=2, q_max=3  (98a)
                    |
Book II pp.295-296: heuristic ground-pattern assignment
                    e- = (k,q)=(1,1), p = (2,1)
                    |
Book II pp.299-302: H-system uses eta_11, eta_12 and A_1,A_2
                    -> Eq. (105)
```

The map is a dependency/status map. It does not say that the empirical
electron/proton input is independently derived by the same chain.

## 1. Where the book's `q` values and integer assumption come from

### Explicit Book-I definition

Book I, printed p. 244 / PDF folio 250, first introduces an integer `p >= 0`
in the extremum argument, selects `N=2p+1` for the absolutely minimal charge
field, and denotes that elementary field by `epsilon_±`. The decisive later
sentence is explicit: with the integers `q >= 0`, the existence of the
elementary charge field gives the quantization

```math
Q_\pm = q\,\epsilon_\pm.
```

The same page defines

```math
\eta_q^4 = \left(1+\frac{4q^4}{\pi^4}\right)^{-1}
```

and calls `q` the electric charge quantum number. Printed p. 245 / PDF folio
251 then summarizes the one-index factor in Eq. (27),

```math
m(n,q)=m(n)\eta_q,
\qquad
\eta_q\sqrt[4]{4q^4+\pi^4}=\pi.
```

Thus the integer domain is source-explicit in the book. It is not inferred
retrospectively from the later numerical trials `q=1,2,3,4`.

### Book-II bridge

Book II, printed p. 258 / PDF folio 264, calls `q` the “elektrische
Ladungsquantenzahl ... des elementaren elektrischen Ladungsfeldes (29)”. On
printed p. 266 / PDF folio 272 it defines

```math
\eta_{qk}\sqrt[4]{\pi^4+q^4(4+k)}=\pi
```

and explicitly gives `eta_(q,0)=eta_q`, while `k=0` is only a formal marker for
the exterior `R_3` action domain. This is the book's direct bridge from the
one-index charge family to the two-index internal family. Printed p. 268 / PDF
folio 274 adds that `k` can appear in `eta_qk` only for `q>=1`.

Consequently:

- `q=0` is the neutral edge case (`eta_(0,k)=1`) and carries no `k`
  dependence in this factor; separately, `k=0` is the book's formal marker
  for the external field;
- the charged internal selection argument starts at the already integer
  values `q=1,2,...`;
- `(98a)` supplies only an upper bound `q_max=3` under its stated condition.
  It does not assert that all `q=1,2,3` states exist.

## 2. Where `k=1,2` comes from

Book II, printed pp. 260–263 / PDF folios 266–269, builds `k` through a
metric/configuration argument. It first treats the relevant counts as whole
numbers, then obtains `kappa=k^2`, `Z_k=2^(k^2)`, and calls `k>0` a
“Kondensorziffer” and “Konfigurationszahl”. The source says it is time
independent in the stated construction.

The first appearance of `1` and `2` is not yet a derived electron/proton label.
On printed p. 263 / PDF folio 269 the source states that empirically two stable
elementary scaffold structures, electron and proton, are known. Since `k>=1`,
it says that besides `k=1`, `k=2` would also be conceivable, and that one may
therefore *try* to infer the zone occupancies from the empiricism of electron
and proton. Printed p. 264 / PDF folio 270 then performs that inductive
occupancy construction. The status is therefore empirical/inductive at this
bridge, not a particle identification proved solely from `kappa=k^2`.

### Conditional restriction in (98a)

On printed pp. 268–269 / PDF folios 274–275, the book constructs potential
ratios and identifies `F_(1,2)=V_(1,2)` and `G_(1,2)=Q_(1,2)` expressly
“spekulativ”. A high-resolution glyph check of the last formula line on
printed p. 268 gives, word for word at the relevant endpoint,

```math
\eta_{qk}V_1=\eta_q,
\quad
4\eta V_2=(1+\sqrt{\eta_q})^2,
\quad
Q_1\sqrt{\eta}=\eta_q^2,
\quad
Q_2=\sqrt{\eta}.
```

The final `Q_2` radicand is plain `eta`, **without** a subscript `q`; the
nearby `sqrt(eta_q)` and `eta_q^2` visibly carry the subscript.

The next page obtains `k<u_q` and numerically **reports** `2<u_q<3` for
`q=1,2`, `1<u_3<2`, `0<u_4<1`, and `u_q<0` for `q>4`. Only then does the
source say:
if this “mehr spekulative Betrachtung” is correct, only `k=1,2` for `q=1`
through `q=3` would be compatible, hence

```math
k_{\max}=2,\qquad q_{\max}=3. \tag{98a}
```

This is a positive source bridge from the preceding inequality to (98a), but
the source itself makes the bridge conditional. Also, an upper bound is not a
selection rule for the hydrogen pair; in particular `q_max=3` does not explain
by itself why Eq. (105) later uses `q=1`.

There is also a narrower arithmetic qualification. Direct evaluation of the
printed `u_q` expression with the printed `eta` definitions gives, to the
shown precision,

```text
u_1 = 2.0637990310
u_2 = 1.9634891981
u_3 = 1.2396666578
u_4 = 0.1007579288
```

Thus the source's `2<u_q<3` statement is reproduced for `q=1` but **not** for
`q=2`; the literal result is `1<u_2<2`. With strict `k<u_q`, the allowed
positive-integer pairs through `q=3` would be `(q,k)=(1,1),(1,2),(2,1),(3,1)`,
not the full rectangle `q=1..3`, `k=1,2`. The separately printed global maxima
`k_max=2` and `q_max=3` still follow from that set, so this is a local
selection-table discrepancy rather than, by itself, a refutation of both
maximum labels. No alpha fit was used in this check.

## 3. Electron/proton assignment and later use in Eq. (105)

Printed p. 295 / PDF folio 301 says that, according to the empirical
interpretation, the stable ground patterns are charged `d` forms with `q=1`.
Printed p. 296 / PDF folio 302 evaluates the coefficients for `(k,q)=(1,1)`
and `(2,1)`. Because the term `F_S` remains unknown, the source says the two
resulting ground masses *must be set approximately* equal to electron and
proton mass and explicitly notes the heuristic determination of the zone
occupancies and coefficients. It then identifies the electron ground pattern
with `k=1` and the proton ground pattern with `k=2`.

This supports the following exact dependency used later:

| Particle in the Book-II hydrogen construction | Charge magnitude | Configuration | Two-index factor |
| --- | ---: | ---: | --- |
| electron `e^-` | `q=1` | `k=1` | `eta_(1,1)` |
| proton `p` | `q=1` | `k=2` | `eta_(1,2)` |

Printed p. 299 / PDF folio 305 explicitly speaks of the internal structures
expressed by `eta_11` or `eta_12` for the `q=1` charged `d` terms in the
attractive electromagnetic `(e^-,p)` correspondence. It also defines `A_k`
for `k=1` or `2`. Printed p. 302 / PDF folio 308 then uses

```math
(1+\sqrt{\eta_{1k}})A_k
=(1-\sqrt{\eta_{1k}})\sqrt{\eta_{1k}}
```

inside Eq. (105). Since Book II has already fixed the index order as `(q,k)`,
the product `A_1A_2` is source-connected to `eta_(1,1)` and `eta_(1,2)`.

The logical status should remain visible: the book has an internally explicit
notation/use chain, while the identification of its two configurations with
electron and proton was introduced using empirical and heuristic input.

## 4. What the 1982 QNUM reproduction adds — and what it does not

The 1982/IGW reproduction supplies several positive, source-local bridges:

- p. 2 defines `k` as a configuration number and metric index, says `k=0`
  means no ponderable particle/rest mass, and states that for ponderable
  corpuscles only `k=1,2`, not `k>2`, are possible;
- p. 2 defines signed `q_x` as the electric charge quantum number of a
  multiplet component and `q=|q_x|`;
- pp. 2–3 give a discrete formula for `q_x` in terms of the source's QNUM
  labels and then list possible configurations `k=1,2`;
- p. 3 assigns mesons to `k=1` and baryons to `k=2`; its displayed
  `k=1` multiplet `x_2` contains `(e_0,e^-)`, while the displayed `k=2`
  multiplet `x_8` contains `(p,n)`.

The `C` in this QNUM block is itself defined there as a structure distributor,
identified with strangeness. It is not identified by this source as the
correlation constant denoted `C` in other alpha-closure discussions.

These statements are compatible with the Book-II semantic assignment. The
short reproduction, however, does not rederive its unconditional sentence
“only k=1 and k=2 possible” from the Book-II conditional argument in (98a),
and it does not repeat Book I's explicit prose that `q` ranges over all
non-negative integers. Its `q` values arise as magnitudes of the displayed
signed component-charge rule. Therefore the book's derivation and the 1982
summary should remain separately versioned even where they agree.

### Material index-order boundary

The 1982 reproduction prints on p. 3, Eq. (V),

```math
\eta_{kq}=\frac{\pi}{[\pi^4+(4+k)q^4]^{1/4}},
```

then defines `A_1` with `eta_11` and `A_2` with `eta_12`. Read literally in
that printed subscript order, `eta_12` means `(k,q)=(1,2)`, not the Book-II
proton factor `(q,k)=(1,2)`. The same reproduction switches on p. 5, Eq. (IX),
to the glyph order `eta_qk` for the same right-hand expression, without an
erratum or semantic explanation. The book's convention is unambiguous within
the book, but it cannot silently repair the 1982 p. 3 glyph.

Accordingly, the existing catalog
`04_reconstruction/formula_library/formulas/HT-F-1982-QNUM.md` is consistent
with this review when it:

- preserves `q=|q_x|` and the two visible `Q(P)` rows without inventing a
  binding;
- treats its transcription as 1982 source-local;
- warns that 1989 changes the `C` and `q_x` formulas rather than importing
  those changes into the 1982 block.

The 1982 alpha block and its eta-index ambiguity are a distinct issue from the
QNUM transcription. Neither a numerical alpha target nor the later Book-II
notation may be used to decide silently what the 1982 p. 3 editor intended.

## 5. Bounded 1989 bridge: `eta_(2,2)` is really printed

The separate 1989/IGW reproduction introduces another version edge that is
material to configuration dependencies:

- printed p. 12 / PDF folio 3 says that the constants `eta_(q,k)`, `vartheta`
  and `eta` (including `eta_(1,0)=eta`) “lauten wie in (IX)”. This is an
  explicit internal reference to the 1982 reproduction's Eq. (IX)-style
  `(q,k)` spelling, not a reference on that page to Book-II Eq. (98a).
- printed p. 18 / PDF folio 9, Eq. (B59), visibly contains `eta_(2,2)` in the
  numerator of the factor defining `1-C'=K_alpha`; the same expression also
  contains `eta_(1,1)` and `eta_(1,2)` in its denominator. B58 uses `C'` in
  the revised fine-structure equation, and B62 gives the two numerical
  branches.

This verifies that `eta_(2,2)` is not merely an implementation invention: it
is a literal 1989 source dependency. It does **not** establish that the source
is asserting the existence of a real particle configuration `(q,k)=(2,2)`.
It may be using the analytic eta family at that argument as an algebraic
correction factor. Nor may Book-II (98a) be automatically imposed on this
separately edited 1989 formula version.

The tension should nevertheless be retained as a next source question. If one
did apply the literal Book-II inequality unchanged, the recalculated
`u_2=1.963489...` would exclude integer `k=2`; the 1989 B59 formula still uses
`eta_(2,2)`. The inspected 1989 pp. 12 and 18 do not say whether this is an
analytic off-configuration evaluation, a revised selection convention, or an
unexplained inheritance. No one of those explanations is chosen here.

## 6. Connected facts, open links, and non-claims

### Source-connected

- Book I explicitly supplies the integer domain `q>=0` and the elementary
  charge-multiple meaning of `q`.
- Book II explicitly connects the one-index `eta_q` family to `eta_(q,k)` and
  fixes first index `q`, second index `k`.
- Book II explicitly connects charged `q=1`, `k=1/2` structures to the
  electron/proton hydrogen construction and then to `A_1,A_2` in (105).
- The 1982 reproduction independently preserves a compatible semantic map:
  `q=|q_x|`, electron multiplet under `k=1`, proton multiplet under `k=2`.
- The 1989 reproduction literally uses `eta_(2,2)` in B59 and separately
  points its `(q,k)` constants back to Eq. (IX).

### Still conditional or open

- `(98a)` depends on the source's own speculative potential identification.
  The review found no independent selection proof in the bounded pages that
  removes that condition, and its printed interval for `u_2` is not reproduced
  by direct evaluation of its formula.
- The step from “two empirically stable scaffold structures” to the candidate
  values `k=1,2`, and the later mass-based particle assignment, is explicitly
  inductive/heuristic in the book.
- `q_max=3` is an allowed upper limit under the condition, not evidence that
  all three nonzero charge magnitudes occur as physical ground patterns.
- The 1982 p. 3 `eta_kq` versus p. 5 `eta_qk` collision is unresolved at the
  source level. No particle assignment or target fit is used here to correct
  it.
- The 1982 source's unconditional summary `k<=2` and Book II's conditional
  derivation are compatible outcomes but not demonstrated here to be identical
  derivations or editions of one formula block.
- The physical/configurational status of the 1989 B59 factor `eta_(2,2)` is
  not stated on the inspected pages and must not be inferred from its mere
  algebraic occurrence.

## Inspection boundary and render record

The targeted inspection covered Book I printed pp. 244–245 (PDF folios
250–251); Book II printed pp. 257–270 and 293–302 (PDF folios 263–276 and
299–308); the 1982/IGW reproduction pp. 1–5; and only printed pp. 10, 12 and 18
of the 1989/IGW reproduction (PDF folios 1, 3 and 9). It did not inspect the
full mass-spectrum catalog, prove that no other discussion exists elsewhere in
the books, or consult modern refutation literature.

Visual checks used these ignored project renders:

- `tmp/pdfs/config_dependency/b1-p244-245-250.jpg` and `-251.jpg`
- `tmp/pdfs/config_dependency/b2-p257-260-263.jpg` through `-266.jpg`
- `tmp/pdfs/config_dependency/b2-p261-270-267.jpg` through `-276.jpg`
- `tmp/pdfs/config_dependency/b2-p293-297-299.jpg` through `-303.jpg`
- `tmp/pdfs/correlation_closure/b2-p298-302-305.jpg` through `-308.jpg`
- `tmp/pdfs/configuration_selection/p268-root-274.png` for the independent
  high-resolution `Q_2=sqrt(eta)` glyph check
- `07_outputs/source_check_images/1982_massenformel/page-01.png` through
  `page-05.png`
- `tmp/pdfs/eta_configuration/igw89-03.png`
- `tmp/pdfs/config_dependency/igw1989-front-01.png` and
  `igw1989-p18-pdf9-09.png`

No canonical formula, implementation, source PDF, or catalog was changed.
