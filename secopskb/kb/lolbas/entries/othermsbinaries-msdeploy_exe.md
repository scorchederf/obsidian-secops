---
title: "Msdeploy.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Msdeploy.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Msdeploy.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Msdeploy.exe"
functions:
  - "Execute"
  - "AWL Bypass"
  - "Copy"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft tool used to deploy Web Applications.

## Paths

- `C:\Program Files\IIS\Microsoft Web Deploy V2\msdeploy.exe`
- `C:\Program Files (x86)\IIS\Microsoft Web Deploy V2\msdeploy.exe`
- `C:\Program Files\IIS\Microsoft Web Deploy V3\msdeploy.exe`
- `C:\Program Files (x86)\IIS\Microsoft Web Deploy V3\msdeploy.exe`
- `C:\Program Files\IIS\Microsoft Web Deploy V4\msdeploy.exe`
- `C:\Program Files (x86)\IIS\Microsoft Web Deploy V4\msdeploy.exe`
- `C:\Program Files\IIS\Microsoft Web Deploy V5\msdeploy.exe`
- `C:\Program Files (x86)\IIS\Microsoft Web Deploy V5\msdeploy.exe`

## Commands

### 1. Execute

Launch .bat file via msdeploy.exe.

```cmd
msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
```

- Use Case: Local execution of batch file using msdeploy.exe.
- Privileges: User
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11, Windows Server
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. AWL Bypass

Launch .bat file via msdeploy.exe.

```cmd
msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
```

- Use Case: Local execution of batch file using msdeploy.exe.
- Privileges: User
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11, Windows Server
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 3. Copy

Copy file from source to destination.

```cmd
msdeploy.exe -verb:sync -source:filePath={PATH_ABSOLUTE:.source.ext} -dest:filePath={PATH_ABSOLUTE:.dest.ext}
```

- Use Case: Copy file.
- Privileges: User
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11, Windows Server
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/995837734379032576'}
- {'Link': 'https://twitter.com/pabraeken/status/999090532839313408'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}
- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Msdeploy.yml)
