---
atomic_guid: "51f17016-d8fa-4360-888a-df4bf92c4a04"
title: "Get-Service Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "51f17016-d8fa-4360-888a-df4bf92c4a04"
  - "Get-Service Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Get-Service Execution

Executes the Get-Service cmdlet to gather objects representing all services on the local system.

## Metadata

- Atomic GUID: 51f17016-d8fa-4360-888a-df4bf92c4a04
- Technique: T1007: System Service Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1007/T1007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Executor

- name: command_prompt

### Command

```cmd
powershell.exe Get-Service
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
