---
atomic_guid: "ab4d04af-68dc-4fee-9c16-6545265b3276"
title: "Shell Creation using busybox command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "ab4d04af-68dc-4fee-9c16-6545265b3276"
  - "Shell Creation using busybox command"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Shell Creation using busybox command

BusyBox is a multi-call binary. A multi-call binary is an executable program that performs the same job as more than one utility program. It can be used to break out from restricted environments by spawning an interactive system shell. 
Reference - https://gtfobins.github.io/gtfobins/busybox/

## Metadata

- Atomic GUID: ab4d04af-68dc-4fee-9c16-6545265b3276
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
busybox sh &
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
