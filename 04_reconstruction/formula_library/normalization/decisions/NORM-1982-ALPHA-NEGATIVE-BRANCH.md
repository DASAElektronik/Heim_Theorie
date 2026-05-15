# NORM-1982-ALPHA-NEGATIVE-BRANCH

Date: 2026-05-15

Decision ID resolved:

- `NORM-1982-ALPHA-003`

## Decision

The printed 1982 negative reciprocal value is preserved as a source-literal datum, but it is not an implementation regression target for any implementation of the source-checked branch equation.

The source-checked equation is:

```text
alpha * sqrt(1 - alpha^2)
  = 9 * vartheta * (1 - A1*A2) / (2*pi)^5
```

For this equation, the two branches are coupled by:

```text
alpha_minus = sqrt(1 - alpha_plus^2)
```

Using the printed positive reciprocal,

```text
alpha_(+)^-1 = 137.03596147
```

the same branch equation implies:

```text
alpha_(-)^-1 ~= 1.000026626755
```

This does not match the printed source value:

```text
alpha_(-)^-1 = 1.00001363
```

Conversely, treating the printed negative reciprocal as branch-equation exact would imply:

```text
alpha_(+)^-1 ~= 191.532075038398
```

That is incompatible with the printed positive reciprocal.

## Implementation Rule

- Store the printed `alpha_(-)^-1 = 1.00001363` only as a source reference value.
- Do not tune `eta_12`, `vartheta`, branch signs, or the branch equation to match the printed negative reciprocal.
- If an implementation declares `source_transcription_variant`, compute `alpha_minus` from the same branch equation and expect `alpha_minus^-1 ~= 1.000026621616`.
- If an implementation declares `printed_alpha_fit_variant`, compute `alpha_minus` from the same branch equation and expect `alpha_minus^-1 ~= 1.000026626755`.
- Any future model that claims the printed negative reciprocal as computed output needs a separate decision with source-only evidence.

## Guardrails

- This decision does not mathematically reconcile the printed negative reciprocal.
- This decision resolves the P0 blocker by preventing a false regression target.
- Keep both printed values in the formula record because they are source-visible.
- Keep reciprocal notation explicit: `alpha_(+)^-1` and `alpha_(-)^-1`.
- External evidence may explain this as a later version drift, but it must not overwrite the 1982 source-checked formula.

## External Evidence

Related entries are tracked in `04_reconstruction/external_evidence/EXTERNAL_EVIDENCE.csv`:

- `EXT-ALPHA-1989-001`: 1989 alpha formulation reports a nearby but version-specific negative reciprocal value.
- `EXT-ALPHA-1992-001`: secondary online overview claims a later 1992 value close to the branch-equation-implied 1982 negative reciprocal; this still needs primary-source discovery.

## Critic Check

A read-only Critic check accepted resolving `NORM-1982-ALPHA-003` only as a residual policy: document the source value, do not correct it, and do not use it as a regression target.
