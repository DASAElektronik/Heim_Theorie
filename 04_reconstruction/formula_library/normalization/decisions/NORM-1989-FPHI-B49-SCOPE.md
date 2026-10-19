# NORM-1989-FPHI-B49-SCOPE

Date: 2026-05-18

Decision ID resolved:

- `NORM-1989-FPHI-001`

## Decision

Resolve B49 expression scope except for separately tracked dependencies.

The source-supported B49 decomposition is:

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
  * (fourth_root(2) - 4*B_1989_B28*U_B50/W_N0_1989)
```

```text
phi_B49_alpha_correction =
  P*(P - 2)^2
  * (1 + kappa*(1 - q)/(2*alpha*vartheta))
  * (pi/e_base)^2
  * sqrt(eta_12)
  * (Q_m - Q_n)
```

```text
phi_B49_tail =
  (P + 1) * choose(Q, 3) / alpha
```

This resolves the B49 scope decision. It does not make `phi_B49` executable while `U_B50` still has an unresolved sign anomaly.

## Evidence

- `1989_erweiterte_massenformel/page-03.png` gives the first B49 occurrence.
- `1989_erweiterte_massenformel/page-08.png` repeats B49 in the lifetime section.
- The repeated B49 line-wrap supports denominator-product scope for `kappa*(1 - q)/(2*alpha*vartheta)`.
- The B49 tail uses the same parenthesized vertical `(Q over 3)` notation normalized by `NORM-STACKED-BINOMIAL`.
- The same notation class repeats around B52/B53 on `page-08.png`, including `(P over 2)`, `(P over 3)`, and `(Q over 3)`.

## Rules

- Use denominator-product binding for the compact B49 kappa factor.
- Normalize B49 tail stack as `choose(Q, 3)`, not `Q/3`.
- Use `B_1989_B28 * U_B50 * reciprocal(W_N0_1989)` for the compact source cluster; see `NORM-1989-FPHI-002`.
- Do not use this decision to resolve the B50 sign anomaly; see `NORM-1989-FPHI-003`.
- Preserve left-associative `((kappa*(1 - q))/(2*alpha))*vartheta` only as an explicit regression variant.

## Residual Risk

The B49 expression still cannot be used for numerical implementation until the B50 sign anomaly inside `U_B50` is resolved. This decision removes the remaining B49 parenthesis and stack-scope ambiguity.
