---
title: "iscsicpl.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Iscsicpl.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Iscsicpl.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "iscsicpl.exe"
functions:
  - "UAC Bypass"
attack_technique_ids:
  - "T1548.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# iscsicpl.exe

Microsoft iSCSI Initiator Control Panel tool

## Metadata

- Category: OSBinaries
- Created: 2025-08-17
- Author: Ekitji
- Source Path: yml/OSBinaries/Iscsicpl.yml

## Paths

- `c:\windows\system32\iscsicpl.exe`
- `c:\windows\syswow64\iscsicpl.exe`

## Commands

### 1. UAC Bypass

c:\windows\syswow64\iscsicpl.exe has a DLL injection through `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll`, resulting in UAC bypass.

```cmd
c:\windows\syswow64\iscsicpl.exe
```

- Use Case: Execute a custom DLL via a trusted high-integrity process without a UAC prompt.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

### 2. UAC Bypass

Both `c:\windows\system32\iscsicpl.exe` and `c:\windows\system64\iscsicpl.exe` have UAC bypass through launching iscicpl.exe, then navigating into the Configuration tab, clicking Report, then launching your custom command.

```cmd
iscsicpl.exe
```

- Use Case: Execute a binary or script as a high-integrity process without a UAC prompt.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml
- IOC: C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll
- IOC: Suspicious child process to iscsicpl.exe like cmd, powershell etc.

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/windows-server/storage/iscsi/iscsi-initiator-portal'}
- {'Link': 'https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC'}

## Acknowledgements

- {'Person': 'hacker.house'}
- {'Person': 'Ekitji', 'Handle': '@eki_erk'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Iscsicpl.yml)
