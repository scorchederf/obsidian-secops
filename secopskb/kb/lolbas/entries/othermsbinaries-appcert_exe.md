---
title: "AppCert.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Appcert.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Appcert.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "AppCert.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
  - "T1218.007"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AppCert.exe

Windows App Certification Kit command-line tool.

## Metadata

- Category: OtherMSBinaries
- Created: 2024-03-06
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/Appcert.yml

## Paths

- `C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe`
- `C:\Program Files\Windows Kits\10\App Certification Kit\appcert.exe`

## Commands

### 1. Execute

Execute an executable file via the Windows App Certification Kit command-line tool.

```cmd
appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml}
```

- Use Case: Performs execution of specified file, can be used as a defense evasion
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. Execute

Install an MSI file via an msiexec instance spawned via appcert.exe as parent process.

```cmd
appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.msi} -setupcommandline /q -reportoutputpath {PATH_ABSOLUTE:.xml}
```

- Use Case: Execute custom made MSI file with malicious code
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Resources

- {'Link': 'https://learn.microsoft.com/windows/win32/win_cert/using-the-windows-app-certification-kit'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Appcert.yml)
