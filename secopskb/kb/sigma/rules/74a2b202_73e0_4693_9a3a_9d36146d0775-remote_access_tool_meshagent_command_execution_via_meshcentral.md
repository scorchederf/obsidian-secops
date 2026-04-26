---
sigma_id: "74a2b202-73e0-4693-9a3a-9d36146d0775"
title: "Remote Access Tool - MeshAgent Command Execution via MeshCentral"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_exec.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "74a2b202-73e0-4693-9a3a-9d36146d0775"
  - "Remote Access Tool - MeshAgent Command Execution via MeshCentral"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - MeshAgent Command Execution via MeshCentral

Detects the use of MeshAgent to execute commands on the target host, particularly when threat actors might abuse it to execute commands directly.
MeshAgent can execute commands on the target host by leveraging win-console to obscure their activities and win-dispatcher to run malicious code through IPC with child processes.

## Metadata

- Rule ID: 74a2b202-73e0-4693-9a3a-9d36146d0775
- Status: test
- Level: medium
- Author: @Kostastsale
- Date: 2024-09-22
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  ParentImage|endswith: \meshagent.exe
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
condition: selection
```

## False Positives

- False positives can be found in environments using MeshAgent for remote management, analysis should prioritize the grandparent process, MeshAgent.exe, and scrutinize the resulting child processes triggered by any suspicious interactive commands directed at the target host.

## References

- https://github.com/Ylianst/MeshAgent
- https://github.com/Ylianst/MeshAgent/blob/52cf129ca43d64743181fbaf940e0b4ddb542a37/modules/win-dispatcher.js#L173
- https://github.com/Ylianst/MeshAgent/blob/52cf129ca43d64743181fbaf940e0b4ddb542a37/modules/win-info.js#L55

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_exec.yml)
