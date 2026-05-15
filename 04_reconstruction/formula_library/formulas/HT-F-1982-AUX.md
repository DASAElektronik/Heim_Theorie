# HT-F-1982-AUX: 1982 Auxiliary Functions

## Formula Group

Source-checked transcription from page images:

```math
\eta = \frac{\pi}{(\pi^4 + 4)^{1/4}}
```

Original label: `(VII)`.

```math
t = 1 - \frac{2}{3}\xi\eta^2(1-\sqrt{\eta})

\alpha_+ = t(\eta^2\eta^{1/3})^{-1} - 1

\alpha_- = t(\eta\eta^{1/3})^{-1} - 1
```

Original label: `(VIII)`.

```math
\eta_{qk} =
\frac{\pi}{[\pi^4 + (4+k)q^4]^{1/4}}

N1 = alpha1
N2 = (2/3) alpha2
N3 = 2 alpha3

\alpha_1 = \frac{1}{2}(1+\sqrt{\eta_{qk}})

\alpha_2 = \frac{1}{\eta_{qk}}

\alpha_3 =
\frac{e^{(k-1)}}{k}
- q \left\{
\frac{\alpha}{3}
\left[(1+\sqrt{\eta_{qk}})\left(\frac{\xi}{\eta_{qk}^2}\right)\right]^{(2k+1)}
\eta_{qk}^3
+ \left[\frac{\eta(1,1)}{e\eta_{qk}}\right]
\left(2\sqrt{\xi\eta_{qk}}\right)^k
\left[\frac{1-\sqrt{\eta_{qk}}}{1+\sqrt{\eta_{qk}}}\right]^2
\right\}
```

Original label: `(IX)`.

```math
s = k^2 + 1

Q_1 = 3 \cdot 2^{s-2}

Q_2 = 2^s - 1

Q_3 = 2^s + 2(-1)^k

Q_4 = 2^{s-1} - 1
```

Original label: `(X)`.

```math
K =
n_1^2(1+n_1)^2N_1
+ n_2(2n_2^2+3n_2+1)N_2
+ n_3(1+n_3)N_3
+ 4n_4

G =
Q_1^2(1+Q_1)^2N_1
+ Q_2(2Q_2^2+3Q_2+1)N_2
+ Q_3(1+Q_3)N_3
+ 4Q_4

H =
2n_1Q_1[1+3(n_1+Q_1+n_1Q_1)+2(n_1^2+Q_1^2)]N_1
+ 6n_2Q_2(1+n_2+Q_2)N_2
+ 2n_3Q_3N_3

\Phi =
\frac{3P}{\pi\sqrt{\eta_{qk}}}
\left(1-\frac{\alpha_-}{\alpha_+}\right)
(P+Q)(-1)^{P+Q}
\left[1-\frac{\alpha}{3}+\frac{\pi}{2}(k-1)3^{1-q/2}\right]
\cdot
\left\{1+\frac{2k\kappa}{3\eta^2}\xi
\left[1+\xi^2(P-Q)(\pi^2-q)\right]\right\}
\left[1+\frac{4\xi {P \choose 2}}{k}\left(\frac{\xi}{6}\right)^q\right]^{-1}
\cdot
\left[2\sqrt{\eta_{11}}\sqrt{\eta_{qk}}+q\eta^2(k-1)\right]
\left(1+\frac{4\pi\alpha}{\eta\sqrt{\eta}}\right)
\left[1+\frac{Q(1-\kappa)(2-k)n_1}{Q_1}\right]
+ \frac{4(1-\alpha_-/\alpha_+)\alpha(P+Q)}{\xi^2}
+ \frac{4q\alpha_-}{\alpha_+}
```

Original label: `(XI)`.

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 169-220
- Source images:
  - `07_outputs/source_check_images/1982_massenformel/page-04.png`
  - `07_outputs/source_check_images/1982_massenformel/page-05.png`
- Original labels: `(VII)` to `(XI)`

## Outputs

- `eta`
- `t`
- `alpha_plus`, `alpha_minus`
- `eta_qk`
- `N1`, `N2`, `N3`
- `Q1`, `Q2`, `Q3`, `Q4`
- `K`, `G`, `H`, `Phi`

## Current Status

`source_checked`

## Audit Notes

- The OCR text damages most superscripts and several roots; this transcription is from `page-04.png` and `page-05.png`.
- `(VII)` and `(VIII)` overlap conceptually with `HT-F-1982-ALPHA`; they are repeated here because they are printed in the same auxiliary-function block.
- `HT-F-1982-ALPHA` separately source-checks the earlier page-03 abbreviation block using source-local `eta_{kq}`. This AUX entry uses source-local `eta_{qk}`. Normalization decision `NORM-1982-ETA-INDEX` maps both aliases to canonical helper `eta_k_q(k,q)` by the printed formula body.
- In `Phi`, the factor after the binomial term is printed with exponent `-1` on the full bracket.
- Normalization decision `NORM-1982-AUX-PHI-PRECEDENCE` records the implementation-facing `Phi` factorization as product chain `F1..F9` plus additive terms `A1` and `A2`.
- The final multiplicative factor in `Phi` appears in the source with an opening parenthesis and closing square bracket. `NORM-1982-AUX-PHI-PRECEDENCE` treats this only as a delimiter-closure typo for that factor, not as scope expansion over the following additive terms.
- Normalization decision `NORM-1982-AUX-SYMBOL-ROLES` resolves reused symbol roles for implementation. Branch `alpha_(+)`/`alpha_(-)`, AUX unparenthesized `alpha+`/`alpha-`, and selection coefficients `alpha_1..3` are distinct implementation families.
- The displayed formula block remains the source transcription. Implementation must use the linked normalization decisions; the record is not derived, dimension-checked, or implementation-ready.

## Risks

- `Phi` bracket and precedence scope is resolved by `NORM-1982-AUX-PHI-PRECEDENCE`; implementation must also use typed symbol roles from `NORM-1982-AUX-SYMBOL-ROLES`.
- `G` collides with `G_count`.
- `eta(1,1)` in `alpha_3` maps to `eta_k_q(1,1)` under `NORM-1982-ETA-INDEX`; use named arguments at call sites.
- Selection tuple and resonance rules remain outside this AUX normalization decision and are still blocked separately.
