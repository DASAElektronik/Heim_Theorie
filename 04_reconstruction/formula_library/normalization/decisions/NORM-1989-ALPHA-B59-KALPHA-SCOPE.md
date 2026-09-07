# NORM-1989-ALPHA-B59-KALPHA-SCOPE

Date: 2026-05-18

Decision ID resolved:

- `NORM-1989-ALPHA-001`

## Decision

The 1989 `(B59)` equality chain is implementation-ready when preserved as the full source-visible chain:

```text
1 - C_prime_1989 = 1 - eta_term_1989 = K_alpha_1989
```

with:

```text
eta_term_1989 =
  ((1 + eta_2_2) / (eta * eta_1_1 * eta_1_2))
  * ((1 - sqrt(eta)) / (1 + sqrt(eta)))^2
```

Therefore:

```text
C_prime_1989 = eta_term_1989
K_alpha_1989 = 1 - C_prime_1989
K_alpha_1989 = 1 - eta_term_1989
C_prime_1989 = 1 - K_alpha_1989
```

The old shortcut:

```text
1 - C_prime = 1 - K_alpha
```

is rejected as structurally wrong.

## Downstream Scope

For `(B61)`, `K_alpha_1989` is the whole `1 - C_prime_1989` value:

```text
D_prime_1989 = (2*pi)^5 / (9 * vartheta * K_alpha_1989)
```

Do not substitute `eta_term_1989` directly for `K_alpha_1989`.

## Rules

- Preserve the source-visible chain `1 - C' = 1 - (...) = K_alpha`.
- Use `vartheta`, not an untracked `theta`, per `NORM-1989-ALPHA-VARTHETA-NAME`.
- Use model-scoped branch names `alpha_plus_1989` and `alpha_minus_1989` per `NORM-1989-ALPHA-BRANCH-ALIASES`.
- Preserve source branch notation `alpha_(+)` and `alpha_(-)` in source-facing records.
- Keep the 2002 comparison line as source context only, not formula-core validation.
- Treat comma-style eta subscripts as source-visible `eta_2_2`, `eta_1_1`, and `eta_1_2`.

## Rejected Variant

Keep this only as a historical bad-normalization regression check:

```text
bad_shortcut_1989_alpha_b59 = "1 - C_prime = 1 - K_alpha"
```

An implementation must fail review if it uses that shortcut.

## Critic Check

A read-only Critic check accepted the full-chain normalization and confirmed that `K_alpha_1989` is the whole `1 - C_prime_1989` value. It also confirmed that `(B61)` uses `9 * vartheta * K_alpha_1989` in the denominator and that the 2002 comparison line is not part of the formula core.
