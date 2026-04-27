---
title: "At.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/At.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/At.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "At.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1053.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# At.exe

Schedule periodic tasks

## Metadata

- Category: OSBinaries
- Created: 2019-09-20
- Author: Freddie Barr-Smith
- Source Path: yml/OSBinaries/At.yml

## Paths

- `C:\WINDOWS\System32\At.exe`
- `C:\WINDOWS\SysWOW64\At.exe`

## Commands

### 1. Execute

Create a recurring task to execute every day at a specific time.

```cmd
C:\Windows\System32\at.exe 09:00 /interactive /every:m,t,w,th,f,s,su {CMD}
```

- Use Case: Create a recurring task, to eg. to keep reverse shell session(s) alive
- Privileges: Local Admin
- Operating System: Windows 7 or older
- ATT&CK: [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/builtin/security/win_security_atsvc_task.yml
- IOC: C:\Windows\System32\Tasks\At1 (substitute 1 with subsequent number of at job)
- IOC: C:\Windows\Tasks\At1.job
- IOC: Registry Key - Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\At1.

## Resources

- {'Link': 'https://freddiebarrsmith.com/at.txt'}
- {'Link': 'https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_windows.html'}
- {'Link': 'https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems'}

## Acknowledgements

- {'Person': 'Freddie Barr-Smith', 'Handle': None}
- {'Person': 'Riccardo Spolaor', 'Handle': None}
- {'Person': 'Mariano Graziano', 'Handle': None}
- {'Person': 'Xabier Ugarte-Pedrero', 'Handle': None}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/At.yml)
