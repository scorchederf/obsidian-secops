---
atomic_guid: "98d34bb4-6e75-42ad-9c41-1dae7dc6a001"
title: "Take ownership using takeown utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.001"
attack_technique_name: "File and Directory Permissions Modification: Windows File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "98d34bb4-6e75-42ad-9c41-1dae7dc6a001"
  - "Take ownership using takeown utility"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Take ownership using takeown utility

Modifies the filesystem permissions of the specified file or folder to take ownership of the object. Upon execution, "SUCCESS" will
be displayed for the folder and each file inside of it.

## Metadata

- Atomic GUID: 98d34bb4-6e75-42ad-9c41-1dae7dc6a001
- Technique: T1222.001: File and Directory Permissions Modification: Windows File and Directory Permissions Modification
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: command_prompt
- Source Path: atomics/T1222.001/T1222.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

## Input Arguments

### file_folder_to_own

- description: Path of the file or folder for takeown to take ownership.
- type: path
- default: %temp%\T1222.001_takeown_folder

## Dependencies

Test requrires a file to take ownership of to be located at (#{file_folder_to_own})

### Prerequisite Check

```text
IF EXIST #{file_folder_to_own} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```text
mkdir #{file_folder_to_own}
echo T1222.001_takeown1 >> #{file_folder_to_own}\T1222.001_takeown1.txt
echo T1222.001_takeown2 >> #{file_folder_to_own}\T1222.001_takeown2.txt
```

## Executor

- name: command_prompt

### Command

```commandprompt
takeown.exe /f #{file_folder_to_own} /r
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml)
