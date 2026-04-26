---
atomic_guid: "718aebaa-d0e0-471a-8241-c5afa69c7414"
title: "WMI Reconnaissance Software"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "718aebaa-d0e0-471a-8241-c5afa69c7414"
  - "WMI Reconnaissance Software"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WMI Reconnaissance Software

An adversary might use WMI to list installed Software hotfix and patches.
When the test completes, there should be a list of installed patches and when they were installed.

## Metadata

- Atomic GUID: 718aebaa-d0e0-471a-8241-c5afa69c7414
- Technique: T1047: Windows Management Instrumentation
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1047/T1047.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Executor

- name: command_prompt

### Command

```cmd
wmic qfe get description,installedOn /format:csv
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
