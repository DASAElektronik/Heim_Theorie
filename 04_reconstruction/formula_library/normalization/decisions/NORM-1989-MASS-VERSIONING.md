# NORM-1989-MASS-VERSIONING

Date: 2026-05-15

Decision ID resolved:

- `NORM-1989-MASS-002`

## Decision

The 1982 and 1989 mass formulas are separate model versions:

```text
model_1982_from_text:
  M = mu_mass_element_1982 * alpha_mass_plus_1982 * (K_aux_1982 + G_aux_1982 + H_aux_1982 + Phi_aux_1982)

model_1989_extension:
  M = mu * alpha_plus_1989 * [(G_1989 + S_1989 + F_1989 + Phi_1989) + 4*q*alpha_minus_1989]
```

## Rules

- Do not create an unversioned `M` implementation.
- Do not mix 1982 `K+G+H+Phi` with 1989 `G+S+F+Phi`.
- Do not import the 1989 `4*q*alpha_minus` term into the 1982 model.
- Source records keep the visible source notation; implementation code must declare the model version.
