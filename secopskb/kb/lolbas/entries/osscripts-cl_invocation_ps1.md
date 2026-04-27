---
title: "CL_Invocation.ps1"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/Cl_invocation.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Cl_invocation.yml"
build_date: "2026-04-27 19:14:21"
category: "OSScripts"
aliases:
  - "CL_Invocation.ps1"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Aero diagnostics script

## Paths

- `C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1`
- `C:\Windows\diagnostics\system\Audio\CL_Invocation.ps1`
- `C:\Windows\diagnostics\system\WindowsUpdate\CL_Invocation.ps1`

## Commands

### 1. Execute

Import the PowerShell Diagnostic CL_Invocation script and call SyncInvoke to launch an executable.

```cmd
. C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1   \nSyncInvoke {CMD}
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_cl_invocation.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_cl_invocation_lolscript.yml

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Cl_invocation.yml)
