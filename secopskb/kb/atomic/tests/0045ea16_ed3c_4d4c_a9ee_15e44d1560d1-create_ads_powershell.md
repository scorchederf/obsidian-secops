---
atomic_guid: "0045ea16-ed3c-4d4c-a9ee-15e44d1560d1"
title: "Create ADS PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.004"
attack_technique_name: "Hide Artifacts: NTFS File Attributes"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "0045ea16-ed3c-4d4c-a9ee-15e44d1560d1"
  - "Create ADS PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create an Alternate Data Stream with PowerShell. Write access is required. To verify execution, run the command "ls -Recurse | %{ gi $_.Fullname -stream *} | where stream -ne ':$Data' | Select-Object pschildname"
in the %temp% directory to view all files with hidden data streams. To view the data in the alternate data stream, run "notepad.exe T1564.004_has_ads_powershell.txt:adstest.txt" in the %temp% folder.

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Input Arguments

### ads_filename

- description: Name of ADS file.
- type: string
- default: adstest.txt

### file_name

- description: File name of file to create ADS on.
- type: string
- default: $env:TEMP\T1564.004_has_ads_powershell.txt

## Dependencies

The file must exist on disk at specified location (#{file_name})

### Prerequisite Check

```powershell
if (Test-Path #{file_name}) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
New-Item -Path #{file_name} | Out-Null
```

## Executor

- name: powershell

### Command

```powershell
echo "test" > #{file_name} | set-content -path test.txt -stream #{ads_filename} -value "test"
set-content -path #{file_name} -stream #{ads_filename} -value "test2"
set-content -path . -stream #{ads_filename} -value "test3"
```

### Cleanup

```powershell
Remove-Item -Path #{file_name} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml)
