---
atomic_guid: "ffbcfd62-15d6-4989-a21a-80bfc8e58bb5"
title: "Suspicious LAPS Attributes Query with Get-ADComputer all properties and SearchScope"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "ffbcfd62-15d6-4989-a21a-80bfc8e58bb5"
  - "Suspicious LAPS Attributes Query with Get-ADComputer all properties and SearchScope"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious LAPS Attributes Query with Get-ADComputer all properties and SearchScope

This test executes LDAP query using powershell command Get-ADComputer with SearchScope as subtree and lists all the properties including Microsoft LAPS attributes ms-mcs-AdmPwd and ms-mcs-AdmPwdExpirationTime

## Metadata

- Atomic GUID: ffbcfd62-15d6-4989-a21a-80bfc8e58bb5
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
Get-adcomputer -SearchScope subtree -filter "name -like '*'" -Properties *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
