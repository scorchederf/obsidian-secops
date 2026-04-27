---
atomic_guid: "e184b6bd-fb28-48aa-9a59-13012e33d7dc"
title: "Check internet connection using ping Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016.001"
attack_technique_name: "System Network Configuration Discovery: Internet Connection Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml"
build_date: "2026-04-27 19:12:25"
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

Check internet connection using ping on Windows. The default target of the ping is 8.8.8.8 (Google Public DNS).

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery#^t1016001-internet-connection-discovery|T1016.001: Internet Connection Discovery]]

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
