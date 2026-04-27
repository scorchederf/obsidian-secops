---
atomic_guid: "96e86706-6afd-45b6-95d6-108d23eaf2e9"
title: "Indicator Manipulation using FSUtil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070"
attack_technique_name: "Indicator Removal on Host"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070/T1070.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "96e86706-6afd-45b6-95d6-108d23eaf2e9"
  - "Indicator Manipulation using FSUtil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Indicator Manipulation using FSUtil

Finds a file by user name (if Disk Quotas are enabled), queries allocated ranges for a file, sets a file's short name, sets a file's valid data length, sets zero data for a file, or creates a new file. Upon execution, no output
will be displayed. More information about fsutil can be found at https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-file
- https://tria.ge/230601-x8x6bsgb24/behavioral2

## Metadata

- Atomic GUID: 96e86706-6afd-45b6-95d6-108d23eaf2e9
- Technique: T1070: Indicator Removal on Host
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1070/T1070.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Input Arguments

### file_data_length

- description: Data length to setzero
- type: integer
- default: 10

### file_to_manipulate

- description: Path of file to manipulate
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1070-2.txt

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
if (-not (Test-Path "#{file_to_manipulate}")) { New-Item "#{file_to_manipulate}" -Force } 
echo "1234567890" > "#{file_to_manipulate}"
fsutil  file setZeroData offset=0 length=#{file_data_length} "#{file_to_manipulate}"
```

### Cleanup

```powershell
rm "#{file_to_manipulate}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070/T1070.yaml)
