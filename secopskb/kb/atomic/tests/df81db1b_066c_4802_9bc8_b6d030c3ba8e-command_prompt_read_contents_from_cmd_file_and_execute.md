---
atomic_guid: "df81db1b-066c-4802-9bc8-b6d030c3ba8e"
title: "Command Prompt read contents from CMD file and execute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.003"
attack_technique_name: "Command and Scripting Interpreter: Windows Command Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "df81db1b-066c-4802-9bc8-b6d030c3ba8e"
  - "Command Prompt read contents from CMD file and execute"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulate Raspberry Robin using the "standard-in" command prompt feature cmd `/R <` to read and execute a file via cmd.exe
See https://redcanary.com/blog/raspberry-robin/.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

## Input Arguments

### input_file

- description: CMD file that is read by Command Prompt and execute, which launches calc.exe
- type: path
- default: PathToAtomicsFolder\T1059.003\src\t1059.003_cmd.cmd

## Dependencies

CMD file must exist on disk at specified location (#{input_file})

### Prerequisite Check

```powershell
if (Test-Path "#{input_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{input_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1059.003/src/t1059.003_cmd.cmd" -OutFile "#{input_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
cmd /r cmd<"#{input_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml)
