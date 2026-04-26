---
atomic_guid: "b8a8bdb2-7eae-490d-8251-d5e0295b2362"
title: "Invoke HTML Application - Simulate Lateral Movement over UNC Path"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b8a8bdb2-7eae-490d-8251-d5e0295b2362"
  - "Invoke HTML Application - Simulate Lateral Movement over UNC Path"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke HTML Application - Simulate Lateral Movement over UNC Path

Executes an HTA Application with Simulate lateral movement over UNC Path.

## Metadata

- Atomic GUID: b8a8bdb2-7eae-490d-8251-d5e0295b2362
- Technique: T1218.005: Signed Binary Proxy Execution: Mshta
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1218.005/T1218.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Input Arguments

### mshta_file_path

- description: Location of mshta.exe
- type: string
- default: $env:windir\system32\mshta.exe

## Dependencies

The AtomicTestHarnesses module must be installed and Invoke-ATHHTMLApplication must be exported in the module.

### Prerequisite Check

```untitled
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Invoke-ATHHTMLApplication']) {exit 1} else {exit 0}
```

### Get Prerequisite

```untitled
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Invoke-ATHHTMLApplication -TemplatePE -AsLocalUNCPath -MSHTAFilePath #{mshta_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
