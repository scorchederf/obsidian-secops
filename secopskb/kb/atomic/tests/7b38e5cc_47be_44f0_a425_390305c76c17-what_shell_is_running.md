---
atomic_guid: "7b38e5cc-47be-44f0-a425-390305c76c17"
title: "What shell is running"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "7b38e5cc-47be-44f0-a425-390305c76c17"
  - "What shell is running"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary will want to discover what shell is running so that they can tailor their attacks accordingly. The following commands will discover what shell is running.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
echo $0
if $(env |grep "SHELL" >/dev/null); then env |grep "SHELL"; fi
if $(printenv SHELL >/dev/null); then printenv SHELL; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
