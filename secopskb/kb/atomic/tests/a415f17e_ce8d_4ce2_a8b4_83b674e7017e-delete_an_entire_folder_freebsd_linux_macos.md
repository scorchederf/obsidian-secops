---
atomic_guid: "a415f17e-ce8d-4ce2-a8b4-83b674e7017e"
title: "Delete an entire folder - FreeBSD/Linux/macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "a415f17e-ce8d-4ce2-a8b4-83b674e7017e"
  - "Delete an entire folder - FreeBSD/Linux/macOS"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete an entire folder - FreeBSD/Linux/macOS

Recursively delete the temporary directory and all files contained within it

## Metadata

- Atomic GUID: a415f17e-ce8d-4ce2-a8b4-83b674e7017e
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: linux, macos
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### folder_to_delete

- description: Path of folder to delete
- type: path
- default: /tmp/victim-folder

## Dependencies

The folder must exist in order to be deleted

### Prerequisite Check

```text
test -e #{folder_to_delete} && exit 0 || exit 1
```

### Get Prerequisite

```text
mkdir -p #{folder_to_delete}
```

## Executor

- name: sh

### Command

```sh
rm -rf #{folder_to_delete}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
