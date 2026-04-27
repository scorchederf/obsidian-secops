---
atomic_guid: "f151ee37-9e2b-47e6-80e4-550b9f999b7a"
title: "Hidden Window"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.003"
attack_technique_name: "Hide Artifacts: Hidden Window"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "f151ee37-9e2b-47e6-80e4-550b9f999b7a"
  - "Hidden Window"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Launch PowerShell with the "-WindowStyle Hidden" argument to conceal PowerShell windows by setting the WindowStyle parameter to hidden.
Upon execution a hidden PowerShell window will launch calc.exe

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]

## Input Arguments

### powershell_command

- description: Command to launch calc.exe from a hidden PowerShell Window
- type: string
- default: powershell.exe -WindowStyle hidden calc.exe

## Executor

- name: powershell

### Command

```powershell
Start-Process #{powershell_command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml)
