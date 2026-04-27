---
atomic_guid: "8164a4a6-f99c-4661-ac4f-80f5e4e78d2b"
title: "Set a file's creation timestamp"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "8164a4a6-f99c-4661-ac4f-80f5e4e78d2b"
  - "Set a file's creation timestamp"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Stomps on the create timestamp of a file

Setting the creation timestamp requires changing the system clock and reverting.
Sudo or root privileges are required to change date. Use with caution.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070006-timestomp|T1070.006: Timestomp]]

## Input Arguments

### target_filename

- description: Path of file that we are going to stomp on last access time
- type: path
- default: /tmp/T1070.006-creation.txt

## Executor

- elevation_required: True
- name: sh

### Command

```bash
NOW=$(date +%m%d%H%M%Y)
date 010100001971
touch #{target_filename}
date "$NOW"
stat #{target_filename}
```

### Cleanup

```bash
rm -f #{target_filename}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
