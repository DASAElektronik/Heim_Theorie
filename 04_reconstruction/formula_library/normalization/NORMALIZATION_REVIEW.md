# Normalization Review Snapshot

Date: 2026-05-15

Scope: all 14 formula records currently marked `source_checked` and `not_implemented`.

This review does not implement formulas. It identifies the decisions required before implementation can start without hiding transcription ambiguity.

## Current Gate Status

- Formula catalog: 14/14 records are `source_checked`.
- Implementation status: 14/14 records are `not_implemented`.
- Source-check queue: 14/14 entries are `checked`.
- Agent OCR task queue: 11/11 entries are `integrated`.
- All catalogued formula IDs have a corresponding formula file.

Gate result: implementation remains blocked until the remaining P0 normalization decisions are resolved or explicitly model-scoped.

## Resolved Decisions

- `NORM-1982-QNUM-002` / `NORM-1989-QX-001`: visible stacked parenthesis notation such as `(P over 2)`, `(P over 3)`, and `(Q over 3)` is normalized as `choose(P,2)`, `choose(P,3)`, and `choose(Q,3)`. See `decisions/NORM-STACKED-BINOMIAL.md`.

## P0 Blockers

### 1982 Base Definitions

- `HT-F-1982-QNUM`: the two underlined `Q(P)` lines are source-checked but not semantically bound to `P_1` and `P_2`.
- `HT-F-1982-ALPHA`: `eta_{kq}` versus later `eta_{qk}`/`eta` notation needs an explicit alias/index convention.
- `HT-F-1982-AUX`: `Phi` needs a line-by-line bracket, exponent, and fraction-precedence normalization.
- `HT-F-1982-AUX`: reused symbols (`P`, `Q`, `q`, `Q_j`, `kappa`, `alpha`, `alpha_plus`, `alpha_minus`) need typed implementation names.
- `HT-F-1982-QNUM` / `HT-F-1982-AUX` / `HT-F-1982-MASS`: `G` must be split into structural-count and mass-contribution roles before code.
- `HT-F-1982-MASS`: source-visible `µα+` may be normalized to `mu * alpha_plus` only as an explicit branch decision.

### 1982 Selection Rules

- `HT-F-1982-SELECTION`: the rightmost `(XIII)` factor is source-checked as `alpha_3`; changing it to `alpha_1` would be an emendation.
- `HT-F-1982-SELECTION`: `iF(Gamma)` has no safe implementation meaning yet.
- `HT-F-1982-SELECTION-WVX`: dense slash expressions in A-matrix terms need explicit parentheses.
- `HT-F-1982-SELECTION-N`: source-local `vx` notation must be scoped or promoted to a project-wide convention.
- `HT-F-1982-SELECTION-N`: doubled `+ + exp[...]` must not be silently removed.
- `HT-F-1982-SELECTION-N` / `HT-F-1982-SELECTION-ALGO`: `Q_N = Q(N)` and `Q = Q(0)` require a state-dependent convention.
- `HT-F-1982-SELECTION-ALGO`: integer/truncation/decimal-place rules for `K_j` must be specified before tuple enumeration.
- `HT-F-1982-SELECTION-ALGO`: `W_4` cases require deterministic pseudocode before numeric use.
- `HT-F-1982-SELECTION-ALGO`: printed `K < 0` in case `(c)` must not be rewritten to `K_4 < 0` without an interpretation decision.

### 1989 Corrections And Extensions

- `HT-F-1989-QX`: the `C/k` prose rule must remain separate from the visible `+ C` in `(B2)` until normalized.
- `HT-F-1989-MASS`: `(B4)` alpha constants need a dedicated normalization before being used as dependencies.
- `HT-F-1989-MASS`: 1989 mass terms must remain versioned separately from 1982 mass terms.
- `HT-F-1989-FPHI`: `(B49)` self-coupling scope must be fully parenthesized.
- `HT-F-1989-FPHI`: `BUW^{-1}_{N=0}` is an unresolved source token.
- `HT-F-1989-FPHI`: `(B50)` double minus needs a sign decision.
- `HT-F-1989-FPHI`: `(B8)` through `(B14)`, especially `(B13)`, need line-wrap-aware normalization.
- `HT-F-1989-FPHI`: subscript conventions for `Q_*`, `N_i`, `N(k)`, `N'(k)`, and comma-like `eta` subscripts need implementation aliases.
- `HT-F-1989-ALPHA`: `(B59)` must preserve the full equality chain and normalize scope step by step.
- `HT-F-1989-NEUTRINO`: the formula can only be modeled as Heim's field-mass construct until modern-neutrino validation is separately scoped.
- `HT-F-1989-NEUTRINO`: the four-digit state labels need an explicit tuple-order convention before computation.

## Recommended Work Order

1. Resolve notation-level decisions shared across formulas:
   - `eta_{kq}` / `eta_{qk}`
   - `vartheta` / theta naming
   - `vx` / `nu x` scoping
   - `µα+` branch notation
   - `G` role split
2. Normalize 1982 core dependencies:
   - QNUM
   - ALPHA
   - AUX/Phi
   - MASS
3. Normalize 1982 selection and tuple algorithm:
   - SELECTION core
   - SELECTION-WVX A-matrix
   - SELECTION-N resonance rules
   - SELECTION-ALGO pseudocode
4. Treat 1989 as a separate model variant:
   - QX and MASS
   - FPHI/self-coupling
   - ALPHA
   - NEUTRINO interpretation boundary

## Agent Cross-Check

Two read-only explorer agents independently reviewed the 1982 and 1989 formula subsets.

The 1982 review confirmed the local blocker list and added these explicit items:

- stacked `P/3`-like notation should be handled with the same rule as stacked `P/2`; this is now resolved as `choose(P,3)` / `choose(P,2)`;
- `Q_N = Q(N)` versus `Q = Q(0)` is a separate state-dependent decision;
- visible `K < 0` in the `W_4` case logic must not be normalized away;
- `G` must be split into structural-count and mass-contribution meanings.

The 1989 review confirmed that the highest-risk implementation blockers are:

- `QX` charge normalization (`C/k`; stacked `P/2` is now resolved as `choose(P,2)`);
- `FPHI` scope and symbol parsing, especially `(B49)`, `BUW`, `(B50)`, `(B8)`, and `(B13)`;
- `ALPHA` branch and `K_alpha` semantics;
- strict separation of 1989 mass/neutrino variants from 1982 formulas.

## Non-Negotiable Guardrail

No numerical implementation should start from the readable LaTeX alone. Each coded expression must link back to a normalization decision ID in `NORMALIZATION_DECISIONS.csv`.
