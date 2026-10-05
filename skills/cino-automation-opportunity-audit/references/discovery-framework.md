# Automation audit discovery framework

Use this to reconstruct the workflow from evidence rather than from a generic automation template.

## Minimum discovery fields

### Outcome
- What outcome is the workflow supposed to produce?
- Who owns the result?
- Who receives or depends on it?
- What currently counts as success/failure?

### Trigger and demand
- What starts the workflow?
- How many times does it occur in a stated period?
- Is volume stable, seasonal, bursty, or unknown?

### Step map
For each step capture step ID, actor, system, input, action, decision rule, output, manual minutes if known, wait time if known, exception path, and approval/permission boundary.

### Pain evidence
Prefer observed evidence such as queue age, missed enquiries, duplicate entry, rework, errors, response time, abandonment, complaints, staff interruption, and support burden.

Do not translate “this is annoying” into a financial loss without measurements.

### Existing systems
Record source of truth, current systems, native automation features, integrations/APIs/webhooks, authentication/permissions, credential ownership, and vendor limits.

### Exceptions
Ask what happens when required information is missing, duplicates exist, customer details conflict, an amount is disputed, a human disagrees, an integration is unavailable, an automation runs twice, or an external message fails.

## Discovery stopping rule

Stop asking questions when there is enough evidence to identify the highest-priority bottleneck, classify the task, determine whether existing features/process changes dominate, describe the smallest safe test, and state remaining unknowns explicitly.
