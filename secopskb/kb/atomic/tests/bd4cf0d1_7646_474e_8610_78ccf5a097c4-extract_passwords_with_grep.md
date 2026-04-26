---
atomic_guid: "bd4cf0d1-7646-474e-8610-78ccf5a097c4"
title: "Extract passwords with grep"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "bd4cf0d1-7646-474e-8610-78ccf5a097c4"
  - "Extract passwords with grep"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Extract passwords with grep

Extracting credentials from files

## Metadata

- Atomic GUID: bd4cf0d1-7646-474e-8610-78ccf5a097c4
- Technique: T1552.001: Unsecured Credentials: Credentials In Files
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1552.001/T1552.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Input Arguments

### file_path

- description: Path to search
- type: string
- default: /

## Executor

- name: sh

### Command

```sh
grep -ri password #{file_path}
exit 0
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
