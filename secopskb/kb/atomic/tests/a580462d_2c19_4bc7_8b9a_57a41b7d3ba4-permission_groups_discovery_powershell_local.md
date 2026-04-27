---
atomic_guid: "a580462d-2c19-4bc7-8b9a-57a41b7d3ba4"
title: "Permission Groups Discovery PowerShell (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a580462d-2c19-4bc7-8b9a-57a41b7d3ba4"
  - "Permission Groups Discovery PowerShell (Local)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Permission Groups Discovery PowerShell (Local)

Permission Groups Discovery utilizing PowerShell. This test will display some errors if run on a computer not connected to a domain. Upon execution, domain
information will be displayed.

## Metadata

- Atomic GUID: a580462d-2c19-4bc7-8b9a-57a41b7d3ba4
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
get-localgroup
Get-LocalGroupMember -Name "Administrators"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
