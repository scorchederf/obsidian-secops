---
atomic_guid: "4eafdb45-0f79-4d66-aa86-a3e2c08791f5"
title: "Disable history collection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "4eafdb45-0f79-4d66-aa86-a3e2c08791f5"
  - "Disable history collection"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable history collection

Disables history collection in shells

## Metadata

- Atomic GUID: 4eafdb45-0f79-4d66-aa86-a3e2c08791f5
- Technique: T1562.003: Impair Defenses: Impair Command History Logging
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1562.003/T1562.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.003]]

## Input Arguments

### evil_command

- description: Command to run after shell history collection is disabled
- type: string
- default: whoami

## Executor

- name: sh

### Command

```bash
export HISTCONTROL=ignoreboth
#{evil_command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
