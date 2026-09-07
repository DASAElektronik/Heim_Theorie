# H004 selection/exhaustion procedure: source reconstruction

Stand: 2026-09-06. Bounded visual review of Heim, *Elementarstrukturen der
Materie II* (1996 edition), local file
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`,
SHA-256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
The principal scope was printed pp. 340--342 / PDF pp. 346--348, visually
read at `tmp/pdfs/book_selection_source/edm2-346.png` through `edm2-348.png`.
The necessary source anchors were read in full: (107), printed 321 / PDF 327
(`edm2-327.png`); (107a), 328 / 334 (`edm2-334.png`); and (108)/(108a),
330 / 336 (`edm2-336.png`). Immediate context printed 322--327 / PDF
328--333 was also read (`edm2-328.png` through `edm2-333.png`). OCR served
only as a locator. No mass or F_S calculation, and no H006 constants or
normalisation were used.

## Result

The book does give an ordered, conditional exhaustion procedure for the
four `N_(j)` values. It states a truncation convention with a special case
whose measurement threshold remains unspecified, and a special `j=3 -> j=4`
transfer. It does **not** fully specify the bounds of the transfer sum or an
iteration/re-logarithmisation rule after transfer; those cannot be silently
filled in by an implementation.

## 1. Inputs and structure conditions

Equation (107), printed 321 / PDF 327, gives the structure relations

```text
delta_j G_j > G_(j+1),        delta_j G_j >= delta_(j+1) G_(j+1),
```

with `j` only up to 3. The text says the occupancy of a zone is thereby
governed by zone 1. Equation (107a), printed 328 / PDF 334, adds for
`j>1` the bandwidth and range conditions, including

```text
beta_j = delta_(j-1) G_(j-1) - G_j >= 1,
beta_j = 0, G_j = 0  ->  n_(j-1) -> 1+n_(j-1),
-Q_j <= n_j <= L_j < infinity.
```

Here `beta_4` is this bandwidth symbol, not the earlier coupling `beta`.
The prose explains that the boundary condition is what excludes a transfer
that would leave the source zone negative.

For the V6 point, (108) / printed 330 / PDF 336 gives

```text
alpha_1 N_(1)^3 + alpha_2 N_(2)^2 + alpha_3 N_(3)
 + exp[-(2k-1)N_(4)/(3Q_4)] = W(vx) [1+f(N)],
W(vx)=g(k,q) w(vx).
```

The same page requires `f(N>=0)>=0`, `delta_N f>0`, integral unit steps
in `N`, a finite upper `L_N`, real `w`, and source-underlined `w_k(n_j=0)=0`.
It calls `w`'s displayed decomposition a heuristic ansatz.

On printed 340 / PDF 346, the author says (108)--(110d) permit numerical
determination of `W`, `a`, and `b` for each V6 point and `N>=0`. The visible
exhaustion instructions take `W_1 = W[1+f]` as their quantity to allocate.
They do not use `a` or `b` as separate operands in the printed steps on
340--342; their independent input status and construction remain in the
referenced equations, outside this bounded algorithm transcription.

## 2. Ordered exhaustion through N_(3)

Printed 340--341 / PDF 346--347 first states that the positive integers are
raised to the maximal `N_(1)` for which

```text
alpha_1 N_(1)^3 <= W_1,
alpha_1 (N_(1)+1)^3 > W_1,
W_2 = W_1 - alpha_1 N_(1)^3.
```

The same procedure is repeated for `j=2`, using
`alpha_2 N_(2)^2 <= W_2`, then

```text
W_3 = W_2 - alpha_2 N_(2)^2.
```

It is repeated for `j=3`, using `alpha_3 N_(3) <= W_3`, then

```text
W_4 = W_3 - alpha_3 N_(3).
```

This is an explicit order `N_(1)`, then `N_(2)`, then `N_(3)`, with a
residual after each allocation. It is not a source statement that an
arbitrary simultaneous solution would produce the same tuple.

The printed alternatives are `0 <= W_4 <= 1`, or
`1 < W_4 < (alpha_3 N_(3))_max`, the latter stated as possible for `k=2`
because `alpha_3>1`.

## 3. TRC and determination of N_(4)

The source defines `TRC` on printed 341 / PDF 347 as cutting decimal places,
not rounding. Its special exception is a displayed `0.99...99` through a
decimal place `x` below the measurement threshold: `TRC(0.99...99)=1`.
The explicit contrasting example is `TRC(e)=2`. No general binary floating
point or precision policy is stated.

For `N_(4)`, the page says to logarithmise `W_4` in the form

```text
(2k-1) W_5 = -3 Q_4 ln W_4.
```

If `W_4=0`, this gives the cited divergence `W_5 -> infinity`. If that
holds, or if `W_5 > alpha_3 N_(3)`, the text calls for the maximal zone-4
occupancy

```text
N_(4) = TRC(alpha_3 N_(3)).
```

Only if additionally `TRC(alpha_3 N_(3)) > alpha_3 N_(3)` is the
`beta_4=1` condition of (107a) applied in the displayed form
`N_(4)=TRC(alpha_3 N_(3))-1`. Conversely, for
`W_5 <= alpha_3 N_(3)`, the instruction is `N_(4)=TRC(W_5)`.

## 4. k=2 negative-W_5 transfer

The book says that for `k=2`, `W_5<0` is additionally possible. If zone 3
is then occupied with `N'_(3)`, it permits a Protosimplex transfer **only**
from `j=3` to `j=4`, because `G_4` and `delta_3 G_3=alpha_3 N'_(3)` share
the cited linear character. Its displayed stopping notation is

```text
W_6 = W_5 + alpha_3 sum_mu (N'_(3)+1-mu) >= 0,
N_(3) = N'_(3)-mu,
W_6 <= alpha_3 N_(3).
```

The prose says that in general `mu=1` is sufficient to reach `W_6>=0`.
But the printed sigma has no numerical lower or upper bound beyond its
visible `mu` marker. It also does not say to reapply the logarithm to `W_6`.
Therefore neither a closed triangular-sum formula nor a new `W_5` after
transfer is a source-established step.

Where the stated `W_4>1` condition applies, it then sets
`N_(4)=TRC(W_6)`, provided the transfer leaves `N_(3)>=0`. A transfer that
would make `N_(3)<0` while requiring `N_(4)>=0` is labelled a forbidden,
nonexistent c- or d-term. The following printed p. 342 / PDF 348 says an
analogous `j=2 -> j=3` or `j=1 -> j=2` transfer is impossible because the
relevant `G_3`/`G_2` terms contain lower-degree summands as well. No other
conserved quantity is named in this local rule.

## 5. A16 and feedback boundary

Within H004, the earlier visible chain is `A16 -> w -> W=g*w`: (109a),
printed 334 / PDF 340, contains the `kappa*Q*eta_qk*A16` contribution to
the shifted structural term, while (108) makes `W` proportional to `w`.
Together with p. 340's `W_1=W[1+f]`, this supports the **forward**
dependency

```text
A16 -> w -> W -> W_1 -> ordered N_(1),N_(2),N_(3),N_(4) selection.
```

Pages 340--342 do not name `A16`, do not solve it back from an exhausted
quadruple, and do not state a fixed-point or feedback rule. Hence a reverse
inference from the selected `N_(j)` to A16 would be an additional analysis,
not this book algorithm. The later empirical F_S discussion beginning on
p. 342 was deliberately not used as a substitute.

## Scope limits

The report records the book's explicit procedure and gaps only. It makes no
claim that its input functions have been independently derived, that all
branches have been implemented, or that the selection is unique beyond the
stated conditional, ordered procedure.
