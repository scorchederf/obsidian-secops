---
title: "Dotnet.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Dotnet.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dotnet.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Dotnet.exe"
functions:
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1218"
  - "T1059"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dotnet.exe

dotnet.exe comes with .NET Framework

## Metadata

- Category: OtherMSBinaries
- Created: 2019-11-12
- Author: felamos
- Source Path: yml/OtherMSBinaries/Dotnet.yml

## Paths

- `C:\Program Files\dotnet\dotnet.exe`

## Commands

### 1. AWL Bypass

dotnet.exe will execute any DLL even if applocker is enabled.

```cmd
dotnet.exe {PATH:.dll}
```

- Use Case: Execute code bypassing AWL
- Privileges: User
- Operating System: Windows 7 and up with .NET installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

dotnet.exe will execute any DLL.

```cmd
dotnet.exe {PATH:.dll}
```

- Use Case: Execute DLL
- Privileges: User
- Operating System: Windows 7 and up with .NET installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 3. Execute

dotnet.exe will open a console which allows for the execution of arbitrary F# commands

```cmd
dotnet.exe fsi
```

- Use Case: Execute arbitrary F# code
- Privileges: User
- Operating System: Windows 10 and up with .NET SDK installed
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

### 4. AWL Bypass

dotnet.exe with msbuild (SDK Version) will execute unsigned code

```cmd
dotnet.exe msbuild {PATH:.csproj}
```

- Use Case: Execute code bypassing AWL
- Privileges: User
- Operating System: Windows 10 and up with .NET Core installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dotnet.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: dotnet.exe spawned an unknown process

## Resources

- {'Link': 'https://twitter.com/_felamos/status/1204705548668555264'}
- {'Link': 'https://gist.github.com/bohops/3f645a7238d8022830ecf5511b3ecfbc'}
- {'Link': 'https://bohops.com/2019/08/19/dotnet-core-a-vector-for-awl-bypass-defense-evasion/'}
- {'Link': 'https://learn.microsoft.com/en-us/dotnet/fsharp/tools/fsharp-interactive/'}

## Acknowledgements

- {'Person': 'felamos', 'Handle': '@_felamos'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'yamalon', 'Handle': '@mavinject'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dotnet.yml)
