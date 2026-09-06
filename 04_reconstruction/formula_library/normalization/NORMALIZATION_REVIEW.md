# Normalization Review Snapshot

Date: 2026-09-06 (initial review: 2026-05-15).

Scope: all 14 source-checked formula records; two isolated ALPHA audits implemented.

This register tracks decisions and implementation boundaries. The September
alpha audit is executable; it does not implement the complete mass spectrum.

## Current Gate Status

- Formula catalog: 14/14 records are `source_checked`.
- Implementation status: 2/14 `audit_implemented`, 12/14 `not_implemented`.
- Source-check queue: 14/14 entries are `checked`.
- Agent OCR task queue: 11/11 entries are `integrated`.
- All catalogued formula IDs have a corresponding formula file.

Gate result: the isolated ALPHA audit is scoped by `NORM-ALPHA-AUDIT-001`.
Full mass reconstruction remains blocked and lacks complete dependency coverage;
closing the two listed blockers alone would not establish implementation readiness.
Decision register: 44 resolved, two blocked (46 total).

Fifth-stage addition: `NORM-LORENTZ-MEANING-001` scopes exact rational
boost, simultaneity and source-literal matrix diagnostics. The local
p21 matrix issue is separately documented, not counted among the two
old mass-catalog blockers. No original matrix or alpha profile is repaired.

Fourth-stage addition: `NORM-ENERGY-KINEMATICS-001` scopes the conditional
pc/T and wavelength comparisons, with an independently reviewed calculator.
The mass bridge and the two deliberate substitutions remain assumptions;
this implementation boundary does not resolve their physical justification.

Third-stage additions: `NORM-CHARGE-001` scopes the EDM1 preliminary-alpha
charge-mean diagnosis; `NORM-BOOK-ETA-001` resolves the book-only eta(q,k)
definition chain. Full physical derivations remain open. The separate
book energy-order issue is in `alpha_audit/BOOK_ENERGY_ORDER_ISSUE.md`,
not counted among the two historical mass-catalog blockers.

The separate book-structure Y3 diagnosis is scoped by `NORM-BOOK-ALPHA-001`.
Its inversion is explicitly ex-post and uses the existing IGW1982 eta variants;
it does not resolve the book's missing eta-index derivation or either mass blocker.

## Alpha Audit 2026-09-06

- Both 1982 variants miss the printed positive reciprocal rounding interval.
- 1989 eta order follows the explicit (q,k) source reference chain.
- Three printed branch pairs violate the complementary-square identity;
  two B62-to-box reciprocal checks also fail, including printing intervals.
- Source transcriptions remain unchanged. See `06_docs/ALPHA_AUDIT_2026-09-06.md`.

## Resolved Decisions

- `NORM-1982-QNUM-002` / `NORM-1989-QX-001`: visible stacked parenthesis notation such as `(P over 2)`, `(P over 3)`, and `(Q over 3)` is normalized as `choose(P,2)`, `choose(P,3)`, and `choose(Q,3)`. See `decisions/NORM-STACKED-BINOMIAL.md`.
- `NORM-1982-QNUM-001`: the two underlined `Q(P)` rows are normalized as ordered source rows `Q_of_P_line_1` and `Q_of_P_line_2` with no default binding to `P_1`/`P_2`; any line-order binding is an explicit model variant. See `decisions/NORM-1982-QNUM-QOF-P-BINDING.md`.
- `NORM-1989-QX-002`: the 1989 `C/k` prose rule is normalized as `C_1989 = C_1982 / k`; visible `(B2)` remains `+ C`, with `C` denoting `C_1989` in the 1989 implementation model. See `decisions/NORM-1989-QX-C-OVER-K.md`.
- `NORM-1982-ALPHA-001`: `eta_{kq}` and `eta_{qk}` are source aliases around one semantic helper `eta_k_q(k,q)` defined by the printed formula body. ALPHA `eta_12` remains source-literal as `eta_k_q(1,2)`. See `decisions/NORM-1982-ETA-INDEX.md`.
- `NORM-1982-ALPHA-002`: explicit source-literal and target-motivated variants
  document the discrepancy; neither reproduces the printed precision. Resolution
  is a handling policy, not mathematical reconciliation. See
  `decisions/NORM-1982-ALPHA-RECONCILIATION.md`.
