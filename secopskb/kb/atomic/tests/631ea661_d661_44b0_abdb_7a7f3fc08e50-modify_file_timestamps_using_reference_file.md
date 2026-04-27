---
atomic_guid: "631ea661-d661-44b0-abdb-7a7f3fc08e50"
title: "Modify file timestamps using reference file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "631ea661-d661-44b0-abdb-7a7f3fc08e50"
  - "Modify file timestamps using reference file"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Modifies the `modify` and `access` timestamps using the timestamps of a specified reference file.

This technique was used by the threat actor Rocke during the compromise of Linux web servers.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070006-timestomp|T1070.006: Timestomp]]

## Input Arguments

### reference_file_path

- description: Path of reference file to read timestamps from
- type: path
- default: /bin/sh

### target_file_path

- description: Path of file to modify timestamps of
- type: path
- default: /tmp/T1070.006-reference.txt

## Executor

- name: sh

### Command

```bash
touch #{target_file_path}
touch -acmr #{reference_file_path} #{target_file_path}
```

### Cleanup

```bash
rm -f #{target_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
