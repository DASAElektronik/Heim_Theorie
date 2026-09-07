# H004 F16/A16: stated constraints, limits, and remaining freedom

Stand: 2026-09-06. Bounded visual source review of Burkhard Heim,
*Elementarstrukturen der Materie II* (1996 edition), local file
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`,
SHA-256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
OCR was used only as a locator. Visually read in full: printed pp. 330--335 /
PDF pp. 336--341 (`tmp/pdfs/a16_book/edm2-336.png` through `edm2-341.png`).
Targeted direct references were also read: (101a), printed 289 / PDF 295
(`tmp/pdfs/a16_book/ref101-295.png`); (101b), printed 291 / PDF 297
(`ref101-297.png`); and (105)/(105a), printed 302 / PDF 308
(`ref105-308.png`). The directly cited selection result (98a) was checked
at printed 269 / PDF 275 (`tmp/pdfs/f16_constraints/edm2-275.png`). No mass
calculation, fitted replacement function, or claim about the whole work is
made here.

## Result in one sentence

The book specifies a general metronic-function role and a finite asymptotic
limit for `F_im`, but gives no separate functional equation, finite-point
value, derivative, rate, or symmetry condition for `F16`; its displayed
`A16` is subsequently introduced as a heuristic numerical parametrisation
with `Y9`, not derived from those constraints.

## 1. What is explicitly defined

On printed p. 330 / PDF p. 336, in the discussion following (108), the text
calls the form of `w` a “heuristischer Ansatz”. It says that the
Strukturpotenz is determined by the quantum numbers of the V6 lattice points
in (101a) and by metronic R3 selector functions. The printed notation is
read here with its index range made explicit:

```text
F_im(mu_1, mu_2, mu_3) = phi_im;mu,  with s = 1,...,3.
```

That is, the superscript/range marking on the printed `F_im(mu_s)` denotes
the three R3 metron digits, not a third power. They represent the pertinent
`(+7)` structure in R3. The zero point of `mu_s` is said to be fixed by the
correlation centre of the internal condenser flows projected into R3. This
is a role and origin statement for the arguments; it does not state a
numerical value such as `F16(0)`.

For the pseudosinglet `(1111)_0(-1)`, printed p. 332 / PDF p. 338 gives the
specific occurrence

```text
X6 = kappa * eta_qk * F16,
underline(w1) = (1-Q) sum_(i=1)^5 X_i + Q*X6.
```

The surrounding text describes `X6` as a spinor contribution, with the
correction `V_QQ : V_ee = eta_qk`. Thus `F16` has a documented structural
role in this source-underlined `w1` component. The source supplies no extra
F16-only equation on this page.

## 2. Actual limit condition

Printed p. 331 / PDF p. 337 says explicitly that the form of `F_im` could
not yet be deduced, but that for diverging `mu_s` it must converge to
constant finite bounds. Printed p. 334 / PDF p. 340 states the displayed
limit more precisely, for the observable R3 environment beyond `j=3`:

```text
lim_(tau -> 0) F_im = lim_(mu -> infinity) phi_im;mu = A_im = const < infinity,
lim_(tau -> 0) F = A = const < infinity.
```

The text calls this a good approximation and qualifies its measurement-limit
claim on `A_im` and `A` having been correctly determined. It specifies no
convergence rate, uniformity condition, sign, monotonicity, differentiability,
finite-`mu` boundary value, or equation relating distinct matrix entries.

`F16` is naturally an indexed member of the displayed `F_im` family, so the
general finite-limit statement is relevant to it. That application by its
indices is an inference from the notation and matrix discussion, however;
the author does not print a separate line `lim F16=A16` in the inspected
passage.

## 3. What the limiting substitution does--and does not--fix

After introducing the limits, printed p. 334 / PDF p. 340 calls the
constants `A_im` and writes (109a), including

```text
w1 + 1 - k = (1-Q)[A11 - P(A12 + kappa*q/eta_qk*A13)
                    - binom(P,2)(A14 - q/eta_qk*A15)]
              + kappa*Q*eta_qk*A16.
```

Here `w1 = k - 1 + underline(w1)` is the preceding shifted notation. Thus
the `w1` at the left of (109a) is not itself source-underlined; the
underlined quantity occurs specifically in the earlier `X6` connection.

It also sets `A=A66` “aus Gründen der späteren Vereinfachung”. This is a
stated simplifying identification for the unindexed `A`; it is not an
identification of `A16` with `A66`, nor a numerical boundary condition on
`A16`.

Printed p. 335 / PDF p. 341 represents the `A_im` as the entries of
`A_hat_(3,6)=(A_im)_(3,6)` and displays self-conjugacy conditions for
`A_im` and `A66`. Immediately afterwards it says that `F_im` had not yet
been explicitly derived, and consequently neither had `A_im` and `A66`.
The self-conjugacy notation therefore does not supply a missing magnitude or
functional law for `A16` in this source passage.

## 4. Status of the printed A16 expression

The same p. 335 / PDF p. 341 says that, using the interpretation (101b) and
empirical ground-state data, the coefficients can *heuristically* be reduced
numerically to `pi`, `e`, `xi`, and the couplings `alpha`, `beta` of (105a).
It then prints

```text
A16 = (pi e)^2 (1 + alpha/(5 eta) (1 + 6 alpha/pi)) Y9.     (109b)
```

This is positive evidence for that historical parametrisation and for its
explicit uncertainty factor `Y9`; it is not an explicit derivation from the
preceding asymptotic condition. In particular, no inspected line derives the
factors `(pi e)^2`, `1/5`, `6/pi`, `eta^(-1)`, or selects a value of `Y9`.

The directly checked references do not close that gap. (101a), printed
p. 289 / PDF p. 295, gives the configuration list used in the structural
discussion; (101b), p. 291 / PDF p. 297, supplies its particle
interpretations. (105)/(105a), p. 302 / PDF p. 308, supplies the named
couplings and its own numerical specialization. None states a boundary or
symmetry rule for `F16`. The directly checked (98a), printed p. 269 / PDF
p. 275, gives the conditional `k_max=2, q_max=3` selection endpoint after
its preceding speculative identification; it supplies no F16 condition.

## 5. Bounded conclusion for a further reconstruction

The source-supported chain is

```text
R3 metronic selector family F_im(mu_1, mu_2, mu_3)
  -> finite asymptotic constants A_im
  -> X6 = kappa eta_qk F16 in the pseudosinglet contribution
  -> heuristic A16 parametrisation carrying Y9.
```

It does **not** source-support treating the displayed A16 formula as the
unique consequence of a stated F16 boundary problem. A future quellenreine
step would need a directly cited additional equation governing the selector
functions or an explicitly stated condition on `A16`; neither was found in
the bounded pages and direct references above. This is a scope-limited
negative finding, not a claim that no such material exists elsewhere.
