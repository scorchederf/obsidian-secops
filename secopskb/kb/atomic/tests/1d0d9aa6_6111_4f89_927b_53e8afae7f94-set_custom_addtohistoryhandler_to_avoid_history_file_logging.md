---
atomic_guid: "1d0d9aa6-6111-4f89-927b-53e8afae7f94"
title: "Set Custom AddToHistoryHandler to Avoid History File Logging"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "1d0d9aa6-6111-4f89-927b-53e8afae7f94"
  - "Set Custom AddToHistoryHandler to Avoid History File Logging"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The "AddToHistoryHandler" receives the current command as the $line variable and then returns $true if 
the line should be written to the history file. Here we simply return $false so nothing gets added to 
the history file for the current session.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]

## Executor

- name: powershell

### Command

```powershell
Set-PSReadLineOption -AddToHistoryHandler { return $false }
```

### Cleanup

```powershell
Set-PSReadLineOption -AddToHistoryHandler $null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
