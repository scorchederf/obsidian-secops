---
atomic_guid: "17d1a3cc-3373-495a-857a-e5dd005fb302"
title: "Adding custom debugger for Windows Error Reporting"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "17d1a3cc-3373-495a-857a-e5dd005fb302"
  - "Adding custom debugger for Windows Error Reporting"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Adding custom debugger for Windows Error Reporting

When applications hang, the Windows Error Reporting framework allows us to attach a debugger, if it is set up in the Registry.
Adding executable of choice will let the executable to auto-execute when during any application crash due to functioning of WER framework

## Metadata

- Atomic GUID: 17d1a3cc-3373-495a-857a-e5dd005fb302
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
reg add "HKLM\Software\Microsoft\Windows\Windows Error Reporting\Hangs" /v Debugger /t REG_SZ /d "C:\Windows\System32\notepad.exe" /f
```

### Cleanup

```cmd
reg delete "HKLM\Software\Microsoft\Windows\Windows Error Reporting\Hangs" /v Debugger /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
