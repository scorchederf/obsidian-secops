---
atomic_guid: "22c779cd-9445-4d3e-a136-f75adbf0315f"
title: "Clear PowerShell Session History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This technique involves using the Clear-History cmdlet in PowerShell to remove all records of previously executed commands.
This action is often performed by attackers to eliminate traces of their activities, making incident detection and forensic 
investigation more challenging. By clearing the session history, adversaries aim to obfuscate their operational footprint.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Clear-History
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
