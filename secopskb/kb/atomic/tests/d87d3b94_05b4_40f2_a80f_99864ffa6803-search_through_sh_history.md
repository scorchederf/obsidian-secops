---
atomic_guid: "d87d3b94-05b4-40f2-a80f-99864ffa6803"
title: "Search Through sh History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.003"
attack_technique_name: "Unsecured Credentials: Bash History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.003/T1552.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "d87d3b94-05b4-40f2-a80f-99864ffa6803"
  - "Search Through sh History"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Search through sh history for specifice commands we want to capture

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552003-shell-history|T1552.003: Shell History]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: ~/loot.txt

### sh_history_filename

- description: Path of the sh history file to capture
- type: path
- default: ~/.history

### sh_history_grep_args

- description: grep arguments that filter out specific commands we want to capture
- type: path
- default: -e '-p ' -e 'pass' -e 'ssh'

## Executor

- name: sh

### Command

```bash
cat #{sh_history_filename} | grep #{sh_history_grep_args} > #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.003/T1552.003.yaml)
