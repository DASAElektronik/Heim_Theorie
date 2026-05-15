# HT-F-1982-MASS: 1982 Unified Mass Spectrum

## Formula

Source-checked image transcription from `page-05.png`:

```text
Einheitliches Massenspektrum:

M = µα+ (K + G + H + Φ)                                 (XII)
```

Source formatting notes:

- The formula line is printed in red.
- `G` is underlined in the source image.
- The `α+` cluster is source-visible; its exact plus binding is not normalized in this entry.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 222-224
- Source image: `07_outputs/source_check_images/1982_massenformel/page-05.png`
- Original label: `(XII)`
- Worker packets:
  - `agent_workspace/worker_packets/OCR-1982-MASS__worker-a.md`
  - `agent_workspace/worker_packets/OCR-1982-MASS__worker-b.md`
- Critic review:
  - `agent_workspace/critic_reviews/OCR-1982-MASS__critic.md`

## Dependencies

- `HT-F-1982-MU`
- `HT-F-1982-ALPHA`
- `HT-F-1982-AUX`
- `HT-F-1982-SELECTION`

## Outputs

- Particle mass `M`.

## Current Status

`source_checked`

## Audit Notes

- This is only an image-vs-OCR source check. It is not normalized, derived, implemented, or validated.
- The source image is `page-05.png`, not `page-06.png`.
- The source-visible factor is `µα+`. Treating this as `mu * alpha_plus` is a later normalization step.
- The underlined `G` is preserved as source formatting. Per `NORM-1982-MASS-UNDERLINED-G`, it does not create a special weighted term by default.
- Per `NORM-1982-G-SYMBOL-ROLES`, the `G` in `(K + G + H + Phi)` is the auxiliary mass contribution `G_aux`, not `G_count = k + 1`.
- This is the central 1982 mass expression, but it is not independently usable until `K`, `G`, `H`, `Phi`, `mu`, `alpha_plus`, and the occupation tuple selection rule are normalized.

## Risks

- `G` is overloaded: one symbol is the count of subconstituents, another is a mass contribution.
- `Phi` is a long OCR-fragile expression.
- Selection of valid `n_j` tuples is a major source of hidden freedom.
