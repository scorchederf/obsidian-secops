---
atomic_guid: "2988133e-561c-4e42-a15f-6281e6a9b2db"
title: "Parent PID Spoofing - Spawn from New Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.004"
attack_technique_name: "Access Token Manipulation: Parent PID Spoofing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "2988133e-561c-4e42-a15f-6281e6a9b2db"
  - "Parent PID Spoofing - Spawn from New Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Parent PID Spoofing - Spawn from New Process

Creates a notepad.exe process and then spawns a powershell.exe process as a child of it.

## Metadata

- Atomic GUID: 2988133e-561c-4e42-a15f-6281e6a9b2db
- Technique: T1134.004: Access Token Manipulation: Parent PID Spoofing
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1134.004/T1134.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.004]]

## Input Arguments

### command_line

- description: Specified command line to use
- type: string
- default: -Command Start-Sleep 10

### file_path

- description: File path or name of process to spawn
- type: path
- default: $Env:windir\System32\WindowsPowerShell\v1.0\powershell.exe

### parent_name

- description: Parent process to spoof from
- type: path
- default: $Env:windir\System32\notepad.exe

## Dependencies

The AtomicTestHarnesses module must be installed and Start-ATHProcessUnderSpecificParent must be exported in the module.

### Prerequisite Check

```untitled
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Start-ATHProcessUnderSpecificParent']) {exit 1} else {exit 0}
```

### Get Prerequisite

```untitled
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Start-Process -FilePath #{parent_name} -PassThru | Start-ATHProcessUnderSpecificParent -FilePath #{file_path} -CommandLine '#{command_line}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml)
