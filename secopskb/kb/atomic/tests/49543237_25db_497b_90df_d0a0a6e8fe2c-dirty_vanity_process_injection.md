---
atomic_guid: "49543237-25db-497b-90df-d0a0a6e8fe2c"
title: "Dirty Vanity process Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "49543237-25db-497b-90df-d0a0a6e8fe2c"
  - "Dirty Vanity process Injection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dirty Vanity process Injection

This test used the Windows undocumented remote-fork API RtlCreateProcessReflection to create a cloned process of the parent process
with shellcode written in its memory. The shellcode is executed after being forked to the child process. The technique was first presented at 
BlackHat Europe 2022. Shellcode will open a messsage box and a notepad.

## Metadata

- Atomic GUID: 49543237-25db-497b-90df-d0a0a6e8fe2c
- Technique: T1055: Process Injection
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1055/T1055.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Input Arguments

### pid

- description: Parent process ID
- type: string
- default: (Start-Process calc.exe -PassThru).Id

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Start-Process "$PathToAtomicsFolder\T1055\bin\x64\redVanity.exe" #{pid}
```

### Cleanup

```powershell
Get-Process -Name calc, CalculatorApp -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
