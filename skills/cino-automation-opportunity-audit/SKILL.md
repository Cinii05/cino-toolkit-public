---
name: cino-automation-opportunity-audit
description: Audit a business workflow to find, rank, scope, price, and test worthwhile automation opportunities. Use when a user asks what a business should automate, wants an AI or automation audit, needs a workflow mapped, wants ROI or feasibility assessed, needs a smallest viable automation defined, or wants service opportunities extracted for Cino Engine A or the Tiny Automations Library. Separate measured facts from claims and assumptions, reject tool-first or unsafe automation, and produce a decision-ready audit rather than implementing changes.
---

# Cino Automation Opportunity Audit

Find the smallest automation that solves a measured business problem. Do not begin with a tool, agent, or interface. Begin with the workflow, evidence, failure modes, and decision the audit must support.

## Operating boundary

- Work read-only unless implementation is separately authorised.
- Never invent volumes, wages, conversion rates, error rates, savings, prices, permissions, or system capabilities.
- Label each important input as source fact, observed evidence, direct inference, assumption, or unknown.
- Verify unstable or material claims with current authoritative sources. This includes laws, platform capabilities, product pricing, security requirements, and regulated workflows.
- Confirm the relevant jurisdiction before making legal, privacy, employment, tax, or sector-specific conclusions. Flag legal questions for qualified review rather than presenting the audit as legal advice.
- Reject deceptive activity, copying without rights, impersonation, unsafe credential handling, and unsupervised high-impact decisions.
- Before reporting a secret exposure from OCR or logs, confirm that a plausible value is present rather than only a label. Do not reproduce suspected credentials in the audit.
- Treat released staff time as capacity, not cash savings, unless the business can remove a real cost or has a measurable plan to reuse that capacity.
- Keep the first implementation narrow, reversible, observable, and supported by a manual fallback.

## Choose the audit mode

1. **Triage** - Decide whether a workflow deserves deeper discovery.
2. **Discovery** - Map the workflow, collect the baseline, and rank candidates.
3. **Full audit** - Produce a decision-ready pilot, value scenarios, controls, and verdict.
4. **Commercial packaging** - Turn an evidenced opportunity into a scoped Cino offer.

For Discovery and Full audit modes, read `references/interview-and-scoring.md`. For the final deliverable, also read `references/audit-report-template.md`.

## Audit workflow

### 1. Establish the decision

Record:

- the business, customer group, workflow, and accountable owner;
- the problem and desired outcome;
- what is inside and outside scope;
- affected systems and manual work;
- legal, contractual, operational, data, and budget constraints;
- success, failure, and stop conditions.

If the decision is unclear, ask focused questions before calculating value.

### 2. Build an evidence ledger

Collect the minimum facts needed to test the case:

- event volume and seasonality;
- staff touch time and waiting time;
- errors, rework, missed enquiries, no-shows, churn, or delays;
- loaded labour cost, avoidable cost, and gross contribution per recovered outcome;
- implementation, software, model, monitoring, support, and correction costs;
- system access, APIs, permissions, consent, and data availability;
- common exceptions, failure paths, and recovery work.

Keep creator claims, vendor claims, management estimates, sampled records, and measured baselines separate. Do not upgrade an estimate into a fact through repetition.

### 3. Map the current workflow

For each step capture the trigger, owner, input, system, action, decision, output, handoff, touch time, wait time, frequency, exceptions, and recovery path.

Identify the actual constraint. A slow handoff, unclear rule, bad data, duplicated entry, or unnecessary approval may matter more than the visible task. Recommend removing or simplifying a step when that is better than automating it.

### 4. Generate interventions in the right order

Consider candidates in this order:

1. Remove the unnecessary step.
2. Clarify the rule or ownership.
3. Configure the existing system.
4. Use deterministic automation.
5. Use AI when interpretation or generation is genuinely required.
6. Use an agent only when a bounded but open-ended action path creates enough value to justify the added control burden.

Do not recommend an AI agent where a form, webhook, template, rule, or queue will do the job more reliably.

### 5. Score candidates and apply gates

Use the scoring model in `references/interview-and-scoring.md`. Show the component scores and supporting evidence, not only the total.

Apply gates before recommending implementation:

- **Reject** if the activity is illegal, deceptive, rights-infringing, unauthorised, or cannot be made acceptably safe.
- **Pause** when authority, consent, security, regulation, data rights, or critical vendor capability is unresolved.
- **Simplify first** when the underlying process is unstable or poorly owned.
- **Discovery only** when the baseline is too weak to support ROI.
- **Pilot** when delivery and economics are plausible but uncertain.
- **Adopt** only when live evidence meets the agreed thresholds.

Hard gates override the numeric score.

### 6. Model value conservatively

Create low, base, and high scenarios. Separate:

- time capacity released;
- avoidable cash cost;
- recoverable gross contribution;
- one-time implementation cost;
- recurring software, model, monitoring, support, and correction costs;
- risk-adjusted monthly net value and payback.

Do not double-count labour capacity and payroll savings. Do not treat revenue as profit. Reduce expected value for adoption, exceptions, failure, review time, and ramp-up. If the inputs are assumptions, present scenario maths, not a proven ROI claim.

If a material input cannot be bounded honestly, mark net value or payback **not calculable yet** and state the measurement needed. Never create a scenario merely to fill the table.

### 7. Define the smallest viable pilot

Specify:

- user, problem, trigger, input, steps, output, and exclusions;
- integrations, permissions, and data boundaries;
- human approvals, alerts, manual fallback, retry, and rollback;
- logging, retention, and audit requirements;
- measures, sample size or duration, owner, and review date;
- pass, change, and stop thresholds.

Prefer shadow mode, drafts, recommendations, or human confirmation before autonomous external actions.

Choose duration and sample size to cover normal operating variation, known peak periods, and enough eligible cases to expose common failures. Derive thresholds from the current baseline, customer harm tolerance, and operational capacity; label unvalidated thresholds as provisional.

### 8. Package a commercial offer only after evidence

Where appropriate, separate:

- paid discovery and baseline measurement;
- implementation and integration;
- third-party software and usage costs;
- training and operating documentation;
- monthly monitoring, support, optimisation, and change allowance.

Price from delivery effort, risk, ongoing support, and credible customer value. Mark untested pricing and demand as hypotheses. Never imply guaranteed savings or outcomes.

### 9. Issue the verdict

Use one verdict: **Continue**, **Modify**, **Pause**, or **Reject**.

- **Continue** when the proposed next step is suitably scoped and no unresolved gate blocks it.
- **Modify** when a narrower or materially changed version can proceed while broader elements are excluded.
- **Pause** when the useful next step itself is blocked by missing authority, evidence, access, or controls.
- **Reject** when the case is unsafe, uneconomic, unnecessary, or inferior to a non-automation change.

State the next action, owner, missing evidence, and next decision point. End with a plain-English verdict and the main worries or limitations.

## Quality checklist

Before delivering the audit, confirm that:

- the recommendation addresses the real constraint;
- facts, claims, inferences, assumptions, and unknowns are visibly separated;
- current material claims have authoritative support;
- every number can be traced to an input and formula;
- time capacity is not mislabelled as cash savings;
- risk, privacy, permissions, security, and failure recovery are covered;
- the pilot is smaller than the full vision and can be reversed;
- success and stop rules are measurable;
- the commercial offer follows evidence rather than hype;
- the verdict is explicit even when the answer is no.
