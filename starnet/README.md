# Cino StarNet Registry

Public StarNet skill registry maintained by Cino.

## Registry URL

`https://raw.githubusercontent.com/Cinii05/cino-toolkit-public/main/.well-known/starnet-skills.json`

The registry uses StarNet's `starnet-skill-registry/v1` format and points to public HTTPS `SKILL.md` sources.

## Published release

**Cino AgentOps Core v1.0.0**

- 8 core AgentOps skills.
- 1 internal approval-model reference used by `cino-skill-governor`.
- Canonical StarNet package digests are included in the registry.
- The published skill bytes are exact copies of the sealed v1 packages that passed the local acceptance gate.
- Publication does not grant broader tool, deployment, account, or external-system authority.

See [the v1.0.0 release record](./agentops/v1.0.0/README.md).

## Licensing

The v1.0.0 skill package license metadata is currently unspecified. No licence identifier is invented by the registry.

## Companion plugin

**Cino AgentOps Companion v0.1.0** is the observe-only StarNet plugin that records local AgentOps runtime receipts without changing agent authority or decisions.

- Plugin index: `starnet/plugins/cino-agentops/`
- v0.1.0 source, checksums and install instructions: `starnet/plugins/cino-agentops/v0.1.0/`
- Public ZIP release: `cino-agentops-companion-v0.1.0`

The plugin is separate from the AgentOps reasoning skills and from the Cino Toolkit ChatGPT/Codex plugin package.
