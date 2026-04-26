---
atomic_guid: "861ea0b4-708a-4d17-848d-186c9c7f17e3"
title: "Delete a single file - Windows cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "861ea0b4-708a-4d17-848d-186c9c7f17e3"
  - "Delete a single file - Windows cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete a single file - Windows cmd

Delete a single file from the temporary directory using cmd.exe.
Upon execution, no output will be displayed. Use File Explorer to verify the file was deleted.

## Metadata

- Atomic GUID: 861ea0b4-708a-4d17-848d-186c9c7f17e3
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: command_prompt
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### file_to_delete

- description: File to delete. Run the prereq command to create it if it does not exist.
- type: string
- default: %temp%\deleteme_T1551.004

## Dependencies

The file to delete must exist on disk at specified location (#{file_to_delete})

### Prerequisite Check

```text
IF EXIST "#{file_to_delete}" ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```text
echo deleteme_T1551.004 >> #{file_to_delete}
```

## Executor

- name: command_prompt

### Command

```commandprompt
del /f #{file_to_delete}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
