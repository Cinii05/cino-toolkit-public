# Risk and authority boundaries

## Consequential actions

Treat these as high-impact unless strong context proves otherwise:
- moving or releasing money;
- approving/refusing credit or financial eligibility;
- signing or submitting legal documents;
- deleting authoritative records;
- changing permissions or identity;
- making medical or safety decisions;
- hiring, firing, disciplinary, or materially adverse employment actions;
- sending binding quotes/contracts without required review;
- publishing sensitive/private data;
- irreversible production writes.

The first pilot must not make these actions unattended. Automation may prepare evidence, draft, validate inputs, flag cases, or queue an approval.

## Communication risk

For customer/client messaging identify sender authority, consent/rules, duplicate-send prevention, suppression state where relevant, delivery failure handling, and prohibited claims.

## Data and privacy

Record data classes, systems of record, retention, least privilege, secret handling, logging, deletion/correction, and vendor data exposure.

## Reliability

Every live candidate needs duplicate protection where relevant, failure alerting, observable run state, manual fallback, exception ownership, and rollback/removal.

## Tool-first prohibition

Do not recommend n8n, Zapier, Make, custom code, an agent, or a model simply because it is available. Select implementation only after workflow, risks, constraints, and incumbent capabilities are understood.
