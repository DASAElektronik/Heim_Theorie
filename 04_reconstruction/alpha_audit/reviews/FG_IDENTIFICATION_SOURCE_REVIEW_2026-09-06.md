# Source review: the `F_1,F_2,G_1,G_2` identification before Eq. (98a) — 2026-09-06

## Scope and result

This is a bounded source review of the four symbols introduced on printed
p. 269 of Burkhard Heim, *Elementarstrukturen der Materie II* (1996), and of
their targeted antecedents in Eqs. (58)/(58a). It asks what the book actually
defines, which signs and order it prints, and whether the tensor/trace context
closes the later identification with `V_1,V_2,Q_1,Q_2`. It does not review the
separate derivation of the exponential approximation, calculate an alpha fit,
or import a later formula version.

The principal result is negative but precise: **the checked antecedent defines
the selector and tensor machinery, but not four separately characterized
scalars `F_1,F_2,G_1,G_2`.** Printed p. 269 first introduces those labels as
the four “`sp K;()` bestimmenden Summanden” in an approximate trace expression.
The immediately following identification with the four potential ratios is
expressly speculative. Nothing in (58)/(58a) supplies an index reversal or a
sign convention that repairs the next line.

There is an exact local sign break:

```text
printed premise:        F2 - F1 + G2 - G1 > 0
printed identification: F1=V1, F2=V2, G1=Q1, G2=Q2
ordinary substitution: V2 + Q2 > V1 + Q1
next printed line:      V1 + Q1 > V2 + Q2
```

Equivalently, for the project's diagnostic
`R_VQ = V1+Q1-V2-Q2`, the first two source lines imply `R_VQ<0`, whereas the
next printed line asserts `R_VQ>0`. This is a source-internal ordering/sign
conflict, not a proposed correction.

## Source and inspection locations

Primary book source:

`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`

The targeted visual inspection covered:

- printed pp. 97–111 / PDF folios 104–118: construction of the
  synmetronic fundamental problem, (58), (58a), and the later indexed field
  quantity `F^i_(kl)`;
- printed p. 261 / PDF folio 267: the distinct earlier `G_j` zone-count
  notation;
- printed pp. 267–269 / PDF folios 273–275: phenomenological potentials,
  `V_i,Q_i`, application of (58)/(58a), and the `F_i,G_i` identification.

The title/edition provenance is the primary 1996 Book-II edition already used
in the alpha audit. No 1982 or 1989 equation was treated as part of this book's
local derivation.

## 1. What (58) and (58a) define

### Structural and correlation operators, not four scalar contributions

Printed p. 97 / PDF folio 104 begins “Das synmetronische
Fundamentalproblem”. It splits the compositive world selector using a
polymetric structural condenser `K`. It describes the correlation term as a
tensor built quadratically from correlation tensors and synmetronic
fundamental condensers, and represents that term by the action of a quadratic
correlation selector `D` on a fundamental condenser of the same signature.

Printed p. 98 / PDF folio 105 writes the components of `D` as a long alternating
sum of Kronecker/exchange and coupling-tensor terms. It also introduces a
function selector of the schematic form

```text
Lambda = K ; (1 + sp^2 Q x ()) + D.
```

Here `Q` is a coupling tensor and `sp` is used in the matrix-trace machinery.
The page then relates the selector spectrum to an energy-density tensor only
after a macroscopic transition containing an additional constant scale and an
`R_3` integration. It does not define four scalar energy contributions.

Printed p. 99 / PDF folio 106 defines the synmetronic world selector
schematically as

```text
L = Lambda - lambda_bar x (1 + sp^2 Q x ())
```

and gives the selector equation as Eq. (58). Printed p. 100 / PDF folio 107
collects `L`, `Lambda`, `K`, `D`, the Kronecker product and exchange operator
as Eq. (58a). Thus the source does establish a definite operator-level
subtraction: the `lambda_bar` term is subtracted in `L`, while `D` enters
`Lambda` additively. When the equation is rearranged for the later
application, `D` correspondingly appears with a minus sign on the opposite
side.

This operator algebra does **not** label any of its many positive and negative
component terms as `F_1,F_2,G_1,G_2`, nor does it assign four scalar endpoints
or magnitudes to them.

### The later capital `F` in the solution is a different object

Printed p. 108 / PDF folio 115 introduces an underlined/barred `F` expressly
as a “Fremdfeldselektor” for a field quantity and then uses indexed components
`F^i_(kl)`. Printed pp. 109–111 / PDF folios 116–118 derive differential and
integrated relations for these indexed field components and their integration
constants.

