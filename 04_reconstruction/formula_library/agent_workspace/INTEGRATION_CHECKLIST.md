# Integration Checklist

Use this before editing canonical files from an approved packet.

## Pre-Integration

- [ ] Task exists in `TASK_QUEUE.csv`.
- [ ] At least two worker packets exist, or one worker packet plus direct main-agent image read.
- [ ] Critic review exists.
- [ ] Critic verdict is `critic_ready`.
- [ ] No unresolved worker conflict affects formula output.

## Canonical Edits

- [ ] Formula file updated or created.
- [ ] `formula_catalog.csv` status updated only as far as justified.
- [ ] `SOURCE_CHECK_QUEUE.csv` row updated.
- [ ] `DERIVATION_INDEX.md` updated if derivation/status wording changes.
- [ ] `symbol_register.csv` updated for new or ambiguous symbols.
- [ ] `PARAMETER_BOOK.md` updated for constants or free choices.
- [ ] `00_admin/PROGRESS.md` records the integration.

## Required Wording

Every integrated transcription must preserve these distinctions:

- source-checked vs. normalized
- stated formula vs. derived formula
- transcription vs. implementation
- historical source value vs. modern comparison value

## Post-Integration

- [ ] Search for stale placeholders or contradictory status text.
- [ ] Search for overclaims such as `validated`, `proven`, `implemented`, unless actually true.
- [ ] Leave next unresolved risks visible.

