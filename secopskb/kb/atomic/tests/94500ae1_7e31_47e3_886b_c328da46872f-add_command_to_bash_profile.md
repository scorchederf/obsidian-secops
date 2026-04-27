---
atomic_guid: "94500ae1-7e31-47e3-886b-c328da46872f"
title: "Add command to .bash_profile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.004"
attack_technique_name: "Event Triggered Execution: .bash_profile .bashrc and .shrc"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "94500ae1-7e31-47e3-886b-c328da46872f"
  - "Add command to .bash_profile"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adds a command to the .bash_profile file of the current user

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]]

## Input Arguments

### command_to_add

- description: Command to add to the .bash_profile file
- type: string
- default: echo "Hello from Atomic Red Team T1546.004" > /tmp/T1546.004

## Executor

- name: sh

### Command

```bash
echo '#{command_to_add}' >> ~/.bash_profile
```

### Cleanup

```bash
head -n '-2' ~/.bash_profile > /tmp/T1546.004
mv /tmp/T1546.004 ~/.bash_profile
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml)
