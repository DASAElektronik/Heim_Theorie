# NORM-1989-FPHI-B49-SCOPE-BLOCKER

Date: 2026-05-15

Decision ID triaged:

- `NORM-1989-FPHI-001`

## Triage Result

Do not mark `NORM-1989-FPHI-001` resolved yet.

The outer additive and multiplicative structure of `(B49)` can be documented, but two inner source scopes remain too ambiguous for an executable default:

- the compact factor `kappa(1-q)/2 alpha vartheta`;
- the final stacked `(Q over 3)` factor before division by `alpha`.

`BUW^{-1}_{N=0}` remains blocked separately under `NORM-1989-FPHI-002`.

## Non-Executable Decomposition

The source-visible `(B49)` self-coupling line can be held as:

```text
phi_B49_source =
  phi_B49_self_coupling
  + phi_B49_alpha_correction
  - phi_B49_tail
```

with:

```text
phi_B49_self_coupling =
  (N_4*p^2)/(1 + p^2)
  * (sigma + Q_sigma)/sqrt(1 + sigma^2)
  * (fourth_root(2) - 4*BUW_N0_inverse_source_token)
```

```text
phi_B49_alpha_correction =
  P*(P - 2)^2
  * (1 + kappa_alpha_vartheta_B49_source)
  * (pi/e_base)^2
  * sqrt(eta_12)
  * (Q_m - Q_n)
```

```text
phi_B49_tail =
  (P + 1) * stacked_Q_over_3_B49_source / alpha
```

This decomposition is audit structure only. It is not sufficient for numerical implementation.

## Unresolved Inner Scopes

The source-visible compact factor:

```text
kappa(1-q)/2 alpha vartheta
```

has at least two plausible implementation parses:

```text
(kappa*(1 - q)/(2*alpha)) * vartheta
kappa*(1 - q)/(2*alpha*vartheta)
```

Do not choose between them without additional source evidence or an explicit model-variant decision.

The final parenthesized stack is source-visible as an upper `Q` over lower `3`. Do not silently normalize it as quotient `Q/3`.

Possible future treatments:

```text
stacked_Q_over_3_B49_source
choose(Q, 3) if NORM-STACKED-BINOMIAL is explicitly extended to B49
choose(q, 3) only as an explicit small-glyph variant if later image evidence supports lowercase q
```

## Rules

- Do not implement numeric `phi_B49` from the current readable formula.
- Do not expand `BUW_N0_inverse_source_token`; see `NORM-1989-FPHI-002`.
- Do not normalize the B49 final stack as `Q/3`.
- Do not borrow the WVX A-matrix slash-binding default for `kappa(1-q)/2 alpha vartheta`; this is a separate 1989 FPHI scope problem.
- Keep the source-visible outer three-term structure available for future normalization.

## Critic Check

Two read-only Critic checks agreed that the outer B49 structure can be documented while preserving `BUW` as a separate blocker. The second check flagged `kappa(1-q)/2 alpha vartheta` and the final stacked `(Q over 3)` as unresolved enough to keep `NORM-1989-FPHI-001` blocked.
