---
atomic_guid: "f70974c8-c094-4574-b542-2c545af95a32"
title: "Create Windows System File with Attrib"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "f70974c8-c094-4574-b542-2c545af95a32"
  - "Create Windows System File with Attrib"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a file and marks it as a system file using the attrib.exe utility. Upon execution, open the file in file explorer then open Properties > Details
and observe that the Attributes are "SA" for System and Archive.

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]

## Input Arguments

### file_to_modify

- description: File to modify using Attrib command
- type: string
- default: %temp%\T1564.001.txt

## Dependencies

The file must exist on disk at specified location (#{file_to_modify})

### Prerequisite Check

```cmd
IF EXIST #{file_to_modify} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```cmd
echo system_Attrib_T1564.001 >> #{file_to_modify}
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
attrib.exe +s #{file_to_modify}
```

### Cleanup

```cmd
del /A:S #{file_to_modify} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
