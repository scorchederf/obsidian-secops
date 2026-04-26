---
atomic_guid: "2770dea7-c50f-457b-84c4-c40a47460d9f"
title: "Execution of program.exe as service with unquoted service path"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.009"
attack_technique_name: "Hijack Execution Flow: Path Interception by Unquoted Path"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.009/T1574.009.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "2770dea7-c50f-457b-84c4-c40a47460d9f"
  - "Execution of program.exe as service with unquoted service path"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execution of program.exe as service with unquoted service path

When a service is created whose executable path contains spaces and isn’t enclosed within quotes, leads to a vulnerability
known as Unquoted Service Path which allows a user to gain SYSTEM privileges.
In this case, if an executable program.exe in C:\ exists, C:\program.exe will be executed instead of test.exe in C:\Program Files\subfolder\test.exe.

## Metadata

- Atomic GUID: 2770dea7-c50f-457b-84c4-c40a47460d9f
- Technique: T1574.009: Hijack Execution Flow: Path Interception by Unquoted Path
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1574.009/T1574.009.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.009]]

## Input Arguments

### service_executable

- description: Path of the executable used for the service and as the hijacked program.exe
- type: path
- default: PathToAtomicsFolder\T1574.009\bin\WindowsServiceExample.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
copy "#{service_executable}" "C:\Program Files\windows_service.exe"
copy "#{service_executable}" "C:\program.exe"
sc create "Example Service" binpath= "C:\Program Files\windows_service.exe" Displayname= "Example Service" start= auto
sc start "Example Service"
```

### Cleanup

```cmd
sc stop "Example Service" >nul 2>&1
sc delete "Example Service" >nul 2>&1
del "C:\Program Files\windows_service.exe" >nul 2>&1
del "C:\program.exe" >nul 2>&1
del "C:\Time.log" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.009/T1574.009.yaml)
