---
atomic_guid: "dda6fc7b-c9a6-4c18-b98d-95ec6542af6d"
title: "PowerShell Modify A Scheduled Task"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "dda6fc7b-c9a6-4c18-b98d-95ec6542af6d"
  - "PowerShell Modify A Scheduled Task"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create a scheduled task with an action and modify the action to do something else. The initial idea is to showcase Microsoft Windows TaskScheduler Operational log modification of an action on a Task already registered. 
It will first be created to spawn cmd.exe, but modified to run notepad.exe.

Upon successful execution, powershell.exe will create a scheduled task and modify the action.

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$Action = New-ScheduledTaskAction -Execute "cmd.exe"
$Trigger = New-ScheduledTaskTrigger -AtLogon
$User = New-ScheduledTaskPrincipal -GroupId "BUILTIN\Administrators" -RunLevel Highest
$Set = New-ScheduledTaskSettingsSet
$object = New-ScheduledTask -Action $Action -Principal $User -Trigger $Trigger -Settings $Set
Register-ScheduledTask AtomicTaskModifed -InputObject $object
$NewAction = New-ScheduledTaskAction -Execute "Notepad.exe"
Set-ScheduledTask "AtomicTaskModifed" -Action $NewAction
```

### Cleanup

```powershell
Unregister-ScheduledTask -TaskName "AtomicTaskModifed" -confirm:$false >$null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
