---
title: "Ilasm.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ilasm.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ilasm.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Ilasm.exe"
functions:
  - "Compile"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

used for compile c# code into dll or exe.

## Paths

- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ilasm.exe`

## Commands

### 1. Compile

Binary file used by .NET to compile C#/intermediate (IL) code to .exe

```cmd
ilasm.exe {PATH_ABSOLUTE:.txt} /exe
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows 7, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Compile

Binary file used by .NET to compile C#/intermediate (IL) code to dll

```cmd
ilasm.exe {PATH_ABSOLUTE:.txt} /dll
```

- Use Case: A description of the usecase
- Privileges: User
- Operating System: Windows 7, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- IOC: Ilasm may not be used often in production environments (such as on endpoints)
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ilasm.yml

## Resources

- {'Link': 'https://github.com/LuxNoBulIshit/BeforeCompileBy-ilasm/blob/master/hello_world.txt'}

## Acknowledgements

- {'Person': 'Hai Vaknin(Lux)', 'Handle': '@VakninHai'}
- {'Person': 'Lior Adar'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ilasm.yml)
