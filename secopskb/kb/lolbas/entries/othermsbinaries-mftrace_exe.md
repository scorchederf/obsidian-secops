---
title: "Mftrace.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Mftrace.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Mftrace.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Mftrace.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Trace log generation tool for Media Foundation Tools.

## Paths

- `C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe`
- `C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x64\mftrace.exe`
- `C:\Program Files (x86)\Windows Kits\10\bin\x86\mftrace.exe`
- `C:\Program Files (x86)\Windows Kits\10\bin\x64\mftrace.exe`

## Commands

### 1. Execute

Launch specified executable as a subprocess of Mftrace.exe.

```cmd
Mftrace.exe {PATH:.exe}
```

- Use Case: Local execution of cmd.exe as a subprocess of Mftrace.exe.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_mftrace.yml

## Resources

- {'Link': 'https://twitter.com/0rbz_/status/988911181422186496'}

## Acknowledgements

- {'Person': 'fabrizio', 'Handle': '@0rbz_'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Mftrace.yml)
