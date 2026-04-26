---
atomic_guid: "4469192c-2d2d-4a3a-9758-1f31d937a92b"
title: "Abusing Windows TelemetryController Registry Key for Persistence"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "4469192c-2d2d-4a3a-9758-1f31d937a92b"
  - "Abusing Windows TelemetryController Registry Key for Persistence"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Abusing Windows TelemetryController Registry Key for Persistence

The Windows Compatibility Telemetry system makes use of the CompatTelRunner.exe binary to run a variety of telemetry tasks. It relies on the registry for instructions on which commands to run. 
It will run any arbitrary command without restriction of location or type. Blog :https://www.trustedsec.com/blog/abusing-windows-telemetry-for-persistence

## Metadata

- Atomic GUID: 4469192c-2d2d-4a3a-9758-1f31d937a92b
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### new_executable

- description: Custom Executable to run
- type: string
- default: C:\Windows\System32\notepad.exe

### new_key

- description: New Registry Key Added
- type: string
- default: NewKey

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\TelemetryController\#{new_key}" /t REG_SZ /v Command /d #{new_executable} /f
```

### Cleanup

```commandprompt
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\TelemetryController\#{new_key}" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
