---
name: cino-automation-opportunity-audit
description: Diagnose a real business workflow before a concrete automation solution, plan, or specification exists, and decide what should or should not be automated. Use for current-state workflow mapping, bottleneck diagnosis, automation-opportunity ranking, conservative business-case analysis, and smallest safe pilot definition from raw operational evidence. Prefer existing product features, process fixes, or human handling when they dominate custom automation. If a concrete automation plan, specification, vendor choice, claim, or implementation proposal already exists and the user wants it reviewed or challenged, use cino-critical-review instead. Do not use for open-ended interview mode, website/UI audits, prose rewriting, teaching, video extraction, or implementation/deployment.
---

# Cino Automation Opportunity Audit

Diagnose the workflow before recommending technology. The objective is not to find an automation at any cost; it is to identify the smallest justified intervention that improves a real business outcome.

## Operating boundary

- Audit and specify only. Do not deploy, purchase, message customers, change production systems, create accounts, or perform other external mutations unless the user separately and explicitly authorizes a later implementation workflow.
- Never invent labour volumes, staff costs, conversion rates, savings, error rates, revenue, support burden, tool pricing, or integration capability.
- Never guarantee savings, revenue, headcount reduction, or ROI.
- Treat a native feature in the client's existing system, a process change, a template, training, or continued human judgment as valid outcomes.
- High-impact financial, legal, medical, safety, employment, identity, permission, or irreversible actions require explicit human approval and cannot be proposed as unsupervised first pilots.
- Separate facts from inferences, assumptions, and unknowns. Missing evidence weakens the recommendation.

## Required references

Read discovery-framework.md to structure evidence collection and the current-state workflow.
Read opportunity-scoring.md to classify tasks and rank opportunities without false precision.
Read risk-and-boundaries.md before recommending any automation that writes, sends, approves, pays, deletes, discloses, or changes consequential state.
Read report-contract.md for the required audit output.
Read routing-and-precedence.md when this skill overlaps another Cino Toolkit skill.
Read acceptance-criteria.md only when validating or revising this skill itself.

## Evidence labels

Use these labels for decision-changing claims:

- CLIENT_FACT — stated by the client/user or supplied in their records.
- SOURCE_FACT — directly established from an inspected system, file, documentation, or authoritative source.
- DIRECT_INFERENCE — follows reasonably from established facts.
- ASSUMPTION — a provisional value or condition used only to explore a scenario.
- UNKNOWN — needed before the recommendation can safely depend on it.

Do not relabel an assumption as a fact because it produces a convenient business case.

## Audit workflow

### 1. Define the outcome

Identify the business outcome, actors, trigger, end state, current systems of record, known volume/frequency, observed pain, and the decision the audit must support.

Ask only for missing information that materially changes the ranking or safety decision. If enough evidence already exists, proceed and record the gaps.

### 2. Map the current state

Represent the workflow as ordered steps:
trigger -> input -> action -> decision -> write/send -> exception -> completion

For each material step, record actor, system/tool, input, action, output, wait time if known, manual time if known, error/rework signal if known, approval boundary, and exception path.

Do not infer hidden steps merely because they are common in the industry.

### 3. Identify the real bottleneck

Distinguish repetitive manual work, waiting/latency, duplicate entry, missed follow-up, inconsistent decisions, missing information, avoidable errors, poor handoff, bad process design, inadequate existing configuration, and genuinely judgment-heavy work.

Rank the bottleneck before discussing tools.

### 4. Classify each candidate task

Use one of:

- AUTOMATE_CANDIDATE — repetitive, bounded, measurable, and safely automatable.
- PILOT_WITH_HUMAN_GATE — automation may help, but a consequential action needs review/approval.
- USE_EXISTING_FEATURE — the incumbent system already provides an adequate capability.
- PROCESS_FIRST — a simpler operating-process change dominates software.
- KEEP_HUMAN — judgment, empathy, negotiation, or accountability is the core value.
- NEEDS_EVIDENCE — evidence is insufficient for a responsible automation decision.
- DO_NOT_AUTOMATE — risk, fragility, cost, or low value clearly outweighs likely benefit.

Classification is not a maturity score. Do not force every task toward automation.

If no material problem, measurable consequence, or credible opportunity is demonstrated, classify DO_NOT_AUTOMATE and normally REJECT. If whether a problem exists is itself unknown, classify NEEDS_EVIDENCE and PAUSE instead of assuming pain.

### 5. Quantify conservatively

When the necessary facts exist, calculate transparent ranges rather than a single optimistic ROI number.

Useful formulas:

- hours_per_period = volume * minutes_per_item / 60
- hours_saved_range = volume * minutes_saved_range / 60
- labour_value_range = hours_saved_range * loaded_hourly_cost_range
- net_value_range = measurable_benefit_range - setup_cost - ongoing_cost_range

State the period and units.

If volume, time saved, loaded labour cost, error cost, conversion impact, setup cost, or operating cost is unknown, leave that component unknown. Do not substitute industry averages unless the user explicitly asks for a scenario model and the assumption is labelled.

Avoid double-counting the same benefit as both labour saving and revenue gain.

### 6. Check existing capabilities before custom build

Before recommending custom software or orchestration, determine whether the current CRM, booking, accounting, helpdesk, form, email, or vertical SaaS already provides the needed feature or a reliable integration.

If an existing feature adequately solves the problem, recommend using/configuring it first.

### 7. Build the risk register

Check wrong-recipient/wrong-record risk, duplicate/missed action, permissions, secrets, privacy, consent, consequential actions, irreversible writes/deletes, vendor dependency, exception handling, monitoring/support burden, and rollback/manual fallback.

Prefer reversible, observable first pilots.

### 8. Rank opportunities

Prioritize clear pain, measurable volume/consequence, bounded input/output, manageable exceptions, reversibility, reliable access, low support burden, and short path to evidence.

Do not rank by novelty or AI intensity.

### 9. Specify the smallest testable intervention

Define:
- trigger;
- inputs;
- deterministic steps;
- AI/judgment step only if genuinely needed;
- human approval point;
- outputs;
- failure alert;
- manual fallback;
- logging/evidence;
- acceptance measures;
- rollback/removal path;
- trial period or sample size.

### 10. Give a decision

Choose one:

- CONTINUE — evidence supports a bounded pilot or configuration change now.
- MODIFY — the opportunity is real, but scope, authority, safety, or design must change before a pilot.
- PAUSE — missing evidence or access prevents a responsible decision.
- REJECT — automation/custom build is not justified; another approach dominates or the risk/value balance is poor.

A rejection of custom automation can still recommend an existing feature or process improvement.

## Required output

At minimum include:
1. Decision and one-sentence reason
2. Evidence quality and unknowns
3. Current-state workflow
4. Bottleneck table
5. Task classifications
6. Conservative value/cost analysis
7. Risk register
8. Ranked opportunities
9. Smallest testable intervention
10. Measurements and rollback
11. Next safe action

Keep the report decision-ready. Do not bury the verdict under generic AI commentary.
