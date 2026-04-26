---
atomic_guid: "0ae9e327-3251-465a-a53b-485d4e3f58fa"
title: "Ammyy Admin Software Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "0ae9e327-3251-465a-a53b-485d4e3f58fa"
  - "Ammyy Admin Software Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Ammyy Admin Software Execution

An adversary may attempt to trick the user into downloading Ammyy Admin Remote Desktop Software for use as a C2 channel. 
Upon successful execution, Ammyy Admin will be executed.

## Metadata

- Atomic GUID: 0ae9e327-3251-465a-a53b-485d4e3f58fa
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Input Arguments

### Ammyy_Admin_Path

- description: Path of Ammyy Admin executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\ammyy.exe

## Dependencies

Ammyy Admin must exist on disk at the specified location (#{Ammyy_Admin_Path})

### Prerequisite Check

```text
if (Test-Path "#{Ammyy_Admin_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://web.archive.org/web/20140625232737/http://www.ammyy.com/AA_v3.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\ammyy.exe" -UseBasicParsing
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{Ammyy_Admin_Path}"
```

### Cleanup

```powershell
Stop-Process -Name "Ammyy" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
