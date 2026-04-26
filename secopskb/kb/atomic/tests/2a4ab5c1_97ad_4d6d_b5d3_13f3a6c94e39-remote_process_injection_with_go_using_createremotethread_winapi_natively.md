---
atomic_guid: "2a4ab5c1-97ad-4d6d-b5d3-13f3a6c94e39"
title: "Remote Process Injection with Go using CreateRemoteThread WinAPI (Natively)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "2a4ab5c1-97ad-4d6d-b5d3-13f3a6c94e39"
  - "Remote Process Injection with Go using CreateRemoteThread WinAPI (Natively)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote Process Injection with Go using CreateRemoteThread WinAPI (Natively)

Leverages the Windows CreateRemoteThread function from Kernel32.dll to execute shellcode in a remote process.

This program loads the DLLs and gets a handle to the used procedures itself instead of using the windows package directly.

1. Get a handle to the target process
2. Allocate memory for the shellcode with VirtualAllocEx setting the page permissions to Read/Write
3. Use the WriteProcessMemory to copy the shellcode to the allocated memory space in the remote process
4. Change the memory page permissions to Execute/Read with VirtualProtectEx
5. Execute the entrypoint of the shellcode in the remote process with CreateRemoteThread
6. Close the handle to the remote process

- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode#createremotethreadnative)

## Metadata

- Atomic GUID: 2a4ab5c1-97ad-4d6d-b5d3-13f3a6c94e39
- Technique: T1055: Process Injection
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1055/T1055.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Input Arguments

### spawn_process_name

- description: Name of the process spawned
- type: string
- default: werfault

### spawn_process_path

- description: Path of the binary to spawn
- type: string
- default: C:\Windows\System32\werfault.exe

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$process = Start-Process #{spawn_process_path} -passthru
$PathToAtomicsFolder\T1055\bin\x64\CreateRemoteThreadNative.exe -pid $process.Id -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
Stop-Process -Name #{spawn_process_name} -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
