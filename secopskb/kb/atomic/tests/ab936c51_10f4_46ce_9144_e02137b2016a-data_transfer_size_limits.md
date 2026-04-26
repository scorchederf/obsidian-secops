---
atomic_guid: "ab936c51-10f4-46ce-9144-e02137b2016a"
title: "Data Transfer Size Limits"
framework: "atomic"
generated: "true"
attack_technique_id: "T1030"
attack_technique_name: "Data Transfer Size Limits"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1030/T1030.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "ab936c51-10f4-46ce-9144-e02137b2016a"
  - "Data Transfer Size Limits"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Data Transfer Size Limits

Take a file/directory, split it into 5Mb chunks

## Metadata

- Atomic GUID: ab936c51-10f4-46ce-9144-e02137b2016a
- Technique: T1030: Data Transfer Size Limits
- Platforms: macos, linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1030/T1030.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1030-data_transfer_size_limits|T1030]]

## Input Arguments

### file_name

- description: File name
- type: path
- default: T1030_urandom

### folder_path

- description: Path where the test creates artifacts
- type: path
- default: /tmp/T1030

## Dependencies

The file must exist for the test to run.

### Prerequisite Check

```bash
if [ ! -f #{folder_path}/#{file_name} ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
if [ ! -d #{folder_path} ]; then mkdir -p #{folder_path}; touch #{folder_path}/safe_to_delete; fi; dd if=/dev/urandom of=#{folder_path}/#{file_name} bs=25000000 count=1
```

## Executor

- name: sh

### Command

```bash
cd #{folder_path}; split -b 5000000 #{file_name}
ls -l #{folder_path}
```

### Cleanup

```bash
if [ -f #{folder_path}/safe_to_delete ]; then rm -rf #{folder_path}; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1030/T1030.yaml)
