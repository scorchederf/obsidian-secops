---
atomic_guid: "394012d9-2164-4d4f-b9e5-acf30ba933fe"
title: "Suspicious LAPS Attributes Query with Get-ADComputer all properties"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "394012d9-2164-4d4f-b9e5-acf30ba933fe"
  - "Suspicious LAPS Attributes Query with Get-ADComputer all properties"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test executes LDAP query using powershell command Get-ADComputer and lists all the properties including Microsoft LAPS attributes ms-mcs-AdmPwd and ms-mcs-AdmPwdExpirationTime

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]

## Input Arguments

### hostname

- description: Name of the host
- type: string
- default: $env:computername

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Get-ADComputer #{hostname} -Properties *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
