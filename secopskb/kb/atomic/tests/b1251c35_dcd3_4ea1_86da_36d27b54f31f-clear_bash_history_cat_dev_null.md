---
atomic_guid: "b1251c35-dcd3-4ea1-86da-36d27b54f31f"
title: "Clear Bash history (cat dev/null)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "b1251c35-dcd3-4ea1-86da-36d27b54f31f"
  - "Clear Bash history (cat dev/null)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear Bash history (cat dev/null)

Clears bash history via cat /dev/null

## Metadata

- Atomic GUID: b1251c35-dcd3-4ea1-86da-36d27b54f31f
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux, macos
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

```sh
cat /dev/null > #{history_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
