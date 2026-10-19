# H004 mass-chain source review — 2026-09-07

## Result

The 1996 H004 text gives a locally explicit route from the scale in (97),
through the configuration functions in (98d,e), to the rearranged spectral
formula (112).  The displayed identity

```text
4 sum_(j=1)^4 alpha_j G_j = K + F + H
```

is an exact polynomial regrouping of the printed definitions, conditional on
the stated substitutions.  It does **not** derive the empirical function
`F_S`, establish the selection rule (108), or validate a physical mass
prediction.

H004 itself says that the description is not complete after (98e), and later
states that `F_S` is initially to be found empirically from assigned measured
masses.  Thus the source supports an algebraic mass-formula chain, not a
source-complete, parameter-free calculation.

## Sources and visual scope

Primary source: *Elementarstrukturen der Materie 2* (1996), local H004 PDF,
SHA-256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
The following complete pages were visually read:

| Printed page | PDF folio | Role | Image inspected |
|---|---:|---|---|
| 253 | 259 | (97), mass scale | `tmp/pdfs/mass_chain/edm2-259.png` |
| 275–279 | 281–285 | immediate context; (98b–e) | `tmp/pdfs/alpha3_book_origin/edm2-281.png`, `...-282.png`, `...-283.png`, `...-284.png`, `tmp/pdfs/mass_chain/edm2-285.png` |
| 342–344 | 348–350 | empirical `F_S`, (111), (112) | `tmp/pdfs/eq108_status/edm2-348.png`, `...-349.png`, `tmp/pdfs/eq108_status/edm2-350.png`, `tmp/pdfs/mass_chain/edm2-350.png` |

PDF folios are the PDF viewer's one-based page numbers; printed pagination is
the source pagination.  No claim is made here about uninspected parts of H004.

## Printed definitions and formula chain

### Scale and configuration variables

At printed p.253/PDF 259, (97) prints, among further terms,

```text
mu_± = 4 mu alpha_±,          mu_S = (1 - alpha_- / alpha_+) mu_+,
s_0 = 1 [m].
```

The nearby prose calls `eta` and `xi` pure numbers and introduces the partial
mass construction; this review does not infer an independent derivation of
the scale from that statement.

At printed p.277/PDF 283, (98b) defines the parenthesized configuration
quantities

```text
N_(j)(t) = n_j(t) + Q_j,       j <= 4,
```

and identifies the four configuration-zone labels with `(n,m,p,sigma)`.
These parenthesized `N_(j)` must not be conflated with the unparenthesized
coefficients `N1,N2,N3` introduced much later in (112b), nor with the
resonance label `N` in `M(N)`.

At printed p.278/PDF 284, (98d) is printed as

```text
M(c,d) = T;m = mu_+ [ sum_(j=1)^4 alpha_j G_j
                    + (1 - alpha_- / alpha_+) F_S
                    + q alpha_- / alpha_+ ].
```

The same page gives (98e):

```text
eta_j N_(j) = G_j,
4 G1 = N_(1)^2 (1 + N_(1))^2,
6 G2 = N_(2) (2 N_(2)^2 + 3 N_(2) + 1),
2 G3 = N_(3) (1 + N_(3)),
G4 = N_(4),
eta_1 >= eta_2 >= eta_3 >= eta_4 = 1.
```

The leading glyph in the first line is visibly `eta_j`, not a silently
substituted delta/partial symbol.  On the same page, (98c) supplies in
particular `alpha_4 = 1` and the preceding alpha definitions used below.
Immediately after (98e), the text says the description is by no means
complete and calls for a selection rule for the zone occupancies.

### `F_S`, phi, and the later spectral form

Printed p.342/PDF 348 first recovers `n_j = N_(j) - Q_j`, then says `G_j` can
be determined from (98d,e).  It describes `F_S` as initially empirically
determinable from assigned measured component masses.  The displayed
relation is

```text
mu_S F_S = M_emp - mu_+ [ sum_j alpha_j G_j + q alpha_- / alpha_+ ],
mu_S = mu_+ (1 - alpha_- / alpha_+).
```

The text limits the stated empirical assignment to components `v=1` through
`v=10`, excluding `e_0` in `v=2`, and discusses 17 measurement points.
That is a source-reported fitting/assignment role, not a new audit fit.

Printed p.343/PDF 349 defines the aggregate `phi` in (111):

```text
phi = A_nu F_1 F_q F_kappa / F_2 + B_nu (P + Q)
      + 4 q alpha_- / alpha_+.
```

