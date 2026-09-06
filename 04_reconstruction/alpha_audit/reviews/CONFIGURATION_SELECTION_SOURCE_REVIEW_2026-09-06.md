# Configuration selection, `L Delta = k`, and (98a) — 2026-09-06

Scope: bounded, source-led reconstruction of the configuration-number
selection on printed pp. 263–269 of *Elementarstrukturen der Materie II*.
This note records what the local edition prints, distinguishes its stated
assumptions from its algebra, and checks the immediately displayed
substitution.  It neither chooses an `eta` index by a fit nor supplies a
historical correction to the text.

## Result

`L Delta = k > 0` is **not presented as a proved quantization theorem**.
On p. 265 Heim calls `L` the number of dimensions of condensing manifest
events and says that one *could perhaps set* the configurative basic quantum
number to `L Delta = k > 0`.  He then fixes `L=L(R4)=4` because the stated
world-flucton occurs only in the d-hermetry / spacetime condensations, and
uses that tentative setting algebraically.  The source's earlier
metronisation discussion makes `k>0` an integer configuration/condensor
number; no operator condition or independent derivation of the `L Delta`
identification occurs in this bounded chain.

The printed selection `k_max=2`, `q_max=3` in (98a) is explicitly
conditional on a “more speculative consideration.”  Its immediate printed
route is:

```text
exponential approximation and F2-F1+G2-G1 > 0
  -- [speculative F1,2=V1,2 and G1,2=Q1,2] -->
printed V1+Q1 > V2+Q2
  --> printed eta_qk^(-1) < A_q
  -- [(98), algebra] --> k < u_q --> printed numerical intervals --> (98a)
```

The final arrow is algebraically correct **from the preceding printed
`eta_qk^(-1) < A_q` inequality**.  But the preceding three links do not
cohere under ordinary substitution of the values printed on p. 268.  This is
one source-internal derivational issue, not evidence of an intended erratum
or of a physical conclusion.

## Direct source record

| Location (PDF folio / printed page) | Printed definition or claim | Status |
| --- | --- | --- |
| 269 / 263 | `k>0` is the `Kondensorziffer` of possible elementary protosimplices in a hermetric subspace.  The text derives `r=k epsilon`, `kappa=k^2`, and `Z_k=2^(k^2)`, calls `k` time-independent (`k=const(R6)`), and calls it an identifier of a time-constant metric configuration and contour. | Source framework / definition.  The metronisation prose treats the condensation steps as integral multiples; `k` is the positive integer configuration number used below. |
| 270 / 264 | `Q_j` form a `k`-fold configurative framework with a `k`-fold time-constant base contour in four configuration zones.  It says positive integers `nu>=0` give even `k=2nu` or odd `k=2nu+1`. | Explicit discrete/integer context for `k`; not a derivation of the later bound. |
| 271 / 265 | For the deviation between `epsilon'_±` and `epsilon_±`, it writes `Delta(epsilon_±^4) != 0`, calls `L` the dimension number of condensing manifest events, and says one *could perhaps* set `L Delta = k > 0`.  It sets `L=L(R4)=4`, then prints `Delta(epsilon_±^4)=(epsilon'_±^4-epsilon_±^4)/epsilon_±^4=(epsilon'_±/epsilon_±)^4-1`. | Conditional configuration-basic-quantum ansatz, followed by algebra. |
| 271 / 265 | Comparing with `L Delta=k` and `L=4` gives `epsilon'_±=epsilon_±(1+k/4)^(1/4)` for protosimplex mass `M`. | Algebra conditional on the preceding setting. |
| 272 / 266 | It obtains `(mu f/M)^4=1+(q/pi)^4(4+k)`, introduces `eta_qk` via `M=mu f eta_qk`, and prints `eta_qk [pi^4+q^4(4+k)]^(1/4)=pi`.  It explicitly makes `eta_q0=eta_q` the formal external-field member and says `k>0` where the internal structure is defined. | Defined internal `eta` family and source-local q/k roles. |
| 273 / 267, Eq. (98) | `vartheta_qk=5 eta_qk+2 sqrt(eta_qk)+1`; component definitions include `e_C=epsilon_± sqrt(vartheta_qk/8)`.  Eq. (98) repeats the displayed `eta_qk` equation.  It names `E(N,q)` external interaction energy and `E_k(N,q,k)` internal interaction energy for any `k>0`. | Definition/analogy.  The potential description is called phenomenological. |
| 274 / 268 | It defines `V1=E(N,q):E_k(k,N,q)=V_RR:V_OmegaOmega(k)=eta_q eta_qk^(-1)` and `V2=V_omegaomega:V_RR`, then defines `Q1` and `Q2` as **distinct products of underlined potential ratios**.  (The exact underline placement is material and is not flattened into plain-text products here.)  It prints `4 eta V2=(1+sqrt(eta_q))^2`, `Q1 sqrt(eta)=eta_q^2`, and **`Q2=sqrt(eta)`**. | Definitions / claimed relations for the substitution check.  `Q2` was rechecked against a 500-dpi primary-PDF render. |
| 275 / 269 | From an exponential approximation the text says one *could* assume `F2-F1+G2-G1>0`; it then makes the expressly “spekulativ” identification `F1,2=V1,2`, `G1,2=Q1,2`.  It prints `V1+Q1>V2+Q2`, then the `eta_qk` inequality below. | The explicit speculative premise of the selection. |
| 275 / 269, (98a) | It prints numerical intervals for `u_q`; assuming the more speculative consideration correct, it gives `k_max=2`, `q_max=3`. | Conditional reported selection, not a proved universal bound. |

