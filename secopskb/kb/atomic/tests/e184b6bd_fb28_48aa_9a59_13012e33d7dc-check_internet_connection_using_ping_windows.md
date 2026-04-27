---
atomic_guid: "e184b6bd-fb28-48aa-9a59-13012e33d7dc"
title: "Check internet connection using ping Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016.001"
attack_technique_name: "System Network Configuration Discovery: Internet Connection Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "e184b6bd-fb28-48aa-9a59-13012e33d7dc"
  - "Check internet connection using ping Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Check internet connection using ping Windows

Check internet connection using ping on Windows. The default target of the ping is 8.8.8.8 (Google Public DNS).

## Metadata

- Atomic GUID: e184b6bd-fb28-48aa-9a59-13012e33d7dc
- Technique: T1016.001: System Network Configuration Discovery: Internet Connection Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1016.001/T1016.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016.001]]

## Input Arguments

### ping_target

- description: target of the ping
- type: url
- default: 8.8.8.8

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
ping -n 4 #{ping_target}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml)
