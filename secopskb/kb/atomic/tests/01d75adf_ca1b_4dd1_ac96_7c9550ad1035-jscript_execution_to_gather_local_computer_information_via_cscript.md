---
atomic_guid: "01d75adf-ca1b-4dd1-ac96-7c9550ad1035"
title: "JScript execution to gather local computer information via cscript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.007"
attack_technique_name: "Command and Scripting Interpreter: JavaScript"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.007/T1059.007.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "01d75adf-ca1b-4dd1-ac96-7c9550ad1035"
  - "JScript execution to gather local computer information via cscript"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# JScript execution to gather local computer information via cscript

JScript execution test, execute JScript via cscript command. When successful, system information will be written to $env:TEMP\T1059.007.out.txt

## Metadata

- Atomic GUID: 01d75adf-ca1b-4dd1-ac96-7c9550ad1035
- Technique: T1059.007: Command and Scripting Interpreter: JavaScript
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1059.007/T1059.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Input Arguments

### jscript

- description: Path to sample script
- type: string
- default: PathToAtomicsFolder\T1059.007\src\sys_info.js

## Dependencies

Sample script must exist on disk at specified location (#{jscript})

### Prerequisite Check

```text
if (Test-Path "#{jscript}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -ItemType Directory (Split-Path "#{jscript}") -Force | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.007/src/sys_info.js" -OutFile "#{jscript}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
cscript "#{jscript}" > %tmp%\T1059.007.out.txt
```

### Cleanup

```commandprompt
del %tmp%\T1059.007.out.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.007/T1059.007.yaml)
