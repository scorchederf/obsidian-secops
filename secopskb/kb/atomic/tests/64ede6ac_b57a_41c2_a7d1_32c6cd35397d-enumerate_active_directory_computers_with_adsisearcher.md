---
atomic_guid: "64ede6ac-b57a-41c2-a7d1-32c6cd35397d"
title: "Enumerate Active Directory Computers with ADSISearcher"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "64ede6ac-b57a-41c2-a7d1-32c6cd35397d"
  - "Enumerate Active Directory Computers with ADSISearcher"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The following Atomic test will utilize ADSISearcher to enumerate computers within Active Directory.
Upon successful execution a listing of computers will output with their paths in AD.
Reference: https://devblogs.microsoft.com/scripting/use-the-powershell-adsisearcher-type-accelerator-to-search-active-directory/

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
([adsisearcher]"objectcategory=computer").FindAll(); ([adsisearcher]"objectcategory=computer").FindOne()
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
