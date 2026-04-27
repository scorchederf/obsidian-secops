---
atomic_guid: "edd779e4-a509-4cba-8dfa-a112543dbfb1"
title: "Delete an entire folder - Windows PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "edd779e4-a509-4cba-8dfa-a112543dbfb1"
  - "Delete an entire folder - Windows PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete an entire folder - Windows PowerShell

Recursively delete a folder in the temporary directory using Powershell. Upon execution, no output will be displayed. Use File Explorer to verify the folder was deleted.

## Metadata

- Atomic GUID: edd779e4-a509-4cba-8dfa-a112543dbfb1
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### folder_to_delete

- description: Folder to delete. Run the prereq command to create it if it does not exist.
- type: string
- default: $env:TEMP\deleteme_folder_T1551.004

## Dependencies

The folder to delete must exist on disk at specified location (#{folder_to_delete})

### Prerequisite Check

```powershell
if (Test-Path #{folder_to_delete}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Path #{folder_to_delete} -Type Directory | Out-Null
```

## Executor

- name: powershell

### Command

```powershell
Remove-Item -Path #{folder_to_delete} -Recurse
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
