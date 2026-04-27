---
atomic_guid: "7362ecef-6461-402e-8716-7410e1566400"
title: "Process Injection with Go using EtwpCreateEtwThread WinAPI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7362ecef-6461-402e-8716-7410e1566400"
  - "Process Injection with Go using EtwpCreateEtwThread WinAPI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Injection with Go using EtwpCreateEtwThread WinAPI

Uses EtwpCreateEtwThread function from ntdll.dll to execute shellcode within the application's process.
This program loads the DLLs and gets a handle to the used procedures itself instead of using the windows package directly.

Steps taken with this technique
1. Allocate memory for the shellcode with VirtualAlloc setting the page permissions to Read/Write
2. Use the RtlCopyMemory macro to copy the shellcode to the allocated memory space
3. Change the memory page permissions to Execute/Read with VirtualProtect
4. Call EtwpCreateEtwThread on shellcode address
5. Call WaitForSingleObject so the program does not end before the shellcode is executed

- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode/tree/master#EtwpCreateEtwThread)
- References: 
  - https://gist.github.com/TheWover/b2b2e427d3a81659942f4e8b9a978dc3
  - https://www.geoffchappell.com/studies/windows/win32/ntdll/api/etw/index.htm

## Metadata

- Atomic GUID: 7362ecef-6461-402e-8716-7410e1566400
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
$PathToAtomicsFolder\T1055\bin\x64\EtwpCreateEtwThread.exe -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
