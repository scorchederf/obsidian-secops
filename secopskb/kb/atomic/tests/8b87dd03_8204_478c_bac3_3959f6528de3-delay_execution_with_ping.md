---
atomic_guid: "8b87dd03-8204-478c-bac3-3959f6528de3"
title: "Delay execution with ping"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.003"
attack_technique_name: "Time Based Evasion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.003/T1497.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "8b87dd03-8204-478c-bac3-3959f6528de3"
  - "Delay execution with ping"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delay execution with ping

Uses the ping command to introduce a delay before executing a malicious payload.

## Metadata

- Atomic GUID: 8b87dd03-8204-478c-bac3-3959f6528de3
- Technique: T1497.003: Time Based Evasion
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1497.003/T1497.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.003]]

## Input Arguments

### evil_command

- description: Command to run after the delay
- type: string
- default: whoami

### ping_count

- description: Number of ping requests to send (higher counts increase the delay)
- type: integer
- default: 250

## Executor

- name: sh

### Command

```bash
ping -c #{ping_count} 8.8.8.8 > /dev/null
#{evil_command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.003/T1497.003.yaml)
