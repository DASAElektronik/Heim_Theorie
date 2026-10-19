# H015 archive check: W4/K4 cases and integer rule (2026-09-06)

## Scope and visual anchors

Read visually in the photographed H015 archive scan:

- `tmp/pdfs/alpha3_origin/desy-42.png`: PDF 42, visible upper sheet marker
  `- 6 -` (the lower `- 7 -` is a continuation marker, not used as the sheet
  identity);
- `tmp/pdfs/alpha3_origin/desy-43.png`: PDF 43, visible upper marker `- 7 -`,
  read only for its immediate continuation/structural context.

H015 is `01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`,
SHA-256 `C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.
For an edition-separated comparison only, H006 print/PDF 9 was reread at
`tmp/pdfs/n0_alias/h006-09.png` (H006 hash in the existing source note).
H015 has no H006 Roman equation labels. No numerical mass or source-text
substitution is made here.

## What H015 sheet 6 visibly contains

The sheet gives the staged determination from a designated right side `W1`:
maximal cubic `K1`, then quadratic `K2`, then linear `K3`, leaving a
non-negative rest `W4`. The residual equations carry the already established
grouped exponential form, i.e. the factor `(1-2k)/(3Q4)` multiplied by the
fourth-zone bracket. This is the archive's own typography; it does not make
the H006 `(XIV)` line disappear.

It then explicitly states three W4 cases:

| visible case on H015 Blatt 6 | accompanying text / consequence |
| --- | --- |
| (a) `W4=0` | The limiting `W4 -> 0` would make `K4` diverge. The text rejects this using the stated bound `K4 <= alpha3*K3` and its no-divergent-self-potentials premise, then directs determination of maximal `K4=alpha3*K3`. |
| (b) `0<W4<=1` | Called the general case; it gives `ln W4<=0` and `K4(2k-1)=-3Q4 ln W4`. |
| (c) `W4>1` | It says `ln W4>0` and the resulting `K4<0` is impossible because `n_j+Q_j` must remain non-negative. It describes reducing `K3` by one and adding `alpha3*K3` to the negative K4 to obtain a new `K4>=0`; this explicitly requires `K3>0`. With `K3=0`, the described dilation cannot occur and the resonance ordering is said not to exist (a forbidden term). |

The archive does **not** visibly introduce separately named pre- and
post-correction variables for `K3`, `K4`, or `W4`. The phrases describe an
operation on them, but the exact bookkeeping/order is not written as a new
equation on this sheet. That is an open operational detail, not a license to
choose an update convention.

Immediately afterwards H015 prints `n_j=K_j-Q_j`; it allows both signs of
`n_j`, while retaining `K_j>=0` and hence `n_j>=-Q_j`. It states that the
obtained quadrupel is used with Phi in the mass spectrum, but supplies no
particular component or mass calculation on this page.

## Integer/decimal provision

The **Vermerk** on H015 Blatt 6 explicitly says that the `K_j` are always
integers. It singles out `K4` as regularly producing decimal places. A tail
of the displayed repeating `0.99...` type is to use the identity to one;
if the decimal sequence differs, it must not be rounded and is to be cut
off. The stated reason is that `K_j` count structural entities.

Thus the photographed typescript does contain both the W4 special cases and
the K4 integer/decimal instruction. This is positive evidence that these
rules are not confined to the later H006 re-typesetting. It is not evidence
for an exact historical program, a tolerance magnitude, or an unprinted
rounding rule.

## Sheet 7 and H006 comparison

H015 Blatt 7 continues with the general construction/bounds of the
configuration zones and a grouped exponential in its resonance context. It
also contains a separate no-rounding/cut-decimals instruction for its visible
`L` quantities. That page does not define a new K4 special-case algorithm;
the `L` notation is not silently identified with `K`.

H006 p9 visibly has the same local architecture: staged `W1`--`W4`, cases
(a)--(c), the logarithmic relation in case (b), the K3 reduction prose in
case (c), `n_j=K_j-Q_j`, and the K4 decimal provision. H006 additionally
numbers nearby residual relations `(XXX)` and `(XXXI)` and is a later IGW
rendering. H015's visible date/signature material on Blatt 7 supports only
the scan's document appearance; it does not prove that the two documents are
identical versions, establish their chronology, or authorize replacing an
H006 token with an H015 token.

## Bounded conclusion

For the requested narrow question, the answer is **yes**: H015 Blatt 6
visibly preserves the three W4 cases, the K3/K4 adjustment prose, and the
K4 integer/decimal rule. The special-case machinery therefore has a
photographed-archive counterpart. What remains unexpressed on that sheet is
the exact before/after state convention for the K3-decrement/K4-addition;
any algebraic test must retain that ambiguity and must not turn it into a
new selection or mass rule.
