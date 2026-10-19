# Energy ordering: conditional mathematics review

Date: 2026-09-06. Scope: independent algebra applied to source equations
supplied by the principal reviewer. This review did not inspect the source
page images or verify their glyphs. It performs no modern-data comparison
and makes no physical-validation claim.

## Supplied source statements

EDM2 printed page 299 was reported to state

```text
W <= X <= V
0 <= E <= E_k.
```

Printed page 300 was reported to state

```text
-E_k = integral from W to V of dX = V-W = V(1-C)
W = VC
V < 0.
```

The interpretation below is conditional on those transcriptions. It does
not establish whether any discrepancy originated with the author, typesetter,
edition, or transcription.

## Algebraic finding

The first ordering requires `W<=V`, hence `V-W>=0`. The energy bounds
require `E_k>=0`, hence `-E_k<=0`. Their equality therefore permits only

```text
E_k = 0
W = V
X = W = V.
```

The supplied energy bounds also force `E=0`. Since `V<0`, the additional
relation `W=VC` then forces `C=1`. Consequently the statements are
inconsistent for a nontrivial positive `E_k`. If a strict `0<C<1` is also
required, even the degenerate case is excluded.

## Explicit correction candidate

Replacing only the ordering by

```text
V <= X <= W
```

is algebraically consistent with `V<0`, `W=VC`, and `0<C<1`, because

```text
V < W < 0
V-W = V(1-C) < 0
E_k = W-V = -V(1-C) > 0.
```

The original oriented integral from `W` to `V` is then negative, as required
by `-E_k`. No absolute value should silently replace this signed integral.

This is a local correction candidate for an explicitly authorized, separately
identified reconstruction version. It is not a verified reading of the
source and not established authorial intent. A change to the integral sign
or its limits is another algebraically conceivable repair; algebra alone
does not determine which source statement was intended. Canonical source
transcriptions must remain distinguishable from any adopted correction.

## Conditional consequence for equation (105)

The ordering correction leaves `-E_k=V-W=V(1-C)` and
`E_k=-V(1-C)` unchanged. Thus it leaves equation (105) unchanged if the
subsequent derivation uses only these unchanged relations and does not use
the original ordering elsewhere. This review has not independently traced
every later derivation step, so invariance of (105) is conditional rather
than an unrestricted conclusion.

Resolving this sign/order inconsistency would establish local algebraic
consistency only. It would not prove the underlying energy assumptions,
the subsequent spectrum construction, or the physical validity of (105).

Only this review file was created; no canonical equation, source record,
implementation, or Git state was modified.
