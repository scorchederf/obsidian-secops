---
atomic_guid: "53ead5db-7098-4111-bb3f-563be390e72e"
title: "System Time with Windows time Command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1124"
attack_technique_name: "System Time Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "53ead5db-7098-4111-bb3f-563be390e72e"
  - "System Time with Windows time Command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# System Time with Windows time Command

Displays the current system time via the Windows builtin time command: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/time
Recently observed in use in the wild during an incident involving Ursnif malware:
https://github.com/The-DFIR-Report/Sigma-Rules/blob/dc72f0b557fc63347379be0a33439788256761c8/rules/windows/process_creation/proc_creation_win_system_time_lookup.yml
https://thedfirreport.com/2023/01/09/unwrapping-ursnifs-gifts/

## Metadata

- Atomic GUID: 53ead5db-7098-4111-bb3f-563be390e72e
- Technique: T1124: System Time Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1124/T1124.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1124-system_time_discovery|T1124]]

## Executor

- name: command_prompt

### Command

```cmd
time
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml)
