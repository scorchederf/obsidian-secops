---
atomic_guid: "ffe2346c-abd5-4b45-a713-bf5f1ebd573a"
title: "Pad Binary to Change Hash - Linux/macOS dd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.001"
attack_technique_name: "Obfuscated Files or Information: Binary Padding"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.001/T1027.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "ffe2346c-abd5-4b45-a713-bf5f1ebd573a"
  - "Pad Binary to Change Hash - Linux/macOS dd"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses dd to add a zero byte, high-quality random data, and low-quality random data to the binary to change the hash.

Upon successful execution, dd will modify `/tmp/evil-binary`, therefore the expected hash will change.

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027001-binary-padding|T1027.001: Binary Padding]]

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
dd if=/dev/zero bs=1 count=1 >> #{file_to_pad} #adds null bytes
dd if=/dev/random bs=1 count=1 >> #{file_to_pad} #adds high-quality random data
dd if=/dev/urandom bs=1 count=1 >> #{file_to_pad} #adds low-quality random data
```

### Cleanup

```bash
rm #{file_to_pad}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.001/T1027.001.yaml)
