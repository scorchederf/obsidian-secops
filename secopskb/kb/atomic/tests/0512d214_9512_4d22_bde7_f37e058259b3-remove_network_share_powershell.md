---
atomic_guid: "0512d214-9512-4d22-bde7-f37e058259b3"
title: "Remove Network Share PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.005"
attack_technique_name: "Indicator Removal on Host: Network Share Connection Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0512d214-9512-4d22-bde7-f37e058259b3"
  - "Remove Network Share PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remove Network Share PowerShell

Removes a Network Share utilizing PowerShell

## Metadata

- Atomic GUID: 0512d214-9512-4d22-bde7-f37e058259b3
- Technique: T1070.005: Indicator Removal on Host: Network Share Connection Removal
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1070.005/T1070.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Input Arguments

### share_name

- description: Share to remove.
- type: string
- default: \\test\share

## Executor

- name: powershell

### Command

```powershell
Remove-SmbShare -Name #{share_name}
Remove-FileShare -Name #{share_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml)
