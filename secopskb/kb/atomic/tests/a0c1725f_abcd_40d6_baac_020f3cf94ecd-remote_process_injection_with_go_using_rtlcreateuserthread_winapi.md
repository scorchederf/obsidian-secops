---
atomic_guid: "a0c1725f-abcd-40d6-baac-020f3cf94ecd"
title: "Remote Process Injection with Go using RtlCreateUserThread WinAPI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "a0c1725f-abcd-40d6-baac-020f3cf94ecd"
  - "Remote Process Injection with Go using RtlCreateUserThread WinAPI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes shellcode in a remote process.

Steps taken with this technique
1. Get a handle to the target process
2. Allocate memory for the shellcode with VirtualAllocEx setting the page permissions to Read/Write
3. Use the WriteProcessMemory to copy the shellcode to the allocated memory space in the remote process
4. Change the memory page permissions to Execute/Read with VirtualProtectEx
5. Execute the entrypoint of the shellcode in the remote process with RtlCreateUserThread
6. Close the handle to the remote process

- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode/tree/master#rtlcreateuserthread)
- References: 
  - https://www.cobaltstrike.com/blog/cobalt-strikes-process-injection-the-details-cobalt-strike

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

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
$PathToAtomicsFolder\T1055\bin\x64\RtlCreateUserThread.exe -pid $process.Id -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
Stop-Process -Name #{spawn_process_name} -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
