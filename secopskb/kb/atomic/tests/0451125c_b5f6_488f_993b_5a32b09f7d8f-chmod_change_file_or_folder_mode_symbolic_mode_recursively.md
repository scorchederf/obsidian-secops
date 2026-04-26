---
atomic_guid: "0451125c-b5f6-488f-993b-5a32b09f7d8f"
title: "chmod - Change file or folder mode (symbolic mode) recursively"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "0451125c-b5f6-488f-993b-5a32b09f7d8f"
  - "chmod - Change file or folder mode (symbolic mode) recursively"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# chmod - Change file or folder mode (symbolic mode) recursively

Changes a file or folder's permissions recursively using chmod and a specified symbolic mode.

## Metadata

- Atomic GUID: 0451125c-b5f6-488f-993b-5a32b09f7d8f
- Technique: T1222.002: File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification
- Platforms: linux, macos
- Executor: bash
- Source Path: atomics/T1222.002/T1222.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Input Arguments

### file_or_folder

- description: Path of the file or folder
- type: path
- default: /tmp/AtomicRedTeam/atomics/T1222.002

### symbolic_mode

- description: Specified symbolic mode value
- type: string
- default: a+w

## Executor

- name: bash

### Command

```bash
chmod -R #{symbolic_mode} #{file_or_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
