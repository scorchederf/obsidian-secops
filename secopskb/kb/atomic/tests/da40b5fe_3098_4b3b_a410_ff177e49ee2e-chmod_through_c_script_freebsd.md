---
atomic_guid: "da40b5fe-3098-4b3b-a410-ff177e49ee2e"
title: "Chmod through c script (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "da40b5fe-3098-4b3b-a410-ff177e49ee2e"
  - "Chmod through c script (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Chmod through c script (freebsd)

chmods a file using a c script

## Metadata

- Atomic GUID: da40b5fe-3098-4b3b-a410-ff177e49ee2e
- Technique: T1222.002: File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1222.002/T1222.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Input Arguments

### compiled_file

- description: Path of compiled file
- type: path
- default: /tmp/T1222002

### source_file

- description: Path of c source file
- type: path
- default: PathToAtomicsFolder/T1222.002/src/T1222.002.c

## Dependencies

Compile the script from (#{source_file}). Destination is #{compiled_file}

### Prerequisite Check

```text
cc #{source_file} -o #{compiled_file}
```

### Get Prerequisite

```text
cc #{source_file} -o #{compiled_file}
```

## Executor

- name: sh

### Command

```sh
#{compiled_file} /tmp/ T1222002
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
