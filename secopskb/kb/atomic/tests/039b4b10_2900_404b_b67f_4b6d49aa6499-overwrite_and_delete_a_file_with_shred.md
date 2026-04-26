---
atomic_guid: "039b4b10-2900-404b-b67f-4b6d49aa6499"
title: "Overwrite and delete a file with shred"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 14:38:39"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Overwrite and delete a file with shred

Use the `shred` command to overwrite the temporary file and then delete it

## Metadata

- Atomic GUID: 039b4b10-2900-404b-b67f-4b6d49aa6499
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### file_to_shred

- description: Path of file to shred
- type: path
- default: /tmp/victim-shred.txt

## Dependencies

Check if file already exists

### Prerequisite Check

```text
if [ -f "#{file_to_shred}" ]; then echo "File already exists"; else echo "File does NOT exist yet"; exit 1; fi
```

### Get Prerequisite

```text
touch #{file_to_shred}
```

## Executor

- name: sh

### Command

```sh
shred -u #{file_to_shred}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
