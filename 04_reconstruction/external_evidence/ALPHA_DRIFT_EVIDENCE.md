# Alpha Drift External Evidence

Date: 2026-05-15

Scope:

- `HT-F-1982-ALPHA`
- `HT-F-1989-ALPHA`
- `NORM-1982-ALPHA-003`
- `NORM-1989-ALPHA-001`
- `NORM-1989-BRANCH-001`

## Current Local Baseline

The 1982 source-checked branch equation gives:

```text
source_transcription_variant:
  alpha_plus^-1  ~= 137.049188026668
  alpha_minus^-1 ~= 1.000026621616

printed_alpha_fit_variant:
  alpha_plus^-1  ~= 137.035960995197
  alpha_minus^-1 ~= 1.000026626755
```

The 1982 source prints:

```text
alpha_(+)^-1 = 137.03596147
alpha_(-)^-1 = 1.00001363
```

`NORM-1982-ALPHA-NEGATIVE-BRANCH` therefore treats the printed negative reciprocal as a source-literal residual, not as an implementation regression target.

## External Evidence Registered

### EXT-ALPHA-1989-001

The online 1989 extension reports a different alpha formulation and gives:

```text
alpha_plus  ~= 0.0072973525253328589
alpha_minus ~= 0.999985890199089

1/alpha_plus  ~= 137.03601
1/alpha_minus ~= 1.0000142
```

This is near the 1982 printed negative reciprocal, but it belongs to the 1989 formula generation. It must not be used to correct the 1982 source residual.

### EXT-ALPHA-1992-001

A secondary English overview states:

```text
better formula, 1992:
  alpha_plus  = 1/137.0360085
  alpha_minus = 1/1.000026627
```

The negative reciprocal is close to the value implied by the 1982 branch equation. This may explain a version drift, but the entry is only a research lead until the underlying 1992 source is found and source-checked.

## Interpretation

The alpha drift is likely a version/model drift, not an OCR-only drift:

- 1982 printed negative reciprocal: `1.00001363`
- 1989 reported negative reciprocal: `1.0000142`
- 1982 branch-equation-implied negative reciprocal: about `1.00002663`
- secondary 1992 reported negative reciprocal: `1.000026627`

The evidence supports keeping separate model versions. It does not justify merging the 1982, 1989, and claimed 1992 values.

## Guardrails

- Do not patch 1982 formulas from 1989 or 1992 claims.
- Do not use secondary online snippets as primary proof.
- Treat `EXT-ALPHA-1992-001` as a source-discovery task.
- Any future alpha implementation must declare its model version before choosing branch constants.
