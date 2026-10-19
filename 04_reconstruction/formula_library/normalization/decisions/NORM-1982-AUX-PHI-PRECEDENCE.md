# NORM-1982-AUX-PHI-PRECEDENCE

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-AUX-001`

## Decision

The 1982 `Phi` expression is normalized as one multiplicative chain followed by two additive terms.

Source-visible structure:

```text
Phi =
  F1 * F2 * F3 * F4 * F5 * F6 * F7 * F8 * F9
  + A1
  + A2
```

where:

```text
F1 = 3P / (pi * sqrt(eta_qk))

F2 = 1 - alpha_minus / alpha_plus

F3 = (P + Q) * (-1)^(P + Q)

F4 = 1 - alpha/3 + (pi/2) * (k - 1) * 3^(1 - q/2)

F5 = 1 + [2*k*kappa/(3*eta^2)] * xi
       * [1 + xi^2*(P - Q)*(pi^2 - q)]

F6 = [1 + (4*xi*choose(P,2)/k) * (xi/6)^q]^(-1)

F7 = 2*sqrt(eta_11)*sqrt(eta_qk) + q*eta^2*(k - 1)

F8 = 1 + 4*pi*alpha/(eta*sqrt(eta))

F9 = 1 + Q*(1 - kappa)*(2 - k)*n_1/Q_1

A1 = 4*(1 - alpha_minus/alpha_plus)*alpha*(P + Q)/xi^2

A2 = 4*q*alpha_minus/alpha_plus
```

## Source-Scope Rules

- `F6` is the only factor carrying exponent `-1`.
- The exponent `-1` applies to the full bracket:

```text
[1 + (4*xi*choose(P,2)/k) * (xi/6)^q]^(-1)
```

- The final source factor is printed with mismatched delimiters:

```text
(1 + Q(1-kappa)(2-k)n_1/Q_1]
```

  Normalize this only as a delimiter-closure typo for that one factor:

```text
F9 = 1 + Q*(1-kappa)*(2-k)*n_1/Q_1
```

- The mismatched delimiter does not pull `A1` or `A2` into the multiplicative chain.
- The trailing additive terms are outside the product chain.

## What This Does Not Resolve

This decision does not itself resolve:

- the overload between `G_count` and the auxiliary `G` term;
- numerical validity of `Phi`;
- occupation-tuple selection rules for `n_j`;
- any 1989 `Phi` or self-coupling expression.

Symbol-role disambiguation for `P`, `Q`, `q`, `Q_j`, `kappa`, `alpha`, `alpha_plus`, and `alpha_minus` is covered by `NORM-1982-AUX-SYMBOL-ROLES`.

## Implementation Guardrails

- Do not implement `Phi` directly from raw OCR line 217.
- Do not flatten the `F6` inverse into only `(xi/6)^q` or only the final term inside the bracket.
- Do not move `A1` or `A2` inside the product chain.
- Implementations must reference this decision ID and `NORM-1982-AUX-SYMBOL-ROLES` before evaluating `Phi`.

## Critic Check

A read-only Critic check accepted this narrow precedence decision. A later read-only Critic check accepted `NORM-1982-AUX-SYMBOL-ROLES` as the paired symbol-role resolution.
