---
title: "Infdefaultinstall.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Infdefaultinstall.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Infdefaultinstall.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Infdefaultinstall.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary used to perform installation based on content inside inf files

## Paths

- `C:\Windows\System32\Infdefaultinstall.exe`
- `C:\Windows\SysWOW64\Infdefaultinstall.exe`

## Commands

### 1. Execute

Executes SCT script using scrobj.dll from a command in entered into a specially prepared INF file.

```cmd
InfDefaultInstall.exe {PATH:.inf}
```

- Use Case: Code execution
- Privileges: Admin
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_infdefaultinstall_execute_sct_scripts.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules

## Resources

- {'Link': 'https://twitter.com/KyleHanslovan/status/911997635455852544'}
- {'Link': 'https://blog.conscioushacker.io/index.php/2017/10/25/evading-microsofts-autoruns/'}
- {'Link': 'https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/'}

## Acknowledgements

- {'Person': 'Kyle Hanslovan', 'Handle': '@kylehanslovan'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Infdefaultinstall.yml)
