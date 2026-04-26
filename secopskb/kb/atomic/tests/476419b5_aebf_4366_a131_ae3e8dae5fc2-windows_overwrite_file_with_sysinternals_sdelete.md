---
atomic_guid: "476419b5-aebf-4366-a131-ae3e8dae5fc2"
title: "Windows - Overwrite file with SysInternals SDelete"
framework: "atomic"
generated: "true"
attack_technique_id: "T1485"
attack_technique_name: "Data Destruction"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "476419b5-aebf-4366-a131-ae3e8dae5fc2"
  - "Windows - Overwrite file with SysInternals SDelete"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Overwrite file with SysInternals SDelete

Overwrites and deletes a file using SysInternals SDelete. Upon successful execution, "Files deleted: 1" will be displayed in
the powershell session along with other information about the file that was deleted.

## Metadata

- Atomic GUID: 476419b5-aebf-4366-a131-ae3e8dae5fc2
- Technique: T1485: Data Destruction
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1485/T1485.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Input Arguments

### file_to_delete

- description: Path of file to delete
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1485.txt

### sdelete_exe

- description: Path of sdelete executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\Sdelete\sdelete.exe

## Dependencies

Secure delete tool from SysInternals must exist on disk at specified location (#{sdelete_exe})

### Prerequisite Check

```text
if (Test-Path "#{sdelete_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/SDelete.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\SDelete.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\SDelete.zip" "PathToAtomicsFolder\..\ExternalPayloads\Sdelete" -Force
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\SDelete.zip" -Force
```

## Executor

- name: powershell

### Command

```powershell
if (-not (Test-Path "#{file_to_delete}")) { New-Item "#{file_to_delete}" -Force }
& "#{sdelete_exe}" -accepteula "#{file_to_delete}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml)
