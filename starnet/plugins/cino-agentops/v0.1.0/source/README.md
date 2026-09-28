# Cino AgentOps Companion

StarNet companion plugin for the Cino AgentOps core skill pack.

## v0.1.0 scope
- Observe Cino skill activation order.
- Count tool calls and tool errors.
- Flag mutation-capable tool calls in receipts.
- Record memory-write observation and session completion metadata.
- Write one local JSONL receipt per session.

## Non-goals
This plugin does not inject prompts, make routing decisions, grant authority, block calls, call the network, or replace the eight Cino AgentOps reasoning skills.

## StarNet install
Place this folder under the StarNet workspaces/plugins directory. StarNet binds plugin approval to the exact code digest, so changed code must be approved again.

## Privacy
Run receipts remain local to the StarNet workspace. The distribution package contains no run telemetry.
