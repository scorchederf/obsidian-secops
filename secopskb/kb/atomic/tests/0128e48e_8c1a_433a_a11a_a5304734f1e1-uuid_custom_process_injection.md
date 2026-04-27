---
atomic_guid: "0128e48e-8c1a-433a-a11a-a5304734f1e1"
title: "UUID custom process Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "0128e48e-8c1a-433a-a11a-a5304734f1e1"
  - "UUID custom process Injection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The UUIDs Process Injection code was first introduced by the NCC Group. The code can be stored in UUID forms on the heap and converted back to binary via UuidFromStringA at runtime. In this new custom version of UUID injection, EnumSystemLocalesA is the only API called to execute the code. We used custom UuidToString and UuidFromString implementations to avoid using UuidFromStringA and RPCRT4.dll, thereby eliminating the static signatures. This technique also avoided the use of VirtualAlloc, WriteProcessMemory and CreateThread

The injected shellcode will open a message box and a notepad.

Reference to NCC Group: https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/
Concept from: http://ropgadget.com/posts/abusing_win_functions.html

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Input Arguments

### exe_binary

- description: PE binary
- type: path
- default: PathToAtomicsFolder\T1055\bin\x64\uuid_injection.exe

## Dependencies

Portable Executable to inject must exist at specified location (#{exe_binary})

### Prerequisite Check

```powershell
if (Test-Path "#{exe_binary}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{exe_binary}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055/bin/x64/uuid_injection.exe" -OutFile "#{exe_binary}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{exe_binary}"
Start-Sleep -Seconds 7
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

### Cleanup

```powershell
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
