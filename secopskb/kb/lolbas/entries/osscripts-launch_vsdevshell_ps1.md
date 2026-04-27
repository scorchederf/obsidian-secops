---
title: "Launch-VsDevShell.ps1"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/Launch-VsDevShell.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Launch-VsDevShell.yml"
build_date: "2026-04-27 18:39:01"
category: "OSScripts"
aliases:
  - "Launch-VsDevShell.ps1"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Launch-VsDevShell.ps1

Locates and imports a Developer PowerShell module and calls the Enter-VsDevShell cmdlet

## Metadata

- Category: OSScripts
- Created: 2022-06-13
- Author: Nasreddine Bencherchali
- Source Path: yml/OSScripts/Launch-VsDevShell.yml

## Paths

- `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1`
- `C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1`

## Commands

### 1. Execute

Execute binaries from the context of the signed script using the "VsWherePath" flag.

```cmd
powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsWherePath {PATH_ABSOLUTE:.exe}
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

### 2. Execute

Execute binaries and commands from the context of the signed script using the "VsInstallationPath" flag.

```cmd
powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;"
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml

## Resources

- {'Link': 'https://twitter.com/nas_bench/status/1535981653239255040'}

## Acknowledgements

- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Launch-VsDevShell.yml)
