---
atomic_guid: "af9fd58f-c4ac-4bf2-a9ba-224b71ff25fd"
title: "Powershell Cmdlet Scheduled Task"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "af9fd58f-c4ac-4bf2-a9ba-224b71ff25fd"
  - "Powershell Cmdlet Scheduled Task"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powershell Cmdlet Scheduled Task

Create an atomic scheduled task that leverages native powershell cmdlets.

Upon successful execution, powershell.exe will create a scheduled task to spawn cmd.exe at 20:10.

## Metadata

- Atomic GUID: af9fd58f-c4ac-4bf2-a9ba-224b71ff25fd
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$Action = New-ScheduledTaskAction -Execute "calc.exe"
$Trigger = New-ScheduledTaskTrigger -AtLogon
$User = New-ScheduledTaskPrincipal -GroupId "BUILTIN\Administrators" -RunLevel Highest
$Set = New-ScheduledTaskSettingsSet
$object = New-ScheduledTask -Action $Action -Principal $User -Trigger $Trigger -Settings $Set
Register-ScheduledTask AtomicTask -InputObject $object
```

### Cleanup

```powershell
Unregister-ScheduledTask -TaskName "AtomicTask" -confirm:$false >$null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
