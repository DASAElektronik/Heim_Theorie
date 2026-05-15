# OCR-1982-SELECTION-N Critic Review

## Verdict

worker_conflict

## Findings

1. Blocking subscript conflict on page 8, OCR lines 360, 365, 367-369, 374, 376, and 384: Worker A transcribes the repeated compact subscript as `\nu x` in `a_{\nu x}`, `b_{\nu x}`, `W_{\nu x}`, `x_{\nu x}`, `M_0(\nu x)`, and `M_N(\nu x)`; Worker B transcribes the same source positions as `vx`. The page image shows a v-shaped glyph, but this source-check pass is image transcription only and the scan/font does not unambiguously distinguish Greek `\nu` from Latin `v`. Because this is formula-relevant and the image does not clearly resolve the code point, the task cannot be marked `critic_ready`.

2. Page 8, OCR line 360: both workers correctly restore the radical in `f(N)`. The page image shows the square-root bar spanning the whole `N(N-2)` expression in the `b_*` term; the OCR flattened this to plain `N ( N - 2)`.

3. Page 8, OCR line 374: the equation label beside the real-part relation appears in the page image as `(XVII)`, matching OCR line 374 and both worker packets, not as a clearly visible `(XXVII)`. This is anomalous in sequence after `(XXVI)` and before `(XXVIII)`, so it must be preserved as a source label anomaly rather than normalized during source check.

4. Page 8, OCR line 384: the final displayed real relation visibly contains `+ + exp[...]` before the exponential term. Both workers preserve this visible doubled plus. It must not be normalized away in a source transcription.

5. Page 8, OCR lines 362-376: the N-case prose and the real/imaginary split are broadly consistent across the worker packets: `F(\Gamma)=0` for `N != 1`, `N=0` gives `f=0`, and `f(1)` is complex. This does not resolve the subscript conflict.

## Blockers

- Resolve the repeated subscript glyph as either Greek-nu form (`\nu x`) or Latin-v form (`vx`) using a higher-resolution/source-level check, typographic evidence from adjacent pages, or an explicit integrator decision that records the ambiguity. Under the current Critic Protocol, the worker disagreement remains formula-relevant and unresolved.

## Required Canonical Changes

- None while this review remains `worker_conflict`.
- Do not update `04_reconstruction/formula_library/SOURCE_CHECK_QUEUE.csv`, `04_reconstruction/formula_library/formula_catalog.csv`, or canonical formula files from either worker packet until the subscript conflict is resolved.

## Risk Notes To Preserve

- Source-checked status, once achieved, will still be image transcription only; it will not validate, normalize, derive, or implement the resonance-order rule.
- Preserve the verified square root over `N(N-2)` in `f(N)`.
- Preserve the visible doubled plus in the `(XXIX)` line as a source glyph unless a later normalization pass explicitly treats it as a typo.
- Preserve the real-part label anomaly as printed: current page-image reading is `(XVII)`, not a normalized sequence label.
