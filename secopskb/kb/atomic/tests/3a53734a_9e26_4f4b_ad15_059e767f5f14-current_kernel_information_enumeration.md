---
atomic_guid: "3a53734a-9e26-4f4b-ad15-059e767f5f14"
title: "Current kernel information enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "3a53734a-9e26-4f4b-ad15-059e767f5f14"
  - "Current kernel information enumeration"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may want to enumerate the kernel information to tailor their attacks for that particular kernel. The following command will enumerate the kernel information.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
uname -srm
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
