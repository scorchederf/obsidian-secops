---
atomic_guid: "4f3c7502-b111-4dfe-8a6e-529307891a59"
title: "Process injection ListPlanting"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.015"
attack_technique_name: "Process Injection: ListPlanting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.015/T1055.015.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4f3c7502-b111-4dfe-8a6e-529307891a59"
  - "Process injection ListPlanting"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process injection ListPlanting

This test injects shellcode into a remote RegEdit process using the ListPlanting technique. ListPlanting exploits Window with ListView control. Code write to memory with NtWriteVirtualMemory. The shellcode is executed via PostMessage. When successful, a message box will appear with the title "Warning" and the content "Atomic Red Team" after a few seconds. Notepad will open following the appearance of the message box.

## Metadata

- Atomic GUID: 4f3c7502-b111-4dfe-8a6e-529307891a59
- Technique: T1055.015: Process Injection: ListPlanting
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1055.015/T1055.015.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.015]]

## Input Arguments

### exe_binary

- description: PE binary
- type: path
- default: PathToAtomicsFolder\T1055.015\bin\ListPlanting.exe

## Dependencies

Injector ListPlanting.exe must exist at specified location (#{exe_binary})

### Prerequisite Check

```powershell
if (Test-Path "#{exe_binary}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{exe_binary}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055.015/bin/ListPlanting.exe" -OutFile "#{exe_binary}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{exe_binary}"
Start-Sleep -Seconds 7
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

### Cleanup

```powershell
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.015/T1055.015.yaml)
