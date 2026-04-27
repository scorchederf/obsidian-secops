---
title: "Bitsadmin.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Bitsadmin.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Bitsadmin.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Bitsadmin.exe"
functions:
  - "ADS"
  - "Download"
  - "Copy"
  - "Execute"
attack_technique_ids:
  - "T1564.004"
  - "T1105"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bitsadmin.exe

Used for managing background intelligent transfer

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Bitsadmin.yml

## Paths

- `C:\Windows\System32\bitsadmin.exe`
- `C:\Windows\SysWOW64\bitsadmin.exe`

## Commands

### 1. ADS

Create a bitsadmin job named 1, add cmd.exe to the job, configure the job to run the target command from an Alternate data stream, then resume and complete the job.

```cmd
bitsadmin /create 1 bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\1.txt:cmd.exe NULL bitsadmin /RESUME 1 bitsadmin /complete 1
```

- Use Case: Performs execution of specified file in the alternate data stream, can be used as a defensive evasion or persistence technique.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 2. Download

Create a bitsadmin job named 1, add cmd.exe to the job, configure the job to run the target command, then resume and complete the job.

```cmd
bitsadmin /create 1 bitsadmin /addfile 1 https://live.sysinternals.com/autoruns.exe c:\data\playfolder\autoruns.exe bitsadmin /RESUME 1 bitsadmin /complete 1
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 3. Copy

Command for copying cmd.exe to another folder

```cmd
bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /RESUME 1 & bitsadmin /Complete 1 & bitsadmin /reset
```

- Use Case: Copy file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 4. Execute

One-liner that creates a bitsadmin job named 1, add cmd.exe to the job, configure the job to run the target command, then resume and complete the job.

```cmd
bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\cmd.exe NULL & bitsadmin /RESUME 1 & bitsadmin /Reset
```

- Use Case: Execute binary file specified. Can be used as a defensive evasion.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/bitsadmin_download_file.yml
- IOC: Child process from bitsadmin.exe
- IOC: bitsadmin creates new files
- IOC: bitsadmin adds data to alternate data stream

## Resources

- {'Link': 'https://www.slideshare.net/chrisgates/windows-attacks-at-is-the-new-black-26672679'}
- {'Link': 'https://www.youtube.com/watch?v=_8xJaaQlpBo'}
- {'Link': 'https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f'}
- {'Link': 'https://www.soc-labs.top/en/detections/100'}

## Acknowledgements

- {'Person': 'Rob Fuller', 'Handle': '@mubix'}
- {'Person': 'Chris Gates', 'Handle': '@carnal0wnage'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Bitsadmin.yml)
