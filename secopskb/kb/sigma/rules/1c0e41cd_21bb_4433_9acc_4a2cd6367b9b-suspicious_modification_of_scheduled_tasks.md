---
sigma_id: "1c0e41cd-21bb-4433-9acc-4a2cd6367b9b"
title: "Suspicious Modification Of Scheduled Tasks"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_change.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1c0e41cd-21bb-4433-9acc-4a2cd6367b9b"
  - "Suspicious Modification Of Scheduled Tasks"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Modification Of Scheduled Tasks

Detects when an attacker tries to modify an already existing scheduled tasks to run from a suspicious location
Attackers can create a simple looking task in order to avoid detection on creation as it's often the most focused on
Instead they modify the task after creation to include their malicious payload

## Metadata

- Rule ID: 1c0e41cd-21bb-4433-9acc-4a2cd6367b9b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-28
- Modified: 2022-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_change.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_schtasks:
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - ' /Change '
  - ' /TN '
selection_susp_locations:
  CommandLine|contains:
  - \AppData\Local\Temp
  - \AppData\Roaming\
  - \Users\Public\
  - \WINDOWS\Temp\
  - \Desktop\
  - \Downloads\
  - \Temporary Internet
  - C:\ProgramData\
  - C:\Perflogs\
  - '%ProgramData%'
  - '%appdata%'
  - '%comspec%'
  - '%localappdata%'
selection_susp_images:
  CommandLine|contains:
  - regsvr32
  - rundll32
  - 'cmd /c '
  - 'cmd /k '
  - 'cmd /r '
  - 'cmd.exe /c '
  - 'cmd.exe /k '
  - 'cmd.exe /r '
  - powershell
  - mshta
  - wscript
  - cscript
  - certutil
  - bitsadmin
  - bash.exe
  - 'bash '
  - scrcons
  - 'wmic '
  - wmic.exe
  - forfiles
  - scriptrunner
  - hh.exe
  - 'hh '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_change.yml)