- `NORM-1982-ALPHA-003`: the printed negative alpha reciprocal is preserved as a source-literal residual, but it is not a regression target for branch-equation implementations. See `decisions/NORM-1982-ALPHA-NEGATIVE-BRANCH.md`.
- `NORM-1982-AUX-001`: 1982 `Phi` bracket and precedence scope is normalized as product chain `F1..F9` plus additive terms `A1` and `A2`; the final mismatched delimiter closes only `F9`. See `decisions/NORM-1982-AUX-PHI-PRECEDENCE.md`.
- `NORM-1982-AUX-002`: reused AUX symbols now have typed implementation roles. In particular, branch `alpha_(+)`/`alpha_(-)`, AUX unparenthesized `alpha+`/`alpha-`, and selection `alpha_1..3` are distinct names. See `decisions/NORM-1982-AUX-SYMBOL-ROLES.md`.
- `NORM-1982-MASS-001`: the 1982 source-visible `µα+` cluster is normalized as `mu_mass_element_1982 * alpha_mass_plus_1982`, with the mass sum using `K_aux_1982 + G_aux_1982 + H_aux_1982 + Phi_aux_1982`. See `decisions/NORM-1982-MASS-MU-ALPHA-PLUS.md`.
- `NORM-1982-SELECTION-001`: `(XIII)` keeps source-literal final `alpha_3` by default; `alpha_1` is allowed only as an explicit emendation variant. See `decisions/NORM-1982-SELECTION-XIII-ALPHA3.md`.
- `NORM-1982-SELECTION-002`: `iF(Gamma)` contributes zero for enumerated mass-spectrum states `N=0` and `N>=2`; `N=1` has no spectral term and remains source context. See `decisions/NORM-1982-SELECTION-IF-GAMMA.md`.
- `NORM-1982-N-001`: `nu_x` and `vx` are preserved as source-local notation families; no cross-record aliasing is implied without a later decision. See `decisions/NORM-1982-SELECTION-VX-NUX-SCOPING.md`.
- `NORM-1982-N-002`: the `(XXIX)` doubled `+ + exp[...]` is preserved in transcription but normalized as binary plus plus unary positive exponential for implementation. See `decisions/NORM-1982-SELECTION-N-DOUBLE-PLUS.md`.
- `NORM-1982-N-004`: the page-9 tuple algorithm uses `Q_base_1982 = Q(0)` of `x_v`; `Q_N_1982 = Q(N)` remains an unresolved resonance/bandwidth relation. See `decisions/NORM-1982-SELECTION-QN-Q0-SCOPING.md`.
- `NORM-1982-ALGO-001`: `K_j` integerization is deterministic: maximum nonnegative `K_1..K_3`, and `K_4` uses only the source `,99...99` identity exception or truncation. See `decisions/NORM-1982-ALGO-INTEGER-DECIMAL-RULE.md`.
- `NORM-1982-ALGO-002` / `NORM-1982-ALGO-004`: `W_4` cases are normalized as source-literal pseudocode; printed `K < 0` is preserved and `K_4 < 0` use is an explicit case-c interpretation variant. See `decisions/NORM-1982-ALGO-W4-CASES.md`.
- `NORM-1982-WVX-001`: compact slash expressions in WVX A-matrix rows use denominator-product binding for implementation while source-literal and left-associative variants remain available for audit/regression checks. See `decisions/NORM-1982-WVX-A-MATRIX-SLASH-BINDING.md`.
- `NORM-1989-MASS-001`: `(B4)` is resolved as a mass-record dependency boundary; `HT-F-1989-MASS` consumes versioned `alpha_plus_1989`/`alpha_minus_1989` inputs while executable alpha computation remains under `NORM-1989-ALPHA-001`. See `decisions/NORM-1989-MASS-B4-DEPENDENCY-SCOPE.md`.
- P1/P2 policy decisions now resolved: historical 1982 constants profile, 1982 `G` role split, underlined mass-formula `G`, WVX symbol families, ALGO `x_v`/`x_vx` scoping, 1989 alpha branch aliases, 1982/1989 mass-model versioning, 1989 FPHI naming, 1989 `vartheta` naming, 1989 neutrino `phi` glyph, 1989 neutrino tuple order, and decimal-comma parsing.

## Triaged Blockers

