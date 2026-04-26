---
sigma_id: "2a072a96-a086-49fa-bcb5-15cc5a619093"
title: "Start Windows Service Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_start_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_start_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "2a072a96-a086-49fa-bcb5-15cc5a619093"
  - "Start Windows Service Via Net.EXE"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Start Windows Service Via Net.EXE

Detects the usage of the "net.exe" command to start a service using the "start" flag

## Metadata

- Rule ID: 2a072a96-a086-49fa-bcb5-15cc5a619093
- Status: test
- Level: low
- Author: Timur Zinniatullin, Daniil Yugoslavskiy, oscd.community
- Date: 2019-10-21
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_net_start_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
  CommandLine|contains: ' start '
condition: all of selection_*
```

## False Positives

- Legitimate administrator or user executes a service for legitimate reasons.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1569.002/T1569.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_start_service.yml)
