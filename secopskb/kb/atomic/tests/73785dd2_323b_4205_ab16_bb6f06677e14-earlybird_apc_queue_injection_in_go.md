---
atomic_guid: "73785dd2-323b-4205-ab16-bb6f06677e14"
title: "EarlyBird APC Queue Injection in Go"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.004"
attack_technique_name: "Process Injection: Asynchronous Procedure Call"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.004/T1055.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "73785dd2-323b-4205-ab16-bb6f06677e14"
  - "EarlyBird APC Queue Injection in Go"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a process in a suspended state and calls QueueUserAPC WinAPI to add a UserAPC to the child process that points to allocated shellcode. 
ResumeThread is called which then calls NtTestAlert to execute the created UserAPC which then executes the shellcode.
This technique allows for the early execution of shellcode and potentially before AV/EDR can hook functions to support detection.
- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode#createprocesswithpipe)
- References: 
  - https://www.bleepingcomputer.com/news/security/early-bird-code-injection-technique-helps-malware-stay-undetected/
  - https://www.ired.team/offensive-security/code-injection-process-injection/early-bird-apc-queue-code-injection

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection#^t1055004-asynchronous-procedure-call|T1055.004: Asynchronous Procedure Call]]

## Input Arguments

### spawn_process_name

- description: Name of the process to spawn
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
$PathToAtomicsFolder\T1055.004\bin\x64\EarlyBird.exe -program "#{spawn_process_path}" -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
Stop-Process -Name "#{spawn_process_name}" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.004/T1055.004.yaml)
