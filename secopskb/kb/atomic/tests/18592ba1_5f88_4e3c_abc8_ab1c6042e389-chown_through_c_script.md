---
atomic_guid: "18592ba1-5f88-4e3c-abc8-ab1c6042e389"
title: "Chown through c script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "18592ba1-5f88-4e3c-abc8-ab1c6042e389"
  - "Chown through c script"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Chown through c script

chowns a file to root using a c script

## Metadata

- Atomic GUID: 18592ba1-5f88-4e3c-abc8-ab1c6042e389
- Technique: T1222.002: File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification
- Platforms: macos, linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1222.002/T1222.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Input Arguments

### compiled_file

- description: Path of compiled file
- type: path
- default: /tmp/T1222002own

### source_file

- description: Path of c source file
- type: path
- default: PathToAtomicsFolder/T1222.002/src/chown.c

## Dependencies

Compile the script from (#{source_file}). Destination is #{compiled_file}

### Prerequisite Check

```text
gcc #{source_file} -o #{compiled_file}
```

### Get Prerequisite

```text
gcc #{source_file} -o #{compiled_file}
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo #{compiled_file} #{source_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
