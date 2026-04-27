---
atomic_guid: "514e9cd7-9207-4882-98b1-c8f791bae3c5"
title: "Map Admin Share PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.002"
attack_technique_name: "Remote Services: SMB/Windows Admin Shares"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "514e9cd7-9207-4882-98b1-c8f791bae3c5"
  - "Map Admin Share PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Map Admin Share PowerShell

Map Admin share utilizing PowerShell

## Metadata

- Atomic GUID: 514e9cd7-9207-4882-98b1-c8f791bae3c5
- Technique: T1021.002: Remote Services: SMB/Windows Admin Shares
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1021.002/T1021.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Input Arguments

### computer_name

- description: Target Computer Name
- type: string
- default: Target

### map_name

- description: Mapped Drive Letter
- type: string
- default: g

### share_name

- description: Examples C$, IPC$, Admin$
- type: string
- default: C$

## Executor

- name: powershell

### Command

```powershell
New-PSDrive -name #{map_name} -psprovider filesystem -root \\#{computer_name}\#{share_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml)
