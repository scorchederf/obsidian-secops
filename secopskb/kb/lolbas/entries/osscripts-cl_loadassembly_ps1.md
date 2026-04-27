---
title: "CL_LoadAssembly.ps1"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/CL_LoadAssembly.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/CL_LoadAssembly.yml"
build_date: "2026-04-27 18:39:01"
category: "OSScripts"
aliases:
  - "CL_LoadAssembly.ps1"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CL_LoadAssembly.ps1

PowerShell Diagnostic Script

## Metadata

- Category: OSScripts
- Created: 2021-09-26
- Author: Jimmy (@bohops)
- Source Path: yml/OSScripts/CL_LoadAssembly.yml

## Paths

- `C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1`

## Commands

### 1. Execute

Proxy execute Managed DLL with PowerShell

```cmd
powershell.exe -ep bypass -command "set-location -path C:\Windows\diagnostics\system\Audio; import-module .\CL_LoadAssembly.ps1; LoadAssemblyFromPath ..\..\..\..\testing\fun.dll;[Program]::Fun()"
```

- Use Case: Execute proxied payload with Microsoft signed binary
- Privileges: User
- Operating System: Windows 10 21H1 (likely other versions as well), Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/ff6c54ded6b52f379cec11fe17c1ccb956faa660/rules/windows/process_creation/proc_creation_win_lolbas_cl_loadassembly.yml

## Resources

- {'Link': 'https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-powershell-diagnostic-scripts/'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/CL_LoadAssembly.yml)
