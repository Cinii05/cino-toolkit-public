[Reading 28 lines from start (total: 28 lines, 0 remaining)]

---
name: "cino-skill-governor-approval-model"
description: "StarNet reference adapter for cino-skill-governor. Load only when install, promotion, update, rollback, retirement or another persistence lifecycle decision is material."
category: "Cino AgentOps Trial"
state: "active"
created_by: "agent"
source_run_id: "fd85fa39-cb23-47b6-a1f3-5eb793dab7be"
pinned: false
---

# Approval Model

Use only when cino-skill-governor reaches a persistence lifecycle decision.

Keep lifecycle state separate from the requested change. An already installed global skill remains INSTALLED_GLOBAL while an UPDATE request is pending. A stated candidate version and reviewer recommendation do not establish that the candidate package has been received or reviewed; keep candidate content, digest, provenance, and reviewer evidence explicitly unavailable when not supplied.

For install/update/promotion/rollback/retirement record: current lifecycle state; change_request; candidate version/digest/provenance (mark unavailable fields explicitly rather than inventing them); requested scope, distinguishing explicit from inferred; reviewer recommendation if any; approval_state PENDING | APPROVED | REJECTED | CANCELLED; rollback target where relevant. Keep lifecycle state separate from the change request: a pending update does not create a staged, installed, or updated state. If approval is pending or absent, stop before execution. State explicitly that no change was made, identify the unchanged installed version/state, and preserve the current lifecycle state. A reviewer recommendation alone never changes approval_state to APPROVED. Do not describe a candidate as staged or reviewed without evidence of those steps; preserve the installed version as the active lifecycle state until an authorized update actually executes.

## Human Authority boundary
Global install or promotion requires Human Authority. Updating an already globally installed Cino skill also requires Human Authority. A designated senior reviewer may inspect, test and recommend, but cannot self-approve. For an already-installed global skill update, retain lifecycle state INSTALLED_GLOBAL and the current version as active while recording UPDATE as pending; favorable reviewer recommendation does not satisfy the Human Authority gate. When governance procedures are readable but candidate package/version/digest/provenance are absent, report the known lifecycle path and Human Authority gate anyway; mark only the missing candidate evidence unavailable. Do not claim the governance path is uninspectable merely because candidate details are missing. In a stop-at-gate report, explicitly list current state, UPDATE request, PENDING approval, active version unchanged (or mark its identifier unavailable), candidate metadata unavailable if absent, reviewer recommendation as evidence only, and no mutation. Do not solicit approval when explicitly told to stop. If instructed to stop at the gate, report pending approval and no mutation without soliciting approval. Rejection/cancellation leaves the approved version and lifecycle state unchanged.

## Third-party install review
Inspect read-only first. Review permissions, scripts, network behaviour, telemetry/data handling, provenance/license and package/version. Do not enable auto-update or expand permissions silently. If package bytes or metadata are absent, explicitly mark each uninspectable field unavailable; do not infer safety, duplication, provenance, or license from a name/version description. A duplicate check requires enough candidate content to compare against existing skills; otherwise record it as undetermined.

For a requested global third-party install, keep the lifecycle state distinct from the request: if no installed state is evidenced, record current state as NOT_INSTALLED (or unknown if the inventory is incomplete), the explicit requested scope, and approval_state PENDING until Human Authority is given. When the applicable approval model has been read, report the prescribed governance path and Human Authority gate based on that source; do not say the path or gate is unverifiable merely because package materials or an inventory are unavailable. Distinguish these evidence gaps: governance procedure inspected, package/provenance review unavailable if materials were not supplied, and inventory state unknown unless checked. Stop without installation or trial unless separately authorized. Request the actual package and provenance for read-only review before the approval decision where review evidence is required. When the user explicitly says to stop at the Human Authority gate, do not seek or imply approval in the same response; provide the pending decision state and the minimum evidence needed to resume review, then stop.

## Trial
A local controlled trial may be authorised separately from global trust. Trial success is evidence for a later promotion request, not promotion itself.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]