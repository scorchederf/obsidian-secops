---
title: "Createdump.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Createdump.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Createdump.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Createdump.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft .NET Runtime Crash Dump Generator (included in .NET Core)

## Paths

- `C:\Program Files\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe`
- `C:\Program Files (x86)\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe`
- `C:\Program Files\Microsoft Visual Studio\<version>\Community\dotnet\runtime\shared\Microsoft.NETCore.App\6.0.0\createdump.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\dotnet\runtime\shared\Microsoft.NETCore.App\6.0.0\createdump.exe`

## Commands

### 1. Dump

Dump process by PID and create a minidump file. If "-f dump.dmp" is not specified, the file is created as '%TEMP%\dump.%p.dmp' where %p is the PID of the target process.

```cmd
createdump.exe -n -f {PATH:.dmp} {PID}
```

- Use Case: Dump process memory contents using PID.
- Privileges: SYSTEM
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_proc_dump_createdump.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_renamed_createdump.yml
- IOC: createdump.exe process with a command line containing the lsass.exe process id

## Resources

- {'Link': 'https://twitter.com/bopin2020/status/1366400799199272960'}
- {'Link': 'https://docs.microsoft.com/en-us/troubleshoot/developer/webapps/aspnetcore/practice-troubleshoot-linux/lab-1-3-capture-core-crash-dumps'}

## Acknowledgements

- {'Person': 'bopin', 'Handle': '@bopin2020'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Createdump.yml)
