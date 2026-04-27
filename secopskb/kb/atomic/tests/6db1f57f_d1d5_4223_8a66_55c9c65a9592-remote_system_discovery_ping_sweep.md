---
atomic_guid: "6db1f57f-d1d5-4223-8a66-55c9c65a9592"
title: "Remote System Discovery - ping sweep"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "6db1f57f-d1d5-4223-8a66-55c9c65a9592"
  - "Remote System Discovery - ping sweep"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote System Discovery - ping sweep

Identify remote systems via ping sweep.

Upon successful execution, cmd.exe will perform a for loop against the 192.168.1.1/24 network. Output will be via stdout.

## Metadata

- Atomic GUID: 6db1f57f-d1d5-4223-8a66-55c9c65a9592
- Technique: T1018: Remote System Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Input Arguments

### start_host

- description: Last octet starting value for ping sweep.
- type: string
- default: 1

### stop_host

- description: Last octet ending value for ping sweep.
- type: string
- default: 254

### subnet

- description: Subnet used for ping sweep.
- type: string
- default: 192.168.1

## Executor

- name: command_prompt

### Command

```cmd
for /l %i in (#{start_host},1,#{stop_host}) do ping -n 1 -w 100 #{subnet}.%i
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
