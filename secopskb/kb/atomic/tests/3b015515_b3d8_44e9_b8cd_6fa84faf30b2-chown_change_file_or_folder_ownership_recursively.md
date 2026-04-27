---
atomic_guid: "3b015515-b3d8-44e9-b8cd-6fa84faf30b2"
title: "chown - Change file or folder ownership recursively"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "3b015515-b3d8-44e9-b8cd-6fa84faf30b2"
  - "chown - Change file or folder ownership recursively"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Changes a file or folder's ownership only recursively using chown.

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]

## Input Arguments

### file_or_folder

- description: Path of the file or folder
- type: path
- default: /tmp/AtomicRedTeam/atomics/T1222.002

### owner

- description: Username of desired owner
- type: string
- default: root

## Executor

- name: bash

### Command

```bash
chown -R #{owner} #{file_or_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
