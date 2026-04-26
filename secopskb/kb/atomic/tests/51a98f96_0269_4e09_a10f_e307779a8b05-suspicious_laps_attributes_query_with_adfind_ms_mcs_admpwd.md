---
atomic_guid: "51a98f96-0269-4e09-a10f-e307779a8b05"
title: "Suspicious LAPS Attributes Query with adfind ms-Mcs-AdmPwd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "51a98f96-0269-4e09-a10f-e307779a8b05"
  - "Suspicious LAPS Attributes Query with adfind ms-Mcs-AdmPwd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious LAPS Attributes Query with adfind ms-Mcs-AdmPwd

This test executes LDAP query using adfind command and lists Microsoft LAPS attributes ms-mcs-AdmPwd and ms-mcs-AdmPwdExpirationTime

## Metadata

- Atomic GUID: 51a98f96-0269-4e09-a10f-e307779a8b05
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Input Arguments

### domain

- description: Domain of the host
- type: string
- default: $env:USERDOMAIN

### optional_args

- description: Allows defining arguments to add to the adfind command to tailor it to the specific needs of the environment. Use "-arg" notation to add arguments separated by spaces.
- type: string

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
& "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe" #{optional_args} -h #{domain} -s subtree -f "objectclass=computer" ms-Mcs-AdmPwd, ms-Mcs-AdmPwdExpirationTime
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
