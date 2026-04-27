---
atomic_guid: "039b4b10-2900-404b-b67f-4b6d49aa6499"
title: "Overwrite and delete a file with shred"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "039b4b10-2900-404b-b67f-4b6d49aa6499"
  - "Overwrite and delete a file with shred"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use the `shred` command to overwrite the temporary file and then delete it

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]

## Input Arguments

### file_to_shred

- description: Path of file to shred
- type: path
- default: /tmp/victim-shred.txt

## Dependencies

Check if file already exists

### Prerequisite Check

```untitled
if [ -f "#{file_to_shred}" ]; then echo "File already exists"; else echo "File does NOT exist yet"; exit 1; fi
```

### Get Prerequisite

```untitled
touch #{file_to_shred}
```

## Executor

- name: sh

### Command

```bash
shred -u #{file_to_shred}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
