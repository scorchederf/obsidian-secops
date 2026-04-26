---
sigma_id: "56c217c3-2de2-479b-990f-5c109ba8458f"
title: "HackTool - Default PowerSploit/Empire Scheduled Task Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_powersploit_empire_default_schtasks.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_powersploit_empire_default_schtasks.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "56c217c3-2de2-479b-990f-5c109ba8458f"
  - "HackTool - Default PowerSploit/Empire Scheduled Task Creation"
attack_technique_ids:
  - "T1053.005"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Default PowerSploit/Empire Scheduled Task Creation

Detects the creation of a schtask via PowerSploit or Empire Default Configuration.

## Metadata

- Rule ID: 56c217c3-2de2-479b-990f-5c109ba8458f
- Status: test
- Level: high
- Author: Markus Neis, @Karneades
- Date: 2018-03-06
- Modified: 2023-03-03
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_powersploit_empire_default_schtasks.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

### Software Tags

- S0111

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - /Create
  - powershell.exe -NonI
  - /TN Updater /TR
  CommandLine|contains:
  - /SC ONLOGON
  - /SC DAILY /ST
  - /SC ONIDLE
  - /SC HOURLY
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/0xdeadbeefJERKY/PowerSploit/blob/8690399ef70d2cad10213575ac67e8fa90ddf7c3/Persistence/Persistence.psm1
- https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/powershell/persistence/userland/schtasks.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_powersploit_empire_default_schtasks.yml)
