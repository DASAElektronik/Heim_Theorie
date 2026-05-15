# NORM-1989-MASS-B4-DEPENDENCY-SCOPE

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-MASS-001`

## Decision

For `HT-F-1989-MASS`, the adjacent `(B4)` alpha-constant line is a dependency boundary, not part of the normalized mass-formula body.

The 1989 mass implementation may consume versioned alpha branch inputs:

```text
alpha_plus_1989
alpha_minus_1989
```

The normalized 1989 mass model remains:

```text
M_1989 =
  mu_1989 * alpha_plus_1989 *
  ((G_1989 + S_1989 + F_1989 + Phi_1989) + 4*q*alpha_minus_1989)
```

`HT-F-1989-MASS` must not compute or inline `(B4)`.

## B4 Source Context

The source-visible `(B4)` line defines alpha constants in the mass section:

```text
alpha_plus_B4_source =
  eta^(1/6) / eta^2 *
  (1 - vartheta * [2*(1 - sqrt(eta)) / (eta*(1 + sqrt(eta)))]^2 * sqrt(2*eta))
  - 1

alpha_minus_B4_source =
  (alpha_plus_B4_source + 1) * eta - 1
```

This source-context transcription is not an executable default for the mass record.

## Delegated Alpha Work

Executable alpha-branch computation remains delegated to the 1989 alpha normalization work:

```text
NORM-1989-ALPHA-001
HT-F-1989-ALPHA
```

That work must decide how `(B4)` relates to the later `(B58)` to `(B62)` exact fine-structure constant chain before any code computes `alpha_plus_1989` or `alpha_minus_1989`.

## Rules

- Do not fold `(B4)` into the normalized `(B3)` mass formula.
- Do not use unversioned `alpha_plus` or `alpha_minus` in implementation code.
- Do not use `(B4)` source context to bypass the unresolved `(B59)`/`K_alpha` scope in `NORM-1989-ALPHA-001`.
- Do not use the `(B62)` numeric values as proof that `(B4)` or `(B59)` implementation scope is solved.
- Keep 1982 alpha branch, 1982 mass alpha, and 1989 alpha branch symbols separate.

## Critic Check

A read-only Critic check accepted this narrow resolution: `NORM-1989-MASS-001` is resolved only as a mass-record dependency boundary. B4 numeric evaluation and the exact alpha-chain normalization remain blocked under `NORM-1989-ALPHA-001`.
