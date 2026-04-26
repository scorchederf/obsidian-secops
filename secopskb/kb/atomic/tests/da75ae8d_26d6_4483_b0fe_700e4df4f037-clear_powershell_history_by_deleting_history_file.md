---
atomic_guid: "da75ae8d-26d6-4483-b0fe-700e4df4f037"
title: "Clear Powershell History by Deleting History File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "da75ae8d-26d6-4483-b0fe-700e4df4f037"
  - "Clear Powershell History by Deleting History File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear Powershell History by Deleting History File

Clears Powershell history

## Metadata

- Atomic GUID: da75ae8d-26d6-4483-b0fe-700e4df4f037
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
Remove-Item (Get-PSReadlineOption).HistorySavePath
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
