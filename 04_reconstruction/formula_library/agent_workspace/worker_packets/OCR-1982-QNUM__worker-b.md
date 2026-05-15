# OCR-1982-QNUM Worker b

## Scope

- Formula ID: HT-F-1982-QNUM
- Image pages: page-02.png; page-03.png
- OCR lines: 61-81

## Transcription

Einheitliche Beschreibung der Quantenzahlen durch k und \epsilon

G = k + 1
B = k - 1
\underline{P_1} = 2 - k
\underline{P_2} = 2k - 1
I = P + 1, 0 \le P \le G } (I)
\underline{Q(P)} = k - 1
\underline{Q(P)} = 2k - 1
\kappa(\lambda) = (1 - \delta_{1\lambda}) \delta_{1P}, 1 \le \lambda \le \Lambda = 4 - k
C = 2(P\epsilon_P + Q\epsilon_Q)(k - 1 + \kappa)/(1 + \kappa)
\epsilon_{P,Q} = \epsilon \cos \alpha_{P,Q}

\alpha_P = \pi Q\left(\kappa + \binom{P}{2}\right)
\alpha_Q = \pi Q\left[Q(k - 1) + \binom{P}{2}\right] } (II)
2q_x = (P - 2x)\left[1 - \kappa Q(2 - k)\right] + \epsilon\left[k - 1 - (1 + \kappa)Q(2 - k)\right] + C, 0 \le x \le P, q = |q_x|

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| page-02.png / OCR 65 | `\underline{P_1}` | high | Source shows underline on the label. |
| page-02.png / OCR 66 | `\underline{P_2}` | high | Source shows underline on the label. |
| page-02.png / OCR 67 | `I = P + 1, 0 \le P \le G } (I)` | medium | Right-edge brace/label is tight; kept as laid out in the source. |
| page-02.png / OCR 68-69 | `\underline{Q(P)}` on both lines | high | Source shows both `Q(P)` entries underlined and on separate lines. |
| page-02.png / OCR 70 | `\kappa(\lambda) = (1 - \delta_{1\lambda}) \delta_{1P}, 1 \le \lambda \le \Lambda = 4 - k` | medium | Tight Kronecker-delta subscripts are visible but dense. |
| page-02.png / OCR 71 | `C = 2(P\epsilon_P + Q\epsilon_Q)(k - 1 + \kappa)/(1 + \kappa)` | high | Epsilon subscripts are visible in the source. |
| page-02.png / OCR 72 | `\epsilon_{P,Q} = \epsilon \cos \alpha_{P,Q}` | high | Subscripts apply to both `\epsilon` and `\alpha`. |
| page-03.png / OCR 79-80 | `\binom{P}{2}`-style stacked term | medium | Source shows a stacked `P` over `2`, not `2P` or a simple fraction. |
| page-03.png / OCR 81 | `q = |q_x|` | high | Absolute-value bars and the subscript on `q_x` are visible. |

## Ambiguities

- The two `\underline{Q(P)}` lines appear as separate source lines, but the image does not explicitly spell out whether they are alternatives tied to `P_1/P_2` or simply consecutive definitions.
- The `\binom{P}{2}`-like term in `\alpha_P` and `\alpha_Q` is small and could be misread if the stack is not preserved.
- The `\kappa(\lambda)` line has dense `\delta_{1\lambda}` and `\delta_{1P}` clusters; the subscripts are read from the image, not inferred from OCR.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `P1 = 2 - k` | `\underline{P_1} = 2 - k` | page-02.png | 65 |
| `P2 = 2k -1` | `\underline{P_2} = 2k - 1` | page-02.png | 66 |
| `I = P +1, 0≤P≤G } (I)` | `I = P + 1, 0 \le P \le G } (I)` | page-02.png | 67 |
| `Q(P) = k - 1` | `\underline{Q(P)} = k - 1` | page-02.png | 68 |
| `Q(P) = 2k -1` | `\underline{Q(P)} = 2k - 1` | page-02.png | 69 |
| `κ(λ) = (1 - δ1λ ) δ1P , 1≤λ≤Λ=4-k` | `\kappa(\lambda) = (1 - \delta_{1\lambda}) \delta_{1P}, 1 \le \lambda \le \Lambda = 4 - k` | page-02.png | 70 |
| `C = 2(PεP + QεQ)(k - 1 + κ)/(1 + κ)` | `C = 2(P\epsilon_P + Q\epsilon_Q)(k - 1 + \kappa)/(1 + \kappa)` | page-02.png | 71 |
| `εP,Q = ε cos αP,Q` | `\epsilon_{P,Q} = \epsilon \cos \alpha_{P,Q}` | page-02.png | 72 |
| `αP = πQ(κ + ( 2P ) )` | `\alpha_P = \pi Q\left(\kappa + \binom{P}{2}\right)` | page-03.png | 79 |
| `αQ = πQ[Q(k - 1)+ ( 2P ) ]` | `\alpha_Q = \pi Q\left[Q(k - 1) + \binom{P}{2}\right]` | page-03.png | 80 |
| `2qx = (P - 2x)[1 - κQ(2 - k)] + ε[k - 1 - (1 + κ)Q(2 - k)] + C , 0 ≤ x ≤ P , q = qx` | `2q_x = (P - 2x)\left[1 - \kappa Q(2 - k)\right] + \epsilon\left[k - 1 - (1 + \kappa)Q(2 - k)\right] + C, 0 \le x \le P, q = |q_x|` | page-03.png | 81 |

## Do Not Integrate Yet

Hold canonical edits until the separate `\underline{Q(P)}` lines and the stacked `P/2` notation are confirmed against the source layout.
