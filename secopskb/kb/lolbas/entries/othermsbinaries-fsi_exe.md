---
title: "Fsi.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Fsi.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Fsi.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Fsi.exe"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1059"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Fsi.exe

64-bit FSharp (F#) Interpreter included with Visual Studio and DotNet Core SDK.

## Metadata

- Category: OtherMSBinaries
- Created: 2021-09-26
- Author: Jimmy (@bohops)
- Source Path: yml/OtherMSBinaries/Fsi.yml

## Paths

- `C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsi.exe`

## Commands

### 1. AWL Bypass

Execute F# code via script file

```cmd
fsi.exe {PATH:.fsscript}
```

- Use Case: Execute payload with Microsoft signed binary to bypass WDAC policies
- Privileges: User
- Operating System: Windows 10 2004 (likely previous and newer versions as well)
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

### 2. AWL Bypass

Execute F# code via interactive command line

```cmd
fsi.exe
```

- Use Case: Execute payload with Microsoft signed binary to bypass WDAC policies
- Privileges: User
- Operating System: Windows 10 2004 (likely previous and newer versions as well)
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detections

- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Fsi.exe execution may be suspicious on non-developer machines
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml

## Resources

- {'Link': 'https://twitter.com/NickTyrer/status/904273264385589248'}
- {'Link': 'https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/'}

## Acknowledgements

- {'Person': 'Nick Tyrer', 'Handle': '@NickTyrer'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Fsi.yml)
