# EDM2 Y3 diagnostics - independent mathematics review - 2026-09-06

## Scope

Reviewed, without editing, the new `scripts/audit_alpha_book.py`, `tests/test_alpha_book.py`, and `05_analysis/alpha_book_diagnostics.json`. This is an internal arithmetic and reproducibility review only. An inferred `Y_3` is explicitly target-conditioned ex-post calibration/diagnosis, never a prediction or a standalone reconstruction of Eq. (105) from EDM2.

The diagnostic combines the book-(105) structure with the two explicit IGW1982 eta profiles already recorded in the source audit. It does not claim to reconstruct the complete equation independently from EDM2. No web comparison or later criticism was used.

## Execution evidence

These commands completed successfully from the repository root:

```text
py -3.13 -m unittest discover -s tests -p test_alpha_book.py -v
# 8 tests, OK

py -3.13 scripts/audit_alpha_book.py --check
# Diagnostic snapshot matches fresh calculation.
```

The fresh check reproduced the JSON byte-for-byte. I also probed interval inputs below, across, and above `sqrt(2)`, including a broad interval; each result enclosed independently evaluated endpoints, midpoint, and the turning point where applicable.

## Inversion algebra: accepted

For `I=1/alpha`, `I >= 1`, the book left side is

```math
R=alpha sqrt(1-alpha^2)=sqrt(I^2-1)/I^2.
```

With `R0=9 vartheta/(2 pi)^5` and `P=A1 A2`, Eq. (105) reads

```math
R=R0(1-PY3),
```

so the implemented inversion

```math
Y3=(1-R/R0)/P
```

is correct provided `R0>0` and `P>0`. The independent sanity case in the tests (`I=1.25`, `R=.48`, `R0=.5`, `P=.1`, hence `Y3=.4`) is correct.

The snapshot appropriately preserves each target literal and interval. Therefore the two printed-branch `Y3` values and their incompatible intervals are valid target-conditioned results: they show that no one common `Y3` fits both printed branch values under the selected profile. They do not constitute a physical falsification, calibration-free prediction, or invitation to tune the model.

## Interval extrema and current outward bounds: accepted

For `f(I)=sqrt(I^2-1)/I^2`, differentiation gives one maximum:

```math
f(sqrt(2))=1/2.
```

It rises on `[1,sqrt(2)]` and falls afterwards. Thus `rhs_interval` has the correct mathematical structure: it takes the lower endpoint envelope from the lower of the endpoint values, and it takes the upper envelope as `1/2` when the interval contains `sqrt(2)`, otherwise from the higher endpoint value. Since `Y3=(1-R/R0)/P` decreases in `R` for positive `R0,P`, `implied_y3_interval` uses the correct reversed ordering.

For the checked snapshot, `next_minus`/`next_plus` around the square root followed by directed division gives conservative Decimal bounds. `build_report` fixes 80-digit precision while all actual source literals are much shorter; the JSON interval claims are accepted under those conditions.

## Open robustness defect: generic Decimal near one

`required_rhs` and `rhs_interval` square the supplied Decimal **before** installing a guarded or directed context. Their general public behavior is therefore not an outward enclosure when a valid input has more significant resolution than the caller's Decimal context.

Reproduction under Python's default 28-digit context for valid

```text
I = 1.0000000000000000000000000000000000000000000000000000000000001
```

gave:

```text
required_rhs(I)       = 0E+13
rhs_interval((I, I))  = (0E+27, 0E+27)
```

At 100-digit precision, the same mathematical value is approximately `4.4721359549995793928e-31`, and the high-precision interval encloses it. The low-context squaring rounds `I^2` to one before `sqrt` is applied, so the returned zero interval fails to contain the nonzero value.

Impact: **none on the checked snapshot**, which has 80-digit evaluation and comfortably resolved inputs. It is nevertheless a real helper robustness defect, and the existing tests do not detect it. Before reuse with arbitrary Decimal inputs, use a guarded precision based on operand digit counts before squaring (or reject insufficient context), and add this near-one case as a regression test. Perform the `sqrt(2)` membership comparison in the same guarded context.

## Cancellation diagnostic: accepted, but only at stated scope

For small `R`, the stable core calculation obtains the small root by division from the large root. The diagnostic correctly contrasts this with the cancellation-prone near-one-branch expression. The reported binary64 errors are approximately `3.23e-14` and `3.31e-13`, whereas the printed inverse-minus error is about `1.299e-5`. Hence the narrow statement “ordinary binary64 cancellation cannot explain the source mismatch” is sound, and its test is correct.

It must not become the broader claim that no finite-precision cancellation could matter. The script's own low-precision Decimal trials show comparable-scale 8-digit cancellation errors:

| Profile | printed-minus error | 8-digit trial error |
| --- | ---: | ---: |
| `1982_source_literal` | about `-1.299e-5` | about `-1.042e-5` |
| `1982_printed_alpha_fit_variant` | about `-1.300e-5` | about `-1.303e-5` |

Those trials neither reproduce the printed number exactly nor establish a historical calculator or rounding policy. They do show that the evidence excludes binary64 specifically, not every low-precision or transcription mechanism. The snapshot itself labels this correctly as an arithmetic experiment rather than a historical reconstruction.

## Overall finding

The new JSON is reproducible, and its inversion, `sqrt(2)` extremum logic, profile-specific interval comparison, and binary64 cancellation check are mathematically sound for the stated 80-digit source inputs. One non-impacting-but-real generic Decimal interval defect remains near `I=1` under insufficient caller precision. No canonical file was changed in this review.

## Follow-up verification - 2026-09-06

The reported Decimal defect has been fixed and independently rechecked. The
new `exact_square_and_radicand()` performs both `I*I` and `I*I-1` in a local
context with an `Inexact` trap. Thus an input that cannot be represented
exactly enough for the endpoint-enclosure proof now raises `ValueError`
instead of silently producing a spurious zero radicand. `rhs_interval()` also
uses these exact endpoint squares for its `sqrt(2)` membership test.

The two new regressions are appropriate:

- at 28 digits, `I=1` plus a 61st-decimal-place increment is explicitly
  rejected; at 180 digits its returned interval is positive and encloses an
  independently calculated 220-digit value formed through
  `alpha*(1-alpha^2).sqrt()`;
- six-digit context rejects the otherwise ordinary `I=137.036` rather than
  relying on a rounded square.

Full verification now passes:

```text
py -3.13 -m unittest discover -s tests -v
# 23 tests, OK

py -3.13 scripts/audit_alpha_book.py --check
# Diagnostic snapshot matches fresh calculation.
```

The snapshot's numeric content is unchanged. The new `source_scope` metadata
correctly records that this is a book-(105)-structure diagnostic combined with
explicit IGW1982 eta profiles, not a complete book-only derivation. No further
mathematical defect was found in this focused fix review. The earlier
qualification remains necessary: the cancellation result excludes binary64
specifically, not every possible historical low-precision mechanism.
