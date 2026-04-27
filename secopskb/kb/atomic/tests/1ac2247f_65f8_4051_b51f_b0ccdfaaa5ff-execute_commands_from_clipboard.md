---
atomic_guid: "1ac2247f-65f8-4051-b51f-b0ccdfaaa5ff"
title: "Execute commands from clipboard"
framework: "atomic"
generated: "true"
attack_technique_id: "T1115"
attack_technique_name: "Clipboard Data"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "1ac2247f-65f8-4051-b51f-b0ccdfaaa5ff"
  - "Execute commands from clipboard"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Execute commands from clipboard

Echo a command to clipboard and execute it

## Metadata

- Atomic GUID: 1ac2247f-65f8-4051-b51f-b0ccdfaaa5ff
- Technique: T1115: Clipboard Data
- Platforms: macos
- Executor: bash
- Source Path: atomics/T1115/T1115.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1115-clipboard_data|T1115]]

## Executor

- name: bash

### Command

```bash
echo ifconfig | pbcopy
$(pbpaste)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml)
