---
atomic_guid: "13daa2cf-195a-43df-a8bd-7dd5ffb607b5"
title: "Network Share Discovery via dir command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "13daa2cf-195a-43df-a8bd-7dd5ffb607b5"
  - "Network Share Discovery via dir command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Network Share Discovery utilizing the dir command prompt. The computer ip variable may need to be modified to point to a different host ip
Upon execution available network shares will be displayed in the commandline session

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135: Network Share Discovery]]

## Input Arguments

### computer_ip

- description: Computer IP to find a mount on.
- type: string
- default: 127.0.0.1

## Executor

- name: command_prompt

### Command

```cmd
dir \\#{computer_ip}\c$
dir \\#{computer_ip}\admin$
dir \\#{computer_ip}\IPC$
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
