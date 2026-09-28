---
name: "cino-source-of-truth"
description: "Relevant when sources conflict or authority must be resolved. REQUIRED: if relevant, call skill.view for cino-source-of-truth before reasoning or answering. Discovery summary only."
category: "Cino AgentOps Trial"
state: "active"
created_by: "agent"
source_run_id: "fd85fa39-cb23-47b6-a1f3-5eb793dab7be"
pinned: false
---

# Cino Source of Truth

## Trigger
Use when explicit sources conflict, or when the task asks what currently governs a consequential claim. If the evidence set is already narrow, start here; do not invoke Context Funnel just for ceremony.

## Procedure
1. Write the exact claim being resolved.
2. Classify the claim: code/implementation, deployed runtime, tests, commercial policy/pricing, product decision, legal/compliance, release authority, or historical context.
3. Match the claim to the authority that can actually prove it. Current repository proves code; live runtime proves deployed behaviour; current approved business authority proves commercial rules. A handoff or memory is a lead unless it is itself governing authority. For a commercial-policy claim that conflicts with runtime behavior, the current approved business authority governs policy; describe runtime as observed implementation behavior and label the mismatch as a policy-versus-implementation discrepancy. Keep policy authority separate from implementation compliance: resolving which source governs policy does not establish whether implementation complies. If the requester supplies the authority and runtime claims but asks a read-only question without providing source access, answer conditionally from the stated premises: identify which source class governs, attribute the conclusion to the supplied facts, and explicitly say the source's current approval/version and the runtime comparison were not independently verified. Do not withhold the general authority mapping merely because source inspection was not performed. When relying only on facts supplied in the prompt, explicitly attribute the conclusion to those supplied facts rather than implying independent source inspection; note missing exact source/version as unknown when material. Do not imply runtime behavior changes or overrides policy.
4. Confirm each cited source was actually readable and reviewed. A supplied path or presumed file-access capability is not proof of access; first check and use the tools actually exposed in the current environment to read sources within scope. If a source cannot be read after that check, mark the claim UNKNOWN / EVIDENCE MISSING, name the precise access/evidence gap, and request the minimum missing input. Do not fabricate findings or imply a comparison occurred.
5. Compare source version, timestamp, environment, branch/SHA, and scope where relevant.
6. Return one of: GOVERNING AUTHORITY FOUND; CONFLICT; UNKNOWN / EVIDENCE MISSING.
6. Never split the difference. Never use runtime behaviour to invent commercial policy, branch state to prove deployment, or an old summary to overrule current evidence.

## Output
Claim; governing authority class; exact source/version; conflicting/stale sources; unresolved unknowns. For activation-only requests, describe the claim-to-authority mapping and conflict procedure without querying sources; do not present any authority as found or current. If the request explicitly asks to load applicable skills, call skill.view on the relevant procedures in the chosen sequence; do not substitute merely naming them or claim the capability is unavailable when exposed.

## Guardrails
Read-only unless an outer authorised workflow explicitly moves beyond evidence resolution. Cannot grant implementation, push, merge, deploy, publish, install, or production authority.
