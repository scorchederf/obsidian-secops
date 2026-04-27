---
atomic_guid: "ee72b37d-b8f5-46a5-a9e7-0ff50035ffd5"
title: "Shell Creation using awk command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "ee72b37d-b8f5-46a5-a9e7-0ff50035ffd5"
  - "Shell Creation using awk command"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

In awk the begin rule runs the first record without reading or interpreting it. This way a shell can be created and used to break out from restricted environments with the awk command.
Reference - https://gtfobins.github.io/gtfobins/awk/#shell

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Executor

- name: sh

### Command

```bash
awk 'BEGIN {system("/bin/sh &")}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
