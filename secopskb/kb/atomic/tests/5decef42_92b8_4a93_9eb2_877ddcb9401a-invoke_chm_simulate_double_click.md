---
atomic_guid: "5decef42-92b8-4a93-9eb2-877ddcb9401a"
title: "Invoke CHM Simulate Double click"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.001"
attack_technique_name: "Signed Binary Proxy Execution: Compiled HTML File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "5decef42-92b8-4a93-9eb2-877ddcb9401a"
  - "Invoke CHM Simulate Double click"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke CHM Simulate Double click

Executes a CHM file simulating a user double click.

## Metadata

- Atomic GUID: 5decef42-92b8-4a93-9eb2-877ddcb9401a
- Technique: T1218.001: Signed Binary Proxy Execution: Compiled HTML File
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1218.001/T1218.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Input Arguments

### chm_file_path

- description: Default path of CHM
- type: string
- default: Test.chm

## Dependencies

The AtomicTestHarnesses module must be installed and Invoke-ATHCompiledHelp must be exported in the module.

### Prerequisite Check

```untitled
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Invoke-ATHCompiledHelp']) {exit 1} else {exit 0}
```

### Get Prerequisite

```untitled
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Invoke-ATHCompiledHelp -SimulateUserDoubleClick -CHMFilePath #{chm_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml)
