---
title: "CustomShellHost.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/CustomShellHost.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/CustomShellHost.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "CustomShellHost.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

A host process that is used by custom shells when using Windows in Kiosk mode.

## Paths

- `C:\Windows\System32\CustomShellHost.exe`

## Commands

### 1. Execute

Executes explorer.exe (with command-line argument /NoShellRegistrationCheck) if present in the current working folder.

```cmd
CustomShellHost.exe
```

- Use Case: Can be used to evade defensive counter-measures
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- IOC: CustomShellHost.exe is unlikely to run on normal workstations
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_customshellhost.yml

## Resources

- {'Link': 'https://twitter.com/YoSignals/status/1381353520088113154'}
- {'Link': 'https://docs.microsoft.com/en-us/windows/configuration/kiosk-shelllauncher'}

## Acknowledgements

- {'Person': 'John Carroll', 'Handle': '@YoSignals'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/CustomShellHost.yml)
