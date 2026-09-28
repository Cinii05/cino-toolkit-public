[Reading 25 lines from start (total: 25 lines, 0 remaining)]

---
name: "cino-repo-navigator"
description: "Use for read-only codebase navigation when implementation location or direct dependency surface is unclear."
category: "Cino AgentOps"
state: "active"
created_by: "user"
source_run_id: "e2693b79-64ac-4171-8fe4-dadac1fd44c3_skill_review"
pinned: false
---

# Cino Repo Navigator

## Trigger
Use when asked where code lives, what directly depends on a symbol or flow, or when an implementation workflow needs a narrow code map before editing. Do not use when the exact target file/function is already supplied and clear.

## Procedure
1. Start with search: symbol, route, model, API field, test name, or distinctive string.
2. Build a small candidate list.
3. Read only the definition plus directly relevant callers, contracts/types, configuration and nearby tests.
4. Follow direct edges only until the question is answerable. Prefer current active code over generated output, archives, vendored code, build artefacts, or unrelated migrations.
5. Name candidate tests if useful, but do not choose or execute a test plan unless testing was requested or an implementation workflow hands off to cino-test-router.
6. Return a compact repo map: active files, responsibility of each, direct dependency edges, and remaining unknowns.

## Guardrails
Navigation is read-only. Never edit during this phase and never open secret-bearing or generated data without a concrete reason.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]