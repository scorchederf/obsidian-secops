---
atomic_guid: "be3b5fe3-a575-4fb8-83f6-ad4a68dd5ce7"
title: "Discover OS Product Name via Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "be3b5fe3-a575-4fb8-83f6-ad4a68dd5ce7"
  - "Discover OS Product Name via Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Discover OS Product Name via Registry

Identify the Operating System Product Name via registry with the reg.exe command.
Upon execution, the OS Product Name will be displayed.

## Metadata

- Atomic GUID: be3b5fe3-a575-4fb8-83f6-ad4a68dd5ce7
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
