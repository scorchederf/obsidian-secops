---
atomic_guid: "970ab6a1-0157-4f3f-9a73-ec4166754b23"
title: "System Network Configuration Discovery on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "970ab6a1-0157-4f3f-9a73-ec4166754b23"
  - "System Network Configuration Discovery on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Network Configuration Discovery on Windows

Identify network configuration information

Upon successful execution, cmd.exe will spawn multiple commands to list network configuration settings. Output will be via stdout.

## Metadata

- Atomic GUID: 970ab6a1-0157-4f3f-9a73-ec4166754b23
- Technique: T1016: System Network Configuration Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Executor

- name: command_prompt

### Command

```cmd
ipconfig /all
netsh interface show interface
arp -a
nbtstat -n
net config
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
