# Alpha Mathematical Review - 2026-09-06

Verdict: accepted for the bounded IGW alpha consistency audit. No blocking
mathematical or implementation defect found. This review does not validate
Heim's physical theory, publication priority, or the complete mass spectrum.

## Independence and reviewed material

The reviewer first derived the branch identities and calculated reference
numbers in a separate standard-library Decimal calculation, before receiving
the implementation. That calculation used independently entered pi digits
at 65-digit working precision, rather than the implementation's
Gauss-Legendre routine. No external source programs or macros were executed.

Reviewed `scripts/audit_alpha.py`, `tests/test_alpha_audit.py`,
`04_reconstruction/alpha_audit/inputs.json`, the local model card and README,
`NORM-ALPHA-AUDIT-SCOPE`, `NORM-1989-ALPHA-ETA-CROSSREF`, the four earlier
1982/1989 normalization decisions specified for this review, and
`SOURCE_REVIEW_2026-09-06.md`. The two canonical ALPHA formula records and
`00_admin/GUARDRAILS.md` were also read. Source-image transcription is the
separate source reviewer's responsibility; this mathematical review did not
independently re-read the raster pages.

## Branch derivation and stable calculation

For `a*sqrt(1-a^2)=R`, `0<R<=1/2`, set `t=a^2`. Squaring within this
positive real domain gives `t^2-t+R^2=0`, hence

```text
t_small = (1-sqrt(1-4R^2))/2 = 2R^2/(1+sqrt(1-4R^2))
t_large = (1+sqrt(1-4R^2))/2
a_small^2+a_large^2 = 1
a_small*a_large = R
```

The implemented `a_large=sqrt(t_large)`, `a_small=R/a_large` avoids
subtractive cancellation in the small root. Both values satisfy the original
unsquared equation in this domain. At `R=1/2` they coincide. Rejecting `R=0`
is consistent with the declared two-positive-branch contract.

Putting `D_prime=1/R` into B60 gives the inverse squares. Its positive sign
therefore selects the small alpha, consistent with the project's source
aliases. The sign does not make either alpha negative.

At extremely small R, finite precision can round the large alpha to exactly
1. The implementation and tests correctly retain the small root without
claiming to resolve the large root's lost complement. The IGW computations
are far from that precision limit.

## Independent numerical agreement

The independently computed central values agree with the implementation:

| Interpretation, mathematical pi | Small-branch inverse | Large-branch inverse |
|---|---|---|
| 1982 literal k=1, q=2 | 137.0491880266639604664053491 | 1.0000266216158851546304255 |
| 1982 existing swapped hypothesis k=2, q=1 | 137.0359609951515777422060897 | 1.0000266267554997251308537 |
| 1989 qk reference-chain interpretation | 137.0360395297220016297477588 | 1.0000266267249792323730379 |
| 1989 kq counterfactual | 137.0362791189414662440929534 | 1.0000266266318692104597640 |

The 1982 swapped hypothesis misses the printed `137.03596147` by about
`-4.74848422e-7`, roughly 47.48 printed last-place units, or 94.97 half-place
widths. It is closer than the literal reading but does not reproduce the
printed rounding interval. These width ratios are arithmetic comparisons,
not statistical sigmas. Neither pi profile in the reviewed report removes
the mismatch.

B59 correctly implements the entire `K_alpha=1-C_prime`; its inner eta term
is not mistakenly substituted for K_alpha. The 1989 qk reading is explicitly
supported by the separately reviewed source continuation to IX. The
vartheta-location qualification is retained, and the kq reading is visibly
a counterfactual. Closeness to printed or modern numbers does not select
either index convention.

## Printed-number interval checks

For a token whose last decimal place is `10^(-d)`, the reviewed code uses
the closed conditional interval `value +/- 0.5*10^(-d)`. Trailing zeros and
decimal commas are preserved. These intervals assume rounding to nearest;
they are not physical measurement uncertainties. Closed endpoints permit
either tie convention. All supplied tokens are short enough for their
initial endpoint arithmetic to be exact at the audit's minimum precision.

Reciprocal endpoints reverse order on positive inputs. The implementation
rounds inverse and squared-sum bounds outward with Decimal floor/ceiling,
so it does not incorrectly exclude a rounding tie. Independently calculated
branch-pair envelopes are:

| Printed data | Envelope for sum of alpha squares |
|---|---|
| 1982 reciprocal pair | [1.0000259819414792370, 1.0000260019406692312] |
| 1989 B62 direct alpha pair | [1.0000250319511424636, 1.0000250319511444636] |
| 1989 boxed reciprocal pair | [1.0000247519513266394, 1.0000249519505787577] |

Every envelope excludes 1. The shown endpoints are shortened for reading;
the machine report contains the working-precision bounds.

B62 also conflicts separately with its own boxed reciprocals:

```text
1/0.0072973525253328589 = 137.035999909348815214...
printed inverse interval: [137.036005, 137.036015]

1/0.999985890199089 = 1.000014110000000290...
printed inverse interval: [1.00001415, 1.00001425]
```

Propagating the direct alphas' own printing intervals leaves both reciprocal
intervals disjoint from the respective boxes. These five incompatibility
checks require neither pi, eta, vartheta, nor a modern experimental value.
They establish arithmetic inconsistency in the reviewed IGW presentation;
they do not establish which historical printing or derivation caused it.

## Executed verification and limits

Executed with bytecode writing disabled:

```text
python -B -m unittest discover -s tests -v
  12 tests passed
python -B scripts/audit_alpha.py --check
  tracked result matches fresh calculation
```

The tests cover an independent exact 0.6/0.8 root pair, coalescence, invalid
domain, tiny-root cancellation, independently supplied pi digits, lexical
printing precision, interval direction and endpoint overlap, source-number
contradictions, 80/120-digit convergence, unsquared-equation residuals, and
independence of equation results from the modern reference. Additional
read-only checks confirmed pi convergence at 40, 50, 100, 160 and 200 digits,
and agreement of the generated report with the independent reference values
and interval results above.

The modern comparison's retrieval provenance is recorded, but external NIST
retrieval and local source hash authentication were not independently repeated
by this mathematical reviewer. Software success and extra decimal digits do
not add physical accuracy or historical validation.

Nonblocking recommendation: add the independently calculated 1989 qk central
value above as a dedicated regression assertion, analogous to the existing
1982 independent-reference test, to guard future B59 scope/index changes.

No canonical files, implementation files, or git state were changed by this
reviewer. This review file is the reviewer's sole authored artifact.
