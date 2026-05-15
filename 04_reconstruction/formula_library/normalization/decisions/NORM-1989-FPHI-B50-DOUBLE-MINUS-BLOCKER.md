# NORM-1989-FPHI-B50-DOUBLE-MINUS-BLOCKER

Date: 2026-05-15

Decision ID triaged:

- `NORM-1989-FPHI-003`

## Triage Result

Do not mark `NORM-1989-FPHI-003` resolved.

The visible double minus in `(B50)` is source-present and must not be normalized away during cleanup.

The `+` before the `(k - 1)` group can be treated as a continuation operator, but the source-visible:

```text
P + 2Q -- 4*pi(P - Q)(1 - q)/fourth_root(2)
```

appears inside the same printed brace group. It is not explained by a duplicated line-wrap plus/minus.

## Source-Preserving Form

The safe transcription form remains:

```text
U =
  2^Z * [
    P^2
    + (3/2)*(P - Q)
    + P*(1 - q)
    + 4*kappa*B*(1 - Q)/(3 - 2*q)
    + (k - 1) * {
        P + 2*Q
        -- 4*pi*(P - Q)*(1 - q)/fourth_root(2)
      }
  ] * eta_qk^(-2)
```

This is not an executable sign decision. It preserves the source anomaly.

## Variants To Preserve

Future model work may test explicit variants, but none is the source-default implementation:

```text
b50_double_minus_source_literal
b50_single_minus_typo_candidate
b50_double_negative_candidate
```

Only `b50_double_minus_source_literal` is source-checked.

## Rules

- Do not rewrite `-- 4*pi...` to `- 4*pi...` without an explicit typo/emendation decision.
- Do not rewrite `-- 4*pi...` to `+ 4*pi...` by ordinary programming-language double-negative rules.
- Keep the source image and extracted-text traces attached to any future numeric variant.
- Do not use downstream fit quality to choose the sign.

## Critic Check

A read-only Critic check confirmed that the B50 double minus appears in the same printed source line, unlike the harmless duplicated continuation plus before the `(k - 1)` group. It recommended keeping `NORM-1989-FPHI-003` blocked and preserving single-minus and double-negative variants only as explicit future model candidates.
