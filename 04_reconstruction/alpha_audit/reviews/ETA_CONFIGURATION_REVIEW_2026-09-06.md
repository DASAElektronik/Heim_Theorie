# Eta configuration and index-order reconstruction — 2026-09-06

Scope: a bounded, source-led reconstruction of the one- and two-index
`eta` notation needed around Book II Eq. (105). This is an evidence note,
not a new formula, numerical fit, or claim of physical validity. Formulae
below are short transcriptions from visually inspected local PDF pages.

## Result

**Book II fixes the order of its two-index family as `(q,k)`, not `(k,q)`.**
It explicitly identifies the Book-I one-index factor as the formal
`k=0` member, `eta_(q,0)=eta_q`, and identifies `eta_(1,0)=eta`.
Consequently its Eq. (105) factor `eta_(1,k)` has first index `q=1` and
second index the configuration number `k`. The same page defines `A_k`
from that `eta_(1,k)`; hence the displayed product `A_1 A_2` uses
`eta_(1,1)` and `eta_(1,2)` within the Book-II chain.

This is direct book evidence for the `(q,k)` reading used by 1982 Eq. (IX)
and the 1989 cross-reference. It does **not** make the source-local
`eta_(kq)` spelling in the 1982 Eq. (V) source-identical to that book
definition, nor does it authorize choosing an index order by an alpha fit.

## Visually checked evidence

| Source and location | What is printed / stated | Status for this review |
| --- | --- | --- |
| *Elementarstrukturen der Materie I*, PDF folio 251 / printed p. 245, Eq. (27) | `m(n,q)=m(n) eta_q` and `eta_q (4q^4+pi^4)^(1/4)=pi`. | One-index external factor; q is the charge-labelled argument of `m(n,q)`. |
| Volume I, folio 253 / p. 247, Eq. (28a) and preceding prose | It explicitly abbreviates `eta_1=eta`, then prints `eta (4+pi^4)^(1/4)=pi`. | `q=1` specialization of the one-index family. The surrounding charge-component account is expressly speculative; that qualifier is not removed here. |
| Volume I, folio 254 / p. 248, Eq. (29) | `vartheta=5 eta+2 sqrt(eta)+1`. | Definition/abbreviation for the unindexed case. |
| *Elementarstrukturen der Materie II*, folio 271 / p. 265 | In deriving the internal case it introduces `k>0` as a configurative basic quantum number; the prose uses tentative language ("könnte eventuell"). | The derivational motivation is conditional, not an independently established physical fact. |
| Volume II, folio 272 / p. 266 | It introduces `eta_qk` with `eta_qk [pi^4+q^4(4+k)]^(1/4)=pi`; then explicitly says `eta_0k=1`, `eta_q0=eta_q` for the external-charge-field factor of (27), and `eta_1,0=eta` for the external field at `q=1` of (28a). It further says `k=0` in `eta_q0` is only a formal marker for the external `R_3` domain. | **Explicit Book-I-to-Book-II index bridge.** First slot is q; second slot is k. The `k=0` case is formal, whereas the text says k remains positive when the relevant internal structure is defined. |
| Volume II, folio 273 / p. 267, Eq. (98) | The internal charge components are summarized with `vartheta_qk=5 eta_qk+2 sqrt(eta_qk)+1` and the same defining equation `eta_qk [pi^4+q^4(4+k)]^(1/4)=pi`. It then distinguishes external `E(N,q)` from internal `E_k(N,q)` with any `k>0`. | Explicit two-index eta and vartheta definitions, with q and k separately named in the immediately following prose. |
| Volume II, folio 274 / p. 268 | "nur für q>=1 kann k in eta_qk nach (98) erscheinen"; it then uses `eta_1=eta` in the comparison with (28a). | Direct confirmation that `eta_qk` is the form in which the k dependence appears, for charge q at least one. |
| Volume II, folio 275 / p. 269, Eq. (98a) | After saying *if* a "mehr spekulative Betrachtung" is right, it finds only `k=1,2` for `q=1` through `q=3` compatible, and prints `k_max=2`, `q_max=3`. | Conditional/speculative configuration restriction, not a proved index convention or an empirical fit. |
| Volume II, folio 269 / p. 263 and folio 270 / p. 264 | k is called the `Kondensorziffer` / `Konfigurationszahl`; it is time-independent in the stated construction. Electron and proton motivate considering k=1 and k=2. | Context for the second eta index; no separate eta function is defined on these pages. |
| Volume II, folio 308 / p. 302, Eq. (105) | `(1+sqrt(eta_1k)) A_k=(1-sqrt(eta_1k))sqrt(eta_1k)` alongside the alpha equation containing `A_1 A_2 Y_3`. | Applying the already-defined Book-II family gives `A_k` from `eta_(q=1,k)`. The subsequent numerical calculation visibly sets `Y_3=1`; that is a displayed specialization, not a predictive parameter fit in this review. |

