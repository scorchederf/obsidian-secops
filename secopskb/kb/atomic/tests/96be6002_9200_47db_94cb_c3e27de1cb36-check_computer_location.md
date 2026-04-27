---
atomic_guid: "96be6002-9200-47db-94cb-c3e27de1cb36"
title: "Check computer location"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "96be6002-9200-47db-94cb-c3e27de1cb36"
  - "Check computer location"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Check computer location

Looks up country code configured in the registry, likely geofence. Upon execution, country code info will be displayed.
- https://tria.ge/210111-eaz8mqhgh6/behavioral1

## Metadata

- Atomic GUID: 96be6002-9200-47db-94cb-c3e27de1cb36
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: command_prompt

### Command

```cmd
reg query "HKEY_CURRENT_USER\Control Panel\International\Geo"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
