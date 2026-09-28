[Reading 46 lines from start (total: 46 lines, 0 remaining)]

---
name: "cino-evidence-handoff"
description: "Relevant at a worker/task completion handoff boundary. REQUIRED: call skill.view for cino-evidence-handoff before composing the handoff. Discovery summary only."
category: "Cino AgentOps Trial"
state: "active"
created_by: "user"
source_run_id: ""
pinned: false
---

# Cino Evidence Handoff

Emit exactly one compact handoff at the completion boundary. If the user supplies all required receipt facts and asks for the handoff, use this procedure immediately and emit exactly one receipt—never announce that you will load the procedure, narrate internal tool use, or delay the receipt. Keep it compact by combining fields into a few labeled lines; include every required category, but do not add generic explanation. Do not narrate internal procedure-loading or tool use before the receipt. When the supplied evidence is complete and task status is explicitly complete, present the receipt directly without asking follow-up questions. Before emitting, check that each required field is represented; use the supplied facts as evidence and do not treat stated PASS as independent verification.

Task status: COMPLETE | BLOCKED | FAILED | INCOMPLETE EVIDENCE
Verification: PASS | FAIL | PARTIAL | NOT RUN

Base:
- repo/project
- branch
- SHA/version where relevant

Scope:
- exact files/services/sources

Evidence:
- 1-8 concrete pointers, with observed outputs stated precisely and without implying stronger verification than the evidence supports
- For a direct function/example check, preserve the supplied input and returned output verbatim where practical; label it as an observed result, not as a broader test-suite or runtime guarantee. Do not normalize formatting or numeric representation: e.g. if the recorded output is `20`, report `20`, not `20.0`, even when numerically equivalent.

Changes:
- exact files or none

Side effects:
- none observed
  OR
- exact persistent side effects

Unknowns/conflicts:
- only decision-relevant items

Next action:
- one smallest safe action
  OR
- none â€” task complete

Fail if it dumps a transcript, invents a next task, omits persistent side effects, exposes secrets, or claims a test/SHA/state not actually verified. Do not emit multiple intermediate handoff summaries.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]