The checked text gives no statement that the unadorned scalar labels
`F_1,F_2` on p. 269 are components, endpoints, traces, norms, or boundary
values of this earlier `F^i_(kl)`. The shared letter alone is not a source
bridge.

## 2. Immediate construction on pp. 267–269

### The `V_i,Q_i` side is defined as ratios

Printed p. 267 / PDF folio 273 introduces the static internal law

```math
4\pi\epsilon_0 V_{xy}=e_xe_y f(r)
```

as a phenomenological description of static charge-field components. Printed
p. 268 / PDF folio 274 then defines:

- `V_1` as the ratio of external to internal interaction energy/potential,
  yielding `V_1=eta_q eta_qk^(-1)`;
- `V_2` as another potential ratio;
- `Q_1,Q_2` as distinct products of potential ratios. Their underlining is
  material and is not flattened here into apparently identical plaintext
  products.

The page gives the usable reduced relations

```math
\eta_{qk}V_1=\eta_q,
\qquad
4\eta V_2=(1+\sqrt{\eta_q})^2,
```

```math
Q_1\sqrt{\eta}=\eta_q^2,
\qquad
Q_2=\sqrt{\eta}.
```

All four are therefore dimensionless ratios or products of ratios in this
local construction.

### Application of (58)/(58a)

Still on p. 268, the observable charge-field C-structure is represented by a
sum of fundamental condensers with a displayed signature. A corresponding
coupling tensor is introduced and the signature is written schematically as

```text
S = (1 + sp^2 Q x ()) ; S_base.
```

The page then says that (58) with (58a) can be applied in the rearranged form

```text
lambda_bar x S - D ; S_base = K ; S_base.
```

This is a genuine source bridge from the general operator equations to the
specific charge-field C-structure. It fixes which operator term has been moved
with a minus sign. It still does not decompose the trace into named `F_i,G_i`.

### First and only direct local role of `F_i,G_i`

Printed p. 269 / PDF folio 275 applies the third-validity-region spatial limit
and repeats the exponential falloff. It then says, in conditional language,
that because of this exponential course one *could approximately assume* for
the terms determining the trace of `K`:

```text
sp K ; S ; n  ->  F2 - F1 + G2 - G1,
```

provided, because of the energetic nature of the condensation stages,

```text
F2 - F1 + G2 - G1 > 0.
```

This passage gives the following and no more:

- the four symbols are summands in an approximate scalar trace expression;
- the printed order is `2 minus 1` in both pairs;
- the sum is required to be positive;
- no formula separately defines `F_1`, `F_2`, `G_1`, or `G_2`;
- no statement identifies pair `F` with one of the two operator groups in
  (58a), pair `G` with another group, or indices `1,2` with radial endpoints.

The next sentence expressly says “Wird **spekulativ** die Identifikation
`F_(1,2)=V_(1,2)` und `G_(1,2)=Q_(1,2)` vorgenommen”. The assignment is
index-preserving as printed. It is not written with crossed indices such as
`F_1=V_2` or with sign flips.

## 3. The sign/order conflict is not resolved by the antecedent

Let

```text
Delta_FG = F2-F1+G2-G1.
```

Under the source's own index-preserving speculative identification,

```text
Delta_FG = V2-V1+Q2-Q1
         = -(V1+Q1-V2-Q2)
         = -R_VQ.
```

Therefore the stated positive-energy condition `Delta_FG>0` implies
`R_VQ<0`. The scan at 500 dpi unambiguously prints the reverse inequality in
the next line:

```text
V1+Q1 > V2+Q2,
```

i.e. `R_VQ>0`.

The targeted antecedents offer no source-authorized repair:

- (58)/(58a) do contain operator-level plus and minus signs, but they do not
  attach the four later scalar labels to those operator terms;
- the p. 269 arrow itself visibly fixes `F2-F1+G2-G1`;
- the speculative assignment visibly preserves indices;
- no intervening definition introduces a negative proportionality factor or
  reverses the meaning of `1` and `2`.

It is therefore appropriate to keep both alternatives explicit in any audit:
the `Delta_FG>0` branch maps to `R_VQ<0`, while the book's next printed
potential inequality is the separate `R_VQ>0` branch. Choosing one as an
erratum would require evidence not present in the checked source chain.

