# NORM-1982-WVX-A-MATRIX-SLASH-BINDING

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-WVX-001`

## Decision

The 1982 `SELECTION-WVX` A-matrix source transcription remains source-literal. For implementation normalization, compact slash expressions in the A-matrix use denominator-product binding when a division slash is followed by an adjacent product of constants or symbols.

Default normalized forms for the previously blocking rows:

```text
A16 = (pi*e)^2 * (1 + alpha*(1 + 6*alpha/pi)/(5*eta))
A24 = 2*xi^2/(3*eta)
A35 = 3*alpha/(e*xi^2)
A46 = pi*e/(xi*eta) - e*eta^2*alpha/2
A64 = pi/(3*eta)
A65 = pi/(3*xi)
```

Same-pattern adjacent A-matrix rows use the same rule:

```text
A11 = (xi^2*pi*e)^2*(1 - 4*pi*alpha^2)/(2*eta^2)
A21 = 2*(e*alpha/(2*eta))^2*(1 - alpha/(2*xi^2))
A26 = 2*(1 - pi*(e*xi*alpha)^2*sqrt(eta)/2)/(e*xi^2)
A45 = (3*beta - alpha)/(6*xi)
A61 = pi*xi*(2*beta - alpha)/(12*beta)
```

`A14` is already bracketed by the transcription and keeps its explicit outer division by `alpha`. Its inner compact denominator group is normalized as:

```text
((1 + sqrt(eta))^2 * 4*xi)
```

## Source-Literal Scope

This decision does not rewrite the formula record. It only provides the implementation parentheses for rows that were transcribed from dense inline slash notation.

Every implementation of these A-matrix rows must trace to this decision ID and must keep the source literal available for audit.

## Variants To Preserve

Left-associative slash parses are not defaults, but they remain explicit regression variants:

```text
A16_left_assoc = (pi*e)^2 * (1 + (alpha*(1 + 6*alpha/pi)/5)*eta)
A24_left_assoc = (2*xi^2/3)*eta
A35_left_assoc = (3*alpha/e)*xi^2
A46_left_assoc = (pi*e/xi)*eta - e*eta^2*alpha/2
A64_left_assoc = (pi/3)*eta
A65_left_assoc = (pi/3)*xi
A45_left_assoc = ((3*beta - alpha)/6)*xi
A61_left_assoc = (pi*xi*(2*beta - alpha)/12)*beta
```

Do not silently select a left-associative variant because it improves a numerical fit.

## Rules

- Preserve the source-checked transcription exactly in `HT-F-1982-SELECTION-WVX`.
- Use denominator-product binding for compact slash expressions in A-matrix implementation code.
- Treat this as an implementation normalization rule only, not as proof that the source printed an explicit fraction bar.
- Keep `e` routed through the registered `e_base` symbol in implementation code.
- Keep `eta_qk` routing governed by `NORM-1982-ETA-INDEX`; this decision only covers A-matrix slash binding.

## Critic Check

A read-only Critic check accepted denominator-product binding as the conservative implementation default for `A16`, `A24`, `A35`, `A46`, `A64`, `A65`, and same-pattern adjacent A rows. The Critic explicitly warned to preserve source-literal and left-associative variants for regression checks.
