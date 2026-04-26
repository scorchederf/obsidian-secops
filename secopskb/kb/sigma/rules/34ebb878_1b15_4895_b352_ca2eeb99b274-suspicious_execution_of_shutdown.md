---
sigma_id: "34ebb878-1b15-4895-b352-ca2eeb99b274"
title: "Suspicious Execution of Shutdown"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_shutdown_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_shutdown_execution.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "34ebb878-1b15-4895-b352-ca2eeb99b274"
  - "Suspicious Execution of Shutdown"
attack_technique_ids:
  - "T1529"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution of Shutdown

Use of the commandline to shutdown or reboot windows

## Metadata

- Rule ID: 34ebb878-1b15-4895-b352-ca2eeb99b274
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-01
- Source Path: rules/windows/process_creation/proc_creation_win_shutdown_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Detection

```yaml
selection:
  Image|endswith: \shutdown.exe
  CommandLine|contains:
  - '/r '
  - '/s '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1529/T1529.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_shutdown_execution.yml)
