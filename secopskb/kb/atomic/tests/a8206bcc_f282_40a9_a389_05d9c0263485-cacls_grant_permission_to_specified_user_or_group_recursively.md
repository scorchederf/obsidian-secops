---
atomic_guid: "a8206bcc-f282-40a9-a389-05d9c0263485"
title: "cacls - Grant permission to specified user or group recursively"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.001"
attack_technique_name: "File and Directory Permissions Modification: Windows File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "a8206bcc-f282-40a9-a389-05d9c0263485"
  - "cacls - Grant permission to specified user or group recursively"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# cacls - Grant permission to specified user or group recursively

Modifies the filesystem permissions of the specified folder and contents to allow the specified user or group Full Control. If "Access is denied"
is displayed it may be because the file or folder doesn't exit. Run the prereq command to create it. Upon successfull execution, "Successfully processed 3 files"
will be displayed.

## Metadata

- Atomic GUID: a8206bcc-f282-40a9-a389-05d9c0263485
- Technique: T1222.001: File and Directory Permissions Modification: Windows File and Directory Permissions Modification
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: command_prompt
- Source Path: atomics/T1222.001/T1222.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

## Input Arguments

### file_or_folder

- description: Path of the file or folder to change permissions.
- type: path
- default: %temp%\T1222.001_cacls

### user_or_group

- description: User or group to allow full control
- type: string
- default: Everyone

## Dependencies

Test requrires a file to modify to be located at (#{file_or_folder})

### Prerequisite Check

```cmd
IF EXIST #{file_or_folder} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```cmd
mkdir #{file_or_folder}
echo T1222.001_cacls1 >> #{file_or_folder}\T1222.001_cacls1.txt
echo T1222.001_cacls2 >> #{file_or_folder}\T1222.001_cacls2.txt
```

## Executor

- name: command_prompt

### Command

```cmd
icacls.exe #{file_or_folder} /grant #{user_or_group}:F
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml)
