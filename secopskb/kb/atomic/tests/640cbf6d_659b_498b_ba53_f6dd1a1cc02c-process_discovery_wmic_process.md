---
atomic_guid: "640cbf6d-659b-498b-ba53-f6dd1a1cc02c"
title: "Process Discovery - wmic process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "640cbf6d-659b-498b-ba53-f6dd1a1cc02c"
  - "Process Discovery - wmic process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Discovery - wmic process

Utilize windows management instrumentation to identify processes.

Upon successful execution, WMIC will execute process to list processes. Output will be via stdout.

## Metadata

- Atomic GUID: 640cbf6d-659b-498b-ba53-f6dd1a1cc02c
- Technique: T1057: Process Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1057/T1057.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Executor

- name: command_prompt

### Command

```cmd
wmic process get /format:list
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
