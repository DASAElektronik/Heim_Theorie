# OCR-1982-ALPHA Critic Review

## Verdict

critic_ready

## Findings

1. `TASK_QUEUE.csv`, `SOURCE_CHECK_QUEUE.csv`, and `formula_catalog.csv` have incomplete source-line ranges for the current ALPHA target. The visible source block needed for `HT-F-1982-ALPHA` starts with the page-03 abbreviation block at OCR lines 118-122 and continues through the `Kürzung` line at OCR line 147. The range should be widened to `117-147` if blank separator line 117 is preserved, or at minimum `118-147`; using `128-145` or `131-145` omits source material already represented in canonical ALPHA and omits the branch abbreviation line.

2. Page 04 / OCR line 139 resolves the Worker A vs Worker B coefficient issue in favor of Worker A: the source reads `9ϑ`, not `99`. The second glyph matches the vartheta glyph in page 04 / OCR line 137 (`2ϑ\hbar/R_-`) and page 03 / OCR line 120 (`ϑ = 5η + 2√η + 1`). This should be transcribed as visible glyph `\vartheta`; any normalized `theta` alias must be marked as normalization.

3. Page 04 / OCR lines 143-144 clearly use reciprocal notation with parenthesized branch signs as subscripts: `α_{(+)}^{-1}` and `α_{(-)}^{-1}`. They are not subtraction forms `alpha(+)-1` / `alpha(-)-1`, and clean LaTeX must not hide that the source prints parenthesized signs, not source words `alpha_plus` / `alpha_minus`.

4. Page 04 / OCR line 147 supports Greek beta: `α_{(-)} = β ≈ 137 α`. OCR `ß` is a recognition error. No blocker remains for this glyph.

5. Page 03 / OCR lines 118-122 belong in `HT-F-1982-ALPHA` because the current canonical ALPHA formula directly uses `η`, `ϑ`, `A1`, and `A2`. The source-local abbreviation line is `η_{kq}`, not a normalized `η_{qk}`. `HT-F-1982-AUX` may continue to carry later auxiliary-function formulas from OCR lines 169-220, but canonical notes must prevent those later AUX entries from silently overwriting the source-local ALPHA abbreviation spelling/order.

6. Page 04 / OCR line 137 (`C±`) is context for the preceding elementary-charge paragraph, not part of the accepted ALPHA formula transcription. Its radical scope is visible as `C_\pm = \pm \sqrt{2ϑ\hbar/R_-}/(4π)^2`, with `(4π)^2` outside the radical. It should be preserved only as a boundary/context note unless the integrator decides to source-check the surrounding charge paragraph separately.

7. The next section starts at page 04 after OCR line 147 with `B) Massenspektrum der Grundzustände und ihrer Resonanzen`. Later mass-spectrum constants and formulas `(VI)`, `(VII)`, and `(VIII)` are out of scope for this ALPHA review except as boundary notes.

## Accepted Transcription

Accepted only as visible image transcription from:

- `07_outputs/source_check_images/1982_massenformel/page-03.png`, OCR lines 117-122
- `07_outputs/source_check_images/1982_massenformel/page-04.png`, OCR lines 131-147

This is not normalization, derivation, implementation, or validation.

```math
\eta = \frac{\pi}{(\pi^4 + 4)^{1/4}}
```

```math
\eta_{kq} =
\frac{\pi}{[\pi^4 + (4+k)q^4]^{1/4}}
```

```math
\vartheta = 5\eta + 2\sqrt{\eta} + 1
\tag{V}
```

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

Source context before the fine-structure equation identifies `\hbar = h/2\pi`, `c = (\epsilon_0\mu_0)^{-1/2}`, and `R_- = c\mu_0`; this context is visible on page 04 but is not accepted here as an ALPHA dependency block.

```math
\alpha\sqrt{1-\alpha^2}
=
\frac{9\vartheta(1-A_1A_2)}{(2\pi)^5},
\qquad \alpha > 0.
```

```text
Lösung: α_{(+)} (positiver Zweig) und α_{(-)} (negativer Zweig).
```

```math
\alpha_{(+)}^{-1} = 137{,}03596147
```

```math
\alpha_{(-)}^{-1} = 1{,}00001363
```

```text
Was bedeutet diese starke Kopplung α_{(-)}?
```

```math
\alpha_{(+)} = \alpha,\qquad
\alpha_{(-)} = \beta \approx 137\alpha.
```

Boundary only: the following `B) Massenspektrum...` heading and formulas `(VI)`, `(VII)`, `(VIII)` are excluded from this accepted transcription.

## Blockers

None for image transcription. The remaining work is canonical integration and normalization risk tracking.

## Required Canonical Changes

- `04_reconstruction/formula_library/agent_workspace/TASK_QUEUE.csv`: for `OCR-1982-ALPHA`, change `source_text_lines` from `128-145` to `117-147` and set `critic_status` to `critic_ready` after this review is consumed.

- `04_reconstruction/formula_library/SOURCE_CHECK_QUEUE.csv`: for `HT-F-1982-ALPHA`, change `source_lines` from `128-145` to `117-147`; set status to `checked` only after canonical integration.

- `04_reconstruction/formula_library/formula_catalog.csv`: for `HT-F-1982-ALPHA`, change source lines from `131-145` to `117-147`; set source status to `source_checked` after integration; update notes to state that reciprocal branch notation and beta abbreviation are image-confirmed. Inputs should include the source-local abbreviation symbols `eta`, `eta_kq`, `vartheta`, `A1`, and `A2` or explicitly document any normalized aliases.

- `04_reconstruction/formula_library/formulas/HT-F-1982-ALPHA.md`: replace the raw OCR working form with the accepted visible transcription above; record source images page 03 and page 04; set current status to `source_checked` after integration; preserve that `alpha_plus` / `alpha_minus` are normalized output aliases for source `α_{(+)}` / `α_{(-)}`.

- `04_reconstruction/formula_library/formulas/HT-F-1982-AUX.md`: add or preserve an audit note that AUX covers later auxiliary-function material from OCR lines 169-220 and must not silently override the ALPHA page-03 abbreviation block. In particular, source-local `η_{kq}` in ALPHA and later AUX `η_{qk}`/normalized aliases require an explicit normalization decision before implementation.

- `04_reconstruction/formula_library/symbols/symbol_register.csv`: if updated during integration, distinguish source glyphs/aliases: `vartheta` as the visible page-03/page-04 glyph, `alpha_plus` for source `α_{(+)}`, `alpha_minus` for source `α_{(-)}`, and `beta` for source `β` in the Kürzung line.

## Risk Notes To Preserve

- `source_checked` means image transcription only. It is not normalization, derivation, implementation, or validation.

- Do not normalize `α_{(+)}^{-1}` / `α_{(-)}^{-1}` into branch names without recording the source's parenthesized subscript signs and reciprocal superscript.

- Do not treat OCR `ß` as source text; page 04 / OCR line 147 shows Greek `β`.

- Do not include the later mass-spectrum section or formulas `(VI)`, `(VII)`, `(VIII)` in `HT-F-1982-ALPHA`, except as boundary notes.

- The `C_\pm` line can be used as context for confirming the vartheta glyph, but it is not part of the ALPHA formula dependency set unless a separate source-check task includes the elementary-charge paragraph.
