---
atomic_guid: "9dee89bd-9a98-4c4f-9e2d-4256690b0e72"
title: "Delete a single file - Windows PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "9dee89bd-9a98-4c4f-9e2d-4256690b0e72"
  - "Delete a single file - Windows PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete a single file - Windows PowerShell

Delete a single file from the temporary directory using Powershell. Upon execution, no output will be displayed. Use File Explorer to verify the file was deleted.

## Metadata

- Atomic GUID: 9dee89bd-9a98-4c4f-9e2d-4256690b0e72
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### file_to_delete

- description: File to delete. Run the prereq command to create it if it does not exist.
- type: string
- default: $env:TEMP\deleteme_T1551.004

## Dependencies

The file to delete must exist on disk at specified location (#{file_to_delete})

### Prerequisite Check

```text
if (Test-Path #{file_to_delete}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Path #{file_to_delete} | Out-Null
```

## Executor

- name: powershell

### Command

```powershell
Remove-Item -path #{file_to_delete}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
