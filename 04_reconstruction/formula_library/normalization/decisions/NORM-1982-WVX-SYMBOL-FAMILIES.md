# NORM-1982-WVX-SYMBOL-FAMILIES

Date: 2026-05-15

Update 2026-09-06: `NORM-N0-ELECTRON-AUDIT` supplies the later explicit
H006-only nu/x alias decision. Its source-context correction supersedes
the no-cross-record-alias restriction below, not other symbol boundaries.

Decision ID resolved:

- `NORM-1982-WVX-002`

## Decision

The new symbols introduced by the 1982 `SELECTION-WVX` record are registered as symbol families before implementation:

```text
w_nu_x_family: w_nu_x, w(1), w(2), w_nu_x(k)
a_nu_x_family: a_nu_x, a_n, a_q
b_nu_x_family: b_nu_x
A_matrix: A_rs for r,s in 1..6
constants: xi, e_base, beta
```

This is a registration and naming decision only.

## Rules

- Implement `A_rs` slash scopes only through `NORM-1982-WVX-A-MATRIX-SLASH-BINDING`.
- Treat `A_rs` as a nonsymmetric real matrix family.
- Keep source-local `eta_qk` routed through `NORM-1982-ETA-INDEX`.
- Do not infer missing multiplication or division scopes from the symbol registration.
- Do not silently alias WVX `nu_x` families to page-8/page-9 `vx` families; cross-record scoping is governed by `NORM-1982-SELECTION-VX-NUX-SCOPING`.
