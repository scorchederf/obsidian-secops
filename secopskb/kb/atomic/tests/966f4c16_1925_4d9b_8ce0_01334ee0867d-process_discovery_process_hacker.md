---
atomic_guid: "966f4c16-1925-4d9b-8ce0-01334ee0867d"
title: "Process Discovery - Process Hacker"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "966f4c16-1925-4d9b-8ce0-01334ee0867d"
  - "Process Discovery - Process Hacker"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Discovery - Process Hacker

Process Hacker can be exploited to infiltrate system processes, identify weak points, or achieve unauthorized control over systems. However, its malicious use can often be flagged by security defenses, rendering it a perilous tool for illegitimate purposes.

## Metadata

- Atomic GUID: 966f4c16-1925-4d9b-8ce0-01334ee0867d
- Technique: T1057: Process Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1057/T1057.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Input Arguments

### processhacker_exe

- description: Process hacker installation executables.
- type: string
- default: ProcessHacker.exe

## Dependencies

Process Hacker must be installed in the location

### Prerequisite Check

```powershell
if (Test-Path "c:\Program Files\Process Hacker 2\#{processhacker_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Downloading Process Hacker
New-Item -Type Directory "C:\Temp\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://versaweb.dl.sourceforge.net/project/processhacker/processhacker2/processhacker-2.39-setup.exe" -OutFile "C:\Temp\ExternalPayloads\processhacker-2.39-setup.exe"
Write-Host Installing Process Hacker
Start-Process "c:\Temp\ExternalPayloads\processhacker-2.39-setup.exe" -Wait -ArgumentList "/s"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process -FilePath "$Env:ProgramFiles\Process Hacker 2\#{processhacker_exe}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
