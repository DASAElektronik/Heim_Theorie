# NORM-1982-N-GAMMA-QN-BLOCKER

Date: 2026-05-15

Decision ID triaged:

- `NORM-1982-N-003`

## Triage

The source states that relations involving `n_j`, `F(Gamma)`, full bandwidths `Gamma`, and `Q_N = Q(N)` are needed. The source-checked material does not provide an implementation rule for that resonance/bandwidth relation.

`NORM-1982-SELECTION-QN-Q0-SCOPING` separately resolves the page-9 algorithm convention: use `Q_base_1982 = Q(0)` of `x_v` for numerical tuple enumeration. That decision does not define `Q_N_1982 = Q(N)`.

This item is therefore still blocked until the Gamma/Q_N relation is extracted and normalized in a dedicated Gamma worksheet.

## Rules

- Do not implement resonance-order filtering from this relation yet.
- Do not infer `Q_N_1982 = Q_base_1982`.
- Do not infer a Gamma bandwidth formula from later output tables.
- Resolve with a dedicated Gamma worksheet.
