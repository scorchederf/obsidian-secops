---
atomic_guid: "9f4e344b-8434-41b3-85b1-d38f29d148d0"
title: "Enumerate Active Directory Groups with ADSISearcher"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "9f4e344b-8434-41b3-85b1-d38f29d148d0"
  - "Enumerate Active Directory Groups with ADSISearcher"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Active Directory Groups with ADSISearcher

The following Atomic test will utilize ADSISearcher to enumerate groups within Active Directory.
Upon successful execution a listing of groups will output with their paths in AD.
Reference: https://devblogs.microsoft.com/scripting/use-the-powershell-adsisearcher-type-accelerator-to-search-active-directory/

## Metadata

- Atomic GUID: 9f4e344b-8434-41b3-85b1-d38f29d148d0
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
([adsisearcher]"objectcategory=group").FindAll(); ([adsisearcher]"objectcategory=group").FindOne()
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
