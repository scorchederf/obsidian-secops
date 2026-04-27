---
atomic_guid: "7413be50-be8e-430f-ad4d-07bf197884b2"
title: "Wmic Group Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "7413be50-be8e-430f-ad4d-07bf197884b2"
  - "Wmic Group Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilizing wmic.exe to enumerate groups on the local system. Upon execution, information will be displayed of local groups on system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]

## Executor

- name: command_prompt

### Command

```cmd
wmic group get name
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
