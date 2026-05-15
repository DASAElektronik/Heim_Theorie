# HT-F-1982-ALPHA: 1982 Fine-Structure Equation

## Formula Group

Source-checked image transcription from `page-03.png` and `page-04.png`.

```math
\eta = \frac{\pi}{(\pi^4 + 4)^{1/4}}
```

```math
\eta_{kq} =
\frac{\pi}{[\pi^4 + (4+k)q^4]^{1/4}}
```

```math
\vartheta = 5\eta + 2\sqrt{\eta} + 1
```

Original label: `(V)`.

```math
A_1 =
\frac{\sqrt{\eta_{11}}(1-\sqrt{\eta_{11}})}
     {1+\sqrt{\eta_{11}}}
```

```math
A_2 =
\frac{\sqrt{\eta_{12}}(1-\sqrt{\eta_{12}})}
     {1+\sqrt{\eta_{12}}}
```

The source context before the fine-structure equation identifies `hbar = h/2pi`, `c = (epsilon0 mu0)^-1/2`, and `R_- = c mu0`; this context is visible on `page-04.png` but is not included here as an ALPHA dependency block.

Fine-structure equation:

```math
\alpha\sqrt{1-\alpha^2}
=
\frac{9\vartheta(1-A_1A_2)}{(2\pi)^5},
\qquad \alpha > 0
```

The source states two solution branches:

```text
alpha_{(+)} (positive branch)
alpha_{(-)} (negative branch)
```

Numeric reciprocal values:

```math
\alpha_{(+)}^{-1} = 137{,}03596147
```

```math
\alpha_{(-)}^{-1} = 1{,}00001363
```

The source asks what this strong coupling `alpha_{(-)}` means and then gives the abbreviation:

```math
\alpha_{(+)} = \alpha,\qquad
\alpha_{(-)} = \beta \approx 137\alpha
```

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 117-147
- Source images:
  - `07_outputs/source_check_images/1982_massenformel/page-03.png`
  - `07_outputs/source_check_images/1982_massenformel/page-04.png`
- Worker packets:
  - `agent_workspace/worker_packets/OCR-1982-ALPHA__worker-a.md`
  - `agent_workspace/worker_packets/OCR-1982-ALPHA__worker-b.md`
- Critic review:
  - `agent_workspace/critic_reviews/OCR-1982-ALPHA__critic.md`

## Outputs

- `alpha_plus`
- `alpha_minus`
- `beta`

## Current Status

`source_checked`

## Audit Notes

- This is only an image-vs-OCR source check. It is not normalized, derived, implemented, or validated.
- `alpha_plus` and `alpha_minus` are normalized project aliases for the source branch notation `alpha_{(+)}` and `alpha_{(-)}`.
- The source prints reciprocal values `alpha_{(+)}^{-1}` and `alpha_{(-)}^{-1}`. Do not collapse these into `alpha(+)-1` or `alpha(-)-1`.
- OCR `ß` on the abbreviation line is a recognition error; the source image shows Greek `beta`.
- The coefficient in the fine-structure equation is source-checked as `9 vartheta`, not `99`.
- The source-local abbreviation is `eta_{kq}` in this block. Later `HT-F-1982-AUX` material uses or normalizes nearby `eta_{qk}` notation; reconcile this explicitly during normalization before implementation.
- The next `B) Massenspektrum...` heading and formulas `(VI)`, `(VII)`, and `(VIII)` are out of scope for this entry.

## Risks

- `eta_{kq}` versus later `eta_{qk}` notation requires a normalization decision.
- The surrounding `C_\pm` elementary-charge paragraph was used only as context for the `vartheta` glyph and is not source-checked here as an ALPHA formula.
- Alpha branch naming changes across 1982, 1989, XLSM, and C/Pascal code.
