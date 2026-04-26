---
atomic_guid: "b13e9306-3351-4b4b-a6e8-477358b0b498"
title: "Delete System Logs Using Clear-EventLog"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.001"
attack_technique_name: "Indicator Removal on Host: Clear Windows Event Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b13e9306-3351-4b4b-a6e8-477358b0b498"
  - "Delete System Logs Using Clear-EventLog"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete System Logs Using Clear-EventLog

Clear event logs using built-in PowerShell commands.
Upon successful execution, you should see the list of deleted event logs
Upon execution, open the Security.evtx logs at C:\Windows\System32\winevt\Logs and verify that it is now empty or has very few logs in it.

## Metadata

- Atomic GUID: b13e9306-3351-4b4b-a6e8-477358b0b498
- Technique: T1070.001: Indicator Removal on Host: Clear Windows Event Logs
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1070.001/T1070.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$logs = Get-EventLog -List | ForEach-Object {$_.Log}
$logs | ForEach-Object {Clear-EventLog -LogName $_ }
Get-EventLog -list
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml)
