---
atomic_guid: "69119e58-96db-4110-ad27-954e48f3bb13"
title: "WMIObject Group Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "69119e58-96db-4110-ad27-954e48f3bb13"
  - "WMIObject Group Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WMIObject Group Discovery

Utilizing PowerShell cmdlet - get-wmiobject, to enumerate local groups on the endpoint. Upon execution, Upon execution, information will be displayed of local groups on system.

## Metadata

- Atomic GUID: 69119e58-96db-4110-ad27-954e48f3bb13
- Technique: T1069.001: Permission Groups Discovery: Local Groups
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1069.001/T1069.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Executor

- name: powershell

### Command

```powershell
Get-WMIObject Win32_Group
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
