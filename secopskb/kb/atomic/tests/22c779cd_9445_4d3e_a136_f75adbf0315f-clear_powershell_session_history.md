---
atomic_guid: "22c779cd-9445-4d3e-a136-f75adbf0315f"
title: "Clear PowerShell Session History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "22c779cd-9445-4d3e-a136-f75adbf0315f"
  - "Clear PowerShell Session History"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear PowerShell Session History

This technique involves using the Clear-History cmdlet in PowerShell to remove all records of previously executed commands.
This action is often performed by attackers to eliminate traces of their activities, making incident detection and forensic 
investigation more challenging. By clearing the session history, adversaries aim to obfuscate their operational footprint.

## Metadata

- Atomic GUID: 22c779cd-9445-4d3e-a136-f75adbf0315f
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Clear-History
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
