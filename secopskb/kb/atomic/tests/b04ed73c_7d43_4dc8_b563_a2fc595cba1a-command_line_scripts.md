---
atomic_guid: "b04ed73c-7d43-4dc8-b563-a2fc595cba1a"
title: "Command line scripts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "b04ed73c-7d43-4dc8-b563-a2fc595cba1a"
  - "Command line scripts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Command line scripts

An adversary may type in elaborate multi-line shell commands into a terminal session because they can't or don't wish to create script files on the host. The following command is a simple loop, echoing out Atomic Red Team was here!

## Metadata

- Atomic GUID: b04ed73c-7d43-4dc8-b563-a2fc595cba1a
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- name: sh

### Command

```bash
for i in $(seq 1 5); do echo "$i, Atomic Red Team was here!"; sleep 1; done
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
