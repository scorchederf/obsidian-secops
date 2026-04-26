---
sigma_id: "b66474aa-bd92-4333-a16c-298155b120df"
title: "Potential Persistence Via Powershell Search Order Hijacking - Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_powershell_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_powershell_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b66474aa-bd92-4333-a16c-298155b120df"
  - "Potential Persistence Via Powershell Search Order Hijacking - Task"
attack_technique_ids:
  - "T1053.005"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Powershell Search Order Hijacking - Task

Detects suspicious powershell execution via a schedule task where the command ends with an suspicious flags to hide the powershell instance instead of executeing scripts or commands. This could be a sign of persistence via PowerShell "Get-Variable" technique as seen being used in Colibri Loader

## Metadata

- Rule ID: b66474aa-bd92-4333-a16c-298155b120df
- Status: test
- Level: high
- Author: pH-T (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2022-04-08
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_powershell_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ParentImage: C:\WINDOWS\System32\svchost.exe
  ParentCommandLine|contains|all:
  - -k netsvcs
  - -s Schedule
  CommandLine|endswith:
  - ' -windowstyle hidden'
  - ' -w hidden'
  - ' -ep bypass'
  - ' -noni'
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.malwarebytes.com/threat-intelligence/2022/04/colibri-loader-combines-task-scheduler-and-powershell-in-clever-persistence-technique/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_powershell_persistence.yml)
