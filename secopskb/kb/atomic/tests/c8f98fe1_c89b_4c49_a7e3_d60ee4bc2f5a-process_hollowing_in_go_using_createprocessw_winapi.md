---
atomic_guid: "c8f98fe1-c89b-4c49-a7e3-d60ee4bc2f5a"
title: "Process Hollowing in Go using CreateProcessW WinAPI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.012"
attack_technique_name: "Process Injection: Process Hollowing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.012/T1055.012.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c8f98fe1-c89b-4c49-a7e3-d60ee4bc2f5a"
  - "Process Hollowing in Go using CreateProcessW WinAPI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Hollowing in Go using CreateProcessW WinAPI

Creates a process in a suspended state, executes shellcode to spawn calc.exe in a child process, and then resumes the original process.
- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode#createprocess)

## Metadata

- Atomic GUID: c8f98fe1-c89b-4c49-a7e3-d60ee4bc2f5a
- Technique: T1055.012: Process Injection: Process Hollowing
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1055.012/T1055.012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.012]]

## Input Arguments

### hollow_binary_path

- description: Path of the binary to hollow
- type: string
- default: C:\Windows\System32\werfault.exe

### hollow_process_name

- description: Name of the process to hollow
- type: string
- default: werfault

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$PathToAtomicsFolder\T1055.012\bin\x64\CreateProcess.exe -program "#{hollow_binary_path}" -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
Stop-Process -Name "#{hollow_process_name}" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.012/T1055.012.yaml)
