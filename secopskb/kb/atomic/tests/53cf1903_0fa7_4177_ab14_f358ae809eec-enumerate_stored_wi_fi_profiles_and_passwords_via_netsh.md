---
atomic_guid: "53cf1903-0fa7-4177-ab14-f358ae809eec"
title: "Enumerate Stored Wi-Fi Profiles And Passwords via netsh"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016.002"
attack_technique_name: "System Network Configuration Discovery: Wi-Fi Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.002/T1016.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "53cf1903-0fa7-4177-ab14-f358ae809eec"
  - "Enumerate Stored Wi-Fi Profiles And Passwords via netsh"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Stored Wi-Fi Profiles And Passwords via netsh

Upon successful execution, information about previously connected Wi-Fi networks will be displayed with their corresponding key (if present).

## Metadata

- Atomic GUID: 53cf1903-0fa7-4177-ab14-f358ae809eec
- Technique: T1016.002: System Network Configuration Discovery: Wi-Fi Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1016.002/T1016.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016.002]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
netsh wlan show profile * key=clear
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.002/T1016.002.yaml)
