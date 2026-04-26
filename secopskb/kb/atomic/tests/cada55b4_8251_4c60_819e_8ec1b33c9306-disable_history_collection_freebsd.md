---
atomic_guid: "cada55b4-8251-4c60-819e-8ec1b33c9306"
title: "Disable history collection (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "cada55b4-8251-4c60-819e-8ec1b33c9306"
  - "Disable history collection (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable history collection (freebsd)

Disables history collection in shells

## Metadata

- Atomic GUID: cada55b4-8251-4c60-819e-8ec1b33c9306
- Technique: T1562.003: Impair Defenses: Impair Command History Logging
- Platforms: linux
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
export HISTSIZE=0
#{evil_command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
