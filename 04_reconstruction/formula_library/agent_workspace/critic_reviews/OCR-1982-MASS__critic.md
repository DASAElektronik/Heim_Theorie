# OCR-1982-MASS Critic Review

## Verdict

critic_ready

## Findings

1. `TASK_QUEUE.csv` row `OCR-1982-MASS`, `SOURCE_CHECK_QUEUE.csv` row `HT-F-1982-MASS`, and the source image agree that the central unified mass-spectrum expression `(XII)` is on `07_outputs/source_check_images/1982_massenformel/page-05.png`, not page 06. OCR text lines 222-224 contain only the heading context and the formula line:

   ```text
   Einheitliches Massenspektrum:

   M = µα+ (K + G + H + Φ)                                 (XII)
   ```

2. Worker A and Worker B agree on all formula-relevant visible glyphs: leading Greek `µ`, the `α+` cluster, the parenthesized sum `(K + G + H + Φ)`, underlined `G`, and original right-margin label `(XII)`. There is no worker glyph conflict requiring `worker_conflict`.

3. Page 05 confirms the leading glyph is Greek `µ`, not Latin `m` and not `u`. Clean canonical forms such as `mu * alpha_plus` are normalized aliases, not source transcription.

4. Page 05 shows the source-visible multiplier as `µα+`. The plus glyph is visibly attached to the alpha cluster, but the image is not crisp enough to prove the mathematical binding as `\alpha_+` rather than a source-visible `α+` cluster. Therefore the accepted source transcription must preserve `µα+` with an ambiguity note. A clean LaTeX rendering as `\mu\alpha_+` may be used only as a normalization candidate and must not hide this source ambiguity.

5. Page 05 confirms the central sum is parenthesized as `(K + G + H + Φ)`. The `G` in this sum is visibly underlined in the source image. The underline should be recorded as source formatting; this review does not decide whether the underline has mathematical semantics.

6. The preceding large `Φ` definition on page 05 and the later selection-rule prose beginning after `(XII)` are boundary context only. They are excluded from this accepted transcription except to identify that `(XII)` follows the auxiliary definitions and precedes the selection-rule section.

## Accepted Transcription

Accepted only as visible image transcription from:

- `07_outputs/source_check_images/1982_massenformel/page-05.png`
- `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`, lines 222-224

This is not normalization, derivation, implementation, or validation.

```text
Einheitliches Massenspektrum:

M = µα+ (K + G + H + Φ)                                 (XII)
```

Source formatting to preserve:

- The formula line is printed in red.
- The `G` in `(K + G + H + Φ)` is underlined in the source.
- `(XII)` is the original printed label at the right side of the formula line.
- `µα+` is accepted as visible-glyph transcription only. Do not silently replace it with unqualified `\mu\alpha_+`; if `alpha_plus` or `\alpha_+` is used canonically, mark it as normalization of the visible `α+` cluster.

Boundary notes:

- The preceding `Φ` formula block is not included in this MASS transcription.
- The following selection-rule prose is not included in this MASS transcription.

## Blockers

None for image transcription. The remaining work is canonical integration and explicit normalization tracking.

## Required Canonical Changes

- `04_reconstruction/formula_library/agent_workspace/TASK_QUEUE.csv`: for `OCR-1982-MASS`, set `critic_status` to `critic_ready` after this review is consumed.

- `04_reconstruction/formula_library/SOURCE_CHECK_QUEUE.csv`: for `HT-F-1982-MASS`, set status to `checked` only after canonical integration; preserve the note that the source image is `page-05.png`.

- `04_reconstruction/formula_library/formula_catalog.csv`: for `HT-F-1982-MASS`, change status from `raw_ocr` to `source_checked` after integration; update risk/notes to state that page 05 confirms the visible formula `(XII)`, source-visible `µα+`, underlined `G`, and original label `(XII)`, while `alpha_plus` remains a normalization alias.

- `04_reconstruction/formula_library/formulas/HT-F-1982-MASS.md`: replace the raw OCR working form with the accepted visible transcription above; record source image `page-05.png`; set current status to `source_checked` after integration; preserve that `mu` / `alpha_plus` / `Phi` are normalized aliases for source-visible `µ` / ambiguous `α+` / `Φ`.

- If `04_reconstruction/formula_library/symbols/symbol_register.csv` is updated during integration, distinguish source glyph `µ` from normalized `mu`, source-visible ambiguous `α+` from normalized `alpha_plus`, and source `Φ` from normalized `Phi`.

## Risk Notes To Preserve

- `source_checked` means image transcription only. It is not normalization, derivation, implementation, or validation.

- Do not treat clean LaTeX `\mu\alpha_+` as source-resolved unless a later higher-resolution source check resolves the plus binding. For this review, the source transcription remains `µα+` with ambiguity.

- Preserve the underlined `G` as source formatting; do not infer semantics from the underline in this review.

- Keep the MASS task scoped to the heading context and formula `(XII)` on page 05. Do not absorb the preceding `Φ` definition or the following selection-rule prose into this task.
