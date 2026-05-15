# OCR-1982-QNUM Critic Review

## Verdict

critic_ready

## Findings

1. Source page 02 / OCR lines 68-69 visibly contains two separate underlined `Q(P)` lines:
   `\underline{Q(P)} = k - 1` and `\underline{Q(P)} = 2k - 1`. Both workers preserve the two visible lines. The image does not explicitly bind the first line to `P_1` and the second line to `P_2`; that relation must remain unresolved in source transcription, not silently normalized.

2. Source page 02 / OCR lines 65-66 visibly underlines the labels `P_1` and `P_2`; source page 02 / OCR lines 68-69 visibly underlines the `Q(P)` labels. Both workers preserve this typography. The underline should be treated as source typography on the printed labels, not as a new semantic operator.

3. Source page 02 / OCR line 70 resolves the Kronecker-delta subscripts as `\delta_{1\lambda}` and `\delta_{1P}` in
   `\kappa(\lambda) = (1 - \delta_{1\lambda}) \delta_{1P}, 1 \le \lambda \le \Lambda = 4 - k`.
   Both workers agree, and the source image supports this correction over OCR `δ1λ` / `δ1P`.

4. Source page 03 / OCR lines 79-80 shows a stacked `P` over `2` in both `\alpha_P` and `\alpha_Q`. The workers transcribe this as `\binom{P}{2}`. This is acceptable for canonical transcription if a risk note states that `\binom{P}{2}` is a typographic interpretation of the visible stacked term, not a validated combinatorial normalization. The current canonical file has `binom(2,P)`, which reverses the visible stack.

5. Source page 03 / OCR line 81 confirms the subscripted charge and absolute-value relation:
   `2q_x = ... , 0 \le x \le P, q = |q_x|`.
   Both workers preserve `q_x` and `q = |q_x|`.

## Accepted Transcription

Accepted only as visible image transcription from `07_outputs/source_check_images/1982_massenformel/page-02.png` and `07_outputs/source_check_images/1982_massenformel/page-03.png`, OCR lines 61-81. This is not normalization, derivation, implementation, or validation.

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
\tag{I}
```

```math
\underline{Q(P)} = k - 1
```

```math
\underline{Q(P)} = 2k - 1
```

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
\tag{II}
```

```math
2q_x =
(P - 2x)\left[1 - \kappa Q(2 - k)\right]
+ \epsilon\left[k - 1 - (1 + \kappa)Q(2 - k)\right]
+ C,
\qquad 0 \le x \le P,\qquad q = |q_x|
```

## Blockers

None for source-image transcription. Canonical integration must preserve the unresolved typography and binding notes below.

## Required Canonical Changes

- Update `04_reconstruction/formula_library/formulas/HT-F-1982-QNUM.md` from `raw_ocr` to source-checked transcription for OCR lines `61-81`.
- In `04_reconstruction/formula_library/formulas/HT-F-1982-QNUM.md`, preserve the two separate underlined `Q(P)` source lines and do not infer a `P_1`/`P_2` mapping in the source transcription field.
- In `04_reconstruction/formula_library/formulas/HT-F-1982-QNUM.md`, correct `alpha_P` and `alpha_Q` from `binom(2,P)` to a source-transcription form equivalent to `\binom{P}{2}`, with an explicit risk note that this represents the visible stacked `P` over `2`.
- In `04_reconstruction/formula_library/formulas/HT-F-1982-QNUM.md`, correct `kappa(lambda)` to use `\delta_{1\lambda}` and `\delta_{1P}`.
- In `04_reconstruction/formula_library/formulas/HT-F-1982-QNUM.md`, preserve `q = |q_x|` from source page 03 / OCR line 81.
- Update `04_reconstruction/formula_library/formula_catalog.csv` for `HT-F-1982-QNUM`: set status to `source_checked` after integration and replace the risk note about unresolved OCR symbols with notes about unresolved `Q(P)` binding and stacked-term interpretation.
- Update `04_reconstruction/formula_library/SOURCE_CHECK_QUEUE.csv` for `HT-F-1982-QNUM`: set status to `checked` after integration.
- Update `04_reconstruction/formula_library/agent_workspace/TASK_QUEUE.csv` for `OCR-1982-QNUM`: set `critic_status` to `critic_ready` after integration.

## Risk Notes To Preserve

- `source_checked` here means visible-image transcription only. It is not normalization, derivation, implementation, or validation.
- The two underlined `Q(P)` lines are accepted as visible separate source lines; their relation to underlined `P_1` and `P_2` remains unresolved in this task.
- Underlines on `P_1`, `P_2`, and `Q(P)` are source typography and should not be silently dropped in the transcription layer.
- `\binom{P}{2}` is an accepted LaTeX rendering of the visible stacked `P` over `2`, but this is a typographic interpretation. Any later mathematical interpretation as a binomial coefficient must be marked as normalization or validation, not source transcription.
- Clean LaTeX can hide the ambiguity of the duplicated `Q(P)` notation and the stacked `P/2` term; canonical notes should keep those visible-source warnings.
- The source uses `Q` in multiple nearby roles, including the symbol list's doubled spin `Q = 2J` and the underlined `Q(P)` value. Do not disambiguate these roles during source transcription.