## Source chain

```text
Book I (27): eta_q                         [one-index external family]
       q=1 -> Book I (28a): eta_1 = eta
                         \\
Book II p.266: eta_(q,0) = eta_q; eta_(1,0) = eta
                 |
Book II (98): eta_(q,k)[pi^4+q^4(4+k)]^(1/4) = pi
                 |
                 +-- q = 1 --> eta_(1,k) --> Book II (105): A_k
                                                   |       |
                                                   +-- A_1 A_2
```

The diagram is a notation/reference chain, not a derivation of Eq. (105)
from the preceding equations.

## The 1982/1989 notation collision

The local IGW source reproduction retains two different subscript spellings
for the same printed right-hand expression:

| Source | PDF folio / printed page / label | Literal eta notation |
| --- | --- | --- |
| `Massenformel_nach_B_Heim_1982.pdf` | folio 3 / p. 3 / (V) | `eta_kq=pi/[pi^4+(4+k)q^4]^(1/4)`; this same block uses `eta_11` for `A_1` and `eta_12` for `A_2`. Earlier on that page q is `|q_x|`, and it lists possible configurations `k=1, k=2`. |
| Same 1982 PDF | folio 5 / p. 5 / (IX) | `eta_qk=pi/[pi^4+(4+k)q^4]^(1/4)`. |
| `Erweiterte_Massenformel_Nach_Heim_1989.pdf` | folio 3 / printed p. 12, prose after (B7) | Calls the constants `eta_(q,k)`, gives `eta_(1,0)=eta`, and says they "lauten wie in (IX)". |

Thus, for the 1989 source and the Book-II chain, `eta_(1,2)` is
source-supported as `(q,k)=(1,2)`. The 1982 (V) page visibly uses the
opposite glyph order, `eta_kq`, while its later (IX) uses `eta_qk` without a
stated erratum or semantic explanation. For `eta_11` this is numerically
immaterial; for `eta_12` it is material. No page inspected supplies a
license to silently rewrite (V), or to use an alpha result to decide which
notation the source "must have meant".

## Boundaries and remaining uncertainty

- The book evidence settles **the Book-II index convention** and the
  Book-I external-to-Book-II internal notation bridge. It does not prove
  that the 1982 (V) subscript order was a typographical error.
- The text’s k=1/2 restriction at (98a) is explicitly conditional on a
  more speculative consideration. It must not be upgraded to an empirical
  selection rule.
- Eq. (105) supplies an A-to-eta dependency, but this review does not
  reconstruct all of Eq. (105), determine Y3, or make a fit claim.
- No modern physics literature, external web source, canonical formula, or
  implementation was altered.

## Render record

All images were rendered only to the ignored project temporary directory:

- `tmp/pdfs/eta_configuration/band1-251.png`, `band1-253.png`,
  `band1-254.png`
- `tmp/pdfs/eta_configuration/band2-97-271.png`,
  `band2-98-272.png` through `band2-98-275.png`,
  `band2-105-308.png`
- `tmp/pdfs/eta_configuration/igw82-03.png`, `igw82-05.png`,
  `igw89-03.png`