The page gives the detailed factors in (111a,b), including the displayed
uncertainty factors.  This review records the visible aggregate only; it does
not equate its factors with independently reconstructed functions from other
editions.

### Targeted `B_nu` reading across pp.342–343

On renewed high-resolution comparison, the final displayed constant on
printed p.342/PDF 348 reads

```text
B_nu = (1 - alpha_- / alpha_+)^2 alpha xi^(-2).
```

The mark initially read as a superscript `kappa` is the upper stroke of the
base `xi`, as comparison with the other `xi` glyphs on the same page shows;
the superscript itself consists of `-2`.  On the next page, printed
p.343/PDF 349, (111b) reads

```text
xi^2 B_nu = alpha (1 - alpha_- / alpha_+)^2 Y_44.
```

This review does not infer a relation between the two displayed lines or
between `Y_44` and any other factor.  High-resolution check images:
`tmp/pdfs/mass_chain/edm2-high-348.png` and `...-349.png` (detail:
`tmp/pdfs/mass_chain/bnu-detail-1600.png`).

The prose immediately below (111) uses (97), multiplies the bracket in (98d)
by four, and writes

```text
4 (1 - alpha_- / alpha_+) F_S + 4 q alpha_- / alpha_+ = phi.
```

It then introduces the *unparenthesized* coefficients

```text
N1 = alpha_1,       3 N2 = 2 alpha_2,       N3 = 2 alpha_3,
```

and states the three-way regrouping.  These `N1,N2,N3` are coefficient names
in (112b), not the occupations `N_(j)` of (98b,e).

Printed p.344/PDF 350 gives the components explicitly:

```text
K = N1 Q1^2(1+Q1)^2
  + N2 Q2(2Q2^2+3Q2+1)
  + N3 Q3(1+Q3) + 4Q4,

F = N1 n1^2(1+n1)^2
  + N2 n2(2n2^2+3n2+1)
  + N3 n3(1+n3) + 4n4,

H = 2 n1 Q1 [1+3(n1+Q1+n1Q1)+2(n1^2+Q1^2)] N1
  + 6 n2 Q2(1+n2+Q2) N2 + 2n3Q3N3,

M(N) = mu alpha_+ (K+F+H+phi).                 (112)
```

The page repeats (112b), `N1=alpha_1`, `3N2=2alpha_2`, `N3=2alpha_3`, and
says the alphas are given in (98c).  It presents (112) as the ensuing
spectral function in the context of (108)–(111b); that contextual claim is
not independently verified here.

## Independent local algebra check

With `X_j=N_(j)=n_j+Q_j` from (98b), the printed (98e) and (112b) give:

* `4 alpha_1 G1 = N1 X1^2(1+X1)^2`;
* `4 alpha_2 G2 = N2 X2(2X2^2+3X2+1)`;
* `4 alpha_3 G3 = N3 X3(1+X3)`;
* `4 alpha_4 G4 = 4(n4+Q4)`, using printed `alpha_4=1`.

Expanding each first three polynomial in `n_j+Q_j` produces respectively the
printed pure-`Q` terms `K`, pure-`n` terms `F`, and the displayed mixed terms
`H`; the fourth term splits directly.  Hence the source's
`4 sum alpha_jG_j = K+F+H` is an algebraic identity under the displayed
definitions.  This check establishes neither a derivation of the selections
nor an empirical adequacy claim.

### Targeted glyph check: `3Q2`, not `2Q2`

The high-resolution p.344/PDF 350 image was inspected specifically because a
lower-resolution reading suggested a possible `+2Q2` in (112a).  Both
occurrences of the `K` factor — the preceding displayed `K` expression and
the `K` term in (112a) — visibly read `2 Q2^2 + 3 Q2 + 1`.  This agrees with
the p.278/PDF 284 (98e) factor
`2 N_(2)^2 + 3 N_(2) + 1`.  The `+2Q2` alternative is therefore a rejected
reading hypothesis, not evidence for a second printed form or an erratum.

## Limits

* The labels `F`, `G`, and `H` occur in different local roles: `G_j` are the
  functions in (98e), while capital `F,H` in (112a) are the grouped parts of
  their expansion.  This review does not identify them beyond the printed
  equations.
* The source-supported algebra does not remove the source's explicit
  empirical role for `F_S`, nor supply a checked tolerance/projection for the
  selection relation (108).
* No numerical mass, calibration, choice of uncertainty factor, or modern
  empirical comparison has been performed.
