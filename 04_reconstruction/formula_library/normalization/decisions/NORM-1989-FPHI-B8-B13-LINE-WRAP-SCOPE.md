# NORM-1989-FPHI-B8-B13-LINE-WRAP-SCOPE

Date: 2026-05-18

Decision ID resolved:

- `NORM-1989-FPHI-004`

## Decision

The line-wrap-sensitive scopes in `(B8)` and `(B13)` are normalized for implementation. This decision resolves only B8/B13 parenthesization. It does not resolve the B50 double-minus sign anomaly.

## B8 Normalized Scope

```text
ln((N_3*k)/2) =
  (k - 1)
  * (
      1
      - pi
        * ((1 - eta_q_k) / (1 + sqrt(eta_q_1)))
        * (
            1
            - u
              * (eta_q_1 / theta_q_1)
              * (1 - alpha_minus_1989 / alpha_plus_1989)
              * (1 - sqrt(eta))^2
          )
    )
  - (2 / (3*pi*e_base))
    * (1 - sqrt(eta))^2
    * (
        ((6*pi^2*e_base^2) / vartheta)
        * ((1 + sqrt(eta_q_1)) / (1 - eta))
        - 1
      )
```

## B13 Normalized Scope

```text
N_6 =
  ((2*k) / (pi*e_base*vartheta))
  * (
      sqrt(k)
      * (k^2 - 1)
      * (N_of_k / sqrt(eta_1_k))
      * (
          q
          - (1 - q)
            * (N_prime_of_k / (Q_n * sqrt(eta_1_k)))
        )
      + (-1)^(k + 1)
    )
  * eta
  * (1 - alpha_minus_1989 / alpha_plus_1989)
  * (4 * ((1 - sqrt(eta)) / (1 + sqrt(eta))))^2
  * Q_sigma
```

The leading `4` in `(B13)` is inside the squared factor and is not optional.

## Residual Risks Outside This Decision

- The B8 glyph `u` remains source-visible `u`; do not silently normalize it to `nu`.
- `eta_q_k`, `eta_q_1`, `eta_1_k`, `theta_q_1`, `N_of_k`, and `N_prime_of_k` follow `NORM-1989-FPHI-NAMING`.
- The alpha branch names are versioned by `NORM-1989-ALPHA-BRANCH-ALIASES`.
- B49 scope is resolved by `NORM-1989-FPHI-B49-SCOPE`.
- BUW product scope is resolved by `NORM-1989-FPHI-BUW-PRODUCT-SCOPE`.
- B50 sign remains blocked by `NORM-1989-FPHI-B50-DOUBLE-MINUS-BLOCKER`.

## Trace Requirements

Any future implementation of `(B8)` or `(B13)` must record:

```text
decision_id = NORM-1989-FPHI-004
source_image = 07_outputs/source_check_images/1989_erweiterte_massenformel/page-03.png
source_record = HT-F-1989-FPHI
```

## Critic Check

A read-only Critic check accepted B8 and B13 as fully parenthesizable from the page-03 image and existing Critic transcription. It confirmed that B13's trailing `eta(1 - alpha_-/alpha_+) ... Q_sigma` multiplier is outside the square bracket after `(-1)^(k+1)`.
