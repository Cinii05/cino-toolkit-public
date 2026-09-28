[Reading 32 lines from start (total: 32 lines, 0 remaining)]

---
name: "cino-context-funnel"
description: "Relevant when evidence spans multiple uncertain sources. REQUIRED: if relevant, call skill.view for cino-context-funnel before reasoning or answering. Discovery summary only; it is not the procedure."
category: "Cino AgentOps Trial"
state: "active"
created_by: "agent"
source_run_id: "fd85fa39-cb23-47b6-a1f3-5eb793dab7be"
pinned: false
---

# Cino Context Funnel

## Trigger
Use when the task depends on multiple possible evidence sources and it is not yet clear which ones are necessary. Typical examples: current state across GitHub + Drive + runtime, a broad handoff reconciliation, or a question where source breadth is genuinely uncertain.
Do not use it for a supplied exact file, a known symbol, a single explicit authority conflict, or as a ritual first step.

## Procedure
1. State the exact decision or claim that must be proved.
2. List candidate evidence classes, not every file.
3. Choose the smallest evidence set capable of proving the claim and set a stop condition before retrieval. If the user explicitly supplies a finite set of evidence files, treat that set as the scope; inspect only those files unless a gap makes another source necessary.
4. Confirm that the named evidence is actually accessible in the current environment before claiming to have reviewed it. A named path or a statement that file access is available is not itself evidence that a read operation is available. Check the actual available tools; when suitable read access exists, use it to inspect the supplied finite set rather than prematurely reporting inability. If no suitable read capability exists, state the specific gap and request the minimum missing input. Do not imply that evidence was examined, and do not invent a tool or retry through unrelated mechanisms.
5. Reuse fresh verified evidence when the underlying source/version has not changed.
6. Retrieve narrowly. Do not recursively ingest a repo, Drive, vault, archive, or transcript because it might be useful.
7. If the narrowed evidence conflicts, hand the exact claim and sources to cino-source-of-truth.
8. Stop once the claim is supportable or the missing evidence is identified.

## Output
Claim/decision; evidence classes selected; evidence intentionally excluded; stop condition; unresolved gap if any.
For activation-only requests, state the sequence and stop/conflict rules without retrieving external evidence; label the response as a procedure, not a verified current-state finding. When the user explicitly asks to load the applicable skills, actually call skill.view on them in the determined order before reporting the order and stopping. Do not claim a skill-view capability is unavailable when the skill tool is exposed; a procedural note that names an intended sequence is not a substitute for loading the procedures.

## Guardrails
Read-only. Never enlarges authority and never overrides a stricter specialist/project skill.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]