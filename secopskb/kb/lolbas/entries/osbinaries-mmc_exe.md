---
title: "Mmc.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Mmc.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Mmc.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Mmc.exe"
functions:
  - "Execute"
  - "UAC Bypass"
  - "Download"
attack_technique_ids:
  - "T1218.014"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mmc.exe

Load snap-ins to locally and remotely manage Windows systems

## Metadata

- Category: OSBinaries
- Created: 2018-12-04
- Author: @bohops
- Source Path: yml/OSBinaries/Mmc.yml

## Paths

- `C:\Windows\System32\mmc.exe`
- `C:\Windows\SysWOW64\mmc.exe`

## Commands

### 1. Execute

Launch a 'backgrounded' MMC process and invoke a COM payload

```cmd
mmc.exe -Embedding {PATH_ABSOLUTE:.msc}
```

- Use Case: Configure a snap-in to load a COM custom class (CLSID) that has been added to the registry
- Privileges: User
- Operating System: Windows 10 (and possibly earlier versions), Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.014]]

### 2. UAC Bypass

Load an arbitrary payload DLL by configuring COR Profiler registry settings and launching MMC to bypass UAC.

```cmd
mmc.exe gpedit.msc
```

- Use Case: Modify HKCU\Environment key in Registry with COR profiler values then launch MMC to load the payload DLL.
- Privileges: Administrator
- Operating System: Windows 10 (and possibly earlier versions), Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.014]]

### 3. Download

Download and save an executable to disk

```cmd
mmc.exe -Embedding {PATH_ABSOLUTE:.msc}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows 10 (and possibly earlier versions), Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.014]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mmc_susp_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_dotnet_profiler.yml

## Resources

- {'Link': 'https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/'}
- {'Link': 'https://offsec.almond.consulting/UAC-bypass-dotnet.html'}
- {'Link': 'https://www.youtube.com/watch?v=LFgZOTmhzeA'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'clem', 'Handle': '@clavoillotte'}
- {'Person': 'Fredrik H. Brathen'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Mmc.yml)
