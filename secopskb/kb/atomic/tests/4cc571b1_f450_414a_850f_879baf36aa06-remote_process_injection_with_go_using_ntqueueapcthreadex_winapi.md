---
atomic_guid: "4cc571b1-f450-414a-850f-879baf36aa06"
title: "Remote Process Injection with Go using NtQueueApcThreadEx WinAPI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.004"
attack_technique_name: "Process Injection: Asynchronous Procedure Call"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.004/T1055.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4cc571b1-f450-414a-850f-879baf36aa06"
  - "Remote Process Injection with Go using NtQueueApcThreadEx WinAPI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote Process Injection with Go using NtQueueApcThreadEx WinAPI

Uses the undocumented NtQueueAPCThreadEx WinAPI to create a "Special User APC" in the current thread of the current process to execute shellcode. 
Since the shellcode is loaded and executed in the current process it is considered local shellcode execution.

Steps taken with this technique
1. Allocate memory for the shellcode with VirtualAlloc setting the page permissions to Read/Write
2. Use the RtlCopyMemory macro to copy the shellcode to the allocated memory space
3. Change the memory page permissions to Execute/Read with VirtualProtect
4. Get a handle to the current thread
5. Execute the shellcode in the current thread by creating a Special User APC through the NtQueueApcThreadEx function

- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode/tree/master#rtlcreateuserthread)
- References:
  - https://repnz.github.io/posts/apc/user-apc/
  - https://docs.rs/ntapi/0.3.1/ntapi/ntpsapi/fn.NtQueueApcThreadEx.html
  - https://0x00sec.org/t/process-injection-apc-injection/24608
  - https://twitter.com/aionescu/status/992264290924032005
  - http://www.opening-windows.com/techart_windows_vista_apc_internals2.htm#_Toc229652505

## Metadata

- Atomic GUID: 4cc571b1-f450-414a-850f-879baf36aa06
- Technique: T1055.004: Process Injection: Asynchronous Procedure Call
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1055.004/T1055.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.004]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$PathToAtomicsFolder\T1055.004\bin\x64\NtQueueApcThreadEx.exe -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.004/T1055.004.yaml)
