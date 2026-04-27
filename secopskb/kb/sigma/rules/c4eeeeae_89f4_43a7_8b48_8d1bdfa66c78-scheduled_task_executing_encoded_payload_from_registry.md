---
sigma_id: "c4eeeeae-89f4-43a7-8b48-8d1bdfa66c78"
title: "Scheduled Task Executing Encoded Payload from Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_reg_loader_encoded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_reg_loader_encoded.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c4eeeeae-89f4-43a7-8b48-8d1bdfa66c78"
  - "Scheduled Task Executing Encoded Payload from Registry"
attack_technique_ids:
  - "T1053.005"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a schtask that potentially executes a base64 encoded payload stored in the Windows Registry using PowerShell.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli_create:
  CommandLine|contains: /Create
selection_cli_encoding:
  CommandLine|contains:
  - FromBase64String
  - encodedcommand
selection_cli_get:
  CommandLine|contains:
  - Get-ItemProperty
  - ' gp '
selection_cli_hive:
  CommandLine|contains:
  - 'HKCU:'
  - 'HKLM:'
  - 'registry::'
  - HKEY_
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2022/02/21/qbot-and-zerologon-lead-to-full-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_reg_loader_encoded.yml)
