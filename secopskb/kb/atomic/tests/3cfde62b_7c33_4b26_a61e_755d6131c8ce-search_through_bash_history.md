---
atomic_guid: "3cfde62b-7c33-4b26-a61e-755d6131c8ce"
title: "Search Through Bash History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.003"
attack_technique_name: "Unsecured Credentials: Bash History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.003/T1552.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "3cfde62b-7c33-4b26-a61e-755d6131c8ce"
  - "Search Through Bash History"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Search Through Bash History

Search through bash history for specifice commands we want to capture

## Metadata

- Atomic GUID: 3cfde62b-7c33-4b26-a61e-755d6131c8ce
- Technique: T1552.003: Unsecured Credentials: Bash History
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1552.003/T1552.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.003]]

## Input Arguments

### bash_history_filename

- description: Path of the bash history file to capture
- type: path
- default: ~/.bash_history

### bash_history_grep_args

- description: grep arguments that filter out specific commands we want to capture
- type: path
- default: -e '-p ' -e 'pass' -e 'ssh'

### output_file

- description: Path where captured results will be placed
- type: path
- default: ~/loot.txt

## Executor

- name: sh

### Command

```bash
cat #{bash_history_filename} | grep #{bash_history_grep_args} > #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.003/T1552.003.yaml)
