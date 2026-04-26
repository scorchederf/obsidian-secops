---
atomic_guid: "85cfbf23-4a1e-4342-8792-007e004b975f"
title: "Hostname Discovery (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "85cfbf23-4a1e-4342-8792-007e004b975f"
  - "Hostname Discovery (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hostname Discovery (Windows)

Identify system hostname for Windows. Upon execution, the hostname of the device will be displayed.

## Metadata

- Atomic GUID: 85cfbf23-4a1e-4342-8792-007e004b975f
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
hostname
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
