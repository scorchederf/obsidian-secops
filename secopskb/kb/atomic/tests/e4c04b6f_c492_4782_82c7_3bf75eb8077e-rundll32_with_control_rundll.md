---
atomic_guid: "e4c04b6f-c492-4782-82c7-3bf75eb8077e"
title: "Rundll32 with Control_RunDLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "e4c04b6f-c492-4782-82c7-3bf75eb8077e"
  - "Rundll32 with Control_RunDLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Rundll32 with Control_RunDLL

Rundll32.exe loading dll with 'control_rundll' within the command-line, loading a .cpl or another file type related to CVE-2021-40444.

## Metadata

- Atomic GUID: e4c04b6f-c492-4782-82c7-3bf75eb8077e
- Technique: T1218.011: Signed Binary Proxy Execution: Rundll32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.011/T1218.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Input Arguments

### input_file

- description: DLL File
- type: string
- default: PathToAtomicsFolder\T1047\bin\calc.dll

### input_url

- description: Url to download the DLL
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1047/bin/calc.dll

## Dependencies

DLL file must exist on disk at specified location

### Prerequisite Check

```text
if (Test-Path "#{input_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest "#{input_url}" -OutFile "#{input_file}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
rundll32.exe shell32.dll,Control_RunDLL "#{input_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
