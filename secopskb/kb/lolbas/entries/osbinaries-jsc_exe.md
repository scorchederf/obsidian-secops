---
title: "Jsc.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Jsc.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Jsc.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Jsc.exe"
functions:
  - "Compile"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary file used by .NET to compile JavaScript code to .exe or .dll format

## Paths

- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\Jsc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Jsc.exe`
- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\Jsc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Jsc.exe`

## Commands

### 1. Compile

Use jsc.exe to compile JavaScript code stored in the provided .JS file and generate a .EXE file with the same name.

```cmd
jsc.exe {PATH:.js}
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Compile

Use jsc.exe to compile JavaScript code stored in the .JS file and generate a DLL file with the same name.

```cmd
jsc.exe /t:library {PATH:.js}
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_lolbin_jsc.yml
- IOC: Jsc.exe should normally not run a system unless it is used for development.

## Resources

- {'Link': 'https://twitter.com/DissectMalware/status/998797808907046913'}
- {'Link': 'https://www.phpied.com/make-your-javascript-a-windows-exe/'}

## Acknowledgements

- {'Person': 'Malwrologist', 'Handle': '@DissectMalware'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Jsc.yml)
