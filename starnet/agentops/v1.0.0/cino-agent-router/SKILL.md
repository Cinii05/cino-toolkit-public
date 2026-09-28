---
name: "cino-agent-router"
description: "Relevant when deciding whether and how to delegate work by role. REQUIRED: if relevant, call skill.view for cino-agent-router before making the routing decision. Discovery summary only."
category: "Cino AgentOps Trial"
state: "active"
created_by: "agent"
source_run_id: "fd85fa39-cb23-47b6-a1f3-5eb793dab7be"
pinned: false
---

# Cino Agent Router

## Trigger
Use when delegation is actually useful or the user asks which worker should do a task. Do not load it when one agent can complete a trivial task directly.

## Procedure
1. Classify the task by complexity, risk, scope, and need for independent review.
2. Decide first whether delegation adds value. Prefer no delegation over needless fan-out.
3. Route to stable roles: bounded-worker for narrow implementation/tests/QA/evidence; senior-engineer for difficult or release-sensitive engineering; reviewer for independent verification. For a task explicitly characterized as a bounded backend test fix, select the bounded coding/QA worker, not the senior-engineer role; backend location alone is not a reason to escalate. Do not demand failure logs or implementation details merely to make this role choice when the user has already bounded and classified the task. Ask for more evidence only if the characterization leaves meaningful uncertainty about scope, complexity, or release-sensitive risk. When the request explicitly limits the task to choosing between those roles and forbids implementation, state the role recommendation only: do not implement, initiate delegation, or prepare an implementation brief. Escalate to the senior-engineer role only if investigation reveals cross-repository scope, difficult engineering, or release-sensitive risk. Treat names as runtime mappings, not durable role definitions.
4. Resolve the current runtime roster to an actual worker only after the role is chosen. If the user asks only for the role decision and forbids implementation, this roster lookup and all delegation steps are unnecessary.
5. Give one bounded brief with scope, evidence required, stop condition, and inherited authority.
6. Never use peer-voting fan-out merely to collect opinions.

## Guardrails
Routing does not enlarge authority. A worker inherits at most the caller's allowed scope. Do not hardcode worker or provider/model identities into the procedure.
