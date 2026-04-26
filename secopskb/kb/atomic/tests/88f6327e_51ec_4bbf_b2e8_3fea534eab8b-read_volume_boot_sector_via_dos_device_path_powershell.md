---
atomic_guid: "88f6327e-51ec-4bbf-b2e8-3fea534eab8b"
title: "Read volume boot sector via DOS device path (PowerShell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1006"
attack_technique_name: "Direct Volume Access"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1006/T1006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "88f6327e-51ec-4bbf-b2e8-3fea534eab8b"
  - "Read volume boot sector via DOS device path (PowerShell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Read volume boot sector via DOS device path (PowerShell)

This test uses PowerShell to open a handle on the drive volume via the `\\.\` [DOS device path specifier](https://docs.microsoft.com/en-us/dotnet/standard/io/file-path-formats#dos-device-paths) and perform direct access read of the first few bytes of the volume.
On success, a hex dump of the first 11 bytes of the volume is displayed.

For a NTFS volume, it should correspond to the following sequence ([NTFS partition boot sector](https://en.wikipedia.org/wiki/NTFS#Partition_Boot_Sector_(VBR))):
```
           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

00000000   EB 52 90 4E 54 46 53 20 20 20 20                 ëR?NTFS
```

## Metadata

- Atomic GUID: 88f6327e-51ec-4bbf-b2e8-3fea534eab8b
- Technique: T1006: Direct Volume Access
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1006/T1006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1006-direct_volume_access|T1006]]

## Input Arguments

### volume

- description: Drive letter of the volume to access
- type: string
- default: C:

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$buffer = New-Object byte[] 11
$handle = New-Object IO.FileStream "\\.\#{volume}", 'Open', 'Read', 'ReadWrite'
$handle.Read($buffer, 0, $buffer.Length)
$handle.Close()
Format-Hex -InputObject $buffer
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1006/T1006.yaml)
