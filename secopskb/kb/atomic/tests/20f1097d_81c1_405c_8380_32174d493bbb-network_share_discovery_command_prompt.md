---
atomic_guid: "20f1097d-81c1-405c-8380-32174d493bbb"
title: "Network Share Discovery command prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "20f1097d-81c1-405c-8380-32174d493bbb"
  - "Network Share Discovery command prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Network Share Discovery utilizing the command prompt. The computer name variable may need to be modified to point to a different host
Upon execution available network shares will be displayed in the powershell session

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135: Network Share Discovery]]

## Input Arguments

### computer_name

- description: Computer name to find a mount on.
- type: string
- default: localhost

## Executor

- name: command_prompt

### Command

```cmd
net view \\#{computer_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
