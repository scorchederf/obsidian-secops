---
atomic_guid: "686a9785-f99b-41d4-90df-66ed515f81d7"
title: "ATHPowerShellCommandLineParameter -Command parameter variations"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "686a9785-f99b-41d4-90df-66ed515f81d7"
  - "ATHPowerShellCommandLineParameter -Command parameter variations"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ATHPowerShellCommandLineParameter -Command parameter variations

Executes powershell.exe with variations of the -Command parameter

## Metadata

- Atomic GUID: 686a9785-f99b-41d4-90df-66ed515f81d7
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Input Arguments

### command_line_switch_type

- description: The type of supported command-line switch to use
- type: string
- default: Hyphen

### command_param_variation

- description: The "Command" parameter variation to use
- type: string
- default: C

## Dependencies

The AtomicTestHarnesses module must be installed and Out-ATHPowerShellCommandLineParameter must be exported in the module.

### Prerequisite Check

```text
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Out-ATHPowerShellCommandLineParameter']) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Out-ATHPowerShellCommandLineParameter -CommandLineSwitchType #{command_line_switch_type} -CommandParamVariation #{command_param_variation} -Execute -ErrorAction Stop
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
