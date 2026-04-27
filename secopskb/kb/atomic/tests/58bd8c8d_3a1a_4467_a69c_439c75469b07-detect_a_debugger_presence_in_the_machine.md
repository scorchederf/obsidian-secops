---
atomic_guid: "58bd8c8d-3a1a-4467-a69c-439c75469b07"
title: "Detect a Debugger Presence in the Machine"
framework: "atomic"
generated: "true"
attack_technique_id: "T1622"
attack_technique_name: "Debugger Evasion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1622/T1622.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "58bd8c8d-3a1a-4467-a69c-439c75469b07"
  - "Detect a Debugger Presence in the Machine"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detecting a running debugger process or if the debugger is attached to a process via PowerShell

## ATT&CK Mapping

- [[kb/attack/techniques/T1622-debugger_evasion|T1622: Debugger Evasion]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# Check for common debugger processes
$debuggerProcesses = Get-Process | Where-Object { $_.ProcessName -match "dbg" -or $_.ProcessName -match "debug" }
# Check for debugging flags
$debuggingFlags = [System.Diagnostics.Debugger]::IsAttached
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1622/T1622.yaml)
