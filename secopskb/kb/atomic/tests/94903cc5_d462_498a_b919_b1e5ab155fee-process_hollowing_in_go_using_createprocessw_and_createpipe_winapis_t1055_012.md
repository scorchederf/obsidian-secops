---
atomic_guid: "94903cc5-d462-498a-b919-b1e5ab155fee"
title: "Process Hollowing in Go using CreateProcessW and CreatePipe WinAPIs (T1055.012)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.012"
attack_technique_name: "Process Injection: Process Hollowing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.012/T1055.012.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "94903cc5-d462-498a-b919-b1e5ab155fee"
  - "Process Hollowing in Go using CreateProcessW and CreatePipe WinAPIs (T1055.012)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create a process in a suspended state, execute shellcode to spawn calc.exe in a child process, and then resume the original process.
This test uses the CreatePipe function to create an anonymous pipe that parent and child processes can communicate over. This anonymous pipe
allows for the retrieval of output generated from executed shellcode.
- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode#createprocesswithpipe)

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]

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
$PathToAtomicsFolder\T1055.012\bin\x64\CreateProcessWithPipe.exe -program "#{hollow_binary_path}" -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
Stop-Process -Name "#{hollow_process_name}" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.012/T1055.012.yaml)
