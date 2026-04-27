---
atomic_guid: "10447c83-fc38-462a-a936-5102363b1c43"
title: "Create a Process using obfuscated Win32_Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "10447c83-fc38-462a-a936-5102363b1c43"
  - "Create a Process using obfuscated Win32_Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a Process using obfuscated Win32_Process

This test tries to mask process creation by creating a new class that inherits from Win32_Process. Indirect call of suspicious method such as Win32_Process::Create can break detection logic.
[Cybereason blog post No Win32_ProcessNeeded](https://www.cybereason.com/blog/wmi-lateral-movement-win32)

## Metadata

- Atomic GUID: 10447c83-fc38-462a-a936-5102363b1c43
- Technique: T1047: Windows Management Instrumentation
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1047/T1047.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Input Arguments

### new_class

- description: Derived class name
- type: string
- default: Win32_Atomic

### process_to_execute

- description: Name or path of process to execute.
- type: string
- default: notepad.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$Class = New-Object Management.ManagementClass(New-Object Management.ManagementPath("Win32_Process"))
$NewClass = $Class.Derive("#{new_class}")
$NewClass.Put()
Invoke-WmiMethod -Path #{new_class} -Name create -ArgumentList #{process_to_execute}
```

### Cleanup

```powershell
$CleanupClass = New-Object Management.ManagementClass(New-Object Management.ManagementPath("#{new_class}"))
try { $CleanupClass.Delete() } catch {}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
