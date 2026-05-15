# OCR-1982-SELECTION-N Resolver Supplement

## Verdict

conflict_resolved

## Resolution

The repeated page-8 subscript/function argument is accepted as Latin `vx`, not Greek `\nu x`, for this selection block.

Accepted notation for canonical integration of OCR lines 357-388:

- `a_{vx}`, `b_{vx}`, and `W_{vx}`
- `x_{vx}` for the state/component references
- `M_0(vx)` and `M_N(vx)` for the mass references
- `x_v` for the printed multiplet reference

Basis for resolving the blocker: the high-res page-8 image and crops show the same two-character `vx` cluster in the `f(N)` line, the `W` lines, the prose mass lines, and the final `(XXIX)` relation. The OCR's `νx` is therefore treated as glyph approximation for this page-8 selection block, not as the accepted codepoint sequence.

## Non-Blocking Findings Confirmed

- The radical in `f(N)` spans all of `N(N-2)` in the `b_{vx}` term.
- The final displayed real relation visibly preserves `+ + exp[...]` before the exponential term.
- The real-part equation label is printed as `(XVII)` in the supplied page-8 material and should be preserved as printed, not sequence-normalized.

## Canonical Integration Caveats

- This supplement resolves only the OCR-1982-SELECTION-N blocker. It is an image transcription decision for page 8, OCR lines 357-388, not a derivation or semantic normalization.
- Integrate the selection block with source-local `vx` notation exactly as above; do not silently convert these occurrences to `\nu x`.
- Do not use this page-8 `vx` decision to rewrite already reviewed formulas outside this selection block, including the separate OCR-1982-SELECTION-WVX review, unless a later canonical normalization pass explicitly chooses a project-wide symbol policy.
- Preserve the confirmed source anomalies during integration: the square root over `N(N-2)`, the doubled `+ + exp[...]`, and the printed `(XVII)` real-part label.
