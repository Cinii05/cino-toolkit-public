# Cino AgentOps Companion v0.1.0

![Cino AgentOps Companion icon](./source/assets/icon.svg)

Observe-only StarNet companion plugin for **Cino AgentOps Core**.

The AgentOps skills own reasoning and procedure. The Companion owns only mechanical runtime telemetry: activation receipts, tool counts, side-effect signals, tool errors, memory-write observation and session completion metadata.

## Download

**Package:** [cino-agentops-starnet-plugin-0.1.0.zip](https://github.com/Cinii05/cino-toolkit-public/releases/download/cino-agentops-companion-v0.1.0/cino-agentops-starnet-plugin-0.1.0.zip)

**SHA-256:** `12b93bdb41beaebb5e489671c74e6a4a06e51c22161b9d47ef8e9b7ad718cc03`

Package size: **2,775 bytes**.

Always verify the SHA-256 before installation. See [SHA256SUMS.txt](./SHA256SUMS.txt).

## Install

See [INSTALL.md](./INSTALL.md) for the exact StarNet installation and approval flow.

## Published source

The exact text files packed into the release ZIP are under [source/](./source/):

- `source/index.js`
- `source/plugin.json`
- `source/README.md`
- `source/assets/icon.svg`

The published raw source was re-fetched from GitHub and its byte-level SHA-256 values match the canonical local v0.1.0 package files.

## Runtime scope

The plugin registers four StarNet lifecycle hooks:

- `on_session_start`
- `post_tool_call`
- `on_memory_write`
- `on_session_end`

It records one local JSONL receipt per completed session under the installed plugin's own `data/runs.jsonl`.

It does **not**:

- inject prompts;
- make routing or skill-selection decisions;
- block tool calls;
- grant permissions or authority;
- call external networks;
- publish telemetry;
- replace the AgentOps skills.

The distribution ZIP contains **no run telemetry**.

## Integrity

Current verified StarNet main-code approval digest for this exact v0.1.0 build:

`636eba9eddd4e16b3734231b92406cd34e94487698a3dc07eb914cbc8209ac27`

That value is also the SHA-256 of the packaged `index.js`.

See [release-manifest.json](./release-manifest.json) for the complete publication record.

## Related

- [Cino AgentOps install page](https://cinii05.github.io/cino-toolkit-public/agentops/)
- [Cino StarNet skill registry](https://cinii05.github.io/cino-toolkit-public/agentops/.well-known/starnet-skills.json)
- [AgentOps Core v1.0.0](../../agentops/v1.0.0/)

## Licensing

No explicit software licence identifier is declared for Companion v0.1.0. Public source visibility should not be interpreted as an additional licence grant.
