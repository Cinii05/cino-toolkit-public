# Install Cino AgentOps Companion v0.1.0

## 1. Download the canonical package

Download:

`https://github.com/Cinii05/cino-toolkit-public/releases/download/cino-agentops-companion-v0.1.0/cino-agentops-starnet-plugin-0.1.0.zip`

Expected SHA-256:

`12b93bdb41beaebb5e489671c74e6a4a06e51c22161b9d47ef8e9b7ad718cc03`

On Windows PowerShell:

```powershell
Get-FileHash .\cino-agentops-starnet-plugin-0.1.0.zip -Algorithm SHA256
```

Do not continue if the checksum differs.

## 2. Extract into the StarNet plugins workspace

Create a plugin directory named:

`cino-agentops`

For the standard Windows StarNet workspace used by the verified build, the destination is:

`%APPDATA%\ai.skynet.harness\workspaces\plugins\cino-agentops\`

Extract the ZIP so the directory contains:

```text
cino-agentops/
  index.js
  plugin.json
  README.md
  assets/
    icon.svg
```

Do not add `data/runs.jsonl` from another machine. The plugin creates its own local telemetry file when it runs.

## 3. Restart StarNet

Restart StarNet so the plugin scanner reloads the workspace.

## 4. Review and approve the exact plugin digest

Open StarNet's plugin controls and inspect **Cino AgentOps Companion v0.1.0**.

For the exact verified v0.1.0 `index.js`, the expected StarNet main-code digest is:

`636eba9eddd4e16b3734231b92406cd34e94487698a3dc07eb914cbc8209ac27`

StarNet binds approval to the code digest. If the code changes, approve only after reviewing the changed source.

The verified v0.1.0 scan produced **no findings**.

## 5. Confirm active state

After approval, the plugin should report:

- name: `Cino AgentOps Companion`
- version: `0.1.0`
- active: `true`
- pending: `false`

## Privacy and data handling

Run receipts stay on the local StarNet machine in:

`workspaces/plugins/cino-agentops/data/runs.jsonl`

The plugin does not transmit those receipts and has no network call path in v0.1.0.

## Uninstall

Remove or disable the `cino-agentops` plugin through StarNet's plugin controls. If removing the folder manually, stop StarNet first and then delete the plugin directory. Removing the plugin does not remove or alter the AgentOps skills.