## 4. Notation collisions that do not close the gap

The book reuses the same letters for materially different objects:

| Notation and location | Source-local role | Relation to p. 269 scalar summands |
| --- | --- | --- |
| coupling tensor `Q` in (58)/(58a), pp. 97–100 | Tensor inside the quadratic correlation/trace operator | No component identification with scalar `Q_1,Q_2` is stated. |
| `F^i_(kl)`, pp. 108–111 | Indexed field quantity introduced from a Fremdfeldselektor | No statement makes p. 269 `F_1,F_2` its values or contractions. |
| `G_j`, p. 261 | Protosimplex numbers of the four configuration zones, e.g. formulas for `G_1,G_2` | No cross-reference on p. 269 identifies these zone counts with the four trace summands. |
| `Q_j`, pp. 261 onward | Ground-state/zone occupancies | Distinct context from the underlined-potential products called `Q_1,Q_2` on p. 268. |
| `V_1,V_2,Q_1,Q_2`, p. 268 | Dimensionless ratios/products of potential ratios | These are the objects speculatively assigned to the p. 269 summands. |

The immediate grammar on p. 269 (“die ... bestimmenden Summanden”) favors
reading `F_i,G_i` as local names for trace contributions, not silently as the
earlier field tensor or zone counts. That is a contextual reading, however;
the book supplies no explicit disambiguating definition.

## 5. Scale and dimensional status

The potential-side quantities are source-fixed as dimensionless ratios. The
trace-side quantities are less well specified:

- pp. 97–100 operate with structural condensers, selectors, tensor signatures
  and traces;
- p. 98 relates the selector spectrum to an energy-density tensor only through
  a macroscopic limiting transition containing an additional constant scale
  and an `R_3` integration;
- p. 269 calls the condensation stages energetic, but gives no unit, common
  normalization, proportionality constant, or boundary prescription for the
  individual `F_i,G_i`.

Thus the checked source does not establish a dimensionally normalized equality
between four independently defined trace/energy quantities and four
dimensionless potential ratios. The p. 269 equality is itself the speculative
identification that would supply that bridge; it is not derived earlier. This
is an open normalization question, not enough evidence by itself to declare a
dimensional contradiction, because the book may intend already normalized
trace contributions without stating that normalization here.

## 6. What is positively connected and what remains open

### Positively connected

- (58)/(58a) define the relevant operator equation, coupling tensor, quadratic
  correlation selector and trace framework.
- p. 268 explicitly applies that framework to the charge-field C-structure.
- p. 269 explicitly gives the approximate four-term order and positivity
  premise.
- p. 269 explicitly, but speculatively, maps each index-preserving pair to the
  potential ratios defined on p. 268.
- The exact diagnostic relation under that mapping is
  `Delta_FG=-R_VQ`.

### Open after the bounded search

- No direct definitions of the four scalar summands apart from their combined
  trace role were located in the checked antecedent.
- No source text assigns `F_i` and `G_i` separately to particular terms of the
  multi-term selector `D`, to `lambda_bar`, or to radial boundary values.
- No explicit scale or normalization links them to the dimensionless
  `V_i,Q_i` before the speculative sentence.
- No checked passage reverses indices or signs so as to convert
  `Delta_FG>0` into the next printed `R_VQ>0`.
- The repeated letters `F`, `G`, and `Q` elsewhere in the book are not, without
  an explicit bridge, sufficient to identify the p. 269 scalars.

The narrow next source question would be an authorial erratum, alternate
edition, or manuscript showing how the four trace summands were intended to
be grouped. This review does not infer such a correction from the desired
selection result.

## Search boundary and visual record

The inspection was deliberately limited to the immediate operator antecedent
and nearby same-letter candidates. Targeted full-OCR searches were used only
to locate candidates; all carrying statements and glyphs above were checked
against page images. The search does not prove that no unpublished or remote
definition exists.

Ignored source renders used:

- `tmp/pdfs/fg_identification/b2-p97-112-104.jpg` through
  `b2-p97-112-118.jpg`
- `tmp/pdfs/config_dependency/b2-p261-270-267.jpg`
- `tmp/pdfs/config_dependency/b2-p261-270-273.jpg` through `-275.jpg`
- `tmp/pdfs/fg_identification/b2-p268-hires-274.png`
- `tmp/pdfs/fg_identification/b2-p269-hires-275.png`

No source, canonical formula, implementation, other review, or commit was
changed.
