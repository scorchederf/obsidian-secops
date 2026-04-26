---
atomic_guid: "acfcd709-0013-4f1e-b9ee-bc1e7bafaaec"
title: "Discover OS Build Number via Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "acfcd709-0013-4f1e-b9ee-bc1e7bafaaec"
  - "Discover OS Build Number via Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Discover OS Build Number via Registry

Identify the Operating System Build Number via registry with the reg.exe command.
Upon execution, the OS Build Number will be displayed.

## Metadata

- Atomic GUID: acfcd709-0013-4f1e-b9ee-bc1e7bafaaec
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

```commandprompt
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v CurrentBuildNumber
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
