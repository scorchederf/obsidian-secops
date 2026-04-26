---
atomic_guid: "2ab75061-f5d5-4c1a-b666-ba2a50df5b02"
title: "Store file in Alternate Data Stream (ADS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.004"
attack_technique_name: "Hide Artifacts: NTFS File Attributes"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "2ab75061-f5d5-4c1a-b666-ba2a50df5b02"
  - "Store file in Alternate Data Stream (ADS)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Store file in Alternate Data Stream (ADS)

Storing files in Alternate Data Stream (ADS) similar to Astaroth malware.
Upon execution, cmd will run and attempt to launch desktop.ini. No windows remain open after the test

## Metadata

- Atomic GUID: 2ab75061-f5d5-4c1a-b666-ba2a50df5b02
- Technique: T1564.004: Hide Artifacts: NTFS File Attributes
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1564.004/T1564.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Input Arguments

### ads_file_path

- description: Path of file to create an ADS under
- type: path
- default: C:\Users\Public\Libraries\yanki\desktop.ini

### ads_name

- description: Name of ADS
- type: string
- default: desktop.ini

### payload_path

- description: Path of file to hide in ADS
- type: path
- default: c:\windows\system32\cmd.exe

## Executor

- name: powershell

### Command

```powershell
if (!(Test-Path C:\Users\Public\Libraries\yanki -PathType Container)) {
    New-Item -ItemType Directory -Force -Path C:\Users\Public\Libraries\yanki
    }
Start-Process -FilePath "$env:comspec" -ArgumentList "/c,type,#{payload_path},>,`"#{ads_file_path}:#{ads_name}`""
```

### Cleanup

```powershell
Remove-Item "#{ads_file_path}" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml)
