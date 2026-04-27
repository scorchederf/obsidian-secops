---
title: "Pester.bat"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/pester.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/pester.yml"
build_date: "2026-04-27 18:39:01"
category: "OSScripts"
aliases:
  - "Pester.bat"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Pester.bat

Used as part of the Powershell pester

## Metadata

- Category: OSScripts
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSScripts/pester.yml

## Paths

- `c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat`

## Commands

### 1. Execute

Execute code using Pester. The third parameter can be anything. The fourth is the payload.

```cmd
Pester.bat [/help|?|-?|/?] "$null; {CMD}"
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

### 2. Execute

Execute code using Pester. Example here executes specified executable.

```cmd
Pester.bat ;{PATH:.exe}
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml

## Resources

- {'Link': 'https://twitter.com/Oddvarmoe/status/993383596244258816'}
- {'Link': 'https://twitter.com/_st0pp3r_/status/1560072680887525378'}
- {'Link': 'https://twitter.com/_st0pp3r_/status/1560072680887525378'}

## Acknowledgements

- {'Person': 'Emin Atac', 'Handle': '@p0w3rsh3ll'}
- {'Person': 'Stamatis Chatzimangou', 'Handle': '@_st0pp3r_'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/pester.yml)
