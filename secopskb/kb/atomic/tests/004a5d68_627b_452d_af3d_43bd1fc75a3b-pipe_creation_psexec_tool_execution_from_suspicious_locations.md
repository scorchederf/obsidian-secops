---
atomic_guid: "004a5d68-627b-452d-af3d-43bd1fc75a3b"
title: "Pipe Creation - PsExec Tool Execution From Suspicious Locations"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "004a5d68-627b-452d-af3d-43bd1fc75a3b"
  - "Pipe Creation - PsExec Tool Execution From Suspicious Locations"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Pipe Creation - PsExec Tool Execution From Suspicious Locations

Requires PsExec tool installed. BlackCat Ransomeware tried to propagate by creating pipe using PsExec process executing from suspicious locations (In the particular case the legitimate PsExec executable is embedded within the Windows variant and is dropped in the victim’s %TEMP% directory). pon successful execution, PsExec will be executed from suspicious location and create a new pipe to execute CMD.

## Metadata

- Atomic GUID: 004a5d68-627b-452d-af3d-43bd1fc75a3b
- Technique: T1569.002: System Services: Service Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1569.002/T1569.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Dependencies

PsExec tool from Sysinternals must exist in the '\Users\Public\Temp\' directory

### Prerequisite Check

```powershell
if (Get-ChildItem -Path C:\ -Include *psexec* -File -Recurse -ErrorAction SilentlyContinue) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "C:\Users\Public\Temp\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "C:\Users\Public\Temp\PSTools.zip"
Expand-Archive "C:\Users\Public\Temp\PsTools.zip" "C:\Users\Public\Temp\" -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
cd C:\Users\Public\Temp\ 
.\PsExec.exe -i -s cmd  -accepteula
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
