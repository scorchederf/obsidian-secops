---
sigma_id: "c4eeeeae-89f4-43a7-8b48-8d1bdfa66c78"
title: "Scheduled Task Executing Encoded Payload from Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_reg_loader_encoded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_reg_loader_encoded.yml"
build_date: "2026-04-26 15:01:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Scheduled Task Executing Encoded Payload from Registry

Detects the creation of a schtask that potentially executes a base64 encoded payload stored in the Windows Registry using PowerShell.

## Metadata

- Rule ID: c4eeeeae-89f4-43a7-8b48-8d1bdfa66c78
- Status: test
- Level: high
- Author: pH-T (Nextron Systems), @Kostastsale, TheDFIRReport, X__Junior (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-02-12
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_reg_loader_encoded.yml

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
