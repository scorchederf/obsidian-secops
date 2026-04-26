---
atomic_guid: "3e6791e7-232c-481c-a680-a52f86b83fdf"
title: "Create Hidden Directory via $index_allocation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.004"
attack_technique_name: "Hide Artifacts: NTFS File Attributes"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "3e6791e7-232c-481c-a680-a52f86b83fdf"
  - "Create Hidden Directory via $index_allocation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Hidden Directory via $index_allocation

Create an Alternate Data Stream Directory and File with the command prompt. Write access is required. Upon execution,
run "dir /A /Q /R" in the %temp% folder to view that the alternate data stream folder exists. To view the data in the
alternate data stream, run "type %temp%\...$.......::$index_allocation\secrets.txt"

## Metadata

- Atomic GUID: 3e6791e7-232c-481c-a680-a52f86b83fdf
- Technique: T1564.004: Hide Artifacts: NTFS File Attributes
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1564.004/T1564.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Input Arguments

### folder_name

- description: File name of file to create inside the folder.
- type: string
- default: %temp%\...$.......::$index_allocation

### hidden_filename

- description: Name of the files containing the hidden information
- type: string
- default: secrets.txt

## Executor

- name: command_prompt

### Command

```cmd
md #{folder_name}
echo too many secrets > #{folder_name}\#{hidden_filename}
```

### Cleanup

```cmd
rmdir /S /Q #{folder_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml)
