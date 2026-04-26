---
atomic_guid: "20ef1523-8758-4898-b5a2-d026cc3d2c52"
title: "Set a file's modification timestamp"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "20ef1523-8758-4898-b5a2-d026cc3d2c52"
  - "Set a file's modification timestamp"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Set a file's modification timestamp

Stomps on the modification timestamp of a file

## Metadata

- Atomic GUID: 20ef1523-8758-4898-b5a2-d026cc3d2c52
- Technique: T1070.006: Indicator Removal on Host: Timestomp
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1070.006/T1070.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Input Arguments

### target_filename

- description: Path of file that we are going to stomp on last access time
- type: path
- default: /tmp/T1070.006-modification.txt

## Dependencies

The file must exist in order to be timestomped

### Prerequisite Check

```text
test -e #{target_filename} && exit 0 || exit 1
```

### Get Prerequisite

```text
echo 'T1070.006 file modification timestomp test' > #{target_filename}
```

## Executor

- name: sh

### Command

```sh
touch -m -t 197001010000.00 #{target_filename}
```

### Cleanup

```sh
rm -f #{target_filename}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
