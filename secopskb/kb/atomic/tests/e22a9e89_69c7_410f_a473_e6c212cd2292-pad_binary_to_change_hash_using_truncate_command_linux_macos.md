---
atomic_guid: "e22a9e89-69c7-410f-a473-e6c212cd2292"
title: "Pad Binary to Change Hash using truncate command - Linux/macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.001"
attack_technique_name: "Obfuscated Files or Information: Binary Padding"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.001/T1027.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "e22a9e89-69c7-410f-a473-e6c212cd2292"
  - "Pad Binary to Change Hash using truncate command - Linux/macOS"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Pad Binary to Change Hash using truncate command - Linux/macOS

Uses truncate to add a byte to the binary to change the hash.

Upon successful execution, truncate will modify `/tmp/evil-binary`, therefore the expected hash will change.

## Metadata

- Atomic GUID: e22a9e89-69c7-410f-a473-e6c212cd2292
- Technique: T1027.001: Obfuscated Files or Information: Binary Padding
- Platforms: linux, macos
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1027.001/T1027.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.001]]

## Input Arguments

### file_to_pad

- description: Path of binary to be padded
- type: path
- default: /tmp/evil-binary

## Dependencies

The binary must exist on disk at specified location (#{file_to_pad})

### Prerequisite Check

```bash
if [ -f #{file_to_pad} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
cp /bin/ls #{file_to_pad}
```

## Executor

- name: sh

### Command

```bash
truncate -s +1 #{file_to_pad} #adds a byte to the file size
```

### Cleanup

```bash
rm #{file_to_pad}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.001/T1027.001.yaml)
