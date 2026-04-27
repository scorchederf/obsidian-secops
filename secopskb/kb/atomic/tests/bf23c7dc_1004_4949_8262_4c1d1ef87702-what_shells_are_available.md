---
atomic_guid: "bf23c7dc-1004-4949-8262-4c1d1ef87702"
title: "What shells are available"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "bf23c7dc-1004-4949-8262-4c1d1ef87702"
  - "What shells are available"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may want to discover which shell's are available so that they might switch to that shell to tailor their attacks to suit that shell. The following commands will discover what shells are available on the host.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
cat /etc/shells
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
