---
atomic_guid: "562d737f-2fc6-4b09-8c2a-7f8ff0828480"
title: "Delete a single file - FreeBSD/Linux/macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "562d737f-2fc6-4b09-8c2a-7f8ff0828480"
  - "Delete a single file - FreeBSD/Linux/macOS"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete a single file - FreeBSD/Linux/macOS

Delete a single file from the temporary directory

## Metadata

- Atomic GUID: 562d737f-2fc6-4b09-8c2a-7f8ff0828480
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: linux, macos
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### file_to_delete

- description: Path of file to delete
- type: path
- default: /tmp/victim-files/T1070.004-test.txt

### parent_folder

- description: Path of parent folder
- type: path
- default: /tmp/victim-files/

## Dependencies

The file must exist in order to be deleted

### Prerequisite Check

```bash
test -e #{file_to_delete} && exit 0 || exit 1
```

### Get Prerequisite

```bash
mkdir -p #{parent_folder} && touch #{file_to_delete}
```

## Executor

- name: sh

### Command

```bash
rm -f #{file_to_delete}
```

### Cleanup

```bash
rm -rf #{parent_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
