---
atomic_guid: "007e5672-2088-4853-a562-7490ddc19447"
title: "Invoke HTML Application - Jscript Engine over Local UNC Simulating Lateral Movement"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "007e5672-2088-4853-a562-7490ddc19447"
  - "Invoke HTML Application - Jscript Engine over Local UNC Simulating Lateral Movement"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes an HTA Application using JScript script engine using local UNC path simulating lateral movement.

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

## Input Arguments

### hta_file_path

- description: HTA file name and or path to be used
- type: string
- default: Test.hta

### mshta_file_path

- description: Location of mshta.exe
- type: string
- default: $env:windir\system32\mshta.exe

### script_engine

- description: Script Engine to use
- type: string
- default: JScript

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
Invoke-ATHHTMLApplication -HTAFilePath #{hta_file_path} -ScriptEngine #{script_engine} -AsLocalUNCPath -SimulateLateralMovement -MSHTAFilePath #{mshta_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
