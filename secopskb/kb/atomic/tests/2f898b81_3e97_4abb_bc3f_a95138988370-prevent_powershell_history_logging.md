---
atomic_guid: "2f898b81-3e97-4abb-bc3f-a95138988370"
title: "Prevent Powershell History Logging"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "2f898b81-3e97-4abb-bc3f-a95138988370"
  - "Prevent Powershell History Logging"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Prevents Powershell history

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]

## Executor

- name: powershell

### Command

```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
```

### Cleanup

```powershell
Set-PSReadLineOption -HistorySaveStyle SaveIncrementally
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
