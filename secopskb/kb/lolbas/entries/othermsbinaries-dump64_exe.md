---
title: "Dump64.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Dump64.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dump64.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Dump64.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dump64.exe

Memory dump tool that comes with Microsoft Visual Studio

## Metadata

- Category: OtherMSBinaries
- Created: 2021-11-16
- Author: mr.d0x
- Source Path: yml/OtherMSBinaries/Dump64.yml

## Paths

- `C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe`

## Commands

### 1. Dump

Creates a memory dump of the LSASS process.

```cmd
dump64.exe {PID} out.dmp
```

- Use Case: Create memory dump and parse it offline to retrieve credentials.
- Privileges: Administrator
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dump64.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious

## Resources

- {'Link': 'https://twitter.com/mrd0x/status/1460597833917251595'}

## Acknowledgements

- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dump64.yml)
