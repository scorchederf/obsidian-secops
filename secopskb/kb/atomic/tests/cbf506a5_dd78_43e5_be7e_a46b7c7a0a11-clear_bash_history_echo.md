---
atomic_guid: "cbf506a5-dd78-43e5-be7e-a46b7c7a0a11"
title: "Clear Bash history (echo)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "cbf506a5-dd78-43e5-be7e-a46b7c7a0a11"
  - "Clear Bash history (echo)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear Bash history (echo)

Clears bash history via echo

## Metadata

- Atomic GUID: cbf506a5-dd78-43e5-be7e-a46b7c7a0a11
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Input Arguments

### history_path

- description: Bash history path
- type: path
- default: ~/.bash_history

## Executor

- name: sh

### Command

```bash
echo "" > #{history_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
