---
atomic_guid: "89676ba1-b1f8-47ee-b940-2e1a113ebc71"
title: "System Service Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "89676ba1-b1f8-47ee-b940-2e1a113ebc71"
  - "System Service Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# System Service Discovery

Identify system services.

Upon successful execution, cmd.exe will execute service commands with expected result to stdout.

## Metadata

- Atomic GUID: 89676ba1-b1f8-47ee-b940-2e1a113ebc71
- Technique: T1007: System Service Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1007/T1007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
tasklist.exe /svc
sc query
sc query state= all
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
