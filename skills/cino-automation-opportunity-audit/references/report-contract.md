# Automation Opportunity Audit report contract

Use this structure unless the user requests another format.

## 1. Decision
CONTINUE | MODIFY | PAUSE | REJECT

## 2. Audit scope
Workflow, outcome, people, systems, evidence inspected, and coverage gaps.

## 3. Evidence register
Use CLIENT_FACT, SOURCE_FACT, DIRECT_INFERENCE, ASSUMPTION, or UNKNOWN.

## 4. Current-state workflow
Show step, actor, system, input/action/output, time/wait, exception/approval.

## 5. Bottlenecks
Show rank, evidence, consequence, and root cause.

## 6. Task classifications
Use only the classifications in opportunity-scoring.md.

## 7. Conservative economics
Show formulas and periods. Separate known measurable value, scenario assumptions, setup cost, ongoing cost, support burden, and unknown components.
If evidence is insufficient, state: NOT CALCULABLE FROM CURRENT EVIDENCE.

## 8. Risk register
Show risk, severity, trigger, control, and residual/unknown.

## 9. Ranked opportunities
Include existing-feature or process-first recommendations when they dominate.

## 10. Smallest testable intervention
Include trigger, steps, human gate, output, failure alert, fallback, logging, acceptance measures, rollback, and trial scope.

## 11. Next safe action
The smallest next step that reduces uncertainty or produces evidence. The report is not implementation authorization.
