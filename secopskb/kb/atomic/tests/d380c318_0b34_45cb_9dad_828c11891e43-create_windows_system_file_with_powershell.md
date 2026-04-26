---
atomic_guid: "d380c318-0b34-45cb-9dad-828c11891e43"
title: "Create Windows System File with powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "d380c318-0b34-45cb-9dad-828c11891e43"
  - "Create Windows System File with powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Windows System File with powershell

Creates a file and marks it as System through powershell. Upon execution, open File Epxplorer and enable View > Hidden Items. Then, open Properties > Details on the file
and observe that the Attributes is "S" System.

## Metadata

- Atomic GUID: d380c318-0b34-45cb-9dad-828c11891e43
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
- default: %temp%\T1564.001-10.txt

## Dependencies

The file must exist on disk at specified location (#{file_to_modify})

### Prerequisite Check

```text
IF EXIST #{file_to_modify} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```text
echo system_Attrib_T1564.001-10 >> #{file_to_modify}
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$file = Get-Item $env:temp\T1564.001-10.txt -Force
$file.attributes='System'
```

### Cleanup

```powershell
cmd /c 'del /A:H #{file_to_modify} >nul 2>&1'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
