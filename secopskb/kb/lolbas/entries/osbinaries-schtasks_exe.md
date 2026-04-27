---
title: "Schtasks.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Schtasks.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Schtasks.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Schtasks.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1053.005"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Schedule periodic tasks

## Paths

- `c:\windows\system32\schtasks.exe`
- `c:\windows\syswow64\schtasks.exe`

## Commands

### 1. Execute

Create a recurring task to execute every minute.

```cmd
schtasks /create /sc minute /mo 1 /tn "Reverse shell" /tr "{CMD}"
```

- Use Case: Create a recurring task to keep reverse shell session(s) alive
- Privileges: User
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

### 2. Execute

Create a scheduled task on a remote computer for persistence/lateral movement

```cmd
schtasks /create /s targetmachine /tn "MyTask" /tr "{CMD}" /sc daily
```

- Use Case: Create a remote task to run daily relative to the the time of creation
- Privileges: Administrator
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/persistence_local_scheduled_task_creation.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/schtasks_scheduling_job_on_remote_system.yml
- IOC: Suspicious task creation events

## Resources

- {'Link': 'https://isc.sans.edu/forums/diary/Adding+Persistence+Via+Scheduled+Tasks/23633/'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Schtasks.yml)
