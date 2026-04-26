---
atomic_guid: "7cd7eaa3-9ccc-460d-96d2-c6fb13e6d58a"
title: "System Service Discovery - Windows Scheduled Tasks (schtasks)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "7cd7eaa3-9ccc-460d-96d2-c6fb13e6d58a"
  - "System Service Discovery - Windows Scheduled Tasks (schtasks)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Service Discovery - Windows Scheduled Tasks (schtasks)

Enumerates scheduled tasks on Windows using schtasks.exe.

## Metadata

- Atomic GUID: 7cd7eaa3-9ccc-460d-96d2-c6fb13e6d58a
- Technique: T1007: System Service Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1007/T1007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Executor

- name: command_prompt

### Command

```commandprompt
schtasks /query /fo LIST /v
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
