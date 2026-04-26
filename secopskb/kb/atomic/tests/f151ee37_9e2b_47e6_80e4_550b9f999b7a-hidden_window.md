---
atomic_guid: "f151ee37-9e2b-47e6-80e4-550b9f999b7a"
title: "Hidden Window"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.003"
attack_technique_name: "Hide Artifacts: Hidden Window"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml"
build_date: "2026-04-26 14:38:40"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hidden Window

Launch PowerShell with the "-WindowStyle Hidden" argument to conceal PowerShell windows by setting the WindowStyle parameter to hidden.
Upon execution a hidden PowerShell window will launch calc.exe

## Metadata

- Atomic GUID: f151ee37-9e2b-47e6-80e4-550b9f999b7a
- Technique: T1564.003: Hide Artifacts: Hidden Window
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1564.003/T1564.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

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