Here and below `OmegaOmega`, `omegaomega`, and `Repsilon` merely render the
visible Greek subscripts from the scan; no additional physical identification
is made by this review.

## Symbols and dimensions actually fixed in the span

| Symbol | What the inspected pages establish | Units/status |
| --- | --- | --- |
| `k` | positive condensor/configuration number; a time-constant configuration label; discrete parity discussion on p. 264 | Dimensionless positive integer in this construction. |
| `L` | “Dimensionszahl kondensierender manifester Ereignisse”; then `L(R4)=4` | Dimensionless count, fixed here to 4. |
| `Delta` | relative fourth-power deviation of `epsilon'_±` from `epsilon_±` | Dimensionless by its displayed ratio. |
| `q` | positive protosimplex-charge parameter (`q>0`); the p. 268 comparison uses `q>=1`, and p. 269 tests `q=1,2,3,4` and `q>4` | Dimensionless charge-labelled parameter in this formula chain.  These pages do not provide a separate formal definition beyond that role. |
| `eta_qk`, `eta_q`, `eta` | numerical factors defined by (98), its formal `k=0` member, and the `q=1` specialization | Dimensionless, as required by the displayed fourth-root equations. |
| `vartheta_qk` | `5 eta_qk+2 sqrt(eta_qk)+1` | Dimensionless defined combination; the printed glyph is vartheta, not a separately defined thermodynamic theta. |
| `V1`, `V2`, `Q1`, `Q2` | quotients/products of quotients of potentials or interaction energies | Dimensionless ratios. |
| `V_xy`, `f(r)`, `r` | p. 267 gives `4 pi epsilon_0 V_xy=e_x e_y f(r)` and calls `r` a distance; p. 269 specifies an `R3` distance | `r` is a length.  The inspected passage does not state a unit convention separately for `V_xy` or `f`; only the displayed product equation and the dimensionless ratios are source-fixed. |

## Exact inequality path and the source-internal break

The printed p. 269 inequality is

```text
eta_qk^(-1) < A_q,

A_q = ((1+sqrt(eta_q))/(2 sqrt(eta eta_q)))^2
      + (1-eta_q/eta) sqrt(eta).
```

Together with Eq. (98), equivalently

```text
eta_qk^(-1) = [pi^4 + q^4(4+k)]^(1/4) / pi,
```

For any branch satisfying the preceding strict inequality,
`A_q>eta_qk^(-1)>0`; fourth-powering therefore preserves its order there.
Ordinary algebra then gives exactly the subsequently printed form

```text
k < u_q = (pi/q)^4 [ A_q^4 - 1 ] - 4.
```

Thus the conversion from that **printed** `eta_qk` inequality to `u_q` does
not need an additional assumption.

The earlier claimed path needs more caution.  The stated positive condition
is

```text
F2-F1+G2-G1 > 0.
```

Under the next, expressly speculative, identification `F1,2=V1,2` and
`G1,2=Q1,2`, ordinary replacement yields

```text
V2+Q2 > V1+Q1,
```

whereas the book prints its reverse.  Independently, using the p. 268
relations exactly as printed, its printed reverse inequality would give

```text
eta_q eta_qk^(-1) + eta_q^2/sqrt(eta)
  > (1+sqrt(eta_q))^2/(4 eta) + sqrt(eta),

eta_qk^(-1)
  > ((1+sqrt(eta_q))/(2 sqrt(eta eta_q)))^2
    + sqrt(eta)/eta_q - eta_q/sqrt(eta).
```

This differs from the subsequent printed line in both inequality direction
and its middle term: the latter has `sqrt(eta)-eta_q/sqrt(eta)`, not
`sqrt(eta)/eta_q-eta_q/sqrt(eta)`.  The inspected pages supply neither an
intermediate redefinition nor an erratum.  It would be unsound to silently
repair any of these signs or terms.  Conversely, this limited textual check
cannot identify which, if any, printed component was historically intended
to differ.

## What the printed intervals do and do not select

The book reports, without a calculation reproduced here,

```text
2 < u_q < 3  for q=1 and q=2,
1 < u_3 < 2,
0 < u_4 < 1,
u_q < 0      for all q>4.
```

If one accepts the printed strict inequality `k<u_q` and the already stated
positive integral `k`, the literal allowed-pair reading is:

| q | consequence of the stated interval |
| --- | --- |
| 1 or 2 | `k=1,2` |
| 3 | `k=1` only |
| 4 or above | no positive integral `k` |

The sentence “nur `k=1` und `k=2` von `q=1` bis `q=3`” is therefore safely
read as the combined remaining value set, not as saying that both k values
occur at every q.  This produces the displayed global maxima
`k_max=2`, `q_max=3`, subject throughout to the book's speculative premise
and to the unclosed preceding derivational break.

## Boundaries and visual record

- No numerical evaluation of `u_q` was performed in this review; the
  numerical intervals above are reported as printed, not independently
  confirmed.
- No alpha formula, `A_k`, uncertainty factor, index-order issue, modern
  criticism, source text, or canonical file was changed.
- The direct citations to (27), (28a), (72), (79), and (79a) were retained
  only as local reference labels; this bounded review did not reconstruct
  those earlier chains beyond the immediate p. 263–269 use.

Visually inspected renderings (ignored scratch directory):

- `tmp/pdfs/configuration_selection/edm2-269.png` through `edm2-275.png`
  (PDF folios 269–275 / printed pp. 263–269)
- high-resolution check of the decisive p. 269 formula block:
  `tmp/pdfs/configuration_selection/p269-hi-275.png`.
- independent 500-dpi recheck of the p. 268 `Q2` glyph:
  `tmp/pdfs/configuration_selection/p268-hi-274.png`.
