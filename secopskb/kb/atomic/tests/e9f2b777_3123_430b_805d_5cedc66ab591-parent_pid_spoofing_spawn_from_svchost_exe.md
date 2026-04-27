---
atomic_guid: "e9f2b777-3123-430b-805d-5cedc66ab591"
title: "Parent PID Spoofing - Spawn from svchost.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.004"
attack_technique_name: "Access Token Manipulation: Parent PID Spoofing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "e9f2b777-3123-430b-805d-5cedc66ab591"
  - "Parent PID Spoofing - Spawn from svchost.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Spawnd a process as a child of the first accessible svchost.exe process.

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134004-parent-pid-spoofing|T1134.004: Parent PID Spoofing]]

## Input Arguments

### command_line

- description: Specified command line to use
- type: string
- default: -Command Start-Sleep 10

### file_path

- description: File path or name of process to spawn
- type: path
- default: $Env:windir\System32\WindowsPowerShell\v1.0\powershell.exe

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
Get-CimInstance -ClassName Win32_Process -Property Name, CommandLine, ProcessId -Filter "Name = 'svchost.exe' AND CommandLine LIKE '%'" | Select-Object -First 1 | Start-ATHProcessUnderSpecificParent -FilePath #{file_path} -CommandLine '#{command_line}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml)
