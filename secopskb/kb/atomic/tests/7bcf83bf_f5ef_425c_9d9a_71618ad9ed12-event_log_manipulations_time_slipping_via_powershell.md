---
atomic_guid: "7bcf83bf-f5ef-425c-9d9a-71618ad9ed12"
title: "Event Log Manipulations- Time slipping via Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7bcf83bf-f5ef-425c-9d9a-71618ad9ed12"
  - "Event Log Manipulations- Time slipping via Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Event Log Manipulations- Time slipping via Powershell

Changes the system time on the computer to a time that you specify. It involves altering the system’s clock or adjusting the dates of files, affecting timestamp integrity within Event Logs. This technique can disrupt the sequence of logged events, complicating incident analysis and forensics. 
Reference - 
https://detect.fyi/event-log-manipulations-1-time-slipping-55bf95631c40
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/set-date?view=powershell-7.4

## Metadata

- Atomic GUID: 7bcf83bf-f5ef-425c-9d9a-71618ad9ed12
- Technique: T1070.006: Indicator Removal on Host: Timestomp
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1070.006/T1070.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Input Arguments

### days_to_modify

- description: Value to which system time will update
- type: string
- default: 3

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
try{ 
  Set-Date -Date (Get-Date).AddDays(#{days_to_modify})
  Add-Content "$env:APPDATA\slipDays.bak" #{days_to_modify}
}
catch {exit 1}
```

### Cleanup

```powershell
if(Test-Path "$env:APPDATA\slipDays.bak" ){
  foreach($line in (get-content $env:APPDATA\slipDays.bak)){
    Set-Date -Date (Get-Date).AddDays(-$line)
  }
  rm "$env:APPDATA\slipDays.bak"
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
