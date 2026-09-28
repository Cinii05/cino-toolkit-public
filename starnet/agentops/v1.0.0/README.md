[Reading 40 lines from start (total: 40 lines, 0 remaining)]

# Cino AgentOps Core v1.0.0

Cino AgentOps is a procedural coordination pack for StarNet. It separates planning, source-of-truth checks, routing, repository navigation, test selection, evidence handoff, and skill-governance decisions so agents do not collapse those concerns into one generic workflow.

## Release contents

The public v1.0.0 release contains eight core skills:

1. `cino-context-funnel`
2. `cino-source-of-truth`
3. `cino-agent-router`
4. `cino-repo-navigator`
5. `cino-test-router`
6. `cino-evidence-handoff`
7. `cino-plan-before-build`
8. `cino-skill-governor`

It also includes `cino-skill-governor-approval-model` as an internal reference dependency. That reference is not intended to be invoked directly.

## Install / inspect

Use the Cino registry URL:

`https://raw.githubusercontent.com/Cinii05/cino-toolkit-public/main/.well-known/starnet-skills.json`

StarNet can inspect an entry's public `SKILL.md`, calculate the canonical package digest, run its skill guard, and then stage installation through the normal Skill Exchange lifecycle.

## Integrity

The registry `digest` for each entry is the canonical StarNet package SHA-256 for the exact published bytes. The `packages/` directory also contains the sealed `.starnet-skill.json` export for each skill.

Local acceptance before publication covered the A1-A12 trigger/precedence suite and a real isolated A7 implementation run. Publication itself does not increase any skill's authority.

## Release manifest

See `manifest.json` for the exact public registry entries, package digests, role split, and accepted local bundle fingerprint.

## Licensing

License metadata is unspecified in v1.0.0. The public registry does not invent a licence identifier.

[executed on device: MSI (9be8527d-5592-425c-8ea9-07536be5a529)]