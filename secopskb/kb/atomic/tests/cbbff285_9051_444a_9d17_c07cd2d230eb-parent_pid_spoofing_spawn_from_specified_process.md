---
atomic_guid: "cbbff285-9051-444a-9d17-c07cd2d230eb"
title: "Parent PID Spoofing - Spawn from Specified Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.004"
attack_technique_name: "Access Token Manipulation: Parent PID Spoofing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "cbbff285-9051-444a-9d17-c07cd2d230eb"
  - "Parent PID Spoofing - Spawn from Specified Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Parent PID Spoofing - Spawn from Specified Process

Spawns a notepad.exe process as a child of the current process.

## Metadata

- Atomic GUID: cbbff285-9051-444a-9d17-c07cd2d230eb
- Technique: T1134.004: Access Token Manipulation: Parent PID Spoofing
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1134.004/T1134.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.004]]

## Input Arguments

### parent_pid

- description: PID of process to spawn from
- type: string
- default: $PID

### test_guid

- description: Defined test GUID
- type: string
- default: 12345678-1234-1234-1234-123456789123

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
Start-ATHProcessUnderSpecificParent  -ParentId #{parent_pid} -TestGuid #{test_guid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml)
