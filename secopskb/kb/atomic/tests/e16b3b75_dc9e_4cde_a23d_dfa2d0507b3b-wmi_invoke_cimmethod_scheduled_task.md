---
atomic_guid: "e16b3b75-dc9e-4cde-a23d-dfa2d0507b3b"
title: "WMI Invoke-CimMethod Scheduled Task"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "e16b3b75-dc9e-4cde-a23d-dfa2d0507b3b"
  - "WMI Invoke-CimMethod Scheduled Task"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# WMI Invoke-CimMethod Scheduled Task

Create an scheduled task that executes notepad.exe after user login from XML by leveraging WMI class PS_ScheduledTask. Does the same thing as Register-ScheduledTask cmdlet behind the scenes.

## Metadata

- Atomic GUID: e16b3b75-dc9e-4cde-a23d-dfa2d0507b3b
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Input Arguments

### xml_path

- description: path of vbs to use when creating masquerading files
- type: path
- default: PathToAtomicsFolder\T1053.005\src\T1053_005_WMI.xml

## Dependencies

File to copy must exist on disk at specified location (#{xml_path})

### Prerequisite Check

```powershell
if (Test-Path "#{xml_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{xml_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1053.005/src/T1053_005_WMI.xml" -OutFile "#{xml_path}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$xml = [System.IO.File]::ReadAllText("#{xml_path}")
Invoke-CimMethod -ClassName PS_ScheduledTask -NameSpace "Root\Microsoft\Windows\TaskScheduler" -MethodName "RegisterByXml" -Arguments @{ Force = $true; Xml =$xml; }
```

### Cleanup

```powershell
Unregister-ScheduledTask -TaskName "T1053_005_WMI" -confirm:$false >$null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
