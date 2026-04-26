---
atomic_guid: "b4094750-5fc7-4e8e-af12-b4e36bf5e7f6"
title: "Invoke CHM with InfoTech Storage Protocol Handler"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.001"
attack_technique_name: "Signed Binary Proxy Execution: Compiled HTML File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "b4094750-5fc7-4e8e-af12-b4e36bf5e7f6"
  - "Invoke CHM with InfoTech Storage Protocol Handler"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke CHM with InfoTech Storage Protocol Handler

Executes a CHM file with the ITS protocol handler.

## Metadata

- Atomic GUID: b4094750-5fc7-4e8e-af12-b4e36bf5e7f6
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

### hh_file_path

- description: path of modified HH.exe
- type: path
- default: $env:windir\hh.exe

### infotech_storage_handler

- description: Default InfoTech Storage Protocol Handler
- type: string
- default: its

## Dependencies

The AtomicTestHarnesses module must be installed and Invoke-ATHCompiledHelp must be exported in the module.

### Prerequisite Check

```text
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Invoke-ATHCompiledHelp']) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Invoke-ATHCompiledHelp -InfoTechStorageHandler #{infotech_storage_handler} -HHFilePath #{hh_file_path} -CHMFilePath #{chm_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml)
