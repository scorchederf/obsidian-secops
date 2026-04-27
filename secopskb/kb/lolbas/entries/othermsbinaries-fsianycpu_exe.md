---
title: "FsiAnyCpu.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/FsiAnyCpu.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/FsiAnyCpu.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "FsiAnyCpu.exe"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1059"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

32/64-bit FSharp (F#) Interpreter included with Visual Studio.

## Paths

- `c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe`

## Commands

### 1. AWL Bypass

Execute F# code via script file

```cmd
fsianycpu.exe {PATH:.fsscript}
```

- Use Case: Execute payload with Microsoft signed binary to bypass WDAC policies
- Privileges: User
- Operating System: Windows 10 2004 (likely previous and newer versions as well)
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

### 2. AWL Bypass

Execute F# code via interactive command line

```cmd
fsianycpu.exe
```

- Use Case: Execute payload with Microsoft signed binary to bypass WDAC policies
- Privileges: User
- Operating System: Windows 10 2004 (likely previous and newer versions as well)
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detections

- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: FsiAnyCpu.exe execution may be suspicious on non-developer machines
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml

## Resources

- {'Link': 'https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/'}

## Acknowledgements

- {'Person': 'Nick Tyrer', 'Handle': '@NickTyrer'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/FsiAnyCpu.yml)
