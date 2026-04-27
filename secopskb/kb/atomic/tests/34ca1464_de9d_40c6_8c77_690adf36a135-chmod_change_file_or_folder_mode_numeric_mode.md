---
atomic_guid: "34ca1464-de9d-40c6-8c77-690adf36a135"
title: "chmod - Change file or folder mode (numeric mode)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "34ca1464-de9d-40c6-8c77-690adf36a135"
  - "chmod - Change file or folder mode (numeric mode)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Changes a file or folder's permissions using chmod and a specified numeric mode.

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]

## Input Arguments

### file_or_folder

- description: Path of the file or folder
- type: path
- default: /tmp/AtomicRedTeam/atomics/T1222.002

### numeric_mode

- description: Specified numeric mode value
- type: integer
- default: 755

## Executor

- name: sh

### Command

```bash
chmod #{numeric_mode} #{file_or_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
