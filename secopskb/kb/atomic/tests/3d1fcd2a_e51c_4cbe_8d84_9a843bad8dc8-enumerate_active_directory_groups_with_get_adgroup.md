---
atomic_guid: "3d1fcd2a-e51c-4cbe-8d84-9a843bad8dc8"
title: "Enumerate Active Directory Groups with Get-AdGroup"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3d1fcd2a-e51c-4cbe-8d84-9a843bad8dc8"
  - "Enumerate Active Directory Groups with Get-AdGroup"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enumerate Active Directory Groups with Get-AdGroup

The following Atomic test will utilize Get-AdGroup to enumerate groups within Active Directory.
Upon successful execution a listing of groups will output with their paths in AD.
Reference: https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps

## Metadata

- Atomic GUID: 3d1fcd2a-e51c-4cbe-8d84-9a843bad8dc8
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Executor

- name: powershell

### Command

```powershell
Get-AdGroup -Filter *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
