---
atomic_guid: "8e5c5532-1181-4c1d-bb79-b3a9f5dbd680"
title: "NTFS Alternate Data Stream Access"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "8e5c5532-1181-4c1d-bb79-b3a9f5dbd680"
  - "NTFS Alternate Data Stream Access"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a file with an alternate data stream and simulates executing that hidden code/file. Upon execution, "Stream Data Executed" will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Input Arguments

### ads_file

- description: File created to store Alternate Stream Data
- type: string
- default: $env:TEMP\NTFS_ADS.txt

## Dependencies

Homedrive must be an NTFS drive

### Prerequisite Check

```untitled
if((Get-Volume -DriveLetter $env:HOMEDRIVE[0]).FileSystem -contains "NTFS") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
Write-Host Prereq's for this test cannot be met automatically
```

## Executor

- name: powershell

### Command

```powershell
Add-Content -Path #{ads_file} -Value 'Write-Host "Stream Data Executed"' -Stream 'streamCommand'
$streamcommand = Get-Content -Path #{ads_file} -Stream 'streamcommand'
Invoke-Expression $streamcommand
```

### Cleanup

```powershell
Remove-Item #{ads_file} -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
