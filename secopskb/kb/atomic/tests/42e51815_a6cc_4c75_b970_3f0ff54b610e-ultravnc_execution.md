---
atomic_guid: "42e51815-a6cc-4c75-b970-3f0ff54b610e"
title: "UltraVNC Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "42e51815-a6cc-4c75-b970-3f0ff54b610e"
  - "UltraVNC Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UltraVNC Execution

An adversary may attempt to trick the user into downloading UltraVNC for use as a C2 channel.
Upon successful execution, UltraVNC will be executed.

## Metadata

- Atomic GUID: 42e51815-a6cc-4c75-b970-3f0ff54b610e
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Input Arguments

### UltraVNC_Viewer_Path

- description: Path of UltraVNC Viewer executable
- type: path
- default: $env:ProgramFiles\'uvnc bvba\UltraVnc\vncviewer.exe'

## Dependencies

UltraVNC must exist at (#{UltraVNC_Viewer_Path})

### Prerequisite Check

```powershell
if (Test-Path #{UltraVNC_Viewer_Path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://www.uvnc.eu/download/1381/UltraVNC_1_3_81_X64_Setup.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\vncsetup.exe"
start-process "PathToAtomicsFolder\..\ExternalPayloads\vncsetup.exe" /silent
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process #{UltraVNC_Viewer_Path}
```

### Cleanup

```powershell
Stop-Process -Name "vncviewer" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
