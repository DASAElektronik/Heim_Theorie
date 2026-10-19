# NORM-1982-SELECTION-VX-NUX-SCOPING

Date: 2026-05-15

## Later correction, 2026-09-06

The full-page H006 context establishes one Greek-nu/x family: p3 defines
the multiplet number nu, p6 connects W_(nu,x)=g*w_(nu,x) to component x,
and p8/p9 continue the same state. Our earlier Latin-v reading below was
incorrect. The explicit H006-only mapping is now authorized in
`04_reconstruction/alpha_audit/NORM-N0-ELECTRON-AUDIT.md`, with evidence
in `reviews/N0_ALIAS_REVIEW_2026-09-06.md` under that audit directory.
Only the cross-record alias restriction is superseded. Multiplet and
component indices, Q(0)/Q(N), and all cross-edition boundaries remain.
The historical decision text is preserved below for traceability.

Decision ID resolved:

- `NORM-1982-N-001`

## Decision

The 1982 selection records use source-local notation. Do not project-wide harmonize `nu_x` and `vx`.

Preserve these source-checked families:

```text
HT-F-1982-SELECTION:
  W_nu_x, a_nu_x, b_nu_x, w_nu_x

HT-F-1982-SELECTION-WVX:
  w_nu_x, w_nu_x(k), a_nu_x, b_nu_x

HT-F-1982-SELECTION-N:
  W_vx, a_vx, b_vx, x_vx, M_0(vx), M_N(vx), x_v

HT-F-1982-SELECTION-ALGO:
  Q = Q(0) of x_v
  W_vx, a_vx, b_vx, Phi_vx, x_vx, M_N(vx)
```

## Cross-Record Rule

These notations may be related semantically, but this decision does not assert equivalence.

Implementations must not silently join `W_nu_x` with `W_vx`, or `a_nu_x`/`b_nu_x` with `a_vx`/`b_vx`. Any cross-record alias map must be introduced by a later explicit decision.

## Source Basis

The page-8 high-resolution resolver accepted Latin `vx` for the `HT-F-1982-SELECTION-N` block. The page-9 algorithm record preserves `x_v` for the `Q=Q(0)` state and later `vx`/`x_vx` forms. The earlier core and WVX records retain their source `nu_x` family.

## Remaining Boundaries

This decision resolves only the glyph/convention blocker. It does not resolve:

- doubled `+ + exp[...]` in `(XXIX)`;
- Gamma/Q_N relation;
- `Q_N = Q(N)` versus `Q = Q(0)`;
- `K_j` integer/decimal-place policy;
- `W_4` branch behavior.

## Critic Check

A read-only Critic check accepted this scoped source-alias policy and warned against implicit cross-record joining.
