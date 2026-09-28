# Cino AgentOps Companion v0.1.0

First public Companion release for Cino AgentOps.

## What it does

- observes Cino skill activation order;
- counts tool calls and tool errors;
- flags mutation-capable tool calls in local run receipts;
- records memory-write observation and session completion metadata;
- writes one local JSONL receipt per session.

## What it does not do

- no prompt injection;
- no routing decisions;
- no authority or permission changes;
- no call blocking;
- no network calls;
- no telemetry upload.

## Integrity

Canonical ZIP SHA-256:

`12b93bdb41beaebb5e489671c74e6a4a06e51c22161b9d47ef8e9b7ad718cc03`

Verified StarNet main-code approval digest:

`636eba9eddd4e16b3734231b92406cd34e94487698a3dc07eb914cbc8209ac27`

See the versioned source, checksums and install instructions in:

`starnet/plugins/cino-agentops/v0.1.0/`
