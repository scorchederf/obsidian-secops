---
atomic_guid: "30cbeda4-08d9-42f1-8685-197fad677734"
title: "HTML Smuggling Remote Payload"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.006"
attack_technique_name: "HTML Smuggling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.006/T1027.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "30cbeda4-08d9-42f1-8685-197fad677734"
  - "HTML Smuggling Remote Payload"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HTML Smuggling Remote Payload

The HTML file will download an ISO file from [T1553.005](https://github.com/redcanaryco/atomic-red-team/blob/d0dad62dbcae9c60c519368e82c196a3db577055/atomics/T1553.005/bin/FeelTheBurn.iso) without user interaction. 
The HTML file is based off of the work from [Stan Hegt](https://outflank.nl/blog/2018/08/14/html-smuggling-explained/)

## Metadata

- Atomic GUID: 30cbeda4-08d9-42f1-8685-197fad677734
- Technique: T1027.006: HTML Smuggling
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1027.006/T1027.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.006]]

## Dependencies

T1027_006_remote.html must exist on disk at specified at PathToAtomicsFolder\T1027.006\bin\T1027_006_Remote.html

### Prerequisite Check

```untitled
if (Test-Path "PathToAtomicsFolder\T1027.006\bin\T1027_006_Remote.html") { exit 0} else { exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\T1027.006\bin\" -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027.006/bin/T1027_006_Remote.html" -OutFile "PathToAtomicsFolder\T1027.006\bin\T1027_006_Remote.html"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
& "PathToAtomicsFolder\T1027.006\bin\T1027_006_remote.html"
```

### Cleanup

```powershell
$user = [System.Environment]::UserName; Remove-Item -Path C:\Users\$user\Downloads\FeelTheBurn.iso -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.006/T1027.006.yaml)
