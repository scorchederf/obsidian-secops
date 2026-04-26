---
atomic_guid: "6d5d8c96-3d2a-4da9-9d6d-9a9d341899a7"
title: "Permission Groups Discovery PowerShell (Domain)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "6d5d8c96-3d2a-4da9-9d6d-9a9d341899a7"
  - "Permission Groups Discovery PowerShell (Domain)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Permission Groups Discovery PowerShell (Domain)

Permission Groups Discovery utilizing PowerShell. This test will display some errors if run on a computer not connected to a domain. Upon execution, domain
information will be displayed.

## Metadata

- Atomic GUID: 6d5d8c96-3d2a-4da9-9d6d-9a9d341899a7
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Input Arguments

### user

- description: User to identify what groups a user is a member of
- type: string
- default: $env:USERNAME

## Executor

- name: powershell

### Command

```powershell
get-ADPrincipalGroupMembership #{user} | select name
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
