---
atomic_guid: "b1b8128b-c5d4-4de9-bf70-e60419274562"
title: "MSP360 Connect Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b1b8128b-c5d4-4de9-bf70-e60419274562"
  - "MSP360 Connect Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSP360 Connect Execution

An adversary may attempt to trick the user into downloading MSP360 Connect for use as a C2 channel.
Upon successful execution, MSP360 Connect will be executed.

## Metadata

- Atomic GUID: b1b8128b-c5d4-4de9-bf70-e60419274562
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Input Arguments

### MSP360_Connect_Path

- description: Path of MSP360 executable
- type: path
- default: $env:ProgramFiles\Connect\Connect.exe

### MSP360_Download_Url

- description: URL to download MSP360 Connect from
- type: url

## Dependencies

MSP360 must exist at (#{MSP360_Connect_Path})

### Prerequisite Check

```powershell
if (Test-Path #{MSP360_Connect_Path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\msp360connect.exe" "#{MSP360_Download_Url}"
start-process "PathToAtomicsFolder\..\ExternalPayloads\msp360connect.exe" /S
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process #{MSP360_Connect_Path}
```

### Cleanup

```powershell
Stop-Process -Name "Connect" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
