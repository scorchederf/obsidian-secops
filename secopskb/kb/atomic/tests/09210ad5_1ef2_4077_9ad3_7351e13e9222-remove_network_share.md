---
atomic_guid: "09210ad5-1ef2-4077-9ad3-7351e13e9222"
title: "Remove Network Share"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.005"
attack_technique_name: "Indicator Removal on Host: Network Share Connection Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "09210ad5-1ef2-4077-9ad3-7351e13e9222"
  - "Remove Network Share"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Removes a Network Share utilizing the command_prompt

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070005-network-share-connection-removal|T1070.005: Network Share Connection Removal]]

## Input Arguments

### share_name

- description: Share to remove.
- type: string
- default: \\test\share

## Executor

- name: command_prompt

### Command

```cmd
net share #{share_name} /delete
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml)
