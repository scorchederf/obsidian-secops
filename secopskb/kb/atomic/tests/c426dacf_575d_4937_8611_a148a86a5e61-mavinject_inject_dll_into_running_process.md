---
atomic_guid: "c426dacf-575d-4937-8611-a148a86a5e61"
title: "mavinject - Inject DLL into running process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "c426dacf-575d-4937-8611-a148a86a5e61"
  - "mavinject - Inject DLL into running process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# mavinject - Inject DLL into running process

Injects arbitrary DLL into running process specified by process ID. Requires Windows 10.

## Metadata

- Atomic GUID: c426dacf-575d-4937-8611-a148a86a5e61
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Input Arguments

### dll_payload

- description: DLL to inject
- type: path
- default: PathToAtomicsFolder\T1218\src\x64\T1218.dll

### process_id

- description: PID of process receiving injection
- type: string
- default: 1000

## Dependencies

T1218.dll must exist on disk at specified location (#{dll_payload})

### Prerequisite Check

```text
if (Test-Path "#{dll_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{dll_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218/src/x64/T1218.dll" -OutFile "#{dll_payload}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
mavinject.exe #{process_id} /INJECTRUNNING "#{dll_payload}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
