---
atomic_guid: "36753ded-e5c4-4eb5-bc3c-e8fba236878d"
title: "Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Windows Credentials]"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555"
attack_technique_name: "Credentials from Password Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "36753ded-e5c4-4eb5-bc3c-e8fba236878d"
  - "Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Windows Credentials]"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Windows Credentials]

This module will enumerate credentials stored in Windows Credentials vault of Windows Credential Manager using builtin utility vaultcmd.exe

## Metadata

- Atomic GUID: 36753ded-e5c4-4eb5-bc3c-e8fba236878d
- Technique: T1555: Credentials from Password Stores
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1555/T1555.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
vaultcmd /listcreds:"Windows Credentials" /all
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml)
