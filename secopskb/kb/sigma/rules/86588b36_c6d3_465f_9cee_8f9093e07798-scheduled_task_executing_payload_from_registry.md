---
sigma_id: "86588b36-c6d3-465f-9cee-8f9093e07798"
title: "Scheduled Task Executing Payload from Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_reg_loader.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_reg_loader.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "86588b36-c6d3-465f-9cee-8f9093e07798"
  - "Scheduled Task Executing Payload from Registry"
attack_technique_ids:
  - "T1053.005"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task Executing Payload from Registry

Detects the creation of a schtasks that potentially executes a payload stored in the Windows Registry using PowerShell.

## Metadata

- Rule ID: 86588b36-c6d3-465f-9cee-8f9093e07798
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_reg_loader.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli_create:
  CommandLine|contains: /Create
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
filter_main_encoding:
  CommandLine|contains:
  - FromBase64String
  - encodedcommand
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/02/21/qbot-and-zerologon-lead-to-full-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_reg_loader.yml)
