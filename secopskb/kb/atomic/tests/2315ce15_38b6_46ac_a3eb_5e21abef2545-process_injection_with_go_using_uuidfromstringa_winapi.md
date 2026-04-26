---
atomic_guid: "2315ce15-38b6-46ac-a3eb-5e21abef2545"
title: "Process Injection with Go using UuidFromStringA WinAPI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "2315ce15-38b6-46ac-a3eb-5e21abef2545"
  - "Process Injection with Go using UuidFromStringA WinAPI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Injection with Go using UuidFromStringA WinAPI

Uses WinAPI UuidFromStringA to load shellcode to a memory address then executes the shellcode using EnumSystemLocalesA.
With this technique, memory is allocated on the heap and does not use commonly suspicious APIs such as VirtualAlloc, WriteProcessMemory, or CreateThread 
- PoC Credit: (https://github.com/Ne0nd0g/go-shellcode/tree/master#uuidfromstringa)
- References: 
  - https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/
  - https://twitter.com/_CPResearch_/status/1352310521752662018
  - https://blog.securehat.co.uk/process-injection/shellcode-execution-via-enumsystemlocala

## Metadata

- Atomic GUID: 2315ce15-38b6-46ac-a3eb-5e21abef2545
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
$PathToAtomicsFolder\T1055\bin\x64\UuidFromStringA.exe -debug
```

### Cleanup

```powershell
Stop-Process -Name CalculatorApp -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
