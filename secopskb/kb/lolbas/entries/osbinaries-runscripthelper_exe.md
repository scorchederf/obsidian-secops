---
title: "Runscripthelper.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Runscripthelper.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Runscripthelper.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Runscripthelper.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Runscripthelper.exe

Execute target PowerShell script

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Runscripthelper.yml

## Paths

- `C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.15_none_c2df1bba78111118\Runscripthelper.exe`
- `C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.192_none_ad4699b571e00c4a\Runscripthelper.exe`

## Commands

### 1. Execute

Execute the PowerShell script with .txt extension

```cmd
runscripthelper.exe surfacecheck \\?\{PATH_ABSOLUTE:.txt} {PATH_ABSOLUTE:folder}
```

- Use Case: Bypass constrained language mode and execute Powershell script
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Event ID 4104 - Microsoft-Windows-PowerShell/Operational
- IOC: Event ID 400 - Windows PowerShell

## Resources

- {'Link': 'https://posts.specterops.io/bypassing-application-whitelisting-with-runscripthelper-exe-1906923658fc'}

## Acknowledgements

- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Runscripthelper.yml)
