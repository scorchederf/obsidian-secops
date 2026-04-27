---
atomic_guid: "ae56083f-28d0-417d-84da-df4242da1f7c"
title: "Run Shellcode via Syscall in Go"
framework: "atomic"
generated: "true"
attack_technique_id: "T1106"
attack_technique_name: "Native API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "ae56083f-28d0-417d-84da-df4242da1f7c"
  - "Run Shellcode via Syscall in Go"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Runs shellcode in the current running process via a syscall.

Steps taken with this technique
1. Allocate memory for the shellcode with VirtualAlloc setting the page permissions to Read/Write
2. Use the RtlCopyMemory macro to copy the shellcode to the allocated memory space
3. Change the memory page permissions to Execute/Read with VirtualProtect
4. Use syscall to execute the entrypoint of the shellcode

- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode#syscall)

## ATT&CK Mapping

- [[kb/attack/techniques/T1106-native_api|T1106: Native API]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$PathToAtomicsFolder\T1106\bin\x64\syscall.exe -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml)
