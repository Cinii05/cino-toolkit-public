[Reading 30 lines from start (total: 30 lines, 0 remaining)]

---
name: "cino-test-router"
description: "Relevant when choosing the smallest sufficient verification or test set. REQUIRED: call skill.view for cino-test-router before selecting tests. Discovery summary only."
category: "Cino AgentOps Trial"
state: "active"
created_by: "user"
source_run_id: ""
pinned: false
---

# Cino Test Router

## Trigger
Use when the question is which tests/checks are sufficient, or after an authorised change needs verification. Do not invoke it just because tests exist nearby.

## Classify first
Environment: LOCAL / ISOLATED / SHARED / LIVE.
Effect: PURE / READ-ONLY / MUTATING.
PURE and READ-ONLY are not the same: a read-only check can still contact a shared/live system.

## Procedure
1. State the claim the test must prove and identify the known change surface. If that surface is explicitly known and the task forbids repository inspection or test execution, respect that boundary: give a recommendation only, without inspecting or running anything. Make the answer useful despite the boundary by naming the smallest sufficient test category and what it should cover.
2. Choose the lowest-cost, lowest-effect rung that can genuinely prove it: focused unit/static check → targeted integration → broader regression/build → isolated rendered/E2E → shared/live only when it adds necessary evidence. For one changed pure helper with a known surface, ordinarily recommend only its focused unit test: assert the changed behavior and relevant boundary cases tied to its contract. Do not automatically add contract, integration, broader regression, or build checks just because the helper is described as having a known change surface; add a higher-level test only when the specific contract/dependency boundary requires evidence the focused test cannot provide. Do not add unrelated helper tests. If repository inspection and test execution are explicitly forbidden, give this recommendation without inspecting or running tests, and clearly state no verification was performed. If asked only to recommend (not execute), do not imply that any test was run or passed.
3. Reuse fresh passing evidence when tested code/config and relevant environment are unchanged.
4. Escalate only when the lower rung cannot prove the claim or failed in a way that requires broader evidence.
5. Before any SHARED/LIVE MUTATING test, verify explicit authority for that exact side effect.
6. If the focused test runner is unavailable, do not broaden the test scope. Use the smallest equivalent authorized local check that can prove the claim (for example, direct standard-library assertions for a pure function), if permitted and accessible. Ensure the fallback command is syntactically valid and runs from an allowed workspace-relative path; avoid shell quoting layers when a simpler multiline or temporary-in-workspace script can express the assertions. Treat a rejected/failed attempt as no verification evidence, correct the command or path, and retry only the same focused check. If no equivalent check is feasible, report the dependency/access blocker and leave verification partial rather than imply a pass. Report what passed, what was not run, environment, effect, and evidence gap.

## Guardrails
Never broaden merely for reassurance. Previous implementation approval does not imply permission for shared/live mutation. Load this skill once per stable change surface; do not reload it merely because a command was denied, an environment was busy, or unchanged evidence needs no new routing decision.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]