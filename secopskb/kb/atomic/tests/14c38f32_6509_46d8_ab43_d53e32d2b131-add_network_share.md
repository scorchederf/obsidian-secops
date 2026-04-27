---
atomic_guid: "14c38f32-6509-46d8-ab43-d53e32d2b131"
title: "Add Network Share"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.005"
attack_technique_name: "Indicator Removal on Host: Network Share Connection Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "14c38f32-6509-46d8-ab43-d53e32d2b131"
  - "Add Network Share"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Add Network Share

Add a Network Share utilizing the command_prompt

## Metadata

- Atomic GUID: 14c38f32-6509-46d8-ab43-d53e32d2b131
- Technique: T1070.005: Indicator Removal on Host: Network Share Connection Removal
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1070.005/T1070.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Input Arguments

### share_name

- description: Share to add.
- type: string
- default: \\test\share

## Executor

- name: command_prompt

### Command

```cmd
net use c: #{share_name}
net share test=#{share_name} /REMARK:"test share" /CACHE:No
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml)
