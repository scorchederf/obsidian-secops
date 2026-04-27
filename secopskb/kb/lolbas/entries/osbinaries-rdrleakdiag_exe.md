---
title: "rdrleakdiag.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Rdrleakdiag.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rdrleakdiag.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "rdrleakdiag.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# rdrleakdiag.exe

Microsoft Windows resource leak diagnostic tool

## Metadata

- Category: OSBinaries
- Created: 2022-05-18
- Author: John Dwyer
- Source Path: yml/OSBinaries/Rdrleakdiag.yml

## Paths

- `c:\windows\system32\rdrleakdiag.exe`
- `c:\Windows\SysWOW64\rdrleakdiag.exe`

## Commands

### 1. Dump

Dump process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).

```cmd
rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
```

- Use Case: Dump process by PID.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

### 2. Dump

Dump LSASS process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).

```cmd
rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
```

- Use Case: Dump LSASS process.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### 3. Dump

After dumping a process using `/wait 1`, subsequent dumps must use `/snap` (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).

```cmd
rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /snap
```

- Use Case: Dump LSASS process mutliple times.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_rdrleakdiag_process_dumping.yml
- Elastic: https://www.elastic.co/guide/en/security/current/potential-credential-access-via-windows-utilities.html
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1299071304805560321?s=21'}
- {'Link': 'https://www.pureid.io/dumping-abusing-windows-credentials-part-1/'}
- {'Link': 'https://github.com/LOLBAS-Project/LOLBAS/issues/84'}

## Acknowledgements

- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rdrleakdiag.yml)
