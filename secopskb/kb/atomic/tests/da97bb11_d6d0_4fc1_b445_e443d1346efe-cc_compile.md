---
atomic_guid: "da97bb11-d6d0-4fc1-b445-e443d1346efe"
title: "CC compile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.004"
attack_technique_name: "Obfuscated Files or Information: Compile After Delivery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "da97bb11-d6d0-4fc1-b445-e443d1346efe"
  - "CC compile"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CC compile

Compile a c file with either gcc or clang on FreeBSD, Linux or Macos.

## Metadata

- Atomic GUID: da97bb11-d6d0-4fc1-b445-e443d1346efe
- Technique: T1027.004: Obfuscated Files or Information: Compile After Delivery
- Platforms: linux, macos
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1027.004/T1027.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Input Arguments

### input_file

- description: source file
- type: path
- default: PathToAtomicsFolder/T1027.004/src/T1027-004-test.cc

## Dependencies

the source file must exist on disk at specified location (#{input_file})

### Prerequisite Check

```bash
if [ -e  #{input_file} ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
wget https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027.004/src/T1027-004-test.cc -O #{input_file}
```

## Executor

- name: sh

### Command

```bash
g++ #{input_file} && ./a.out
clang++ #{input_file} && ./a.out
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml)
