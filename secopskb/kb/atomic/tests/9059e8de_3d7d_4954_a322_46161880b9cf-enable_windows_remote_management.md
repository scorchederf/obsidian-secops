---
atomic_guid: "9059e8de-3d7d-4954-a322-46161880b9cf"
title: "Enable Windows Remote Management"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.006"
attack_technique_name: "Remote Services: Windows Remote Management"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "9059e8de-3d7d-4954-a322-46161880b9cf"
  - "Enable Windows Remote Management"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enable Windows Remote Management

Powershell Enable WinRM

Upon successful execution, powershell will "Enable-PSRemoting" allowing for remote PS access.

## Metadata

- Atomic GUID: 9059e8de-3d7d-4954-a322-46161880b9cf
- Technique: T1021.006: Remote Services: Windows Remote Management
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1021.006/T1021.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Enable-PSRemoting -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml)
