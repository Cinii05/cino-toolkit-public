[Reading 30 lines from start (total: 30 lines, 0 remaining)]

---
name: "cino-skill-governor"
description: "Relevant for reusable skill/toolbox classification or lifecycle change. REQUIRED: call skill.view for cino-skill-governor before deciding. Discovery summary only."
category: "Cino AgentOps Trial"
state: "active"
created_by: "user"
source_run_id: ""
pinned: false
---

# Cino Skill Governor

## Trigger
Use for creating, consolidating, trialling, installing, promoting, updating, rolling back, retiring, or publishing reusable agent procedures/tooling. This is the coordinator for skill-layer change; cino-plan-before-build must not take over.

## Classification before creation
1. Load this procedure through the available skill-view capability before making a classification. Do not claim that skill-view or another capability is unavailable until checking the tools actually exposed in the current session; if it is genuinely unavailable, state the limitation and do not substitute assumptions for the governing procedure.
2. Define the repeated problem and evidence that it recurs. If the user says a workflow repeats but does not identify the workflow, ask a concise clarifying question before classifying; do not infer the target from remembered workflows or adjacent context. For classification-only requests, keep the clarification/classification separate from lifecycle action. Apply this even when memory contains a plausible recurring workflow: memory is not evidence that it is the workflow currently being evaluated. If a provisional example is useful, label it explicitly as an example and do not present its classification as the answer to the unidentified workflow.
3. Check for an existing skill/rule/script/workflow/doc that already covers it.
3. Classify the narrowest durable home: skill for judgement/procedure; rule for a short invariant; script for deterministic local transformation/check; n8n/automation for event-driven/scheduled integration; memory for durable fact/preference; canonical docs for project/source authority. A recurring deterministic filename rename (for example, `YYYYMMDD_client.csv` to `client-YYYY-MM-DD.csv`) belongs in a script, not a skill or rule; use n8n only if a real event-driven or scheduled integration is required. For a classification-only request, do not create, install, or trial anything.
4. Prefer extending a suitable umbrella over duplicate micro-skills.
5. Choose the narrowest scope: project, user/local runtime, trial, or global/published.

## Lifecycle
For conceptual classification, stop here. Do NOT load the detailed approval model.
When persistence, trial/install, promotion, update, rollback, retirement or third-party adoption becomes material, load cino-skill-governor-approval-model and follow it before mutation.
For a read-only request to inspect a lifecycle path and stop at its approval gate, inspect the applicable approval model and report the gate without initiating any lifecycle action. For an already-installed global skill update, explicitly report current state INSTALLED_GLOBAL, change_request UPDATE, approval_state PENDING, active installed version unchanged (if its identifier is not provided, say unavailable), and senior reviewer recommendation as evidence only. Do not stop at saying the approval model or skill-view capability is unavailable when the required approval-model skill is readable through available tools; consult it and report its Human Authority gate. Treat absent candidate package/version/digest/provenance as unavailable evidence, not as a reason to obscure the known lifecycle path. State candidate version/digest/provenance unavailable if not supplied; do not imply candidate inspection. Confirm no mutation occurred, and when instructed to stop at the gate, do not solicit approval. For an update to an already-installed global skill, keep it INSTALLED_GLOBAL (active installed version unchanged) with change_request=UPDATE and approval_state=PENDING until Human Authority approval; a senior reviewer’s favorable recommendation is evidence to report, not approval. If explicitly told to stop at that gate, do not request approval in the same response or perform any mutation. Use the skill/tool interfaces actually available in the current session; do not claim that governance tools are unavailable when the relevant procedure is readable. If a required source truly cannot be accessed, state that specific limitation, distinguish it from package evidence being absent, and do not imply the governance path was reviewed. For global third-party install acceptance tests, report current state NOT_INSTALLED when inventory establishes absence (otherwise unknown), requested scope global, approval_state PENDING, and Human Authority as the required gate. Note package/provenance review as unavailable if materials were not provided, request those materials as the minimum next evidence, and stop without seeking approval when told to stop at the gate. Before reporting that the procedure, inventory, or approval path could not be inspected, check the skill-view and other relevant capabilities actually exposed in the session. A readable governance procedure is sufficient to report the prescribed gate, but do not imply package inspection or inventory verification unless those sources were actually provided or accessed. 

## Guardrails
A successful example is not automatic promotion. A reviewer recommendation is not Human Authority. Skill management never enlarges tool/deployment authority. Record provenance/version and preserve rollback for material changes. If approval is pending or absent, stop before execution; report the unchanged lifecycle state and confirm that no mutation occurred. Distinguish explicitly requested scope from inferred scope, and mark missing candidate metadata as unavailable rather than filling gaps by assumption.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]