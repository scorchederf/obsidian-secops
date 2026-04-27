---
title: "AccCheckConsole.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/AccCheckConsole.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/AccCheckConsole.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "AccCheckConsole.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AccCheckConsole.exe

Verifies UI accessibility requirements

## Metadata

- Category: OtherMSBinaries
- Created: 2022-01-02
- Author: bohops
- Source Path: yml/OtherMSBinaries/AccCheckConsole.yml

## Paths

- `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe`
- `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\AccChecker\AccCheckConsole.exe`
- `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\arm\AccChecker\AccCheckConsole.exe`
- `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\arm64\AccChecker\AccCheckConsole.exe`

## Commands

### 1. Execute

Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary active window name.

```cmd
AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
```

- Use Case: Local execution of managed code from assembly DLL.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. AWL Bypass

Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary active window name.

```cmd
AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
```

- Use Case: Local execution of managed code to bypass AppLocker.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_susp_acccheckconsole.yml
- IOC: Sysmon Event ID 1 - Process Creation
- Analysis: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340

## Resources

- {'Link': 'https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340'}
- {'Link': 'https://twitter.com/bohops/status/1477717351017680899'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/AccCheckConsole.yml)
