---
atomic_guid: "6e85bdf9-7bc4-4259-ac0f-f0cb39964443"
title: "Suspicious LAPS Attributes Query with Get-ADComputer ms-Mcs-AdmPwd property"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "6e85bdf9-7bc4-4259-ac0f-f0cb39964443"
  - "Suspicious LAPS Attributes Query with Get-ADComputer ms-Mcs-AdmPwd property"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious LAPS Attributes Query with Get-ADComputer ms-Mcs-AdmPwd property

This test executes LDAP query using powershell command Get-ADComputer and lists Microsoft LAPS attributes ms-mcs-AdmPwd and ms-mcs-AdmPwdExpirationTime

## Metadata

- Atomic GUID: 6e85bdf9-7bc4-4259-ac0f-f0cb39964443
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

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
Get-ADComputer #{hostname} -Properties ms-Mcs-AdmPwd, ms-Mcs-AdmPwdExpirationTime
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
