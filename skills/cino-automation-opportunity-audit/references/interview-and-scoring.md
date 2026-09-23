# Interview and scoring guide

Use this guide for Discovery and Full audit modes. Ask only questions that affect the decision. Prefer records, samples, exports, screenshots, logs, and direct observation over confident estimates.

## Discovery interview

### Business and outcome

- What result matters, to whom, and by when?
- Who owns the workflow and who can approve a change?
- What happens if nothing changes?
- Which outcomes must not be degraded?

### Workflow and volume

- What starts the workflow and what counts as complete?
- Who performs each step, in which system, and how often?
- What are the touch time, wait time, peaks, and seasonality?
- Which decisions require judgement and which follow stable rules?
- What are the common exceptions and recovery paths?

### Pain and evidence

- What is missed, delayed, duplicated, reworked, or abandoned?
- Is the pain supported by logs, records, time samples, or only recollection?
- What is the loaded cost of the work?
- For recovered outcomes, what is the gross contribution rather than top-line revenue?
- How is released capacity expected to be used?

### Systems, permissions, and data

- Which systems hold the source of truth?
- Are APIs, webhooks, exports, sandbox access, and test accounts actually available?
- Who owns the accounts, credentials, data, and vendor relationship?
- Does the workflow involve personal, confidential, financial, health, employment, or children's data?
- What consent, retention, deletion, audit, access-control, and residency rules apply?
- Which actions require human authority or customer confirmation?

### Delivery and support

- What should happen when the automation is wrong, late, duplicated, or unavailable?
- Who receives alerts and who can intervene?
- Is there a manual fallback, retry rule, rollback path, and audit trail?
- Who will maintain prompts, rules, integrations, credentials, and vendor changes?

### Commercial test

- Who experiences the pain, who owns budget, and who signs?
- What does the business already pay for the problem or an adjacent tool?
- Is discovery chargeable before implementation?
- What implementation, training, monitoring, and support will Cino actually provide?
- Which parts can be reused across customers without exposing customer data or copying proprietary work?

## Evidence ledger

For each material input, record:

| Field | Meaning |
|---|---|
| Input or claim | The exact statement or number |
| Classification | Source fact, observed evidence, direct inference, assumption, or unknown |
| Source | Record, person, system, sample, vendor document, or authoritative publication |
| Period and sample | Date range, count, and known exclusions |
| Confidence | High, medium, or low, with a short reason |
| Decision affected | Which recommendation or calculation depends on it |
| Validation action | What would confirm or disprove it |

Use these classifications consistently:

- **Source fact**: directly supported by a supplied authoritative record or reliable system output.
- **Observed evidence**: directly inspected behaviour, media, sample, screenshot, or workflow execution, with its limits stated.
- **Direct inference**: a conclusion that follows from identified facts without adding an unsupported premise.
- **Assumption**: a provisional input used to explore a scenario, not an established fact.
- **Unknown**: missing information that has not been responsibly bounded.

A statement supplied in a brief remains a management or requester claim until its supporting record is inspected.

## Candidate scoring

Score each component from 0 to 3. Explain every score.

Use the general anchor: **0 = absent or adverse, 1 = weak, 2 = adequate, 3 = strong**. For the risk penalty, reverse the direction: **0 = negligible, 1 = low, 2 = material but controllable, 3 = severe or difficult to control**. Calibrate scores comparatively within the same audit and explain the evidence behind them.

### Benefit, maximum 12

- **Frequency**: rare to frequent and sustained.
- **Impact**: trivial to materially affecting cost, contribution, speed, quality, or customer experience.
- **Measurability**: subjective to clean baseline and outcome measure.
- **Reusability**: one-off to repeatable across customers or workflows.

### Feasibility, maximum 12

- **Process stability**: changing and ambiguous to stable and owned.
- **Data quality**: missing and inconsistent to available, representative, and governed.
- **Integration readiness**: manual or unconfirmed access to supported, testable interfaces.
- **Fallback quality**: no safe recovery to clear human fallback, alerting, and rollback.

### Evidence strength, maximum 3

- **0**: unsupported claim.
- **1**: anecdote or rough estimate.
- **2**: records or a limited representative sample.
- **3**: measured baseline across a suitable period.

### Risk penalty, maximum 12

- **Failure consequence**: negligible to severe customer, operational, financial, or safety harm.
- **Data sensitivity**: public or low sensitivity to regulated or highly confidential.
- **External action risk**: internal suggestion to irreversible or high-impact external action.
- **Maintenance burden**: stable rules to frequent model, vendor, policy, or workflow change.

Use:

`priority score = benefit + feasibility + evidence strength - risk penalty`

Interpret the score only after applying hard gates:

| Score | Default interpretation |
|---:|---|
| 18 to 27 | Strong candidate if no hard gate remains |
| 11 to 17 | Pilot, reduce scope, or collect targeted evidence |
| 4 to 10 | Weak candidate; simplify or deprioritise |
| 3 or below | Reject or redesign |

The score is a comparison aid, not proof of ROI. A hard gate overrides it.

Do not penalise the same unknown mechanically in three places. Use low evidence strength for an unsupported claim, reduce feasibility only when the missing information genuinely obstructs delivery, and add risk only when uncertainty increases the consequence or likelihood of harm. Explain overlaps.

## Value model

Use matching time periods and show all inputs.

`gross hours released = events x minutes saved / 60`

`adjusted hours released = gross hours released x adoption rate x accepted-output rate`

`capacity value = adjusted hours released x loaded hourly cost`

`recoverable gross contribution = opportunities x current loss rate x expected improvement x gross contribution per recovered outcome`

`monthly net cash benefit = avoidable cash cost + recoverable gross contribution - recurring tools - monitoring - support - expected correction cost`

`cash payback months = one-time implementation cost / monthly net cash benefit`

Rules:

- Show low, base, and high scenarios.
- Use gross contribution, not revenue, for recovered sales.
- Show capacity value separately. Count it as avoidable cash cost only when a documented staffing or contractor cost actually falls, or as recoverable gross contribution only when a measured plan turns the released time into extra profitable work. Do not count the same benefit twice.
- Include review time, exceptions, failures, correction, monitoring, support, and ramp-up.
- Do not publish a positive cash payback when monthly net cash benefit is zero or negative. A capacity-only case can still be worth testing for service quality, but its cash payback is not yet established.
- When material inputs are assumptions, call the result a scenario, not an ROI finding.
- When an essential input cannot be bounded responsibly, report the affected result as **not calculable yet** and specify how to measure it.

## Pilot duration and thresholds

- Cover normal operating variation and any known peak, weekend, or month-end behaviour relevant to the workflow.
- Include enough eligible cases to observe common exception types; do not set an arbitrary sample solely for a round number.
- Base correctness, speed, and recovery thresholds on the measured baseline and the consequence of failure.
- Use zero-tolerance stop rules for defined critical harms such as unauthorised payment, dangerous advice, material privacy breach, or uncontrolled duplicate action.
- Label thresholds as provisional until the workflow owner accepts them.
