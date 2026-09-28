[Reading 35 lines from start (total: 35 lines, 0 remaining)]

---
name: "cino-plan-before-build"
description: "Relevant for non-trivial authorised implementation when no stricter specialist owns the workflow. REQUIRED: call skill.view for cino-plan-before-build before planning. Discovery summary only."
category: "Cino AgentOps Trial"
state: "active"
created_by: "agent"
source_run_id: "fd85fa39-cb23-47b6-a1f3-5eb793dab7be"
pinned: false
---

# Cino Plan Before Build

## Precedence
If a specialist/project skill fully owns the workflow, it remains coordinator. Do not compete with it. Coordinate only when no stricter specialist applies.

## Trigger
Use for a non-trivial implementation request. Do not use for pure read-only navigation, a simple test-selection question, routing-only questions, or skill-layer lifecycle changes; those belong to cino-skill-governor.

## Procedure
1. Define requested outcome, protected behaviour, scope and stop condition.
2. Separate authority gates: planning/read; local edit; commit; push; merge; deploy/publish/shared/live mutation. Never infer a later gate from an earlier one.
3. Activate cino-source-of-truth only when authority/evidence is material and unresolved.
4. Activate cino-repo-navigator only when implementation surface is unclear.
5. Write a small implementation plan before edits. If the requested change is underspecified, state the missing behavior/scope and stop short of inventing a file-level plan; ask for the intended change. Still provide applicable authority boundaries and a conditional smallest verification path.
6. For acceptance tests that explicitly authorize planning/reasoning but require stopping before edits, keep the response genuinely pre-edit: do not inspect the repository, run tests, or claim repository evidence. If the intended behavior or target is absent, identify that missing specification, state the authorization boundary, and offer only a conditional verification path once specified. This is not a reason to invent a concrete backend/file-level plan.
6. Implement only within the authorised boundary. If the request explicitly authorizes planning but requires stopping before edits, do not inspect or edit files unless separately authorized; give a conditional verification path tied to a later specified change, and accurately report that no repository evidence was gathered. If the intended behavior or change surface is missing, do not invent a concrete implementation or file-level verification plan: ask for the missing specification and name only the conditional smallest verification category (typically a focused unit/static check, escalating only if dependencies require it). A read-only helper phase does not cancel outer edit authority; edit authority does not grant push/merge/deploy.

### Underspecified acceptance tests
When the user asks for a plan for a class of change (for example, “a non-trivial backend change”) but gives no behavior, target, or defect, do not treat authorization to reason as a sufficient specification. State the missing input, explicitly list the authorized and prohibited gates, and give a conditional verification category rather than fabricating a code-level plan. In a stop-before-edit test, do not browse the repository merely to make the answer look concrete; be clear that no repo inspection or verification occurred.
8. Use cino-test-router once, at the point test selection is needed, to choose sufficient verification. Do not reload it unless the change surface materially changes.
8. Verify actual results and side effects.
9. Only after implementation and verification are complete, load cino-evidence-handoff and emit exactly one final handoff. Do not preload the handoff skill and do not emit a preliminary handoff before it.

## Guardrails
Do not load every helper ritualistically. Do not create or update todo/task-tracking state unless the user explicitly asked for it. Do not use generic process to weaken a stricter project rule. Stop at the first unauthorised gate.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]