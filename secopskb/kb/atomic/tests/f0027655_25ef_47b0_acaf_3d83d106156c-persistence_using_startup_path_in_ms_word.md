---
atomic_guid: "f0027655-25ef-47b0-acaf-3d83d106156c"
title: "Persistence using STARTUP-PATH in MS-WORD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "f0027655-25ef-47b0-acaf-3d83d106156c"
  - "Persistence using STARTUP-PATH in MS-WORD"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Persistence using STARTUP-PATH in MS-WORD

When Word starts, it searches for the registry key HKCU\Software\Microsoft\Office\<version>\Word\Options\STARTUP-PATH and if it exists,
it will treat it as a user specific start-up folder and load the contents of the folder with file extensions of .wll,.lnk,.dotm,.dot,.dotx
The registry key can be abused to load malware from the mentioned path. Reboot might be required.

## Metadata

- Atomic GUID: f0027655-25ef-47b0-acaf-3d83d106156c
- Technique: T1546: Event Triggered Execution
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1546/T1546.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKCU\Software\Microsoft\Office\16.0\Word\Options" /v STARTUP-PATH /t REG_SZ /d "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent" /f
```

### Cleanup

```cmd
reg delete HKCU\Software\Microsoft\Office\16.0\Word\Options /v STARTUP-PATH /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
