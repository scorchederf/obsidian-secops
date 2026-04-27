---
atomic_guid: "b3b2c408-2ff0-4a33-b89b-1cb46a9e6a9c"
title: "Windows - Modify file creation timestamp with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b3b2c408-2ff0-4a33-b89b-1cb46a9e6a9c"
  - "Windows - Modify file creation timestamp with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows - Modify file creation timestamp with PowerShell

Modifies the file creation timestamp of a specified file. This technique was seen in use by the Stitch RAT.
To verify execution, use File Explorer to view the Properties of the file and observe that the Created time is the year 1970.

## Metadata

- Atomic GUID: b3b2c408-2ff0-4a33-b89b-1cb46a9e6a9c
- Technique: T1070.006: Indicator Removal on Host: Timestomp
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1070.006/T1070.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Input Arguments

### file_path

- description: Path of file to change creation timestamp
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1551.006_timestomp.txt

### target_date_time

- description: Date/time to replace original timestamps with
- type: string
- default: 01/01/1970 00:00:00

## Dependencies

A file must exist at the path (#{file_path}) to change the creation time on

### Prerequisite Check

```powershell
if (Test-Path "#{file_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Path "#{file_path}" -Force | Out-Null
Set-Content "#{file_path}" -Value "T1551.006 Timestomp" -Force | Out-Null
```

## Executor

- name: powershell

### Command

```powershell
Get-ChildItem "#{file_path}" | % { $_.CreationTime = "#{target_date_time}" }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
