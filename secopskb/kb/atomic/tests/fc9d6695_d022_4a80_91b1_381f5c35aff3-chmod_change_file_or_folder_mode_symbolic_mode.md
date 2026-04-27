---
atomic_guid: "fc9d6695-d022-4a80-91b1-381f5c35aff3"
title: "chmod - Change file or folder mode (symbolic mode)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "fc9d6695-d022-4a80-91b1-381f5c35aff3"
  - "chmod - Change file or folder mode (symbolic mode)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# chmod - Change file or folder mode (symbolic mode)

Changes a file or folder's permissions using chmod and a specified symbolic mode.

## Metadata

- Atomic GUID: fc9d6695-d022-4a80-91b1-381f5c35aff3
- Technique: T1222.002: File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification
- Platforms: linux, macos
- Executor: sh
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

- name: sh

### Command

```bash
chmod #{symbolic_mode} #{file_or_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
