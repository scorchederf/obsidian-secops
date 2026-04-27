---
atomic_guid: "0a898315-4cfa-4007-bafe-33a4646d115f"
title: "Add command to .bashrc"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.004"
attack_technique_name: "Event Triggered Execution: .bash_profile .bashrc and .shrc"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "0a898315-4cfa-4007-bafe-33a4646d115f"
  - "Add command to .bashrc"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Add command to .bashrc

Adds a command to the .bashrc file of the current user

## Metadata

- Atomic GUID: 0a898315-4cfa-4007-bafe-33a4646d115f
- Technique: T1546.004: Event Triggered Execution: .bash_profile .bashrc and .shrc
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1546.004/T1546.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.004]]

## Input Arguments

### command_to_add

- description: Command to add to the .bashrc file
- type: string
- default: echo "Hello from Atomic Red Team T1546.004" > /tmp/T1546.004

## Executor

- name: sh

### Command

```bash
echo '#{command_to_add}' >> ~/.bashrc
```

### Cleanup

```bash
head -n '-2' ~/.bashrc > /tmp/T1546.004
mv /tmp/T1546.004 ~/.bashrc
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml)
