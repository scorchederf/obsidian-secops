---
atomic_guid: "99be2089-c52d-4a4a-b5c3-261ee42c8b62"
title: "Execution through API - CreateProcess"
framework: "atomic"
generated: "true"
attack_technique_id: "T1106"
attack_technique_name: "Native API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "99be2089-c52d-4a4a-b5c3-261ee42c8b62"
  - "Execution through API - CreateProcess"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execution through API - CreateProcess

Execute program by leveraging Win32 API's. By default, this will launch calc.exe from the command prompt.

## Metadata

- Atomic GUID: 99be2089-c52d-4a4a-b5c3-261ee42c8b62
- Technique: T1106: Native API
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1106/T1106.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1106-native_api|T1106]]

## Input Arguments

### output_file

- description: Location of the payload
- type: path
- default: %tmp%\T1106.exe

### source_file

- description: Location of the CSharp source file to compile and execute
- type: path
- default: PathToAtomicsFolder\T1106\src\CreateProcess.cs

## Dependencies

#{source_file} must exist on system.

### Prerequisite Check

```powershell
if (Test-Path "#{source_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{source_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1106/src/CreateProcess.cs" -OutFile "#{source_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /out:"#{output_file}" /target:exe "#{source_file}"
%tmp%/T1106.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml)
