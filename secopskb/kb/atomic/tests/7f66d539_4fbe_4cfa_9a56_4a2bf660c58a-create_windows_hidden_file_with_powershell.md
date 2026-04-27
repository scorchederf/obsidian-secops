---
atomic_guid: "7f66d539-4fbe-4cfa-9a56-4a2bf660c58a"
title: "Create Windows Hidden File with powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "7f66d539-4fbe-4cfa-9a56-4a2bf660c58a"
  - "Create Windows Hidden File with powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Windows Hidden File with powershell

Creates a file and marks it as hidden through powershell. Upon execution, open File Epxplorer and enable View > Hidden Items. Then, open Properties > Details on the file
and observe that the Attributes is "H" Hidden.

## Metadata

- Atomic GUID: 7f66d539-4fbe-4cfa-9a56-4a2bf660c58a
- Technique: T1564.001: Hide Artifacts: Hidden Files and Directories
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: command_prompt
- Source Path: atomics/T1564.001/T1564.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Input Arguments

### file_to_modify

- description: File to modify
- type: string
- default: %temp%\T1564.001-9.txt

## Dependencies

The file must exist on disk at specified location (#{file_to_modify})

### Prerequisite Check

```cmd
IF EXIST #{file_to_modify} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```cmd
echo system_Attrib_T1564.001-9 >> #{file_to_modify}
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$file = Get-Item $env:temp\T1564.001-9.txt -Force
$file.attributes='Hidden'
```

### Cleanup

```powershell
cmd /c 'del /A:H #{file_to_modify} >nul 2>&1'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
