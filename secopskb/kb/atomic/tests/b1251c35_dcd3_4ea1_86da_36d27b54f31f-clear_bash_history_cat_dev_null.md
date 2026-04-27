---
atomic_guid: "b1251c35-dcd3-4ea1-86da-36d27b54f31f"
title: "Clear Bash history (cat dev/null)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Clears bash history via cat /dev/null

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]

## Input Arguments

### history_path

- description: Bash history path
- type: path
- default: ~/.bash_history

## Executor

- name: sh

### Command

```bash
cat /dev/null > #{history_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
