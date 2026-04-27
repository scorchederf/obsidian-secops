---
sigma_id: "c5c00f49-b3f9-45a6-997e-cfdecc6e1967"
title: "Suspicious Schtasks Execution AppData Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_appdata_local_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_appdata_local_system.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c5c00f49-b3f9-45a6-997e-cfdecc6e1967"
  - "Suspicious Schtasks Execution AppData Folder"
attack_technique_ids:
  - "T1053.005"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a schtask that executes a file from C:\Users\<USER>\AppData\Local

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - /Create
  - /RU
  - /TR
  - C:\Users\
  - \AppData\Local\
  CommandLine|contains:
  - NT AUT
  - ' SYSTEM '
filter:
  ParentImage|contains|all:
  - \AppData\Local\Temp\
  - TeamViewer_.exe
  Image|endswith: \schtasks.exe
  CommandLine|contains: /TN TVInstallRestore
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/02/21/qbot-and-zerologon-lead-to-full-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_appdata_local_system.yml)
