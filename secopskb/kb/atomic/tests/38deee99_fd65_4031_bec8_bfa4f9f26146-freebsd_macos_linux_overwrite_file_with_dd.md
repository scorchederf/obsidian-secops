---
atomic_guid: "38deee99-fd65-4031-bec8-bfa4f9f26146"
title: "FreeBSD/macOS/Linux - Overwrite file with DD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1485"
attack_technique_name: "Data Destruction"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "38deee99-fd65-4031-bec8-bfa4f9f26146"
  - "FreeBSD/macOS/Linux - Overwrite file with DD"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# FreeBSD/macOS/Linux - Overwrite file with DD

Overwrites and deletes a file using DD.
To stop the test, break the command with CTRL/CMD+C.

## Metadata

- Atomic GUID: 38deee99-fd65-4031-bec8-bfa4f9f26146
- Technique: T1485: Data Destruction
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1485/T1485.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Input Arguments

### file_to_overwrite

- description: Path of file to overwrite and remove
- type: path
- default: /var/log/syslog

### overwrite_source

- description: Path of data source to overwrite with
- type: path
- default: /dev/zero

## Executor

- name: sh

### Command

```sh
dd of=#{file_to_overwrite} if=#{overwrite_source} count=$(ls -l #{file_to_overwrite} | awk '{print $5}') iflag=count_bytes
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml)
