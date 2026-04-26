---
sigma_id: "363eccc0-279a-4ccf-a3ab-24c2e63b11fb"
title: "Powershell Create Scheduled Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_cmdlet_scheduled_task.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_cmdlet_scheduled_task.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "363eccc0-279a-4ccf-a3ab-24c2e63b11fb"
  - "Powershell Create Scheduled Task"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Create Scheduled Task

Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code

## Metadata

- Rule ID: 363eccc0-279a-4ccf-a3ab-24c2e63b11fb
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-28
- Modified: 2025-10-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_cmdlet_scheduled_task.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains:
  - New-ScheduledTaskAction
  - New-ScheduledTaskTrigger
  - New-ScheduledTaskPrincipal
  - New-ScheduledTaskSettingsSet
  - New-ScheduledTask
  - Register-ScheduledTask
selection_cimmethod:
  ScriptBlockText|contains|all:
  - Invoke-CimMethod
  - -ClassName
  - PS_ScheduledTask
  - -NameSpace
  - Root\Microsoft\Windows\TaskScheduler
filter_main_legitimate_scripts:
  ScriptBlockText|contains|all:
  - Microsoft.PowerShell.Core\Export-ModuleMember
  - Microsoft.Management.Infrastructure.CimInstance
  - __cmdletization_methodParameter
condition: 1 of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1053.005/T1053.005.md#atomic-test-4---powershell-cmdlet-scheduled-task
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1053.005/T1053.005.md#atomic-test-6---wmi-invoke-cimmethod-scheduled-task

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_cmdlet_scheduled_task.yml)
