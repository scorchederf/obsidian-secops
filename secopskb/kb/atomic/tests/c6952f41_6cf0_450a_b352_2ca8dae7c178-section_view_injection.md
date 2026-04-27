---
atomic_guid: "c6952f41-6cf0-450a-b352-2ca8dae7c178"
title: "Section View Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c6952f41-6cf0-450a-b352-2ca8dae7c178"
  - "Section View Injection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Section View Injection

This test creates a section object in the local process followed by a local section view.
The shellcode is copied into the local section view and a remote section view is created in the target process, pointing to the local section view. 
A thread is then created in the target process, using the remote section view as start address.

## Metadata

- Atomic GUID: c6952f41-6cf0-450a-b352-2ca8dae7c178
- Technique: T1055: Process Injection
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1055/T1055.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Executor

- name: powershell

### Command

```powershell
$notepad = Start-Process notepad -passthru
Start-Process "$PathToAtomicsFolder\T1055\bin\x64\InjectView.exe"
```

### Cleanup

```powershell
Stop-Process $notepad.pid
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
