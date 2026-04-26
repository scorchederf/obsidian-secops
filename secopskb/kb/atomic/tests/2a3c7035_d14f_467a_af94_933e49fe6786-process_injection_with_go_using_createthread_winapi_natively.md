---
atomic_guid: "2a3c7035-d14f-467a-af94-933e49fe6786"
title: "Process Injection with Go using CreateThread WinAPI (Natively)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "2a3c7035-d14f-467a-af94-933e49fe6786"
  - "Process Injection with Go using CreateThread WinAPI (Natively)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Injection with Go using CreateThread WinAPI (Natively)

This program executes shellcode in the current process using the following steps
1. Allocate memory for the shellcode with VirtualAlloc setting the page permissions to Read/Write
2. Use the RtlCopyMemory macro to copy the shellcode to the allocated memory space
3. Change the memory page permissions to Execute/Read with VirtualProtect
4. Call CreateThread on shellcode address
5. Call WaitForSingleObject so the program does not end before the shellcode is executed

This program loads the DLLs and gets a handle to the used procedures itself instead of using the windows package directly.

- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode#createthreadnative)

## Metadata

- Atomic GUID: 2a3c7035-d14f-467a-af94-933e49fe6786
- Technique: T1055: Process Injection
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1055/T1055.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$PathToAtomicsFolder\T1055\bin\x64\CreateThreadNative.exe -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
