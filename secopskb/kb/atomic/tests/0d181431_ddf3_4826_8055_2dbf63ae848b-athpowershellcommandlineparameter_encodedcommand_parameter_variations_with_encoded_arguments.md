---
atomic_guid: "0d181431-ddf3-4826-8055-2dbf63ae848b"
title: "ATHPowerShellCommandLineParameter -EncodedCommand parameter variations with encoded arguments"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0d181431-ddf3-4826-8055-2dbf63ae848b"
  - "ATHPowerShellCommandLineParameter -EncodedCommand parameter variations with encoded arguments"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ATHPowerShellCommandLineParameter -EncodedCommand parameter variations with encoded arguments

Executes powershell.exe with variations of the -EncodedCommand parameter with encoded arguments supplied

## Metadata

- Atomic GUID: 0d181431-ddf3-4826-8055-2dbf63ae848b
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

### encoded_arguments_param_variation

- description: The "EncodedArguments" parameter variation to use
- type: string
- default: EncodedArguments

### encoded_command_param_variation

- description: The "EncodedCommand" parameter variation to use
- type: string
- default: E

## Dependencies

The AtomicTestHarnesses module must be installed and Out-ATHPowerShellCommandLineParameter must be exported in the module.

### Prerequisite Check

```untitled
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Out-ATHPowerShellCommandLineParameter']) {exit 1} else {exit 0}
```

### Get Prerequisite

```untitled
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Out-ATHPowerShellCommandLineParameter -CommandLineSwitchType #{command_line_switch_type} -EncodedCommandParamVariation #{encoded_command_param_variation} -UseEncodedArguments -EncodedArgumentsParamVariation #{encoded_arguments_param_variation} -Execute -ErrorAction Stop
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
