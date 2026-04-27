---
atomic_guid: "b26a3340-dad7-4360-9176-706269c74103"
title: "Disable Event Logging with wevtutil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "b26a3340-dad7-4360-9176-706269c74103"
  - "Disable Event Logging with wevtutil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Wevtutil can be used to disable logs. 
NOTE: RansomEXX ransomware uses this to disable Security logs post-encryption.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Input Arguments

### log_name

- description: Name of the log to be disabled
- type: string
- default: Microsoft-Windows-IKE/Operational

## Executor

- name: command_prompt

### Command

```cmd
wevtutil sl "#{log_name}" /e:false
```

### Cleanup

```cmd
wevtutil sl "#{log_name}" /e:true
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
