# OCR-1989-ALPHA Critic Review

Verdict: `critic_ready`

## Accepted source-visible transcription

Intro:
`In φ und β_(0) ist die Feinstrukturkonstante α enthalten.`

B58:
`α sqrt(1 - α^2) = 9ϑ/(2π)^5 (1 - C')`

B59:
`1 - C' = 1 - ((1 + η_{2,2})/(η η_{1,1} η_{1,2})) ((1 - sqrt(η))/(1 + sqrt(η)))^2 = K_α`

B60:
`α_(±)^-2 = 1/2 D'^2 (1 ± sqrt(1 - 4 / D'^2))`

B61:
`D' = (2π)^5 / (9ϑK_α).`

B62:
`α_(+) = 0.0072973525253328589 und α_(-) = 0.999985890199089`

Reciprocal line:
`1/α_(+) = 137,03601, 1/α_(-) = 1,0000142`

Comparison line:
`1/α_+ = 137,0360114 ± 3.4 · 10^-8`

## Resolution notes

- Intro text: accept Greek beta `β_(0)`, not OCR `ß(0)`. The `(0)` is visually subscripted.
- B58: source-visible coefficient is `9ϑ/(2π)^5`; do not read it as `99` and do not replace the source glyph with `9*theta` in source transcription.
- B59: preserve the full chain `1 - C' = 1 - (...) = K_α`. In source transcription, `K_α` applies to the complete right-side expression after `1 -`, and by equality to `1 - C'`; do not normalize this to `1 - C' = 1 - K_alpha`.
- B60/B62: source uses compact branch notation as subscripted parenthesized signs: `α_(±)`, `α_(+)`, `α_(-)`. Canonical source transcription should record that form; normalized implementation names may be separate.
- B61: denominator is `9ϑK_α`.
- Post-1989 comparison: keep `Nistler & Weirauch 2002` only as source-context/comparison text, not as historical proof for the 1989 formula.

## Required canonical edits

- Replace the current B59 working line `1 - C_prime = 1 - K_alpha` with the full source-visible equality chain.
- Add a source note correcting OCR `ß(0)` to `β_(0)`.
- Preserve source-visible `9ϑ`, `(2π)^5`, `K_α`, `D'`, and branch notation in the transcription layer before any ASCII implementation normalization.
- Keep the reciprocal values and the 2002 experimental comparison as separate source-context lines, not outputs of the formula core.

## Unresolved normalization risks

- `ϑ` should likely normalize to the project theta/vartheta symbol, but this review only confirms the source glyph.
- `K_α` is a final equality target for B59; downstream algebra must not infer a different scope from the flattened text.
- `α_(+)` / `α_(-)` and later `α_+` are visibly distinct source notations and should not be silently merged.
- Decimal commas in reciprocal/comparison lines need locale-aware handling if parsed numerically.

## Implementation red flags

- Do not implement B59 from the current canonical shortcut; it is structurally wrong.
- Do not OCR-clean `9ϑK_α` into `99K_α`.
- Do not treat the 2002 comparison as validation metadata for a 1989 prediction.
- Do not derive `alpha_plus/minus` identifiers without carrying the source branch notation alongside them.
