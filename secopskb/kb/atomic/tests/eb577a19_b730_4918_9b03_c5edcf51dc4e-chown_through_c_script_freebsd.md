---
atomic_guid: "eb577a19-b730-4918-9b03-c5edcf51dc4e"
title: "Chown through c script (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "eb577a19-b730-4918-9b03-c5edcf51dc4e"
  - "Chown through c script (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

chowns a file to root using a c script

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]

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

```bash
cc #{source_file} -o #{compiled_file}
```

### Get Prerequisite

```bash
cc #{source_file} -o #{compiled_file}
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
#{compiled_file} #{source_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
