---
sigma_id: "cd1f961e-0b96-436b-b7c6-38da4583ec00"
title: "Suspicious Windows Trace ETW Session Tamper Via Logman.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_logman_disable_eventlog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_logman_disable_eventlog.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cd1f961e-0b96-436b-b7c6-38da4583ec00"
  - "Suspicious Windows Trace ETW Session Tamper Via Logman.EXE"
attack_technique_ids:
  - "T1562.001"
  - "T1070.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Windows Trace ETW Session Tamper Via Logman.EXE

Detects the execution of "logman" utility in order to disable or delete Windows trace sessions

## Metadata

- Rule ID: cd1f961e-0b96-436b-b7c6-38da4583ec00
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-02-11
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_logman_disable_eventlog.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \logman.exe
- OriginalFileName: Logman.exe
selection_action:
  CommandLine|contains:
  - 'stop '
  - 'delete '
selection_service:
  CommandLine|contains:
  - Circular Kernel Context Logger
  - EventLog-
  - SYSMON TRACE
  - SysmonDnsEtwSession
condition: all of selection*
```

## False Positives

- Legitimate deactivation by administrative staff
- Installer tools that disable services, e.g. before log collection agent installation

## References

- https://twitter.com/0gtweet/status/1359039665232306183?s=21
- https://ss64.com/nt/logman.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_logman_disable_eventlog.yml)
