---
atomic_guid: "ded937c4-2add-42f7-9c2c-c742b7a98698"
title: "Delete an entire folder - Windows cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "ded937c4-2add-42f7-9c2c-c742b7a98698"
  - "Delete an entire folder - Windows cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Recursively delete a folder in the temporary directory using cmd.exe.
Upon execution, no output will be displayed. Use File Explorer to verify the folder was deleted.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]

## Input Arguments

### folder_to_delete

- description: Folder to delete. Run the prereq command to create it if it does not exist.
- type: string
- default: %temp%\deleteme_T1551.004

## Dependencies

The file to delete must exist on disk at specified location (#{folder_to_delete})

### Prerequisite Check

```cmd
IF EXIST "#{folder_to_delete}" ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```cmd
mkdir #{folder_to_delete}
```

## Executor

- name: command_prompt

### Command

```cmd
rmdir /s /q #{folder_to_delete}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
