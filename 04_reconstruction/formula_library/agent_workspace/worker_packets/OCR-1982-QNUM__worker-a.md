# OCR-1982-QNUM Worker a

## Scope

- Formula ID: HT-F-1982-QNUM
- Image pages: 1982_massenformel/page-02.png; 1982_massenformel/page-03.png
- OCR lines: 61-81

## Transcription

```text
G    = k+1
B    = k-1
\underline{P_1} = 2 - k
\underline{P_2} = 2k -1
I    = P+1,                 0≤P≤G                                                     } (I)
\underline{Q(P)} = k - 1
\underline{Q(P)} = 2k -1
\kappa(\lambda) = (1 - \delta_{1\lambda}) \delta_{1P}, 1≤\lambda≤\Lambda=4-k
C    = 2(P\epsilon_P + Q\epsilon_Q)(k - 1 + \kappa)/(1 + \kappa)
\epsilon_{P,Q} = \epsilon \cos \alpha_{P,Q}


                                              2
                                  Einführung in die Heimsche Massenformel
                                           IGW Innsbruck, 2003

\alpha_P       = \pi Q(\kappa + \binom{P}{2})
\alpha_Q       = \pi Q[Q(k - 1)+ \binom{P}{2}]                                                              } (II)
2q_x      = (P - 2x)[1 - \kappa Q(2 - k)] + \epsilon[k - 1 - (1 + \kappa)Q(2 - k)] + C ,       0 ≤ x ≤ P , q = |q_x|
```

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| page 2, OCR 65-66 | `\underline{P_1}` and `\underline{P_2}` | 0.78 | The labels are visibly underlined in the source block; OCR drops the underline. |
| page 2, OCR 68-69 | `\underline{Q(P)}` on both lines | 0.69 | The two `Q(P)` entries are underlined in the source and appear as paired alternatives. |
| page 2, OCR 70 | `\delta_{1\lambda}` and `\delta_{1P}` | 0.98 | The Kronecker deltas use lowered subscripts in the image. |
| page 2, OCR 71 | `P\epsilon_P + Q\epsilon_Q` | 0.97 | The subscripts on both epsilons are visible in the source. |
| page 2, OCR 72 | `\epsilon_{P,Q}` and `\alpha_{P,Q}` | 0.97 | The comma is part of the subscript in the image. |
| page 3, OCR 79-80 | `\binom{P}{2}` | 0.96 | The source shows a binomial-style `P` over `2`, not a literal parenthesized `2P`. |
| page 3, OCR 81 | `|q_x|` | 0.99 | The absolute-value bars are clear in the source. |

## Ambiguities

- The underline treatment on `P_1`, `P_2`, and `Q(P)` is visible, but plain text cannot capture the exact typographic extent with perfect fidelity.
- The two consecutive `Q(P)` lines appear to be alternatives tied to the duplicated positions, but the source does not spell out that relationship algebraically.
- The `Q` glyph in `\alpha_P` and `\alpha_Q` is visually clear, but its role is source-local and should not be repaired from later material.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `P1 = 2 - k` / `P2 = 2k -1` | `\underline{P_1} = 2 - k` / `\underline{P_2} = 2k - 1` | page 2 | 65-66 |
| `Q(P) = k - 1` / `Q(P) = 2k -1` | `\underline{Q(P)} = k - 1` / `\underline{Q(P)} = 2k - 1` | page 2 | 68-69 |
| `κ(λ) = (1 - δ1λ ) δ1P , 1≤λ≤Λ=4-k` | `\kappa(\lambda) = (1 - \delta_{1\lambda}) \delta_{1P}, 1\le\lambda\le\Lambda=4-k` | page 2 | 70 |
| `C    = 2(PεP + QεQ)(k - 1 + κ)/(1 + κ)` | `C    = 2(P\epsilon_P + Q\epsilon_Q)(k - 1 + \kappa)/(1 + \kappa)` | page 2 | 71 |
| `εP,Q = ε cos αP,Q` | `\epsilon_{P,Q} = \epsilon \cos \alpha_{P,Q}` | page 2 | 72 |
| `αP       = πQ(κ + ( 2P ) )` | `\alpha_P       = \pi Q(\kappa + \binom{P}{2})` | page 3 | 79 |
| `αQ       = πQ[Q(k - 1)+ ( 2P ) ]` | `\alpha_Q       = \pi Q[Q(k - 1)+ \binom{P}{2}]` | page 3 | 80 |
| `2qx      = (P - 2x)[1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C ,       0 ≤ x ≤ P , q = qx` | `2q_x      = (P - 2x)[1 - \kappa Q(2 - k)] + \epsilon[k - 1 - (1 + \kappa)Q(2 - k)] + C ,       0 \le x \le P , q = |q_x|` | page 3 | 81 |

## Do Not Integrate Yet

Source-local underline treatment and the paired `Q(P)` lines remain ambiguous enough that canonical edits should wait for cross-checking.
