---
atomic_guid: "ae753dda-0f15-4af6-a168-b9ba16143143"
title: "Stop and Remove Arbitrary Security Windows Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "ae753dda-0f15-4af6-a168-b9ba16143143"
  - "Stop and Remove Arbitrary Security Windows Service"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Stop and Remove Arbitrary Security Windows Service

Beginning with Powershell 6.0, the Stop-Service cmdlet sends a stop message to the Windows Service Controller for each of the specified services. The Remove-Service cmdlet removes a Windows service in the registry and in the service database.

## Metadata

- Atomic GUID: ae753dda-0f15-4af6-a168-b9ba16143143
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### service_name

- description: The name of the service to remove
- type: string
- default: McAfeeDLPAgentService

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Stop-Service -Name #{service_name}
Remove-Service -Name #{service_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
