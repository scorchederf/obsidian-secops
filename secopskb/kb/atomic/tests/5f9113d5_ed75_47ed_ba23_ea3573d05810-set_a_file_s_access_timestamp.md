---
atomic_guid: "5f9113d5-ed75-47ed-ba23-ea3573d05810"
title: "Set a file's access timestamp"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "5f9113d5-ed75-47ed-ba23-ea3573d05810"
  - "Set a file's access timestamp"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Set a file's access timestamp

Stomps on the access timestamp of a file

## Metadata

- Atomic GUID: 5f9113d5-ed75-47ed-ba23-ea3573d05810
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
- default: /tmp/T1070.006-access.txt

## Dependencies

The file must exist in order to be timestomped

### Prerequisite Check

```untitled
test -e #{target_filename} && exit 0 || exit 1
```

### Get Prerequisite

```untitled
echo 'T1070.006 file access timestomp test' > #{target_filename}
```

## Executor

- name: sh

### Command

```bash
touch -a -t 197001010000.00 #{target_filename}
```

### Cleanup

```bash
rm -f #{target_filename}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
