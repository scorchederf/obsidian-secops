---
atomic_guid: "09210ad5-1ef2-4077-9ad3-7351e13e9222"
title: "Remove Network Share"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.005"
attack_technique_name: "Indicator Removal on Host: Network Share Connection Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml"
build_date: "2026-04-26 17:02:12"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remove Network Share

Removes a Network Share utilizing the command_prompt

## Metadata

- Atomic GUID: 09210ad5-1ef2-4077-9ad3-7351e13e9222
- Technique: T1070.005: Indicator Removal on Host: Network Share Connection Removal
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1070.005/T1070.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

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
