# NORM-1982-QNUM-QOF-P-BINDING

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-QNUM-001`

## Decision

The two underlined `Q(P)` source lines are normalized as ordered source rows without a default semantic binding to `P_1` and `P_2`.

Source-visible rows:

```text
underlined Q(P) = k - 1
underlined Q(P) = 2k - 1
```

Default implementation-facing representation:

```text
source_literal_no_binding:
  Q_of_P_line_1 = k - 1
  Q_of_P_line_2 = 2k - 1
  binding_to_P1_P2 = none
```

This preserves the source order while preventing an unsupported rewrite into:

```text
Q(P_1) = k - 1
Q(P_2) = 2k - 1
```

## Optional Variant

A model may define an explicit `line_order_binding_variant`:

```text
line_order_binding_variant:
  Q_of_P1 = Q_of_P_line_1
  Q_of_P2 = Q_of_P_line_2
  provenance = our_inference
  requires_explicit_opt_in = true
```

This variant is not source-literal and must not be used as the default in tuple generation, fixtures, or tests.

## Implementation Rule

- Use `Q_of_P_line_1` and `Q_of_P_line_2` as the default normalized names.
- Do not name the default rows `Q_of_P1` or `Q_of_P2`.
- Preserve both underlined `Q(P)` rows in the formula transcription.
- Any downstream code that needs a `P_1`/`P_2` binding must declare a model variant explicitly.
- Do not use target particle assignments or later tuple output to decide this binding.

## Guardrails

- Zeilenreihenfolge is evidence for source order, not by itself evidence for semantic binding.
- The source uses `Q` in multiple nearby roles; this decision does not resolve all `Q` overloads.
- This decision only removes the P0 implementation blocker by providing a safe no-binding default.
- Future evidence may add another variant, but it must not overwrite `source_literal_no_binding`.

## Critic Check

A read-only Critic check accepted this default/no-binding normalization and rejected a silent `P_1`/`P_2` binding.
