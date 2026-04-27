---
title: "UtilityFunctions.ps1"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/UtilityFunctions.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/UtilityFunctions.yml"
build_date: "2026-04-27 19:14:21"
category: "OSScripts"
aliases:
  - "UtilityFunctions.ps1"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

PowerShell Diagnostic Script

## Paths

- `C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1`

## Commands

### 1. Execute

Proxy execute Managed DLL with PowerShell

```cmd
powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[Program.Class]::Main()"
```

- Use Case: Execute proxied payload with Microsoft signed binary
- Privileges: User
- Operating System: Windows 10 21H1 (likely other versions as well), Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/0.21-688-gd172b136b/rules/windows/process_creation/proc_creation_win_lolbas_utilityfunctions.yml

## Resources

- {'Link': 'https://twitter.com/nickvangilder/status/1441003666274668546'}

## Acknowledgements

- {'Person': 'Nick VanGilder', 'Handle': '@nickvangilder'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/UtilityFunctions.yml)
