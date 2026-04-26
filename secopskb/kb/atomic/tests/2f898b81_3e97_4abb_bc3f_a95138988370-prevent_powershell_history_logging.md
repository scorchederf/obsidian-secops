---
atomic_guid: "2f898b81-3e97-4abb-bc3f-a95138988370"
title: "Prevent Powershell History Logging"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 14:38:39"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Prevent Powershell History Logging

Prevents Powershell history

## Metadata

- Atomic GUID: 2f898b81-3e97-4abb-bc3f-a95138988370
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

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
