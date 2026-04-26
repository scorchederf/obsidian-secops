---
atomic_guid: "3e1858ee-3550-401c-86ec-5e70ed79295b"
title: "Splashtop Streamer Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "3e1858ee-3550-401c-86ec-5e70ed79295b"
  - "Splashtop Streamer Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Splashtop Streamer Execution

An adversary may attempt to use Splashtop Streamer to gain unattended remote interactive access. Upon successful execution, Splashtop streamer will be executed.

## Metadata

- Atomic GUID: 3e1858ee-3550-401c-86ec-5e70ed79295b
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Input Arguments

### srserver_exe

- description: Splashtop streamer installation executables
- type: string
- default: SRServer.exe

## Dependencies

Splashtop Streamer must be installed in the location

### Prerequisite Check

```text
if (Test-Path "C:\Program Files (x86)\Splashtop\Splashtop Remote\Server\#{srserver_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host Downloading Splashtop Streamer
New-Item -Type Directory "C:\Temp\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.splashtop.com/win/Splashtop_Streamer_Win_INSTALLER_v3.6.4.1.exe" -OutFile  "C:\Temp\ExternalPayloads\Splashtop.exe"
Write-Host Installing Splashtop Streamer
Start-Process "c:\Temp\ExternalPayloads\Splashtop.exe" -Wait -ArgumentList "/s"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process -FilePath "C:Program Files (x86)\Splashtop\Splashtop Remote\Server\#{srserver_exe}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
