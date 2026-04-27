---
atomic_guid: "69119e58-96db-4110-ad27-954e48f3bb13"
title: "WMIObject Group Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilizing PowerShell cmdlet - get-wmiobject, to enumerate local groups on the endpoint. Upon execution, Upon execution, information will be displayed of local groups on system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]

## Executor

- name: powershell

### Command

```powershell
Get-WMIObject Win32_Group
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
