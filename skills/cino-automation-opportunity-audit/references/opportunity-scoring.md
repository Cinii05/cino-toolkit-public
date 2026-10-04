# Automation opportunity classification and ranking

Avoid false-precision scores unless the user explicitly needs a numeric model and the inputs are evidence-backed.

## Primary classifications

- AUTOMATE_CANDIDATE: repetitive, bounded, measurable, sufficiently frequent or consequential, technically reachable, and low-risk enough for a controlled pilot.
- PILOT_WITH_HUMAN_GATE: automation can prepare or execute part of the workflow but a consequential action remains human-approved.
- USE_EXISTING_FEATURE: the incumbent product can adequately solve the problem through configuration or supported integration.
- PROCESS_FIRST: a form, checklist, template, policy, batching rule, ownership change, or training change likely solves the main bottleneck more cheaply and reliably.
- KEEP_HUMAN: the value lies primarily in judgment, empathy, negotiation, accountability, contextual discretion, or relationship management.
- NEEDS_EVIDENCE: volume, time, failure rate, system access, exception behaviour, or cost is too uncertain to justify a build decision.
- DO_NOT_AUTOMATE: risk, fragility, support burden, poor system access, low frequency, or weak value clearly dominates.

## Ranking dimensions

Use qualitative LOW / MEDIUM / HIGH with evidence notes:
pain/consequence, repeat volume, time burden, rule clarity, data quality, system accessibility, exception complexity, reversibility, monitoring feasibility, ongoing support burden, privacy/security impact, and consequential-action risk.

Do not average these into a meaningless score. A single severe risk can dominate several attractive dimensions.

## Decision rules

- Existing adequate feature -> USE_EXISTING_FEATURE before custom build.
- Process defect dominates -> PROCESS_FIRST.
- Core work is human judgment -> KEEP_HUMAN.
- Missing decision-critical evidence -> NEEDS_EVIDENCE and normally PAUSE.
- No demonstrated material problem or measurable consequence -> DO_NOT_AUTOMATE and normally REJECT; if the existence of the problem is unknown, use NEEDS_EVIDENCE instead.
- High-impact action with automatable preparation -> PILOT_WITH_HUMAN_GATE, not unattended execution.
- Clear bounded repetitive work with measurable benefit and reversible pilot -> AUTOMATE_CANDIDATE.

Low volume alone does not always kill an opportunity if each event has high consequence. High volume does not justify automating a dangerous or unstable decision.
