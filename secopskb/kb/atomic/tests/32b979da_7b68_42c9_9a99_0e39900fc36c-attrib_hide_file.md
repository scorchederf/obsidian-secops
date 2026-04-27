---
atomic_guid: "32b979da-7b68-42c9-9a99-0e39900fc36c"
title: "attrib - hide file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.001"
attack_technique_name: "File and Directory Permissions Modification: Windows File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "32b979da-7b68-42c9-9a99-0e39900fc36c"
  - "attrib - hide file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# attrib - hide file

Attackers leverage an existing Windows binary, attrib.exe, to mark specific files or folder as hidden by using specific flags so that
the victim does not see the file.

## Metadata

- Atomic GUID: 32b979da-7b68-42c9-9a99-0e39900fc36c
- Technique: T1222.001: File and Directory Permissions Modification: Windows File and Directory Permissions Modification
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1222.001/T1222.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

## Input Arguments

### file_or_folder

- description: Path of the files to hide.
- type: path
- default: %temp%\T1222.001_attrib_2

## Executor

- name: command_prompt

### Command

```cmd
mkdir #{file_or_folder} >nul 2>&1
echo T1222.001_attrib1 >> #{file_or_folder}\T1222.001_attrib1.txt
echo T1222.001_attrib2 >> #{file_or_folder}\T1222.001_attrib2.txt
attrib.exe +h #{file_or_folder}\T1222.001_attrib1.txt
attrib.exe +h #{file_or_folder}\T1222.001_attrib2.txt
```

### Cleanup

```cmd
del /A:H #{file_or_folder}\T1222.001_attrib*.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml)
