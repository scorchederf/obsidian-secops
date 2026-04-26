---
atomic_guid: "8b8a6449-be98-4f42-afd2-dedddc7453b2"
title: "Enumerate all accounts via PowerShell (Domain)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8b8a6449-be98-4f42-afd2-dedddc7453b2"
  - "Enumerate all accounts via PowerShell (Domain)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate all accounts via PowerShell (Domain)

Enumerate all accounts via PowerShell. Upon execution, lots of user account and group information will be displayed.

## Metadata

- Atomic GUID: 8b8a6449-be98-4f42-afd2-dedddc7453b2
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Executor

- name: powershell

### Command

```powershell
net user /domain
get-localgroupmember -group Users
get-aduser -filter *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
