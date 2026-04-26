---
atomic_guid: "02e8be5a-3065-4e54-8cc8-a14d138834d3"
title: "Enumerate Active Directory Users with ADSISearcher"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "02e8be5a-3065-4e54-8cc8-a14d138834d3"
  - "Enumerate Active Directory Users with ADSISearcher"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Active Directory Users with ADSISearcher

The following Atomic test will utilize ADSISearcher to enumerate users within Active Directory.
Upon successful execution a listing of users will output with their paths in AD.
Reference: https://devblogs.microsoft.com/scripting/use-the-powershell-adsisearcher-type-accelerator-to-search-active-directory/

## Metadata

- Atomic GUID: 02e8be5a-3065-4e54-8cc8-a14d138834d3
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
([adsisearcher]"objectcategory=user").FindAll(); ([adsisearcher]"objectcategory=user").FindOne()
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
