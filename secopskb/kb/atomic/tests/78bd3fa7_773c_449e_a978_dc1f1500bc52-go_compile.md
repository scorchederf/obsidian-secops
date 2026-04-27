---
atomic_guid: "78bd3fa7-773c-449e-a978-dc1f1500bc52"
title: "Go compile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.004"
attack_technique_name: "Obfuscated Files or Information: Compile After Delivery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "78bd3fa7-773c-449e-a978-dc1f1500bc52"
  - "Go compile"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Compile a go file with golang on FreeBSD, Linux or Macos.

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027004-compile-after-delivery|T1027.004: Compile After Delivery]]

## Input Arguments

### input_file

- description: source file
- type: path
- default: PathToAtomicsFolder/T1027.004/src/T1027-004-test.go

## Dependencies

the source file must exist on disk at specified location (#{input_file})

### Prerequisite Check

```bash
if [ -e  #{input_file} ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
wget https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027.004/src/T1027-004-test.go -O #{input_file}
```

## Executor

- name: sh

### Command

```bash
go run #{input_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml)
