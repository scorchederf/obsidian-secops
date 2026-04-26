---
atomic_guid: "85321a9c-897f-4a60-9f20-29788e50bccd"
title: "Remote System Discovery - net"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "85321a9c-897f-4a60-9f20-29788e50bccd"
  - "Remote System Discovery - net"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote System Discovery - net

Identify remote systems with net.exe.

Upon successful execution, cmd.exe will execute `net.exe view` and display results of local systems on the network that have file and print sharing enabled.

## Metadata

- Atomic GUID: 85321a9c-897f-4a60-9f20-29788e50bccd
- Technique: T1018: Remote System Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Executor

- name: command_prompt

### Command

```cmd
net view /domain
net view
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
