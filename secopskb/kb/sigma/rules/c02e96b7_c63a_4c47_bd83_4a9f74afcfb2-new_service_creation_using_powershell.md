---
sigma_id: "c02e96b7-c63a-4c47-bd83-4a9f74afcfb2"
title: "New Service Creation Using PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_create_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_create_service.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "c02e96b7-c63a-4c47-bd83-4a9f74afcfb2"
  - "New Service Creation Using PowerShell"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Service Creation Using PowerShell

Detects the creation of a new service using powershell.

## Metadata

- Rule ID: c02e96b7-c63a-4c47-bd83-4a9f74afcfb2
- Status: test
- Level: low
- Author: Timur Zinniatullin, Daniil Yugoslavskiy, oscd.community
- Date: 2023-02-20
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_create_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - New-Service
  - -BinaryPathName
condition: selection
```

## False Positives

- Legitimate administrator or user creates a service for legitimate reasons.
- Software installation

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.003/T1543.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_create_service.yml)
