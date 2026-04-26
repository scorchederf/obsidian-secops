---
atomic_guid: "7413be50-be8e-430f-ad4d-07bf197884b2"
title: "Wmic Group Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-26 17:02:12"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Wmic Group Discovery

Utilizing wmic.exe to enumerate groups on the local system. Upon execution, information will be displayed of local groups on system.

## Metadata

- Atomic GUID: 7413be50-be8e-430f-ad4d-07bf197884b2
- Technique: T1069.001: Permission Groups Discovery: Local Groups
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1069.001/T1069.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Executor

- name: command_prompt

### Command

```cmd
wmic group get name
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
