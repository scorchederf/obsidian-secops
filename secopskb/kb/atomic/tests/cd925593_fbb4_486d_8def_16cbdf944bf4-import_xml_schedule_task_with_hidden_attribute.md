---
atomic_guid: "cd925593-fbb4-486d-8def-16cbdf944bf4"
title: "Import XML Schedule Task with Hidden Attribute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "cd925593-fbb4-486d-8def-16cbdf944bf4"
  - "Import XML Schedule Task with Hidden Attribute"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Import XML Schedule Task with Hidden Attribute

Create an scheduled task that executes calc.exe after user login from XML that contains hidden setting attribute. 
This technique was seen several times in tricbot malware and also with the targetted attack campaigne the industroyer2.

## Metadata

- Atomic GUID: cd925593-fbb4-486d-8def-16cbdf944bf4
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
- default: PathToAtomicsFolder\T1053.005\src\T1053_05_SCTASK_HIDDEN_ATTRIB.xml

## Dependencies

File to copy must exist on disk at specified location (#{xml_path})

### Prerequisite Check

```powershell
if (Test-Path "#{xml_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{xml_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1053.005/src/T1053_05_SCTASK_HIDDEN_ATTRIB.xml" -OutFile "#{xml_path}"
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
Unregister-ScheduledTask -TaskName "atomic red team" -confirm:$false >$null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
