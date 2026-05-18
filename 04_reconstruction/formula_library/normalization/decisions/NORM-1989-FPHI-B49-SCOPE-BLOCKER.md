# NORM-1989-FPHI-B49-SCOPE-BLOCKER

Date: 2026-05-15

Last updated: 2026-05-18

Decision ID triaged:

- `NORM-1989-FPHI-001`

## Triage Result

Historical blocker note. `NORM-1989-FPHI-001` is now resolved by `NORM-1989-FPHI-B49-SCOPE.md`; this file preserves the path that led to that resolution.

The outer additive and multiplicative structure of `(B49)` can be documented. The repeated lifetime-section source form narrows the compact factor:

- the repeated source form supports the compact factor as denominator-product `kappa(1-q)/(2*alpha*vartheta)`;
- the final stacked `(Q over 3)` factor before division by `alpha` is resolved by extending `NORM-STACKED-BINOMIAL` to FPHI parenthesized vertical stack notation.

The compact `BUW^{-1}_{N=0}` cluster was later resolved separately under `NORM-1989-FPHI-002`.

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
  * (1 + kappa_alpha_vartheta_B49_denominator_product_candidate)
  * (pi/e_base)^2
  * sqrt(eta_12)
  * (Q_m - Q_n)
```

```text
phi_B49_tail =
  (P + 1) * stacked_Q_over_3_B49_source / alpha
```

This decomposition is now the source-supported B49 scope. It is still not sufficient for numerical implementation because `BUW_N0_inverse_source_token` remains unresolved separately.

## Narrowed Inner Scopes

The source-visible compact factor:

```text
kappa(1-q)/2 alpha vartheta
```

was ambiguous in the first occurrence on `1989_erweiterte_massenformel/page-03.png`. The repeated occurrence on `page-08.png` line-wraps the same factor as:

```text
kappa*(1 - q)/(2*alpha*vartheta)
```

This makes the denominator-product parse the only currently source-supported candidate. It was still not an executable `phi_B49` default at this triage stage because the B49 tail and `BUW` dependency were unresolved then.

Preserve the left-associative alternative only as a regression variant:

```text
(kappa*(1 - q)/(2*alpha)) * vartheta
```

The final parenthesized stack is source-visible as an upper `Q` over lower `3`. It is normalized by `NORM-STACKED-BINOMIAL` as:

```text
choose(Q, 3)
```

## Rules

- Do not implement numeric `phi_B49` while `BUW_N0_inverse_source_token` remains unresolved.
- Do not expand `BUW_N0_inverse_source_token`; see `NORM-1989-FPHI-002`.
- Do not claim B49 is executable only because the compact kappa factor is narrowed.
- Keep the source-visible outer three-term structure available for future normalization.

## 2026-05-18 Source Recheck

`page-08.png` repeats `(B49)` in the lifetime section and supports the denominator-product parse for the compact kappa factor. The same repeated source also keeps the final stacked `(Q over 3)` form and the compact `BUW^{-1}_{N=0}` cluster. The stack is resolved by `NORM-STACKED-BINOMIAL`; BUW product scope is resolved separately by `NORM-1989-FPHI-BUW-PRODUCT-SCOPE`.

## Critic Check

Two earlier read-only Critic checks agreed that the outer B49 structure could be documented while preserving `BUW` as a separate blocker. The 2026-05-18 recheck adds the repeated B49 source and extends `NORM-STACKED-BINOMIAL`, so `NORM-1989-FPHI-001` is resolved by `NORM-1989-FPHI-B49-SCOPE.md`. BUW product scope was then resolved by `NORM-1989-FPHI-BUW-PRODUCT-SCOPE`; the remaining executable blocker is B50 sign selection under `NORM-1989-FPHI-003`.
