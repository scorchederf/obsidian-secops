---
atomic_guid: "60eee3ea-2ebd-453b-a666-c52ce08d2709"
title: "chflags - Remove immutable file attribute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "60eee3ea-2ebd-453b-a666-c52ce08d2709"
  - "chflags - Remove immutable file attribute"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# chflags - Remove immutable file attribute

Remove's a file's `immutable` attribute using `chflags`.
This technique was used by the threat actor Rocke during the compromise of Linux web servers.

## Metadata

- Atomic GUID: 60eee3ea-2ebd-453b-a666-c52ce08d2709
- Technique: T1222.002: File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1222.002/T1222.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Input Arguments

### file_to_modify

- description: Path of the file
- type: path
- default: /tmp/T1222.002.txt

## Executor

- name: sh

### Command

```bash
touch #{file_to_modify}
chflags simmutable #{file_to_modify}
chflags nosimmutable #{file_to_modify}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
