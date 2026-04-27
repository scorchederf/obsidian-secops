---
atomic_guid: "d6dc21af-bec9-4152-be86-326b6babd416"
title: "Execute Commands from Clipboard using PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1115"
attack_technique_name: "Clipboard Data"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "d6dc21af-bec9-4152-be86-326b6babd416"
  - "Execute Commands from Clipboard using PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize PowerShell to echo a command to clipboard and execute it

## ATT&CK Mapping

- [[kb/attack/techniques/T1115-clipboard_data|T1115: Clipboard Data]]

## Executor

- name: powershell

### Command

```powershell
echo Get-Process | clip
Get-Clipboard | iex
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml)
