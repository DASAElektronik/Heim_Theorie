# HT-F-1982-QNUM: 1982 Quantum-Number Definitions

## Formula Group

Source-checked image transcription from `page-02.png` and `page-03.png`.

```math
G = k + 1
```

```math
B = k - 1
```

```math
\underline{P_1} = 2 - k
```

```math
\underline{P_2} = 2k - 1
```

```math
I = P + 1,\qquad 0 \le P \le G
```

Original label: `(I)`.

The source then prints two separate underlined `Q(P)` lines:

```math
\underline{Q(P)} = k - 1
```

```math
\underline{Q(P)} = 2k - 1
```

The source does not explicitly bind these two lines to `P_1` and `P_2` in this block.

```math
\kappa(\lambda) = (1 - \delta_{1\lambda})\delta_{1P},
\qquad 1 \le \lambda \le \Lambda = 4 - k
```

```math
C = 2(P\epsilon_P + Q\epsilon_Q)(k - 1 + \kappa)/(1 + \kappa)
```

```math
\epsilon_{P,Q} = \epsilon \cos \alpha_{P,Q}
```

```math
\alpha_P = \pi Q\left(\kappa + \binom{P}{2}\right)
```

```math
\alpha_Q = \pi Q\left[Q(k - 1) + \binom{P}{2}\right]
```

Original label: `(II)`.

```math
2q_x =
(P - 2x)\left[1 - \kappa Q(2 - k)\right]
+ \epsilon\left[k - 1 - (1 + \kappa)Q(2 - k)\right]
+ C,
\qquad 0 \le x \le P,\qquad q = |q_x|
```

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 61-81
- Source images:
  - `07_outputs/source_check_images/1982_massenformel/page-02.png`
  - `07_outputs/source_check_images/1982_massenformel/page-03.png`
- Original labels: `(I)`, `(II)`
- Worker packets:
  - `agent_workspace/worker_packets/OCR-1982-QNUM__worker-a.md`
  - `agent_workspace/worker_packets/OCR-1982-QNUM__worker-b.md`
- Critic review:
  - `agent_workspace/critic_reviews/OCR-1982-QNUM__critic.md`

## Outputs

- `G`, `B`, `P_1`, `P_2`, `I`
- `Q(P)` lines
- `kappa(lambda)`
- `C`
- `epsilon_{P,Q}`
- `alpha_P`, `alpha_Q`
- `q_x`, `q`

## Current Status

`source_checked`

## Audit Notes

- This is only an image-vs-OCR source check. It is not normalized, derived, implemented, or validated.
- Underlines on `P_1`, `P_2`, and the two `Q(P)` labels are source typography and are preserved in the transcription layer.
- The two separate underlined `Q(P)` lines are accepted as visible source lines. Their relation to underlined `P_1` and `P_2` remains unresolved in this task.
- The source uses `Q` in multiple nearby roles, including the symbol list's doubled spin `Q = 2J` and the underlined `Q(P)` value. Do not disambiguate these roles during source transcription.
- `\binom{P}{2}` is a LaTeX rendering of the visible stacked `P` over `2`. Normalization decision `NORM-STACKED-BINOMIAL` maps this notation to `choose(P, 2)` for implementation.

## Risks

- Clean LaTeX can hide the ambiguity of the duplicated `Q(P)` notation; the stacked parenthesis notation itself is normalized by `NORM-STACKED-BINOMIAL`.
- The exact semantic role of the underlined labels requires a separate normalization pass before implementation.
- 1989 changes `C` and `qx`; `NORM-1989-QX-C-OVER-K` requires versioned `C_1982` and `C_1989` implementation names.