- `NORM-1982-N-003`: Gamma/Q_N relation is no longer merely pending. The source states that the relation is needed but does not give a safe implementation rule; `Q_N_1982 = Q(N)` remains reserved while tuple enumeration uses `Q_base_1982 = Q(0)` by separate decision. See `decisions/NORM-1982-N-GAMMA-QN-BLOCKER.md`.
- `NORM-1989-FPHI-001`: B49 outer three-term structure is resolved. A repeated source form supports denominator-product scope for `kappa(1-q)/(2*alpha*vartheta)`, and the final stacked `(Q over 3)` factor is covered by `NORM-STACKED-BINOMIAL` as `choose(Q,3)`. See `decisions/NORM-1989-FPHI-B49-SCOPE.md`.
- `NORM-1989-FPHI-002`: `BUW^{-1}_{N=0}` is resolved as `B_1989_B28 * U_B50 * reciprocal(W_N0_1989)`, with inverse/subscript attached to `W`. See `decisions/NORM-1989-FPHI-BUW-PRODUCT-SCOPE.md`.
- `NORM-1989-FPHI-003`: `(B50)` visible `-- 4*pi...` appears on the first printed source line and repeats as a line-wrapped minus plus continuation minus in the lifetime section. It remains blocked as a sign anomaly. See `decisions/NORM-1989-FPHI-B50-DOUBLE-MINUS-BLOCKER.md`.
- `NORM-1989-FPHI-004`: `(B8)` and `(B13)` line-wrap-sensitive scopes are fully parenthesized; B13's leading `4` remains inside the squared factor. See `decisions/NORM-1989-FPHI-B8-B13-LINE-WRAP-SCOPE.md`.
- `NORM-1989-ALPHA-001`: `(B59)` is normalized as the full equality chain `1 - C_prime_1989 = 1 - eta_term_1989 = K_alpha_1989`; the old shortcut `1 - C_prime = 1 - K_alpha` remains rejected. See `decisions/NORM-1989-ALPHA-B59-KALPHA-SCOPE.md`.
- `NORM-1989-NEUTRINO-001`: the field-mass interpretation boundary is resolved as a model-card rule. `M_nu` may be implemented only as Heim's internal field-mass construct; modern comparison requires a separate cited comparison profile. See `decisions/NORM-1989-NEUTRINO-FIELD-MASS-BOUNDARY.md`.

## P0 Blockers

### 1989 Corrections And Extensions

- `HT-F-1989-FPHI`: `(B50)` double minus remains source-visible and needs a future explicit sign decision.

## Recommended Work Order

1. Normalize 1982 core dependencies:
   - remaining selection-facing dependency boundaries
   - tuple-state conventions before numeric mass use
2. Normalize 1982 selection and tuple algorithm:
   - SELECTION core
   - SELECTION-WVX A-matrix slash binding complete; keep variants attached to any future implementation
   - SELECTION-N resonance rules
   - SELECTION-ALGO pseudocode
3. Treat 1989 as a separate model variant:
   - QX and MASS
   - FPHI/self-coupling
   - ALPHA
   - NEUTRINO interpretation boundary

## Agent Cross-Check

Two read-only explorer agents independently reviewed the 1982 and 1989 formula subsets.

The 1982 review confirmed the local blocker list and added these explicit items:

- stacked `P/3`-like notation should be handled with the same rule as stacked `P/2`; this is now resolved as `choose(P,3)` / `choose(P,2)`;
- `Q_N = Q(N)` versus `Q = Q(0)` is resolved for tuple enumeration by `NORM-1982-SELECTION-QN-Q0-SCOPING`; Gamma/Q_N bandwidth semantics remain blocked separately;
- visible `K < 0` in the `W_4` case logic must not be normalized away;
- `G` role splitting is now resolved as `G_count` versus `G_aux_1982` by `NORM-1982-G-SYMBOL-ROLES`.

The 1989 review confirmed that the highest-risk implementation blockers are:

- `QX` stacked notation and `C/k` charge normalization are resolved; downstream charge code must still keep 1982 and 1989 variants separate;
- `FPHI` scope and symbol parsing, especially the remaining `(B50)` sign anomaly;
- `ALPHA` branch and `K_alpha` semantics;
- strict separation of 1989 mass/neutrino variants from 1982 formulas.

## Non-Negotiable Guardrail

No numerical implementation should start from the readable LaTeX alone. Each coded expression must link back to a normalization decision ID in `NORMALIZATION_DECISIONS.csv`.

External evidence can create research tasks and model-version hypotheses, but it cannot overwrite source-checked transcriptions or resolved normalization decisions.
