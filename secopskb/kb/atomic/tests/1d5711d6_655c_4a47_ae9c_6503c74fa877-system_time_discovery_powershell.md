---
atomic_guid: "1d5711d6-655c-4a47-ae9c-6503c74fa877"
title: "System Time Discovery - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1124"
attack_technique_name: "System Time Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1d5711d6-655c-4a47-ae9c-6503c74fa877"
  - "System Time Discovery - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# System Time Discovery - PowerShell

Identify the system time via PowerShell. Upon execution, the system time will be displayed.

## Metadata

- Atomic GUID: 1d5711d6-655c-4a47-ae9c-6503c74fa877
- Technique: T1124: System Time Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1124/T1124.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1124-system_time_discovery|T1124]]

## Executor

- name: powershell

### Command

```powershell
Get-Date
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml)
