---
atomic_guid: "25c5d1f1-a24b-494a-a6c5-5f50a1ae7f47"
title: "Discover System Time Zone via Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1124"
attack_technique_name: "System Time Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "25c5d1f1-a24b-494a-a6c5-5f50a1ae7f47"
  - "Discover System Time Zone via Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Discover System Time Zone via Registry

Identify the Operating System Time Zone via registry with the reg.exe command.
Upon execution, the system Time Zone will be shown.

## Metadata

- Atomic GUID: 25c5d1f1-a24b-494a-a6c5-5f50a1ae7f47
- Technique: T1124: System Time Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1124/T1124.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1124-system_time_discovery|T1124]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation" /v TimeZoneKeyName
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml)
