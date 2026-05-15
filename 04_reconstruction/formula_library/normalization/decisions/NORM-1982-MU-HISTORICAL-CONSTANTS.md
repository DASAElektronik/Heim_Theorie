# NORM-1982-MU-HISTORICAL-CONSTANTS

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-MU-001`

## Decision

The constants printed in the 1982/IGW transcription define a versioned constants profile:

```text
constants_profile = model_1982_igw2003_printed
```

This profile is the default for reproducing the source-checked 1982 mass element `mu`.

## Rules

- Do not mix printed 1982 constants with modern CODATA values in one run.
- Modern constants may be used only in a separately named comparison profile.
- Numeric residual comparisons must record the constants profile used.
- `mu` remains the mass element, not the muon.

## Critic Scope

This resolves only constants provenance and versioning. It does not validate the numerical formula or modern residuals.
