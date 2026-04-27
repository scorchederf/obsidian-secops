---
atomic_guid: "2db7852e-5a32-4ec7-937f-f4e027881700"
title: "Load custom DLL on mstsc execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "2db7852e-5a32-4ec7-937f-f4e027881700"
  - "Load custom DLL on mstsc execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adding ClxDllPath under Terminal Server Client subkey of HKLM hive with a path to custom DLL allows for DLL loading during execution of mstsc.exe

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]

## Input Arguments

### dll_inf

- description: custom DLL to be executed
- type: Path
- default: C:\Windows\System32\amsi.dll

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Terminal Server Client" /v ClxDllPath /t REG_SZ /d "#{dll_inf}" /f
```

### Cleanup

```cmd
reg delete "HKLM\SOFTWARE\Microsoft\Terminal Server Client" /v ClxDllPath /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
