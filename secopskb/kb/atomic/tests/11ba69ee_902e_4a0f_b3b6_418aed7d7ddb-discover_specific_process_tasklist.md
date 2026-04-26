---
atomic_guid: "11ba69ee-902e-4a0f-b3b6-418aed7d7ddb"
title: "Discover Specific Process - tasklist"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "11ba69ee-902e-4a0f-b3b6-418aed7d7ddb"
  - "Discover Specific Process - tasklist"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Discover Specific Process - tasklist

Adversaries may use command line tools to discover specific processes in preparation of further attacks. 
Examples of this could be discovering the PID of lsass.exe to dump its memory or discovering whether specific security processes (e.g. AV or EDR) are running.

## Metadata

- Atomic GUID: 11ba69ee-902e-4a0f-b3b6-418aed7d7ddb
- Technique: T1057: Process Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1057/T1057.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Input Arguments

### process_to_enumerate

- description: Process name string to search for.
- type: string
- default: lsass

## Executor

- name: command_prompt

### Command

```commandprompt
tasklist | findstr #{process_to_enumerate}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
