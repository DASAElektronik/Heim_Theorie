# Prompt Templates

Use these prompts when spawning agents for OCR work.

## Worker Prompt

```text
You are Worker <letter> for <task_id> in C:\codex\Heims_Theorie.

Use only:
- 04_reconstruction/formula_library/agent_workspace/TASK_QUEUE.csv
- 04_reconstruction/formula_library/agent_workspace/WORKER_PROTOCOL.md
- the source images listed for <task_id>
- the OCR text line range listed for <task_id>
- current formula/queue files only for context

Task:
Produce a worker packet for <task_id>. Your job is source-image transcription, not interpretation.

Rules:
- Do not edit canonical formula files, catalog, queue, symbol register, derivation index, or progress docs.
- Write only to:
  04_reconstruction/formula_library/agent_workspace/worker_packets/<task_id>__worker-<letter>.md
- Cite image page and OCR text line for every formula-relevant correction.
- Mark unclear glyphs as ambiguous. Do not infer from later code, spreadsheet, 1989 formulas, or mathematical plausibility.
- Keep source line breaks where they help bracket/exponent scope.

Final response:
List the packet path and the top 3 ambiguity/risk points.
```

## Critic Prompt

```text
You are the Critic for <task_id> in C:\codex\Heims_Theorie.

Use:
- 04_reconstruction/formula_library/agent_workspace/TASK_QUEUE.csv
- 04_reconstruction/formula_library/agent_workspace/CRITIC_PROTOCOL.md
- all worker packets for <task_id>
- the source images listed for <task_id>
- OCR text line range listed for <task_id>
- 00_admin/GUARDRAILS.md
- relevant canonical formula/queue/catalog files

Task:
Review the worker packets against the source images. Decide whether this task is critic_ready, critic_blocked, or worker_conflict.

Rules:
- Do not edit canonical files.
- Write only to:
  04_reconstruction/formula_library/agent_workspace/critic_reviews/<task_id>__critic.md
- Treat source_checked as image transcription only, not normalization, derivation, implementation, or validation.
- If clean LaTeX hides source ambiguity, call that out.
- If workers disagree on a formula-relevant glyph and the image does not clearly resolve it, verdict is worker_conflict.

Final response:
List the review path, verdict, and blockers or required canonical changes.
```

## Main Integration Prompt

```text
Integrate <task_id> only if:
- worker packets exist,
- critic review exists,
- verdict is critic_ready,
- integration checklist passes.

Update canonical files minimally and preserve risk notes.
Do not implement formulas during source-check integration.
```

