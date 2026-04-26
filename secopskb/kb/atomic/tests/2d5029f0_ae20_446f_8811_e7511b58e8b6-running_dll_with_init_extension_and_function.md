---
atomic_guid: "2d5029f0-ae20-446f-8811-e7511b58e8b6"
title: "Running DLL with .init extension and function"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "2d5029f0-ae20-446f-8811-e7511b58e8b6"
  - "Running DLL with .init extension and function"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Running DLL with .init extension and function

This test, based on common Gamarue tradecraft, consists of a DLL file with a .init extension being run by rundll32.exe. When this DLL file's 'krnl' function is called, it launches a Windows pop-up.
DLL created with the AtomicTestHarnesses Portable Executable Builder script.

## Metadata

- Atomic GUID: 2d5029f0-ae20-446f-8811-e7511b58e8b6
- Technique: T1218.011: Signed Binary Proxy Execution: Rundll32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.011/T1218.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Input Arguments

### dll_file

- description: The DLL file to be called
- type: string
- default: PathToAtomicsFolder\T1218.011\bin\_WT.init

### dll_url

- description: The URL to the DLL file that must be downloaded
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.011/bin/_WT.init

## Dependencies

The DLL file to be called must exist at the specified location (#{dll_file})

### Prerequisite Check

```text
if (Test-Path "#{dll_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{dll_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "#{dll_url}" -OutFile "#{dll_file}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
rundll32.exe #{dll_file},krnl
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
