---
atomic_guid: "cddb9098-3b47-4e01-9d3b-6f5f323288a9"
title: "Mac Hidden file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "cddb9098-3b47-4e01-9d3b-6f5f323288a9"
  - "Mac Hidden file"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mac Hidden file

Hide a file on MacOS

## Metadata

- Atomic GUID: cddb9098-3b47-4e01-9d3b-6f5f323288a9
- Technique: T1564.001: Hide Artifacts: Hidden Files and Directories
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1564.001/T1564.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Executor

- name: sh

### Command

```bash
xattr -lr * / 2>&1 /dev/null | grep -C 2 "00 00 00 00 00 00 00 00 40 00 FF FF FF FF 00 00"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
