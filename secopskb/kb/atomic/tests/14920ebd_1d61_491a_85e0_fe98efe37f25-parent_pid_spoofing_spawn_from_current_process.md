---
atomic_guid: "14920ebd-1d61-491a-85e0-fe98efe37f25"
title: "Parent PID Spoofing - Spawn from Current Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.004"
attack_technique_name: "Access Token Manipulation: Parent PID Spoofing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "14920ebd-1d61-491a-85e0-fe98efe37f25"
  - "Parent PID Spoofing - Spawn from Current Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Parent PID Spoofing - Spawn from Current Process

Spawns a powershell.exe process as a child of the current process.

## Metadata

- Atomic GUID: 14920ebd-1d61-491a-85e0-fe98efe37f25
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

### parent_pid

- description: PID of process to spawn from
- type: string
- default: $PID

## Dependencies

The AtomicTestHarnesses module must be installed and Start-ATHProcessUnderSpecificParent must be exported in the module.

### Prerequisite Check

```text
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Start-ATHProcessUnderSpecificParent']) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Start-ATHProcessUnderSpecificParent -FilePath #{file_path} -CommandLine '#{command_line}' -ParentId #{parent_pid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml)
